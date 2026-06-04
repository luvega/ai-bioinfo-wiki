$ErrorActionPreference = "Continue"
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
