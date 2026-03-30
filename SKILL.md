---
name: company-industry-research-writer
description: Use when writing company research reports, industry deep dives, private-company analysis, equity-style report drafts, or redrafting a report to match a benchmark sample without turning it into a shell copy. Also use when reviewing a research draft for thesis quality, evidence quality, valuation wording, chapter structure, or when upgrading the writing workflow itself from final human edits.
---

# Company Industry Research Writer

Write research reports that feel structured, evidence-backed, and decision-oriented. The job is not to summarize materials. The job is to turn materials into a report with a clear thesis, chapter logic, evidence responsibilities, and explicit uncertainty boundaries.

## Load the right references first

Read only what is needed for the current task:

- New report from materials:
  - `references/language-policy.md`
  - `references/input-contract.md`
  - `references/length-budgeting.md`
  - `references/workflow-overview.md`
  - `assets/benchmark-profiles/*.json` when the task is benchmark-driven
  - `references/benchmark-archetypes.md`
  - `references/research-trigger.md`
  - `references/iteration-and-orchestration.md`
  - `references/report-framework.md`
  - `references/writing-style.md`
  - `references/style-signatures.md`
  - `references/summary-and-opening.md`
  - `references/evidence-financial-rules.md`
  - `references/quality-scorecard.md`
- Review an existing draft:
  - `references/language-policy.md`
  - `references/input-contract.md`
  - `references/length-budgeting.md`
  - `references/workflow-overview.md`
  - `references/quality-scorecard.md`
  - `references/evidence-financial-rules.md`
  - `references/style-signatures.md`
  - `references/iteration-and-orchestration.md`
- Rewrite one chapter or section from zero:
  - `references/language-policy.md`
  - `references/input-contract.md`
  - `references/length-budgeting.md`
  - `references/report-framework.md`
  - `references/writing-style.md`
  - `references/style-signatures.md`
  - `references/summary-and-opening.md`
  - `references/evidence-financial-rules.md`
  - `references/iteration-and-orchestration.md`
- Upgrade the skill from human edits:
  - `references/skill-upgrade-protocol.md`
  - `references/eval-benchmark-loop.md`
  - `references/grading-conventions.md`
  - `references/quality-scorecard.md`
  - `references/local-source-map.md`

## Non-negotiables

1. Imitate analytical method, not company-specific facts, numbers, or valuation conclusions from a sample report.
2. State the thesis before expanding evidence. Every chapter should answer a question that serves the thesis.
3. Separate confirmed facts, informed inferences, and working hypotheses. Do not flatten them into one confidence level.
4. Use source-appropriate financial wording. For private companies, do not casually convert financing valuations, target valuations, rumor valuations, revenue clues, and audited revenue into the same thing.
5. Give charts and screenshots an evidence job. Never treat them as decoration.
6. If a long report is underpowered chapter by chapter, rewrite chapters from zero instead of endlessly patching a weak whole draft.
7. When a fact cannot be confirmed, downgrade the wording instead of pretending certainty.
8. For Chinese research tasks, default to Chinese output unless the user explicitly asks for English or bilingual delivery.
9. For benchmark-driven `medium` and `full` deliverables, budgets must come from a benchmark profile rather than from fixed default word counts.
10. For full polished reports, default to orchestration discipline. If chapter subagents require explicit user approval and approval is not granted, switch to sequential fallback using the same assignment board.

## Standard workflow

### Step 0: Open a run folder

Create or update a run under `runs/<run_id>/` using the template in `references/workflow-overview.md`.

Before drafting, capture the brief using `references/input-contract.md`.

Write a short startup summary with:

- task type
- audience
- benchmark mode
- company type
- source-pack status
- whether deeper research is triggered
- output language
- benchmark profile, ratio band, and derived total budget
- subagent mode

If the report is benchmark-driven, bind the run to one profile under `assets/benchmark-profiles/` before thesis or outline work begins.

### Step 0.5: Decide whether deeper research is required

Use `references/research-trigger.md`.

If the task involves unstable facts, contested claims, valuation language, or an incomplete source pack, save a research pass before drafting.

### Step 1: Calibrate to the benchmark

Before drafting, write two short lists:

- Five things to imitate from the benchmark sample
- Five things that must remain different so this is a genuinely new report

This prevents shell-copy drift.

If multiple benchmark samples are available, choose the primary benchmark using `references/benchmark-archetypes.md`.

If the task is benchmark-driven, record:

- `transferable_body_chars`
- `counting_rules_version`
- `short / medium / full` ratio band
- derived total budget

### Step 2: Define the thesis and chapter question tree

Write:

- one central judgment
- three to six chapter-level questions
- one sentence on why this report is about this company or sector, not a generic market write-up
- the highest-priority evidence types for each chapter
- chapter weights and word budgets using `references/length-budgeting.md` and the bound benchmark profile

If the thesis is vague, stop and sharpen it before outlining.

### Step 3: Build the report skeleton

Default structure:

1. Title page
2. Core conclusions
3. Company overview
4. Industry analysis
5. Company highlights or competitive position
6. Commercialization, financial clues, and valuation discussion
7. Risks
8. Figure or source index when useful

Each chapter needs:

- one-sentence judgment
- question answered
- expected evidence
- planned figure anchors
- min/target/max word budget
- owner: global control or chapter execution

For `medium` and `full` reports, add a chapter budget table before prose starts.

For benchmark-driven reports, every chapter budget must be profile-derived rather than manually estimated.

### Step 3.5: Decide orchestration and request approval when needed

Use `references/iteration-and-orchestration.md`.

If the report is full or chapter-heavy:

- create an assignment board
- mark the run as `orchestrated-proposed`
- if actual subagents would be used, explicitly ask the user to approve the proposed chapter split before spawning them
- if approval is not granted, continue as `orchestrated-sequential` with the same chapter briefs

The global controller keeps:

- title and front page
- core conclusions
- overall thesis and budget ownership
- merge and style unification

### Step 4: Map evidence before prose

For each important claim, log:

- claim
- confidence tier
- source type
- exact source or file
- why it matters

If a claim has no support, weaken or remove it.

### Step 5: Draft in judgment-first form

Within each chapter and paragraph:

- open with the judgment
- explain mechanism or context
- support with facts, numbers, charts, or screenshots
- close with implication

For `medium` and `full` reports, do not write the whole report as one monolithic draft after budgets are declared.

Instead:

- draft chapter by chapter
- require each chapter to meet its minimum budget before merge
- merge into `05_draft.md` only after the controller checks coverage, duplication, and boundary wording

Use the orchestration pattern in `references/iteration-and-orchestration.md`.

Use `references/summary-and-opening.md` for:

- the opening page
- executive summary
- chapter openers
- dense concept translation

When prose finish matters, load one matching file under `assets/style-samples/` so the draft inherits real report moves instead of generic "professional tone."

### Step 6: Review with gates first

Before detailed scoring, answer:

1. Is this close to benchmark quality?
2. Is this clearly a new report with its own thesis and boundaries?
3. Does the report meet its declared total and chapter-level budget floor?

Also record:

- `budget_attainment_rate`
- `chapter_floor_pass_rate`

If any answer is no, do not waste time polishing sentences yet.

### Step 7: Score and revise by priority

Use `references/quality-scorecard.md`.

Fix in this order:

1. red lines and factual errors
2. thesis, chapter structure, and evidence gaps
3. financial wording and valuation boundaries
4. style, readability, and compression

After each revision round, log what changed and what remains unresolved.

### Step 8: Upgrade the skill from real edits

When both an AI-generated version and a final edited version exist:

- categorize the diff
- extract reusable changes
- promote only recurring patterns into references
- add a regression eval if the failure is important

Follow `references/skill-upgrade-protocol.md`.

If comparing versions, also use `references/eval-benchmark-loop.md`.

If grading benchmark outputs, also use `references/grading-conventions.md`.

## Output contract

Unless the user asks for something else, aim to save:

- `00_request.md`
- `01_calibration.md`
- `02_thesis.md`
- `03_outline.md`
- `orchestration/01_assignment_board.md` when applicable
- `orchestration/chapters/<chapter_id>/...` outputs when applicable
- `04_evidence_map.md`
- `05_draft.md`
- `06_review.md`
- `07_revision.md`
- `08_final.md`
- `09_upgrade_notes.md` when applicable

## Good defaults

- Prefer cautious, research-style wording over hype.
- Prefer one strong thesis over many weak themes.
- Prefer explicit uncertainty over fake completeness.
- Prefer source-linked claims over smooth but unsupported prose.
- Prefer reusable process notes over one-off taste changes when upgrading the skill.
- Prefer real benchmark-derived writing moves over abstract style adjectives.
