# MINIMAX Deep Extraction

## Source

- Local PDF in `materials/`
- Identifier:
  - GF Securities MINIMAX deep-dive report, dated `2026-02-10`
- Matching rule:
  - local file name contains `MINIMAX-WP` and `2026-02-10`

## One-line judgment

这篇样本最值得学的，不只是“AI 公司深度报告怎么排版”，而是它把一个高成长 AI 公司的 thesis 收成了清晰的推进链：

`模型能力 -> 产品矩阵 -> 商业化进展 -> 全球化验证 -> 预测/估值 -> 风险`

## Why this deeper extraction matters

旧版 benchmark note 解决的是“这篇报告值不值得学”。  
这一版深提取解决的是“到底该学它的哪一页、哪一章、哪种句法和哪类证据组织”。

对于后续模仿型 run，这一版更适合作为真正的 calibration 资产。

## Page-level map

### Front matter

- `P1` 首页：
  - 标题
  - 6 条左右核心观点
  - 财务摘要
  - 评级区块
- `P2` 目录索引
- `P3-P4` 图表索引与表格索引

### Main body

- `P5-P14` 公司概况
  - 发展历程
  - 管理层
  - 产品矩阵
  - 开放平台架构与定价
  - 财务分析
- `P15-P22` 行业分析
  - 技术进步
  - 市场空间
  - 竞争格局
- `P23-P31` 公司看点
  - 模型
  - 产品/商业化
  - 出海
- `P32-P33` 盈利预测与投资建议
- `P34` 风险提示

### Closing matter

- `P35` 财务报表与比率
- `P36-P37` 研究团队、评级说明、免责声明

## Front-page formula

这篇样本首页不是“摘要”，而是一个压缩版 thesis tree。

典型顺序是：

1. 先给公司定位句
2. 再给 2 到 3 条模型与产品判断
3. 再给商业化/全球化验证
4. 再给财务改善或预测
5. 最后补估值与风险

它的首页写法值得模仿的点：

- 不是把章节缩写成目录
- 而是把正文里最重要的判断提前释放
- 每条 bullet 都带一个证据方向
- 读者只看首页，就已经知道后文每章会证明什么

## What each chapter is really doing

### Company overview

表面上在写“公司是什么”，实际上承担 4 个任务：

1. 证明公司不是空壳概念，而是有时间线、有团队、有产品矩阵的主体
2. 先把产品和平台框架搭出来，为后文商业化铺路
3. 用价格、架构、产品截图把“能卖什么”写具体
4. 在同一章末尾接财务分析，让公司概况直接过渡到经营状态

这一章的关键不是信息多，而是“公司画像”和“业务骨架”要一次立住。

### Industry analysis

这一章不是泛行业背景，而是在回答：

- 为什么现在值得看大模型公司
- 为什么市场空间还在打开
- 为什么竞争尚未定型

它的结构非常标准：

1. 技术进步
2. 成本下降和空间扩张
3. 海外领先、国内追赶的格局

这让后面的公司看点不至于变成“脱离赛道的自夸”。

### Company highlights

这是全篇最值得学的一章。

它没有重复公司概况，而是把“为什么 MiniMax 值得单独看”单独拉了出来，按三条主线推进：

1. `模型`
2. `产品`
3. `出海`

每一条都不是空话：

- 模型：核心模型矩阵 + 第三方榜单/调用量
- 产品：收入结构 + 用户量 + 付费用户 + ARPPU
- 出海：海外产品表现 + 海外收入增长 + 区域拆分

这说明真正的“看点章”不是再讲一遍公司介绍，而是把最强差异化 thesis 拆成 2 到 3 条可验证主线。

### Forecast and recommendation

这一章的本质是把战略叙事翻译成经济语言。

它先拆业务，再给收入和毛利假设，最后才进入可比和 PS。

这个顺序很重要：

- 不是先估值，再找理由
- 而是先拆业务逻辑，再进入预测与估值

### Risks

风险页非常克制，只保留 3 条高相关风险：

- 研发投入大、成果转化不及预期
- 市场竞争
- 知识产权

这种写法说明，风险页不是凑数，而是只保留最可能击穿 thesis 的 failure path。

## Evidence architecture

这篇样本的证据不是平铺的，而是分层组织：

### Layer 1: company-owned evidence

- 招股书
- 官网
- 定价页
- 产品页面

### Layer 2: third-party market evidence

- Artificial Analysis
- OpenRouter
- 灼识咨询
- EPOCH AI

### Layer 3: operating proof

- 收入拆分
- 毛利率/费用率/净亏损率
- 用户量、MAU、付费用户、ARPPU
- 海外收入与区域拆分

### Layer 4: translation to economics

- 主营业务收入预测
- 可比公司估值表

最关键的经验不是“证据很多”，而是每一层证据都在承担明确章节职责。

## Figure and table responsibilities

这份样本的图表索引尤其值得学，因为图表不是点缀。

### Company overview anchors

- `图1` 发展历程
- `表1` 管理层
- `表2` 产品矩阵
- `图6` 开放平台技术与业务架构
- `表3/表4/表5` 定价与套餐

### Company financial anchors

- `图7-图12`
  - 收入
  - 业务拆分
  - 毛利
  - 成本结构
  - 费用率
  - 净亏损

### Industry anchors

- `图13-图18`
  - 技术发布时间线
  - 用户增长
  - 推理成本下降
  - 市场空间
  - OpenAI/Anthropic 商业化

### Highlights anchors

- `表9`
  - 核心模型矩阵
- `图22-图27`
  - 模型/视频/语音能力与排名
- `图28-图35`
  - 收入结构
  - 用户与 MAU
  - 付费用户
  - ARPPU
  - 海外收入

结论：

- 图表索引本身就是写作规划工具
- 在写正文之前就已经决定每章需要什么证据

## Style signatures worth imitating

### 1. Judgment-first

几乎每章开头第一段就先给判断，不先铺背景。

### 2. One chapter, one job

每章只回答一个核心问题，不互相抢任务。

### 3. Mechanism before slogan

不是只说“公司强”，而是说清：

- 为什么强
- 强在什么能力链
- 如何转化为商业结果

### 4. Numbers appear after the logic is framed

数字不是先堆出来，而是在判断成型后进入。

### 5. Risk is short and thesis-linked

风险页只保留最相关的断裂点，不写泛泛免责声明。

## Non-transferable parts

以下内容不能直接迁移到新报告：

1. 上市公司评级语言
2. `PS` 估值与目标价格逻辑
3. 财务报表和详细盈利预测壳
4. MiniMax 专有产品矩阵、用户数据和收入假设
5. `Pureplay` 上市 AI 公司视角下的可比公司表

## Translation rules for Moonshot-like private-company work

如果把这篇样本迁移到月之暗面这类非上市 AI 公司，建议做如下翻译：

### Keep

- 首页高密度核心观点
- 公司概况 -> 行业/竞争 -> 公司看点 -> 商业化边界 -> 风险 的大顺序
- 看点章里的 `模型/产品/平台/全球化` 推进方式
- 图表和证据先规划再写正文

### Replace

- 把 `盈利预测与投资建议` 改成 `商业化与估值边界`
- 把 `评级/目标价/PS` 改成
  - 已有商业化抓手
  - 尚未验证的部分
  - 资本预期与兑现门槛

### Remove

- 财务三表壳
- 公开股票评级
- 可比公司目标估值锚定

## Copy-ready benchmark takeaway

如果只压缩成一句可供新 run 调用的话：

> 模仿 MINIMAX，不是模仿“上市公司研报壳”，而是模仿它把 AI 公司写成“模型能力、产品矩阵、商业化进展与全球化验证”四条证据链共同支撑的高密度 thesis。
