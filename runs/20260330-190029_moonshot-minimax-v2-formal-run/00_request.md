# Request

## Startup summary

- Task type: 完整公司深度报告
- Audience: 内部研究与投资视角读者
- Benchmark mode: 单一主 benchmark，强模仿
- Benchmark profile: `assets/benchmark-profiles/minimax-born-global-2026-02-10.json`
- Company type: 非上市公司
- Source-pack status: partial pack
- Deeper research triggered: 是
- Output language: 中文
- Length band: full
- Ratio band: `75% / 82.5% / 90%`
- Derived total budget: `18962 / 20858 / 22754`
- Subagent mode: orchestrated-proposed

## Benchmark profile binding

- Counting rules version: `md-clean-transferable-v2`
- Source md path: `materials/广发证券-【广发计算机&海外】MINIMAX-WP（00100.HK）-Born-Global的稀缺全模态大模型公司-刘雪峰-公司深度研究-增持-2026-02-10-3.md`
- Raw md chars: `37652`
- Clean full report chars: `25892`
- Transferable body chars: `25282`

## Task

- 基于 `MINIMAX` 的 v2 deep extraction 与 length profile，为月之暗面创建新的正式长稿 run。
- 这轮先完成正式 run 起手包：
  - request
  - calibration
  - thesis
  - outline
  - assignment board
- 不复用旧的 Moonshot run 的预算体系，也不沿用旧的 request / outline 文案。

## Target object

- 月之暗面 / Moonshot AI

## Benchmark or reference sample

- `assets/benchmark-samples/minimax-born-global-2026-02-10-deep-extraction.md`
- `assets/benchmark-profiles/minimax-born-global-2026-02-10.json`

## Audience

- 需要判断月之暗面是否值得做正式深度覆盖的中文研究读者
- 关心 AI 公司研究框架、结构密度、商业化边界和风险路径的人

## Constraints

- 不套用上市公司评级、目标价和 PS 估值壳
- 不把融资估值、目标估值和经营结果混写
- 不把应用流量或平台框架直接写成收入已验证
- 正式长稿必须遵守 profile 派生预算，不能回退到旧的固定长稿字数
- 若需要拉章节子 agent，必须先向用户申请授权

## Expected deliverable

- 一套新的正式长稿起手包：
  - `00_request.md`
  - `01_calibration.md`
  - `02_thesis.md`
  - `03_outline.md`
  - `orchestration/01_assignment_board.md`

## Chapter budget plan

| Chapter | Min | Target | Max |
| --- | --- | --- | --- |
| Core conclusions | 554 | 609 | 664 |
| Company overview | 6438 | 7081 | 7725 |
| Industry / competition | 4665 | 5131 | 5597 |
| Highlights / differentiation | 5890 | 6478 | 7067 |
| Commercialization / valuation boundary | 1183 | 1302 | 1420 |
| Risks | 233 | 257 | 280 |
