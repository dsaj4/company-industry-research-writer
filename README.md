# Company Industry Research Writer

This directory is the working `v1` of a reusable skill for writing company and industry research reports.

It is designed for two loops that reinforce each other:

1. Report execution loop: calibrate -> thesis -> outline -> evidence map -> draft -> score -> revise.
2. Skill upgrade loop: generated version vs final edited version -> diff review -> reusable rule extraction -> regression eval update.

This workspace is intentionally local-first. We improve it here before installing it into a global skills directory.

The skill now has two preservation layers:

1. analysis layer: thesis, chapter logic, evidence responsibility, valuation wording
2. style layer: opening density, chapter-opening pattern, argument compression, and risk-writing pattern distilled from current reports

It now also has two control layers for long-form work:

1. length-budget layer: total and chapter word budgets
2. orchestration layer: assignment board, approval gate, chapter execution, and merge

## Directory map

- `SKILL.md`: main skill entrypoint
- `references/`: rules loaded on demand
- `references/language-policy.md`: which layers should default to Chinese for Chinese research tasks
- `references/input-contract.md`: how to stabilize the brief at run start
- `references/length-budgeting.md`: how to turn soft length targets into total and chapter budgets
- `references/research-trigger.md`: when deeper research is required
- `references/summary-and-opening.md`: how to write strong openings and executive summaries
- `references/style-signatures.md`: benchmark-derived writing signatures from current broker reports
- `references/eval-benchmark-loop.md`: how to benchmark the skill against a baseline
- `references/benchmark-archetypes.md`: how to choose the right benchmark family when multiple samples exist
- `references/external-skill-borrow-map.md`: what to borrow from external skills and where to integrate it
- `references/external-skill-vetting.md`: safety and fit notes for external skills
- `assets/`: curated examples and future diff pairs
- `assets/benchmark-samples/`: distilled notes from benchmark reports
- `assets/style-samples/`: derived writing-pattern anchors from current research reports
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
