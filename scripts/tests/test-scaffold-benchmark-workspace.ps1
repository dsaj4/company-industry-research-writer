param(
    [string]$RepoRoot = (Split-Path -Parent (Split-Path -Parent $PSScriptRoot)),
    [string]$WorkspaceRoot = (Join-Path $env:TEMP "company-industry-research-writer-workspace-test"),
    [string]$IterationName = "iteration-test"
)

$ErrorActionPreference = "Stop"

$ScaffoldScript = Join-Path $RepoRoot "scripts\scaffold-benchmark-workspace.ps1"
$EvalJsonPath = Join-Path $RepoRoot "evals\evals.json"

if (Test-Path $WorkspaceRoot) {
    Remove-Item -Recurse -Force $WorkspaceRoot
}

& $ScaffoldScript -WorkspaceRoot $WorkspaceRoot -IterationName $IterationName

$EvalConfig = Get-Content -Raw $EvalJsonPath | ConvertFrom-Json
$IterationPath = Join-Path $WorkspaceRoot $IterationName

if (-not (Test-Path $IterationPath)) {
    throw "Missing iteration directory: $IterationPath"
}

$WorkspaceReadme = Join-Path $WorkspaceRoot "README.md"
if (-not (Test-Path $WorkspaceReadme)) {
    throw "Missing workspace README: $WorkspaceReadme"
}

foreach ($Eval in $EvalConfig.evals) {
    $EvalPath = Join-Path $IterationPath $Eval.eval_name
    $EvalMetadata = Join-Path $EvalPath "eval_metadata.json"
    $WithSkillOutputs = Join-Path $EvalPath "with_skill\outputs"
    $WithoutSkillOutputs = Join-Path $EvalPath "without_skill\outputs"
    $WithSkillGrading = Join-Path $EvalPath "with_skill\grading.json"
    $WithoutSkillGrading = Join-Path $EvalPath "without_skill\grading.json"
    $WithSkillTiming = Join-Path $EvalPath "with_skill\timing.json"
    $WithoutSkillTiming = Join-Path $EvalPath "without_skill\timing.json"

    foreach ($Path in @(
        $EvalPath,
        $EvalMetadata,
        $WithSkillOutputs,
        $WithoutSkillOutputs,
        $WithSkillGrading,
        $WithoutSkillGrading,
        $WithSkillTiming,
        $WithoutSkillTiming
    )) {
        if (-not (Test-Path $Path)) {
            throw "Missing scaffold path: $Path"
        }
    }
}

Write-Output "PASS test-scaffold-benchmark-workspace"
