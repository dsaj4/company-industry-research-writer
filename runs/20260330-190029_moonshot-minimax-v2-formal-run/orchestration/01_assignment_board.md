# Assignment Board

## Mode

- Orchestration state: orchestrated-proposed
- Subagent approval required: yes
- User approval status: pending
- Benchmark profile: `assets/benchmark-profiles/minimax-born-global-2026-02-10.json`
- Length band: `full`

## Chapter assignment table

| Chapter | Question | Evidence pack | Min | Target | Max | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Company overview | 月之暗面的入口、模型、平台和专业助手是怎样的一体化骨架？ | `A01 A02 A04 A05 A08 B11` | 6438 | 7081 | 7725 | company-agent | brief-ready |
| Industry / competition | 为什么这家公司既有窗口期，也面对更高平台化门槛？ | `B14 B17` + DeepSeek / 豆包 / MiniMax 官方页 | 4665 | 5131 | 5597 | industry-agent | brief-ready |
| Highlights / differentiation | 月之暗面最值得单独看的差异化主线是什么？ | `A02 A04 A05 A08 B11 B15` | 5890 | 6478 | 7067 | highlights-agent | brief-ready |
| Commercialization / valuation boundary | 平台化抓手是否已形成，哪些地方还不能写成经营结果？ | `A03 A06 A07 B02 B03 B13 B24 B25` | 1183 | 1302 | 1420 | commercialization-agent | brief-ready |
| Risks | 什么会击穿 thesis？ | `B14 B17 B02 B03` + 竞品官方页 | 233 | 257 | 280 | global | brief-ready |

## Approval note

- 若要真正启动章节子 agent，需要先向用户明确申请授权。
- 若用户未批准，则保留同一份 assignment board，按 `orchestrated-sequential` 串行执行。
- 所有预算均来自 benchmark profile 派生，不允许后续手工重估。
- `04_evidence_map.md` 已完成，章节 brief 已进入可执行状态。
