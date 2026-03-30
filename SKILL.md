---
name: company-industry-research-writer
description: Use when writing company research reports, industry deep dives, private-company analysis, equity-style report drafts, or redrafting a report to match a benchmark sample without turning it into a shell copy. Also use when reviewing a research draft for thesis quality, evidence quality, valuation wording, chapter structure, or when upgrading the writing workflow itself from final human edits.
---

# Company Industry Research Writer

Write research reports that feel structured, evidence-backed, and decision-oriented. The job is not to summarize materials. The job is to turn materials into a report with a clear thesis, chapter logic, evidence responsibilities, and explicit uncertainty boundaries.

## Load the right references first

Read only what is needed for the current task:

- New report from materials:
  - `references/input-contract.md`
  - `references/workflow-overview.md`
  - `references/benchmark-archetypes.md`
  - `references/research-trigger.md`
  - `references/report-framework.md`
  - `references/writing-style.md`
  - `references/summary-and-opening.md`
  - `references/evidence-financial-rules.md`
  - `references/quality-scorecard.md`
- Review an existing draft:
  - `references/input-contract.md`
  - `references/workflow-overview.md`
  - `references/quality-scorecard.md`
  - `references/evidence-financial-rules.md`
  - `references/iteration-and-orchestration.md`
- Rewrite one chapter or section from zero:
  - `references/input-contract.md`
  - `references/report-framework.md`
  - `references/writing-style.md`
  - `references/summary-and-opening.md`
  - `references/evidence-financial-rules.md`
  - `references/iteration-and-orchestration.md`
- Upgrade the skill from human edits:
  - `references/skill-upgrade-protocol.md`
  - `references/eval-benchmark-loop.md`
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

### Step 0.5: Decide whether deeper research is required

Use `references/research-trigger.md`.

If the task involves unstable facts, contested claims, valuation language, or an incomplete source pack, save a research pass before drafting.

### Step 1: Calibrate to the benchmark

Before drafting, write two short lists:

- Five things to imitate from the benchmark sample
- Five things that must remain different so this is a genuinely new report

This prevents shell-copy drift.

If multiple benchmark samples are available, choose the primary benchmark using `references/benchmark-archetypes.md`.

### Step 2: Define the thesis and chapter question tree

Write:

- one central judgment
- three to six chapter-level questions
- one sentence on why this report is about this company or sector, not a generic market write-up
- the highest-priority evidence types for each chapter

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

For long reports, prefer chapter-by-chapter drafting. Use the orchestration pattern in `references/iteration-and-orchestration.md`.

Use `references/summary-and-opening.md` for:

- the opening page
- executive summary
- chapter openers
- dense concept translation

### Step 6: Review with dual gates first

Before detailed scoring, answer:

1. Is this close to benchmark quality?
2. Is this clearly a new report with its own thesis and boundaries?

If either answer is no, do not waste time polishing sentences yet.

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

## Output contract

Unless the user asks for something else, aim to save:

- `00_request.md`
- `01_calibration.md`
- `02_thesis.md`
- `03_outline.md`
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
