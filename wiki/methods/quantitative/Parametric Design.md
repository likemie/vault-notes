---
title: Parametric Design
aliases:
  - 参数设计
  - parametric experiment
summary: "真实验设计的变体，将参与者随机分配到自变量水平固定的组别中，以绘制干预对不同取值区间的差异效应曲线，比单一实验组更敏感"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 12
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/experimental
  - quantitative-research
  - design-type
related_concepts:
  - "[[Independent Variable]]"
  - "[[Variable]]"
  - "[[Effect Size]]"
  - "[[Interaction Effect]]"
  - "[[Pre-test and Post-test]]"
  - "[[Research Purpose]]"
  - "[[Sample Size Determination]]"
related_methods:
  - "[[True Experimental Design]]"
  - "[[Random Assignment]]"
  - "[[Factorial Design]]"
  - "[[Trend Study]]"
  - "[[Pilot Testing]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
status: draft
created: 2026-07-13
updated: 2026-07-13
---
# Parametric Design

## 定义

> [!def] 参数设计
> 参数设计（Parametric Design）是[[True Experimental Design|真实验设计]]的变体：参与者被[[Random Assignment|随机分配]]到[[Independent Variable|自变量]]水平固定的组别中，以绘制干预对不同取值区间的**差异效应曲线**。与将所有能力水平的参与者混在一个实验组中相比，参数设计更敏感——可以知道**哪一组受影响最大、哪一组最小**（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 324]]）。

> [!method-scope] 方法范围
> - **研究对象** 被随机分配至不同自[[Variable|变量]]水平组别的参与者。
> - **问题类型** 干预的效果是否因自变量的不同取值水平而异？哪个区间获益最大？
> - **分析单位** 个体参与者，按自变量水平分组。
> - **输出形式** 各组差异效应曲线——不同水平组的[[Effect Size|效应量]]比较。

## 方法定位

> [!method-position] 与[[Factorial Design|因子设计]]的关系
> - **与[[Factorial Design|因子设计]]的区别** 因子设计同时操纵多个[[Independent Variable|自变量]]以检验[[Interaction Effect|交互效应]]；参数设计仅操纵一个自[[Variable|变量]]的不同水平，目的是绘制**剂量-反应曲线**而非检验变量间的交互。
> - **有效性标准** 比单一实验组包含广泛能力范围的实验更敏感——可以发现干预对特定区间的效应，避免平均效应掩盖子群差异。
> - **不能回答的问题** 不能检验多个自变量之间的交互效应（那是因子设计的任务）。

> [!method-stack] 方法层级
> - **研究设计** 真实验——[[Random Assignment|随机分配]]至自变量固定水平的组别。
> - **数据收集** 各组[[Pre-test and Post-test|前测]]和后测数据。
> - **分析方法** 比较各组[[Effect Size|效应量]]的差异模式；[[Trend Study|趋势分析]]。
> - **辅助技术** 随机数生成器。

## 研究程序

> [!case] 阅读干预的参数设计示例
> 阅读干[[Pilot Testing|预实验]]按阅读能力分为差、中等、良好、优秀四个水平（四组实验组），加上不接受干预的控制组（第五组）。可绘制干预对**不同组**的差异效应曲线——比单一实验组包含广泛能力范围的实验更敏感，因为可以知道**哪一组受影响最大、哪一组最小**（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 324]]）。

> [!warrant]- 为什么按固定水平分组？
> 如果[[Independent Variable|自变量]]是连续的（如阅读能力从低到高），将其分成几个固定水平来分组，可以绘制**剂量-反应曲线**——不同能力水平的学生对同一干预的反应可能截然不同。将所有能力水平的学生混在一个实验组中，平均效应可能掩盖重要的子群差异（如干预对低能力学生有效、对高能力学生无效甚至有害）。

参数设计适用于两种[[Research Purpose|研究目的]]：
- **确认性研究** 某自[[Variable|变量]]被认为对结果有影响，需要确认。
- **探索性研究** 想发现自变量的不同水平是否对结果有不同影响。

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** [[Independent Variable|自变量]]是连续[[Variable|变量]]且有理由相信不同水平会产生不同效应时；需要发现干预对哪个区间最有效时。
> - **谨慎使用** 自变量水平划分的合理性需要基于理论或先前研究；分组过多会导致[[Sample Size Determination|样本量]]需求过大。
> - **不适合使用** 自变量是二分类时（使用标准前[[Pre-test and Post-test|后测]]设计）；需要同时检验多个自变量交互时（使用[[Factorial Design|因子设计]]）。

## 局限性

> [!method-limits]
> - **[[Sample Size Determination|样本量]]需求大** 每个水平需要一个组加上控制组，水平越多样本量需求越大。
> - **水平划分的任意性** 将连续[[Variable|变量]]划分为离散水平（如差/中等/良好/优秀）的切分点可能影响结果——不同的切分可能得出不同的结论。
> - **不能检验[[Interaction Effect|交互效应]]** 参数设计只处理一个[[Independent Variable|自变量]]的多个水平，不涉及多个自变量的交叉。

## 相关理论与方法

> [!entry-map]
> | 条目 | 类型 | 关系 |
> |---|---|---|
> | [[True Experimental Design]] | 方法 | 所属类别——参数设计是真实验的一种变体 |
> | [[Factorial Design]] | 方法 | 互补方法——参数设计关注一个[[Variable\|变量]]的剂量-反应，因子设计关注多变量交互 |
> | [[Random Assignment]] | 方法 | 前提条件——参与者随机分配至各自变量水平组别 |

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011, Ch16)]] — 以阅读干预按阅读能力分四组+控制组的示例，系统介绍参数设计的逻辑和适用场景。
