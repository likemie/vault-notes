---
title: Pretest-Posttest Control Group Design
aliases:
  - 前后测控制组设计
  - 前后测对照组设计
  - pretest-posttest control-group design
  - pre-test-post-test control group design
summary: "最经典的真实验设计，随机分配参与者至实验组和控制组，两组均接受前测和后测，通过比较两组前后测差异来估计干预的净效应"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 19
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/experimental
  - quantitative-research
  - design-type
related_concepts:
  - "[[Pre-test and Post-test]]"
  - "[[Effect Size]]"
  - "[[Threats to Internal Validity]]"
  - "[[Internal Validity]]"
  - "[[Pre-test Sensitisation]]"
  - "[[Variable]]"
  - "[[Counterfactual]]"
  - "[[Causality]]"
  - "[[Interaction Effect]]"
  - "[[Sample Size Determination]]"
  - "[[Ecological Validity]]"
related_methods:
  - "[[True Experimental Design]]"
  - "[[Random Assignment]]"
  - "[[Solomon Four-Group Design]]"
  - "[[Analysis of Covariance]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Experimental Research]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
  - "[[Argument_Creswell_2022_SAGE]]"
status: draft
created: 2026-07-13
updated: 2026-07-13
---
# Pretest-Posttest Control Group Design

## 定义

> [!def] 前[[Pre-test and Post-test|后测]]控制组设计
> 前后测控制组设计（Pretest-Posttest Control Group Design）是最经典的[[True Experimental Design|真实验设计]]：参与者通过[[Random Assignment|随机分配]]分为实验组和控制组，两组均接受前测（O₁ 和 O₃）和后测（O₂ 和 O₄），仅实验组接受干预（X）。因果效应的估计量为 (O₂−O₁) − (O₄−O₃)（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 317–319]]）。

> [!method-scope] 方法范围
> - **研究对象** 被随机分配至实验组和控制组的参与者。
> - **问题类型** 干预是否产生了因果效应？效应的大小和方向如何？
> - **分析单位** 个体参与者，随机分配至两个条件之一。
> - **输出形式** 实验组与控制组前后测差异的比较，通常以独立样本 t 检验或[[Effect Size|效应量]]报告。

## 方法定位

> [!method-position] 在[[True Experimental Design|真实验设计]]中的核心地位
> - **为何是金标准** Campbell & Stanley (1963) 认为该设计强大到足以控制第 10 章中识别的所有[[Threats to Internal Validity|内部效度威胁]]——[[Random Assignment|随机化]]排除选择偏差，控制组排除历史和成熟效应，[[Pre-test and Post-test|前测]]验证基线等价。
> - **有效性标准** [[Internal Validity|内部效度]]最高——是区分真实验与准实验的基准设计。
> - **不能回答的问题** 无法区分干预效应中是否有[[Pre-test Sensitisation|前测敏感化]]的贡献——前测可能使受试者对干预更加敏感（Good, 1963）。如需分离前测效应，需升级至[[Solomon Four-Group Design|所罗门四组设计]]。

> [!method-stack] 方法层级
> - **研究设计** 真实验——随机分配 + 前测 + 干预 + 后测。
> - **数据收集** 两组前测和后测数据（共四组测量值）。
> - **分析方法** 独立样本 t 检验比较两组前后测差异，或 [[Analysis of Covariance|ANCOVA]] 以前测为协[[Variable|变量]]。
> - **辅助技术** 随机数生成器；基线平衡检验。

## 研究程序

> [!design-notation] 前[[Pre-test and Post-test|后测]]控制组设计
> 参与者[[Random Assignment|随机分配]]至实验组和控制组，两组均接受前测和后测，仅实验组接受干预（pp. 317–319）：
>
> - **实验组** **R** ==O₁== `X` ==O₂==
> - **控制组** **R** ==O₃== ~~·~~ ==O₄==

$$\text{因果效应} = (O_2 - O_1) - (O_4 - O_3)$$

> [!warrant]- 为什么需要前测和随机分配？
> **前测（O₁ 和 O₃）**确保两组在干预前基线等价——如果随机化成功，O₁ 和 O₃ 的均值应接近。**随机分配（R）**使两组在所有已知和未知[[Variable|变量]]上等价，排除选择偏差。**控制组**提供[[Counterfactual|反事实]]参照——O₄−O₃ 是自然变化，O₂−O₁ 是干预+自然变化，两者相减即得纯净的干预效应。

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 可以[[Random Assignment|随机分配]]参与者且可以进行[[Pre-test and Post-test|前测]]时；需要最高[[Internal Validity|内部效度]]的[[Causality|因果推断]]时；经典的教育实验情境。
> - **谨慎使用** 担心前测可能产生敏感化效应时——考虑升级至[[Solomon Four-Group Design|所罗门四组设计]]。
> - **不适合使用** 无法随机分配时（使用[[Quasi-Experimental Designs|准实验设计]]）；前测不可能或不道德时（使用仅后测设计）。

## 局限性

> [!method-limits]
> - **[[Pre-test Sensitisation|前测敏感化]]** [[Pre-test and Post-test|前测]]可能使受试者对干预更加敏感，前测×处理的[[Interaction Effect|交互效应]]可能混淆干预效应的估计（Good, 1963）。
> - **[[Sample Size Determination|样本量]]需求** 两组设计需要足够的样本量才能使[[Random Assignment|随机化]]发挥有效控制。
> - **推广性受限** 实验室或高度受控情境中的发现可能缺乏[[Ecological Validity|生态效度]]。

## 相关理论与方法

> [!entry-map]
> | 条目 | 类型 | 关系 |
> |---|---|---|
> | [[Experimental Research]] | 方法 | 母方法——前后测控制组设计是最经典的[[True Experimental Design|真实验设计]]形式 |
> | [[Random Assignment]] | 方法 | 前提条件——随机分配是实现组间等价的关键 |
> | [[Solomon Four-Group Design]] | 方法 | 升级版——通过增加两个无前测组来分离前测×处理[[Interaction Effect|交互效应]] |
> | [[Quasi-Experimental Designs]] | 方法 | 降级替代——当无法随机分配时使用的设计 |

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Creswell_2022_SAGE|Creswell & Creswell (2022, Ch8)]] — 将前[[Pre-test and Post-test|后测]]控制组设计列为[[True Experimental Design|真实验设计]]的基本形式，以 Campbell & Stanley 符号系统表示。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011, Ch16)]] — 以 Bhadwal & Panda (1991) 印度农村阅读研究为例，展示前后测控制组加两个控制组的扩展设计。
