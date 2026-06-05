"""Copy SCBP static images and extract notebook outputs."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from scbp_utils import (
    BOOK_ROOT,
    EXTRACTED_OUTPUTS_ROOT,
    IMAGE_EXTENSIONS,
    RAW_ROOT,
    STATIC_ASSETS_ROOT,
    copy_file,
    extract_notebook_output_files,
    load_notebook,
    read_json,
    rel,
    sha256_file,
    write_json,
)


def copy_static_assets() -> list[dict]:
    records: list[dict] = []
    for path in sorted((RAW_ROOT / BOOK_ROOT).rglob("*")):
        if not path.is_file() or path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        relative = path.relative_to(RAW_ROOT / BOOK_ROOT)
        target = STATIC_ASSETS_ROOT / relative
        copy_file(path, target)
        records.append(
            {
                "upstream_path": path.relative_to(RAW_ROOT).as_posix(),
                "local_path": rel(target),
                "bytes": target.stat().st_size,
                "sha256": sha256_file(target),
            }
        )
    return records


def extract_outputs() -> list[dict]:
    manifest_path = RAW_ROOT / "source_manifest.json"
    manifest = read_json(manifest_path)
    records: list[dict] = []
    entries = manifest.get("toc_entries", [])
    for entry in entries:
        source_path = entry.get("source_path")
        if not source_path or not source_path.endswith(".ipynb"):
            continue
        nb_path = RAW_ROOT / source_path
        if not nb_path.exists():
            continue
        chapter_slug = f"{entry['order']:02d}_{entry['file'].replace('/', '_')}"
        output_dir = EXTRACTED_OUTPUTS_ROOT / chapter_slug
        output_records = extract_notebook_output_files(load_notebook(nb_path), output_dir)
        for record in output_records:
            record["toc_file"] = entry["file"]
            record["upstream_path"] = source_path
        records.extend(output_records)
    return records


def write_indexes(static_records: list[dict], output_records: list[dict]) -> None:
    EXTRACTED_OUTPUTS_ROOT.mkdir(parents=True, exist_ok=True)
    lines = [
        "# SCBP Extracted Outputs",
        "",
        "Notebook outputs are extracted from upstream notebooks for teaching inspection. They are not local re-execution results.",
        "",
        f"- Static image files copied: {len(static_records)}",
        f"- Notebook output files extracted: {len(output_records)}",
        "",
        "## Output Summary",
        "",
        "| File | MIME | Cell | Output | Bytes |",
        "|---|---|---:|---:|---:|",
    ]
    for record in output_records[:500]:
        lines.append(f"| `{record['path']}` | {record['mime']} | {record['cell']} | {record['output']} | {record['bytes']} |")
    (EXTRACTED_OUTPUTS_ROOT / "outputs_index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    write_json(EXTRACTED_OUTPUTS_ROOT / "outputs_manifest.json", {"version": 1, "items": output_records})
    write_json(STATIC_ASSETS_ROOT / "static_assets_manifest.json", {"version": 1, "items": static_records})


def run_write() -> dict:
    static_records = copy_static_assets()
    output_records = extract_outputs()
    write_indexes(static_records, output_records)
    return {"static_assets": len(static_records), "notebook_outputs": len(output_records)}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Copy and extract assets.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.write:
        parser.error("Choose --write")
    print(json.dumps(run_write(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

