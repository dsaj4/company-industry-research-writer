# Eval Templates

This folder stores reusable JSON scaffolds for benchmark workspaces.

Current template:

- `grading-template.json`: starter shape for each run's `grading.json`

Typical use:

1. Copy the relevant file from `metadata/` into the eval folder as `eval_metadata.json`.
2. Copy `templates/grading-template.json` into each run folder as `grading.json`.
3. Replace the placeholder expectation entry with the assertion texts from `eval_metadata.json`.
4. Fill evidence, summary, and notes after grading.
