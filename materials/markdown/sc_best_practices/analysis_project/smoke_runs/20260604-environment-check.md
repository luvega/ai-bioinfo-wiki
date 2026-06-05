# SCBP Smoke Run Environment Check

Date: 2026-06-04

## Requested Smoke Scope

- `introduction/fundamental_data_structures_and_frameworks.ipynb`
- `preprocessing_visualization/quality_control.ipynb`
- `cellular_structure/clustering.ipynb`
- `conditions/differential_gene_expression.ipynb`
- `conditions/gsea_pathway.ipynb`

## Result

Smoke execution was not started because the active Python environment does not provide Jupyter execution tooling.

```text
python -m jupyter --version
C:\Python313\python.exe: No module named jupyter

python -c "import nbconvert, nbformat"
ModuleNotFoundError: No module named 'nbconvert'
```

## Follow-up

Use `run_smoke.ps1` after creating the relevant upstream Conda/Jupyter environments. The five notebooks and their exported scripts are already present under `analysis_project/chapters/`.
