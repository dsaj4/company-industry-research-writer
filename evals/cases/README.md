# Eval Cases

This folder stores file-backed evaluation inputs.

Each case should provide enough context for a realistic skill run without depending on raw copyrighted PDFs.

Exception:

- benchmark-length calibration may reference a local `materials/*.md` extraction file, because that eval is meant to verify the local calibration pipeline itself.

Pair each case with the matching file under `../metadata/` when moving into a benchmark workspace.

## Current case types

- outline generation with benchmark calibration
- draft diagnosis with benchmark leakage
- weak-chapter rewrite from evidence pack
- benchmark-family selection when multiple samples exist
- benchmark-length calibration from local `.md` extraction
- Gate-C underfill audit using a benchmark profile

## Design rule

A case should test one primary capability at a time.

Good examples:

- can the skill preserve benchmark structure without shell copying
- can the skill detect listed-equity leakage in a private-company draft
- can the skill rebuild a weak chapter from evidence instead of patching it
- can the skill choose the right benchmark family and limit secondary borrowing

Keep one main capability per case so the expectations remain discriminating.
