---
title: Time Series Design
aliases:
  - 时间序列设计
  - time series quasi-experiment
  - interrupted time series
summary: "准实验设计的一种，对非随机取样的组在接受实验处理前后各进行多次重复测量，通过比较前后测数列的变化趋势来判断处理效果"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 13
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/experimental-design
  - source/textbook
  - paradigm/positivist
related_concepts:
  - "[[Pre-test and Post-test]]"
  - "[[Reliability]]"
  - "[[Causality]]"
  - "[[Order Effects]]"
  - "[[Attrition]]"
  - "[[Hawthorne Effect]]"
  - "[[Interaction Effect]]"
related_methods:
  - "[[Quasi-Experimental Designs]]"
  - "[[Trend Study]]"
  - "[[Random Assignment]]"
  - "[[True Experimental Design]]"
  - "[[Repeated Measures Design]]"
related_arguments:
  - "[[Argument_QiMei_2015_EducationalResearchMethods]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
status: draft
created: 2026-06-25
updated: 2026-07-13
---
# Time Series Design

## 定义

> [!def] 时间序列设计
> 时间序列设计（Time Series Design）是对一个非随机取样的实验组（或控制组），在接受实验处理**之前和之后各进行多次重复测量**，而非仅在处理前后各测一次的[[Quasi-Experimental Designs|准实验设计]]。通过比较前[[Pre-test and Post-test|后测]]数列的变化趋势——而非单次前后测的差异——来判断处理效果（[[Argument_QiMei_2015_EducationalResearchMethods|齐梅, 2015, Ch.4]]；[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 328]]）。

> [!method-scope] 方法范围
> - **研究对象** 固定整组，常用于学校课堂教学研究——受试者成为自身的控制。
> - **问题类型** 干预是否引起了结果的稳定趋势变化？变化是即时、延迟还是持续？
> - **分析单位** 组在多个时间点的测量数据。
> - **输出形式** 前后测数列的趋势比较——通过视觉分析判断干预是否改变了趋势的方向或斜率。

## 方法定位

> [!method-position] 在[[Quasi-Experimental Designs|准实验设计]]中的位置
> - **与单次前[[Pre-test and Post-test|后测]]的区分** 单次前后测只能捕捉两个时间点的差异，无法区分"干预效应"和"已有趋势的延续"。多次前测建立了**干预前的趋势基线**——如果前测数列稳定而后测跃升，干预效应的推断更有力。
> - **有效性标准** 通过多次测量提高[[Reliability|信度]]，避免仅依赖前后各一个数据收集点。受试者成为自身控制，降低了反应性效应。
> - **不能回答的问题** 无法像真实验那样排除所有替代解释——历史事件（同时事件）的影响无法通过时间序列本身消除。

> [!method-stack] 方法层级
> - **研究设计** 准实验——单组或两组 × 多个时间点。
> - **数据收集** 处理前后各时间点的重复测量数据。
> - **分析方法** 视觉[[Trend Study|趋势分析]]；分段回归（interrupted time series analysis）；比较干预前后的截距和斜率变化。
> - **辅助技术** 控制组时间序列（增加控制组以排除历史效应）。

## 研究程序

> [!design-notation] 单组时间序列设计
> 单一实验组接受多次[[Pre-test and Post-test|前测]]和多次后测，受试者成为自身的控制（p. 328）：
>
> - **实验组** ==O₁== ==O₂== ==O₃== `X` ==O₄== ==O₅== ==O₆==

> [!warrant]- 为什么需要多次前测和多次后测？
> 单次前测和后测只能捕捉两个时间点的差异，无法区分"干预效应"和"已有趋势的延续"。多次前测建立了**干预前的趋势基线**——如果前测数列稳定（持平），后测突然跃升，则干预效应的推断更有力；如果前测已在上升，后测只是延续趋势，则不能归因于干预。多次后测还可以区分**即时效应**和**延迟效应**，以及效应是否**持续**。

> [!contrast-table] 时间序列可观察的三种趋势
> | 趋势类型 | 表现 | [[Causality\|因果]]含义 |
> |---|---|---|
> | **无效应** | 延续已有的上升、下降或持平趋势，干预前后趋势没有改变 | 干预未产生可检测的影响 |
> | **明显效应** | 干预后出现持续的上升或下降，趋势方向或斜率发生可见变化 | 干预可能改变了结果的轨迹 |
> | **延迟效应** | 干预一段时间后才出现效果，即时后测看不到变化，但后续后测出现趋势改变 | 干预的效应需要时间积累或传播 |

### 三种设计变体

> [!design-notation] 控制组时间序列设计
> 增加一个控制组，两组各有一系列时间前测和后测。通过比较两组时间序列的差异来排除历史效应（[[Argument_QiMei_2015_EducationalResearchMethods|齐梅, 2015, Ch.4]]）：
>
> - **实验组** ==O₁== ==O₂== ==O₃== `X` ==O₄== ==O₅== ==O₆==
> - **控制组** ==O₁== ==O₂== ==O₃== ~~·~~ ==O₄== ==O₅== ==O₆==

统计分析上，可以比较两组各自的前测平均值与后测平均值，也可以直接比较两组各时间点的差异。

> [!design-notation] 相等时间样本设计
> 实验处理（X₁）与控制处理（X₀）在相等的时间内交替出现，每位被试重复接受两种处理。通过比较 X₁ 期间的观测与 X₀ 期间的观测来判断处理效果（[[Argument_QiMei_2015_EducationalResearchMethods|齐梅, 2015, Ch.4]]）：
>
> - **实验组** `X₁` ==O₁== `X₀` ==O₂== `X₁` ==O₃== `X₀` ==O₄==

为控制[[Order Effects|练习效应]]，可设计成 ABBA 顺序安排（A 为无处理，B 为实施处理）。

## 资料与分析

> [!info]
> 时间序列数据的分析核心是**趋势识别**——判断干预是否在时间序列中引入了一个可检测的间断点（interruption）。分段回归分析（segmented regression / interrupted time series analysis）是标准的统计方法：分别拟合干预前后的回归线，检验截距变化（即时效应）和斜率变化（持续效应）是否显著。视觉分析（visual analysis）是辅助手段——绘制时间序列折线图，标注干预时间点，观察趋势的视觉变化。

## 效度特征

> [!feature] 时间序列设计的控制能力
> - **可有效控制** 成熟、测验、测量工具、统计回归、选择偏差、被试[[Attrition|流失]]——通过系列[[Pre-test and Post-test|前测与后测]]对一组被试的稳定变化有所了解，也能对两组处理前后的稳定变化进行比较。
> - **无法避免** 同时事件（历史因素）、[[Hawthorne Effect|霍桑效应]]、练习误差——测验的反作用或[[Interaction Effect|交互作用]]效果以及实验安排的反作用效果无法避免。

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 固定整组的课堂教学研究；需要在自然情境下检验干预效果；无法[[Random Assignment|随机分组]]的场景；政策或制度变革的效果评估（如新课程标准的实施效果）。
> - **谨慎使用** 实验时间较长时，历史事件的影响可能增大；需要对[[Order Effects|练习效应]]和[[Hawthorne Effect|霍桑效应]]有额外控制措施。
> - **不适合使用** 需要严格[[Causality|因果推断]]的研究（优先选择[[True Experimental Design|真实验设计]]）。

## 局限性

> [!method-limits]
> - **历史因素无法消除** 干预期间发生的外部事件可能同时影响时间序列，趋势变化可能由外部事件而非干预导致。
> - **[[Hawthorne Effect|霍桑效应]]和[[Order Effects|练习效应]]** 因多次重复测量而产生——受试者可能因反复测试而改变表现。
> - **[[Causality|因果推断]]力弱于真实验** 缺乏[[Random Assignment|随机分配]]意味着组间差异可能来自选择效应而非干预。
> - **对数据质量要求高** 需要多个时间点的一致测量——如果测量工具在不同时间点不一致（工具变化），[[Trend Study|趋势分析]]失效。

## 相关理论与方法

> [!entry-map]
> | 条目 | 类型 | 关系 |
> |---|---|---|
> | [[Quasi-Experimental Designs]] | 方法 | 所属类别——时间序列是一种准实验设计 |
> | [[Repeated Measures Design]] | 方法 | 亲缘方法——共享多次重复测量的逻辑，但时间序列是准实验（单组），重复测量是真实验（受试者内） |
> | [[True Experimental Design]] | 方法 | 升级参照——增加[[Random Assignment\|随机分配]]和控制组后升级为真实验 |
> | [[Random Assignment]] | 方法 | 缺失的关键——时间序列设计最根本的局限就是缺乏随机分配 |

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_QiMei_2015_EducationalResearchMethods|齐梅 (2015, Ch.4)]] — 系统介绍时间序列设计的三种形式（单组、控制组、相等时间样本）及其效度控制特征。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011, Ch16)]] — 以 Campbell & Stanley (1963) 符号系统表示单组时间序列设计，说明多次[[Pre-test and Post-test|前测]]和后测使受试者成为自身控制，可观察无效应、明显效应和延迟效应三种趋势。
