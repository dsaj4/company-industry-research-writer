[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$scriptPath = Join-Path $repoRoot "scripts\\build-benchmark-length-profile.py"
$profilesDir = Join-Path $repoRoot "assets\\benchmark-profiles"

$cases = @(
    @{
        Benchmark = "minimax"
        ProfilePath = Join-Path $profilesDir "minimax-born-global-2026-02-10.json"
    },
    @{
        Benchmark = "fourth-paradigm"
        ProfilePath = Join-Path $profilesDir "fourth-paradigm-decision-intelligence-2024-12-03.json"
    }
)

foreach ($case in $cases) {
    $generated = (& python $scriptPath --benchmark $case.Benchmark) | Out-String | ConvertFrom-Json
    $checkedIn = Get-Content $case.ProfilePath -Raw -Encoding utf8 | ConvertFrom-Json

    if ($generated.benchmark_id -ne $checkedIn.benchmark_id) {
        throw "benchmark_id mismatch for $($case.Benchmark)"
    }

    foreach ($field in @("raw_md_chars", "clean_full_report_chars", "transferable_body_chars")) {
        if ($generated.$field -ne $checkedIn.$field) {
            throw "$field mismatch for $($case.Benchmark): expected $($checkedIn.$field), got $($generated.$field)"
        }
    }

    if ($generated.transferable_body_chars -gt $generated.clean_full_report_chars) {
        throw "transferable_body_chars should not exceed clean_full_report_chars for $($case.Benchmark)"
    }

    foreach ($chapter in $checkedIn.chapter_weight_profile.PSObject.Properties.Name) {
        $expectedWeight = [double]$checkedIn.chapter_weight_profile.$chapter
        $actualWeight = [double]$generated.chapter_weight_profile.$chapter
        if ([math]::Abs($expectedWeight - $actualWeight) -gt 0.0001) {
            throw "chapter weight mismatch for $($case.Benchmark)::$chapter"
        }
    }
}

Write-Output "benchmark length profile tests passed"
