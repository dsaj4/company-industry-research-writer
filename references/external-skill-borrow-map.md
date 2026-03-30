# External Skill Borrow Map

This file records which external skills are worth learning from, what to borrow, what not to borrow, and where those ideas should land inside this workspace.

## Source set

External:

- `wechat-writer`: https://clawhub.ai/wzdavid/wechat-writer
- `doc-coauthoring`: https://github.com/zephyrwang6/myskill/tree/main/doc-coauthoring
- `article-review`: https://github.com/zephyrwang6/myskill/tree/main/article-review

Local meta skills:

- `skill-creator`: `C:/Users/Administrator/.codex/skills/skill-creator/SKILL.md`
- `skill-vetter`: `C:/Users/Administrator/.agents/skills/skill-vetter-1.0.0/SKILL.md`

## High-value borrow matrix

| Source | Borrowable pattern | Why it is valuable | Do not copy blindly | Best landing place |
| --- | --- | --- | --- | --- |
| wechat-writer | Mandatory `references + assets` loading before execution | Turns style and process constraints into runtime behavior instead of passive docs | Its module names and WeChat-publication-specific style stack are domain-specific | `SKILL.md`, future `references/runtime-loading.md` |
| wechat-writer | Explicit input template and fallback defaults | Reduces ambiguity at run start and makes drafting more stable | Its audience and article-length defaults do not fit research reports | future `references/input-contract.md`, run template |
| wechat-writer | Deep-research trigger based on topic recency and fact volatility | Strong fit for company and industry research | Its tool names are specific to that environment | future `references/research-trigger.md` |
| wechat-writer | Forced saving of intermediate artifacts | Very useful for later diff-driven upgrading | Its exact file names should be adapted to our research workflow | already partially in `runs/`, extend later |
| wechat-writer | Post-delivery `Step 8` that upgrades the skill from final edits | This is one of the best patterns for long-term self-improvement | Needs stricter promotion rules for research rigor | `references/skill-upgrade-protocol.md` |
| doc-coauthoring | Stage-based workflow: context -> structure -> reader test | Good lightweight interaction model | Too user-interactive for autonomous research drafting | chapter rewrite or guided mode |
| doc-coauthoring | Per-section brainstorm -> select -> write -> iterate | Useful for thin chapters and section rebuilding | Asking the user to choose every section would slow research work | `references/iteration-and-orchestration.md` |
| doc-coauthoring | Style preference capture before writing | Good if the user gives target report preferences | Should not override analytical rigor | future `references/input-contract.md` |
| article-review | Identify the public hook before deeper value | Useful for writing executive summary, intro, and chapter openers | Full social-media framing is too content-marketing oriented | future `references/summary-and-opening.md` |
| article-review | Translate dense concepts into plain language | Strong fit for research readability | Must not become over-simplification | `references/writing-style.md` or later summary guide |
| article-review | Quote strongest lines and then interpret them | Useful for expert quotes or source excerpts | Needs evidence discipline and citation care | future `references/summary-and-opening.md` |
| skill-creator | Baseline vs with-skill evaluation loop | Essential for proving the skill improves outcomes | Subjective writing quality still needs human review | `evals/`, later benchmark workflow |
| skill-creator | Iteration workspace and eval metadata | Good structure for repeatable improvement | Its full viewer flow may be heavier than we need at first | future `company-industry-research-writer-workspace/` pattern |
| skill-vetter | Source check and full-file review before adopting external skills | Prevents unsafe imports and low-quality cargo-culting | Low-risk text-only skills can still be useful as references | `references/external-skill-vetting.md` |
| skill-vetter | Risk classification and permission scope | Helps decide whether to install, reference, or avoid | Should not be treated as a one-time check | future import checklist |

## Recommended adoption order

### Priority 1: integrate soon

- runtime loading of `references + assets`
- research trigger and source hierarchy
- stronger run artifact persistence
- diff-driven skill upgrade loop
- baseline-vs-skill evaluation discipline

### Priority 2: integrate after first real benchmark runs

- input contract and fallback defaults
- chapter rebuild loop inspired by `doc-coauthoring`
- opening and summary heuristics inspired by `article-review`

### Priority 3: use cautiously

- user-choice-heavy coauthoring interactions
- highly stylized title or opening modules
- social-content framing patterns

## Recently integrated files

These borrow targets have now been added:

1. `references/research-trigger.md`
2. `references/input-contract.md`
3. `references/summary-and-opening.md`
4. `references/eval-benchmark-loop.md`

## Next likely integration targets

1. `references/runtime-loading.md`
2. `references/reader-friction-check.md`
3. file-backed eval cases under `evals/`
4. curated benchmark and diff-pair assets under `assets/`
