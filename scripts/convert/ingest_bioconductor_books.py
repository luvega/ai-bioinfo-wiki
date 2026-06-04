"""Ingest Bioconductor OSTA/OSCA books as course materials.

The script keeps large source artifacts under materials/raw and writes searchable
Markdown/index files under materials/markdown. Project paths are derived from
this file location; no absolute workspace root is embedded.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import http.client
import json
import os
import re
import shutil
import tarfile
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup
from markdownify import markdownify as html_to_markdown


ROOT = Path(__file__).resolve().parents[2]
RAW_ROOT = ROOT / "materials" / "raw" / "bioconductor_books"
MARKDOWN_ROOT = ROOT / "materials" / "markdown" / "bioconductor_books"
ARCHIVES_DIR = RAW_ROOT / "archives"
EXTRACTED_DIR = RAW_ROOT / "extracted"
ASSETS_DIR = RAW_ROOT / "assets"
GITHUB_DIR = RAW_ROOT / "github" / "OSCA-source"

BIOC_VERSION = "3.23"
PACKAGE_BASE_URL = f"https://bioconductor.org/packages/{BIOC_VERSION}/books/src/contrib/"
PACKAGES_URL = urllib.parse.urljoin(PACKAGE_BASE_URL, "PACKAGES")
OSTA_RELEASE_URL = "https://bioconductor.org/books/release/OSTA/"
OSCA_RELEASE_URL = "https://bioconductor.org/books/release/OSCA/"

OSCA_REPOS = [
    "OSCA",
    "OSCA.intro",
    "OSCA.basic",
    "OSCA.advanced",
    "OSCA.multisample",
    "OSCA.workflows",
    "OSCA.trajectory",
]

BOOK_PACKAGES = [
    "OSTA",
    "OSCA",
    "OSCA.intro",
    "OSCA.basic",
    "OSCA.advanced",
    "OSCA.multisample",
    "OSCA.workflows",
]

SOURCE_RELEASE_URLS = {
    "OSTA": OSTA_RELEASE_URL,
    "OSCA": OSCA_RELEASE_URL,
}

WORKFLOW_KEYWORDS = (
    "workflow",
    "case",
    "visium",
    "spatial",
    "quality",
    "control",
    "normalization",
    "clustering",
    "dimensional",
    "differential",
    "trajectory",
    "integration",
)


@dataclass
class PackageRecord:
    package: str
    version: str
    license: str
    md5: str
    tarball_url: str
    source: str = "bioconductor-packages"


@dataclass
class ImageRecord:
    source: str
    page_slug: str
    alt: str
    src: str
    original_url: str
    local_asset_path: str


@dataclass
class CodeChunk:
    source: str
    page_slug: str
    chunk_id: str
    language: str
    code: str
    local_path: str
    page_url: str


@dataclass
class PageContent:
    source: str
    title: str
    slug: str
    url: str
    markdown: str
    images: list[ImageRecord]
    code_chunks: list[CodeChunk]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def ensure_dirs() -> None:
    for path in (ARCHIVES_DIR, EXTRACTED_DIR, ASSETS_DIR, GITHUB_DIR, MARKDOWN_ROOT):
        path.mkdir(parents=True, exist_ok=True)


def request_url(url: str, *, method: str = "GET", headers: dict[str, str] | None = None) -> urllib.request.Request:
    final_headers = {
        "User-Agent": "AI_Course Bioconductor book ingest/1.0",
    }
    if headers:
        final_headers.update(headers)
    return urllib.request.Request(url, headers=final_headers, method=method)


def fetch_text(url: str, timeout: int = 60, attempts: int = 3) -> str:
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request_url(url), timeout=timeout) as response:
                charset = response.headers.get_content_charset() or "utf-8"
                return response.read().decode(charset, errors="replace")
        except urllib.error.HTTPError:
            raise
        except (TimeoutError, urllib.error.URLError, http.client.IncompleteRead) as exc:
            last_error = exc
            if attempt < attempts:
                time.sleep(2 * attempt)
                continue
            raise
    if last_error:
        raise last_error
    raise RuntimeError(f"Unable to fetch {url}")


def fetch_head(url: str, timeout: int = 60) -> dict[str, str]:
    try:
        with urllib.request.urlopen(request_url(url, method="HEAD"), timeout=timeout) as response:
            return {key.lower(): value for key, value in response.headers.items()}
    except urllib.error.HTTPError:
        raise
    except Exception:
        return {}


def parse_packages(text: str, base_url: str) -> dict[str, PackageRecord]:
    records: dict[str, PackageRecord] = {}
    current: dict[str, str] = {}
    last_key: str | None = None

    def flush() -> None:
        if not current.get("Package") or not current.get("Version"):
            return
        package = current["Package"].strip()
        version = current["Version"].strip()
        tarball = urllib.parse.urljoin(base_url, f"{package}_{version}.tar.gz")
        records[package] = PackageRecord(
            package=package,
            version=version,
            license=current.get("License", "").strip(),
            md5=current.get("MD5sum", "").strip(),
            tarball_url=tarball,
        )

    for raw_line in text.splitlines():
        line = raw_line.rstrip("\n")
        if not line.strip():
            flush()
            current = {}
            last_key = None
            continue
        if line.startswith((" ", "\t")) and last_key:
            current[last_key] += " " + line.strip()
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        current[key] = value.strip()
        last_key = key

    flush()
    return records


def slugify(value: str) -> str:
    value = urllib.parse.unquote(value)
    value = re.sub(r"\.html?$", "", value)
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip().lower())
    value = re.sub(r"-+", "-", value).strip("-._")
    return value or "index"


def page_slug_from_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    parts = [part for part in parsed.path.strip("/").split("/") if part]
    if not parts:
        return "index"
    name = parts[-1]
    parent = parts[-2] if len(parts) > 1 else ""
    if not name:
        return slugify(parent)
    if name.lower() in {"index.html", "index.htm"}:
        return slugify(parent)
    if parent.startswith(("OSCA", "OSCA.")):
        return f"{slugify(parent)}-{slugify(name)}"
    return slugify(name)


def infer_code_language(code_node) -> str:
    classes: list[str] = []
    for node in (code_node, code_node.parent):
        if not node:
            continue
        classes.extend(node.get("class", []))
    class_text = " ".join(classes).lower()
    if "python" in class_text or "py" in class_text.split():
        return "python"
    if "language-r" in class_text or "sourcecode r" in class_text or re.search(r"\br\b", class_text):
        return "r"

    code = code_node.get_text("\n")
    if re.search(r"^\s*(import|from)\s+\w+", code, flags=re.MULTILINE):
        return "python"
    if re.search(r"(<-|library\(|set\.seed\(|BiocManager::|::)", code):
        return "r"
    return "text"


def make_image_record(source: str, page_slug: str, page_url: str, img_node) -> ImageRecord:
    src = img_node.get("src", "").strip()
    original_url = urllib.parse.urljoin(page_url, src)
    parsed_path = urllib.parse.urlparse(original_url).path
    filename = Path(parsed_path).name or f"{slugify(src)}.png"
    asset_rel = Path("materials") / "raw" / "bioconductor_books" / "assets" / source / page_slug / filename
    return ImageRecord(
        source=source,
        page_slug=page_slug,
        alt=img_node.get("alt", "").strip(),
        src=src,
        original_url=original_url,
        local_asset_path=asset_rel.as_posix(),
    )


def extract_page_content(html: str, page_url: str, source_slug: str) -> PageContent:
    soup = BeautifulSoup(html, "lxml")
    main = soup.select_one("main#quarto-document-content") or soup.select_one("main") or soup.body or soup
    for selector in ("script", "style", "nav", ".sidebar", ".margin-sidebar", ".toc-actions", ".chapter-nav"):
        for node in main.select(selector):
            node.decompose()
    for anchor in main.find_all("a", href=True):
        href = anchor["href"].strip()
        if not href or href.startswith(("http://", "https://", "mailto:", "tel:", "javascript:")):
            continue
        anchor["href"] = urllib.parse.urljoin(page_url, href)

    title_node = main.find(["h1", "h2"]) or soup.find("title")
    title = title_node.get_text(" ", strip=True) if title_node else page_slug_from_url(page_url)
    slug = page_slug_from_url(page_url)

    images = [make_image_record(source_slug, slug, page_url, img) for img in main.find_all("img") if img.get("src")]

    code_chunks: list[CodeChunk] = []
    for idx, code_node in enumerate(main.select("pre code"), start=1):
        code = code_node.get_text("\n").strip("\n")
        if not code:
            continue
        language = infer_code_language(code_node)
        ext = {"r": "R", "python": "py"}.get(language, "txt")
        chunk_id = f"{slug}-chunk-{idx:03d}"
        local_path = (
            Path("materials")
            / "markdown"
            / "bioconductor_books"
            / source_slug
            / "code"
            / slug
            / f"{chunk_id}.{ext}"
        )
        code_chunks.append(
            CodeChunk(
                source=source_slug,
                page_slug=slug,
                chunk_id=chunk_id,
                language=language,
                code=code,
                local_path=local_path.as_posix(),
                page_url=page_url,
            )
        )

    markdown = html_to_markdown(str(main), heading_style="ATX").strip() + "\n"
    return PageContent(
        source=source_slug,
        title=title,
        slug=slug,
        url=page_url,
        markdown=markdown,
        images=images,
        code_chunks=code_chunks,
    )


def rewrite_images_to_local_assets(markdown: str, images: Iterable[ImageRecord], markdown_dir: Path | None = None) -> str:
    rewritten = markdown
    for image in images:
        replacement = image.local_asset_path
        if markdown_dir is not None:
            replacement = os.path.relpath(ROOT / image.local_asset_path, markdown_dir).replace("\\", "/")
        candidates = {
            image.src,
            image.original_url,
            urllib.parse.quote(image.src),
            urllib.parse.quote(image.original_url, safe="/:"),
        }
        for candidate in candidates:
            rewritten = rewritten.replace(f"]({candidate})", f"]({replacement})")
            rewritten = rewritten.replace(f"](<{candidate}>)", f"]({replacement})")
    return rewritten


def map_workflow_weeks(text: str) -> list[int]:
    lowered = text.lower()
    weeks: set[int] = set()
    if any(term in lowered for term in ("read", "count", "quality", "control", "normalization", "matrix")):
        weeks.add(14)
    if any(term in lowered for term in ("differential", "marker", "de ", "testing", "feature")):
        weeks.add(15)
    if any(term in lowered for term in ("single-cell", "single cell", "scrna", "spatial", "visium", "clustering", "dimensional", "umap", "tsne")):
        weeks.add(16)
    if any(term in lowered for term in ("workflow", "case", "trajectory", "integration", "multi-sample", "multisample", "spatial")):
        weeks.add(17)
    if not weeks and any(term in lowered for term in WORKFLOW_KEYWORDS):
        weeks.update({16, 17})
    return sorted(weeks)


def load_manifest() -> dict:
    manifest_path = MARKDOWN_ROOT / "source_manifest.json"
    if not manifest_path.exists():
        return {}
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def write_manifest(manifest: dict) -> None:
    ensure_dirs()
    manifest_path = MARKDOWN_ROOT / "source_manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def discover_release_links(url: str) -> list[str]:
    try:
        html = fetch_text(url)
    except Exception:
        return [url]
    soup = BeautifulSoup(html, "lxml")
    links = {url}
    parsed_root = urllib.parse.urlparse(url)
    root_prefix = f"{parsed_root.scheme}://{parsed_root.netloc}{parsed_root.path}"
    if not root_prefix.endswith("/"):
        root_prefix += "/"
    for anchor in soup.find_all("a", href=True):
        href = anchor["href"].strip()
        absolute = urllib.parse.urljoin(url, href)
        if absolute.startswith("http://bioconductor.org/"):
            absolute = "https://" + absolute[len("http://") :]
        parsed = urllib.parse.urlparse(absolute)
        if parsed.fragment:
            absolute = urllib.parse.urlunparse(parsed._replace(fragment=""))
            parsed = urllib.parse.urlparse(absolute)
        is_book_root = f"/books/{BIOC_VERSION}/OSCA" in absolute or f"/books/{BIOC_VERSION}/OSTA" in absolute
        if not (absolute.endswith((".html", "/")) or is_book_root):
            continue
        if is_book_root and not absolute.endswith((".html", "/")):
            absolute += "/"
        if absolute.startswith(root_prefix) or f"/books/{BIOC_VERSION}/" in absolute:
            links.add(absolute)
    return sorted(links)


def github_repo_metadata(repo: str) -> dict:
    url = f"https://api.github.com/repos/OSCA-source/{repo}"
    metadata = {
        "name": repo,
        "url": f"https://github.com/OSCA-source/{repo}",
        "api_url": url,
        "available": False,
        "default_branch": None,
        "branches": [],
        "note": None,
    }
    try:
        repo_json = json.loads(fetch_text(url, timeout=30))
        metadata["available"] = True
        metadata["default_branch"] = repo_json.get("default_branch")
        branches = json.loads(fetch_text(f"{url}/branches?per_page=100", timeout=30))
        metadata["branches"] = [
            {
                "name": branch.get("name"),
                "sha": branch.get("commit", {}).get("sha"),
            }
            for branch in branches
            if branch.get("name")
        ]
    except Exception as exc:
        metadata["note"] = f"GitHub metadata fetch failed: {exc}"
    return metadata


def discover_manifest() -> dict:
    packages_text = fetch_text(PACKAGES_URL)
    package_records = parse_packages(packages_text, PACKAGE_BASE_URL)
    selected_packages: dict[str, dict] = {}
    for package in BOOK_PACKAGES:
        if package in package_records:
            if package.startswith("OSCA") and not package_records[package].license:
                package_records[package].license = "CC BY 4.0"
            selected_packages[package] = asdict(package_records[package])
        elif package == "OSCA.advanced":
            selected_packages[package] = {
                "package": package,
                "version": "release-link-missing",
                "license": "CC BY 4.0",
                "md5": "",
                "tarball_url": urllib.parse.urljoin(PACKAGE_BASE_URL, "OSCA.advanced_1.20.0.tar.gz"),
                "source": "github-fallback",
                "note": "Bioconductor release tarball currently unavailable; use OSCA-source/OSCA.advanced.",
            }

    osca_links = set(discover_release_links(OSCA_RELEASE_URL))
    for package in ("OSCA.intro", "OSCA.basic", "OSCA.advanced", "OSCA.multisample", "OSCA.workflows"):
        osca_links.add(f"https://bioconductor.org/books/{BIOC_VERSION}/{package}/")
    release_links = {
        "OSTA": discover_release_links(OSTA_RELEASE_URL),
        "OSCA": sorted(osca_links),
    }
    repositories = [github_repo_metadata(repo) for repo in OSCA_REPOS]
    for repo in repositories:
        if repo["name"] == "OSCA.advanced":
            repo["use_as_release_fallback"] = True

    manifest = {
        "generated_at": utc_now(),
        "bioconductor_version": BIOC_VERSION,
        "package_index_url": PACKAGES_URL,
        "raw_root": str(RAW_ROOT.relative_to(ROOT)).replace("\\", "/"),
        "markdown_root": str(MARKDOWN_ROOT.relative_to(ROOT)).replace("\\", "/"),
        "packages": selected_packages,
        "sources": {
            "OSTA": {
                "release_url": OSTA_RELEASE_URL,
                "package": "OSTA",
                "license": "CC BY 4.0",
                "course_use": "Week 16-17 spatial transcriptomics case extension",
                "release_links": release_links["OSTA"],
            },
            "OSCA": {
                "release_url": OSCA_RELEASE_URL,
                "package": "OSCA",
                "license": "CC BY 4.0",
                "course_use": "Week 14-17 single-cell workflow case extension",
                "release_links": release_links["OSCA"],
                "advanced_fallback": "https://github.com/OSCA-source/OSCA.advanced",
            },
        },
        "github_repositories": repositories,
        "notes": [
            "Large archives, extracted sources, full image mirrors, and GitHub clone caches stay under materials/raw and are ignored by git.",
            "Generated Markdown, code snippet JSONL, image manifest CSV, and workflow catalog are intended for searchable course preparation.",
        ],
    }
    return manifest


def package_records_for_source(source: str) -> list[PackageRecord]:
    manifest = load_manifest()
    records: list[PackageRecord] = []
    packages = manifest.get("packages", {})
    if not packages:
        packages = discover_manifest().get("packages", {})
    selected_names: list[str]
    if source == "OSTA":
        selected_names = ["OSTA"]
    elif source == "OSCA":
        selected_names = [name for name in BOOK_PACKAGES if name != "OSTA"]
    elif source == "all":
        selected_names = BOOK_PACKAGES
    else:
        selected_names = [source]

    for name in selected_names:
        item = packages.get(name)
        if not item or item.get("source") == "github-fallback":
            continue
        records.append(
            PackageRecord(
                package=item["package"],
                version=item["version"],
                license=item.get("license", ""),
                md5=item.get("md5", ""),
                tarball_url=item["tarball_url"],
                source=item.get("source", "bioconductor-packages"),
            )
        )
    return records


def md5sum(path: Path) -> str:
    digest = hashlib.md5()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download_package(record: PackageRecord, *, dry_run: bool = False) -> dict:
    ensure_dirs()
    filename = Path(urllib.parse.urlparse(record.tarball_url).path).name
    archive_path = ARCHIVES_DIR / filename
    part_path = archive_path.with_suffix(archive_path.suffix + ".part")
    head = fetch_head(record.tarball_url)
    info = {
        "package": record.package,
        "version": record.version,
        "url": record.tarball_url,
        "archive_path": str(archive_path.relative_to(ROOT)).replace("\\", "/"),
        "expected_md5": record.md5,
        "content_length": int(head.get("content-length", "0") or 0),
        "last_modified": head.get("last-modified"),
        "status": "dry-run" if dry_run else "pending",
    }
    if dry_run:
        return info

    if archive_path.exists() and record.md5 and md5sum(archive_path) == record.md5:
        info["status"] = "exists-valid"
        return info

    resume_at = part_path.stat().st_size if part_path.exists() else 0
    headers = {"Range": f"bytes={resume_at}-"} if resume_at else None
    request = request_url(record.tarball_url, headers=headers)
    mode = "ab" if resume_at else "wb"
    try:
        with urllib.request.urlopen(request, timeout=120) as response, part_path.open(mode) as output:
            if resume_at and response.status != 206:
                output.close()
                part_path.unlink(missing_ok=True)
                return download_package(record, dry_run=False)
            downloaded = resume_at
            last_report = time.monotonic()
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                output.write(chunk)
                downloaded += len(chunk)
                now = time.monotonic()
                if now - last_report > 20:
                    print(f"{record.package}: downloaded {downloaded / (1024 * 1024):.1f} MB", flush=True)
                    last_report = now
    except Exception:
        raise

    part_path.replace(archive_path)
    if record.md5:
        actual = md5sum(archive_path)
        info["actual_md5"] = actual
        if actual != record.md5:
            info["status"] = "md5-mismatch"
            raise RuntimeError(f"MD5 mismatch for {archive_path}: expected {record.md5}, got {actual}")
    info["status"] = "downloaded-valid"
    return info


def safe_extract_tar(archive_path: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    with tarfile.open(archive_path, "r:gz") as tar:
        destination_resolved = destination.resolve()
        for member in tar.getmembers():
            target = (destination / member.name).resolve()
            try:
                target.relative_to(destination_resolved)
            except ValueError:
                raise RuntimeError(f"Unsafe tar member path: {member.name}")
        tar.extractall(destination)


def extract_archives_for_source(source: str) -> list[dict]:
    extracted: list[dict] = []
    for record in package_records_for_source(source):
        filename = Path(urllib.parse.urlparse(record.tarball_url).path).name
        archive_path = ARCHIVES_DIR / filename
        if not archive_path.exists():
            continue
        destination = EXTRACTED_DIR / f"{record.package}_{record.version}"
        if not destination.exists():
            safe_extract_tar(archive_path, destination)
        extracted.append(
            {
                "package": record.package,
                "version": record.version,
                "archive": str(archive_path.relative_to(ROOT)).replace("\\", "/"),
                "extracted_to": str(destination.relative_to(ROOT)).replace("\\", "/"),
            }
        )
    return extracted


def get_page_urls_for_source(source: str, limit: int | None = None) -> list[str]:
    manifest = load_manifest()
    source_info = manifest.get("sources", {}).get(source, {})
    links = source_info.get("release_links")
    if not links:
        release_url = SOURCE_RELEASE_URLS[source]
        links = discover_release_links(release_url)
    expanded_links = set(links)
    if source == "OSCA":
        for link in list(links):
            if f"/books/{BIOC_VERSION}/OSCA" in link and not link.endswith(".html"):
                expanded_links.update(discover_release_links(link))

    html_links = [link for link in expanded_links if link.endswith(".html") or link.endswith("/")]
    filtered: list[str] = []
    seen: set[str] = set()
    for link in html_links:
        normalized = link if link.endswith("/") else urllib.parse.urlunparse(urllib.parse.urlparse(link)._replace(fragment=""))
        if normalized in seen:
            continue
        seen.add(normalized)
        filtered.append(normalized)
    if limit:
        return filtered[:limit]
    return filtered


def download_image(image: ImageRecord) -> str:
    target = ROOT / image.local_asset_path
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.stat().st_size > 0:
        return "exists"
    try:
        with urllib.request.urlopen(request_url(image.original_url), timeout=120) as response, target.open("wb") as output:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                output.write(chunk)
        return "downloaded"
    except Exception as exc:
        failure_path = target.with_suffix(target.suffix + ".download_error.txt")
        failure_path.write_text(f"{image.original_url}\n{exc}\n", encoding="utf-8")
        return "failed"


def write_page_outputs(page: PageContent, *, fetch_images: bool) -> tuple[list[dict], list[dict]]:
    source_root = MARKDOWN_ROOT / page.source
    page_dir = source_root / "pages"
    page_dir.mkdir(parents=True, exist_ok=True)
    image_rows: list[dict] = []
    available_images: list[ImageRecord] = []
    for image in page.images:
        status = download_image(image) if fetch_images else "listed"
        if status in {"downloaded", "exists"}:
            available_images.append(image)
        image_rows.append(
            {
                "source": image.source,
                "page_slug": image.page_slug,
                "alt": image.alt,
                "original_url": image.original_url,
                "local_asset_path": image.local_asset_path,
                "download_status": status,
            }
        )

    markdown = rewrite_images_to_local_assets(page.markdown, available_images, markdown_dir=page_dir)
    header = (
        "---\n"
        f"source: {page.source}\n"
        f"title: \"{page.title.replace('\"', '\\\"')}\"\n"
        f"original_url: {page.url}\n"
        f"ingested_at: {utc_now()}\n"
        "status: source_ingested\n"
        "---\n\n"
    )
    (page_dir / f"{page.slug}.md").write_text(header + markdown, encoding="utf-8")

    snippet_rows: list[dict] = []
    for chunk in page.code_chunks:
        target = ROOT / chunk.local_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(chunk.code.rstrip() + "\n", encoding="utf-8")
        snippet_rows.append(
            {
                "source": chunk.source,
                "page_slug": chunk.page_slug,
                "chunk_id": chunk.chunk_id,
                "language": chunk.language,
                "local_path": chunk.local_path,
                "page_url": chunk.page_url,
                "line_count": len(chunk.code.splitlines()),
                "week_mapping": map_workflow_weeks(page.title + " " + page.slug),
            }
        )
    return image_rows, snippet_rows


def append_jsonl(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def append_image_manifest(rows: Iterable[dict]) -> None:
    path = MARKDOWN_ROOT / "image_manifest.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["source", "page_slug", "alt", "original_url", "local_asset_path", "download_status"]
    exists = path.exists()
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        if not exists:
            writer.writeheader()
        for row in rows:
            writer.writerow(row)


def reset_generated_indexes() -> None:
    for path in (MARKDOWN_ROOT / "code_snippets.jsonl", MARKDOWN_ROOT / "image_manifest.csv"):
        path.unlink(missing_ok=True)


def reset_source_outputs(sources: Iterable[str]) -> None:
    reset_generated_indexes()
    for source in sources:
        source_root = MARKDOWN_ROOT / source
        for child in ("pages", "code"):
            target = source_root / child
            if target.exists():
                shutil.rmtree(target)
        (source_root / "chapter_index.json").unlink(missing_ok=True)


def extract_source(source: str, *, limit_pages: int | None, fetch_images: bool) -> dict:
    ensure_dirs()
    extracted_archives = extract_archives_for_source(source)
    page_urls = get_page_urls_for_source(source, limit_pages)
    pages: list[dict] = []
    total_images = 0
    total_chunks = 0
    for url in page_urls:
        try:
            html = fetch_text(url, timeout=120)
            page = extract_page_content(html, url, source)
            image_rows, snippet_rows = write_page_outputs(page, fetch_images=fetch_images)
            append_image_manifest(image_rows)
            append_jsonl(MARKDOWN_ROOT / "code_snippets.jsonl", snippet_rows)
            total_images += len(image_rows)
            total_chunks += len(snippet_rows)
            pages.append(
                {
                    "source": source,
                    "slug": page.slug,
                    "title": page.title,
                    "url": url,
                    "markdown_path": f"materials/markdown/bioconductor_books/{source}/pages/{page.slug}.md",
                    "image_count": len(image_rows),
                    "code_chunk_count": len(snippet_rows),
                    "week_mapping": map_workflow_weeks(page.title + " " + page.slug),
                }
            )
            print(f"{source}: extracted {page.slug} ({len(image_rows)} images, {len(snippet_rows)} code chunks)")
        except Exception as exc:
            pages.append({"source": source, "url": url, "status": "failed", "error": str(exc)})

    index_path = MARKDOWN_ROOT / source / "chapter_index.json"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index = {
        "generated_at": utc_now(),
        "source": source,
        "page_count": len(pages),
        "image_count": total_images,
        "code_chunk_count": total_chunks,
        "pages": pages,
        "extracted_archives": extracted_archives,
    }
    index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return index


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def collect_chapter_indexes() -> list[dict]:
    pages: list[dict] = []
    for path in MARKDOWN_ROOT.glob("*/chapter_index.json"):
        index = json.loads(path.read_text(encoding="utf-8"))
        pages.extend(index.get("pages", []))
    return pages


def write_workflow_catalog() -> dict:
    pages = collect_chapter_indexes()
    snippets = read_jsonl(MARKDOWN_ROOT / "code_snippets.jsonl")
    snippet_count_by_page: dict[tuple[str, str], int] = {}
    for row in snippets:
        key = (row.get("source", ""), row.get("page_slug", ""))
        snippet_count_by_page[key] = snippet_count_by_page.get(key, 0) + 1

    candidates = []
    for page in pages:
        title = page.get("title", "")
        slug = page.get("slug", "")
        text = f"{title} {slug}"
        weeks = map_workflow_weeks(text)
        if not weeks and not any(keyword in text.lower() for keyword in WORKFLOW_KEYWORDS):
            continue
        candidates.append(
            {
                "source": page.get("source"),
                "title": title,
                "slug": slug,
                "url": page.get("url"),
                "weeks": weeks,
                "image_count": page.get("image_count", 0),
                "code_chunk_count": snippet_count_by_page.get((page.get("source", ""), slug), page.get("code_chunk_count", 0)),
            }
        )

    lines = [
        "# Bioconductor OSTA/OSCA workflow case catalog",
        "",
        f"- generated_at: {utc_now()}",
        "- scope: OSTA spatial transcriptomics and OSCA single-cell book family.",
        "- status: course extension source only; this catalog does not change week readiness.",
        "",
        "| Source | Chapter | Weeks | Code chunks | Images | URL |",
        "| --- | --- | --- | ---: | ---: | --- |",
    ]
    for item in candidates:
        weeks = ", ".join(f"Week {week:02d}" for week in item["weeks"]) or "TBD"
        lines.append(
            f"| {item['source']} | {item['title']} | {weeks} | {item['code_chunk_count']} | "
            f"{item['image_count']} | {item['url']} |"
        )
    path = MARKDOWN_ROOT / "workflow_case_catalog.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"workflow_case_count": len(candidates), "path": str(path.relative_to(ROOT)).replace("\\", "/")}


def classify_source_file(path: Path) -> str:
    lower_parts = [part.lower() for part in path.parts]
    lower_joined = "/".join(lower_parts)
    name = path.name.lower()
    if ".github" in lower_parts or name.endswith((".yml", ".yaml")):
        return "automation"
    if "workflow" in name or "workflow" in lower_joined:
        return "workflow"
    if name.endswith((".r", ".rmd", ".qmd")):
        return "analysis-code"
    if name.endswith(".md"):
        return "documentation"
    return "source"


def catalog_github_sources() -> dict:
    rows: list[dict] = []
    if not GITHUB_DIR.exists():
        return {"github_repo_count": 0, "github_file_count": 0, "note": "No local OSCA-source clone cache found."}

    for repo_dir in sorted(path for path in GITHUB_DIR.iterdir() if path.is_dir()):
        if repo_dir.name.startswith("."):
            continue
        for path in sorted(repo_dir.rglob("*")):
            if not path.is_file() or ".git" in path.parts:
                continue
            if path.suffix.lower() not in {".r", ".rmd", ".qmd", ".md", ".yml", ".yaml", ".json"}:
                continue
            rel = path.relative_to(ROOT).as_posix()
            repo_rel = path.relative_to(repo_dir).as_posix()
            text = path.read_text(encoding="utf-8", errors="replace")
            category = classify_source_file(path.relative_to(repo_dir))
            rows.append(
                {
                    "repo": repo_dir.name,
                    "path": repo_rel,
                    "category": category,
                    "week_mapping": ",".join(str(week) for week in map_workflow_weeks(f"{repo_dir.name} {repo_rel}")),
                    "line_count": len(text.splitlines()),
                    "local_path": rel,
                }
            )

    csv_path = MARKDOWN_ROOT / "osca_source_workflow_files.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["repo", "path", "category", "week_mapping", "line_count", "local_path"]
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    by_repo: dict[str, dict[str, int]] = {}
    for row in rows:
        by_repo.setdefault(row["repo"], {})
        by_repo[row["repo"]][row["category"]] = by_repo[row["repo"]].get(row["category"], 0) + 1

    lines = [
        "# OSCA-source repository catalog",
        "",
        f"- generated_at: {utc_now()}",
        "- source: `https://github.com/OSCA-source` local clone cache.",
        "- boundary: source structure and workflow discovery only; no workflow execution performed.",
        "",
        "| Repository | Analysis code | Workflows | Automation | Documentation |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for repo, counts in sorted(by_repo.items()):
        lines.append(
            f"| {repo} | {counts.get('analysis-code', 0)} | {counts.get('workflow', 0)} | "
            f"{counts.get('automation', 0)} | {counts.get('documentation', 0)} |"
        )
    lines.extend(
        [
            "",
            "## Candidate Workflow Files",
            "",
            "| Repository | Path | Weeks | Lines |",
            "| --- | --- | --- | ---: |",
        ]
    )
    for row in rows:
        if row["category"] != "workflow" and not row["week_mapping"]:
            continue
        weeks = ", ".join(f"Week {int(week):02d}" for week in row["week_mapping"].split(",") if week) or "TBD"
        lines.append(f"| {row['repo']} | `{row['path']}` | {weeks} | {row['line_count']} |")

    md_path = MARKDOWN_ROOT / "osca_source_repo_catalog.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {
        "github_repo_count": len(by_repo),
        "github_file_count": len(rows),
        "github_catalog_path": str(md_path.relative_to(ROOT)).replace("\\", "/"),
        "github_workflow_csv": str(csv_path.relative_to(ROOT)).replace("\\", "/"),
    }


def write_markdown_root_index() -> None:
    lines = [
        "# Bioconductor books material index",
        "",
        "This folder stores searchable course-preparation derivatives from OSTA and OSCA. Large raw archives, extracted packages, image mirrors, and GitHub clone caches remain under `materials/raw/bioconductor_books/` and are ignored by git.",
        "",
        "## Files",
        "",
        "- `source_manifest.json`: source package metadata, release links, and OSCA-source repository metadata.",
        "- `code_snippets.jsonl`: extracted R/Python/text code block metadata and local script paths.",
        "- `image_manifest.csv`: original image URLs and local raw asset paths.",
        "- `workflow_case_catalog.md`: candidate Week 14-17 case chapters.",
        "- `osca_source_repo_catalog.md`: local `OSCA-source` repository structure and candidate workflow files.",
        "- `osca_source_workflow_files.csv`: scanned OSCA-source R/Rmd/Qmd/Markdown/YAML files with week mappings.",
        "- `OSTA/pages/` and `OSCA/pages/`: generated Markdown pages.",
        "",
        "## Course Boundary",
        "",
        "These materials are source-backed case extensions for Week 14-17. They do not promote any week status or replace `course/syllabus/`.",
    ]
    (MARKDOWN_ROOT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def command_discover(args: argparse.Namespace) -> None:
    manifest = discover_manifest()
    if args.write_manifest:
        write_manifest(manifest)
        write_markdown_root_index()
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


def command_download(args: argparse.Namespace) -> None:
    results = [download_package(record, dry_run=args.dry_run) for record in package_records_for_source(args.source)]
    print(json.dumps({"generated_at": utc_now(), "source": args.source, "results": results}, ensure_ascii=False, indent=2))


def command_extract(args: argparse.Namespace) -> None:
    if args.source == "all":
        sources = ["OSTA", "OSCA"]
    else:
        sources = [args.source]
    if args.reset_indexes:
        reset_source_outputs(sources)
    results = [
        extract_source(source, limit_pages=args.limit_pages, fetch_images=not args.no_images)
        for source in sources
    ]
    write_markdown_root_index()
    print(json.dumps({"generated_at": utc_now(), "results": results}, ensure_ascii=False, indent=2))


def command_catalog(args: argparse.Namespace) -> None:
    result = write_workflow_catalog()
    github_result = catalog_github_sources()
    write_markdown_root_index()
    print(json.dumps({"generated_at": utc_now(), **result, **github_result}, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    discover = subparsers.add_parser("discover", help="Discover Bioconductor package metadata and OSCA-source repos.")
    discover.add_argument("--write-manifest", action="store_true", help="Write source_manifest.json.")
    discover.set_defaults(func=command_discover)

    download = subparsers.add_parser("download", help="Download source tarballs with MD5 validation.")
    download.add_argument("--source", choices=["OSTA", "OSCA", "all"], required=True)
    download.add_argument("--dry-run", action="store_true")
    download.set_defaults(func=command_download)

    extract = subparsers.add_parser("extract", help="Extract archives and scrape release HTML into Markdown/code/image indexes.")
    extract.add_argument("--source", choices=["OSTA", "OSCA", "all"], required=True)
    extract.add_argument("--limit-pages", type=int, default=None)
    extract.add_argument("--no-images", action="store_true", help="List image URLs but do not download image files.")
    extract.add_argument("--reset-indexes", action="store_true", help="Reset shared image/code manifests before extraction.")
    extract.set_defaults(func=command_extract)

    catalog = subparsers.add_parser("catalog", help="Generate workflow case catalog from extracted chapter indexes.")
    catalog.set_defaults(func=command_catalog)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
