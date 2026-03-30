# Benchmark Length Calibration Task

请把附带的 benchmark `.md` 纯文字提取版视为长度校准主源，而不是普通参考材料。

任务要求：

1. 先按内容功能把文档分成：
   - `cover/front-page`
   - `toc/index`
   - `body`
   - `detailed_financials`
   - `disclaimer/research-team`
2. 产出三层计数：
   - `raw_md_chars`
   - `clean_full_report_chars`
   - `transferable_body_chars`
3. 再按可迁移章节给出：
   - 各章字符数
   - 各章权重
4. 最后根据当前 skill 的强模仿比例，推导：
   - `short`
   - `medium`
   - `full`
   三档总预算和章节预算

禁止做法：

- 不要直接使用 PDF 页数或原始 PDF 总字符数
- 不要沿用旧的固定预算档位
- 不要把评级、目标价、详细财务预测壳计入 `transferable_body_chars`
