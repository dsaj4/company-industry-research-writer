# Grading Conventions

Use this reference when grading outputs from the skill's benchmark evals.

This file keeps grading compatible with the `skill-creator` schema while making the judgments stable for research-report writing tasks.

## Core principle

Grade what the output actually did, not what it seemed to be trying to do.

Use binary expectation grading:

- `passed: true` only when the expectation is materially satisfied
- `passed: false` when a required part is missing, weak, or contradicted

Do not award a pass for tone, effort, or partial intent.

## Required inputs

Before grading, read:

- `eval_metadata.json`
- the run output files under `outputs/`
- `timing.json` if present
- `metrics.json` if present
- the execution transcript when the evidence is ambiguous

Use the `assertions[].text` strings from `eval_metadata.json` as the source of truth for `grading.json`.

## Required `grading.json` structure

Use this shape:

```json
{
  "expectations": [
    {
      "text": "Explicitly names a primary benchmark and separates imitate-versus-different items before outlining.",
      "passed": true,
      "evidence": "01_calibration.md lists a benchmark choice and separates 'imitate' from 'must remain different'."
    }
  ],
  "summary": {
    "passed": 1,
    "failed": 0,
    "total": 1,
    "pass_rate": 1.0
  },
  "execution_metrics": {},
  "timing": {},
  "claims": [],
  "user_notes_summary": {
    "uncertainties": [],
    "needs_review": [],
    "workarounds": []
  },
  "eval_feedback": {
    "suggestions": [],
    "overall": "Optional benchmark-quality notes."
  }
}
```

The viewer depends on `expectations[].text`, `expectations[].passed`, and `expectations[].evidence`.

Keep those field names exact.

## Evidence standard

Evidence should be short, specific, and easy to verify.

Good evidence:

- names the file or section where the behavior appears
- explains why the expectation passed or failed
- cites the missing part when failing

Weak evidence:

- "Looks good"
- "Mostly there"
- "The draft is strong overall"

Prefer this pattern:

`<file or section> -> <observed behavior> -> <why it passes or fails>`

## How to grade composite expectations

Many expectations in this skill have two or more required parts.

Examples:

- `thesis plus chapter-level question tree`
- `choose one primary benchmark and constrain secondary borrowing`
- `rewrite from zero and explain what changed`

Grade these strictly:

- pass only if all required parts are materially present
- fail if one key part is missing

If useful, explain partial success in `evidence`, but keep the final verdict binary.

## How to handle anti-pattern expectations

Some expectations are really boundary checks.

Examples:

- avoid stock-rating wording
- avoid benchmark shell copy
- avoid listed-equity leakage

For these:

- pass only when the forbidden pattern is absent
- fail as soon as the output clearly violates the boundary

Do not offset a red-line failure with strengths elsewhere in the same output.

## Human review gates vs benchmark expectations

Keep these separate:

- benchmark expectations drive `pass_rate`
- human review gates judge benchmark quality and originality at a higher level

Do not force human review gates into `passed`/`failed` unless the eval explicitly turned them into an expectation.

When a run feels borderline even though expectation grading is decent, record that under:

- `user_notes_summary.needs_review`
- `eval_feedback.overall`

## Red-line handling

Treat these as major blockers when they appear:

- benchmark shell copy
- listed-equity or target-price leakage in the wrong company type
- unsupported core thesis claims
- missing benchmark calibration where the eval requires it
- patch-not-rewrite behavior in rewrite evals

When a red line appears:

1. Fail every affected expectation directly.
2. Mention the blocker clearly in `user_notes_summary.needs_review`.
3. Use `eval_feedback.suggestions` if the failure suggests a weak or missing assertion.

## Eval-specific guidance

### Eval 1: Report-start package

Look for:

- explicit benchmark calibration
- company type declaration
- central thesis
- chapter question tree
- chapter-level figure or evidence jobs

Fail if the output jumps straight into report prose or turns into a stock call.

### Eval 2: Draft diagnosis and red lines

Look for:

- dual-gate review first
- diagnosis of benchmark leakage with concrete evidence
- company-type-sensitive valuation wording review
- explicit block or no-block decision
- prioritized revision sequence

Fail if the output is mostly generic line editing.

### Eval 3: Chapter rewrite from evidence

Look for:

- chapter breakdown before prose
- evidence plan
- diagnosis of why the old chapter failed
- genuinely rewritten chapter
- explanation of what changed

Fail if the result is only a polished version of the old draft.

### Eval 4: Benchmark family selection

Look for:

- one explicit primary benchmark
- archetype-based justification
- narrow secondary borrowing only if needed
- non-transfer boundaries
- reusable calibration note

Fail if the output blends both benchmark families into a mixed shell.

## Summary math

Use:

- `passed`: count of expectations with `passed: true`
- `failed`: count of expectations with `passed: false`
- `total`: total expectation count
- `pass_rate`: `passed / total`

Do not exclude failed expectations because they felt subjective.

If an expectation is genuinely ungradable, explain why in `eval_feedback` and improve the eval later.

## When to write `claims`

Use `claims` for important factual or evaluative statements the grader wants to isolate.

Good candidates:

- "The output names MINIMAX as the primary benchmark."
- "The draft contains a target-price sentence."
- "The rewrite added a subchapter structure absent from the old draft."

This is optional, but useful when a benchmark result will be reviewed later.

## When to suggest eval improvements

Use `eval_feedback.suggestions` when:

- an expectation passes too easily in both configurations
- an expectation is too vague to grade consistently
- an expectation misses a recurring failure mode
- two expectations are duplicates in practice

The point is not only to grade runs, but also to improve the eval set over time.
