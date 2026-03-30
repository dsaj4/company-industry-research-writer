# Roadmap

This roadmap turns the current skill from a document-first `v1` into a testable and self-improving system.

## V1: Done

- skill skeleton created
- reusable references distilled from local workflow docs
- minimal eval prompt set created
- run directory contract defined

## V2: Benchmarkable

Priority:

1. add 2 to 3 curated benchmark assets under `assets/`
2. create one real run folder from the current project materials
3. expand `evals/evals.json` with concrete file-backed cases
4. draft qualitative and quantitative grading assertions
5. use `references/eval-benchmark-loop.md` to formalize baseline comparisons

Current status:

- first benchmark sample added:
  - `assets/benchmark-samples/minimax-born-global-2026-02-10.md`
- first benchmark seed run added:
  - `runs/20260330-093620_minimax-benchmark-seed/`
- second benchmark sample added:
  - `assets/benchmark-samples/fourth-paradigm-decision-intelligence-2024-12-03.md`
- second benchmark seed run added:
  - `runs/20260330-094538_fourth-paradigm-benchmark-seed/`
- first benchmark-cluster synthesis added:
  - `assets/benchmark-samples/ai-company-benchmark-cluster-v1.md`
- benchmark-selection reference added:
  - `references/benchmark-archetypes.md`
- first file-backed eval cases added:
  - `evals/cases/private-ai-outline-brief.md`
  - `evals/cases/private-ai-draft-with-benchmark-leakage.md`
  - `evals/cases/company-highlights-rewrite-pack.md`
- benchmark-family selection eval added:
  - `evals/cases/benchmark-family-selection-enterprise-platform.md`
- assertion-backed eval index added:
  - `evals/evals.json`
- richer grading metadata added:
  - `evals/metadata/eval-1-report-start-package.json`
  - `evals/metadata/eval-2-draft-diagnosis-and-red-lines.json`
  - `evals/metadata/eval-3-chapter-rewrite-from-evidence.json`
  - `evals/metadata/eval-4-benchmark-family-selection.json`
- grader convention reference added:
  - `references/grading-conventions.md`
- grading scaffold added:
  - `evals/templates/grading-template.json`
- first executed benchmark summary added:
  - `assets/benchmark-results/2026-03-30-report-start-package-iteration-1.md`
- second executed benchmark summary added:
  - `assets/benchmark-results/2026-03-30-draft-diagnosis-and-red-lines-iteration-1.md`
- third executed benchmark summary added:
  - `assets/benchmark-results/2026-03-30-chapter-rewrite-from-evidence-iteration-1.md`
- eval 1 and eval 4 assertions tightened after first benchmark pass:
  - stronger startup-summary and research-trigger requirements
  - stronger non-primary rejection and anti-blend requirements
- fourth executed benchmark summary added:
  - `assets/benchmark-results/2026-03-30-benchmark-family-selection-iteration-1.md`
- tightened reruns confirmed discrimination on the previously weak evals:
  - `assets/benchmark-results/2026-03-30-report-start-package-iteration-2.md`
  - `assets/benchmark-results/2026-03-30-benchmark-family-selection-iteration-2.md`
  - both moved from `5/5 vs 5/5` to `6/6 vs 4/6`
- first style-asset layer added from current GF report pages:
  - `references/style-signatures.md`
  - `assets/style-samples/gf-front-page-and-core-points.md`
  - `assets/style-samples/gf-chapter-opening-patterns.md`
  - `assets/style-samples/gf-argument-density-patterns.md`
  - `assets/style-samples/gf-risk-writing-patterns.md`

Exit condition:

- skill can be compared against a baseline on real report tasks

## V3: Diff-driven upgrading

Priority:

1. save generated draft vs final edited draft pairs
2. standardize `09_upgrade_notes.md`
3. promote recurring edits into references
4. add regression evals for major recurring misses
5. add style-focused evals for executive summary and chapter opener quality

Exit condition:

- final human edits reliably improve the skill instead of disappearing into chat history

## V4: Variant specialization

Potential variants:

- private-company deep dive
- listed-company equity-style report
- chapter-only rewrite and diagnosis
- industry-only landscape report

Exit condition:

- the skill can choose the correct variant without overloading one generic workflow

## New supporting references: Added

- `references/input-contract.md`
- `references/research-trigger.md`
- `references/summary-and-opening.md`
- `references/eval-benchmark-loop.md`

## V5: Light automation

Possible later additions:

- script to scaffold a benchmark workspace
- script to compare draft and final versions
- script to summarize upgrade notes across runs

Exit condition:

- repeated bookkeeping work is reduced without hiding analytical judgment
