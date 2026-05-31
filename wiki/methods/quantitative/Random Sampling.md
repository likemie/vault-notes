---
title: Random Sampling
aliases:
  - 随机抽样
  - probability sampling
  - 概率抽样
  - random sample
  - 随机样本
summary: "从总体中按均等概率选取样本的抽样方法，每个个体有均等概率被选中，目的是提升样本对总体的代表性并支持统计推论"
type: method
method_type: quantitative
tags:
  - method/sampling
  - quantitative-research
  - survey
related_concepts:
  - "[[Study Population and Sample]]"
  - "[[External Validity]]"
  - "[[Causality]]"
  - "[[Internal Validity]]"
  - "[[Response Bias]]"
related_theories: []
related_methods:
  - "[[Random Assignment]]"
  - "[[Survey Research]]"
related_persons: []
related_facts: []
related_arguments: []
sources:
  - "[[Creswell_2022_SAGE]]"
confidence: medium
status: draft
created: 2026-06-01
updated: 2026-06-01
---

# Random Sampling

## 定义

> [!info]
> 随机抽样（Random Sampling）是从研究总体中选取样本的一种概率抽样方法——总体中每个个体都有均等的概率被选中。随机抽样的目标是提升样本对总体的代表性，使研究者能够将样本结果推广到更广泛的总体（Creswell & Creswell, 2022, Ch8）。

## 研究程序

> [!example]
> 抽样类型的理想层级，按方法论严格程度递减（Creswell & Creswell, 2022, Ch8）：

1. **随机抽样（Random Sampling）**：亦称概率抽样或等概率抽样。每个个体有均等概率被选中。这是理论上的金标准。
2. **系统抽样（Systematic Sampling）**：选择随机起点后，按固定间隔（每隔第 X 人）选取样本。可获得与随机抽样等价的精度（Fowler, 2014; 引自 Creswell & Creswell, 2022, Ch8）。间隔 X 由总体列表人数和所需样本人数确定（如每 80 人中选 1 人）。
3. **非概率／便利抽样（Nonprobability / Convenience Sampling）**：基于便利性和可得性选择受试者——虽然不如前两者理想，但最常用。在无法获取完整总体名单或总体成员难以接触时，这通常是唯一可行的选择。

> [!note] 分层抽样
> 若总体成员的某些特征已知（如性别、收入、教育水平），可以在抽样前按这些特征对总体**分层（Stratify）**——将总体按特定特征划分为层后，在各层内分别随机抽样。分层确保样本在这些特征上的比例与总体中的真实比例一致，而简单随机抽样不一定保证这一结果（Fowler, 2014; 引自 Creswell & Creswell, 2022, Ch8）。

## 概念辨析

> [!example]
> - vs [[Random Assignment|随机分配]]（Random Assignment） — 这是两个经常混淆的概念。随机抽样是关于**谁**进入[[Study Population and Sample|研究样本]]——目标是将样本推广到总体（[[External Validity|外部效度]]）。随机分配是关于已进入样本的受试者**如何**被分配到各实验条件——目标是消除组间系统性偏差并支持[[Causality|因果推断]]（[[Internal Validity|内部效度]]）。一项研究可以同时使用随机抽样和随机分配，也可以只使用其中之一或都不使用（Creswell & Creswell, 2022, Ch8）。

## 适用场景

> [!success]
> - 研究目标是从样本结果推广到更广泛的总体时，随机抽样是最理想的选择。
> - 大规模[[Survey Research|调查研究]]（如全国性民意调查）通常追求随机抽样或系统抽样。
> - 当总体名单（抽样框，sampling frame）可获得且完整时，适合随机抽样。

## 局限性

> [!warning]
> - 在许多实际研究情境中，获取总体的完整名单不可行或成本极高，使得真正的随机抽样难以实现。
> - 即使抽样设计是随机的，低回应率仍可能导致最终样本不等同于随机样本——因为拒绝参与的人可能与同意参与的人存在系统性差异（[[Response Bias|回应偏差]]）。
> - 在教育研究中，研究者通常只能接触到特定学校或班级的学生，便利抽样是最常见的选择——这意味着需要诚实地讨论样本对总体的代表性局限（Creswell & Creswell, 2022, Ch8）。

## 来源

- [[Creswell_2022_SAGE]]
