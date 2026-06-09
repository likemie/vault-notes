---
title: Moderator Analysis
aliases:
  - 调节变量分析
  - 调节效应分析
summary: "元分析中识别和检验研究间效果变异来源的统计方法，通过探索哪些研究特征与更大或更小的效应量相关来解释异质性"
type: method
method_type: quantitative
tags:
- moderator-analysis
- meta-analysis
- heterogeneity
- effect-size
- methodology
related_concepts:
  - "[[Variable]]"
  - "[[Effect Size]]"
  - "[[Heterogeneity]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Meta-meta-analysis]]"
related_persons: []
related_arguments:
  - "[[Argument_Higgins_2016_RE]]"
confidence: medium
status: draft
created: '2026-06-08'
updated: '2026-06-08'
---

## 定义

> [!info] 定义
> 调节[[Variable|变量]]分析（Moderator Analysis）是[[Meta-analysis|元分析]]中用于识别和检验研究间[[Effect Size|效应量]]变异来源的统计方法。当元分析发现各研究的效果存在超出抽样误差预期的变异（即[[Heterogeneity|异质性]]）时，调节变量分析通过探索哪些研究特征与更大或更小的效应量相关，来解释这种变异的原因([[Argument_Higgins_2016_RE|Higgins, 2016, p.32]])。
>
> 调节变量（moderator）是指可能影响干预效果大小的研究特征，如学生学习的时长、培训和支持的重要性、特定资源的使用、学生年龄、结果测量类型等。通过在纳入研究的数据中寻找这些特征与效应量之间的相关性，调节变量分析试图回答"什么条件下效果更好"这一问题([[Argument_Higgins_2016_RE|Higgins, 2016, p.32]])。

---

## 核心程序

> [!example] 核心程序
> **1. 检测[[Heterogeneity|异质性]]**
>
> 在进行调节[[Variable|变量]]分析之前，首先需要确认研究间存在显著的[[Heterogeneity|异质性]]。如果各研究的[[Effect Size|效应量]]差异仅在抽样误差范围内，则无需进一步探索调节变量。
>
> **2. 选择候选调节变量**
>
> 基于理论或先前研究，选择可能解释异质性的研究特征作为候选调节变量。[[Argument_Higgins_2016_RE|Higgins (2016)]]举的例子包括学生学习的时长、培训和支持的重要性、以及特定资源的使用（p.32）。
>
> **3. 统计检验**
>
> 通过亚组分析或元回归等方法，检验候选调节变量与效应量之间的关系。例如，比较不同年龄段学生的效果差异，或检验结果测量类型是否与效应量大小相关。
>
> **4. 解释与报告**
>
> 报告哪些调节变量显著解释了异质性，并讨论其对实践的含义。

---

## 适用场景

> [!success] 适用场景
> - 当[[Meta-analysis|元分析]]发现研究间存在实质性[[Heterogeneity|异质性]]，需要理解变异来源时
> - 当实践者需要知道"什么条件下效果更好"而非仅知道"平均效果多大"时
> - Hattie（2015）主张元分析的价值不在于给出平均效应当作最终答案，而在于迫使教育者追问调节[[Variable|变量]]和竞争解释：哪些年龄、学段、文化、先前成绩和结果测量类型会改变效果([[Argument_Higgins_2016_RE|Higgins, 2016, p.42]])
> - 语音教学（phonics）的三项元分析得出不同的汇总[[Effect Size|效应量]]（0.41、0.27、0.30），部分原因就在于各元分析对调节变量的不同结论（如是否应在更年轻时开始语音教学、综合语音与分析语音孰优）([[Argument_Higgins_2016_RE|Higgins, 2016, p.32]])

---

## 局限性

> [!warning] 局限性
> - 调节[[Variable|变量]]分析往往统计效力不足（Valentine et al., 2010, cited in [[Argument_Higgins_2016_RE|Higgins, 2016, p.38]]），难以可靠地识别[[Heterogeneity|异质性]]来源
> - 当纳入研究数量有限时，调节变量分析的统计检验力较低，可能无法检测到真实的调节效应
> - 调节变量之间的交互作用难以在[[Meta-analysis|元分析]]框架中被充分建模
> - 在[[Meta-meta-analysis|元-元分析]]层面，每项一级元分析内部的调节变量信息在二级聚合时进一步丢失([[Argument_Higgins_2016_RE|Higgins, 2016, p.44]])

---

