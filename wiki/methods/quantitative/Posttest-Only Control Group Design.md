---
title: Posttest-Only Control Group Design
aliases:
  - 仅后测控制组设计
  - 仅后测对照组设计
  - posttest-only control-group design
  - post-test only design
summary: "真实验设计的变体，随机分配后无前测、仅后测，通过取消前测来避免前测敏感化效应，代价是无法验证基线等价和测量个体变化"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 13
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/experimental
  - quantitative-research
  - design-type
related_concepts:
  - "[[Pre-test and Post-test]]"
  - "[[Pre-test Sensitisation]]"
  - "[[Research Purpose]]"
  - "[[Internal Validity]]"
  - "[[Variable]]"
  - "[[Sample Size Determination]]"
  - "[[Hypothesis]]"
related_methods:
  - "[[True Experimental Design]]"
  - "[[Random Assignment]]"
  - "[[Pretest-Posttest Control Group Design]]"
  - "[[Solomon Four-Group Design]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
  - "[[Argument_Creswell_2022_SAGE]]"
status: draft
created: 2026-07-13
updated: 2026-07-13
---
# Posttest-Only Control Group Design

## 定义

> [!def] 仅[[Pre-test and Post-test|后测]]控制组设计
> 仅后测控制组设计（Posttest-Only Control Group Design）是[[True Experimental Design|真实验设计]]的变体：参与者通过[[Random Assignment|随机分配]]分为实验组和控制组，**不进行前测**，仅实验组接受干预（X），两组均接受后测。因果效应通过比较两组后测均值来估计（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 320]]）。

> [!method-scope] 方法范围
> - **研究对象** 被随机分配至实验组和控制组的参与者——不进行前测。
> - **问题类型** 干预是否产生了因果效应？（排除[[Pre-test Sensitisation|前测敏感化]]后的纯净估计）
> - **分析单位** 个体参与者。
> - **输出形式** 两组后测均值的比较。

## 方法定位

> [!method-position] 与前[[Pre-test and Post-test|后测]]设计的关系
> - **设计选择的情境** 当担心前测可能使受试者对干预敏感时（如前测让受试者猜到[[Research Purpose|研究目的]]），取消前测是合理选择。当[[Random Assignment|随机化]]已确保组间等价时，前测并非必需。
> - **有效性标准** [[Internal Validity|内部效度]]低于前后测设计——无法用前测数据验证随机化是否成功，无法测量个体层面的变化量。
> - **不能回答的问题** 无法确定两组在基线是否等价（只能依赖随机化的理论保证）；无法测量个体变化。

> [!method-stack] 方法层级
> - **研究设计** 真实验——随机分配 + 无前测 + 干预 + 后测。
> - **数据收集** 两组后测数据（仅两组测量值）。
> - **分析方法** 独立样本 t 检验比较两组后测均值。
> - **辅助技术** 随机数生成器。

## 研究程序

> [!design-notation] 仅[[Pre-test and Post-test|后测]]控制组设计
> 参与者[[Random Assignment|随机分配]]至实验组和控制组，无前测，仅实验组接受干预，两组仅接受后测（p. 320）：
>
> - **实验组** **R** `X` ==O₁==
> - **控制组** **R** ~~·~~ ==O₂==

> [!warrant]- 为什么取消前测？
> 前测本身可能使受试者对实验[[Variable|变量]]敏感（[[Pre-test Sensitisation|前测敏感化]]），也可能让参与者猜到[[Research Purpose|研究目的]]而改变行为。当随机化已确保组间等价、且担心前测污染时，取消前测是合理选择。代价是无法用前测分数验证随机化是否成功、无法测量个体层面的变化量，只能依赖组间后测差异推断因果。

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 担心[[Pre-test and Post-test|前测]]产生敏感化效应时；前测在操作上不可能或不道德时（如一次性事件后的态度调查）；[[Random Assignment|随机化]]可信且[[Sample Size Determination|样本量]]足够大时。
> - **谨慎使用** 样本量较小时——无法用前测数据验证随机化是否成功。
> - **不适合使用** 需要测量个体变化时——使用前后测设计。

## 局限性

> [!method-limits]
> - **无法验证基线等价** 完全依赖[[Random Assignment|随机化]]的理论保证，无法用[[Pre-test and Post-test|前测]]数据实证检验两组是否等价。
> - **无法测量个体变化** 只有后测数据，无法区分"干预前就高的组"和"干预后变高的组"——只能依赖随机化[[Hypothesis|假设]]两组基线相同。
> - **对随机化质量高度敏感** 如果随机化失败（小样本中可能出现），无法通过前测发现。

## 相关理论与方法

> [!entry-map]
> | 条目 | 类型 | 关系 |
> |---|---|---|
> | [[Pretest-Posttest Control Group Design]] | 方法 | 互补设计——有[[Pre-test and Post-test|前测]]时使用，担心前测时使用本设计 |
> | [[Solomon Four-Group Design]] | 方法 | 综合方案——同时包含有前测和无前测组，可分离前测效应 |
> | [[Random Assignment]] | 方法 | 唯一依赖——无前测时随机化的质量决定了设计的有效性 |

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Creswell_2022_SAGE|Creswell & Creswell (2022, Ch8)]] — 将仅[[Pre-test and Post-test|后测]]控制组设计列为[[True Experimental Design|真实验设计]]的四种基本类型之一。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011, Ch16)]] — 在真实验设计部分系统介绍仅后测设计的符号表示和应用场景。
