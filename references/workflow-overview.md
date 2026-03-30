# Workflow Overview

这份 reference 定义 skill 的默认 run contract。

## 核心目标

产出一份同时满足三件事的报告：

- 在结构和完成度上接近强 benchmark
- 明确是一份新报告，而不是套壳
- 在声明的深度上真正写够，而不是表面完成

## 两个循环

### 1. 报告执行循环

1. Request
2. Benchmark profile 绑定
3. Calibration
4. Thesis definition
5. Budgeted outline
6. Assignment and authorization when applicable
7. Evidence map
8. Chapter drafting
9. Merge
10. Review
11. Revision
12. Final delivery

### 2. Skill 升级循环

1. 对比生成稿与人工终稿
2. 分类改动
3. 决定什么可复用
4. 更新 references
5. 为重要失败补 regression eval

## 默认 run 目录

使用：

`runs/YYYYMMDD-HHMMSS_<topic>/`

推荐文件：

- `00_request.md`
- `01_calibration.md`
- `02_thesis.md`
- `03_outline.md`
- `orchestration/01_assignment_board.md`
- `04_evidence_map.md`
- `05_draft.md`
- `06_review.md`
- `07_revision.md`
- `08_final.md`
- `09_upgrade_notes.md`

## 关键约束

### New formal report

如果任务是 benchmark-driven 的 `medium / full` 报告：

- 必须先绑定 benchmark profile
- 必须先写 derived total budget 和 chapter budgets
- 完整报告默认走 orchestration discipline
- 真要拉 Codex 子 agent 时，先出 assignment board，再向用户申请授权

### Draft diagnosis

从 review 开始；如果 thesis 弱，就回退到 thesis 或 outline 层，而不是先做 line edit。

### Chapter-only rewrite

保留 chapter-level budget；如果该章本身属于长交付，就按章节 floor 审核。

## Gate C 在流程中的位置

任何进入 `08_final.md` 的稿件都必须通过：

- Gate A
- Gate B
- Gate C

其中 Gate C 负责判断：

- 写没写够
- 是否前半篇写满、后半篇塌缩
- 是否存在核心章节 underfill
