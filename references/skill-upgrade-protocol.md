# Skill Upgrade Protocol

Use this reference when improving the skill from real report edits.

## Goal

Turn human edits into reusable writing and analysis rules without overfitting the skill to one project.

## Inputs

Prefer to compare:

- generated draft
- revised AI draft
- final human-approved version
- review notes or scorecard

## Diff categories

Classify every meaningful change into one of five buckets:

1. structure and chaptering
2. evidence and sourcing
3. argument and thesis strength
4. style and readability
5. formatting, figure anchors, and delivery shape

## Promotion rule

Promote a change into the skill only if one of these is true:

- it fixes a red-line error
- it improves a core analytical pattern
- it recurs across at least two different runs
- it is clearly a reusable report-quality heuristic

If a change is only about one company, one audience, or one editor's local preference, keep it as a case note instead of a global rule.

## Update order

Apply upgrades in this order:

1. fix red-line failures
2. fix thesis and structure
3. fix evidence usage
4. fix financial wording
5. fix style and formatting

## Where updates should go

- `references/report-framework.md`: reusable structural changes
- `references/evidence-financial-rules.md`: evidence discipline and wording changes
- `references/writing-style.md`: recurring style improvements
- `references/quality-scorecard.md`: new review checks
- `SKILL.md`: only when the top-level workflow or triggering rules change

## Required upgrade note

When a run yields meaningful edits, save `09_upgrade_notes.md` with:

- summary of the main gap
- diff category table
- reusable changes promoted
- case-specific changes not promoted
- new regression evals to add

## Regression mindset

If an important failure appears once, do not just patch the prose. Add a future test so the failure becomes hard to repeat.
