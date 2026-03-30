# Scripts

This folder stores reusable local helpers for the skill.

## Current scripts

- `scaffold-benchmark-workspace.ps1`
  - creates a local benchmark workspace outside the git-tracked repo
  - copies `eval_metadata.json` files into an iteration folder
  - creates `with_skill` and `without_skill` run directories
  - seeds each run with `grading.json` and `timing.json`

- `tests/test-scaffold-benchmark-workspace.ps1`
  - smoke test for the scaffold script

## Example

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\scaffold-benchmark-workspace.ps1
```
