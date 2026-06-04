"""Utilities for ingesting the single-cell-best-practices Jupyter Book."""
from __future__ import annotations

import base64
import hashlib
import json
import re
import shutil
import textwrap
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]

REPO_OWNER = "theislab"
REPO_NAME = "single-cell-best-practices"
REPO_FULL_NAME = f"{REPO_OWNER}/{REPO_NAME}"
REPO_URL = f"https://github.com/{REPO_FULL_NAME}"
BOOK_ROOT = "jupyter-book"
DEFAULT_REF = "735f26fd270b3beceb4ba79f4a556c912192fe83"

RAW_ROOT = ROOT / "materials" / "raw" / "sc_best_practices" / "upstream"
SCBP_ROOT = ROOT / "materials" / "markdown" / "sc_best_practices"
ANALYSIS_ROOT = SCBP_ROOT / "analysis_project"
EXTRACTED_OUTPUTS_ROOT = SCBP_ROOT / "extracted_outputs"
STATIC_ASSETS_ROOT = SCBP_ROOT / "static"
DATASET_OUTPUT_ROOT = ROOT / "outputs" / "sc_best_practices" / "datasets"

USER_AGENT = "AI_Course-scbp-ingest"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".svg", ".gif", ".ico", ".webp"}
SOURCE_EXTENSIONS = {".ipynb", ".md"}
METADATA_EXTENSIONS = {".bib", ".yml", ".yaml"}


@dataclass(frozen=True)
class TocEntry:
    order: int
    part: str
    file: str
    title: str
    source_path: str | None = None
    source_type: str | None = None


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def rel(path: Path, root: Path = ROOT) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def safe_name(value: str, *, max_len: int = 90) -> str:
    value = value.replace("\\", "/").split("/")[-1]
    value = re.sub(r"[^A-Za-z0-9._-]+", "_", value.strip())
    value = value.strip("._-").lower() or "item"
    return value[:max_len].strip("._-") or "item"


def heading_slug(value: str, *, max_len: int = 70) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "_", value.strip())
    value = re.sub(r"_+", "_", value).strip("_").lower()
    return (value or "chapter")[:max_len].strip("_") or "chapter"


def parse_toc(text: str, tree_paths: set[str] | None = None) -> list[TocEntry]:
    """Parse the subset of Jupyter Book _toc.yml used by SCBP."""
    root_file = "preamble"
    current_part = "Introduction"
    entries: list[TocEntry] = []
    pending_index: int | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        root_match = re.match(r"root:\s*(.+)$", stripped)
        if root_match:
            root_file = _strip_yaml_scalar(root_match.group(1))
            continue
        caption_match = re.match(r"-\s+caption:\s*(.+)$", stripped)
        if caption_match:
            current_part = _strip_yaml_scalar(caption_match.group(1))
            pending_index = None
            continue
        file_match = re.match(r"-\s+file:\s*(.+)$", stripped)
        if file_match:
            file_value = _strip_yaml_scalar(file_match.group(1))
            title = _default_title(file_value)
            entries.append(TocEntry(len(entries) + 1, current_part, file_value, title))
            pending_index = len(entries) - 1
            continue
        title_match = re.match(r"title:\s*(.+)$", stripped)
        if title_match and pending_index is not None:
            entry = entries[pending_index]
            entries[pending_index] = TocEntry(
                entry.order,
                entry.part,
                entry.file,
                _strip_yaml_scalar(title_match.group(1)),
            )

    all_entries = [TocEntry(0, "Preamble", root_file, "Single-cell best practices"), *entries]
    if tree_paths is None:
        return all_entries
    return [resolve_toc_entry(entry, tree_paths) for entry in all_entries]


def _strip_yaml_scalar(value: str) -> str:
    return value.strip().strip("'\"")


def _default_title(file_value: str) -> str:
    return file_value.replace("_", " ").replace("/", " / ").title()


def resolve_toc_entry(entry: TocEntry, tree_paths: set[str]) -> TocEntry:
    source = resolve_book_file(entry.file, tree_paths)
    source_type = Path(source).suffix.lstrip(".") if source else None
    return TocEntry(entry.order, entry.part, entry.file, entry.title, source, source_type)


def resolve_book_file(file_value: str, tree_paths: set[str]) -> str | None:
    candidates = [
        f"{BOOK_ROOT}/{file_value}",
        f"{BOOK_ROOT}/{file_value}.ipynb",
        f"{BOOK_ROOT}/{file_value}.md",
    ]
    for candidate in candidates:
        if candidate in tree_paths:
            return candidate
    return None


def github_api_json(url: str) -> Any:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def github_tree(ref: str) -> list[dict[str, Any]]:
    url = f"https://api.github.com/repos/{REPO_FULL_NAME}/git/trees/{urllib.parse.quote(ref)}?recursive=1"
    payload = github_api_json(url)
    return payload.get("tree", [])


def raw_url(ref: str, upstream_path: str) -> str:
    return f"https://raw.githubusercontent.com/{REPO_FULL_NAME}/{urllib.parse.quote(ref)}/{upstream_path}"


def github_blob_url(ref: str, upstream_path: str) -> str:
    return f"{REPO_URL}/blob/{ref}/{upstream_path}"


def download_binary(url: str, target: Path, *, timeout: int = 120) -> int:
    target.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = response.read()
    target.write_bytes(data)
    return len(data)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def load_notebook(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def cell_source(cell: dict[str, Any]) -> str:
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(str(part) for part in source)
    return str(source)


def first_heading_from_markdown(text: str, fallback: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip() or fallback
    return fallback


def first_heading_from_notebook(nb: dict[str, Any], fallback: str) -> str:
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        heading = first_heading_from_markdown(cell_source(cell), "")
        if heading:
            return heading
    return fallback


def guess_code_language(source: str) -> str:
    stripped = source.lstrip()
    if stripped.startswith("%%R") or stripped.startswith("%R"):
        return "r"
    if stripped.startswith("%%bash") or stripped.startswith("%%sh") or stripped.startswith("!"):
        return "bash"
    if stripped.startswith("%%script R"):
        return "r"
    return "python"


def rewrite_markdown_links(text: str, *, ref: str, source_path: str) -> str:
    """Rewrite relative Markdown links to upstream GitHub URLs for link checks."""
    source_dir = Path(source_path).parent.as_posix()

    def repl(match: re.Match[str]) -> str:
        prefix = match.group("prefix")
        label = match.group("label")
        raw_target = match.group("target").strip()
        if prefix == "!":
            return match.group(0)
        clean_target = raw_target.strip("<>")
        if (
            not clean_target
            or clean_target.startswith("#")
            or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", clean_target)
            or clean_target.startswith("mailto:")
        ):
            return match.group(0)
        suffix = ""
        base_target = clean_target
        for sep in ("#", "?"):
            if sep in base_target:
                base_target, suffix = base_target.split(sep, 1)
                suffix = sep + suffix
                break
        normalized = (Path(source_dir) / urllib.parse.unquote(base_target)).as_posix()
        normalized = _normalize_posix_path(normalized)
        url = github_blob_url(ref, normalized) + suffix
        return f"{prefix}[{label}]({url})"

    pattern = re.compile(r"(?P<prefix>!?)\[(?P<label>[^\]\n]+)\]\((?P<target>[^)\n]+)\)")
    return pattern.sub(repl, text)


def _normalize_posix_path(path: str) -> str:
    parts: list[str] = []
    for part in path.replace("\\", "/").split("/"):
        if not part or part == ".":
            continue
        if part == "..":
            if parts:
                parts.pop()
            continue
        parts.append(part)
    return "/".join(parts)


def notebook_to_markdown(nb: dict[str, Any], *, title: str, ref: str, source_path: str) -> str:
    lines = [
        "---",
        "type: scbp-chapter-source",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"upstream_path: {source_path}",
        f"upstream_ref: {ref}",
        "status: generated",
        "tags: [single-cell, scbp, notebook, course-material]",
        "---",
        "",
        f"# {title}",
        "",
        "> Generated from the upstream notebook. Markdown and code cells are preserved; outputs are extracted separately.",
        "",
    ]
    for index, cell in enumerate(nb.get("cells", []), start=1):
        source = cell_source(cell).rstrip()
        if not source:
            continue
        if cell.get("cell_type") == "markdown":
            lines.append(f"<!-- markdown cell {index} -->")
            lines.append(rewrite_markdown_links(source, ref=ref, source_path=source_path))
            lines.append("")
        elif cell.get("cell_type") == "code":
            language = guess_code_language(source)
            lines.append(f"## Code cell {index}")
            lines.append("")
            lines.append(f"```{language}")
            lines.append(source)
            lines.append("```")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def markdown_source_document(text: str, *, title: str, ref: str, source_path: str) -> str:
    rewritten = rewrite_markdown_links(text, ref=ref, source_path=source_path).rstrip()
    return "\n".join(
        [
            "---",
            "type: scbp-markdown-source",
            f"title: {json.dumps(title, ensure_ascii=False)}",
            f"upstream_path: {source_path}",
            f"upstream_ref: {ref}",
            "status: generated",
            "tags: [single-cell, scbp, markdown, course-material]",
            "---",
            "",
            rewritten,
            "",
        ]
    )


def export_notebook_code(nb: dict[str, Any], *, title: str, ref: str, source_path: str) -> str:
    lines = [
        "# Auto-generated from single-cell-best-practices.",
        f"# Title: {title}",
        f"# Upstream: {github_blob_url(ref, source_path)}",
        "# Run with IPython/Jupyter when cells contain magics or shell commands.",
        "",
    ]
    for index, cell in enumerate(nb.get("cells", []), start=1):
        source = cell_source(cell).rstrip()
        if not source:
            continue
        if cell.get("cell_type") == "markdown":
            lines.append("# %% [markdown]")
            for line in source.splitlines():
                lines.append("# " + line)
            lines.append("")
        elif cell.get("cell_type") == "code":
            lines.append("# %%")
            lines.append(f"# Upstream code cell: {index}")
            lines.append(source)
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def code_cell_index(nb: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for index, cell in enumerate(nb.get("cells", []), start=1):
        if cell.get("cell_type") != "code":
            continue
        source = cell_source(cell)
        non_empty = [line for line in source.splitlines() if line.strip()]
        rows.append(
            {
                "cell": index,
                "language": guess_code_language(source),
                "line_count": len(source.splitlines()),
                "first_line": non_empty[0][:160] if non_empty else "",
                "has_outputs": bool(cell.get("outputs")),
            }
        )
    return rows


URL_RE = re.compile(r"https?://[^\s\"'<>\\\]\)]+")
READ_RE = re.compile(
    r"(?P<func>(?:sc|mu)\.read(?:_[A-Za-z0-9_]+)?|(?:pd\.)?read_csv|read_h5ad|read_10x(?:_[A-Za-z0-9_]+)?)\((?P<args>[^)\n]{0,240})\)"
)


def extract_dataset_references(text: str, *, source_id: str) -> list[dict[str, Any]]:
    refs: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for match in URL_RE.finditer(text):
        url = match.group(0).rstrip(".,;:")
        classification = classify_url(url)
        key = ("url", url)
        if key in seen:
            continue
        seen.add(key)
        refs.append({"source": source_id, "kind": "url", "value": url, **classification})

    for match in re.finditer(r"(?m)^\s*[!$]?\s*(?:wget|curl)\b.*$", text):
        command = match.group(0).strip()
        key = ("command", command)
        if key in seen:
            continue
        seen.add(key)
        refs.append({"source": source_id, "kind": "download_command", "value": command, "status": "manual_required"})

    for match in re.finditer(r"Artifact\.connect\((?P<instance>[^)]*)\)", text):
        window = text[match.start() : match.start() + 800]
        key_match = re.search(r"\.get\((?P<args>[^)]{0,260})\)", window)
        value = key_match.group("args").strip() if key_match else match.group("instance").strip()
        key = ("lamindb", value)
        if key in seen:
            continue
        seen.add(key)
        refs.append(
            {
                "source": source_id,
                "kind": "lamindb_artifact",
                "value": value,
                "status": "manual_required",
                "reason": "Requires lamindb connection and artifact lookup.",
            }
        )

    for match in READ_RE.finditer(text):
        value = f"{match.group('func')}({match.group('args').strip()})"
        key = ("read", value)
        if key in seen:
            continue
        seen.add(key)
        refs.append({"source": source_id, "kind": "data_read_call", "value": value, "status": "context_required"})
    return refs


def classify_url(url: str) -> dict[str, str]:
    parsed = urllib.parse.urlparse(url)
    host = parsed.netloc.lower()
    path = parsed.path.lower()
    query = parsed.query.lower()
    if "x-amz-signature" in query or "x-amz-expires" in query:
        return {"status": "blocked", "reason": "Temporary signed URL is likely expired."}
    if "figshare.com" in host and "/ndownloader/files/" in path:
        return {"status": "pending_download", "reason": "Direct figshare file endpoint."}
    if "umd.box.com" in host and "/shared/static/" in path:
        return {"status": "pending_download", "reason": "Direct Box shared static endpoint."}
    if "zenodo.org" in host:
        return {"status": "manual_required", "reason": "Zenodo record requires file selection or license review."}
    if "10xgenomics.com" in host and "/resources/datasets" in path:
        return {"status": "manual_required", "reason": "10x dataset page is not a direct file endpoint."}
    if re.search(r"\.(h5ad|h5|h5mu|rds|csv|tsv|mtx|mtx.gz|tar.gz|tgz|zip|gz)$", path):
        return {"status": "pending_download", "reason": "URL path looks like a data file."}
    return {"status": "skipped_non_dataset", "reason": "Reference URL, documentation, or non-data web page."}


def extract_notebook_output_files(nb: dict[str, Any], output_dir: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    output_dir.mkdir(parents=True, exist_ok=True)
    for cell_index, cell in enumerate(nb.get("cells", []), start=1):
        for output_index, output in enumerate(cell.get("outputs", []) or [], start=1):
            output_type = output.get("output_type", "output")
            if output_type == "stream":
                text = _join_mime_value(output.get("text", ""))
                target = output_dir / f"cell_{cell_index:03d}_output_{output_index:02d}_stream.txt"
                target.write_text(text, encoding="utf-8")
                records.append(_output_record(target, cell_index, output_index, output_type, "text/plain"))
                continue
            if output_type == "error":
                text = "\n".join(output.get("traceback", []))
                target = output_dir / f"cell_{cell_index:03d}_output_{output_index:02d}_error.txt"
                target.write_text(text, encoding="utf-8")
                records.append(_output_record(target, cell_index, output_index, output_type, "error/traceback"))
                continue
            data = output.get("data", {}) or {}
            for mime, value in data.items():
                suffix = mime_to_suffix(mime)
                target = output_dir / f"cell_{cell_index:03d}_output_{output_index:02d}_{safe_name(mime)}{suffix}"
                if mime in {"image/png", "image/jpeg"}:
                    target.write_bytes(base64.b64decode(_join_mime_value(value)))
                elif mime == "application/json" or mime.endswith("+json"):
                    target.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
                else:
                    target.write_text(_join_mime_value(value), encoding="utf-8")
                records.append(_output_record(target, cell_index, output_index, output_type, mime))
    return records


def _join_mime_value(value: Any) -> str:
    if isinstance(value, list):
        return "".join(str(part) for part in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, indent=2)
    return str(value)


def mime_to_suffix(mime: str) -> str:
    mapping = {
        "image/png": ".png",
        "image/jpeg": ".jpg",
        "image/svg+xml": ".svg",
        "text/html": ".html",
        "text/plain": ".txt",
        "application/json": ".json",
    }
    if mime.endswith("+json"):
        return ".json"
    return mapping.get(mime, ".txt")


def _output_record(path: Path, cell: int, output: int, output_type: str, mime: str) -> dict[str, Any]:
    return {
        "path": rel(path),
        "cell": cell,
        "output": output,
        "output_type": output_type,
        "mime": mime,
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
    }


def chapter_dir_name(entry: TocEntry) -> str:
    return f"{entry.order:02d}_{heading_slug(entry.file)}"


def week_mapping(entry: TocEntry, title: str = "") -> list[int]:
    haystack = f"{entry.file} {entry.part} {title}".lower()
    mapping: list[int] = []
    rules = [
        (13, ["dimensionality", "clustering", "pca", "heatmap"]),
        (14, ["scrna_seq", "raw_data_processing", "fundamental_data_structures", "advanced_data_structures", "interoperability", "rapids"]),
        (15, ["differential_gene_expression", "gsea", "pathway", "compositional", "perturbation"]),
        (16, ["quality_control", "normalization", "feature_selection", "annotation", "integration", "pseudotemporal", "rna_velocity", "single-cell", "spatial"]),
    ]
    for week, keywords in rules:
        if any(keyword in haystack for keyword in keywords):
            mapping.append(week)
    return mapping


def markdown_table(rows: list[list[Any]], headers: list[str]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "|" + "|".join(["---"] * len(headers)) + "|",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(item) for item in row) + " |")
    return "\n".join(lines)


def wrap_comment(text: str, width: int = 88) -> list[str]:
    lines: list[str] = []
    for paragraph in text.splitlines() or [""]:
        if not paragraph:
            lines.append("#")
            continue
        lines.extend("# " + item for item in textwrap.wrap(paragraph, width=width))
    return lines


def read_source_text_for_refs(path: Path) -> str:
    if path.suffix.lower() == ".ipynb":
        nb = load_notebook(path)
        chunks: list[str] = []
        for cell in nb.get("cells", []):
            chunks.append(cell_source(cell))
            for output in cell.get("outputs", []) or []:
                chunks.append(_join_mime_value(output.get("text", "")))
                chunks.append(_join_mime_value(output.get("data", {})))
        return "\n".join(chunks)
    return path.read_text(encoding="utf-8", errors="replace")


def file_record(path: Path, upstream_path: str, ref: str, role: str) -> dict[str, Any]:
    return {
        "role": role,
        "upstream_path": upstream_path,
        "local_path": rel(path),
        "url": raw_url(ref, upstream_path),
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
    }
