---
title: Causality
aliases:
  - 因果性
  - 因果关系
  - 因果推断
  - causal inference
  - causation
summary: "教育研究中指原因导致效果的关系，涵盖决定论因果与概率因果两种刻画方式，涉及时间顺序、排除混淆变量、反事实推理和因果过程等核心议题"
type: concept
domain: "research-methodology"
related_count: 8
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - subject/research-methodology
  - paradigm/positivist
related_concepts:
  - "[[Variable]]"
  - "[[Probabilistic Causation]]"
  - "[[Purpose Statement]]"
  - "[[Research Question]]"
  - "[[Counterfactual]]"
  - "[[Fundamental Problem of Causal Inference]]"
  - "[[Necessary and Sufficient Conditions]]"
  - "[[Compound Causes]]"
  - "[[Screening Off]]"
  - "[[Causal Over-determination]]"
  - "[[Homework]]"
  - "[[Causal Processes]]"
  - "[[Rashomon Effect]]"
  - "[[Multiplicity]]"
related_theories: []
related_methods:
  - "[[Quantitative Research]]"
  - "[[Random Assignment]]"
  - "[[Experimental Research]]"
  - "[[Survey Research]]"
  - "[[Intervention Research]]"
  - "[[Mixed Methods Research]]"
  - "[[Ethnography]]"
  - "[[Causal Modeling]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04]]"
confidence: medium
status: draft
created: 2026-05-31
updated: 2026-06-17
---

# Causality

## 定义

> [!def] 核心定义
> 因果性（causality）指原因导致效果的关系。在[[Quantitative Research|量化研究]]中，因果性不仅意味着[[Variable|变量]]间的关联，还要求同时满足三个要件：变量间存在关系的证据；原因在时间上先于结果；排除合理的替代解释（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.56]]）。在更广泛的教育研究语境中，因果性通常不可直接观察而只能推断——社会科学中几乎不可能发现绝对确定的因果性。因果性应当被区分为两种刻画方式：**决定论因果性**（deterministic causation）——X 必然导致 Y；**[[Probabilistic Causation|概率因果性]]**（probabilistic causation）——X 提高 Y 发生的可能性而非保证 Y 发生。教育研究中更恰切的是后者（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 54, 58–59]]）。

> [!concept-lens] 概念透镜
> - **含义**：因果性是变量、事件或过程之间"引起-被引起"的关系，涉及原因如何产生效果以及效果由什么原因导致。
> - **用途**：它帮助研究者超越"什么有效"的简单问题，追问"为什么有效""如何有效""对谁有效""在什么条件下有效"。
> - **边界**：因果性不等于解释（解释可能是错误的）、不等于预测（预测可能基于错误的因果识别）、不等于相关（相关可能由第三变量驱动）。因果性在社会科学中通常是**推断性的**和**概率性的**，而非绝对的逻辑演绎。

> [!quote]
> "Causality means that we would expect variable X to cause variable Y."([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.56]])

## 核心要素

### 时间顺序（Temporal Order）

时间顺序意味着一个[[Variable|变量]]在时间上先于另一个变量。休谟（Hume, 2000）将其列为因果四准则之一——**优先性/先后顺序**（priority/succession）：原因先于效果。由于这种时间排序，一个变量影响或预测另一个变量。时间顺序还意味着[[Quantitative Research|量化研究]]者从左到右思考变量（Punch, 2014），并在[[Purpose Statement|目的陈述]]、[[Research Question|研究问题]]和视觉模型中按此顺序排列变量([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.57]])。

> [!exegesis] 因果的时间与范围问题
> 确定因果关系还需要考虑时间的两个维度：**回溯多远**——如何确定相关的因果历史起点？多年前的旧伤是否应被视为后来骨折的一个原因？**前探多远**——效果可能是短期的、延迟的、即时的、累积的或长期的。癌症发病有几个阶段，不是某一时刻的单一事件。因果的**时间边界**和**范围边界**是研究者的关键决策点（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 64–66]]）。

### 休谟的因果四准则

休谟（Hume, 2000）提出了决定论因果性的经典框架——四准则（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, p. 58]]）：

> [!frames-ref] 休谟的因果四准则
> 1. **时空邻近性**（contiguity of space and time）：原因与效果在时空上邻近。
> 2. **优先性/先后顺序**（priority/succession）：原因先于效果。
> 3. **恒定联结**（constant conjunction）：一个事件及其后继事件的配对反复出现。
> 4. **必然联系**（necessary connection）：从经验、习惯和习俗中习得，而非从演绎的逻辑必然证明中获得。

> [!warrant] 休谟准则的局限
> 休谟的准则中可察觉的实际上是**相关**（correlation）而非真正的因果性。他本人也主张因果性是由人类**归纳推断**的，而非客观事实。这构成了[[Probabilistic Causation|概率因果性]]（[[Probabilistic Causation]]）的哲学起点——教育研究中的因果推断更多是推测性的和概率性的，而非绝对的和演绎的。

### 反事实推理

区分因果是否发生的一个关键指标是**[[Counterfactual|反事实]]**（[[Counterfactual|counterfactuals]]）：如果 X（假设的原因）不存在，那么 Y（效果）也不会发生（Mackie, 1993）。反事实推理追问："如果那个假设的原因不存在，效果还会发生或还是原来那样吗？"如果答案是"否"，则 X 是真正的原因（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 55–56]]）。

在真实验中，反事实问题通过**控制组**来回答——控制组被假定为表明如果干预未发生会发生什么。但大量教育研究并非实验性的，反事实推理因此依赖更不确定的假设和统计建模。Holland（1986: 947）提出了"[[Fundamental Problem of Causal Inference|因果推断的基本问题]]"——同一个人不能同时处于接受和未接受处理的状态——这一问题即使在[[Random Assignment|随机化]]实验中也无法完全解决（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, p. 78]]）。

### 必要条件与充分条件

原因的效果依赖于**条件组合**：是[[Necessary and Sufficient Conditions|必要条件]]与充分条件的特定组合产生了效果，而非单个原因。原因可能需要组合在一起才能发挥因果力——**[[Compound Causes|复合原因]]**（compound causes）只有在共同作用时才施加因果力，且原因之间可能存在**交互效应**（interaction effects）。单个原因在语境化情境中可能既不充分也不必要（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 56–57]]）。

### 混淆变量与筛选隔离

评估因果主张时，一个至关重要的考量是未测量的第三变量 Z 是否导致了结果。例如，在"适度红酒消费降低心脏病风险"的主张中，规律的日常锻炼这一混淆变量 Z 可能既与适度红酒消费正相关，也与心脏病风险降低正相关。如果混淆变量未被测量，研究者可能错误推断因果作用([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.56]])。

更系统的分析框架是 Reichenbach（1956）和 Salmon（1998）提出的**[[Screening Off|筛选隔离]]**（[[Screening Off|screening off]]）：当两个变量被一个共同原因所驱动时，二者之间只有相关关系而无因果关系。例如，气压计读数下降与暴风雨都由气压下降引起，但气压计读数下降不导致暴风雨。在因果分析中，研究者应通过**偏相关**（partial correlation）和**结构方程模型**等技术筛掉无关变量，确保一个变量不被误认为对另一个变量有因果影响（pp.59–60）。Pearl（2009: 423–7）提供了系统识别应被筛选掉的因素的方法（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 59–60]]）。

> [!warning]
> 如果研究目标是检验两个或多个变量之间的因果主张，最佳选择是进行真实验（[[Experimental Research|true experiment]]），因为这能对潜在的未测量变量提供更强的控制。如果对检验因果主张的兴趣较低或无法进行实验，[[Survey Research|调查研究]]方法可以检验变量间假设关联的主张([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.57]])。

## 概念辨析

> [!contrast-table] 因果性 vs 解释 vs 预测 vs 相关
> | 概念 | 与因果性的区别 | 典型例示 |
> |------|---------------|---------|
> | **解释**（explanation） | 解释可能是错误的、说明含义的或指示操作方法的（Salmon, 1998: 5–8） | 以生病为由请假，实际原因可能是偷懒或逛街 |
> | **预测**（prediction） | 观察到一次不等于能预测再次发生（归纳问题）；预测正确可能基于错误的因果识别 | 气压计读数下降预测暴风雨，但气压计不导致暴风雨 |
> | **相关**（correlation） | 两个[[Variable\|变量]]可能被共同原因[[Screening Off\|筛选隔离]]，彼此只有相关无因果 | 手大与脚大由遗传倾向共同驱动 |
> | **因果性**（causation） | X 对 Y 施加因果影响——X"引起"或"产生"了 Y | 气压下降导致气压计读数变化**和**暴风雨 |

> [!example]
> **关联（association）vs 因果（causation）**。流行病学健康科学研究强调适度每日红酒消费（每天 1–2 杯）与心脏病风险降低 20% 之间存在正关联（Szmitko & Verma, 2005），但这不等同于因果。关联是因果的[[Necessary and Sufficient Conditions|必要条件]]而非充分条件([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.57]])。

## 因果过度决定

> [!def] [[Causal Over-determination|因果过度决定]]
> 一个特定效果是多个原因的产物，而其中每一个原因本身都足以单独产生该效果（Morrison, 2009: 51）。例如，两发子弹同时击中一人头部——哪一发导致死亡？每发子弹单独看都足以致命。在教育中，学生成绩提升可能同时由更多[[Homework|家庭作业]]、家长压力、金钱激励和学校压力导致——任何一项单独都可能产生效果（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 63–64]]）。

因果过度决定挑战了教育[[Intervention Research|干预研究]]中常见的主张——即某项干预"独自"改善了表现。效果很少由单一原因产生。

## 因果过程与行动叙事

因果性不仅是[[Variable|变量]]的输入-输出关系，更应当被视为**动态过程**而非静态事件。X 如何导致 Y？在 X 中发生了什么才导致了 Y？理解[[Causal Processes|因果过程]]需要高粒度地考察动机、意志、理由、理解、感知、个体性、条件和语境，以及因素之间的动态互动——通常是历时性的（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 71–72]]）。

### 罗生门效应与多重因果路径

[[Rashomon Effect|罗生门效应]]（Rashomon Effect）揭示了因果解释的[[Multiplicity|多重性]]：同一事件被不同行动者以矛盾且不可兼容的因果叙事加以解释（Roth & Mehta, 2002）。电影《罗生门》中，武士之死有四种自相矛盾的因果叙事——每个叙事都服务于讲述者的利益。教育研究中的启示是：存在多重因果路径，而非简单的输入-输出模型。质性数据在揭示这些因果过程方面占据优先地位，因为它能"进入情境中行动者的头脑"（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 72–74]]）。

## 建立因果性的策略

### 研究原因之效果 vs 研究效果之原因

建立因果性有两种基本策略（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 74–92]]）：

> [!contrast-table] 两种因果研究策略
> | 维度 | 研究原因之效果 | 研究效果之原因 |
> |------|--------------|--------------|
> | **方向** | 前向——施加干预，观察效果 | 后向——从效果回溯寻找原因 |
> | **典型方法** | [[Experimental Research\|实验法]]、行动研究、调查分析、观察法 | 事后回溯研究、七步推理过程（Morrison, 2009） |
> | **确定性** | 相对较高——能操纵[[Variable\|变量]] | 更尝试性和推断性——数据不完整 |
> | **核心挑战** | 隔离与控制全部变量、[[Causal Processes\|因果过程]]可能被忽视 | 从海量潜在原因中确定真正原因、竞争假设的检验 |

> [!tip] [[Mixed Methods Research|混合方法]]路径
> 本章主张混合方法论和混合方法在研究和建立因果性方面的独特力量：量化方法（实验、调查）检验规律性和变量间的关联，质性方法（观察、访谈、[[Ethnography|民族志]]）揭示因果过程如何在具体情境中运作——即因果的"如何"。二者结合能同时回答因果的"是什么"和"如何"（pp.91–92）。

### 竞争解释的检验

建立因果解释的一种稳健方式是：观察规律性后，检验对这些规律性的**竞争解释**和**竞争假设**。最好的因果解释建立在最全面的理论之上——拥抱意向性、能动性、互动和结构——并在不同于产生该理论的语境和数据中得到检验。检验竞争假设必须使用不同于产生假设的数据，以避免循环论证（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 70, 92]]）。

## 理论基础

> [!tip]
> Blalock (1969, 1985, 1991) 是[[Quantitative Research|量化研究]]领域[[Causal Modeling|因果建模]]的主要倡导者，主张将口头理论重构为因果模型，使读者能够可视化[[Variable|变量]]之间的相互联系。他提出了构建视觉因果图的基本符号规则：因变量置于右侧、自变量置于左侧；使用单向箭头表示因果方向；在路径上插入正负价符号表示关系方向；使用双向箭头连接模型中不受其他关系约束的变量之间的未分析关系([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.58]])。

## 相关方法

- [[Causal Modeling]] — 因果建模是将因果性概念操作化的主要统计方法
- [[Quantitative Research]] — 量化研究以检验[[Variable|变量]]间因果关系为核心目标之一
- [[Experimental Research]] — 真实验是检验因果主张的最强设计

