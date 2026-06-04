# SCBP Runnable Analysis Project

This directory is generated from `theislab/single-cell-best-practices`.

- Fixed upstream ref: `735f26fd270b3beceb4ba79f4a556c912192fe83`
- Upstream raw files: `materials/raw/sc_best_practices/upstream`
- Primary runnable form: original `notebook.ipynb` files in each chapter directory.
- Exported scripts: `chapter.py` files use Jupytext/IPython cell markers and may require IPython for magics.
- Dataset cache: `outputs/sc_best_practices/datasets/` (ignored by Git).

## Entry Points

- `run_notebook.ps1`: execute one notebook into `outputs/sc_best_practices/runs/`.
- `run_smoke.ps1`: execute the five course-relevant smoke notebooks.
- `datasets_manifest.json`: data URLs, LaminDB artifacts, and manual/blocked entries.
- `environments_manifest.json`: upstream Conda environment files.

## Smoke Notebook Scope

- `introduction/fundamental_data_structures_and_frameworks.ipynb`
- `preprocessing_visualization/quality_control.ipynb`
- `cellular_structure/clustering.ipynb`
- `conditions/differential_gene_expression.ipynb`
- `conditions/gsea_pathway.ipynb`

## Chapter Count

- Chapters/material pages: 50
