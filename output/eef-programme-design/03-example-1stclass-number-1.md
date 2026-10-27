# 1stClass@Number 1 项目卡片样例

此样例依据 2026-10-27 本地网页快照制作，展示拟议的信息结构。评估 PDF 尚未阅读；本文件不作为正式项目条目或研究摘要。新卡片列结构与 `eef-outcomes` 样式尚待实现。

## 项目与实施

1stClass@Number 1 由 Edge Hill University 的 Every Child Counts 团队开发，面向需要额外数学支持的小学二年级学生。受训助教带领四人小组，每周开展三次、每次 30 分钟的活动，持续 10 周，与常规数学课堂并行。上述安排来自快照中项目页的 The programme 与 How is it implemented? 两节。

项目页同时说明培训、教师协调和准备时间要求。完整项目条目应进一步展开这些条件，并注明适用试验版本。

## 项目总览

> [!eef-programme] [1stClass@Number 1](https://educationendowmentfoundation.org.uk/projects-and-evaluation/promising-programmes/1stclass-number-1)
> 为小学二年级数学学习困难学生设计的 10 周小组干预，由受训助教实施。
>
> 数学 · 小学二年级 · 定向支持
>
> | 项目页影响 | 证据阶段 | 项目页证据强度 | 交付成本 |
> | --- | --- | --- | --- |
> | +2 个月 | 成效试验（effectiveness） | 4/5 | 约 £93／生／年 |
>
> **成本口径** 最近一次试验条件下的学校交付成本，按三年摊销估算，并假定每年向两组、每组四名学生实施。当前购买价格需另查提供方。
>
> **证据覆盖** 两次成效试验，各有结果记录。学生数和学校数按次列出。
>
> **出处** [EEF 项目页](https://educationendowmentfoundation.org.uk/projects-and-evaluation/promising-programmes/1stclass-number-1)，2026-10-27 网页快照。

## 评估记录

> [!eef-trials]- 两次成效试验
>
> | 评估页面 | 阶段与状态 | 页面所列完成时间 | 学生／学校 | 结果范围 | 页面证据强度 | 文件入口 |
> | --- | --- | --- | --- | --- | --- | --- |
> | [首次试验](https://educationendowmentfoundation.org.uk/projects-and-evaluation/projects/1stclassnumber) | 成效试验；已有结果 | 2018 年 7 月 | 532／130 | 数量推理，全体与免费校餐资格亚组 | 4/5 | [项目评估报告](https://d2tic4wvo1iusb.cloudfront.net/production/documents/projects/1stClass%40Number_evaluation_report.pdf) |
> | [第二次试验](https://educationendowmentfoundation.org.uk/projects-and-evaluation/projects/1stclass-number1-second-trial) | 成效试验；已有结果 | 2026 年 10 月，待核 | 1,880／235，口径待核 | 数学成绩，全体与免费校餐资格亚组 | 4/5 | [评估报告 v1.0.0](https://d2tic4wvo1iusb.cloudfront.net/production/documents/projects/1stClassNo.1_evaluation-report_v.1.0.0_2025-06-25-173138_pttn.pdf) |

完成时间与样本数均按快照中的评估页字段展示。报告链接去除抓取时的缓存参数，版本文件名保留。附件链接作为阅读入口，不表示已核对 PDF。

## 分组结果

> [!eef-outcomes]- 四条页面列示结果
>
> | 评估 | 指标 | 人群 | 额外进步月数 | 原始效应量 | 结果证据强度 | 显著性与说明 |
> | --- | --- | --- | --- | --- | --- | --- |
> | 首次试验 | 数量推理（Quantitative Reasoning） | 全体学生 | +2 | 未提供 | 4/5 | 结果文字明确主要结果未达统计显著 |
> | 首次试验 | 数量推理 | 享有免费校餐资格的学生 | 0 | 未提供 | 不适用 | 结构化结果评级为 N/A；结果文字另称该亚组结果安全性较低，保留差异待核 |
> | 第二次试验 | 数学成绩（Maths attainment） | 全体学生 | +2 | 0.12 | 4/5 | 页面摘要描述正向影响；所读文字未报告该项显著性检验 |
> | 第二次试验 | 数学成绩 | 享有免费校餐资格的学生 | +2 | 0.11 | 不适用 | 结果评级为 N/A；所读文字未报告该项显著性检验 |

各行未提供测量时点，正式处理时回查报告。效应量类型在当前结构化字段中没有标识，样例保留“原始效应量”列名。

## 核验事项

> [!eef-errata]- 页面字段与文字的差异
> - **学校数** 项目页 Were the settings in the trial(s) similar to my setting? 一节写最近试验为 226 所学校；第二次评估页 `metrics.schools` 为 235。保留两个值，待核两者是否使用不同样本口径。
> - **完成时间** 第二次评估页 `metrics.completed` 为 Completed October 2026；报告附件 `uploaded_at` 为 2025-06-25。两项字段含义与时间关系待核。
> - **首次试验亚组评级** 结构化行给出 N/A；Evaluation Conclusions 的文字称安全性低于全样本。两者分别保存，待核是否属于不同评级口径。
> - **核验层级** 已读项目页及两次评估页的导出文字与结构化结果，尚未阅读评估 PDF。

正式项目页还需交代首个试验在不同数学测量中的结果差别。Evaluation Conclusions 指出，主要数量推理测量的额外进步未转化为同样的阶段末数学测验收益；结果解释应保留测量对象与测验差异，不能只复述项目总览的 +2 个月。

## 本地数据定位

- 项目：`programmes` 中 `url` 末段为 `1stclass-number-1` 的对象；成本来自 What was the delivery cost? 一节。
- 首次试验：`trials` 中 `url` 末段为 `1stclassnumber` 的对象；结果来自 `trial_outcomes` 与 Evaluation Conclusions。
- 第二次试验：`trials` 中 `url` 末段为 `1stclass-number1-second-trial` 的对象；样本、时间与报告版本分别见 `metrics`、`documents`。
- 原始快照：`raw/EEF/EEF_promising_programmes_full .json`。
