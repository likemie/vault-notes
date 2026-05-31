---
title: Power Analysis
aliases:
  - 统计功效分析
  - 检验力分析
  - statistical power analysis
  - sample size power analysis
  - a priori power analysis
summary: "一种在研究规划阶段用于估计检测特定效应量所需最小样本量的统计方法"
type: method
method_type: quantitative
tags:
  - method/statistical
  - quantitative-research
  - sample-size
related_concepts:
  - "[[Effect Size]]"
  - "[[Statistical Significance]]"
  - "[[Variable]]"
related_theories: []
related_methods:
  - "[[Quantitative Research]]"
  - "[[Survey Research]]"
  - "[[Experimental Research]]"
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

# Power Analysis

## 定义

> [!info]
> 统计功效分析（Power Analysis）是一种在研究规划阶段、正式招募受试者之前，用于估计检测特定效应量所需最小样本量的统计方法（Kraemer & Blasey, 2016）。功效分析的目的是确保研究有足够的统计能力来检测变量间真实存在的关系或组间差异，避免因样本不足而无法发现真实效应（Creswell & Creswell, 2022, Ch8）。

> [!quote]
> "Sample size determination should be based on your analysis plans and expected outcomes"（Fowler, 2014; 引自 Creswell & Creswell, 2022, Ch8）

## 研究程序

> [!example]
> 功效分析的核心程序（Creswell & Creswell, 2022, Ch8）：

1. 明确分析计划——确定主要研究假设和拟用的统计检验类型。
2. 设定输入参数，包括：
   - 预期效应量（effect size）——基于先前研究或理论预期估计变量间关系或组间差异的大小。
   - 显著性水平（α）——通常设定为 .05。
   - 期望功效（power）——通常设定为 .80，表示有 80% 的概率在效应真实存在时检测到该效应。
   - 组数或预测变量数量——取决于研究设计。
3. 使用功效分析软件计算所需的样本量。

常用的功效分析工具包括 G*Power（Faul et al., 2007; Faul et al., 2009）等免费在线或商业软件。

> [!note] 调查与实验的功效分析差异
> - **调查研究**：功效分析侧重于估计在给定预期关联强度下检测变量间显著关联所需的样本量。
> - **实验研究**：输入参数需额外包括实验条件数和对组间差异的效应量估计；分析重点转向估计每个实验条件下所需的受试者人数（Creswell & Creswell, 2022, Ch8）。

## 适用场景

> [!success]
> - 规划任何涉及假设检验的[[Quantitative Research|量化研究]]时，均应在数据收集前进行功效分析。
> - 调查研究中，需要确定样本量以检测变量间关联。
> - 实验研究中，需要估计每个条件下检测显著组间差异所需的人数。
> - 许多科学期刊现在要求在方法部分报告功效分析（Creswell & Creswell, 2022, Ch8）。

## 局限性

> [!warning]
> - 功效分析的输出质量取决于输入参数的合理性；如果预期效应量估计不准确，计算出的样本量可能过大或过小。
> - 仅基于过去研究的样本量或简单取总体的一定比例（如 10%）来确定样本量的做法不是最优的（Fowler, 2014; 引自 Creswell & Creswell, 2022, Ch8）。
> - 事后功效分析（post hoc power analysis）在方法论上有争议，因此应在研究规划阶段而非数据收集后使用。

## 使用此方法的研究

> [!example]
> - [[Argument_Creswell_2022_SAGE]] — 以调查和实验方法计划为例，说明如何在研究规划和正式招募前使用 G*Power 等工具进行样本量功效分析。（Ch8）

## 来源

- [[Creswell_2022_SAGE]]
