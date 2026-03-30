# Upgrade Notes

## Main gap

- The workspace had methodology docs but no first-class benchmark sample note tied to a real institutional AI report.

## Diff categories

### Structure and chaptering

- Added a real sample showing the standard company -> industry -> highlights -> valuation -> risks flow.

### Evidence and sourcing

- Added page-based anchors for where figure planning, summary logic, and valuation sections appear.

### Argument and thesis strength

- Clarified that a strong benchmark can still require adaptation boundaries.

### Style and readability

- Captured the sample's front-loaded judgment style as a reusable pattern.

### Formatting and figure anchors

- Captured figure and table index usage as a benchmark-strength pattern.

## Reusable changes promoted

- Use benchmark notes under `assets/benchmark-samples/`.
- Explicitly distinguish structural borrowing from valuation transfer.
- Treat figure indexes as evidence-planning tools.

## Case-specific changes not promoted

- MiniMax-specific products, metrics, and valuation assumptions.

## Regression evals to add

- A test that checks whether a generated report keeps the benchmark structure without copying the benchmark company's business split or stock-rating language.
