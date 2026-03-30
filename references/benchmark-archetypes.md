# Benchmark 原型选择

当手头不止一份 benchmark 样本时，读取这份 reference。

这里要回答的问题不是“哪份样本更强”，而是“哪份样本更匹配目标公司的报告原型”。

## 核心规则

先选一个 primary benchmark。

如果确实需要，再从另一个 benchmark 借一个很窄的 secondary pattern。

不要把多个强 benchmark 混成一个臃肿 outline。

## 共享 backbone

当前 benchmark 集合里，以下骨架是共同成立且较强的：

1. 高密度前页
2. 公司概况
3. 行业分析
4. 差异化或亮点章节
5. 商业化、财务逻辑或估值讨论
6. 风险
7. 图表或表格规划

除非任务明确需要另一种形状，否则这就是默认应保留的骨架。

## 当前两类主要原型

### 原型 A：模型与产品驱动型 AI 公司

#### Primary benchmark

- `assets/benchmark-samples/minimax-born-global-2026-02-10.md`

#### 适用对象

- 模型驱动
- 消费产品驱动
- 全球产品驱动
- 使用量或产品 momentum 驱动

#### 它最值得借的模式

- `能力 -> 产品化 -> 商业化` 桥接
- 强公司亮点章节
- 产品截图与定价证据
- 使用量、市场 benchmark 类证据

### 原型 B：企业平台型 AI 公司

#### Primary benchmark

- `assets/benchmark-samples/fourth-paradigm-decision-intelligence-2024-12-03.md`

#### 适用对象

- 企业平台驱动
- 工作流或决策智能驱动
- 客户策略驱动
- 架构和解决方案驱动

#### 它最值得借的模式

- 平台中心的公司概况
- 对比型定位章节
- `先 challenge、后估值` 的章节节奏
- 客户与行业渗透类证据

## Secondary pattern 借用规则

只有当 secondary benchmark 提供了 primary benchmark 没有的特定模式时，才允许借用。

例如：

- 从原型 B 借 `challenge chapter`
- 从原型 A 借 `产品化到商业化桥接`

借用时必须满足三条：

1. 明确点名借的是什么
2. 保留 primary benchmark 的整体骨架
3. 不要把 secondary benchmark 的整套章节系统搬进来

## 不可迁移内容

对于任何上市公司 benchmark，默认不要继承以下内容：

- 评级语言
- 目标价
- 目标价值措辞
- 公司专属预测
- 公司专属业务拆分
- 完整公股财务报表机器

## 选择清单

在正式 drafting 前，先回答这五个问题：

1. 目标对象更偏模型驱动，还是更偏企业平台驱动？
2. 公司的故事更主要由产品使用驱动，还是由客户/解决方案架构驱动？
3. analogue/comparison chapter 会让 thesis 更清楚，还是会干扰它？
4. 这份报告是否需要在估值前先单列一个 challenge 章节？
5. 目标对象是上市公司还是非上市公司？

这五个答案共同决定 benchmark 选型。

## 输出要求

只要 benchmark 选型会影响结构，就在 `01_calibration.md` 里写一个短 note，至少包括：

- 选了哪个 primary benchmark
- 为什么选它
- 借了哪个 secondary pattern（如果有）
- 哪些内容不会迁移
