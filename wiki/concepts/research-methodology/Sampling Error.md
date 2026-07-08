---
title: Sampling Error
aliases:
  - 抽样误差
  - standard error
  - sampling distribution
  - 抽样分布
summary: "从同一总体中多次抽样时样本统计量之间的变异，以均值的标准误（SEM）和比例的标准误度量，其分布规律由中心极限定理描述，是确定样本量和置信区间的基础概念"
type: concept
domain: "research-methodology"
related_count: 11
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - method/sampling
  - quantitative-research
  - statistics
related_concepts:
  - "[[Sample Size Determination]]"
  - "[[Confidence Interval]]"
  - "[[Response Bias]]"
  - "[[Sampling Frame]]"
  - "[[Standard Error]]"
  - "[[School Effectiveness]]"
  - "[[Variable]]"
  - "[[Effect Size]]"
related_theories:
  - "[[Central Limit Theorem]]"
related_methods:
  - "[[Causal Modeling]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]]"
confidence: medium
status: draft
created: 2026-06-21
updated: 2026-06-21
---
# Sampling Error

## 定义

> [!def] 核心定义
> 抽样误差（Sampling Error）是指从同一总体中多次抽样时，各样本统计量（如均值）之间以及与总体真值之间的差异。抽样误差通常被量化为样本均值与总体均值之间的差距。它不一定是抽样程序错误的结果——即使抽样程序完全正确，由于不同个体的随机选择，变异仍可能出现。抽样误差的大小取决于总体的变异性（$SD_{pop}$）和[[Sample Size Determination|样本量]]（$N$）；总体变异性越小、样本量越大，抽样误差越小。

> [!concept-lens] 概念透镜
> - **含义** 抽样误差指向样本统计量与总体参数之间的随机偏离，反映的是从有限样本推断总体时所固有的不确定性。
> - **用途** 帮助研究者量化从样本结果推论总体时的精确度，确定所需样本量，以及设定[[Confidence Interval|置信区间]]。
> - **边界** 抽样误差不等于抽样偏差（sampling bias）——前者是随机变异，后者是系统性偏离。也不等于测量误差或非抽样误差（如[[Response Bias|无回应偏差]]、覆盖误差）。

> [!citation-card]- 关键表述
> 抽样误差不一定是抽样程序错误的结果。更确切地说，变异可能源于对不同个体的随机选择。例如，若我们从总体中取大量样本并测量每个样本的均值，这些样本均值不会完全相同。（第8章，p.149）
>
> *Sampling error is not necessarily the result of mistakes made in sampling procedures. Rather, variations may occur due to the chance selection of different individuals.* (Ch. 8, p. 149)

> [!boundary]- 概念边界
> - 不等于抽样偏差（Sampling Bias）——抽样偏差是抽样程序或[[Sampling Frame|抽样框]]导致的系统性偏离，而抽样误差是随机变异。
> - 不等于测量误差——测量误差来自工具本身的不精确，抽样误差来自样本对总体的随机偏离。
> - 不等于无回应偏差——无回应偏差是特定类型的非抽样误差，因某些群体系统性拒绝参与而导致。

---

## 核心要素

### 中心极限定理

> [!feature]
> - **[[Central Limit Theorem|中心极限定理]]（Central Limit Theorem）**：若从任何总体中反复抽取等大的随机大样本，这些样本的均值将近似正态分布，且样本均值的均值将近似等于总体均值。[[Sample Size Determination|样本量]]越大，样本均值的分布越接近正态分布——无论原始总体的形状如何。Hopkins 等（1996: 159, 388）指出，除非存在极不寻常的分布，25 例及以上的样本通常即可产生正态的均值抽样分布。Rose & Sullivan（1993: 144）提醒，95% 的所有样本均值落在总体均值加减 1.96 个[[Standard Error|标准误]]的范围内。

### 均值的标准误

> [!feature]
> - **均值的标准误**（Standard Error of the Mean, [[Causal Modeling|SEM]]）：抽样分布的标准差，是抽样误差的基本度量。$SEM = \frac{SD_{s}}{\sqrt{N}}$，其中 $SD_{s}$ 为样本标准差，$N$ 为样本量。严格公式以总体标准差为分母，但因通常无法获取总体标准差，故用样本标准差替代。SEM 越小，样本均值越接近总体均值。当 $SD_{pop}$ 很大时，$N$ 需非常大以抵消之；当 $SD_{pop}$ 很小时，$N$ 也可较小。

### 比例的标准误

> [!feature]
> - **比例的标准误（Standard Error of Proportions）** 适用于分类或百分比数据。$[[School Effectiveness|SE]] = \sqrt{\frac{P \times Q}{N}}$，其中 $P$ 为某类别的百分比，$Q = 100\% - P$。通常在此基础上应用有限总体校正（finite population correction, fpc）：$fpc = \sqrt{1 - f}$，其中 $f$ 为样本占总体的比例。例如样本为 100（总总体 1,000），$f = 0.1$。

### 置信水平与置信区间

> [!feature]
> - **[[Confidence Interval|置信水平]]**（Confidence Level）：通常以百分比表示（95% 或 99%），是对回应落在给定变异范围内的确信程度指标。95% 置信水平意味着 95% 的情况下结果落在指定范围内。
> - **[[Confidence Interval|置信区间]]**（Confidence Interval）：希望确保的变异程度或变异范围（如 ± 1%、± 2%、± 3%）。置信区间越小，所需样本量越大。常规抽样策略使用 95% 置信水平和 3% 置信区间。

---

## 围绕概念形成的命题

### 命题类型一：样本量与抽样误差的关系（Sample Size–Error Relationship）

> [!concept-lens] 大样本缩小抽样误差但不完全消除
> [[Sample Size Determination|样本量]]与抽样误差之间存在反向关系，但这种关系的边际收益在样本量达到一定水平后递减。

> [!claim] 30 例以下危险地小
> 少于 30 例的样本危险性较大，因其允许相当程度的[[Standard Error|标准误]]存在。超过约 80 例后，样本量的进一步增加对标准误的影响很小（p.152）。

> [!claim] 变异性放大抽样误差
> 若总体中某[[Variable|变量]]的变异性（$SD_{pop}$）很大，则需要大得多的样本才能将抽样误差控制在可接受水平。Gorard（2003: 62）指出，调查如 IQ 这类范围从 70 到约 150 的变量，可能需要比变异较小的变量更大的样本（p.145）。

> [!claim] 统计功效与大样本
> Gorard（2003: 62）指出："功效是对你所使用的检验将[[Effect Size|效应量]]与随机变异区分开来之能力的估计"，大样本帮助研究者实现统计功效（p.152）。

---

## 实证数据

> [!example] 比例[[Standard Error|标准误]]的数值实例
>
> 某校长随机询问 25 名学生，66% 赞成改变午休时间（$P = 66$, $Q = 34$, $N = 25$）。$[[School Effectiveness|SE]] = 9.4$。这意味着：
> - 赞成票可在 56.6%–75.4% 之间变动
> - 反对票可在 43.4%–24.6% 之间变动
>
> 若将样本扩大至 100 名学生：$SE = 4.5$，范围缩小至 61.5%–70.5%（p.151）。
>
> 调查全校 1,000 名学生：$SE = 1.5$，范围缩小至 64.5%–67.5%（p.151）。
>
> 这解释了为何政治民调通常基于 1,000–1,500 的[[Sample Size Determination|样本量]]（Gardner, 1978）。

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen, Manion & Morrison (2011, Ch. 8)]] — 系统介绍抽样误差、[[Standard Error|标准误]]和[[Central Limit Theorem|中心极限定理]]在教育研究中的应用，提供比例标准误的数值实例和民调[[Sample Size Determination|样本量]]解释。
