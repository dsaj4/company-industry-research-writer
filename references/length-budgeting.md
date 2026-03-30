# 篇幅预算

这份 reference 用于把“篇幅目标”从软约束改成 benchmark 派生的硬预算合同。

核心原则：

- 完整深度报告优先跟 benchmark 正文量级对齐，不再用固定字数拍脑袋。
- 预算单位统一为：`清洗后可见字符数（去空白）`。
- 对私有公司模仿上市 benchmark 时，预算锚点一律使用 `transferable_body_chars`，不是 raw PDF、不是 raw `.md`，也不是总页数。

## 预算模式

先判断任务是否属于 benchmark-driven：

### 1. Benchmark-driven 深度报告

适用于：

- 完整公司深度报告
- 行业/公司专题长稿
- 明确要求模仿券商深度样本的长稿

必须绑定：

- `assets/benchmark-profiles/*.json`

### 2. 非 benchmark 的短交付

只适用于：

- short memo
- review memo
- chapter opener
- 单章短改

只有这一类任务还能使用固定小预算。

## 计数字段

benchmark profile 至少记录：

- `benchmark_id`
- `source_md_path`
- `raw_md_chars`
- `clean_full_report_chars`
- `transferable_body_chars`
- `clean_full_chapter_counts`
- `transferable_chapter_counts`
- `chapter_weight_profile`
- `counting_rules_version`

## 计数口径

统一统计：

- 中文或中英混排正文里的可见字符
- 去除所有空格、换行和制表

### 计入

- 首页核心结论
- 正文标题
- 正文段落
- bullet 正文
- 图表解释语句
- 表格单元格中的正文
- 风险与边界表达

### 不计入

- 目录
- 图表索引 / 表格索引
- 页眉页脚
- 研究团队介绍
- 免责声明
- 详细财务附表

### Transferable 再剔除

在 `clean_full_report_chars` 的基础上，`transferable_body_chars` 继续删除：

- 评级语言
- 目标价
- PS / PE 等股票研究结论
- 详细盈利预测壳
- 纯股票 call block

## 比例档位

当前锁定：

- 预算模式：`纯 benchmark 比例`
- 模仿强度：`强模仿`

比例带固定为：

| 档位 | min | target | max |
| --- | --- | --- | --- |
| short | 35% | 40% | 45% |
| medium | 55% | 62.5% | 70% |
| full | 75% | 82.5% | 90% |

## 预算公式

### 总预算

```
total_budget = transferable_body_chars * ratio_band
```

### 章节预算

```
chapter_budget = total_budget * chapter_weight_profile
```

章节预算必须由 profile 自动派生，不允许手工拍数后再写进 run。

## `00_request.md` 必填字段

每次 benchmark-driven run 至少写：

- `Benchmark profile`
- `Counting rules version`
- `Source md path`
- `Raw md chars`
- `Clean full report chars`
- `Transferable body chars`
- `Length band`
- `Ratio min / target / max`
- `Derived total budget`

如果是 `medium` 或 `full`，还必须写：

- 章节预算表
- 协作模式

## `03_outline.md` 必填预算表

至少包含：

- 章节名
- 本章问题
- 证据责任
- `min / target / max`
- 负责人

## Gate C 审核口径

`06_review.md` 中的 Gate C 固定检查：

1. 总字数是否达到当前档位下限
2. 所有核心章节是否达到各自下限
3. 是否出现“前半程写满、后半程骨架化”
4. 是否存在单章超配，挤压了更重要章节的预算

需要同时给出两个指标：

- `budget_attainment_rate = actual_count / declared_target`
- `chapter_floor_pass_rate = 通过 floor 的核心章节数 / 核心章节总数`

## 默认小预算只保留给短交付

以下默认值只能用于非 benchmark 的短任务：

| 任务 | min | target | max |
| --- | --- | --- | --- |
| short memo | 1500 | 2200 | 3000 |
| review memo | 1200 | 1800 | 2400 |
| opener / very short rewrite | 600 | 900 | 1200 |

它们不得再用于完整深度报告。

## 预算不达标时怎么处理

### 情况 1：证据足够，但正文没展开

回到章节补写或重写，不进入 polish。

### 情况 2：证据不足，导致写不到预算

先补 research，或收窄本章问题，不要靠行业空话凑字数。

### 情况 3：总量够了，但后半程骨架化

这仍然视为未完成，因为 `chapter_floor_pass_rate` 不达标。

## Orchestration 规则

- 总控先根据 profile 派生总预算和章节预算
- assignment board 里的章节预算必须直接引用派生结果
- 章节 agent 只对自己的 `min / target / max` 负责
- 任何低于本章 `min` 的章节不得进入 merge

## 现阶段基准

当前已落盘的 profile：

- `assets/benchmark-profiles/minimax-born-global-2026-02-10.json`
- `assets/benchmark-profiles/fourth-paradigm-decision-intelligence-2024-12-03.json`

重新生成方式：

- `python scripts/build-benchmark-length-profile.py --benchmark minimax --pretty`
- `python scripts/build-benchmark-length-profile.py --benchmark fourth-paradigm --pretty`
