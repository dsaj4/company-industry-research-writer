# Workflow Overview

This reference defines the default run contract for the skill.

## Core objective

Produce a report that is both:

- close to a strong benchmark in structure and finish
- clearly a new report with its own object, thesis, and evidence base
- complete at the declared depth rather than superficially "finished"

## Two working loops

### 1. Report execution loop

1. Calibration
2. Thesis definition
3. Budgeted outline
4. Evidence map
5. Assignment and authorization when applicable
6. Chapter drafting
7. Merge
8. Review
9. Revision
10. Final delivery

### 2. Skill upgrade loop

1. Compare generated draft with final edited draft
2. Classify changes
3. Decide what is reusable
4. Update references or keep as case-specific note
5. Add regression evals for important misses

## Default run directory

Use:

`runs/YYYYMMDD-HHMMSS_<topic>/`

Recommended files:

- `00_request.md`: user task, constraints, benchmark, target audience
- `01_calibration.md`: five imitate / five do-not-copy bullets
- `02_thesis.md`: central judgment, chapter questions, scope boundary
- `03_outline.md`: report skeleton, chapter goals, figure plan, chapter budgets
- `orchestration/01_assignment_board.md`: chapter owners, chapter budgets, and subagent approval state when orchestration is used
- `orchestration/chapter_template/...`: per-chapter breakdown, draft, review, and revision artifacts when orchestration is used
- `04_evidence_map.md`: claim-to-evidence table
- `05_draft.md`: merged first complete version
- `06_review.md`: multi-gate review, weighted score, red lines, budget audit
- `07_revision.md`: revised version after targeted fixes
- `08_final.md`: final delivery version
- `09_upgrade_notes.md`: reusable learnings from edits

## Use cases

### New formal report

Use the full loop.

If the report is `full` + `polished`, default to orchestration discipline:

- create the assignment board
- declare total and chapter budgets
- request user approval before true subagent spawning
- if approval is not available, keep the same assignment board and run chapters sequentially

### Draft diagnosis

Start at review, then go backward only as far as needed. If the thesis is weak, rebuild from thesis or outline instead of line editing.

### Chapter-only rewrite

Keep the same run folder, but create a chapter-specific subsection in the outline, evidence map, and revision notes.

If the chapter deliverable is `medium` or `full`, keep a chapter-level word budget for the rewrite.

### Skill upgrade

Open the existing run, compare `05_draft.md` or `07_revision.md` against the human-approved version, then log reusable changes in `09_upgrade_notes.md`.
