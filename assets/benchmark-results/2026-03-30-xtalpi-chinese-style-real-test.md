# XtalPi Chinese Style Real Test

## Run identity

- Date: `2026-03-30`
- Run: `runs/20260330-161912_xtalpi-chinese-style-real-test/`
- Task type: scoped real-world style test
- Target object: `晶泰控股`
- Deliverable slice:
  - 首页标题与核心结论
  - 公司概况开篇

## Why this test exists

This is the first real-world validation pass after the writing-facing layers were switched to Chinese-first constraints.

The goal is not to benchmark a full report yet.

The goal is to see whether the current skill can produce a more realistic Chinese sell-side-style slice while keeping:

- clear thesis
- evidence traceability
- benchmark boundaries
- non-copycat writing

## Source pack used

- local GF Securities XtalPi report
- extracted evidence from pages `1`, `2`, `16`, and `36`
- current Chinese-first references:
  - `references/language-policy.md`
  - `references/writing-style.md`
  - `references/style-signatures.md`
  - `references/report-framework.md`
  - `references/quality-scorecard.md`
  - `references/evidence-financial-rules.md`

## What was produced

- `00_request.md`
- `01_calibration.md`
- `02_thesis.md`
- `03_outline.md`
- `04_evidence_map.md`
- `05_draft.md`
- `06_review.md`
- `07_revision.md`
- `08_final.md`
- `09_upgrade_notes.md`

All artifacts are stored under:

- `runs/20260330-161912_xtalpi-chinese-style-real-test/`

## Main qualitative result

The Chinese-first writing layers appear to help meaningfully on this scoped slice.

Most visible gains:

1. the front-page output now reads like a compressed judgment map rather than a translated material summary
2. the company-overview opener starts from company archetype and stage judgment instead of background dumping
3. the tone is more recognizably Chinese research writing and less like generic analysis prose

## What still needs work

1. title sharpening can still be stronger
2. risk compression on the page-1 ending line can still be tighter
3. stage-judgment sentences deserve their own reusable micro-patterns

## What this means for the skill

This test increases confidence that the current workflow is not only preserving analytical structure, but also beginning to preserve Chinese research-report writing quality.

It also suggests the next high-value eval additions are:

1. `front-page-core-points`
2. `company-overview-opener`
