---
title: Non-Equivalent Control Group Design
aliases:
  - 非等价控制组设计
  - 不等价控制组设计
  - non-equivalent group design
  - NEGD
summary: "最常用的准实验设计之一，实验组与控制组未通过随机化等价，通过匹配或使用尽可能相似的样本来增强组间可比性"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 8
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/quasi-experimental
  - quantitative-research
  - design-type
  - causal-inference
related_concepts:
  - "[[Variable]]"
  - "[[Threats to Internal Validity]]"
  - "[[Causality]]"
  - "[[Internal Validity]]"
related_theories: []
related_methods:
  - "[[Quasi-Experimental Designs]]"
  - "[[Random Assignment]]"
  - "[[Matching]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
confidence: medium
status: draft
created: 2026-07-12
updated: 2026-07-12
---
# Non-Equivalent Control Group Design

## 定义

> [!def] 非等价控制组设计
> 非等价控制组设计（Non-Equivalent Control Group Design）是最常用的[[Quasi-Experimental Designs|准实验设计]]之一，其关键特征是实验组与控制组**未通过[[Random Assignment|随机化]]实现等价**——因此在设计图中用虚线分隔两组（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16]]）。

Campbell & Stanley (1963) 符号表示为：

```
实验组  O₁  X  O₂
------------------
控制组  O₃     O₄
```

虚线表示两组未通过随机分配等价。

## 方法定位

> [!method-position] 与真实验的关键区别
> - **研究者角色** 使用已有完整组别（intact groups），无法控制"谁何时接受何种暴露"。
> - **有效性标准** 组间可比性依赖于匹配而非[[Random Assignment|随机化]]；随机化在理论上控制所有可能的自[[Variable|变量]]，匹配只控制少数命名变量（Smith, 1991, p. 215）。
> - **不能回答的问题** 无法像真实验一样排除全部[[Threats to Internal Validity|内部效度威胁]]；[[Causality|因果推断]]是试探性的。

## 研究程序

组间等价性可通过以下方式增强（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16]]）：

1. 在关键自[[Variable|变量]]上对实验组和控制组进行**匹配（[[Matching]]）**，然后[[Random Assignment|随机分配]]至两组。
2. 若匹配不可行，使用**来自同一总体的样本**或尽可能相似的样本（Kerlinger, 1970）。
3. 若完整组别差异较大，匹配可能因**回归效应（regression effects）**导致后测均值差异，此时匹配效果不佳。

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 教育研究中无法[[Random Assignment|随机分配]]学校或班级的场景；需要对已有组别进行干预效果评估。
> - **谨慎使用** 组间前测差异较大时；缺乏匹配[[Variable|变量]]时。
> - **不适合使用** 需要严格[[Causality|因果推断]]的研究。

## 局限性

> [!method-limits]
> - 缺乏[[Random Assignment|随机化]]意味着组间可能存在未测量的系统性差异，威胁[[Internal Validity|内部效度]]。
> - 匹配仅覆盖少数命名[[Variable|变量]]，无法像随机化一样控制全部可能的混淆变量。
> - 回归效应可能使匹配失效，尤其是当组间差异较大时。

## 使用此方法的研究

> [!example]
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011, Ch16)]] — Mason et al. (1992) 在 Shevington 综合中学使用非等价控制组设计，检验显性语言教学对 GCSE 考试成绩的影响。
