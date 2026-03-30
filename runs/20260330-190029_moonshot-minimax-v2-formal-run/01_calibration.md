# Calibration

## Benchmark profile note

- Primary benchmark: `MINIMAX`
- Benchmark profile: `assets/benchmark-profiles/minimax-born-global-2026-02-10.json`
- Why this profile fits:
  - 月之暗面和 MINIMAX 都属于“模型能力 + AI 原生产品 + 平台输出”并存的 AI 公司研究对象
  - 两者都需要把“模型能力 -> 产品矩阵 -> 商业化抓手 -> 风险”写成连续链条
  - 月之暗面虽然不是上市公司，但仍适合借 MINIMAX 的前页压缩度和章节推进方式
- Why transferable body is the right budget anchor:
  - 月之暗面的正式长稿需要模仿 sell-side 正文密度
  - 但不能继承 MINIMAX 的评级、目标价、PS 和详细盈利预测壳
  - 因此预算锚点必须用 `transferable_body_chars`，而不是 raw `.md` 或 clean full report 全量
- Length band: `full`
- Ratio band: `75% / 82.5% / 90%`

## Five things to imitate

1. 首页写成压缩版 thesis tree，而不是目录摘要。
2. 每章只承担一个核心任务，不互相抢职责。
3. 按 `模型能力 -> 产品矩阵 -> 商业化抓手 -> 风险` 推进主线。
4. 在写正文前先确定图表 / 证据责任。
5. 风险页短而锋利，只保留最可能击穿 thesis 的 failure path。

## Five things that must remain different

1. 不使用上市公司评级、目标价和 PS 估值语言。
2. 不把 `Kimi` 写成等同于公司全貌，而是写成入口层。
3. 不把平台结构直接写成已验证经营结果。
4. 不照搬 MINIMAX 的全球化主线，月之暗面需要更重平台化与企业采用边界。
5. 竞争章节必须围绕国内 AI 应用、模型平台与开发者生态现实展开，而不是复述样本中的格局。

## Non-transferable shell

1. 首页财务摘要与评级区块
2. 详细盈利预测表
3. 目标价和 PS 估值结论
4. 面向股票投资建议的句式
