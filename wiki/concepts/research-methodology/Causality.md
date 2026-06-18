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
  - "[[Causal Processes]]"
  - "[[Rashomon Effect]]"
  - "[[Action Narratives]]"
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
updated: 2026-06-18
---

# Causality

## 定义

> [!def] 核心定义
> 因果性（causality）指原因导致效果的关系。在[[Quantitative Research|量化研究]]中，因果性不仅意味着[[Variable|变量]]间的关联，还要求同时满足三个要件：变量间存在关系的证据；原因在时间上先于结果；排除合理的替代解释（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.56]]）。在更广泛的教育研究语境中，因果性通常不可直接观察而只能推断——社会科学中几乎不可能发现绝对确定的因果性。因果性应当被区分为两种刻画方式：**决定论因果性**（deterministic causation）——X 必然导致 Y；**[[Probabilistic Causation|概率因果性]]**（probabilistic causation）——X 提高 Y 发生的可能性而非保证 Y 发生。教育研究中更恰切的是后者（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 54, 58–59]]）。

> [!concept-lens] 概念透镜
> - **含义**：因果性是变量、事件或过程之间"引起-被引起"的关系，涉及原因如何产生效果以及效果由什么原因导致。
> - **用途**：它帮助研究者超越"什么有效"的简单问题，追问"为什么有效""如何有效""对谁有效""在什么条件下有效"。
> - **边界**：因果性不等于解释（解释可能是错误的）、不等于预测（预测可能基于错误的因果识别）、不等于相关（相关可能由第三变量驱动）。因果性在社会科学中通常是推断性的和概率性的，而非绝对的逻辑演绎。

> [!quote]
> "Causality means that we would expect variable X to cause variable Y."([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.56]])

---

## 概念辨析

> [!contrast-table] 因果性 vs 解释 vs 预测 vs 相关
> | 概念 | 与因果性的区别 | 典型例示 |
> |------|---------------|---------|
> | **解释**（explanation） | 解释可能是错误的、说明含义的或指示操作方法的（Salmon, 1998: 5–8） | 以生病为由请假，实际原因可能是偷懒或逛街 |
> | **预测**（prediction） | 观察到一次不等于能预测再次发生（归纳问题）；预测正确可能基于错误的因果识别 | 气压计读数下降预测暴风雨，但气压计不导致暴风雨 |
> | **相关**（correlation） | 两个[[Variable\|变量]]可能被共同原因[[Screening Off\|筛选隔离]]，彼此只有相关无因果 | 手大与脚大由遗传倾向共同驱动 |
> | **因果性**（causation） | X 对 Y 施加因果影响——X 引起或产生了 Y | 气压下降同时导致气压计读数变化和暴风雨 |

> [!example]
> **关联（association）vs 因果（causation）**。流行病学健康科学研究强调适度每日红酒消费（每天 1–2 杯）与心脏病风险降低 20% 之间存在正关联（Szmitko & Verma, 2005），但这不等同于因果。关联是因果的[[Necessary and Sufficient Conditions|必要条件]]而非充分条件（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.57]]）。

---

## 核心要素

### 时间顺序、边界条件与休谟准则

> [!feature] 因果性的结构化前提
> - **时间顺序**：原因必须在时间上先于效果。休谟（Hume, 2000）将其列为因果准则之一。[[Quantitative Research|量化研究]]者在[[Purpose Statement|目的陈述]]、[[Research Question|研究问题]]和视觉模型中按从左到右排列[[Variable|变量]]（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.57]]）。
> - **边界条件**：确定因果关系需要考虑回溯多远（因果历史起点）和前探多远（效果可能是短期的、延迟的、即时的、累积的或长期的）。Pearl（2009: 420）提出了边界条件（boundary conditions）和限定（circumscription）概念——哪些因素被纳入或排除会影响因果判断，危险在于循环性：只对感兴趣的效果寻找可能的原因，因未考虑替代解释而误判因果（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 64–66]]）。

> [!frames-ref] 休谟的因果四准则
> 休谟（Hume, 2000）提出了决定论因果性的经典框架（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, p. 58]]）：
> 1. **时空邻近性**（contiguity of space and time）：原因与效果在时空上邻近
> 2. **优先性/先后顺序**（priority/succession）：原因先于效果
> 3. **恒定联结**（constant conjunction）：一个事件及其后继事件的配对反复出现
> 4. **必然联系**（necessary connection）：从经验、习惯和习俗中习得，而非从演绎证明中获得

休谟本人也指出，这些准则中可察觉的实际上是**相关**而非真正的因果性——因果性是由人类归纳推断的，而非客观事实。这构成了[[Probabilistic Causation|概率因果性]]的哲学起点：教育研究中的因果推断更多是推测性的和概率性的，而非绝对的和演绎的。

---

### 决定论因果性 vs 概率因果性

> [!contrast-table] 两种因果刻画方式
> | 维度 | 决定论因果性 | [[Probabilistic Causation\|概率因果性]] |
> |------|-----------|-------------------------------|
> | 因果关系 | X 必然导致 Y | X 提高 Y 发生的可能性 |
> | 认知方式 | 逻辑演绎 | 归纳推断 |
> | 确定性 | 100% 确定 | 不完全确定 |
> | 社会科学适用性 | 较低——过度简化多重因果现实 | 较高——承认语境和不确定性 |
> | 原因-效果关系 | 预设线性、规则关系 | 可能呈现非线性、不规则模式 |

决定论因果性是经典刻画方式——休谟四准则是其代表。但教育研究中几乎不可能发现绝对确定的因果性。在一个多重因果、交互关联的世界中，条件和交互可能比线性决定论提供更好的因果说明。原因通常提高效果的可能性而非保证效果的发生（Mellor, 1995: 69–70）；最强的概率也不总是等同于最强的因果性（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, p. 59]]）。

---

### 反事实推理

区分因果是否发生的一个关键指标是**[[Counterfactual|反事实]]**（counterfactuals）：如果 X（假设的原因）不存在，那么 Y（效果）也不会发生（Mackie, 1993）。反事实推理追问："如果那个假设的原因不存在，效果还会发生或还是原来那样吗？"如果答案是"否"，则 X 是真正的原因（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 55–56]]）。

在真实验中，反事实问题通过**控制组**来回答——控制组被假定为表明如果干预未发生会发生什么。但大量教育研究并非实验性的，反事实推理因此依赖更不确定的假设和统计建模。Holland（1986: 947）提出了"[[Fundamental Problem of Causal Inference|因果推断的基本问题]]"——同一个人不能同时处于接受和未接受处理的状态——这一问题即使在[[Random Assignment|随机化]]实验中也无法完全解决（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, p. 78]]）。

---

### 必要条件、充分条件与复合原因

原因的效果依赖于**条件组合**：是[[Necessary and Sufficient Conditions|必要条件]]与充分条件的特定组合产生了效果，而非单个原因。原因可能需要组合在一起才能发挥因果力——**[[Compound Causes|复合原因]]**（compound causes）只有在共同作用时才施加因果力，且原因之间可能存在**交互效应**（interaction effects）。单个原因在语境化情境中可能既不充分也不必要（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 56–57]]）。

---

### 混淆变量与筛选隔离

评估因果主张时的一个重要考量是未测量的第三变量是否导致了结果。更系统的分析框架是 Reichenbach（1956）和 Salmon（1998）提出的**[[Screening Off|筛选隔离]]**（screening off）：当两个变量被一个共同原因所驱动时，二者之间只有相关关系而无因果关系。在因果分析中，应通过**偏相关**和**结构方程模型**等技术筛掉无关变量，确保一个变量不被误认为对另一个变量有因果影响（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 59–60]]；[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.56]]）。

> [!warning]
> 如果研究目标是检验两个或多个变量之间的因果主张，最佳选择是进行真实验（[[Experimental Research|true experiment]]），因为这能对潜在的未测量变量提供更强的控制（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.57]]）。

---

## 围绕概念形成的命题

### 因果过度决定

> [!claim] [[Causal Over-determination|因果过度决定]]
> 一个特定效果是多个原因的产物，而其中每一个原因本身都足以单独产生该效果（Morrison, 2009: 51）。例如，两发子弹同时击中一人头部——每发子弹单独都足以致命；学生成绩提升可能同时由[[Homework|家庭作业]]、家长压力、金钱激励和学校压力导致——任何一项单独都可能产生效果（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 63–64]]）。因果过度决定意味着单一原因的归因需要更谨慎的论证——效果很少由单一原因产生。

---

### 因果过程与行动叙事

因果性不仅是[[Variable|变量]]的输入-输出关系，更应当被视为**动态过程**而非静态事件。理解[[Causal Processes|因果过程]]需要高粒度地考察动机、意志、理由、理解、感知、个体性、条件和语境，以及因素之间的动态互动（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 71–72]]）。

[[Rashomon Effect|罗生门效应]]进一步揭示了因果解释的[[Multiplicity|多重性]]：同一事件被不同行动者以矛盾且不可兼容的因果叙事加以解释（Roth & Mehta, 2002）。教育研究中的启示是：存在多重因果路径，而非简单的输入-输出模型。[[Action Narratives|行动叙事]]在揭示这些因果过程方面具有核心重要性，质性数据能进入情境中行动者的头脑（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 72–74]]）。

---

### 建立因果性的策略

> [!contrast-table] 两种因果研究策略
> | 维度 | 研究原因之效果 | 研究效果之原因 |
> |------|--------------|--------------|
> | **方向** | 前向——施加干预，观察效果 | 后向——从效果回溯寻找原因 |
> | **典型方法** | [[Experimental Research\|实验法]]、行动研究、调查分析、观察法 | 事后回溯研究、七步推理过程（Morrison, 2009） |
> | **确定性** | 相对较高——能操纵[[Variable\|变量]] | 更尝试性和推断性——数据不完整 |
> | **核心挑战** | 隔离与控制全部变量、[[Causal Processes\|因果过程]]可能被忽视 | 从海量潜在原因中确定真正原因、竞争假设的检验 |

两种策略互补：量化方法（实验、调查）检验规律性和变量关联，质性方法（观察、访谈、[[Ethnography|民族志]]）揭示因果过程如何运作。[[Mixed Methods Research|混合方法]]能同时回答因果的"是什么"和"如何"（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 74–92]]）。

---

### 竞争解释与最佳因果解释

建立因果解释的一种稳健方式是：观察规律性后，检验对这些规律性的**竞争解释**和**竞争假设**。最好的因果解释建立在最全面的理论之上——拥抱意向性、能动性、互动和结构——并在不同于产生该理论的语境和数据中得到检验。检验竞争假设必须使用不同于产生假设的数据，以避免循环论证（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 70, 92]]）。

---

## 概念演变

> [!timeline] 因果性概念的发展
> - **18世纪** — 休谟（Hume）提出因果四准则（时空邻近性、优先性、恒定联结、必然联系），指出因果性是人类归纳推断而非客观事实
> - **1956** — Reichenbach 提出[[Screening Off|筛选隔离]]（screening off）概念，区分相关与因果
> - **1969–1991** — Blalock 倡导将口头理论重构为因果模型，建立视觉因果图的基本符号规则（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.58]]）
> - **1986** — Holland 提出"[[Fundamental Problem of Causal Inference|因果推断的基本问题]]"：个体层面[[Counterfactual|反事实]]永远不可观察
> - **1993** — Mackie 将反事实推理系统引入因果分析
> - **1998** — Salmon 进一步发展筛选隔离概念，强调[[Causal Processes|因果过程]]而非因果事件
> - **2009** — Pearl 提出边界条件和限定概念，系统化因果推断中的[[Variable|变量]]选择问题；Morrison 提出从效果追溯原因的七步推理过程

---

## 实证发现

> [!evidence-grid-a] 实证发现索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04]] — 系统梳理教育研究中因果推断的核心议题：[[Probabilistic Causation|概率因果性]]、[[Counterfactual|反事实推理]]、[[Screening Off|筛选隔离]]、[[Causal Over-determination|因果过度决定]]、[[Action Narratives|行动叙事]]，以及研究原因之效果与效果之原因的两种策略
> - [[Argument_Creswell_2022_SAGE]] — 从[[Quantitative Research|量化研究]]角度定义因果性的三要件（关联证据、时间顺序、排除替代解释），并介绍 Blalock [[Causal Modeling|因果建模]]传统

---

## 争议与批评

> [!tension] 核心争议
> - **决定论 vs 概率论**：教育研究中绝对确定的因果性几乎不可能被发现——[[Probabilistic Causation|概率因果性]]是更恰切的刻画方式。但接受概率因果性意味着研究结论永远带有不确定性。
> - **量化 vs 质性路径**：量化方法（实验、回归、结构方程）能识别[[Variable|变量]]关联和规律性，但不能揭示因果如何运作（how）；质性方法能揭示[[Causal Processes|因果过程]]，但难以建立可推广的因果结论。[[Mixed Methods Research|混合方法]]被主张为综合路径。
> - **线性 vs 非线性因果**：许多因果模型预设线性关系，但因果效果可能是非线性的——小原因可能产生大效果、无效果或不规则效果。因果网络和因果条件比因果线或因果事件链更恰切。

---

## 应用案例

> [!case] 冰面摔倒——多重因果的完整展示
> 冰面导致摔倒骨折。但[[Counterfactual|反事实推理]]表明：冰只是众多促成原因之一，不是充分原因。其他因素（平衡感差、视力不佳、环境黑暗、鞋底滑、骨质脆）合在一起才构成[[Necessary and Sufficient Conditions|充分条件]]组合。这一案例同时展示了反事实推理、[[Compound Causes|复合原因]]、必要条件与充分条件的区分。

> [!case] 阅读时间与阅读能力——[[Causal Processes|因果过程]]的"望远镜"式展开
> 增加阅读时间导致阅读能力提高看似简单因果，但增加时间如何转化为能力提升涉及至少 18 个维度的因果过程（动机、专注、兴趣、难度、目的、环境、教师支持等）。简单的输入[[Variable|变量]]可能只是众多原因之一，或是一个伞状术语，或解放了一系列其他原因。确定效果的真实原因极其困难（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 75–76]]）。
