"""Ingest Open Water Foundation Git and shell tutorials as course materials.

The script keeps upstream source mirrors under materials/raw and writes
searchable Markdown/source-card derivatives under materials/markdown and
knowledge/sources. Project paths are derived from this file location; no
absolute workspace root is embedded.
"""
from __future__ import annotations

import argparse
import json
import posixpath
import re
import shutil
import sys
import urllib.parse
import urllib.request
import zipfile
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Iterable

import yaml


ROOT = Path(__file__).resolve().parents[2]
RAW_ROOT = ROOT / "materials" / "raw" / "openwaterfoundation_learning"
MARKDOWN_ROOT = ROOT / "materials" / "markdown" / "openwaterfoundation_learning"
KNOWLEDGE_SOURCES = ROOT / "knowledge" / "sources"
ARCHIVES_DIR = RAW_ROOT / "archives"
EXTRACTED_DIR = RAW_ROOT / "extracted"

ASSET_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico"}
EXAMPLE_SUFFIXES = {".bat", ".cmd", ".ps1", ".sh", ".py", ".txt", ".csv"}
LINK_RE = re.compile(r"(!?\[[^\]\n]*\]\()([^)\s]+)(\))")


@dataclass(frozen=True)
class SourceConfig:
    key: str
    title: str
    repo: str
    site_url: str
    commit_sha: str
    course_use: str
    tags: tuple[str, ...]
    knowledge_filename: str

    @property
    def repo_url(self) -> str:
        return f"https://github.com/{self.repo}"

    @property
    def archive_url(self) -> str:
        owner, name = self.repo.split("/", 1)
        return f"https://codeload.github.com/{owner}/{name}/zip/{self.commit_sha}"


@dataclass
class DocsTree:
    markdown_files: list[Path]
    asset_files: list[Path]
    example_files: list[Path]

    @property
    def registry(self) -> set[str]:
        return {
            *[path.as_posix() for path in self.markdown_files],
            *[path.as_posix() for path in self.asset_files],
            *[path.as_posix() for path in self.example_files],
        }


SOURCES: dict[str, SourceConfig] = {
    "git": SourceConfig(
        key="git",
        title="OWF Learn Git",
        repo="OpenWaterFoundation/owf-learn-git",
        site_url="https://learn.openwaterfoundation.org/owf-learn-git/",
        commit_sha="42a393fb0e2daff55ae973f940ca946ae8d05acf",
        course_use="Week 02/03/17 version-control and reproducible workflow reference",
        tags=("git", "github", "version-control", "week-02", "week-03", "week-17"),
        knowledge_filename="OWF_Learn_Git.md",
    ),
    "windows_shell": SourceConfig(
        key="windows_shell",
        title="OWF Learn Windows Shell",
        repo="OpenWaterFoundation/owf-learn-windows-shell",
        site_url="https://learn.openwaterfoundation.org/owf-learn-windows-shell/",
        commit_sha="3d459b386751e1d799f13c63fa9a7dbcda1ac6d3",
        course_use="Week 02/03/17 Windows shell, batch file, and troubleshooting reference",
        tags=("windows-shell", "batch", "reproducibility", "week-02", "week-03", "week-17"),
        knowledge_filename="OWF_Learn_Windows_Shell.md",
    ),
    "linux_shell": SourceConfig(
        key="linux_shell",
        title="OWF Learn Linux Shell",
        repo="OpenWaterFoundation/owf-learn-linux-shell",
        site_url="https://learn.openwaterfoundation.org/owf-learn-linux-shell/",
        commit_sha="4cf789ec9b3ae88a6f8be218dcd4dadcf86ac18d",
        course_use="Week 02/03/17 Linux shell, Bash scripting, cron, and troubleshooting reference",
        tags=("linux-shell", "bash", "reproducibility", "week-02", "week-03", "week-17"),
        knowledge_filename="OWF_Learn_Linux_Shell.md",
    ),
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def request_url(url: str) -> urllib.request.Request:
    return urllib.request.Request(
        url,
        headers={"User-Agent": "AI_Course OpenWaterFoundation learning ingest/1.0"},
    )


def ensure_dirs() -> None:
    for path in (RAW_ROOT, MARKDOWN_ROOT, KNOWLEDGE_SOURCES, ARCHIVES_DIR, EXTRACTED_DIR):
        path.mkdir(parents=True, exist_ok=True)


def safe_reset_dir(path: Path, allowed_root: Path) -> None:
    target = path.resolve()
    allowed = allowed_root.resolve()
    if target == allowed:
        raise RuntimeError(f"Refusing to reset root directory: {path}")
    try:
        target.relative_to(allowed)
    except ValueError as exc:
        raise RuntimeError(f"Refusing to reset path outside {allowed_root}: {path}") from exc
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def safe_extract_zip(archive_path: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    destination_resolved = destination.resolve()
    with zipfile.ZipFile(archive_path) as archive:
        for member in archive.infolist():
            target = (destination / member.filename).resolve()
            try:
                target.relative_to(destination_resolved)
            except ValueError as exc:
                raise RuntimeError(f"Unsafe zip member path: {member.filename}") from exc
        archive.extractall(destination)


def download_archive(source: SourceConfig, *, force: bool = False) -> Path:
    ensure_dirs()
    archive_path = ARCHIVES_DIR / f"{source.key}_{source.commit_sha[:12]}.zip"
    if archive_path.exists() and archive_path.stat().st_size > 0 and not force:
        return archive_path

    part_path = archive_path.with_suffix(".zip.part")
    part_path.unlink(missing_ok=True)
    with urllib.request.urlopen(request_url(source.archive_url), timeout=180) as response, part_path.open("wb") as handle:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            handle.write(chunk)
    part_path.replace(archive_path)
    return archive_path


def extracted_repo_root(destination: Path) -> Path:
    candidates = [path for path in destination.iterdir() if path.is_dir()]
    for candidate in candidates:
        if (candidate / "mkdocs-project" / "docs").is_dir():
            return candidate
    raise RuntimeError(f"Could not find mkdocs-project/docs under {destination}")


def extract_source_archive(source: SourceConfig, *, force_download: bool = False) -> Path:
    archive_path = download_archive(source, force=force_download)
    destination = EXTRACTED_DIR / source.key
    safe_reset_dir(destination, RAW_ROOT)
    safe_extract_zip(archive_path, destination)
    return extracted_repo_root(destination)


def rel_files(root: Path, suffixes: set[str]) -> list[Path]:
    files = [
        path.relative_to(root)
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in suffixes
    ]
    return sorted(files, key=lambda item: item.as_posix().lower())


def discover_docs_tree(docs_root: Path) -> DocsTree:
    return DocsTree(
        markdown_files=rel_files(docs_root, {".md"}),
        asset_files=rel_files(docs_root, ASSET_SUFFIXES),
        example_files=rel_files(docs_root, EXAMPLE_SUFFIXES),
    )


def collect_nav_pages(node) -> list[str]:
    pages: list[str] = []
    if isinstance(node, str):
        if node.endswith(".md"):
            pages.append(node)
        return pages
    if isinstance(node, list):
        for item in node:
            pages.extend(collect_nav_pages(item))
        return pages
    if isinstance(node, dict):
        for value in node.values():
            pages.extend(collect_nav_pages(value))
    return pages


def parse_mkdocs_nav_pages(mkdocs_text: str) -> list[str]:
    data = yaml.safe_load(mkdocs_text) or {}
    pages = collect_nav_pages(data.get("nav", []))
    ordered: list[str] = []
    for page in pages:
        normalized = PurePosixPath(page).as_posix()
        if normalized not in ordered:
            ordered.append(normalized)
    return ordered


def split_local_target(raw_target: str) -> tuple[str, str, str] | None:
    parsed = urllib.parse.urlsplit(raw_target.strip("<>"))
    if parsed.scheme or parsed.netloc:
        return None
    if raw_target.startswith("#") or not parsed.path:
        return None
    suffix = ""
    if parsed.query:
        suffix += f"?{parsed.query}"
    if parsed.fragment:
        suffix += f"#{parsed.fragment}"
    return parsed.path, suffix, raw_target


def candidate_registry_paths(current_doc_path: Path, target_path: str) -> list[str]:
    current_dir = current_doc_path.parent.as_posix()
    if current_dir == ".":
        current_dir = ""
    normalized_target = target_path.replace("\\", "/")
    if normalized_target.startswith("/"):
        normalized_target = normalized_target.lstrip("/")
    if normalized_target.endswith(".html"):
        normalized_target = normalized_target[:-5] + ".md"
    elif normalized_target.endswith(".htm"):
        normalized_target = normalized_target[:-4] + ".md"
    bases: list[str] = []

    def add_base(value: str) -> None:
        value = posixpath.normpath(value).lstrip("./")
        if value and not value.startswith("../") and value not in bases:
            bases.append(value)

    add_base(posixpath.join(current_dir, normalized_target))
    stripped = normalized_target
    while stripped.startswith("../"):
        stripped = stripped[3:]
    add_base(stripped)
    add_base(normalized_target)

    candidates: list[str] = []
    for base in bases:
        expanded = [base]
        if "." not in PurePosixPath(base).name:
            expanded.extend([f"{base}.md", posixpath.join(base, "index.md")])
            last = PurePosixPath(base).name
            expanded.append(posixpath.join(base, f"{last}.md"))
        for item in expanded:
            if item not in candidates:
                candidates.append(item)
    return candidates


def unresolved_upstream_url(site_url: str, target_path: str, target_suffix: str) -> str:
    normalized = target_path.replace("\\", "/").lstrip("/")
    while normalized.startswith("../"):
        normalized = normalized[3:]
    if normalized.endswith(".md"):
        normalized = normalized[:-3] + ".html"
    elif not PurePosixPath(normalized).suffix:
        normalized = normalized.rstrip("/") + ".html"
    return urllib.parse.urljoin(site_url, normalized + target_suffix)


def rewrite_local_links(
    markdown: str,
    current_doc_path: Path,
    registry: set[str],
    *,
    site_url: str | None = None,
) -> str:
    def replace(match: re.Match[str]) -> str:
        prefix, raw_target, suffix = match.groups()
        split = split_local_target(raw_target)
        if split is None:
            return match.group(0)
        target_path, target_suffix, _ = split
        for candidate in candidate_registry_paths(current_doc_path, target_path):
            if candidate not in registry:
                continue
            start = current_doc_path.parent.as_posix()
            if start == ".":
                start = "."
            rel_target = posixpath.relpath(candidate, start=start)
            if rel_target == ".":
                rel_target = PurePosixPath(candidate).name
            return f"{prefix}{rel_target}{target_suffix}{suffix}"
        if site_url:
            return f"{prefix}{unresolved_upstream_url(site_url, target_path, target_suffix)}{suffix}"
        return match.group(0)

    return LINK_RE.sub(replace, markdown)


def first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip() or fallback
    return fallback


def first_summary(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith(("!", "|")):
            continue
        if stripped.startswith(("- ", "* ")):
            stripped = stripped[2:].strip()
        if stripped:
            return stripped[:160]
    return ""


def page_url(source: SourceConfig, rel_path: Path) -> str:
    rel = rel_path.as_posix()
    if rel == "index.md":
        return source.site_url
    if rel.endswith(".md"):
        rel = rel[:-3] + ".html"
    return urllib.parse.urljoin(source.site_url, rel)


def github_blob_url(source: SourceConfig, source_path: str) -> str:
    return f"{source.repo_url}/blob/{source.commit_sha}/{source_path}"


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def page_frontmatter(source: SourceConfig, rel_path: Path, title: str, ingested_at: str) -> str:
    source_path = f"mkdocs-project/docs/{rel_path.as_posix()}"
    tags = ", ".join(source.tags)
    return (
        "---\n"
        f"type: source-page\n"
        f"source: {source.key}\n"
        f"title: {yaml_string(title)}\n"
        f"original_url: {yaml_string(page_url(source, rel_path))}\n"
        f"repo_url: {yaml_string(source.repo_url)}\n"
        f"commit_sha: {source.commit_sha}\n"
        f"source_path: {yaml_string(source_path)}\n"
        f"source_blob: {yaml_string(github_blob_url(source, source_path))}\n"
        "license: license_needs_review\n"
        f"ingested_at: {ingested_at}\n"
        "status: source_ingested\n"
        f"tags: [{tags}]\n"
        "---\n\n"
    )


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def infer_license(repo_root: Path) -> str:
    license_files = list(repo_root.glob("LICENSE*")) + list(repo_root.glob("COPYING*"))
    if license_files:
        return "see-upstream-license-file"
    scan_paths = [
        repo_root / "README.md",
        repo_root / "mkdocs-project" / "docs" / "index.md",
        repo_root / "mkdocs-project" / "mkdocs.yml",
    ]
    combined = "\n".join(read_text(path) for path in scan_paths if path.exists()).lower()
    if "cc by-nc-sa" in combined or "creative commons attribution-noncommercial-sharealike" in combined:
        return "CC BY-NC-SA 4.0"
    if "creative commons" in combined:
        return "creative-commons-needs-review"
    return "license_needs_review"


def copy_support_file(docs_root: Path, output_pages_root: Path, rel_path: Path) -> dict:
    source_path = docs_root / rel_path
    target_path = output_pages_root / rel_path
    target_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, target_path)
    return {
        "source_path": f"mkdocs-project/docs/{rel_path.as_posix()}",
        "local_path": target_path.relative_to(ROOT).as_posix(),
        "suffix": rel_path.suffix.lower(),
    }


def copy_source_to_markdown(source: SourceConfig, repo_root: Path, *, ingested_at: str) -> dict:
    docs_root = repo_root / "mkdocs-project" / "docs"
    mkdocs_path = repo_root / "mkdocs-project" / "mkdocs.yml"
    readme_path = repo_root / "README.md"
    output_root = MARKDOWN_ROOT / source.key
    output_pages_root = output_root / "pages"
    safe_reset_dir(output_root, MARKDOWN_ROOT)

    tree = discover_docs_tree(docs_root)
    registry = tree.registry
    nav_pages = parse_mkdocs_nav_pages(read_text(mkdocs_path)) if mkdocs_path.exists() else []
    nav_order = {page: index for index, page in enumerate(nav_pages, start=1)}
    license_value = infer_license(repo_root)

    page_rows: list[dict] = []
    for rel_path in tree.markdown_files:
        source_text = read_text(docs_root / rel_path)
        rewritten = rewrite_local_links(source_text, rel_path, registry, site_url=source.site_url)
        title = first_heading(source_text, rel_path.stem.replace("-", " ").title())
        target_path = output_pages_root / rel_path
        write_text(target_path, page_frontmatter(source, rel_path, title, ingested_at) + rewritten.rstrip() + "\n")
        page_rows.append(
            {
                "title": title,
                "summary": first_summary(source_text),
                "source_path": f"mkdocs-project/docs/{rel_path.as_posix()}",
                "local_path": target_path.relative_to(ROOT).as_posix(),
                "original_url": page_url(source, rel_path),
                "source_blob": github_blob_url(source, f"mkdocs-project/docs/{rel_path.as_posix()}"),
                "nav_order": nav_order.get(rel_path.as_posix()),
            }
        )

    asset_rows = [copy_support_file(docs_root, output_pages_root, path) for path in tree.asset_files]
    example_rows = [copy_support_file(docs_root, output_pages_root, path) for path in tree.example_files]

    source_manifest = {
        "generated_at": ingested_at,
        "source": asdict(source),
        "repo_url": source.repo_url,
        "archive_url": source.archive_url,
        "license": license_value,
        "license_note": "GitHub repository metadata does not expose SPDX license; review upstream site/repo before PPT reuse.",
        "raw_repo_root": repo_root.relative_to(ROOT).as_posix(),
        "markdown_root": output_root.relative_to(ROOT).as_posix(),
        "mkdocs_nav_pages": nav_pages,
        "page_count": len(page_rows),
        "asset_count": len(asset_rows),
        "example_count": len(example_rows),
        "pages": page_rows,
        "assets": asset_rows,
        "examples": example_rows,
    }
    write_text(output_root / "chapter_index.json", json.dumps(source_manifest, ensure_ascii=False, indent=2) + "\n")
    write_source_readme(source, source_manifest)
    return source_manifest


def write_source_readme(source: SourceConfig, manifest: dict) -> None:
    output_root = MARKDOWN_ROOT / source.key
    lines = [
        f"# {source.title}",
        "",
        f"- upstream_site: [{source.site_url}]({source.site_url})",
        f"- upstream_repo: [{source.repo}]({source.repo_url})",
        f"- fixed_commit: `{source.commit_sha}`",
        f"- license: `{manifest['license']}`",
        f"- course_use: {source.course_use}",
        "- boundary: reference material only; does not change any week readiness or PPT status.",
        "",
        "## Local Files",
        "",
        "- `pages/`: mirrored MkDocs source pages plus support assets/examples.",
        "- `chapter_index.json`: page, asset, and example manifest.",
        "",
        "## Course Mapping",
        "",
        "- Week 02: reproducible workflow, shell environment, Git workflow, and troubleshooting.",
        "- Week 03: programming setup, small command-line operations, and AI-assisted coding prerequisites.",
        "- Week 17: project collaboration, scripted workflows, and result verification.",
        "- Week 14/15: Bash or shell references only; does not replace AIDD bioinformatics workflow sources.",
    ]
    write_text(output_root / "README.md", "\n".join(lines) + "\n")


def write_root_manifest(source_manifests: list[dict], *, ingested_at: str) -> None:
    manifest = {
        "generated_at": ingested_at,
        "raw_root": RAW_ROOT.relative_to(ROOT).as_posix(),
        "markdown_root": MARKDOWN_ROOT.relative_to(ROOT).as_posix(),
        "sources": source_manifests,
        "boundary": "Reference-only teaching material; knowledge/ supports preparation and does not override course/syllabus.",
    }
    write_text(MARKDOWN_ROOT / "source_manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# Open Water Foundation learning materials",
        "",
        "This folder contains source-backed, fixed-commit derivatives from Open Water Foundation tutorials for AI_Course preparation.",
        "",
        "## Sources",
        "",
    ]
    for item in source_manifests:
        source = item["source"]
        lines.append(
            f"- [{source['title']}]({source['key']}/README.md): `{source['repo']}` at `{source['commit_sha'][:12]}`; "
            f"{item['page_count']} pages, {item['asset_count']} assets, {item['example_count']} examples."
        )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- Raw archives and extracted upstream mirrors stay under `materials/raw/openwaterfoundation_learning/` and are ignored by Git.",
            "- These materials support Week 02, Week 03, and Week 17 preparation; they do not promote week readiness.",
            "- License status is recorded as `license_needs_review` unless a stable upstream license file or explicit license text is found.",
        ]
    )
    write_text(MARKDOWN_ROOT / "README.md", "\n".join(lines) + "\n")


def write_knowledge_source_card(source: SourceConfig, manifest: dict, *, ingested_at: str) -> None:
    license_value = manifest["license"]
    title_cn = {
        "git": "OWF Learn Git",
        "windows_shell": "OWF Learn Windows Shell",
        "linux_shell": "OWF Learn Linux Shell",
    }[source.key]
    path = KNOWLEDGE_SOURCES / source.knowledge_filename
    tags = ", ".join(source.tags)
    content = f"""---
type: source
title: {title_cn}
authors: [Open Water Foundation]
year: 2022
raw_path:
  - materials/raw/openwaterfoundation_learning/archives/{source.key}_{source.commit_sha[:12]}.zip
  - materials/raw/openwaterfoundation_learning/extracted/{source.key}/
  - materials/markdown/openwaterfoundation_learning/{source.key}/
ingested: {ingested_at[:10]}
language: en
kind: online-course
license: {license_value}
status: source_ingested
tags: [{tags}]
---

# {title_cn}

## 一句话定位

**Git / shell / 可复现工作流参考源**，服务 Week 02、Week 03 和 Week 17 的版本控制、命令行环境、脚本化和故障排查讲解。它是课程备课辅助材料，不替代 `course/syllabus/` 和 `course/weeks/` 主线。

## 来源与固定版本

- Online book: [{source.site_url}]({source.site_url})
- Upstream repository: [{source.repo}]({source.repo_url})
- Fixed commit: `{source.commit_sha}`
- License status: `{license_value}`
- Copyright: Open Water Foundation

## 本地素材位置

- Source manifest: [source_manifest](../../materials/markdown/openwaterfoundation_learning/source_manifest.json)
- Course index: [{source.key}/README](../../materials/markdown/openwaterfoundation_learning/{source.key}/README.md)
- Chapter index: [{source.key}/chapter_index](../../materials/markdown/openwaterfoundation_learning/{source.key}/chapter_index.json)
- Mirrored pages: `materials/markdown/openwaterfoundation_learning/{source.key}/pages/`

## 课程使用边界

- Week 02：用于解释复现规范、Git 工作流、目录和命令行环境。
- Week 03：用于补充 AI 辅助编程前的 Git 与 shell 操作，不替代 Python 小数据主线。
- Week 17：用于综合项目协作、脚本化、故障排查和结果核验。
- Week 14/15：只作为 Bash/命令行辅助参考，不替代 AIDD 生信上游流程、DESeq2 或官方文档。

## 待核验点

- 进入 PPT 前必须复核许可证、图片使用边界和截图上下文。
- 教程示例来自通用水资源/软件工程场景，进入药学课堂前需要改写为医药数据处理语境。
- 工具界面和安装步骤可能随版本变化，正式讲义只使用稳定原则，不依赖过时界面截图。
"""
    write_text(path, content)


def ingest_sources(source_keys: Iterable[str], *, force_download: bool = False) -> list[dict]:
    ensure_dirs()
    ingested_at = utc_now()
    manifests: list[dict] = []
    for key in source_keys:
        source = SOURCES[key]
        repo_root = extract_source_archive(source, force_download=force_download)
        manifest = copy_source_to_markdown(source, repo_root, ingested_at=ingested_at)
        write_knowledge_source_card(source, manifest, ingested_at=ingested_at)
        manifests.append(manifest)
        print(
            f"{source.key}: ingested {manifest['page_count']} pages, "
            f"{manifest['asset_count']} assets, {manifest['example_count']} examples",
            flush=True,
        )
    write_root_manifest(manifests, ingested_at=ingested_at)
    return manifests


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest = subparsers.add_parser("ingest", help="Download fixed commits and write course material derivatives.")
    ingest.add_argument("--source", choices=["all", *SOURCES.keys()], required=True)
    ingest.add_argument("--force-download", action="store_true", help="Re-download upstream fixed-commit archives.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "ingest":
        keys = list(SOURCES) if args.source == "all" else [args.source]
        manifests = ingest_sources(keys, force_download=args.force_download)
        print(json.dumps({"generated_at": utc_now(), "sources": manifests}, ensure_ascii=False, indent=2))
        return 0
    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
