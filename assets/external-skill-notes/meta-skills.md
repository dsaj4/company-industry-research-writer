# Notes From Local Meta Skills

Sources:

- `C:/Users/Administrator/.codex/skills/skill-creator/SKILL.md`
- `C:/Users/Administrator/.agents/skills/skill-vetter-1.0.0/SKILL.md`

## Why they matter

These two local skills define the two meta-capabilities our research-writing skill needs:

- how to improve itself
- how to safely learn from outside skills

## `skill-creator`: most important takeaways

### 1. Benchmark the skill against a baseline

Do not assume the skill helps. Compare:

- with skill
- without skill or with old skill

### 2. Save eval prompts in a structured file

This is already started in `evals/evals.json` and should expand with real file-backed cases.

### 3. Keep an iteration workspace

Each iteration should preserve outputs, review notes, and grading data.

### 4. Turn observations into assertions

Not every quality dimension is machine-checkable, but factual and structural rules often are.

## `skill-vetter`: most important takeaways

### 1. Do not import external skills casually

Even text-heavy skills should be checked for:

- source credibility
- hidden scripts
- network actions
- unexpected file access

### 2. Classify the risk, not just the quality

A useful skill can still be risky. A safe skill can still be low-value.

### 3. Prefer borrowing patterns over blind installation

For this project, most external skills are best used as pattern libraries, not as direct dependencies.

## Concrete future upgrades inspired by these meta skills

1. create a real benchmark run folder
2. add assertions to `evals/`
3. keep vetting notes whenever we study a new external skill
