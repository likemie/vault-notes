---
title: Repeated Measures Design
aliases:
  - 重复测量设计
  - repeated measures
  - within-subjects design
  - 受试者内设计
  - crossover design
summary: "真实验设计变体，同一组受试者在两种或多种实验条件下接受测试，以自身为控制消除个体差异，但需应对顺序效应和延续效应"
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
  - "[[Effect Size]]"
  - "[[Variable]]"
  - "[[Order Effects]]"
  - "[[Hypothesis]]"
  - "[[Interaction Effect]]"
  - "[[Growth]]"
  - "[[Threats to Internal Validity]]"
related_methods:
  - "[[True Experimental Design]]"
  - "[[Matched Pairs Design]]"
  - "[[Analysis of Variance]]"
  - "[[Random Assignment]]"
  - "[[Pilot Testing]]"
  - "[[ABAB Design]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
status: draft
created: 2026-07-12
updated: 2026-07-13
---
# Repeated Measures Design

## 定义

> [!def] 重复测量设计
> 重复测量设计（Repeated Measures Design）是[[True Experimental Design|真实验设计]]的变体：同一组受试者在**两种或多种实验条件**下接受测试，同一人可能接受不止一种干预（可能包含或不包含控制条件）。这是[[Matched Pairs Design|配对设计]]的变体，具有显著的控制潜力——**完全相同的人**接受不同干预，彻底消除了所有个体差异混淆（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 325–326]]）。

> [!method-scope] 方法范围
> - **研究对象** 同一组参与者，依次接受全部实验条件。
> - **问题类型** 不同干预条件之间的效应是否存在差异？（以个体为自身控制）
> - **分析单位** 个体在多种条件下的重复测量数据。
> - **输出形式** 条件间比较（重复测量 [[Analysis of Variance|ANOVA]] 或配对 t 检验），[[Effect Size|效应量]]估计。

## 方法定位

> [!method-position] 在实验设计中的独特位置
> - **与组间设计的根本区别** 组间设计中，实验组和控制组是不同的人——即使[[Random Assignment|随机化]]也只能在期望上等价，小样本中仍可能出现系统性差异。重复测量设计让**完全相同的人**接受所有条件，个体差异被自动消除，统计检验力更高（去除了个体间变异）。
> - **有效性标准** 对个体差异的控制力最强——每个参与者作为自身对照，组内变异（个体差异）不进入误差项。
> - **不能回答的问题** 无法用于干预效应不可逆的情境（如学习效应）——一旦参与者学会了某种技能，撤除条件后行为不会回到基线。

> [!method-stack] 方法层级
> - **研究设计** 真实验变体——受试者内设计（within-subjects），同一参与者经历全部条件。
> - **数据收集** 每个参与者在每种条件下的测量数据（每个参与者贡献多个数据点）。
> - **分析方法** 重复测量 [[Analysis of Variance|ANOVA]]、配对 t 检验、线性混合模型。
> - **辅助技术** 拉丁方排列、随机化顺序排列。

## 研究程序

> [!warrant]- 为什么同一组人接受全部条件？
> 组间设计中，实验组和控制组是**不同的人**，个体差异（能力、性格、经历）成为混淆[[Variable|变量]]——即使[[Random Assignment|随机化]]也只能在期望上等价，小样本中仍可能出现系统性差异。重复测量设计让**完全相同的人**接受所有条件，彻底消除了个体差异混淆，统计检验力更高（去除了个体间变异）。代价是引入了[[Order Effects|顺序效应]]——先接受的条件可能影响后续条件的表现。

> [!factors] [[Order Effects|顺序效应]]的两类表现
> - **延续效应（Carry-over Effect）** 第一次干预的影响**持续**到第二次干预的测量时段——前一次干预的效果没有完全消退。
> - **早期优势效应** 早期干预可能比后期干预产生更大的效应——不是因为更有效，而是因为参与者在研究初期更投入、更不疲倦。

> [!proc] 拉丁方排列：均衡顺序效应
> 在三干[[Pilot Testing|预实验]]中，通过系统性排列顺序来均衡（不一定是消除）顺序效应。六组覆盖全部可能的干预序列：
>
> | 组别 | 序列 |
> |---|---|
> | 组 1 | 干预 1 → 干预 2 → 干预 3 |
> | 组 2 | 干预 2 → 干预 3 → 干预 1 |
> | 组 3 | 干预 3 → 干预 1 → 干预 2 |
> | 组 4 | 干预 1 → 干预 3 → 干预 2 |
> | 组 5 | 干预 2 → 干预 1 → 干预 3 |
> | 组 6 | 干预 3 → 干预 2 → 干预 1 |

也可以[[Random Assignment|随机化]]干预顺序并将参与者随机分配至不同序列，但这不保证平衡序列（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 325–326]]）。

## 资料与分析

> [!info]
> 重复测量数据的分析需要考虑数据内部的**相关结构**——同一参与者的多次测量不是独立的。重复测量 [[Analysis of Variance|ANOVA]] 通过球形[[Hypothesis|假设]]（sphericity）来处理这种相关性；当球形假设不满足时，使用 Greenhouse-Geisser 或 Huynh-Feldt 校正。线性混合模型（LMM）是更灵活的替代方案，可以直接建模个体随机效应和不同的协方差结构。在分析[[Interaction Effect|交互效应]]时需特别注意：如果交互效应显著，简单效应分析（simple effects）比主效应更有信息量。

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** [[Order Effects|顺序效应]]不重要或不太可能时；需要消除个体差异混淆时（如小样本研究）；干预效应可逆时——参与者可以在不同条件下回到可比状态。
> - **谨慎使用** 干预可能产[[Growth|生长]]期延续效应时；干预本身的性质可能在序列中变化时。
> - **不适合使用** 干预效应不可逆时（如学习效应——一旦学会就不会遗忘）；当顺序效应本身就是研究对象时（需使用组间设计）。

> [!example] 适合重复测量设计的研究场景
> - **教学方法比较** 同一批学生在三个单元分别接受讲授法、讨论法和翻转课堂，比较三种方法的效果。前提是三个单元难度相当、前一方法效应不会延续到下一单元。
> - **反馈类型研究** 同一组学生在三次写作任务后分别收到即时反馈、延迟反馈和无反馈，比较修改稿质量。个体写作差异自动控制。
> - **药物剂量交叉试验** 同一组患者在三个治疗期依次接受低剂量、高剂量和安慰剂，每期间隔足够的洗脱期（washout period）。患者间体质差异被消除。
> - **界面可用性测试** 同一组用户依次使用三种界面设计完成相同任务，测量完成时间和错误率。操作熟练度差异自动控制。

## 局限性

> [!method-limits]
> - **[[Order Effects|顺序效应]]** 是最主要的威胁——前一次干预可能影响后一次干预的结果，即使通过拉丁方排列也只能均衡而非消除。
> - **延续效应难以完全消除** 某些干预的效应是持久性的——一旦参与者接受了某种训练，其影响可能贯穿后续所有条件。
> - **疲劳和练习效应** 随着参与的进行，受试者可能因疲劳而表现下降，或因练习而表现上升——两者都混淆条件效应。
> - **不可逆干预不适用** 如果干预产生永久性的学习或改变，撤除后行为不会回到基线，重复测量的逻辑失效。

## 相关理论与方法

> [!entry-map]
> | 条目 | 类型 | 关系 |
> |---|---|---|
> | [[True Experimental Design]] | 方法 | 所属类别——重复测量设计是真实验的受试者内变体 |
> | [[Matched Pairs Design]] | 方法 | 亲缘方法——配对设计的逻辑延伸到同一人接受多种条件 |
> | [[Order Effects]] | 概念 | 核心威胁——重复测量设计特有的[[Threats to Internal Validity|内部效度威胁]] |
> | [[ABAB Design]] | 方法 | 共享逻辑——ABAB 也是通过同一受试者接受多种条件来消除个体差异 |

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011, Ch16)]] — 系统介绍重复测量设计的逻辑、[[Order Effects|顺序效应]]挑战、拉丁方排列应对方案及适用条件，并提供了教学方法比较、反馈类型研究、药物交叉试验和界面测试等应用场景。
