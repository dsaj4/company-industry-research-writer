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
| Company overview | 月之暗面的入口、模型、平台和专业助手是怎样的一体化骨架？ | 官网、平台文档、GitHub、Playground、产品页 | 6438 | 7081 | 7725 | company-agent | planned |
| Industry / competition | 为什么这家公司既有窗口期，也面对更高平台化门槛？ | 同类 AI 应用与模型平台资料、用户/流量信号、竞品页 | 4665 | 5131 | 5597 | industry-agent | planned |
| Highlights / differentiation | 月之暗面最值得单独看的差异化主线是什么？ | 模型/产品/生态案例、Kimi+、MCP / 开发者信号 | 5890 | 6478 | 7067 | highlights-agent | planned |
| Commercialization / valuation boundary | 平台化抓手是否已形成，哪些地方还不能写成经营结果？ | 定价页、协议、Contact Sales、融资估值报道 | 1183 | 1302 | 1420 | commercialization-agent | planned |
| Risks | 什么会击穿 thesis？ | 竞争、兑现节奏、估值预期相关证据 | 233 | 257 | 280 | global | planned |

## Approval note

- 若要真正启动章节子 agent，需要先向用户明确申请授权。
- 若用户未批准，则保留同一份 assignment board，按 `orchestrated-sequential` 串行执行。
- 所有预算均来自 benchmark profile 派生，不允许后续手工重估。
