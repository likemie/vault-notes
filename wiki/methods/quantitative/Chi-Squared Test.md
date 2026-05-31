---
title: Chi-Squared Test
aliases:
  - 卡方检验
  - 卡方检定
  - chi-square test
  - χ2 test
  - chi-squared test of independence
summary: "检验两个类别变量之间是否存在关联的推断统计方法，使用χ2统计量，适用于类别数据和期望频数比较"
type: method
method_type: quantitative
tags:
  - method/statistical
  - quantitative-research
  - categorical-data
related_concepts:
  - "[[Variable]]"
  - "[[Research Question]]"
  - "[[Effect Size]]"
  - "[[Causality]]"
related_theories: []
related_methods:
  - "[[Survey Research]]"
related_persons: []
related_facts: []
related_arguments: []
sources:
  - "[[Creswell_2022_SAGE]]"
confidence: medium
status: draft
created: 2026-05-31
updated: 2026-05-31
---

# Chi-Squared Test

## 定义

> [!info]
> 卡方检验（Chi-Squared Test, χ² test）是一种检验两个类别[[Variable|变量]]（categorical variables）之间是否存在关联的推断统计方法，使用 χ² 统计量。其核心思想是：比较观测频数（实际数据中各单元格的频数）与期望频数（假设两变量独立时的理论频数），两者差异越大，χ² 值越大，关联越可能真实存在（Creswell & Creswell, 2022, Ch8）。

## 研究程序

> [!example]
> Creswell & Creswell (2022, Ch8, Table 8.3) 提供的选择标准：
> - [[Research Question|研究问题]]性质：组间关联（association between groups）
> - 自[[Variable|变量]]数量：1
> - 因变量数量：1
> - 协变量数量：0
> - 变量类型：类别／类别（两个变量均为类别变量，如性别 [男／女] × 投票意向 [支持／反对／未定]）
> - 分数分布：非正态（non-normal）——类别变量本身不产生连续分布分数

当变量是类别变量且研究问题涉及组间关联时，卡方检验是唯一的选择（Creswell & Creswell, 2022, Ch8）。

## 方法变体与相近方法

> [!tip]
> - **卡方独立性检验（Chi-Squared Test of Independence）**：检验两个类别[[Variable|变量]]是否独立——本章 Table 8.3 描述的就是这一形式。
> - **卡方拟合优度检验（Chi-Squared Goodness-of-Fit Test）**：检验单一类别变量的观测分布是否符合某一理论分布。
> - vs t 检验 — t 检验比较两组在一个连续变量上的均值（如男性和女性的平均成绩），卡方检验考察两个类别变量的关联模式（如性别与是否通过考试的交叉表）。
> - vs Pearson 相关 — Pearson 相关要求两个连续变量；卡方检验是两个类别变量关联的首选方法。

## 适用场景

> [!success]
> - [[Survey Research|调查研究]]中检验两个类别[[Variable|变量]]间是否存在显著关联——如性别与教育水平、族裔与投票偏好。
> - 报告样本特征分布是否与总体已知分布一致时（拟合优度）。
> - 分析问卷中多选题或单选题的交叉表数据时。

## 局限性

> [!warning]
> - 对样本量敏感——小样本中期望频数过低（通常 < 5）时 χ² 近似不可靠，应使用 Fisher's 精确检验。
> - 只告知是否存在关联，不提供关联的强度或方向——需要补充 Cramér's V 或 φ 系数等[[Effect Size|效应量]]指标来量化关联强度。
> - 卡方检验显著只表明[[Variable|变量]]间非独立，不能直接解读为[[Causality|因果关系]]。
> - 当表格维度较大（如 5 × 5 交叉表）时，即使关联显著，也很难从 χ² 值本身判断关联的具体模式——需要检查标准化残差来定位具体的差异来源。

## 来源

- [[Creswell_2022_SAGE]]
