# 语言策略

当这个 skill 用于中文公司研究、行业研究或研报改写时，默认把中文作为输出语言，而不是把中文当作翻译后的外壳。

## 核心原则

对于中文研报任务，语言不只是表达介质，也是分析风格的一部分。

如果流程层用英文、风格层用英文、最后只在成稿时“翻成中文”，通常会出现几个问题：

1. 句法像英文分析 memo，不像中文券商研报
2. 标题、章节名、风险提示的节奏不自然
3. 摘要和开篇容易变成翻译腔
4. 置信度表达不够像中文研究写法

因此，凡是直接影响成文语言、句法、章节命名、开篇和风险表达的 reference，优先使用中文约束。

## 默认规则

除非用户明确要求英文或双语：

- 报告正文默认用中文
- 标题、摘要、章节名、图表说明、风险提示默认用中文
- `00_request.md` 到 `08_final.md` 这些贴近写作的 run artifact，优先用中文
- 若必须保留英文术语，先保留专业名词，再补一句中文解释

## 必须强制中文的层

这些文件会直接塑造成文风格，建议强制中文：

- `references/writing-style.md`
- `references/style-signatures.md`
- `references/summary-and-opening.md`
- `references/input-contract.md` 中与输出语言、startup summary、章节命名相关的部分

当前已经转为中文主约束的结构与审稿层：

- `references/report-framework.md`
- `references/quality-scorecard.md`

## 不必强制中文的层

这些文件更像技能工程基础设施，不一定需要强制中文：

- `references/eval-benchmark-loop.md`
- `references/grading-conventions.md`
- `references/skill-upgrade-protocol.md`
- `scripts/`
- `README.md`
- `ROADMAP.md`
- `evals/metadata/*.json`

原因不是它们不重要，而是它们主要服务于：

- benchmark 设计
- grader 约定
- 仓库维护
- 技能升级流程

这些层只要语义稳定即可，不必为了中文化牺牲工程清晰度。

## 中间层的建议

有些文件不一定要“全中文强制”，但最好至少做到中文优先：

- `references/report-framework.md`
- `references/evidence-financial-rules.md`
- `references/benchmark-archetypes.md`
- `references/quality-scorecard.md`

原因：

- 它们会参与真实写作和审稿
- 它们决定章节名、结构判断、财务措辞、红线判断
- 如果长期保持英文，模型容易在中文成稿里保留英文分析骨架

目前其中 `report-framework.md` 和 `quality-scorecard.md` 已经完成中文主约束，后续更值得继续推进的是：

- `references/evidence-financial-rules.md`
- `references/benchmark-archetypes.md`

目前 `references/evidence-financial-rules.md` 也已经完成中文主约束，因此剩下最值得继续推进的是：

- `references/benchmark-archetypes.md`

## 实操规则

当任务是中文研报时：

1. 先读取中文风格层 reference
2. 再读取结构和证据层 reference
3. 写作时优先生成中文标题、中文判断句、中文风险表述
4. 只有在专业术语确实需要时才保留英文词

## 判断标准

如果一个 reference 会直接影响以下内容，就应该优先中文化：

- 标题怎么写
- 摘要怎么压缩
- 段落怎么起句
- 风险怎么收束
- 章节名怎么命名
- 置信度怎么表达

如果一个 reference 主要影响以下内容，则不必强制中文：

- benchmark 目录结构
- grader 字段规范
- JSON 约定
- 脚本使用方式
- 仓库工程说明
