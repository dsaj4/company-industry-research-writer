# Eval Metadata

Each file in this folder is a richer grading companion for one eval.

Use these files when creating a benchmark workspace:

1. Copy the matching file into the run folder as `eval_metadata.json`.
2. Keep the `assertions[].text` strings stable so they can map cleanly into `grading.json`.
3. Use `grading_hint` to make grading more consistent across iterations.

The main `evals.json` stays lightweight and schema-friendly.

This folder carries the extra review context:

- descriptive eval name
- structured assertions
- human review gates
- common failure patterns to watch for
