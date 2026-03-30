# Materials

This folder is for local raw inputs used during skill development.

## Expected contents

- broker reports
- benchmark PDFs
- target-company source packs
- screenshots or exported tables

## Tracking policy

Raw PDFs and local `.md` extraction files are treated as local working inputs and are ignored by git.

Reason:

- they may be copyrighted
- they are often large
- `.md` 提取版属于原始来源的派生文本，不应默认进入仓库
- the repository should track derived notes and reusable abstractions, not every raw source file

## What should be committed instead

- benchmark notes under `assets/`
- run artifacts under `runs/`
- derived checklists and references under `references/`
