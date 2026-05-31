---
title: t-test
aliases:
  - t检验
  - independent samples t-test
  - 独立样本t检验
  - paired samples t-test
  - 配对样本t检验
  - Student's t-test
summary: "比较两组均值的推断统计方法，包括比较两个独立组均值的独立样本t检验和比较同一组两次测量均值的配对样本t检验"
type: method
method_type: quantitative
tags:
  - method/statistical
  - quantitative-research
  - group-comparison
related_concepts:
  - "[[Variable]]"
  - "[[Effect Size]]"
  - "[[Confidence Interval]]"
related_theories: []
related_methods:
  - "[[Analysis of Variance (ANOVA)]]"
  - "[[Survey Research]]"
  - "[[Single-Subject Design]]"
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

# t-test

## 定义

> [!info]
> t 检验（t-test）是一种比较两组均值的推断统计方法，使用 t 统计量。独立样本 t 检验（Independent Samples t-test）比较两个独立组的均值；配对样本 t 检验（Paired Samples t-test）比较同一组在两次测量中的均值。报告时应将 t 统计量以斜体呈现（Creswell & Creswell, 2022, Ch8）。

## 研究程序

> [!example]
> t 检验的典型使用步骤（Creswell & Creswell, 2022, Ch8）：

1. 明确分组[[Variable|变量]]（二分类，如实验组 vs 对照组）和结果变量（连续变量）。
2. 检查两组是否独立（独立样本 t 检验）或配对（配对样本 t 检验）。
3. 检查正态分布假设和方差同质性假设。
4. 计算 t 统计量并比较 p 值与预设显著性水平。
5. 报告[[Effect Size|效应量]]（如 Cohen's d）和[[Confidence Interval|置信区间]]。

## 方法变体与相近方法

> [!tip]
> - **独立样本 t 检验**：比较两个独立组的均值，如实验组 vs 对照组的后测得分。
> - **配对样本 t 检验**：比较同一组在两次测量中的均值，如前测 vs 后测。
> - vs [[Analysis of Variance (ANOVA)|ANOVA]] — t 检验是 ANOVA 在两组比较时的特例；当需要比较三组或以上时，应使用 ANOVA 而非多次 t 检验（以避免第一类错误膨胀）。

## 适用场景

> [!success]
> - 实验中比较两个处理条件之间的均值差异。
> - [[Survey Research|调查研究]]中比较两个群体在某[[Variable|变量]]上的均值差异。
> - [[Single-Subject Design|单受试者设计]]中偶尔用于比较基线和处理阶段的合并均值，但可能违反独立测量假设（Borg & Gall, 2006; 引自 Creswell & Creswell, 2022, Ch8）。

## 局限性

> [!warning]
> - 假设数据呈正态分布且方差同质；假设违反时可能需要使用非参数替代方法（如 Mann-Whitney U 检验）。
> - 只能比较两组；多组比较使用独立 t 检验会增加第一类错误。
> - 对异常值敏感。

## 来源

- [[Creswell_2022_SAGE]]
