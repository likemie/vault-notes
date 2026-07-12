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
related_count: 31
related_level: 3
related_stars: "⭐⭐⭐"
related_color: "#fde68a"
tags:
  - subject/research-methodology
  - paradigm/positivist
related_concepts:
  - "[[Variable]]"
  - "[[Probabilistic Causation]]"
  - "[[Effect Size]]"
  - "[[Screening Off]]"
  - "[[Necessary and Sufficient Conditions]]"
  - "[[Purpose Statement]]"
  - "[[Research Question]]"
  - "[[Counterfactual]]"
  - "[[Hypothesis]]"
  - "[[Operationalization]]"
  - "[[Compound Causes]]"
  - "[[Interaction Effect]]"
  - "[[Causal Over-determination]]"
  - "[[Homework]]"
  - "[[Causal Processes]]"
  - "[[Rashomon Effect]]"
  - "[[Multiplicity]]"
  - "[[Action Narratives]]"
  - "[[Fundamental Problem of Causal Inference]]"
  - "[[Emergence]]"
related_theories: []
related_methods:
  - "[[Quantitative Research]]"
  - "[[Pretest-Posttest Control Group Design]]"
  - "[[Random Assignment]]"
  - "[[Experimental Research]]"
  - "[[Ex Post Facto Research]]"
  - "[[Ethnography]]"
  - "[[Mixed Methods Research]]"
  - "[[Causal Modeling]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
confidence: medium
status: draft
created: 2026-05-31
updated: 2026-07-13
---

# Causality

因果推断（causal inference）是教育研究中最核心也最具挑战性的任务之一——它追问"X 是否导致了 Y"以及"X 如何导致 Y"，并在此基础上回答"什么有效、为什么有效、对谁有效、在什么条件下有效"。教育研究中的因果推断通常是概率性的和基于证据的，而非绝对确定的逻辑演绎。

## 定义

> [!def] 核心定义
> 因果推断（causal inference）指通过研究设计和数据分析，建立原因与效果之间关系的推理过程。在[[Quantitative Research|量化研究]]中，一个有效的因果推断需要同时满足三个要件：[[Variable|变量]]间存在关系的证据；原因在时间上先于结果；排除合理的替代解释（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.56]]）。因果性有两种刻画方式：**决定论因果性（deterministic causation）**——X 必然导致 Y；**[[Probabilistic Causation|概率因果性]]（probabilistic causation）**——X 提高 Y 发生的可能性。教育研究中更恰切的是后者——社会科学中几乎不可能发现绝对确定的因果性（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 54, 58–59]]）。

> [!concept-lens] 因果推断的操作含义
> - **含义** 因果推断是建立"X 引起 Y"这一主张的推理过程，涉及设计（如何收集能支持因果推断的数据）、分析（如何从数据中分离因果效应）和论证（如何排除替代解释）。
> - **用途** 因果推断超越"什么有效"的简单问题，追问"**为什么**有效""**如何**有效""**对谁**有效""**在什么条件下**有效"——这四个追问构成了教育研究中因果推断的完整框架。
> - **边界** 因果推断不等于解释（解释可能错误）、不等于预测（预测可能基于错误的因果识别）、不等于相关（相关可能由第三变量驱动）。因果推断在社会科学中始终是概率性的——研究者积累证据支持因果主张，而非一劳永逸地证明因果关系。

> [!formula-step] 真实验中的平均因果[[Effect Size|效应量]]化
> 在[[Pretest-Posttest Control Group Design|前后测控制组设计]]中，平均因果效应可通过以下公式量化（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 314]]）：
>
> $$\text{平均因果效应} = (E_1 - E_2) - (C_1 - C_2)$$
>
> - **数学解释** E₁ = 实验组后测，E₂ = 实验组前测，C₁ = 控制组后测，C₂ = 控制组前测。(E₁−E₂) 是实验组的干预+自然变化，(C₁−C₂) 是控制组的纯自然变化，两者相减得纯净的干预效应。
> - **前提条件** 依赖于**其他条件不变（ceteris paribus）**——除干预外，两组在所有其他方面完全相同。[[Random Assignment|随机化]]正是试图满足这一前提的关键手段（Morrison, 2009, pp. 143–144）。

> [!quote]
> "Causality means that we would expect variable X to cause variable Y."([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.56]])

---

## 概念辨析

> [!contrast-table] 因果性 vs 解释 vs 预测 vs 相关
> | 概念 | 与因果性的区别 | 典型例示 |
> |------|---------------|---------|
> | **解释（explanation）** | 解释可能是错误的、说明含义的或指示操作方法的（Salmon, 1998: 5–8） | 以生病为由请假，实际原因可能是偷懒或逛街 |
> | **预测（prediction）** | 观察到一次不等于能预测再次发生（归纳问题）；预测正确可能基于错误的因果识别 | 气压计读数下降预测暴风雨，但气压计不导致暴风雨 |
> | **相关（correlation）** | 两个[[Variable\|变量]]可能被共同原因[[Screening Off\|筛选隔离]]，彼此只有相关无因果 | 手大与脚大由遗传倾向共同驱动 |
> | **因果性（causation）** | X 对 Y 施加因果影响——X 引起或产生了 Y | 气压下降同时导致气压计读数变化和暴风雨 |

> [!example]
> **关联（association）vs 因果（causation）**。流行病学健康科学研究强调适度每日红酒消费（每天 1–2 杯）与心脏病风险降低 20% 之间存在正关联（Szmitko & Verma, 2005），但这不等同于因果。关联是因果的[[Necessary and Sufficient Conditions|必要条件]]而非充分条件（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.57]]）。

---

## 核心要素

### 因果推断的基本结构：时间顺序与边界条件

进行因果推断时，两个结构化前提必须满足——原因先于效果，且因果判断的范围必须被明确界定。

> [!feature] 因果性的结构化前提
> - **时间顺序** 原因必须在时间上先于效果。休谟（Hume, 2000）将其列为因果准则之一。[[Quantitative Research|量化研究]]者在[[Purpose Statement|目的陈述]]、[[Research Question|研究问题]]和视觉模型中按从左到右排列[[Variable|变量]]（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.57]]）。
> - **边界条件** 确定因果关系需要考虑回溯多远（因果历史起点）和前探多远（效果可能是短期的、延迟的、即时的、累积的或长期的）。Pearl（2009: 420）提出了边界条件（boundary conditions）和限定（circumscription）概念——哪些因素被纳入或排除会影响因果判断，危险在于循环性：只对感兴趣的效果寻找可能的原因，因未考虑替代解释而误判因果（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 64–66]]）。

> [!frames-ref] 休谟的因果四准则
> 休谟（Hume, 2000）提出了决定论因果性的经典框架（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, p. 58]]）：
> 1. **时空邻近性（contiguity of space and time）** 原因与效果在时空上邻近
> 2. **优先性/先后顺序（priority/succession）** 原因先于效果
> 3. **恒定联结（constant conjunction）** 一个事件及其后继事件的配对反复出现
> 4. **必然联系（necessary connection）** 从经验、习惯和习俗中习得，而非从演绎证明中获得

> [!warrant]- 休谟准则的哲学含义
> 这些准则中可察觉的实际上是**相关**而非真正的因果性——因果性是由人类归纳推断的，而非客观事实。这构成了[[Probabilistic Causation|概率因果性]]的哲学起点：教育研究中的因果推断更多是推测性的和概率性的，而非绝对的和演绎的。

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

> [!info] 教育研究中的因果性现实
> 在一个多重因果、交互关联的世界中，条件和交互可能比线性决定论提供更好的因果说明。原因通常提高效果的可能性而非保证效果的发生（Mellor, 1995: 69–70），且最强的概率也不总是等同于最强的因果性（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, p. 59]]）。

---

### 因果推断的底层逻辑是反事实比较

所有因果推断在逻辑上都依赖同一个操作：比较"有 X"的世界与"没有 X"的世界中 Y 的差异。[[Counterfactual|反事实推理]]提供了这一比较的逻辑框架——它是因果推断的推理引擎，而非一个并列概念。

> [!def] 反事实推理
> **[[Counterfactual|反事实]]（counterfactuals）**指"如果[[Hypothesis|假设]]的原因不存在，效果是否还会发生"。如果答案是否，则 X 是真正的原因（Mackie, 1993; [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 55–56]]）。

> [!chain-link] 从反事实到因果推断的逻辑链条
> - **反事实问题** 如果干预未发生，结果会怎样？这是因果推断必须回答的根本问题。
> - **Holland 的基本问题** 同一个人不能同时处于接受和未接受处理的状态——因此个体层面的反事实**永远不可观察（Holland, 1986, p. 947）**。
> - **实验的[[Operationalization|操作化]]回答** 通过[[Random Assignment|随机化]]将参与者分为控制组和实验组，用控制组的平均结果**替代**实验组在反事实世界中的结果。随机化使两组在期望上等价。
> - **数学表达** 参见上方的平均因果效应公式。控制组的 O₄−O₃ 近似于实验组若无干预时的变化，(E₁−E₂)−(C₁−C₂) 即得纯净的干预效应（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 314]]）。

> [!dimension] Schneider et al. (2007) 的三种统计应对方案
> - **重复测量策略**
>   将同一人先放入控制组再放入实验组，假定时间稳定性且第一次分组不污染第二次反应（cf. Holland, 1986, p. 948）。
> - **完全等同假定**
>   假定所有参与者完全等同，在物理科学中可能成立但在人类科学中极不可能，即使在双胞胎研究中也存疑（Holland, 1986, p. 947）。
> - **平均结果策略**
>   关注平均分数，但可能掩盖子群间的重要差异（如高智商与低智商学生表现迥异），可通过分层子样本应对（Holland, 1986, p. 948）。

在非[[Experimental Research|实验研究]]中，反事实推理依赖更不确定的假设和统计建模——控制组不再存在，反事实必须通过统计手段（如匹配、工具变量、断点回归）来构建。Holland (1986, p. 947) 建议通过[[Random Assignment|随机化]]和平均效应的测量来统计解决基本问题（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 314]]）。

---

### 因果推断需要区分必要、充分与复合原因

单称"X 导致 Y"在逻辑上是不完整的——X 可能在有某些条件时产生效果、在另一些条件时不产生效果。因果推断的精度取决于是否识别了这些条件。

> [!claim] 因果效果依赖条件组合
> 是[[Necessary and Sufficient Conditions|必要条件]]与充分条件的特定组合产生了效果，而非单个原因。原因可能需要组合在一起才能发挥因果力——**[[Compound Causes|复合原因]]（compound causes）**只有在共同作用时才施加因果力，且原因之间可能存在**[[Interaction Effect|交互效应]]（interaction effects）**。单个原因在语境化情境中可能既不充分也不必要（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 56–57]]）。

---

### 因果推断必须排除混淆变量

> [!def] [[Screening Off|筛选隔离]]
> 评估因果主张时的一个重要考量是未测量的第三变量是否导致了结果。Reichenbach (1956) 和 Salmon (1998) 提出的筛选隔离（screening off）框架指出：当两个变量被一个共同原因所驱动时，二者之间只有相关关系而无因果关系。在因果分析中，应通过**偏相关**和**结构方程模型**等技术筛掉无关变量，确保一个变量不被误认为对另一个变量有因果影响（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 59–60]]；[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.56]]）。

> [!warning]
> 如果研究目标是检验两个或多个变量之间的因果主张，最佳选择是进行真实验（[[Experimental Research|true experiment]]），因为这能对潜在的未测量变量提供更强的控制（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.57]]）。

---

## 围绕概念形成的命题

### 单一原因的归因需要更谨慎的论证

> [!claim] [[Causal Over-determination|因果过度决定]]
> 一个特定效果是多个原因的产物，而其中每一个原因本身都足以单独产生该效果（Morrison, 2009: 51）。例如，两发子弹同时击中一人头部——每发子弹单独都足以致命；学生成绩提升可能同时由[[Homework|家庭作业]]、家长压力、金钱激励和学校压力导致——任何一项单独都可能产生效果（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 63–64]]）。因果过度决定意味着单一原因的归因需要更谨慎的论证——效果很少由单一原因产生。

---

### 因果推断不能止步于变量关联

> [!claim] 因果性是动态过程而非静态事件
> 因果性不仅是[[Variable|变量]]的输入-输出关系，更应当被视为**动态过程**而非静态事件。理解[[Causal Processes|因果过程]]需要高粒度地考察动机、意志、理由、理解、感知、个体性、条件和语境，以及因素之间的动态互动（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 71–72]]）。

> [!info] [[Rashomon Effect|罗生门效应]]与因果解释的[[Multiplicity|多重性]]
> 同一事件被不同行动者以矛盾且不可兼容的因果叙事加以解释（Roth & Mehta, 2002）。教育研究中的启示是：存在多重因果路径，而非简单的输入-输出模型。[[Action Narratives|行动叙事]]在揭示这些因果过程方面具有核心重要性，质性数据能进入情境中行动者的头脑（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 72–74]]）。

---

### 因果推断有两条互补的操作路径

> [!contrast-table] 两种因果研究策略
> | 维度 | 研究原因之效果 | 研究效果之原因 |
> |------|--------------|--------------|
> | **方向** | 前向——施加干预，观察效果 | 后向——从效果回溯寻找原因 |
> | **典型方法** | [[Experimental Research\|实验法]]、行动研究、调查分析、观察法 | [[Ex Post Facto Research\|事后回溯研究]]、七步推理过程（Morrison, 2009） |
> | **确定性** | 相对较高——能操纵[[Variable\|变量]] | 更尝试性和推断性——数据不完整 |
> | **核心挑战** | 隔离与控制全部变量、[[Causal Processes\|因果过程]]可能被忽视 | 从海量潜在原因中确定真正原因、竞争[[Hypothesis\|假设]]的检验 |

> [!conclusion] 两种策略互补
> 量化方法（实验、调查）检验规律性和变量关联，质性方法（观察、访谈、[[Ethnography|民族志]]）揭示因果过程如何运作。[[Mixed Methods Research|混合方法]]能同时回答因果的是什么和如何（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 74–92]]）。

---

### 因果推断的可信度来自排除竞争解释

> [!claim] 竞争解释与最佳因果解释
> 建立因果解释的一种稳健方式是：观察规律性后，检验对这些规律性的**竞争解释**和**竞争假设**。最好的因果解释建立在最全面的理论之上——拥抱意向性、能动性、互动和结构——并在不同于产生该理论的语境和数据中得到检验。检验竞争假设必须使用不同于产生假设的数据，以避免循环论证（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 70, 92]]）。

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

## 实证数据

> [!evidence-grid-a] 实证发现索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04]] — 系统梳理教育研究中因果推断的核心议题：[[Probabilistic Causation|概率因果性]]、[[Counterfactual|反事实推理]]、[[Screening Off|筛选隔离]]、[[Causal Over-determination|因果过度决定]]、[[Action Narratives|行动叙事]]，以及研究原因之效果与效果之原因的两种策略
> - [[Argument_Creswell_2022_SAGE]] — 从[[Quantitative Research|量化研究]]角度定义因果性的三要件（关联证据、时间顺序、排除替代解释），并介绍 Blalock [[Causal Modeling|因果建模]]传统

---

## 争议与批评

> [!debates] 核心争议
>
> > [!axis] 量化 vs 质性路径
> > 量化方法能识别[[Variable|变量]]关联和规律性，但不能揭示因果如何运作（how）；质性方法能揭示[[Causal Processes|因果过程]]，但难以建立可推广的因果结论。
> >
> > - **量化路径** 实验、回归、结构方程——检验规律性和变量关联，识别原因之效果。
> > - **质性路径** 观察、访谈、[[Ethnography|民族志]]——揭示因果过程如何运作，理解效果之原因。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|(Cohen et al., 2011, pp. 74–92)]]
>
> > [!axis] 线性 vs 非线性因果
> > 许多因果模型预设线性关系，但因果效果可能是非线性的。因果网络和因果条件比因果线或因果事件链更恰切（Cohen & Stewart, 1995）。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, Ch16, p. 319)]]
>
> > [!axis] 实验方法的基本前提是否成立
> > 实验方法[[Hypothesis|假设]]单一原因产生效应、变量可在封闭系统中被隔离和控制——这些前提在复杂社会现象和开放系统中可能不成立。
> >
> > - **Hage & Meeker (1988, p. 55)** 单一原因假设在复杂社会现象中可能不成立。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, Ch16, p. 314)]]
> > - **Morrison (2001)** [[Emergence|涌现]]、动态系统和开放系统使实验室逻辑失效。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, Ch16, p. 319)]]
> > - **Maxwell (2004)** 情境效应（setting effect）——实际产生因果效应的是情境而非干预本身。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, Ch16, p. 314)]]

---

## 应用案例

> [!case] 冰面摔倒——多重因果的完整展示
> 冰面导致摔倒骨折。但[[Counterfactual|反事实推理]]表明：冰只是众多促成原因之一，不是充分原因。其他因素（平衡感差、视力不佳、环境黑暗、鞋底滑、骨质脆）合在一起才构成[[Necessary and Sufficient Conditions|充分条件]]组合。这一案例同时展示了反事实推理、[[Compound Causes|复合原因]]、必要条件与充分条件的区分。

> [!case] 阅读时间与阅读能力——[[Causal Processes|因果过程]]的"望远镜"式展开
> 增加阅读时间导致阅读能力提高看似简单因果，但增加时间如何转化为能力提升涉及至少 18 个维度的因果过程（动机、专注、兴趣、难度、目的、环境、教师支持等）。简单的输入[[Variable|变量]]可能只是众多原因之一，或是一个伞状术语，或解放了一系列其他原因。确定效果的真实原因极其困难（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 75–76]]）。
