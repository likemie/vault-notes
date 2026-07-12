---
title: Attrition
aliases:
  - 流失
  - 实验流失
  - 样本流失
  - experimental mortality
  - attrition bias
  - 流失偏差
  - dropout
summary: "实验中参与者因各种原因中途退出导致组间不等价的内部效度威胁，退出者与留下者可能存在系统性差异，仅分析留守者会高估或低估干预效果"
type: concept
domain: "research-methodology"
related_count: 11
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - subject/research-methodology
  - experiment
  - bias-control
related_concepts:
  - "[[Internal Validity]]"
  - "[[Evaluation Research]]"
  - "[[Effect Size]]"
  - "[[Variable]]"
  - "[[Pre-test and Post-test]]"
related_methods:
  - "[[Random Assignment]]"
  - "[[Intent-to-Treat Analysis]]"
  - "[[Cross-sectional Study]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Random Sampling]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
status: draft
created: 2026-07-12
updated: 2026-07-13
---
# Attrition

## 定义

> [!def] 实验流失
> 实验流失（Attrition / Experimental Mortality）指在实验过程中参与者因各种原因中途退出，导致实验组和控制组不再等价，威胁[[Internal Validity|内部效度]]的现象。流失不是随机发生的——退出者与留下者通常存在**系统性差异**，仅分析留下者的数据会产生流失偏差（attrition bias）（Torgerson & Torgerson, 2003a, pp. 74–75; [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 333–334]]）。

> [!concept-lens] 流失在效度威胁中的位置
> - **含义** 流失不仅仅是"样本变小了"——它意味着实验组和控制组的构成在实验过程中发生了**系统性变化**，使[[Random Assignment|随机化]]建立的初始等价性被破坏。流失后的两组不再是"在其他方面完全相同"的，因此干预效应的估计可能被污染。
> - **用途** 识别和报告流失帮助研究者[[Evaluation Research|评估研究]]结论的稳健性——如果流失严重且退出者与留下者存在系统性差异，报告的[[Effect Size|效应量]]可能不能反映干预在原始样本中的真实效果。
> - **边界** 流失不等于排除偏差——排除偏差指参与者名义上在组内但从未实际接受干预，流失指参与者已开始实验但中途退出。流失也不等于小样本问题——小样本可能通过最小化策略应对，但流失改变了组的构成而非只是缩小了组。

---

## 核心要素

> [!feature] 流失偏差的三个关键机制
> - **退出者的系统性特征** 退出者通常不是随机子集——他们可能在动机水平、基线表现、家庭支持或其他关键[[Variable|变量]]上与留下者存在系统性差异。Torgerson & Torgerson (2003a, pp. 74–75) 给出的典型例子：参加自愿周六早间"加强班"的学生中，退出者可能本身动机水平就较低、学业基础更薄弱，排除他们会**高估**干预效果。
> - **组间不对称流失** 流失在实验组和控制组中可能不对称——干预组的流失率可能因干预本身的特征（如负担重、效果不明显）而高于控制组，导致两组在流失后不再可比。
> - **[[Effect Size|效应量]]扭曲** 如果仅分析留守者（completers-only analysis），效应量可能被高估（退出者是效果最差的）或被低估（退出者是效果最好的，因为已经"痊愈"）——方向和程度取决于退出者的特征和退出原因。
> - **应对策略** 招募大样本缓冲流失影响；比较退出者与留下者基线特征；采用[[Intent-to-Treat Analysis|意向治疗分析]]（ITT）按初始分组分析所有参与者；同时报告 completers-only 和 ITT 两种分析以评估流失偏差的严重程度。

> [!boundary]- 概念边界
> - 不等于排除偏差 — 排除偏差指参与者名义上在组内但从未接受干预，流失指已开始实验但中途退出。
> - 不等于小样本问题 — 小样本可通过最小化策略应对，但流失改变了组的构成而非只是缩小了组。
> - 不适用于[[Cross-sectional Study|横截面研究]] — 流失是纵向实验特有的威胁，单次测量的横截面研究中不存在。

---

## 应用案例

> [!case] 自愿周六加强班的流失
> Torgerson & Torgerson (2003a, pp. 74–75) 描述了一个周六早间数学加强班的 [[Randomised Controlled Trials|RCT]]：部分学生自愿报名参加，[[Random Assignment|随机分配]]至实验组（参加加强班）或控制组（不参加）。实验组的流失率较高——部分学生因各种原因（缺乏动机、家庭不支持、交通不便）在数周后退出。如果只分析坚持到最后的留守学生，实验组的[[Pre-test and Post-test|后测]]均值可能高于干预的真实效果——因为退出者本身就是动机最低、基础最薄弱的学生，他们留在数据中会降低实验组的平均表现。[[Intent-to-Treat Analysis|ITT]] 分析将退出者按初始分组纳入分析，给出干预效果的保守估计（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 333–334]]）。

> [!case] 减肥实验中的不对称流失
> 一项为期三个月的减肥实验将参与者随机分配至运动干预组和常规护理对照组。干预组中体重最重、效果最差的部分参与者在中期退出。如果仅分析干预组的留守者，干预效果会被高估——留守者是那些本身更容易减重的参与者。同时，对照组中没有类似的退出动机（他们只是在维持现状），因此对照组的留守者更接近原始[[Random Sampling|随机样本]]。两组流失的不对称使留守者之间的比较不再反映随机化建立的初始等价性。
