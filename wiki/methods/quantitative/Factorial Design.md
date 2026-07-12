---
title: Factorial Design
aliases:
  - 因子设计
  - 析因设计
  - factorial experiment
  - 2x2 factorial design
summary: "同时操纵两个或多个自变量以检验每个变量的主效应以及变量间交互效应的实验设计，其核心价值在于揭示条件性因果关系"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 17
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/experimental
  - quantitative-research
  - design-type
related_concepts:
  - "[[Independent Variable]]"
  - "[[Variable]]"
  - "[[Interaction Effect]]"
  - "[[Causality]]"
  - "[[Effect Size]]"
  - "[[Confidence Interval]]"
  - "[[Dependent Variable]]"
  - "[[Sample Size Determination]]"
  - "[[Research Question]]"
related_methods:
  - "[[Experimental Research]]"
  - "[[Random Assignment]]"
  - "[[Analysis of Variance]]"
  - "[[True Experimental Design]]"
  - "[[Solomon Four-Group Design]]"
  - "[[Parametric Design]]"
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
status: draft
created: 2026-05-31
updated: 2026-07-13
---
# Factorial Design

## 定义

> [!def] 因子设计
> 因子设计（Factorial Design）是[[Experimental Research|实验研究]]中同时操纵两个或多个[[Independent Variable|自变量]]，以检验每个[[Variable|变量]]的主效应（main effects）以及变量间[[Interaction Effect|交互效应]]（interactions）的设计类型。其命名基于自变量的数量和水平数——例如 2 × 2 受试者间因子设计表示两个自变量各有两个水平，每个受试者只经历一个处理条件组合（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）。

因子设计的核心价值在于揭示**条件性[[Causality|因果关系]]**——一个自变量的效应是否依赖于另一个自变量的水平。这是单因子实验无法回答的问题（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 323–324]]）。

> [!method-scope] 方法范围
> - **研究对象** 被[[Random Assignment|随机分配]]至自变量各水平组合的参与者——每个组合构成一个独立的实验条件。
> - **问题类型** 多个自变量的主效应各是什么？它们之间是否存在交互效应？
> - **分析单位** 个体参与者，随机分配至各实验条件组合。
> - **输出形式** 各主效应的显著性检验 + 交互效应检验 + [[Effect Size|效应量]]估计。

## 方法定位

> [!method-position] 在实验设计中的独特位置
> - **与单因子实验的区别** 单因子实验只能回答"X 是否影响 Y"；因子设计可以回答"X₁ 的效应是否依赖于 X₂ 的水平"。教育现象通常是多[[Variable|变量]][[Interaction Effect|交互作用]]的结果。
> - **有效性标准** 一个实验同时检验多个[[Independent Variable|自变量]]的主效应和交互效应——效率最高。
> - **不能回答的问题** 三向或更高阶交互效应的解释极为困难——统计显著的高阶交互在实际中常常难以给出有意义的实质解释。

> [!method-stack] 方法层级
> - **研究设计** 真实验——多自变量 × 多水平，[[Random Assignment|随机分配]]至各条件组合。
> - **数据收集** 各组后测数据（可选择性包含前测）。
> - **分析方法** [[Analysis of Variance|ANOVA]] 检验主效应和交互效应；报告[[Effect Size|效应量]]和[[Confidence Interval|置信区间]]。
> - **辅助技术** 随机数生成器；交互效应图。

## 研究程序

> [!ref-table] 3 × 3 因子设计的[[Independent Variable|自变量]]与水平
> | 自[[Variable\|变量]] | 水平 1 | 水平 2 | 水平 3 |
> |---|---|---|---|
> | **资源可用性** | 有限（1） | 中等（2） | 高（3） |
> | **学习动机** | 低（4） | 中等（5） | 高（6） |

九种组合为两个自变量各水平的全交叉：1+4, 1+5, 1+6, 2+4, 2+5, 2+6, 3+4, 3+5, 3+6，共 9 个实验组。例如，可能发现有限资源+低动机对考试成绩有显著负面影响，而中等+高资源没有——因子设计的价值正在于揭示这类**条件性效应**（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 323–324]]）。

自变量可有不同数量的水平（如一个变量 2 水平、另一个 3 水平、第三个 4 水平），组合数为 2 × 3 × 4 = 24 组。最常见的简化变体是 **2 × 2 设计**（两个自变量各两个水平 = 四组）。

> [!proc] 因子设计的关键步骤
> 1. **确定自变量和水平** 确定至少两个自变量，每个至少有两个水平；明确变量是受试者间还是受试者内类型。
> 2. **[[Random Assignment|随机分配]]** 使用[[Random Assignment|随机分配]]将受试者分配到各条件组合中（受试者间变量）。
> 3. **收集[[Dependent Variable|因变量]]数据** 对各实验条件组合的参与者测量[[Dependent Variable|因变量]]。
> 4. **检验主效应** 使用[[Analysis of Variance|ANOVA]]检验每个自变量的主效应。
> 5. **检验[[Interaction Effect|交互效应]]** 检验自变量之间的[[Interaction Effect|交互效应]]——一个变量的效应是否依赖于另一个变量的水平。
> 6. **报告[[Effect Size|效应量]]** 报告[[Effect Size|效应量]]和[[Confidence Interval|置信区间]]以评估实际意义（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）。

> [!def] [[Interaction Effect|交互效应]]
> 当两个或多个自变量同时作用于因变量时，一个自变量的效应**依赖于**另一个自变量的水平。以性别 × 年龄对数学学习动机的影响为例（Figure 16.3）：男女之间的动机差异不是恒定的，而是**随年龄变化**。因子设计特别适合检验交互效应，这是其区别于单因子实验的核心优势（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 324]]）。

## 资料与分析

> [!info]
> 因子设计的分析核心是[[Analysis of Variance|ANOVA]]的方差分解——总变异被分解为主效应项、[[Interaction Effect|交互效应]]项和误差项。[[Interaction Effect|交互效应]]的图示诊断至关重要：两条线不平行意味着可能存在交互。如果交互效应显著，主效应的解释需要条件化——不能说"X₁ 有效应"，而应该说"X₁ 的效应取决于 X₂ 的水平"。三向或更高阶交互的解释应谨慎，通常需要很大的[[Sample Size Determination|样本量]]才能检测，且实质含义常常难以清晰表述。

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 理论预测处理效果可能依赖于另一个条件时；需要同时检验多个[[Independent Variable|自变量]]的独立和联合效应时；希望在一个实验中回答多个[[Research Question|研究问题]]时。
> - **谨慎使用** 自[[Variable|变量]]超过三个时——组合数和[[Sample Size Determination|样本量]]需求指数增长；高阶交互解释困难。
> - **不适合使用** 只关心单个自变量的主效应时（标准前后测设计即可）；样本量不足以覆盖所有条件组合时。

## 局限性

> [!method-limits]
> - **指数增长的组数** 随着[[Independent Variable|自变量]]数量增加，所需条件组合数和总[[Sample Size Determination|样本量]]呈指数增长——3×3 需 9 组，2×3×4 需 24 组。
> - **高阶交互的解释困难** 三向或更高阶[[Interaction Effect|交互效应]]的实质含义常常难以清晰表述，统计显著不等于实质重要。
> - **设计复杂性增加** 更多组意味着更多后勤协调和更大的分析复杂度。

## 相关理论与方法

> [!entry-map]
> | 条目 | 类型 | 关系 |
> |---|---|---|
> | [[True Experimental Design]] | 方法 | 所属类别——因子设计是真实验的一种变体 |
> | [[Interaction Effect]] | 概念 | 核心检验对象——因子设计的核心价值就是检验交互效应 |
> | [[Solomon Four-Group Design]] | 方法 | 特例——所罗门四组是 2 × 2 因子设计的特殊案例（前测×处理） |
> | [[Analysis of Variance]] | 方法 | 分析方法——ANOVA 是因子设计标准的数据分析工具 |
> | [[Parametric Design]] | 方法 | 互补方法——参数设计关注单一[[Variable\|变量]]的剂量-反应，因子设计关注多变量交互 |

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Creswell_2022_SAGE|Creswell & Creswell (2022, Ch8)]] — 以 2 × 4 混合因子设计为例（价值肯定条件 × 时间），检验两者对压力荷尔蒙皮质醇响应的影响。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011, Ch16)]] — 以 3 × 3 资源可用性×学习动机设计和性别×年龄[[Interaction Effect|交互效应]]图（Figure 16.3），系统展示因子设计的组合逻辑和交互效应的检验。
