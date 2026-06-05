param(
  [Parameter(Mandatory=$true)][string]$Notebook,
  [string]$OutputRoot = "outputs/sc_best_practices/runs"
)

$ErrorActionPreference = "Stop"
$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")
$notebookPath = Resolve-Path (Join-Path $repoRoot $Notebook)
$runRoot = Join-Path $repoRoot $OutputRoot
New-Item -ItemType Directory -Force -Path $runRoot | Out-Null

python -m jupyter nbconvert --to notebook --execute $notebookPath --output-dir $runRoot
