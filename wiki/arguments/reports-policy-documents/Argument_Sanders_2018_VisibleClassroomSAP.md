---
summary: "预设分队列意向治疗与免费校餐资格亚组分析，并因对照组缺少教师评分放弃最低评分组的因果比较"
type: "argument"
authors: ["Sanders, M.", "Carr, D.", "Ní Chonaire, A.", "Northcott, H."]
source_language: "en"
citation: "Sanders, M., Carr, D., Ní Chonaire, A., & Northcott, H. (2018). Statistical analysis plan: Visible Classroom. Education Endowment Foundation."
year: 2018
doi: ""
citation_aliases:
  - "Sanders et al., 2018"
  - "Sanders et al. (2018)"
isbn: ""
tags: ["eef", "visible-classroom", "teacher-professional-development"]
related_methods:
  - "[[Cluster Randomized Trials]]"
  - "[[Complier Average Causal Effect]]"
related_facts:
  - "[[Visible Classroom Programme]]"
related_arguments:
  - "[[Argument_Sanders_2021_EEF]]"
sources:
  - "[[sources/Sanders_2018_VisibleClassroomSAP|Sanders_2018_VisibleClassroomSAP]]"
status: "active"
created: "2026-10-28"
updated: "2026-10-28"
subtype: "report"
publication_type: "report"
title: "Argument_Sanders_2018_VisibleClassroomSAP"
argument_key: "Argument_Sanders_2018_VisibleClassroomSAP"
argument_display_title: "Statistical analysis plan: Visible Classroom"
argument_kind: "report"
argument_related_count: 4
argument_related_level: 0
argument_related_stars: "☆"
argument_related_color: "#dcfce7"
publisher: "Education Endowment Foundation"
issuing_organization: "Education Endowment Foundation"
---

---

> [!question]
> [[Visible Classroom Programme|可见课堂项目]]的分年级效果、依从分析与免费校餐资格亚组应如何估计，缺失资料和缺少对照评分如何限制结论？

> [!claim] 计划保留分队列随机比较，并限制缺少对照评分的教师亚组推断
> 统计分析计划日期为 2018 年 6 月 5 日，注册号 ISRCTN14774597。原五年级与原六年级队列分别分析，主要结局为数学与阅读原始分数之和；免费校餐资格亚组采用相同模型。教师评分最低三分之一的计划因对照组缺少评分而不能作因果比较。（pp. 1–3, 6–10）

> [!method-panel] 预设分析
>
> | 项目 | 规定 |
> | --- | --- |
> | [[Cluster Randomized Trials\|学校集群随机设计]] | 86 校随机进入干预 44 校、常规教学 42 校，按校级免费校餐比例、第一关键阶段成绩及名额准入方式分层。 |
> | 主要意向治疗分析（Intention-to-Treat Analysis，ITT） | 普通最小二乘回归控制分层及学生基线，标准误按学校聚类，报告 95% 置信区间；所有预设协变量保留。 |
> | 单科分析 | 数学、阅读分别按队列复用主分析模型。 |
> | 免费校餐资格亚组 | 国家学生数据库（National Pupil Database，NPD）的 EVERFSM_6_P 指标，按队列分别估计综合成绩效应。 |
> | 缺失结局 | 超过 5% 时分析缺失机制；符合计划条件时多重插补并逐步检查敏感性。 |
> | 缺失基线 | 有结局而无基线者按学校均值插补；缺少结局者不进入主分析。 |
> | [[Complier Average Causal Effect\|顺从者平均因果效应]]（Complier Average Causal Effect，CACE） | 至少两份反馈报告、即至少十次录课作为原依从标准；以随机分组为工具进行两阶段最小二乘估计。 |
> | 描述性扩展 | 拟使用干预教师评分作描述性剂量分析；教师实践调查探索自陈与学生成绩的关系。 |
>
> （pp. 3–10）

> [!sample-panel] 计划更新时的招募记录（表 2）
>
> | 入组队列 | 学校数 | 学生数 | 最小可检测效应 |
> | --- | ---: | ---: | ---: |
> | 原六年级 | 85 | 3,547 | 0.179 |
> | 原五年级 | 86 | 3,609 | 0.177 |
>
> 计划更新时记录合计 7,156 人（p. 6），最终报告记录入组 7,230 人；两者属于不同记录时点，不能把差额直接解释为流失。[[Argument_Sanders_2021_EEF|(Sanders et al., 2021, p. 15)]]

> [!ref-table]- 学校随机分层概况（表 1）
>
> | 分层变量 | 干预 | 对照 |
> | --- | ---: | ---: |
> | 免费校餐比例高于中位数 | 21 | 20 |
> | 免费校餐比例不高于中位数 | 21 | 21 |
> | 第一关键阶段成绩高于或等于中位数 | 20 | 20 |
> | 第一关键阶段成绩不高于中位数 | 22 | 22 |
> | 限额准入 | 5 | 6 |
> | 不限额准入 | 39 | 36 |
>
> 原表中位数标签存在边界交叠，且部分分层资料缺失，行和不全部等于 86 校；保留原表口径。（p. 4）

> [!boundary] 对照评分与实际执行限制预设分析
> - **教师最低评分组** 对照组没有教学准则评分，教师能力、动机与参与程度又可能影响评分，因此无法识别该组的干预因果效应。（pp. 9–10）
> - **剂量指标变更** 计划拟依据评分作描述性剂量分析，最终报告改用上传录课次数；报告依从门槛还增加第二年至少五次的路径。[[Argument_Sanders_2021_EEF|(Sanders et al., 2021, pp. 18, 36–37)]]
> - **时间记录** 计划称干预于 2017 年末开始（p. 2），最终报告时间表写 2016 年 9 月至 2018 年 6 月；实施时间采用最终报告。[[Argument_Sanders_2021_EEF|(Sanders et al., 2021, p. 21)]]

## 来源

- [[sources/Sanders_2018_VisibleClassroomSAP|Sanders_2018_VisibleClassroomSAP]]
