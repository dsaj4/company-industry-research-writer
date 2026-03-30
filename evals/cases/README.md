# Eval Cases

This folder stores file-backed evaluation inputs.

Each case should provide enough context for a realistic skill run without depending on raw copyrighted PDFs.

Pair each case with the matching file under `../metadata/` when moving into a benchmark workspace.

## Current case types

- outline generation with benchmark calibration
- draft diagnosis with benchmark leakage
- weak-chapter rewrite from evidence pack
- benchmark-family selection when multiple samples exist

## Design rule

A case should test one primary capability at a time.

Good examples:

- can the skill preserve benchmark structure without shell copying
- can the skill detect listed-equity leakage in a private-company draft
- can the skill rebuild a weak chapter from evidence instead of patching it
- can the skill choose the right benchmark family and limit secondary borrowing

Keep one main capability per case so the expectations remain discriminating.
