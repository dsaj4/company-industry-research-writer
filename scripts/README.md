# Scripts

This folder stores reusable local helpers for the skill.

## Current scripts

- `scaffold-benchmark-workspace.ps1`
  - creates a local benchmark workspace outside the git-tracked repo
  - copies `eval_metadata.json` files into an iteration folder
  - creates `with_skill` and `without_skill` run directories
  - seeds each run with `grading.json` and `timing.json`
- `build-benchmark-length-profile.py`
  - builds a benchmark length profile from a local `.md` text extraction in `materials/`
  - outputs `raw_md_chars`, `clean_full_report_chars`, `transferable_body_chars`
  - derives chapter weights and ratio-based budgets for `short / medium / full`

- `tests/test-scaffold-benchmark-workspace.ps1`
  - smoke test for the scaffold script
- `tests/test-build-benchmark-length-profile.ps1`
  - verifies that the generated profile matches the checked-in benchmark profile JSON files

## Example

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\scaffold-benchmark-workspace.ps1
python .\scripts\build-benchmark-length-profile.py --benchmark minimax --pretty
```
