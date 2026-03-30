# Iteration And Orchestration

当报告太长、太不均衡，或需要按 benchmark profile 严格分配预算时，使用这份 reference。

## 什么时候切换

以下情况默认进入 orchestration discipline：

- benchmark-driven 的 `full` 报告
- benchmark-driven 的 `medium` 长稿且章节数较多
- thesis 大体正确，但章节明显失衡
- 前半程较完整、后半程仍像提纲
- 某一章必须从零重写

## 主体角色

### 总控

负责：

- thesis
- benchmark profile 绑定
- total budget
- chapter budgets
- question tree
- evidence priorities
- assignment board
- subagent approval 状态
- merge
- final style unification

### 章节执行

每个章节只负责自己一章：

- subchapter breakdown
- chapter draft from zero
- chapter self-review
- chapter revision
- chapter budget compliance

## 预算规则

- assignment board 里的章节预算必须来自 profile 派生
- 不允许先手工写章节预算，再回头“贴 profile”
- 任何低于本章 `min` 的章节不得进入 merge
- merge 前后都要做 budget audit

## 文件契约

### Global files

- 保留标准 run 文件
- 新增 `orchestration/01_assignment_board.md`
- `05_draft.md` 保留合并后的完整稿
- `06_review.md` 保留整稿 review

### Per-chapter files

- `orchestration/chapters/<chapter_id>/01_subchapter_breakdown.md`
- `orchestration/chapters/<chapter_id>/02_chapter_draft.md`
- `orchestration/chapters/<chapter_id>/03_chapter_review.md`
- `orchestration/chapters/<chapter_id>/04_chapter_revision.md`

## Authorization gate

如果要真正拉 Codex 子 agent：

1. 先完成 thesis、outline、evidence priorities 和 chapter budgets
2. 先写 assignment board
3. 明确告诉用户哪些章节会被分派、为什么这样分
4. 用户批准后，才能真正启动子 agent

然后：

- 批准后，标记为 `orchestrated-approved`
- 未批准或不方便批准，标记为 `orchestrated-sequential`

## Sequential fallback

即使没有多 agent 支持，也要保留同一套 chapter brief 和 budget table，逐章串行执行。

不要因为没并行起来，就退回“一口气写整篇”的旧模式。

## Merge rule

合稿时必须做：

- 去重同义判断
- 统一标题粒度
- 统一置信度措辞
- 统一平台 / 商业化 / 风险边界表达
- 预算审计
- figure anchor 复核
