---
title: ABAB Design
aliases:
  - ABAB设计
  - ABAB实验设计
  - withdrawal design
  - 撤回设计
  - reversal design
  - 单一案研究
  - ABAB 设计
summary: "单一案实验设计的核心格式，通过交替引入和撤除干预来排除替代解释，建立个体层面的因果推断"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 10
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/experimental
  - single-case-design
  - quantitative-research
related_concepts:
  - "[[Causality]]"
  - "[[Reliability]]"
  - "[[Statistical Significance]]"
  - "[[Research Question]]"
related_methods:
  - "[[Coding in Qualitative Research]]"
  - "[[Single-Case Design]]"
  - "[[Repeated Measures Design]]"
  - "[[Experimental Research]]"
  - "[[Random Assignment]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
status: draft
created: 2026-07-13
updated: 2026-07-13
---
# ABAB Design

## 定义

> [!def] ABAB 设计
> ABAB 设计（ABAB Design，亦称撤回设计或逆转设计）是单一案研究的核心实验格式，由 Kazdin (1982) 系统阐述。它通过四个阶段的交替——基线（A₁）、干预（B₁）、撤除（A₂）、再引入（B₂）——来建立个体层面的[[Causality|因果推断]]。每个阶段内进行多次重复观测，行为变化与干预的引入和撤除精确对应时，干预效应得到有力确认（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 328–330]]）。

> [!method-scope] 方法范围
> - **研究对象** 单个个体或小群体——在特殊教育、临床心理学、行为干预中最常用。
> - **问题类型** 干预是否对该特定个体产生了因果效应？
> - **分析单位** 个体行为在时间维度上的重复测量数据。
> - **输出形式** 四阶段的行为变化折线图（视觉分析）。

## 方法定位

> [!method-position] 在实验设计谱系中的位置
> - **[[Causality|因果推断]]逻辑** 如果只是 A→B，行为改善可能来自干预，也可能来自成熟或历史。撤除干预回到 A₂ 是关键——如果行为也随之回到基线，就排除了成熟和历史的替代解释。B₂ 是对 B₁ 的复制——两次独立验证使因果推断的可[[Reliability|信度]]大幅提升。
> - **有效性标准** 通过可逆性排除替代解释——因果推断力来自阶段间行为变化的**精确对应**，而非组间比较或[[Statistical Significance|统计显著性]]。
> - **不能回答的问题** 无法推广到其他个体或情境（推广性受限）；无法区分干预的多个成分（如果干预是复合的）。

> [!method-stack] 方法层级
> - **研究设计** 单一个体 × 四个时间阶段 × 每阶段多次重复测量。
> - **数据收集** 各阶段内对目标行为的连续观测和记录。
> - **分析方法** 视觉分析——比较各阶段的行为水平、趋势和变异性。
> - **辅助技术** 行为观测[[Coding in Qualitative Research|编码]]系统；观察者间信度检验。

## 研究程序

> [!design-notation] ABAB 设计的记号表示
> 四阶段交替：A = 基线（无干预），B = 干预。每个阶段内进行多次重复观测，`X` = 干预施加，`~~·~~` = 干预撤除（p. 329）：
>
> - **A₁（基线）** ~~·~~ ==O₁== ==O₂== ==O₃==
> - **B₁（干预）** `X` ==O₄== ==O₅== ==O₆==
> - **A₂（撤除）** ~~·~~ ==O₇== ==O₈== ==O₉==
> - **B₂（再引入）** `X` ==O₁₀== ==O₁₁== ==O₁₂==

> [!phase] ABAB 四个阶段的[[Causality|因果]]逻辑
>
> - **A₁ 阶段（基线）**
>
>   无干预状态，连续多次观测建立行为自然频率的基线。
>
> - **B₁ 阶段（干预）**
>
>   引入干预，连续多次观测行为变化。如果干预有效，观测值应从基线水平明显偏离。
>
> - **A₂ 阶段（撤除）**
>
>   撤除干预，观测行为是否**回到或接近基线水平**。如果行为随干预撤除而逆转，则成熟和历史不能解释 B₁ 的变化——这是排除替代解释的关键逻辑。
>
> - **B₂ 阶段（再引入）**
>
>   再次施加干预，观测行为是否**再次改善**。B₂ 是对 B₁ 的复制——两次独立验证使因果推断的可[[Reliability|信度]]大幅提升。

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 聚焦于个体行为变化时；特殊教育、临床心理学、行为干预领域；目标行为具有可逆性时（撤除干预后可以回到基线）。
> - **谨慎使用** 干预效应不可逆时（如学会了某项技能）——撤除后行为不会回到基线，ABAB 逻辑失效。
> - **不适合使用** 需要推广到群体时；[[Research Question|研究问题]]涉及多个体比较时；干预撤除在伦理上不可接受时（如撤除有效治疗）。

## 局限性

> [!method-limits]
> - **可逆性要求** 干预效应必须是可逆的——如果行为一旦学会就不会遗忘，ABAB 的撤除逻辑失效。
> - **推广性受限** 单一个体的结果难以推广到其他个体或情境。
> - **基线和趋势的模糊性** 如果基线阶段行为本身有上升或下降趋势，难以判断干预效应。
> - **伦理考虑** 在 B₁ 证明干预有效后撤除干预（A₂）让个体回到问题状态，需要伦理上的正当性论证。

## 相关理论与方法

> [!entry-map]
> | 条目 | 类型 | 关系 |
> |---|---|---|
> | [[Single-Case Design]] | 方法 | 母方法——ABAB 是单一案研究中最经典的实验格式 |
> | [[Repeated Measures Design]] | 方法 | 亲缘方法——共享重复测量和个体作为自身控制的逻辑 |
> | [[Experimental Research]] | 方法 | 对比参照——组间实验依赖[[Random Assignment\|随机化]]和平均效应，ABAB 依赖可逆性和视觉分析 |

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011, Ch16)]] — 以 Kazdin (1982) ABAB 设计为框架，系统介绍四阶段的[[Causality|因果]]逻辑，并以 Dietz (1977) 在特殊教育中对一名青少年男孩使用 DRL 程序减少课堂干扰为例展示完整 ABAB 循环（Figure 16.5–16.6）。
