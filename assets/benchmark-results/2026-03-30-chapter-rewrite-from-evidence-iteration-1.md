# Chapter-Rewrite-From-Evidence Benchmark Result

## Run identity

- Date: `2026-03-30`
- Eval: `chapter-rewrite-from-evidence`
- Workspace path: `E:/Project/实习/公司研究/company-industry-research-writer-workspace/iteration-1/chapter-rewrite-from-evidence/`
- Compared configurations:
  - `with_skill`
  - `without_skill`

## Result summary

- `with_skill`: `5/5` expectations passed
- `without_skill`: `4/5` expectations passed

## What separated the two sides

The discriminator was not whether a decent rewritten chapter could be produced.

Both sides could:

- identify what the old draft was missing
- produce a cleaner rewritten chapter
- use the supplied evidence pack
- explain that commercialization evidence is weaker than product-identity evidence

The actual separator was whether the rewrite followed a chapter-first planning discipline.

### With-skill advantage

- opened with request capture and chapter purpose
- wrote the chapter job and rewrite target explicitly
- created a subchapter structure before prose
- mapped evidence before drafting
- preserved a full rewrite loop through draft, review, revision, final, and upgrade notes

### Baseline limitation

- gave a quick critique
- then jumped directly into rewritten prose
- did not show an explicit subchapter breakdown and evidence plan first

## Main interpretation

This eval is another good discriminator for the skill.

It is especially useful because it tests a workflow behavior that is easy for a baseline to skip:

- plan the chapter
- define the evidence burden
- then rewrite

That is more structurally meaningful than simply asking for "a better chapter."

## What this teaches about the skill

The skill is showing clear value on tasks where order matters:

- planning before drafting
- separating evidence strength by claim type
- rebuilding weak sections from first principles rather than polishing generic text

## What this teaches about the eval set

The stronger evals so far are the ones where the skill's advantage comes from process discipline:

- explicit dual-gate review
- explicit chapter-first rewrite planning

This suggests future benchmark design should keep emphasizing:

- workflow ordering
- confidence boundaries
- non-transfer guardrails

rather than only checking whether requested sections appear.

## Operational note

- This run was executed in the local workspace through a delegated subagent.
- Timing and token metrics remain placeholders because the current setup does not persist those notifications into the workspace automatically.
