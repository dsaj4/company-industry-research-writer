# Benchmark Length Profile Calibration V2

## What changed

这轮把 benchmark 的字数预算从固定档位改成了基于本地 `.md` 纯文字提取版的 profile 派生。

## New benchmark profiles

### MINIMAX

- `raw_md_chars`: `37652`
- `clean_full_report_chars`: `25892`
- `transferable_body_chars`: `25282`
- `full target`: `20858`

### Fourth Paradigm

- `raw_md_chars`: `52864`
- `clean_full_report_chars`: `38316`
- `transferable_body_chars`: `37623`
- `full target`: `31039`

## What this teaches about the skill

- 旧的 `full = 4500 / 6000 / 8000` 预算属于 memo 级，不足以约束 sell-side 风格深度报告。
- 现在可以先绑定 benchmark profile，再自动派生总预算和章节预算。
- `transferable_body_chars` 是更合适的私有公司模仿锚点，因为它剔除了评级、目标价和详细盈利预测壳。

## Regression on old Moonshot runs

### `20260330-163753_moonshot-formal-run`

- final count: `2815`
- against MINIMAX `full min 18962`: `14.85%`
- conclusion: severe underfill, should fail Gate C

### `20260330-183043_moonshot-minimax-minimal-run`

- final count: `2441`
- against MINIMAX `full min 18962`: `12.87%`
- conclusion: valid as minimal implementation, invalid as formal long-report final

## Next implication

新的 Moonshot 正式 run 必须先绑定 `MINIMAX` v2 profile，再自动生成 request、outline 和 assignment board；旧预算体系不再允许复用到正式深度报告。
