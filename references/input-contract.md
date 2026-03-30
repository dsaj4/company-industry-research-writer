# 输入契约

这份 reference 用于每次 run 的起点，让报告从稳定任务单开始，而不是从模糊动量开始。

## 最小输入集

在 `00_request.md` 里至少写清：

1. 研究对象
2. 任务类型
3. 目标受众
4. 预期交付物
5. benchmark 样本
6. benchmark profile
7. 当前 source pack
8. 约束与截止时间
9. 输出语言
10. 篇幅档位
11. 完成度目标
12. 协作模式

## benchmark-driven 报告必填

如果任务是 benchmark-driven 深度报告，还必须写：

- `Benchmark profile`
- `Counting rules version`
- `Source md path`
- `Raw md chars`
- `Clean full report chars`
- `Transferable body chars`
- `Length band`
- `Ratio min / target / max`
- `Derived total budget`

如果是 `medium` 或 `full`，再补：

- 章节预算表
- 协作模式：`single-agent / orchestrated-proposed / orchestrated-approved / orchestrated-sequential`

## 任务类型

先选一个主模式：

- 完整公司深度报告
- 行业格局 / 专题报告
- 单章重写
- 旧稿诊断与修订
- 基于人工改稿的 skill 升级复盘

## 受众类型

记录主要读者：

- 内部研究使用
- 投资者阅读
- 管理层简报
- 一般专业读者
- 技术型读者

## Benchmark 处理

如果存在 benchmark，记录：

- 文件或链接
- primary benchmark
- scoped borrowing
- 什么必须不同
- 什么不能复制

如果没有 benchmark，用一句话写期望参考风格。

## Source pack 状态

四选一：

- rich pack
- partial pack
- thin pack
- draft-first

## 公司类型声明

必须明确写一个：

- 上市公司
- 非上市公司
- 混合对比对象

## 篇幅与完成度

两项都要写：

- 篇幅档位：`short / medium / full`
- 完成度目标：`rough / working / polished / final`

如果是 benchmark-driven 深度报告：

- 总预算来自 profile 派生
- 章节预算来自 profile 的 `chapter_weight_profile`

只有非 benchmark 的短任务才允许直接使用固定小预算。

## 默认假设

如果用户没说清楚：

- 受众：默认内部研究使用
- 交付物：完整报告默认 markdown 报告
- benchmark：默认用本地最强样本
- 公司类型：若不清晰且估值敏感，优先按非上市公司措辞
- 完成度：默认 polished
- 输出语言：默认中文
- 协作模式：完整公司深度报告默认 `orchestrated-proposed`
- 预算：benchmark-driven 任务默认从 profile 派生，不再回退到固定长稿预算

## Startup summary

run 开始时，在 `00_request.md` 里至少写：

- 任务类型
- 受众
- benchmark 模式
- benchmark profile
- 公司类型
- source-pack 状态
- 是否触发 deeper research
- 输出语言
- 篇幅档位
- ratio band
- derived total budget
- 协作模式
