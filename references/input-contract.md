# 输入契约

这份 reference 用于每次 run 的起点，让报告从一个稳定任务单开始，而不是从模糊动量开始。

## 最小输入集

在 `00_request.md` 里至少写清这几项：

1. 研究对象
2. 任务类型
3. 目标受众
4. 预期交付物
5. benchmark 样本（如果有）
6. 当前 source pack 或材料范围
7. 约束与截止时间
8. 输出语言
9. 篇幅档位
10. 完成度目标
11. 协作模式

## 任务类型

先选一个主模式：

- 完整公司深度报告
- 行业格局/专题报告
- 单章重写
- 旧稿诊断与修订
- 基于人工改稿的 skill 升级复盘

如果一个任务跨了多个模式，先写主模式，再标注次模式。

## 受众类型

记录主要读者：

- 内部研究使用
- 投资者阅读
- 管理层简报
- 一般专业读者
- 技术型读者

受众会影响：

- 压缩程度
- 术语容忍度
- 需要补多少背景解释

## 交付物类型

优先确定一个主交付物：

- 仅 outline
- 完整 markdown 报告
- 单章修订稿
- review memo
- scorecard 与 next actions
- skill 升级 note

## 语言要求

默认规则：

- 中文研报任务默认输出中文
- 标题、摘要、章节名、图表说明、风险提示默认用中文
- 若保留英文术语，优先“术语 + 中文解释”

仅在以下情况改为非中文：

- 用户明确要求英文
- 任务对象就是英文投资 memo
- 对外双语交付是明确需求

## Benchmark 处理

如果存在 benchmark，记录：

- 文件或链接
- 要模仿什么
- 什么不能复制

如果没有 benchmark，用一句话写期望参考风格：

- 券商深度风格
- 机构研究 memo
- 战略简报
- 技术市场分析

## Source pack 状态

四选一，取最接近的：

- rich pack：大部分核心主张都有材料支撑
- partial pack：足够出 outline，但不足以直接定稿
- thin pack：需要先做 deeper research
- draft-first：已经有旧稿，需要 review 或重构

## 公司类型声明

必须明确写一个：

- 上市公司
- 非上市公司
- 混合对比对象

这会直接影响财务措辞和估值纪律。

## 篇幅与完成度

这两项都要写：

- 篇幅档位：short / medium / full
- 完成度目标：rough / working / polished / final
- 总字数预算：min / target / max

如果是 `medium` 或 `full`，再补：

- 章节预算表：每章 min / target / max
- 协作模式：`single-agent / orchestrated-proposed / orchestrated-approved / orchestrated-sequential`

建议默认值：

- 完整公司报告 -> `full` + `polished` + orchestration discipline
- 旧稿诊断 -> `medium` + `working`
- 单章重写 -> `medium` + `polished`

默认预算从 `references/length-budgeting.md` 读取。

## 当 brief 不完整时的默认假设

如果用户没说清楚：

- 受众：默认内部研究使用
- 交付物：完整报告任务默认完整 markdown 报告，诊断任务默认 review memo
- benchmark：默认使用本地最强样本
- 公司类型：从材料推断；若不清晰且估值措辞敏感，优先用更谨慎的非上市公司措辞
- 完成度：默认 polished，不默认 final
- 输出语言：默认中文
- 协作模式：完整公司深度报告默认 `orchestrated-proposed`
- 字数预算：默认从 `references/length-budgeting.md` 取对应档位

## Startup summary

run 开始时，在 `00_request.md` 或 `01_calibration.md` 里写一个简短 summary，至少包括：

- 任务类型
- 受众
- benchmark 模式
- 公司类型
- source-pack 状态
- 是否触发 deeper research
- 输出语言
- 篇幅档位与总字数预算
- 协作模式

保持简短。目标是对齐，不是增加仪式感。
