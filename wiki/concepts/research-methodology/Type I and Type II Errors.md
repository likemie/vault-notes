---
title: Type I and Type II Errors
aliases:
  - 第一类错误
  - 第二类错误
  - Type I error
  - Type II error
  - false positive
  - false negative
  - 统计错误
summary: "统计推断中两类对称的决策错误——拒绝真零假设（第一类，冤枉无辜）和接受假零假设（第二类，放过有罪），两者之间存在内在权衡，在量化与质性研究中均有对应"
type: concept
domain: "research-methodology"
related_count: 12
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - method/research-methods
  - theme/validity
  - theme/statistics
related_concepts:
  - "[[Null Hypothesis]]"
  - "[[Hypothesis]]"
  - "[[Reliability]]"
  - "[[Internal Validity]]"
  - "[[Threats to Internal Validity]]"
  - "[[Sample Size Determination]]"
  - "[[Effect Size]]"
  - "[[Classroom Management]]"
  - "[[Confidence Interval]]"
  - "[[Causality]]"
related_methods:
  - "[[Qualitative Research]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10]]"
status: draft
created: 2026-06-23
updated: 2026-06-23
---
# Type I and Type II Errors

---

## 定义

> [!def] 核心定义
> 第一类错误（Type I error）和第二类错误（Type II error）是统计推断中两类对称的决策错误。**第一类错误**指拒绝了实际上为真的[[Null Hypothesis|零假设]]；**第二类错误**指接受了实际上不为真的零[[Hypothesis|假设]]。Mitchell & Jolley (1988: 121) 提供了一个直观类比：第一类错误相当于**冤枉无辜者（convicting an innocent person）**，第二类错误相当于**放过有罪者（finding a guilty person innocent）**。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|(Cohen et al., 2011, Ch. 10, pp. 165–166)]]

> [!concept-lens] 概念透镜
> - **含义** 两类错误是[[Null Hypothesis|零假设]]显著性检验（NHST）框架内生的不确定性来源——即使研究设计和执行完美无缺，统计推断本身仍然包含这两类错误的风险。它们不是研究者的操作失误，而是**统计决策的固有属性**。
> - **用途** 两类错误框架帮助研究者在设计阶段权衡显著性水平的选择（α 值），并在解释结果时评估结论的[[Reliability|可靠性]]——特别是在高风险决策情境中（如药物审批、教育政策评估）。
> - **边界** 在 Cook & Campbell 的效度框架中，两类错误属于**统计结论效度（statistical conclusion validity）**而非[[Internal Validity|内部效度]]——但 Cohen, Manion & Morrison (2011) 将其列为[[Threats to Internal Validity|内部效度威胁]]之一。在[[Qualitative Research|质性研究]]中，两类错误被重新解释为信念错误而非统计错误。

---

## 概念辨析

> [!contrast-table] 第一类错误 vs 第二类错误
> | 维度 | 第一类错误（Type I） | 第二类错误（Type II） |
> |---|---|---|
> | **定义** | 拒绝真的[[Null Hypothesis\|零假设]] | 接受假的零假设 |
> | **通俗类比** | 冤枉无辜者 | 放过有罪者 |
> | **概率符号** | α（alpha）——显著性水平 | β（beta）；1-β = 统计效力（power） |
> | **典型后果** | 宣称无效的干预有效 | 错失真正有效的干预 |
> | **教育案例** | 认为新教学法优于传统法，但实际无效——浪费资源推广无效方法 | 认为新教学法与传统法无差异，但实际有效——埋没了有价值的创新 |
> | **应对策略** | 降低 α（如 ρ < 0.01 而非 0.05） | 增大样本量提高统计效力，或降低 α 到 ρ < 0.20–0.30 |
> | **在[[Qualitative Research\|质性研究]]中的对应** | 相信了一个实际上不真实的陈述 | 拒绝了一个实际上真实的陈述 |

---

## 核心要素

> [!feature] 两类错误的关键特征
> - **内在权衡（Trade-off）** 减少第一类错误（降低 α）必然增加第二类错误的风险（降低统计效力），反之亦然。这不是方法论缺陷，而是统计推断的数学必然——在[[Sample Size Determination|样本量]]固定的条件下，两类错误概率无法同时最小化。
> - **显著性水平的选择（Choice of α）** 常规 α = 0.05 只是约定俗成，并非方法论的必然要求。研究者应根据研究的实际后果来选择适当的显著性水平：（a）如果推广无效干预的代价高昂（如医疗、高风险评估），应选择更严格的 α（如 0.01）；（b）如果错失有效干预的代价更高（如探索性研究），可适度放宽 α（如 0.10）。
> - **统计效力（Statistical power = 1-β）** 第二类错误的补充概念——研究正确拒绝假[[Null Hypothesis|零假设]]的概率。效力取决于样本量、[[Effect Size|效应量]]和 α 水平。Boruch (1997: 211) 指出第二类错误可能在以下情况发生：（a）对干预反应的测量效度不足；（b）干预的测量相关性不足；（c）实验统计效力太低；（d）选择了错误的研究总体。
> - **在[[Qualitative Research|质性研究]]中的重释（Qualitative counterpart）** 在质性数据中，第一类错误是相信了一个实际上不真实的陈述（过度信任数据），第二类错误是拒绝了一个实际上真实的陈述（过度怀疑数据）。这一区分提醒质性研究者：对数据的过度怀疑（拒绝真实）和过度信任（相信虚假）都是效度威胁。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|(Cohen et al., 2011, Ch. 10, pp. 165–166)]]

---

## 围绕概念形成的命题

> [!claim] 两类错误的权衡是研究设计的核心决策之一
> 在教育研究中，选择 α = 0.05 作为显著性阈值是一项**惯例**而非**方法论必然**。一项评估新教学法效果的研究——如果第一类错误意味着将无效方法推广至全区学校（浪费公共资源），而第二类错误意味着错过一个可能真正帮助学生的方法——研究者需要在这两种风险之间做出有意识的权衡，而非机械地遵循惯例。

> [!example] 两类错误权衡的教育案例
> **场景一：高成本干预评估**。一项评估某昂贵教育科技产品效果的研究。第一类错误→学区花费巨额资金购买无效产品；第二类错误→错失一个虽贵但有效的工具。在此场景中，第一类错误的代价可能更高——应选择更严格的 α。
>
> **场景二：低成本探索性研究**。一项评估课堂座位调整对注意力影响的小规模研究。第一类错误→教师尝试了一种无效但无成本的调整；第二类错误→错过了发现一个简单有效的[[Classroom Management|课堂管理]]策略。在此场景中，第二类错误的代价可能更高——可适度放宽 α。

---

## 争议与批评

> [!tension] NHST 框架内两类错误的局限
> - **α = 0.05 的任意性** 支持者认为 0.05 作为惯例提供了跨研究的可比性标准；批评者指出这一阈值缺乏方法论依据——Fisher 最初提出时并未意图将其固化为普适标准。不同类型的教育研究（探索性 vs. 确证性）可能需要不同的 α 水平。
> - **NHST 之外的替代框架** 贝叶斯统计提供了不同于两类错误框架的推断逻辑——不以"拒绝/接受[[Null Hypothesis|零假设]]"为核心，而以"更新信念的概率"为核心。[[Effect Size|效应量]]（effect size）和[[Confidence Interval|置信区间]]（confidence interval）的强调也是对 NHST 过度依赖的纠正——它们提供了比简单的"显著/不显著"二分更丰富的信息。
> - **在 Cook & Campbell 效度框架中的归属争议** Cook & Campbell 将两类错误归入统计结论效度而非[[Internal Validity|内部效度]]——认为它们是统计推断的问题而非[[Causality|因果推断]]的内部混淆问题。Cohen, Manion & Morrison 则将其列为[[Threats to Internal Validity|内部效度威胁]]。这一归属差异反映了对"效度"概念边界的不同理解。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|(Cohen et al., 2011, Ch. 10)]]
