---
title: Matching
aliases:
  - 匹配法
summary: "观察性研究中的因果推断方法，通过匹配协变量分布提高处理组与对照组可比性，以减少选择偏差对效果估计的干扰"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 21
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
tags:
  - matching
  - observational-studies
  - causal-inference
  - subject/research-methodology
  - paradigm/positivist
related_concepts:
  - "[[Variable]]"
  - "[[Hypothesis]]"
  - "[[Causality]]"
  - "[[Epistemology]]"
  - "[[Counterfactual]]"
  - "[[Dependent Variable]]"
  - "[[Stable Unit Treatment Value Assumption]]"
  - "[[Interaction Effect]]"
related_theories:
  - "[[Potential Outcomes Framework]]"
related_methods:
  - "[[Matched Pairs Design]]"
  - "[[Random Assignment]]"
  - "[[Causal Modeling]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Experimental Research]]"
  - "[[Covariate Adjustment]]"
  - "[[Non-intervention Research]]"
  - "[[Ex Post Facto Research]]"
related_persons: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
  - "[[Argument_Berk_2011_ER]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch15]]"
related_facts:
  - "[[Parliamentary Office of Science and Technology]]"
confidence: low
status: draft
created: 2026-05-03
updated: 2026-07-13
---

## 定义

> [!def] 匹配的双重含义
> 匹配（Matching）在教育研究方法论中有两种不同但互补的用途（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16]]）：
>
> **作为实验设计技术** 在真实验的[[Matched Pairs Design|配对设计]]中，先在关键[[Variable|变量]]上配对参与者，再[[Random Assignment|随机分配]]每对成员至实验组和控制组——随机化发生在配对层面。在准实验中，匹配是增强组间可比性的主要手段。
>
> **作为观察性研究技术** 在处理组和对照组之间匹配协变量分布相似的研究对象，使两组在可观测特征上变得可比。[[Argument_Berk_2011_ER|Berk (2011)]] 推荐其为[[Causal Modeling|因果建模]]（SEM）的替代方法——"更少依赖不可检验的[[Hypothesis|假设]]，更多受实证诊断约束"([[Argument_Berk_2011_ER|Berk, 2011, p.198]])。

> [!method-scope] 方法范围
> - **研究对象** 需要在关键变量上可比的两组或多组参与者——可以是实验设计中的实验组/控制组，也可以是观察性数据中的处理组/对照组。
> - **问题类型** 在无法[[Random Assignment|随机分配]]时，如何使组间在关键特征上等价以支持[[Causality|因果推断]]？
> - **分析单位** 个体参与者——通过配对使成员在匹配变量上相似。
> - **输出形式** 匹配后的平衡检验、匹配样本的比较分析。

## 方法定位

> [!method-position] [[Epistemology|认识论]]定位
> - **知识观** 匹配隐含[[Counterfactual|反事实]][[Causality|因果推断]]立场：如果能找到在处理前协[[Variable|变量]]分布相同的两组主体，则两组结果的差异可归因于处理本身。这要求"自然进行的等效于在给定一组协变量条件下的随机实验"([[Argument_Berk_2011_ER|Berk, 2011, p.198]])。
> - **与[[Random Assignment|随机化]]的关系** 随机化在**全部变量**（已知和未知）上产生等价性；匹配只在**少数命名变量**上产生等价性。Smith (1991, p. 215) 明确指出：匹配在排除替代因果解释方面**远不如随机化（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 323]]）**。
> - **不能推出的结论** 匹配不能替代随机化——未匹配的变量仍可能混淆结果。样本中的平衡不意味着未观测协变量也存在平衡。

> [!method-stack] 方法层级
> - **研究设计** 观察性研究或[[Quasi-Experimental Designs|准实验设计]]——匹配是在非随机分配条件下增强组间可比性的策略。
> - **数据收集** 处理组和对照组的协变量数据 + [[Dependent Variable|结果变量]]数据。
> - **分析方法** 倾向得分匹配（PSM）、精确匹配、马氏距离匹配；匹配后通过标准化均值差（SMD）评估平衡。
> - **辅助技术** 敏感性分析（Rosenbaum bounds）评估未观测混杂因素的影响。

## 研究程序

> [!proc] 观察性研究中的匹配步骤
> 1. **确定匹配[[Variable|变量]]** 选择用于匹配的协变量，关键操作原则是——匹配变量的选择**不参考[[Dependent Variable|结果变量]]**。[[Argument_Berk_2011_ER|Berk (2011, p.198)]] 强调："匹配变量的集合在不参考结果变量的情况下确定。目标是使样本达到平衡，为此，结果变量可以被锁在保险箱里。"
>
> 2. **匹配处理组与对照组** 将处理组和对照组的主体进行匹配，使两组在匹配变量上的分布有效相同
>
> 3. **评估样本平衡** 检验匹配后两组在协变量上的平衡程度。最近的进展已改善了进行匹配、评估样本平衡和确定对遗漏协变量的敏感性的方法（Rosenbaum, 2010: Part II）
>
> 4. **敏感性测试** 评估结果对未观测协变量（遗漏变量）的敏感性。"敏感性测试可以有所帮助，但除了在极端情况下，很少能提供决定性证据"


> [!contrast-table] 匹配 vs [[Causal Modeling|因果建模]]
> | 维度 | 匹配 | [[Causality\|因果]]建模（SEM） |
> |---|---|---|
> | 变量选择 | 不参考结果变量 | 常涉及模型选择 |
> | 模型选择问题 | 匹配变量锁定后不再搜索 | 所有后续统计推断可能严重错误（Leeb & Pötscher, 2005, 2006） |
> | 对软件依赖 | 较低 | 较高——统计软件包使因果建模看似容易（[[Argument_Berk_2011_ER\|Berk, 2011, p.197]]） |

## 资料与分析

> [!info]
> 匹配后的数据分析需要在匹配样本（而非原始样本）上进行。关键分析步骤包括：检验匹配后两组在协[[Variable|变量]]上的标准化均值差（SMD < 0.1 通常视为平衡良好）；在匹配样本上估计处理效应（平均处理效应 ATT 或 ATE）；通过 Rosenbaum 敏感性分析评估结果对未观测混杂的稳健性。[[Argument_Berk_2011_ER|Berk (2011, p. 198)]] 强调匹配过程中的[[Dependent Variable|结果变量]]应"锁在保险箱里"——匹配变量的选择不得参考结果变量，以避免循环论证。

## 适用场景

> [!method-fit] 适用判断
> - 当随机实验不可行、不道德或成本过高时，匹配提供了从观察数据中推断因果效应的替代方法
> - 当研究人员有过去研究和理论的坚实基础来论证相关协[[Variable|变量]]已被纳入匹配时——因为"样本中的平衡并不意味着未观测协变量也存在平衡"([[Argument_Berk_2011_ER|Berk, 2011, p.198]])
> - 大型观察性研究中"使用匹配来调整混杂因素有时可以提供有启发性的结果"([[Argument_Berk_2011_ER|Berk, 2011, p.195]])

## 局限性

> [!method-limits]
> - **对未观测混杂因素的敏感性** "样本中的平衡并不意味着未观测协[[Variable|变量]]也存在平衡"([[Argument_Berk_2011_ER|Berk, 2011, p.198]])。匹配仅能基于已观测和已包含的协变量建立可比性——如果关键混杂因素未被测量，结果的因果解释仍然脆弱。
> - **需要满足与随机实验相同的[[Hypothesis|假设]]** 匹配不能豁免随机实验所需的关键假设——同样必须满足无干扰（no interference）的 [[Stable Unit Treatment Value Assumption|SUTVA]] 要求([[Argument_Berk_2011_ER|Berk, 2011, p.199]])。
> - **远不如[[Random Assignment|随机化]]** Smith (1991, p. 215) 指出匹配最常用于准实验和非[[Experimental Research|实验研究]]，在排除替代因果解释方面远不如随机化——随机化控制所有变量，匹配只控制命名变量（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 323]]）。
> - **样本缩减风险** 匹配可能导致样本大幅缩减——Lewis-Beck (1993) 报告了一个从 1,194 缩减至 46 的实例（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch15|Cohen et al., 2011, Ch15]]）。
> - **协变量[[Interaction Effect|交互效应]]** "与协变量的交互效应最好通过事后分层（[[Parliamentary Office of Science and Technology|POST]] stratification）来解决，而非因果模型"([[Argument_Berk_2011_ER|Berk, 2011, p.199]])。

## 相关理论与方法

> [!entry-map]
> | 条目 | 类型 | 关系 |
> |---|---|---|
> | [[Potential Outcomes Framework]] | 理论 | 匹配的[[Causality\|因果推断]]逻辑直接建立在潜在结果框架之上 |
> | [[Random Assignment]] | 方法 | 对比参照——随机化控制所有变量，匹配只控制命名变量（Smith, 1991, p. 215） |
> | [[Causal Modeling]] | 方法 | [[Argument_Berk_2011_ER\|Berk (2011)]] 将匹配定位为因果建模的替代路径，认为其较少依赖不可检验模型假设 |
> | [[Covariate Adjustment]] | 方法 | 匹配和协[[Variable\|变量]]控制都试图处理第三变量问题；前者通过样本平衡，后者在模型中纳入协变量 |
> | [[Matched Pairs Design]] | 方法 | 实验设计中的匹配——配对后随机分配，是匹配在真实验中的具体实现 |
> | [[Non-intervention Research]] | 方法 | 匹配属于在非干预数据中改善因果推断的策略 |

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Berk_2011_ER|Berk (2011)]] — 将匹配推荐为[[Causal Modeling|因果建模]]的替代方法，论证其更少依赖不可检验[[Hypothesis|假设]]，更多受实证诊断约束。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch15|Cohen et al. (2011, Ch. 15)]] — 将匹配列为[[Ex Post Facto Research|事后回溯研究]]中最常用的控制手段之一，在因果-比较设计中通过匹配实验组与对照组的关键特征提高可比性；同时指出匹配可能导致样本大幅缩减（Lewis-Beck, 1993 报告从 1,194 缩减至 46 的实例）。

