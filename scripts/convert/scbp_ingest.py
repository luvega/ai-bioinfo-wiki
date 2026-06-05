"""Download upstream single-cell-best-practices source files into materials/raw."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

from scbp_utils import (
    BOOK_ROOT,
    DEFAULT_REF,
    IMAGE_EXTENSIONS,
    METADATA_EXTENSIONS,
    RAW_ROOT,
    REPO_URL,
    SCBP_ROOT,
    SOURCE_EXTENSIONS,
    TocEntry,
    download_binary,
    file_record,
    github_tree,
    now_iso,
    parse_toc,
    raw_url,
    read_json,
    rel,
    write_json,
)


ROOT_FILES = ("LICENSE", "README.md", "CONTRIBUTING.md", "environment.yml", "pyproject.toml")


def collect_upstream_paths(ref: str) -> tuple[list[dict[str, Any]], list[TocEntry]]:
    tree = github_tree(ref)
    paths = {item["path"] for item in tree if item.get("type") == "blob"}
    toc_url = raw_url(ref, f"{BOOK_ROOT}/_toc.yml")
    toc_tmp = RAW_ROOT / "_tmp_toc.yml"
    download_binary(toc_url, toc_tmp)
    toc_text = toc_tmp.read_text(encoding="utf-8")
    toc_tmp.unlink(missing_ok=True)
    toc_entries = parse_toc(toc_text, paths)

    selected: dict[str, str] = {}
    for root_file in ROOT_FILES:
        if root_file in paths:
            selected[root_file] = "repo-root"
    for path in paths:
        if not path.startswith(f"{BOOK_ROOT}/"):
            continue
        suffix = Path(path).suffix.lower()
        if path in {f"{BOOK_ROOT}/_toc.yml", f"{BOOK_ROOT}/_config.yml", f"{BOOK_ROOT}/references.bib"}:
            selected[path] = "book-config"
        elif suffix in SOURCE_EXTENSIONS:
            selected[path] = "book-source"
        elif suffix in METADATA_EXTENSIONS:
            selected[path] = "book-metadata"
        elif suffix in IMAGE_EXTENSIONS:
            selected[path] = "book-static-image"

    for entry in toc_entries:
        if entry.source_path:
            selected[entry.source_path] = "toc-chapter"

    records = [{"path": path, "role": role} for path, role in sorted(selected.items())]
    return records, toc_entries


def write_source_note(manifest: dict[str, Any]) -> None:
    SCBP_ROOT.mkdir(parents=True, exist_ok=True)
    lines = [
        "---",
        "type: source-asset-bundle",
        "title: Single-cell best practices upstream bundle",
        f"upstream_ref: {manifest['ref']}",
        "status: generated",
        "tags: [single-cell, scbp, upstream, course-material]",
        "---",
        "",
        "# Single-cell Best Practices · Upstream Bundle",
        "",
        "本目录记录 `theislab/single-cell-best-practices` 的课程素材抓取结果。",
        "",
        f"- Upstream repository: [{REPO_URL}]({REPO_URL})",
        f"- Fixed ref: `{manifest['ref']}`",
        f"- Raw bundle: `{rel(RAW_ROOT)}`",
        f"- Manifest: `{rel(RAW_ROOT / 'source_manifest.json')}`",
        "- License: Apache License 2.0, see upstream `LICENSE` in the raw bundle.",
        "- Scope: Jupyter Book notebooks, Markdown chapters, BibTeX files, Conda YAML files, and static images.",
        "- Execution policy: notebooks are not executed during ingest; runnable entrypoints are built by `scbp_build_analysis_project.py`.",
        "",
        "本素材只作为备课辅助层使用；课程事实主线仍以 `course/syllabus/` 和 `course/weeks/` 为准。",
        "",
    ]
    (SCBP_ROOT / "SOURCE.md").write_text("\n".join(lines), encoding="utf-8")


def write_course_index_stub(toc_entries: list[TocEntry], ref: str) -> None:
    rows = []
    for entry in toc_entries:
        rows.append(
            f"| {entry.order:02d} | {entry.part} | {entry.title} | `{entry.file}` | {entry.source_type or 'missing'} |"
        )
    lines = [
        "---",
        "type: course-source-index",
        "title: Single-cell Best Practices 课程素材索引",
        f"upstream_ref: {ref}",
        "status: generated_draft",
        "tags: [single-cell, scbp, course-material, auto-extract]",
        "---",
        "",
        "# Single-cell Best Practices 课程素材索引",
        "",
        "本索引由 `scripts/convert/scbp_ingest.py` 初始化，完整课程映射由 `scbp_build_analysis_project.py` 更新。",
        "",
        "| Order | Part | Title | TOC file | Source type |",
        "|---:|---|---|---|---|",
        *rows,
        "",
    ]
    (SCBP_ROOT / "scbp.course_index.md").write_text("\n".join(lines), encoding="utf-8")


def run_write(ref: str) -> dict[str, Any]:
    records, toc_entries = collect_upstream_paths(ref)
    downloaded: list[dict[str, Any]] = []
    RAW_ROOT.mkdir(parents=True, exist_ok=True)
    for record in records:
        upstream_path = record["path"]
        target = RAW_ROOT / upstream_path
        download_binary(raw_url(ref, upstream_path), target)
        downloaded.append(file_record(target, upstream_path, ref, record["role"]))

    missing = [entry.file for entry in toc_entries if not entry.source_path]
    manifest = {
        "version": 1,
        "generated_at": now_iso(),
        "repo": REPO_URL,
        "ref": ref,
        "raw_root": rel(RAW_ROOT),
        "toc_entries": [entry.__dict__ for entry in toc_entries],
        "file_count": len(downloaded),
        "total_bytes": sum(item["bytes"] for item in downloaded),
        "missing_toc_sources": missing,
        "files": downloaded,
    }
    write_json(RAW_ROOT / "source_manifest.json", manifest)
    write_source_note(manifest)
    write_course_index_stub(toc_entries, ref)
    return manifest


def run_check() -> list[str]:
    manifest_path = RAW_ROOT / "source_manifest.json"
    if not manifest_path.exists():
        return [f"Missing {rel(manifest_path)}"]
    manifest = read_json(manifest_path)
    issues: list[str] = []
    for item in manifest.get("files", []):
        path = RAW_ROOT / item["upstream_path"]
        if not path.exists():
            issues.append(f"Missing downloaded file: {rel(path)}")
        elif path.stat().st_size != item["bytes"]:
            issues.append(f"Size changed: {rel(path)}")
    if manifest.get("missing_toc_sources"):
        issues.append("Unresolved TOC entries: " + ", ".join(manifest["missing_toc_sources"]))
    return issues


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", default=DEFAULT_REF, help="Git ref or commit to download.")
    parser.add_argument("--write", action="store_true", help="Download source files and write manifests.")
    parser.add_argument("--check", action="store_true", help="Check downloaded files against manifest.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.write and not args.check:
        parser.error("Choose --write and/or --check")
    if args.write:
        manifest = run_write(args.ref)
        print(f"Downloaded {manifest['file_count']} files ({manifest['total_bytes']} bytes).")
    if args.check:
        issues = run_check()
        if issues:
            for issue in issues:
                print(f"SCBP_INGEST_CHECK: {issue}")
            return 1
        print("OK: SCBP upstream files match source_manifest.json.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

