# External Skill Vetting Notes

This file applies the spirit of `skill-vetter` to the external skills we are learning from.

The goal is not just to ask whether they are safe to install. The goal is to decide whether they are safe and useful to borrow from.

## Vetting outcome summary

| Skill | Source | Files reviewed | Risk level | Verdict |
| --- | --- | --- | --- | --- |
| wechat-writer | ClawHub page | public skill page and listed file inventory | Medium | Safe to borrow patterns from; do not import blindly without rebuilding for our domain |
| doc-coauthoring | GitHub | `SKILL.md` | Low | Safe to borrow structural patterns from |
| article-review | GitHub | `SKILL.md` | Low | Safe to borrow specific writing heuristics from |

## 1. wechat-writer

### Source

- URL: https://clawhub.ai/wzdavid/wechat-writer

### What was reviewed

- the published skill page
- runtime workflow sections
- listed `references/` and `assets/` structure

### Useful observations

- strong separation between `references` rules and `assets` examples
- good handling of deep research triggers
- strong artifact persistence
- strong post-edit skill update loop

### Risk observations

- environment-specific tool references
- domain-specific style system aimed at WeChat-publication writing
- large style apparatus that could overfit us toward article writing rather than research writing

### Verdict

- safe to use as a structural benchmark
- not recommended for direct installation into this project as-is

## 2. doc-coauthoring

### Source

- URL: https://raw.githubusercontent.com/zephyrwang6/myskill/main/doc-coauthoring/SKILL.md

### What was reviewed

- the full `SKILL.md`

### Useful observations

- fast stage-based authoring loop
- section-by-section iteration discipline
- optional reader-testing stage
- explicit anti-pattern list for verbose writing

### Risk observations

- no executable scripts or suspicious operations visible
- workflow is conversation-heavy and may slow autonomous research work

### Verdict

- low risk
- useful as a guided rewrite pattern, especially for weak sections

## 3. article-review

### Source

- URL: https://raw.githubusercontent.com/zephyrwang6/myskill/main/article-review/SKILL.md

### What was reviewed

- the full `SKILL.md`

### Useful observations

- effective sequence for extracting hook, author context, core concept, key quotes, vivid reframing, and concluding lift
- useful for making dense material more readable without losing the center

### Risk observations

- no executable scripts or suspicious operations visible
- optimized for commentary and interpretation, not full formal research reports

### Verdict

- low risk
- useful as a micro-pattern source, not as a master template

## Borrowing policy

For this project:

- borrow structure, workflow, and upgrade patterns
- borrow selected readability heuristics
- do not borrow public-writing tone or article-growth mechanics unless explicitly needed

## Recheck trigger

Re-run vetting when:

- a new version of any source skill is considered
- we want to install instead of just reference
- a source starts including scripts, network actions, or credentials
