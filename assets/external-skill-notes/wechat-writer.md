# Notes From `wechat-writer`

Source:

- https://clawhub.ai/wzdavid/wechat-writer

## Why it matters

This is the strongest external reference for turning a writing skill into an operational system instead of a loose prompt.

## Best patterns to borrow

### 1. Load `references + assets` before doing anything

The skill makes runtime loading explicit:

- rules come from `references/`
- style anchoring comes from `assets/`

For our research skill, the equivalent is:

- method comes from `references/`
- benchmark samples and diff pairs come from `assets/`

### 2. Force a short runtime constraint summary

The skill requires a short summary of active writing constraints after loading references and assets.

Research adaptation:

- write a short calibration summary at the start of each run
- include benchmark target, report type, thesis mode, company type, and evidence posture

### 3. Trigger deep research explicitly

The skill does not search casually. It defines when deeper research is required.

Research adaptation:

- trigger deeper research for volatile facts, contested narratives, new products, private-company estimates, and multi-source comparisons

### 4. Save all intermediate artifacts

One of the most reusable ideas:

- request
- research
- topic options
- outline
- draft
- edited draft
- final

Research adaptation:

- our current `runs/` design already follows this direction and should be extended

### 5. Upgrade the skill from the final edited version

This is the most important long-term pattern.

Research adaptation:

- compare generated report vs final approved report
- classify changes
- promote recurring changes only
- add regression evals

## What not to borrow

- public-account title module system
- highly stylized opening and ending modules
- platform-specific formatting assumptions
- tone choices designed for content marketing or traffic growth

## Concrete future upgrades inspired by this skill

1. add `references/research-trigger.md`
2. add `references/input-contract.md`
3. add a short startup calibration summary requirement to `SKILL.md`
4. create a diff review routine inside `09_upgrade_notes.md`
