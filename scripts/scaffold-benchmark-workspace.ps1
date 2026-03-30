param(
    [string]$WorkspaceRoot,
    [string]$IterationName = "iteration-1",
    [switch]$Force
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$ProjectRoot = Split-Path -Parent $RepoRoot

if (-not $WorkspaceRoot) {
    $WorkspaceRoot = Join-Path $ProjectRoot "company-industry-research-writer-workspace"
}

$EvalConfigPath = Join-Path $RepoRoot "evals\evals.json"
$MetadataDir = Join-Path $RepoRoot "evals\metadata"
$GradingTemplatePath = Join-Path $RepoRoot "evals\templates\grading-template.json"
$WorkspaceReadmePath = Join-Path $WorkspaceRoot "README.md"
$HistoryPath = Join-Path $WorkspaceRoot "history.json"
$IterationPath = Join-Path $WorkspaceRoot $IterationName
$IterationReadmePath = Join-Path $IterationPath "README.md"
$IterationManifestPath = Join-Path $IterationPath "iteration_manifest.json"

if ((Test-Path $IterationPath) -and (-not $Force)) {
    throw "Iteration already exists: $IterationPath. Re-run with -Force to overwrite it."
}

$EvalConfig = Get-Content -Raw $EvalConfigPath | ConvertFrom-Json
$GeneratedAt = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")

New-Item -ItemType Directory -Force -Path $WorkspaceRoot | Out-Null
New-Item -ItemType File -Force -Path $WorkspaceReadmePath | Out-Null

$WorkspaceReadme = @"
# Company Industry Research Writer Workspace

Generated from:

- skill repo: `$RepoRoot`
- generated at: `$GeneratedAt`

## Current purpose

This workspace stores benchmark iterations outside the git-tracked skill repository.

## Default loop

1. Open an eval directory under `$IterationName`.
2. Run both `with_skill` and `without_skill` into the pre-created folders.
3. Fill `grading.json` using the assertion texts from `eval_metadata.json`.
4. Save timings in each run folder.
5. Aggregate results after all runs finish.

## Current iteration

- `$IterationName`
"@

Set-Content -Path $WorkspaceReadmePath -Value $WorkspaceReadme -Encoding utf8

$HistoryObject = [ordered]@{
    started_at = $GeneratedAt
    skill_name = $EvalConfig.skill_name
    current_best = ""
    iterations = @()
}

New-Item -ItemType File -Force -Path $HistoryPath | Out-Null
$HistoryObject | ConvertTo-Json -Depth 10 | Set-Content -Path $HistoryPath -Encoding utf8

$IterationReadme = @"
# $IterationName

Generated from `$(Split-Path -Leaf $RepoRoot)` at `$GeneratedAt`.

## Eval directories

Each eval directory contains:

- `eval_metadata.json`
- `with_skill/outputs/`
- `with_skill/grading.json`
- `with_skill/timing.json`
- `without_skill/outputs/`
- `without_skill/grading.json`
- `without_skill/timing.json`

Use `references/grading-conventions.md` in the skill repo when filling the grading files.
"@

if (Test-Path $IterationPath) {
    Remove-Item -Recurse -Force $IterationPath
}

New-Item -ItemType Directory -Force -Path $IterationPath | Out-Null

Set-Content -Path $IterationReadmePath -Value $IterationReadme -Encoding utf8

$IterationManifest = [ordered]@{
    iteration_name = $IterationName
    generated_at = $GeneratedAt
    skill_name = $EvalConfig.skill_name
    skill_repo = $RepoRoot
    eval_count = $EvalConfig.evals.Count
    evals = @()
}

foreach ($Eval in $EvalConfig.evals) {
    $EvalDir = Join-Path $IterationPath $Eval.eval_name
    $EvalMetadataSource = Get-ChildItem -Path $MetadataDir -Filter "eval-$($Eval.id)-*.json" | Select-Object -First 1

    if (-not $EvalMetadataSource) {
        throw "Could not find eval metadata for eval id $($Eval.id)."
    }

    New-Item -ItemType Directory -Force -Path $EvalDir | Out-Null

    Copy-Item -Path $EvalMetadataSource.FullName -Destination (Join-Path $EvalDir "eval_metadata.json") -Force

    $InputFilesBlock = ($Eval.files | ForEach-Object { "- $_" }) -join [Environment]::NewLine

    $EvalReadme = @"
# $($Eval.eval_name)

## Prompt

$($Eval.prompt)

## Expected output

$($Eval.expected_output)

## Input files

$InputFilesBlock
"@

    Set-Content -Path (Join-Path $EvalDir "README.md") -Value $EvalReadme -Encoding utf8

    foreach ($Configuration in @("with_skill", "without_skill")) {
        $RunDir = Join-Path $EvalDir $Configuration
        $OutputsDir = Join-Path $RunDir "outputs"
        $TimingPath = Join-Path $RunDir "timing.json"

        New-Item -ItemType Directory -Force -Path $OutputsDir | Out-Null
        Copy-Item -Path $GradingTemplatePath -Destination (Join-Path $RunDir "grading.json") -Force

        $TimingObject = [ordered]@{
            total_tokens = 0
            duration_ms = 0
            total_duration_seconds = 0.0
        }

        $TimingObject | ConvertTo-Json -Depth 10 | Set-Content -Path $TimingPath -Encoding utf8
    }

    $IterationManifest.evals += [ordered]@{
        eval_id = $Eval.id
        eval_name = $Eval.eval_name
        directory = $Eval.eval_name
    }
}

$IterationManifest | ConvertTo-Json -Depth 10 | Set-Content -Path $IterationManifestPath -Encoding utf8

Write-Output "Workspace scaffolded at $IterationPath"
