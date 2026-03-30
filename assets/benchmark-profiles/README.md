# Benchmark Profiles

This folder stores machine-friendly benchmark calibration assets derived from local `.md` text extractions in `materials/`.

Each profile should record:

- the local source markdown path
- raw markdown character count
- cleaned full-report character count
- transferable-body character count
- chapter counts and chapter weights
- ratio-derived total and chapter budgets

Tracking rule:

- commit the derived JSON profiles
- do not commit the local raw `.md` extraction files unless explicitly intended

Use `scripts/build-benchmark-length-profile.py` to rebuild these profiles from local materials.
