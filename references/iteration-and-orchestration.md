# Iteration And Orchestration

Use this reference when the report is too large or too uneven to improve safely as one monolithic draft.

## When to switch modes

Switch from whole-draft editing to chapter orchestration when:

- the thesis is mostly right but chapters are thin or uneven
- some sections still feel like notes while others feel finished
- the report keeps getting patched without becoming stronger
- one chapter needs a from-zero rewrite

## Main idea

Separate global control from chapter execution.

### Global control

Responsible for:

- thesis
- chapter weights
- question tree
- evidence priorities
- merge logic

### Chapter execution

Responsible for one chapter only:

- subchapter breakdown
- chapter draft from zero
- comparison with benchmark expectations and old attempt
- targeted revision

## File contract

When using a chapter workflow, create:

### Global files

- `00_master_outline.md`
- `01_assignment_board.md`
- `02_merged_report.md`
- `03_merge_notes.md`

### Per-chapter files

- `01_subchapter_breakdown.md`
- `02_chapter_draft.md`
- `03_chapter_comparison.md`
- `04_chapter_revision.md`

## Sequential fallback

If no multi-agent support is available, keep the same file contract and do the chapters one by one. The discipline matters more than true parallelism.

## Rewrite rule

If a chapter is structurally weak, write it from zero using:

- benchmark chapter logic
- current target-company materials
- current thesis

Do not treat the previous weak chapter as the default base text.

## Merge rule

After chapter revisions:

- unify wording
- remove duplicated claims
- restore transitions
- re-check financial wording
- re-check figure anchors
