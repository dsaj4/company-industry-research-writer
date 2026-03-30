# Workflow Overview

This reference defines the default run contract for the skill.

## Core objective

Produce a report that is both:

- close to a strong benchmark in structure and finish
- clearly a new report with its own object, thesis, and evidence base

## Two working loops

### 1. Report execution loop

1. Calibration
2. Thesis definition
3. Outline
4. Evidence map
5. Draft
6. Review
7. Revision
8. Final delivery

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
- `03_outline.md`: report skeleton, chapter goals, figure plan
- `04_evidence_map.md`: claim-to-evidence table
- `05_draft.md`: first complete version
- `06_review.md`: dual-gate review, weighted score, red lines
- `07_revision.md`: revised version after targeted fixes
- `08_final.md`: final delivery version
- `09_upgrade_notes.md`: reusable learnings from edits

## Use cases

### New formal report

Use the full loop.

### Draft diagnosis

Start at review, then go backward only as far as needed. If the thesis is weak, rebuild from thesis or outline instead of line editing.

### Chapter-only rewrite

Keep the same run folder, but create a chapter-specific subsection in the outline, evidence map, and revision notes.

### Skill upgrade

Open the existing run, compare `05_draft.md` or `07_revision.md` against the human-approved version, then log reusable changes in `09_upgrade_notes.md`.
