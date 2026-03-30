# Benchmark-Family-Selection Benchmark Result

## Run identity

- Date: `2026-03-30`
- Eval: `benchmark-family-selection`
- Workspace path: `E:/Project/实习/公司研究/company-industry-research-writer-workspace/iteration-2/benchmark-family-selection/`
- Compared configurations:
  - `with_skill`
  - `without_skill`
- Benchmark version: rerun after tightening eval 4 assertions

## Result summary

- `with_skill`: `6/6` expectations passed
- `without_skill`: `4/6` expectations passed

## What changed from iteration 1

Iteration 1 produced `5/5 vs 5/5`. That showed the prompt already made the correct benchmark family obvious, so the old assertions mainly checked whether the answer was complete.

Iteration 2 tightened the eval by requiring:

1. explicit rejection of the non-primary benchmark as the main template
2. explicit anti-blend language prohibiting mixed chapter systems
3. narrowly scoped secondary borrowing
4. a copy-ready calibration note with named sections

Those changes turned benchmark-family selection from a multiple-choice-style task into a workflow-discipline task.

## Why the with-skill run passed

- chose `Fourth Paradigm` as one clear primary benchmark
- justified the choice with concrete archetype-fit criteria
- explicitly explained why `MINIMAX` should not be the main template
- limited secondary borrowing to one narrow commercialization bridge
- directly prohibited blending the two benchmark chapter systems
- ended with a reusable calibration note structured for `01_calibration.md`

## Why the baseline lost points

- it picked the correct primary benchmark, but did not reject the non-primary benchmark strongly enough as a main template
- it implied structure discipline, but did not include a direct anti-blend rule

The baseline still did several things well:

- chose the right benchmark family
- used enterprise-platform fit criteria
- limited secondary borrowing
- listed non-transfer boundaries

## Main interpretation

The family-selection eval now rewards the exact behavior the skill is supposed to teach:

- choose by archetype fit
- explain why the other benchmark is not the main shell
- prevent mixed-shell drafting before it happens
- write calibration notes that later stages can reuse directly

## What this teaches about the skill

The skill's advantage is not only "choosing the right sample." It is maintaining benchmark-boundary discipline:

- explicit non-primary rejection
- scoped borrowing
- anti-blend control
- reusable calibration artifacts

## What this teaches about the benchmark design

This rerun validates the tightened assertion set. Family selection is now a genuinely discriminating eval instead of an easy correctness check.

## Operational note

- This run was executed inline in the current session.
- Timing and token metrics remain placeholders because inline reruns do not capture subagent notification telemetry.
