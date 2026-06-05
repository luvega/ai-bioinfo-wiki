"""Build a runnable analysis project from ingested SCBP notebooks."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from scbp_utils import (
    ANALYSIS_ROOT,
    BOOK_ROOT,
    RAW_ROOT,
    SCBP_ROOT,
    TocEntry,
    cell_source,
    chapter_dir_name,
    code_cell_index,
    copy_file,
    export_notebook_code,
    extract_dataset_references,
    first_heading_from_markdown,
    first_heading_from_notebook,
    load_notebook,
    markdown_source_document,
    markdown_table,
    notebook_to_markdown,
    read_json,
    read_source_text_for_refs,
    rel,
    week_mapping,
    write_json,
)


SMOKE_NOTEBOOKS = [
    "introduction/fundamental_data_structures_and_frameworks",
    "preprocessing_visualization/quality_control",
    "cellular_structure/clustering",
    "conditions/differential_gene_expression",
    "conditions/gsea_pathway",
]


def load_ingest_manifest() -> dict[str, Any]:
    manifest_path = RAW_ROOT / "source_manifest.json"
    if not manifest_path.exists():
        raise SystemExit("Run scbp_ingest.py --write before building the analysis project.")
    return read_json(manifest_path)


def build_environment_manifest() -> list[dict[str, Any]]:
    envs: list[dict[str, Any]] = []
    for path in sorted((RAW_ROOT / BOOK_ROOT).rglob("*.yml")):
        text = path.read_text(encoding="utf-8", errors="replace")
        name = ""
        deps: list[str] = []
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.startswith("name:"):
                name = stripped.split(":", 1)[1].strip().strip("'\"")
            elif stripped.startswith("- ") and not stripped.startswith("- file:"):
                deps.append(stripped[2:].strip())
        envs.append(
            {
                "name": name or path.stem,
                "source_path": rel(path),
                "upstream_path": path.relative_to(RAW_ROOT).as_posix(),
                "dependency_count": len(deps),
                "dependencies_preview": deps[:30],
            }
        )
    return envs


def pick_environment(entry: TocEntry, environments: list[dict[str, Any]]) -> str | None:
    if not entry.source_path:
        return None
    parent = str(Path(entry.source_path).parent).replace("\\", "/")
    for env in environments:
        if str(Path(env["upstream_path"]).parent).replace("\\", "/") == parent:
            return env["name"]
    if "preprocessing_visualization" in parent:
        for env in environments:
            if env["name"] == "preprocessing":
                return env["name"]
    return None


def source_title(path: Path, fallback: str) -> str:
    if path.suffix.lower() == ".ipynb":
        return first_heading_from_notebook(load_notebook(path), fallback)
    return first_heading_from_markdown(path.read_text(encoding="utf-8", errors="replace"), fallback)


def build_chapter(entry: TocEntry, manifest: dict[str, Any], environments: list[dict[str, Any]]) -> dict[str, Any]:
    if not entry.source_path:
        return {"entry": entry.__dict__, "status": "missing_source"}
    ref = manifest["ref"]
    source = RAW_ROOT / entry.source_path
    title = source_title(source, entry.title)
    out_dir = ANALYSIS_ROOT / "chapters" / chapter_dir_name(entry)
    out_dir.mkdir(parents=True, exist_ok=True)

    code_rows: list[dict[str, Any]] = []
    if source.suffix.lower() == ".ipynb":
        nb = load_notebook(source)
        copy_file(source, out_dir / "notebook.ipynb")
        (out_dir / "chapter.source.md").write_text(
            notebook_to_markdown(nb, title=title, ref=ref, source_path=entry.source_path),
            encoding="utf-8",
        )
        code_text = export_notebook_code(nb, title=title, ref=ref, source_path=entry.source_path)
        (out_dir / "chapter.py").write_text(code_text, encoding="utf-8")
        code_rows = code_cell_index(nb)
    else:
        text = source.read_text(encoding="utf-8", errors="replace")
        (out_dir / "chapter.source.md").write_text(
            markdown_source_document(text, title=title, ref=ref, source_path=entry.source_path),
            encoding="utf-8",
        )
        (out_dir / "chapter.py").write_text(
            "# This upstream chapter is Markdown-only; no notebook code cells were available.\n",
            encoding="utf-8",
        )

    code_index_lines = [
        f"# Code Index · {title}",
        "",
        "| Cell | Language | Lines | Has outputs | First line |",
        "|---:|---|---:|---|---|",
    ]
    for row in code_rows:
        code_index_lines.append(
            f"| {row['cell']} | {row['language']} | {row['line_count']} | {row['has_outputs']} | `{row['first_line']}` |"
        )
    if not code_rows:
        code_index_lines.append("| - | - | - | - | No code cells |")
    (out_dir / "code_index.md").write_text("\n".join(code_index_lines) + "\n", encoding="utf-8")

    refs = extract_dataset_references(read_source_text_for_refs(source), source_id=entry.file)
    chapter_manifest = {
        "order": entry.order,
        "part": entry.part,
        "toc_file": entry.file,
        "title": title,
        "source_type": source.suffix.lstrip("."),
        "upstream_path": entry.source_path,
        "environment": pick_environment(entry, environments),
        "week_mapping": week_mapping(entry, title),
        "code_cell_count": len(code_rows),
        "dataset_reference_count": len(refs),
        "paths": {
            "chapter_dir": rel(out_dir),
            "source_markdown": rel(out_dir / "chapter.source.md"),
            "script": rel(out_dir / "chapter.py"),
            "code_index": rel(out_dir / "code_index.md"),
        },
    }
    write_json(out_dir / "chapter_manifest.json", chapter_manifest)
    return {**chapter_manifest, "dataset_references": refs}


def write_project_readme(chapters: list[dict[str, Any]], ref: str) -> None:
    lines = [
        "# SCBP Runnable Analysis Project",
        "",
        "This directory is generated from `theislab/single-cell-best-practices`.",
        "",
        f"- Fixed upstream ref: `{ref}`",
        f"- Upstream raw files: `{rel(RAW_ROOT)}`",
        "- Primary runnable form: original `notebook.ipynb` files in each chapter directory.",
        "- Exported scripts: `chapter.py` files use Jupytext/IPython cell markers and may require IPython for magics.",
        "- Dataset cache: `outputs/sc_best_practices/datasets/` (ignored by Git).",
        "",
        "## Entry Points",
        "",
        "- `run_notebook.ps1`: execute one notebook into `outputs/sc_best_practices/runs/`.",
        "- `run_smoke.ps1`: execute the five course-relevant smoke notebooks.",
        "- `datasets_manifest.json`: data URLs, LaminDB artifacts, and manual/blocked entries.",
        "- `environments_manifest.json`: upstream Conda environment files.",
        "",
        "## Smoke Notebook Scope",
        "",
    ]
    for item in SMOKE_NOTEBOOKS:
        lines.append(f"- `{item}.ipynb`")
    lines.extend(["", "## Chapter Count", "", f"- Chapters/material pages: {len(chapters)}", ""])
    (ANALYSIS_ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_runner_scripts() -> None:
    run_notebook = r"""param(
  [Parameter(Mandatory=$true)][string]$Notebook,
  [string]$OutputRoot = "outputs/sc_best_practices/runs"
)

$ErrorActionPreference = "Stop"
$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")
$notebookPath = Resolve-Path (Join-Path $repoRoot $Notebook)
$runRoot = Join-Path $repoRoot $OutputRoot
New-Item -ItemType Directory -Force -Path $runRoot | Out-Null

python -m jupyter nbconvert --to notebook --execute $notebookPath --output-dir $runRoot
"""
    run_smoke = r"""$ErrorActionPreference = "Continue"
$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")
$reportDir = Join-Path $repoRoot "materials/markdown/sc_best_practices/analysis_project/smoke_runs"
New-Item -ItemType Directory -Force -Path $reportDir | Out-Null
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$report = Join-Path $reportDir "$stamp-smoke-run.md"
$notebooks = @(
  "materials/markdown/sc_best_practices/analysis_project/chapters/04_introduction_fundamental_data_structures_and_frameworks/notebook.ipynb",
  "materials/markdown/sc_best_practices/analysis_project/chapters/08_preprocessing_visualization_quality_control/notebook.ipynb",
  "materials/markdown/sc_best_practices/analysis_project/chapters/12_cellular_structure_clustering/notebook.ipynb",
  "materials/markdown/sc_best_practices/analysis_project/chapters/18_conditions_differential_gene_expression/notebook.ipynb",
  "materials/markdown/sc_best_practices/analysis_project/chapters/20_conditions_gsea_pathway/notebook.ipynb"
)

"# SCBP Smoke Run`n" | Set-Content -Encoding UTF8 $report
foreach ($notebook in $notebooks) {
  "`n## $notebook`n" | Add-Content -Encoding UTF8 $report
  $started = Get-Date
  python -m jupyter nbconvert --to notebook --execute (Join-Path $repoRoot $notebook) --output-dir (Join-Path $repoRoot "outputs/sc_best_practices/runs") *> "$reportDir/last-notebook.log"
  $exit = $LASTEXITCODE
  $elapsed = [math]::Round(((Get-Date) - $started).TotalSeconds, 1)
  "- exit_code: $exit" | Add-Content -Encoding UTF8 $report
  "- elapsed_seconds: $elapsed" | Add-Content -Encoding UTF8 $report
  "```text" | Add-Content -Encoding UTF8 $report
  Get-Content "$reportDir/last-notebook.log" -ErrorAction SilentlyContinue | Select-Object -Last 80 | Add-Content -Encoding UTF8 $report
  "```" | Add-Content -Encoding UTF8 $report
}
"""
    (ANALYSIS_ROOT / "run_notebook.ps1").write_text(run_notebook, encoding="utf-8")
    (ANALYSIS_ROOT / "run_smoke.ps1").write_text(run_smoke, encoding="utf-8")


def write_course_index(chapters: list[dict[str, Any]], ref: str) -> None:
    def scbp_rel(repo_relative_path: str) -> str:
        return Path(repo_relative_path).relative_to("materials/markdown/sc_best_practices").as_posix()

    rows = []
    for chapter in chapters:
        weeks = ", ".join(f"Week {week:02d}" for week in chapter.get("week_mapping", [])) or "-"
        source = chapter["paths"]["source_markdown"]
        script = chapter["paths"]["script"]
        rows.append(
            [
                f"{chapter['order']:02d}",
                chapter["part"],
                f"[{chapter['title']}]({scbp_rel(source)})",
                weeks,
                f"[code]({scbp_rel(script)})",
                chapter["environment"] or "-",
            ]
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
        "本索引从 upstream Jupyter Book 全量 notebook/Markdown 构建，用于 Week 13-16 的单细胞、降维、聚类、差异分析和可视化备课。",
        "",
        "## 工程入口",
        "",
        f"- Upstream raw bundle: `{rel(RAW_ROOT)}`",
        f"- Runnable project: [`analysis_project/README.md`](analysis_project/README.md)",
        f"- Dataset manifest: [`analysis_project/datasets_manifest.json`](analysis_project/datasets_manifest.json)",
        f"- Extracted outputs: [`extracted_outputs/outputs_index.md`](extracted_outputs/outputs_index.md)",
        "",
        "## 章节映射",
        "",
        markdown_table(rows, ["Order", "Part", "Title", "Course weeks", "Code", "Environment"]),
        "",
        "## 周次使用建议",
        "",
        "- Week 13: dimensionality reduction、clustering、PCA/UMAP 参数解释。",
        "- Week 14: scRNA-seq raw data processing、AnnData/Scanpy 数据结构和互操作。",
        "- Week 15: differential gene expression、compositional analysis、GSEA/pathway。",
        "- Week 16: QC、normalization、feature selection、annotation、integration、trajectory。",
        "",
        "正式进入 PPT 前仍需回查 upstream 章节、数据许可和课程主线，不能把 notebook 输出直接当作医学或统计结论。",
        "",
    ]
    (SCBP_ROOT / "scbp.course_index.md").write_text("\n".join(lines), encoding="utf-8")


def run_write() -> dict[str, Any]:
    manifest = load_ingest_manifest()
    entries = [TocEntry(**item) for item in manifest["toc_entries"]]
    ANALYSIS_ROOT.mkdir(parents=True, exist_ok=True)
    environments = build_environment_manifest()
    chapters: list[dict[str, Any]] = []
    dataset_refs: list[dict[str, Any]] = []
    for entry in entries:
        chapter = build_chapter(entry, manifest, environments)
        if chapter.get("status") == "missing_source":
            continue
        dataset_refs.extend(chapter.pop("dataset_references"))
        chapters.append(chapter)

    write_json(ANALYSIS_ROOT / "chapters_manifest.json", chapters)
    write_json(ANALYSIS_ROOT / "datasets_manifest.json", {"version": 1, "items": dataset_refs})
    write_json(ANALYSIS_ROOT / "environments_manifest.json", {"version": 1, "items": environments})
    write_project_readme(chapters, manifest["ref"])
    write_runner_scripts()
    write_course_index(chapters, manifest["ref"])
    return {"chapter_count": len(chapters), "dataset_reference_count": len(dataset_refs), "environment_count": len(environments)}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Build analysis project files.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.write:
        parser.error("Choose --write")
    summary = run_write()
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
