param(
    [Parameter(Mandatory = $true)]
    [string]$PptxPath,

    [Parameter(Mandatory = $true)]
    [string]$OutputDir,

    [int]$Width = 1600,
    [int]$Height = 900
)

$resolvedPptx = (Resolve-Path -LiteralPath $PptxPath).Path
$resolvedOutput = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($OutputDir)
New-Item -ItemType Directory -Force -Path $resolvedOutput | Out-Null

Get-ChildItem -LiteralPath $resolvedOutput -Filter "*.PNG" -File -ErrorAction SilentlyContinue | Remove-Item -Force
Get-ChildItem -LiteralPath $resolvedOutput -Filter "*.png" -File -ErrorAction SilentlyContinue | Remove-Item -Force

$powerPoint = $null
$presentation = $null

try {
    $powerPoint = New-Object -ComObject PowerPoint.Application
    $presentation = $powerPoint.Presentations.Open($resolvedPptx, $true, $false, $false)
    $presentation.Export($resolvedOutput, "PNG", $Width, $Height)
}
finally {
    if ($presentation -ne $null) {
        $presentation.Close()
        [System.Runtime.InteropServices.Marshal]::ReleaseComObject($presentation) | Out-Null
    }
    if ($powerPoint -ne $null) {
        $powerPoint.Quit()
        [System.Runtime.InteropServices.Marshal]::ReleaseComObject($powerPoint) | Out-Null
    }
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
}

Get-ChildItem -LiteralPath $resolvedOutput -Filter "*.PNG" -File |
    Sort-Object Name |
    Select-Object FullName, Length
