# Assignment Board

## Mode

- Orchestration state: orchestrated-approved
- Subagent approval required: yes
- User approval status: approved
- Benchmark profile: `assets/benchmark-profiles/minimax-born-global-2026-02-10.json`
- Length band: `full`

## Chapter assignment table

| Chapter | Question | Evidence pack | Min | Target | Max | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Company overview | 月之暗面的入口、模型、平台和专业助手是怎样的一体化骨架？ | `A01 A02 A04 A05 A08 B11` | 6438 | 7081 | 7725 | company-agent | completed-underfill |
| Industry / competition | 为什么这家公司既有窗口期，也面对更高平台化门槛？ | `B14 B17` + DeepSeek / 豆包 / MiniMax 官方页 | 4665 | 5131 | 5597 | industry-agent | completed-underfill |
| Highlights / differentiation | 月之暗面最值得单独看的差异化主线是什么？ | `A02 A04 A05 A08 B11 B15` | 5890 | 6478 | 7067 | highlights-agent | completed-floor-pass |
| Commercialization / valuation boundary | 平台化抓手是否已形成，哪些地方还不能写成经营结果？ | `A03 A06 A07 B02 B03 B13 B24 B25` | 1183 | 1302 | 1420 | commercialization-agent | completed-underfill |
| Risks | 什么会击穿 thesis？ | `B14 B17 B02 B03` + 竞品官方页 | 233 | 257 | 280 | global | drafted-floor-pass |

## Approval note

- 用户已批准章节子 agent，本轮按并行协作执行。
- 若后续轮次不再批准子 agent，则保留同一份 assignment board，按 `orchestrated-sequential` 串行执行。
- 所有预算均来自 benchmark profile 派生，不允许后续手工重估。
- `04_evidence_map.md` 已完成，四个章节 worker 已回稿，总控已进入 merge 与 Gate C 审阅阶段。
- 当前合稿已完成，但 Gate C 仍未通过；下一轮应优先补齐 `completed-underfill` 的三章。
