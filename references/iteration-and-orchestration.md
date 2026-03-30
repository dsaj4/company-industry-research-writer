# Iteration And Orchestration

Use this reference when the report is too large or too uneven to improve safely as one monolithic draft.

## When to switch modes

Switch from whole-draft editing to chapter orchestration when:

- the report is a `full` + `polished` company or industry deep dive
- the thesis is mostly right but chapters are thin or uneven
- some sections still feel like notes while others feel finished
- the report keeps getting patched without becoming stronger
- one chapter needs a from-zero rewrite

For full formal reports, orchestration is the default discipline, not a special rescue move.

## Main idea

Separate global control from chapter execution.

### Global control

Responsible for:

- thesis
- chapter weights
- chapter word budgets
- question tree
- evidence priorities
- assignment board
- subagent-approval state
- merge logic
- final style unification

### Chapter execution

Responsible for one chapter only:

- subchapter breakdown
- chapter draft from zero
- chapter-level self-review
- targeted revision
- chapter budget compliance

## File contract

When using a chapter workflow, create:

### Global files

- keep the standard run contract
- add `orchestration/01_assignment_board.md`
- keep `05_draft.md` as the merged whole-report draft
- keep `06_review.md` as the merged whole-report review
- use `07_revision.md` for whole-report revision notes after merge

### Per-chapter files

- `orchestration/chapter_template/01_subchapter_breakdown.md`
- `orchestration/chapter_template/02_chapter_draft.md`
- `orchestration/chapter_template/03_chapter_review.md`
- `orchestration/chapter_template/04_chapter_revision.md`

## Authorization gate

If true Codex subagents would be used, do not spawn them silently.

First:

1. finish thesis, outline, evidence priorities, and chapter budgets
2. write the assignment board
3. tell the user which chapters would be delegated and why
4. ask for explicit approval to launch those chapter agents

Then:

- if approval is granted, mark the run `orchestrated-approved`
- if approval is not granted or not available, mark the run `orchestrated-sequential` and execute the same chapter briefs one by one

## Sequential fallback

If no multi-agent support is available, or if user approval is not granted, keep the same assignment board and do the chapters one by one.

Do not collapse back into one giant whole-report draft. The discipline matters more than true parallelism.

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
- audit chapter and whole-report word budgets
- re-check financial wording
- re-check figure anchors
