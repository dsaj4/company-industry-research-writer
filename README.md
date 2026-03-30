# Company Industry Research Writer

This directory is the working `v1` of a reusable skill for writing company and industry research reports.

It is designed for two loops that reinforce each other:

1. Report execution loop: calibrate -> thesis -> outline -> evidence map -> draft -> score -> revise.
2. Skill upgrade loop: generated version vs final edited version -> diff review -> reusable rule extraction -> regression eval update.

This workspace is intentionally local-first. We improve it here before installing it into a global skills directory.

## Directory map

- `SKILL.md`: main skill entrypoint
- `references/`: rules loaded on demand
- `references/input-contract.md`: how to stabilize the brief at run start
- `references/research-trigger.md`: when deeper research is required
- `references/summary-and-opening.md`: how to write strong openings and executive summaries
- `references/eval-benchmark-loop.md`: how to benchmark the skill against a baseline
- `references/benchmark-archetypes.md`: how to choose the right benchmark family when multiple samples exist
- `references/external-skill-borrow-map.md`: what to borrow from external skills and where to integrate it
- `references/external-skill-vetting.md`: safety and fit notes for external skills
- `assets/`: curated examples and future diff pairs
- `assets/benchmark-samples/`: distilled notes from benchmark reports
- `assets/external-skill-notes/`: paraphrased notes from external and local meta skills
- `materials/`: local raw inputs such as PDFs; raw PDFs stay local and are not tracked
- `evals/`: prompt-level test cases for benchmark runs
- `evals/cases/`: file-backed evaluation fixtures
- `scripts/`: reusable helpers such as benchmark-workspace scaffolding
- `runs/`: saved run artifacts and upgrade notes

## Current source base

The first version is distilled from the local methodology under:

- `E:/Project/实习/公司研究/报告/workflow_docs/`
- `E:/Project/实习/公司研究/报告/chapter_session_workspace/`
- `E:/Project/实习/公司研究/示例/`

Use `references/local-source-map.md` to see how those local files map into this skill.
