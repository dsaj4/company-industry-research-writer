# Evidence And Financial Rules

This reference prevents the most common research-report failures: unsupported claims, blurred confidence levels, and incorrect financial wording.

## Confidence ladder

Every important claim should be tagged mentally as one of three levels:

### Confirmed fact

Definition:

- directly supported by an official document, company page, filing, transcript, or other high-confidence source

Wording:

- "the company disclosed"
- "the filing shows"
- "the pricing page lists"

### Informed inference

Definition:

- supported by multiple signals but not stated directly

Wording:

- "this suggests"
- "the available evidence indicates"
- "taken together, these signals imply"

### Working hypothesis

Definition:

- plausible but still under-verified

Wording:

- "we think"
- "it may indicate"
- "this remains to be confirmed"

## Source hierarchy

Prefer, in order:

1. official sources
2. audited or regulated disclosures
3. reputable third-party datasets
4. mainstream media or financing coverage
5. ecosystem signals such as GitHub, traffic, developer adoption, pricing proxies

If lower-tier sources are used for a critical claim, say so explicitly.

## Evidence map minimum

For each core chapter judgment, record:

- claim
- source
- source type
- confidence level
- implication

If a core claim has no credible source, rewrite or remove it.

## Benchmark-backed evidence classes

A strong AI company benchmark often combines several evidence classes in one report. Useful default buckets are:

1. company timeline and management tables
2. product screenshots and pricing tables
3. financial charts and business-split charts
4. third-party market and benchmark charts
5. comparable-company valuation tables

The lesson is not to force all five into every report. The lesson is that different chapter claims should be carried by different evidence types.

## AI company bridge rule

When writing about AI companies, do not jump directly from model capability to valuation.

Try to show the chain explicitly:

1. model or technical capability
2. product experience or product form
3. user, developer, or enterprise adoption
4. revenue, pricing, or commercialization signal
5. economic or valuation implication

If too many steps in this chain are missing, the report is overstating its confidence.

## Financial wording rules

### Listed companies

You may use:

- market capitalization
- audited revenue
- disclosed guidance
- reported margins
- standard valuation framing

### Private companies

Do not flatten these categories:

- completed financing valuation
- target valuation
- rumored valuation
- revenue clues
- audited revenue
- product pricing
- user or traffic proxies

When discussing a private company, make the category explicit every time it matters.

### Transfer guardrail for listed-company benchmarks

If the benchmark sample is a listed-equity report:

- its chapter structure may transfer
- its evidence density may transfer
- its rating and target-value language do not transfer automatically
- its full financial-statement projection machinery does not transfer automatically

The benchmark can teach report shape without dictating company-type wording.

## Red-line wording mistakes

Never:

- call a private-company valuation a market cap
- present target or rumored valuation as completed financing valuation
- present revenue clues as audited revenue
- present weak signals as proven facts
- cite a screenshot or chart that does not match the written claim

## Figure responsibility

Every figure should answer one question.

For each figure, note:

- what claim it supports
- where it appears
- what the reader should conclude from it

If the report is large, a figure or table index can be used as a planning artifact to make these responsibilities explicit before drafting.
