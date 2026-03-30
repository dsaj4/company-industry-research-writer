# Evals

This directory stores the reusable evaluation layer for the skill.

Use the files together:

- `evals.json`: master index for prompts, source files, and benchmark-ready expectations
- `cases/`: file-backed test inputs that avoid depending on raw copyrighted PDFs
- `metadata/`: richer per-eval grading templates that can be copied into a benchmark workspace
- `templates/`: reusable scaffolds such as the run-level `grading.json` template

## Design rule

Keep `evals.json` close to the `skill-creator` schema so it can be reused in later benchmark runs.

Put richer review context in `metadata/` rather than overloading the main index.

## Current eval coverage

- report-start package with benchmark calibration, budgeting, and orchestration decision
- draft diagnosis with red-line blocking logic
- chapter rewrite from evidence pack
- benchmark-family selection across multiple benchmark samples

## Workflow

1. Read `evals.json` to choose the eval and collect input files.
2. Copy the matching `metadata/*.json` payload into the run workspace as `eval_metadata.json`.
3. Copy `templates/grading-template.json` into the run workspace as the starting `grading.json`.
4. Grade against the `assertions` in `eval_metadata.json`, using `references/grading-conventions.md`, and mirror the same texts into `grading.json`.
5. Keep human review focused on benchmark quality and shell-copy boundaries.
