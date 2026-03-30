# Eval Benchmark Loop

Use this reference when testing whether the skill improves outcomes over a baseline.

This file adapts the `skill-creator` evaluation mindset to research-report writing.

## Core principle

Do not assume the skill helps. Compare it against a baseline and inspect the difference.

## Baseline options

### New skill

Compare:

- with current skill
- without skill

### Improved skill

Compare:

- with new skill
- with previous skill snapshot

## Eval directory pattern

Recommended structure:

`company-industry-research-writer-workspace/iteration-N/<eval-name>/`

Inside each eval:

- `eval_metadata.json`
- `with_skill/`
- `without_skill/` or `old_skill/`

Inside each run folder:

- `outputs/`
- `grading.json`
- `timing.json`

Inside the skill repository:

- `evals/evals.json` should carry the prompt, source files, and benchmark-facing expectations
- `evals/metadata/*.json` should carry richer assertions, grading hints, and human review gates
- `evals/templates/grading-template.json` should provide the starter shape for each run's `grading.json`

Keep the expectation text stable across these files so grading stays comparable over time.

For exact `grading.json` writing rules, use `references/grading-conventions.md`.

## Good eval task types

Use a mix of:

1. full report outline generation
2. existing draft diagnosis
3. chapter-from-zero rewrite
4. valuation-language discipline check
5. benchmark-vs-original boundary control

## What to compare qualitatively

Look at:

- whether the report forms a real thesis
- whether it calibrates against the benchmark before drafting
- whether it separates confirmed facts from weaker claims
- whether it handles private-company valuation language correctly
- whether it uses chapter structure instead of material-dump structure
- whether a weak chapter is truly rebuilt rather than lightly patched

## Candidate assertions

Some important qualities are subjective, but these are often checkable:

- mentions benchmark calibration before outline
- includes a thesis or central judgment
- includes chapter-level questions or structure
- distinguishes listed/private company wording correctly
- mentions risks or uncertainty
- avoids forbidden wording such as private-company market cap where inappropriate
- uses evidence categories or source hierarchy

For this skill, prefer 4 to 6 expectations per eval:

- enough to discriminate useful behavior
- not so many that grading becomes noisy or redundant

Use descriptive expectation text that can be copied directly into `grading.json`.

## Human review gates

Each eval still needs a human pass on these two gates:

1. Is the output close to benchmark quality?
2. Is the output clearly a new report rather than a shell copy?

Quantitative checks should support this review, not replace it.

If a run has a decent pass rate but still feels benchmark-weak, record that in the grader notes rather than inflating the pass/fail counts.

## Timing and cost

Capture for each run:

- total tokens
- duration
- rough cost if available

Track whether gains in quality come with acceptable efficiency tradeoffs.

## Failure logging

When a run fails, record:

- what went wrong
- whether the failure is structural, factual, stylistic, or evaluative
- what reference should be updated
- whether a new regression eval is needed

## Promotion rule

Only upgrade the skill after you can explain:

- what specific failure occurred
- what change in the skill should prevent it
- how a future eval will verify that improvement

When a failure becomes recurring, add or strengthen:

- one expectation in `evals/evals.json`
- one richer assertion in `evals/metadata/*.json`
- one regression case if the current cases do not surface the failure reliably
