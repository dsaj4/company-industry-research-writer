# Input Contract

Use this reference at the beginning of a run so the report starts from a stable brief instead of vague momentum.

## Minimum input set

Capture these items in `00_request.md`:

1. target object
2. task type
3. audience
4. expected deliverable
5. benchmark sample if any
6. source pack or materials available
7. constraints and deadlines

## Task types

Pick one primary mode:

- full company report
- industry landscape report
- chapter-only rewrite
- draft diagnosis and revision
- skill-upgrade review from human edits

If the task spans multiple modes, choose the primary one and note the secondary mode.

## Audience options

Record the main reader:

- internal research use
- investor-facing
- management briefing
- general professional audience
- technical audience

Audience affects compression, jargon tolerance, and how much context has to be surfaced.

## Deliverable options

Choose one main output:

- outline only
- full markdown report
- chapter revision
- review memo
- scorecard and next-action list
- skill upgrade note

## Benchmark handling

If a benchmark exists, capture:

- file or link
- what to imitate
- what must not be copied

If no benchmark exists, state the desired reference style in one line:

- equity-style
- institutional research memo
- strategy brief
- technical market analysis

## Source pack status

Choose the nearest fit:

- rich pack: materials already cover most core claims
- partial pack: enough to outline, not enough to finalize
- thin pack: requires deeper research before drafting
- draft-first: there is already a draft to review or rebuild

## Company-type declaration

Always declare one:

- listed company
- private company
- mixed comparison set

This controls financial wording and valuation discipline.

## Length and finish level

Record both:

- length target: short / medium / full
- finish target: rough / working / polished / final

Suggested default:

- full company report -> `full` + `polished`
- draft diagnosis -> `medium` + `working`
- chapter rewrite -> `medium` + `polished`

## Default assumptions when the brief is incomplete

If the user does not specify:

- audience: assume internal research use
- deliverable: assume full markdown report for full-report tasks, or review memo for diagnosis tasks
- benchmark: use the strongest local sample available
- company type: infer from materials; if unclear and valuation wording matters, use more cautious private-company wording
- finish level: assume polished, not final

## Startup summary

At run start, write a brief summary in `00_request.md` or `01_calibration.md` with:

- task type
- audience
- benchmark mode
- company type
- source-pack status
- whether deep research is triggered

Keep it concise. The goal is alignment, not ceremony.
