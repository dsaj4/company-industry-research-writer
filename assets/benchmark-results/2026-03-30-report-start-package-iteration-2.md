# Report-Start Package Benchmark Result

## Run identity

- Date: `2026-03-30`
- Eval: `report-start-package`
- Workspace path: `E:/Project/实习/公司研究/company-industry-research-writer-workspace/iteration-2/report-start-package/`
- Compared configurations:
  - `with_skill`
  - `without_skill`
- Benchmark version: rerun after tightening eval 1 assertions

## Result summary

- `with_skill`: `6/6` expectations passed
- `without_skill`: `4/6` expectations passed

## What changed from iteration 1

Iteration 1 produced `5/5 vs 5/5`, which meant the prompt and assertions were still rewarding answer completeness more than workflow discipline.

Iteration 2 changed the eval in four important ways:

1. it required a startup summary with six explicit fields
2. it required a real research-trigger decision rather than generic caution
3. it rewarded chapter-specific evidence jobs instead of vague figure placeholders
4. it kept the private-company boundary explicit

Those changes made the eval discriminate the skill more clearly.

## Why the with-skill run passed

- opened with a true startup summary
- stated source-pack status explicitly
- made a yes/no research-trigger decision and tied it to unstable valuation, revenue, traffic, and product-position claims
- separated calibration from thesis and outline
- decomposed the run into request, calibration, thesis, and outline artifacts
- kept the entire package framed as private-company research

## Why the baseline lost points

- did not open with a startup summary
- treated research as a generic caution rather than a triggered decision

The baseline still remained competent on the core content task:

- it named the benchmark
- it produced calibration
- it produced a thesis and six-question tree
- it assigned chapter-level figures
- it respected the private-company boundary

## Main interpretation

The tightened start-package eval now measures more than whether the model can answer a well-specified prompt.

It now measures whether the model behaves like a disciplined report workflow starter:

- classify the run
- state source-pack quality
- decide whether deeper research is triggered
- produce reusable run artifacts instead of only a one-shot answer

That is a much better fit for the skill's actual purpose.

## What this teaches about the skill

The skill's value in this eval is not just richer wording. The value is startup discipline:

- front-loaded framing
- research gating
- artifact decomposition
- private-company boundary control

## What this teaches about the benchmark design

This rerun validates the assertion tightening. The eval is now materially more discriminating and should stay in the core set.

## Operational note

- This run was executed inline in the current session, not through notification-backed subagents.
- Timing and token metrics therefore remain placeholders in the workspace timing files.
