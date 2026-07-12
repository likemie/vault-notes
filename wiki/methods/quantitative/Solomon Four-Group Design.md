---
title: Solomon Four-Group Design
aliases:
  - Solomon四组设计
  - 所罗门四组设计
  - Solomon four-group
  - Solomon design
summary: "将受试者随机分配到四组的真实验设计，通过操纵前测和处理两个因素来评估前测对处理效果的潜在干扰"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 14
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/experimental
  - quantitative-research
  - design-type
related_concepts:
  - "[[Pre-test and Post-test]]"
  - "[[Interaction Effect]]"
  - "[[Research Purpose]]"
  - "[[Order Effects]]"
  - "[[Pre-test Sensitisation]]"
  - "[[Sample Size Determination]]"
  - "[[Research Question]]"
related_methods:
  - "[[True Experimental Design]]"
  - "[[Factorial Design]]"
  - "[[Random Assignment]]"
  - "[[Analysis of Variance]]"
  - "[[Pretest-Posttest Control Group Design]]"
  - "[[Posttest-Only Control Group Design]]"
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
status: draft
created: 2026-06-01
updated: 2026-07-13
---
# Solomon Four-Group Design

## 定义

> [!def] 所罗门四组设计
> 所罗门四组设计（Solomon Four-Group Design）是一种[[True Experimental Design|真实验设计]]，是 2 × 2 [[Factorial Design|因子设计]]的特例。它将受试者[[Random Assignment|随机分配]]到四个组中，通过操纵[[Pre-test and Post-test|前测]]（有 vs 无）和处理（有 vs 无）两个因素，来评估前测本身是否会对处理效果产生干扰效应。全部四个组均接受后测（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）。

> [!method-scope] 方法范围
> - **研究对象** 被随机分配至四个组的受试者——两组接受前测、两组不接受；两组接受处理、两组不接受。
> - **问题类型** 前测是否改变了处理效应？前测本身是否改变后测表现？前测与处理之间是否存在[[Interaction Effect|交互效应]]？
> - **分析单位** 个体参与者，随机分配至四个条件之一。
> - **输出形式** 2 × 2 [[Analysis of Variance|方差分析]]结果：前测主效应、处理主效应、前测×处理交互效应。

## 方法定位

> [!method-position] 在[[True Experimental Design|真实验设计]]中的独特位置
> - **与标准前[[Pre-test and Post-test|后测]]设计的关系** 标准[[Pretest-Posttest Control Group Design|前后测对照组设计]]只能回答"处理是否有效"，但无法区分处理效应中有多少来自前测的敏感化——前测可能使受试者对处理更加敏感（Good, 1963）。所罗门四组通过增设两个无前测组来**分离和量化**前测效应。
> - **有效性标准** 能同时评估前测主效应、处理主效应和前测×处理[[Interaction Effect|交互效应]]——这是标准前后测设计无法做到的。
> - **不能回答的问题** 无法区分前测效应的具体机制——是前测让受试者猜到了[[Research Purpose|研究目的]]（需求特征），还是前测本身提供了[[Order Effects|练习效应]]。

> [!method-stack] 方法层级
> - **研究设计** 2 × 2 因子真实验——前测（有/无）× 处理（有/无），全部四组接受后测。
> - **数据收集** 四组后测数据 + 两组前测数据。
> - **分析方法** 2 × 2 [[Analysis of Variance|ANOVA]] 检验前测主效应、处理主效应和交互效应。详见 Bailey (1994, pp. 231–234)。
> - **辅助技术** 无——所罗门四组是设计层面的控制，不依赖特定统计技术。

## 研究程序

> [!design-notation] 所罗门四组设计
> 参与者[[Random Assignment|随机分配]]至四组，操纵[[Pre-test and Post-test|前测]]（有/无）和处理（有/无）两个因素，全部接受后测（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 320]]）：
>
> - **实验组** *R* ==O₁== `X` ==O₂==
> - **控制组 1** *R* ==O₃== ~~·~~ ==O₄==
> - **控制组 2** *R* ~~·~~ `X` ==O₅==
> - **控制组 3** *R* ~~·~~ ~~·~~ ==O₆==

> [!warrant]- 为什么需要四个组？
> 标准前后测对照组（实验组 R O₁ X O₂ / 控制组 R O₃ O₄）中，实验组的变化可能来自干预本身，也可能来自前测的敏感化——前测让受试者更清楚地意识到[[Research Purpose|研究目的]]，从而改变了他们对处理的反应。所罗门四组通过增设两个无前测组（控制组 2 和控制组 3）来分离这两种效应：如果 O₅−O₆（无前测时的处理效应）与 O₂−O₄（有前测时的处理效应）显著不同，则说明前测×处理之间存在[[Interaction Effect|交互效应]]。

> [!contrast-table] 六组关键比较
> | 比较 | 内容 | 检验什么 |
> |---|---|---|
> | **实验组 vs 控制组 1** | O₂（有前测有干预）vs O₄（有前测无干预） | 有前测条件下的**处理主效应** |
> | **控制组 2 vs 控制组 3** | O₅（无前测有干预）vs O₆（无前测无干预） | 无前测条件下的**处理主效应** |
> | **实验组 vs 控制组 2** | O₂ vs O₅ | **[[Pre-test Sensitisation\|前测敏感化]]效应**——前测是否改变了干预的效应 |
> | **控制组 1 vs 控制组 3** | O₄ vs O₆ | **前测主效应**——前测本身是否改变后测表现 |
> | **(O₂−O₄) vs (O₅−O₆)** | 有前测时的处理效应 vs 无前测时的处理效应 | **前测×处理交互效应**——两者差异显著则存在交互 |

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 担心[[Pre-test and Post-test|前测]]可能使受试者对处理更加敏感时（如前测让受试者意识到[[Research Purpose|研究目的]]从而改变反应）；研究领域存在关于前测效应的争议或理论关切时；需要同时评估处理效应和前测效应时。
> - **谨慎使用** [[Sample Size Determination|样本量]]不足以支撑四组时（每组至少需要足够样本量以检测效应）；研究后勤和资源有限时。
> - **不适合使用** [[Research Question|研究问题]]不涉及前测担忧时（[[Posttest-Only Control Group Design|仅后测对照组设计]]更经济）；前测在操作上不可能时（如一次性事件后的调查）。

## 局限性

> [!method-limits]
> - **[[Sample Size Determination|样本量]]需求翻倍** 需要四倍的样本量（四组而非两组），资源需求显著增加，在实际教育研究中执行门槛高。
> - **统计分析复杂** 需要 2 × 2 [[Analysis of Variance|ANOVA]] 或混合模型来检验[[Pre-test and Post-test|前测]]×处理的[[Interaction Effect|交互效应]]，分析复杂度高于标准前后测设计。
> - **使用频率低** 由于后勤和伦理门槛高，所罗门四组设计的实际使用频率远低于[[Posttest-Only Control Group Design|仅后测对照组设计]]——许多研究者倾向于取消前测而非增设组别来控制前测效应。

## 相关理论与方法

> [!entry-map]
> | 条目 | 类型 | 关系 |
> |---|---|---|
> | [[Factorial Design]] | 方法 | 母设计——所罗门四组是 2 × 2 因子设计的特例，其中"是否有[[Pre-test and Post-test\|前测]]"作为一个因子 |
> | [[Random Assignment]] | 方法 | 前提条件——四组均需通过随机分配实现等价，否则比较逻辑失效 |
> | [[Analysis of Variance]] | 方法 | 分析方法——2 × 2 ANOVA 是标准的分析工具 |
> | [[Pre-test Sensitisation]] | 概念 | 所罗门四组设计旨在检测和量化的核心威胁 |

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Creswell_2022_SAGE|Creswell & Creswell (2022, Ch8)]] — 以所罗门四组设计为例，展示如何通过操纵[[Pre-test and Post-test|前测]]和处理来评估前测对处理效果的潜在干扰，将其定位为 2 × 2 [[Factorial Design|因子设计]]的特例。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011, Ch16)]] — 系统介绍所罗门四组设计的逻辑（前测×处理[[Interaction Effect|交互效应]]的分离）、六组比较的推算，以及 Bailey (1994, pp. 231–234) 的完整阐释。
