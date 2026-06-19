---
title: Fixed-Effect and Random-Effects Models
aliases:
  - 固定效应模型
  - 随机效应模型
  - Fixed-Effect Model
  - Random-Effects Model
summary: "元分析中两种基本的统计汇总模型，前者假设所有研究估计同一真实效应并按精度加权，后者同时考虑研究内和研究间变异"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 7
method_related_level: 0
method_related_stars: ""
method_related_color: "#dcfce7"
tags:
- fixed-effect-model
- random-effects-model
- meta-analysis
- effect-size
- statistical-model
- methodology
related_concepts:
  - "[[Effect Size]]"
  - "[[Confidence Interval]]"
  - "[[Heterogeneity]]"
  - "[[Visible Learning]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
related_persons: []
related_arguments:
  - "[[Argument_Higgins_2016_RE]]"
  - "[[Argument_Wecker_2016_ZfE]]"
confidence: medium
status: draft
created: '2026-06-08'
updated: '2026-06-08'
---

## 定义

> [!info] 定义
> 固定效应模型（Fixed-Effect Model）和随机效应模型（Random-Effects Model）是[[Meta-analysis|元分析]]中两种基本的统计汇总方法。它们的核心区别在于如何理解各研究之间[[Effect Size|效应量]]的变异([[Argument_Higgins_2016_RE|Higgins, 2016, p.39]])。
>
> **固定效应模型**假设所有纳入研究估计的是同一个恒定的真实效应量，观察到的差异仅来自各研究内部的抽样误差。因此按精度（方差的倒数）加权，标准误较小的研究贡献更大([[Argument_Higgins_2016_RE|Higgins, 2016, p.39]])。
>
> **随机效应模型**假设每项研究都是干预的略有不同版本，有自己的随机变异需要被考虑。该模型同时纳入研究内变异和研究间变异，因此给出的汇总估计通常更保守([[Argument_Higgins_2016_RE|Higgins, 2016, p.39]])。

---

## 核心机制

> [!abstract] 核心机制
> **固定效应模型的加权逻辑**
>
> 在固定效应模型中，每项研究的权重与其方差成反比。方差越小（即估计越精确）的研究，权重越大。这相当于将[[Meta-analysis|元分析]]视为一个更大的单一研究，其中更精确的测量应贡献更多信息([[Argument_Higgins_2016_RE|Higgins, 2016, p.39]])。
>
> Richard Peto 是这一方法的主要倡导者，他认为当效果不完全相同时，按精度加权估计加权平均是最合理的做法。
>
> **随机效应模型的加权逻辑**
>
> 随机效应模型在研究内方差之上增加了研究间方差（通常用 τ² 表示）。这使得各研究的权重更加均匀，因为额外的研究间变异降低了精确研究的相对优势。Larry Hedges（1983）倡导这一方法，Rebecca DerSimonian 和 Nan Laird（1986）向医学研究者推广并提供了简化的计算公式([[Argument_Higgins_2016_RE|Higgins, 2016, p.39]])。
>
> **模型选择的影响**
>
> 选择哪种模型直接影响汇总[[Effect Size|效应量]]的估计和[[Confidence Interval|置信区间]]的宽度。在[[Heterogeneity|异质性]]较大时，随机效应模型给出更宽的置信区间，反映了额外的不确定性。

---

## 适用场景

> [!success] 适用场景
> **固定效应模型适用于：**
> - 各研究估计的是理论上相同的干预效果
> - 研究间差异主要来自抽样误差
> - 需要将[[Meta-analysis|元分析]]当作更大单一研究来处理时
>
> **随机效应模型适用于：**
> - 各研究的干预在实施细节上存在差异
> - 研究间存在超出抽样误差的真实变异
> - 需要将推论推广到纳入研究之外的更广泛情境时

---

## 局限性

> [!warning] 局限性
> **固定效应模型的根本限制**
>
> 固定效应模型假设所有研究估计同一恒定真实效应。在教育研究中，鉴于不同的教学主题、不同的实现方法，从一开始就假设一个共同常数比假设各研究存在差异更不合理（[[Argument_Wecker_2016_ZfE|Wecker et al., 2016]], cited in Higgins, 2016, p.39）。当这一假设被违背时，固定效应模型会给出过窄的[[Confidence Interval|置信区间]]和过于乐观的显著性检验。
>
> **随机效应模型的数据需求**
>
> 随机效应模型需要估计研究间方差 τ²，这要求有一定数量的纳入研究。当研究数量较少时，τ² 的估计可能不稳定。Hattie 的数据基础（每个因素平均约 63 项一级[[Meta-analysis|元分析]]）可能不足以支持可靠的随机效应估计([[Argument_Wecker_2016_ZfE|Wecker et al., 2016]])。
>
> **[[Argument_Wecker_2016_ZfE|Wecker et al. (2016)]]的方法论审查**
>
> Hattie 声称在 [[Visible Learning]] 中应用了固定效应模型，但实际使用的是未加权平均。正确加权后某些[[Effect Size|效应量]]从 0.59 变为 0.23，排名从第 26 位跌至第 98 位([[Argument_Wecker_2016_ZfE|Wecker et al., 2016]])。

---

