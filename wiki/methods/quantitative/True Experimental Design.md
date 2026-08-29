---
title: True Experimental Design
aliases:
  - 真实验设计
  - true experimental designs
summary: "具备随机分配、控制组、前测后测和变量操纵全部特征的最高内部效度实验设计，是区分真实验与准实验的基准"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 28
method_related_level: 3
method_related_stars: "⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/experimental
  - quantitative-research
  - design-type
related_concepts:
  - "[[Internal Validity]]"
  - "[[Pre-test and Post-test]]"
  - "[[Dependent Variable]]"
  - "[[Independent Variable]]"
  - "[[Effect Size]]"
  - "[[Statistical Significance]]"
  - "[[Variable]]"
  - "[[Threats to Internal Validity]]"
  - "[[Ecological Validity]]"
  - "[[Blinding]]"
  - "[[Necessary and Sufficient Conditions]]"
  - "[[Pre-test Sensitisation]]"
  - "[[Interaction Effect]]"
  - "[[Causality]]"
  - "[[Research Question]]"
related_methods:
  - "[[Experimental Research]]"
  - "[[Random Assignment]]"
  - "[[Pretest-Posttest Control Group Design]]"
  - "[[Analysis of Variance]]"
  - "[[Analysis of Covariance]]"
  - "[[Posttest-Only Control Group Design]]"
  - "[[Solomon Four-Group Design]]"
  - "[[Factorial Design]]"
  - "[[Matched Pairs Design]]"
  - "[[Repeated Measures Design]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Pre-Experimental Designs]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
status: draft
created: 2026-07-13
updated: 2026-07-13
---
# True Experimental Design

## 定义

> [!def] 真实验设计
> 真实验设计（True [[Experimental Research|experimental design]]）是[[Internal Validity|内部效度]]最高的实验设计类别，必须具备以下**全部八个特征**，缺少任何一个即降级为准实验：一个或多个控制组；一个或多个实验组；[[Random Assignment|随机分配]]至各组；[[Pre-test and Post-test|前测]]以保证等价；后测以观察[[Dependent Variable|因变量]]效应；对实验组施加干预；隔离、控制和操纵[[Independent Variable|自变量]]；控制组与实验组不相互污染（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 317]]）。

> [!method-scope] 方法范围
> - **研究对象** 被随机分配至控制组和实验组的参与者。
> - **问题类型** X 是否导致了 Y？干预的因果效应大小和方向如何？
> - **分析单位** 个体参与者，随机分配至实验条件。
> - **输出形式** 因果效应估计量、[[Effect Size|效应量]]、[[Statistical Significance|统计显著性]]检验。

## 方法定位

> [!method-position] 在实验设计谱系中的位置
> - **与准实验的区分** 唯一的、决定性的区分标准是[[Random Assignment|随机分配]]——真实验具备完整的随机化，准实验缺失或部分缺失随机化。Smith (1991, p. 215) 指出：随机化在全部[[Variable|变量]]范围内产生等价性，而匹配只覆盖少数命名变量。
> - **有效性标准** [[Internal Validity|内部效度]]最高——Campbell & Stanley (1963) 认为[[Pretest-Posttest Control Group Design|前后测控制组设计]]能控制所有[[Threats to Internal Validity|内部效度威胁]]。
> - **不能回答的问题** 高度受控的实验发现能否推广到真实教室和社区（[[Ecological Validity|生态效度]]）？

> [!method-stack] 方法层级
> - **研究设计** 随机分配 + 控制组 + [[Pre-test and Post-test|前测]] + 干预 + 后测（及其变体）。
> - **数据收集** 前测和后测的定量数据。
> - **分析方法** t 检验、[[Analysis of Variance|ANOVA]]、[[Analysis of Covariance|ANCOVA]]、[[Effect Size|效应量]]计算。
> - **辅助技术** 随机数生成器、[[Blinding|盲法]]、安慰剂。

## 研究程序

> [!feature] 真实验的八个[[Necessary and Sufficient Conditions|必要条件]]
> 缺少任何一个即降级为准实验（p. 317）：
>
> 1. 一个或多个控制组
> 2. 一个或多个实验组
> 3. [[Random Assignment|随机分配]]至控制组和实验组
> 4. [[Pre-test and Post-test|前测]]（pre-test）以保证各组等价
> 5. 后测（post-test）以观察对[[Dependent Variable|因变量]]的效应
> 6. 对实验组施加一个或多个干预
> 7. 隔离、控制和操纵[[Independent Variable|自变量]]
> 8. 控制组与实验组不相互污染（non-contamination）

> [!contrast-table] 真实验的主要设计变体
> | 设计 | 前测 | 后测 | 控制组 | 核心特征 |
> |---|---|---|---|---|
> | [[Pretest-Posttest Control Group Design|前后测控制组]] | 有 | 有 | 有 | 最经典，[[Internal Validity|内部效度]]最高 |
> | [[Posttest-Only Control Group Design|仅后测控制组]] | 无 | 有 | 有 | 避免[[Pre-test Sensitisation|前测敏感化]] |
> | [[Solomon Four-Group Design|所罗门四组]] | 有/无 | 有 | 有（含两个控制组） | 分离前测×处理[[Interaction Effect|交互效应]] |
> | [[Factorial Design|因子设计]] | 可有 | 有 | 可有 | 同时操纵多个自[[Variable|变量]]，检验交互效应 |
> | [[Matched Pairs Design|配对设计]] | 有 | 有 | 有 | 先配对再随机分配，控制个体差异 |
> | [[Repeated Measures Design|重复测量]] | 可有 | 有 | 可有 | 同一人接受多种条件，消除个体差异 |

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 可以[[Random Assignment|随机分配]]参与者时；需要最高[[Internal Validity|内部效度]]的[[Causality|因果推断]]时；[[Research Question|研究问题]]适合在受控环境中检验时。
> - **谨慎使用** 当随机分配在伦理或实践上不可行时——降级至准实验。
> - **不适合使用** 研究问题需要高度自然情境时（[[Ecological Validity|生态效度]]优先于内部效度）；无法满足伦理要求时。

## 局限性

> [!method-limits]
> - **[[Ecological Validity|生态效度]]受限** 实验室或高度受控情境的发现可能不适用于真实教育情境（Hammersley, 2008, p. 4）。
> - **伦理约束** 拒绝控制组获得可能有益的干预存在伦理争议（Gorard, 2001b, p. 146）。
> - **复杂理论的挑战** Morrison (2001) 指出在动态、演化的开放系统中保持[[Variable|变量]]恒定是误导性的。

## 相关理论与方法

> [!entry-map]
> | 条目 | 类型 | 关系 |
> |---|---|---|
> | [[Experimental Research]] | 方法 | 母方法——真实验是实验研究中[[Internal Validity|内部效度]]最高的形式 |
> | [[Random Assignment]] | 方法 | 前提条件——随机分配是区分真实验与准实验的唯一决定性标准 |
> | [[Quasi-Experimental Designs]] | 方法 | 降级替代——当无法随机分配时使用 |
> | [[Pre-Experimental Designs]] | 方法 | 更低层级——无控制组或随机分配的设计 |

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011, Ch16)]] — 系统介绍真实验设计的八个[[Necessary and Sufficient Conditions|必要条件]]、七种主要变体、与准实验的区分标准，以及 Bhadwal & Panda (1991) 印度农村阅读研究的真实验案例。
