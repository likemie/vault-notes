---
title: Matched Pairs Design
aliases:
  - 配对设计
  - 匹配对设计
  - matched pairs
  - paired design
summary: "真实验设计的变体，先将受试者按关键变量配对，再随机将每对成员分配至控制组与实验组，以控制个体差异对处理效应的干扰"
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
  - "[[Independent Variable]]"
  - "[[Sample Size Determination]]"
  - "[[Variable]]"
  - "[[Effect Size]]"
  - "[[Pre-test and Post-test]]"
  - "[[Attrition]]"
  - "[[Dependent Variable]]"
related_methods:
  - "[[True Experimental Design]]"
  - "[[Random Assignment]]"
  - "[[Matching]]"
  - "[[Experimental Research]]"
  - "[[Repeated Measures Design]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
status: draft
created: 2026-07-12
updated: 2026-07-13
---
# Matched Pairs Design

## 定义

> [!def] 配对设计
> 配对设计（Matched Pairs Design）是[[True Experimental Design|真实验设计]]的一种变体：受试者首先在若干被认为重要的[[Independent Variable|自变量]]上配对，然后将每对成员[[Random Assignment|随机分配]]至控制组和实验组。随机化发生在**配对的层面**而非整组的层面（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 322–323]]）。

该设计适用于无法确定个体差异是否会掩盖处理效应时——通过对配对来控制这些差异。当[[Sample Size Determination|样本量]]较小、随机化可能偶然产生不等价组时，配对设计是在随机化的理论保证之上增加了一层实践保障。

> [!method-scope] 方法范围
> - **研究对象** 先在关键[[Variable|变量]]上配对、再随机分配至两组的参与者。
> - **问题类型** 在控制了个体差异后，干预是否产生了因果效应？
> - **分析单位** 配对个体——分析以配对为单位（如配对 t 检验）。
> - **输出形式** 配对比较的处理效应估计 + [[Effect Size|效应量]]。

## 方法定位

> [!method-position] 在实验设计中的位置
> - **与纯[[Random Assignment|随机化]]的关系** 随机化在整个[[Variable|变量]]范围内产生等价性（Smith, 1991, p. 215），但需要**足够大的样本**才能有效运作。配对设计在小样本中提供了额外的保障——即使随机化偶然失衡，配对确保了关键变量上的等价。
> - **有效性标准** 比纯随机化在小样本中更稳健——匹配变量上的组间差异被强制消除。但控制力仍弱于大样本随机化（因为只控制了命名变量）。
> - **不能回答的问题** 未匹配的变量仍可能混淆结果——配对设计不能替代大样本和随机化，只是在样本受限时的补偿策略。

> [!method-stack] 方法层级
> - **研究设计** 真实验变体——先配对、再随机分配每对成员。
> - **数据收集** [[Pre-test and Post-test|前测]]数据（用于配对）+ 后测数据（用于比较）。
> - **分析方法** 配对 t 检验、配对比较的[[Effect Size|效应量]]。
> - **辅助技术** 配对标准的定义（匹配区间）；排序配对作为折衷。

## 研究程序

> [!warrant]- 为什么先配对再[[Random Assignment|随机分配]]？
> 随机化在大样本中有效，但在**小样本**中可能偶然产生不等价的组（如全部阅读障碍者落入同一组）。配对设计通过在关键[[Variable|变量]]上**先匹配、再随机分配**，确保两组在这些变量上等价——即使[[Sample Size Determination|样本量]]很小。代价是：(1) 需要[[Pre-test and Post-test|前测]]所有候选参与者；(2) 难以找到精确匹配会导致[[Attrition|样本流失]]；(3) 只控制了匹配变量，未匹配的变量仍可能混淆。Smith (1991, p. 215) 指出，匹配远不如随机化——因为随机化控制**所有**变量，匹配只控制**命名**变量。

> [!proc] Borg & Gall (1979, p. 547) 的五步操作程序
> 1. **测量[[Dependent Variable|因变量]]** 对所有潜在受试者进行前测，获取基线分数。
> 2. **建立配对** 基于前测分数将受试者配对——两个得分相同或最接近的受试者组成一对。
> 3. **随机分配** 每对中随机分配一人至控制组，一人至实验组（如掷硬币）。
> 4. **施加干预** 对实验组施加处理，控制组接受安慰剂或不干预，确保两组不接触。
> 5. **后测比较** 对两组测量[[Dependent Variable|因变量]]，比较差异以确定处理效应及其大小。

> [!tension] 配对精度的根本张力（pp. 322–323）
> - **高精度匹配（蓝方）** 定义严格的匹配区间（如 ±3 分），匹配越接近则控制越严密、实验误差越小。但越难找到匹配样本，大量候选参与者因无法匹配而被排除，样本流失严重。
> - **低精度匹配（红方）** 放宽匹配区间，容易抽取足够样本，样本流失少。但匹配精度下降，实验误差增大，组间在关键变量上的残余差异可能混淆处理效应。
>
> **折衷方案** 按因变量分数排序，前两名配对、三四名配对，以损失匹配精度换取保留全部参与者。Borg & Gall (1979, p. 547) 建议匹配多个与因变量相关的变量比匹配单个变量更能减少误差，但变量越多越难抽取——需在精度和可行性之间取得平衡。

Mitchell & Jolley (1988, p. 103) 提出比较两组时需考虑的三个问题：(1) 两组在实验开始时是否等价？(2) 无论干预如何，两组是否会自然分化？(3) 两组初始测量误差在多大程度上导致了分数差异？

> [!contrast-table] 配对 vs [[Random Assignment|随机化]]（Smith, 1991, p. 215）
> | 维度 | [[Random Assignment|随机化]] | 配对（[[Matching]]） |
> |---|---|---|
> | **等价性范围** | **全部变量**（已知和未知、已测量和未测量） | 仅**少数命名变量** |
> | **样本量要求** | 需要足够大才能有效运作 | 小样本中也能在匹配变量上确保等价 |
> | **未测量变量** | 自动控制 | 无法控制，是主要混淆来源 |
> | **适用场景** | 真实验，条件允许[[Random Assignment|随机分配]]时 | 准实验和非[[Experimental Research|实验研究]]，无法随机分配时 |
> | **排除替代解释的能力** | 强——最佳手段 | 弱——远不如随机化 |

## 资料与分析

> [!info]
> 配对设计的分析以**配对**为分析单位——不是比较两组的均值，而是比较每对内部实验组成员与控制组成员的**差异分数**。配对 t 检验是标准的分析方法。如果配对[[Variable|变量]]与[[Dependent Variable|因变量]]高度相关，配对设计可以显著减少误差方差，提高统计检验力。但需要注意：如果配对变量选择不当（与因变量相关性低），配对不仅不能减少误差，反而会因为损失自由度而降低检验力。

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** [[Sample Size Determination|样本量]]较小、[[Random Assignment|随机化]]可能偶然失衡时；有明确的与[[Dependent Variable|因变量]]高度相关的配对[[Variable|变量]]时；需要在小样本中确保组间等价性时。
> - **谨慎使用** 配对变量数量过多时——越难找到匹配样本；配对变量与因变量相关性低时——配对不能有效减少误差。
> - **不适合使用** 大样本真实验（随机化已足够有效）——配对增加了操作复杂度而无额外收益。

## 局限性

> [!method-limits]
> - **难以找到精确匹配** 尤其在实地实验中，候选参与者池有限时。
> - **[[Variable|变量]]数与可行性的权衡** 匹配的变量越多，越难抽取匹配样本；变量越少，未匹配的混淆风险越大。
> - **未匹配变量仍可能混淆** 配对只控制了命名变量——与[[Random Assignment|随机化]]控制所有变量的能力相比有本质差距（Smith, 1991, p. 215）。
> - **配对变量选择依赖前知** 如果选错了配对变量（与[[Dependent Variable|因变量]]相关性低），配对不仅无益反而降低检验力。

## 相关理论与方法

> [!entry-map]
> | 条目 | 类型 | 关系 |
> |---|---|---|
> | [[True Experimental Design]] | 方法 | 所属类别——配对设计是真实验的一种变体 |
> | [[Random Assignment]] | 方法 | 互补技术——随机化在配对之后施加于每对内部 |
> | [[Matching]] | 方法 | 核心操作——配对是匹配技术在实验设计中的具体应用 |
> | [[Repeated Measures Design]] | 方法 | 逻辑延伸——配对设计让不同但相似的人比较，重复测量让同一个人比较 |

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011, Ch16)]] — 系统介绍配对设计的逻辑、Borg & Gall (1979) 五步操作程序、配对精度的权衡、Mitchell & Jolley (1988) 三问题检验，以及 Smith (1991) 对配对 vs [[Random Assignment|随机化]]的对比。
