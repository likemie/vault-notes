---
title: Independent Variable
aliases:
  - 自变量
  - independent variables
  - predictor variable
  - 预测变量
  - treatment variable
  - manipulated variable
summary: "实验或量化研究中被有意识操纵、控制或选择以观察其对因变量效应的变量，是因果推断中的输入条件"
type: concept
domain: "research-methodology"
related_count: 15
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - subject/research-methodology
  - paradigm/positivist
  - causal-inference
  - experiment
related_concepts:
  - "[[Variable]]"
  - "[[Dependent Variable]]"
  - "[[Causality]]"
  - "[[Operationalization]]"
  - "[[Construct]]"
  - "[[Definition of Terms]]"
  - "[[Interaction Effect]]"
  - "[[School Effectiveness]]"
related_theories: []
related_methods:
  - "[[Quantitative Research]]"
  - "[[Ex Post Facto Research]]"
  - "[[Analytic Framework]]"
  - "[[Factorial Design]]"
  - "[[Pre-test and Post-test]]"
  - "[[Correlational Research]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
confidence: medium
status: draft
created: 2026-07-12
updated: 2026-10-18
---
# Independent Variable

## 定义

> [!def] 自[[Variable\|变量]]
> 自变量（independent variable）是实验或[[Quantitative Research\|量化研究]]中的**输入变量**，被有意识地操纵、控制或选择，以观察其变化对[[Dependent Variable\|因变量]]（结果变量）产生的效应（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16\|Cohen et al., 2011, Ch16]]）。

在真实验中，自变量被主动操纵（manipulated），例如施加一种新的教学方法、给予不同剂量的干预。在[[Ex Post Facto Research|事后回溯研究]]中，自变量已经自然发生，只能选择而非操纵它，但分析逻辑相同：考察自变量的不同水平或取值如何与因变量的变化相关联。

> [!concept-lens] 自变量在[[Causality\|因果推断]]中的角色
> - **含义** 自变量是因果链条中的**前因**，被假定为对因变量产生影响的变量。在实验设计中，自变量是可以控制的条件或处理。
> - **用途** 通过操纵自变量的不同水平（如干预的有无、干预的不同强度），检验因果假设：自变量的变化是否系统性地引起了因变量的变化。
> - **边界** 自变量不等于原因本身，它只是原因的[[Operationalization\|操作化]]指标。一个自变量能否真正代表[[Construct\|理论构念]]取决于[[Definition of Terms\|操作性定义]]的有效性。自变量与因变量的区分只在特定研究设计中成立，同一变量在不同研究中可以扮演不同角色。

> [!boundary]- 概念边界
> - 不等于原因本身：自变量是假定前因的操作化代理。当操作化指标失效时（如用身高代理体适能），对自变量的操纵无法支持有效的因果推断。
> - 区别于[[Dependent Variable\|因变量]]：自变量是输入端的前因指标，因变量是输出端的结果指标。同一变量在不同研究设计中可以转换角色。
> - 不适用于纯描述性或探索性研究：自变量概念预设了因果推断的[[Analytic Framework\|分析框架]]，在不涉及因果假设的纯描述性研究中不使用。

---

## 核心要素

> [!feature] 自[[Variable\|变量]]的关键属性
> - **可操纵性** 在真实验中，研究者主动控制和改变自变量的水平（如施加或不施加干预）。在准实验和[[Ex Post Facto Research\|事后回溯研究]]中，自变量的水平自然存在，研究者通过选择具有不同特征的组别展开观察比较（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16\|Cohen et al., 2011, Ch16]]）。
> - **多水平取值** 自变量可以有两个或多个水平。最简单的形式是二分类（有/无干预），也可以有多个水平（如低/中/高剂量的干预），或连续取值（如学习时间长度）（pp. 323–324）。
> - **控制与隔离** 在真实验中，除被操纵的自变量外，其他可能影响[[Dependent Variable\|因变量]]的变量必须被控制或保持恒定，这是[[Causality\|因果推断]]的核心前提（pp. 312–313）。
> - **[[Definition of Terms\|操作性定义]]** 自变量必须通过[[Operationalization\|操作化]]使其可测量或可操纵。抽象的[[Construct\|构念]]（如学习动机）需要通过具体的操作（如特定的激励方案）转化为可实施的自变量（p. 330）。
> - **优先级排序** 当存在多个候选自变量时，最重要的变量在实验中操纵，其他的保持恒定或作为协变量处理（p. 330）。

[[Factorial Design|因子设计]]中，两个或多个自变量同时被操纵，每个自变量的不同水平组合构成不同的实验条件。此时不仅可以检验每个自变量的主效应（main effect），还可以检验自变量之间的[[Interaction Effect|交互效应]]（interaction effect），即一个自变量的效应是否依赖于另一个自变量的水平（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 323–324]]）。

---

## 概念辨析

> [!contrast-table] 自[[Variable\|变量]] vs [[Dependent Variable\|因变量]]
> | 维度 | 自变量 | [[Dependent Variable\|因变量]] |
> |---|---|---|
> | **角色** | 输入（input），原因 | 输出（outcome），结果 |
> | **操纵方式** | 被主动操纵或选择 | 被观察和测量 |
> | **[[Causality\|因果]]位置** | 前因（presumed cause） | 后果（presumed effect） |
> | **研究设计中的处理** | 控制、隔离、操纵其水平 | 通过[[Pre-test and Post-test\|前测]]和后测测量其变化 |
> | **示例** | 教学方法、药物剂量、课程时长 | 考试成绩、康复速度、阅读能力 |

---

## 争议与批评

> [!critique] 方法论反思与批判
> - **自变量与因变量的循环界定与封闭牢笼** [[Argument_Rømer_2018_EPT|Rømer (2018, pp. 5–6)]] 指出，在宏观评价综合与实证建模中，自变量面临严重的循环定义危机：当核心因变量（学业成就/学习结果）缺乏独立的操作化界定时，评价体系通过自变量（教学干预）的效果反向界定因变量，又以因变量的指标反馈来确认自变量的有效性；这种自变量与因变量的循环互证割裂了研究与外部真实教育实践的联系，在方法论上构筑起封闭的研究牢笼（research cage）。
> - **自变量的原子化与去脉络化风险** [[Argument_Rømer_2018_EPT|Rømer (2018, pp. 4–5)]] 批评将整体性教育实践生硬切碎为上百个孤立自变量（如将学校拆解为班级规模、经费、管理层编制等零散参数）的还原主义做法；这种处理忽视了各变量深嵌其中的历史文化与教学论脉络，导致统计上的自变量操纵脱离真实的制度生态。

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research\|相关研究]]索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16\|Cohen et al. (2011, Ch16)]] — Kgaile and Morrison (2006) 识别了七个影响[[School Effectiveness\|学校效能]]的自[[Variable\|变量]]；小麦肥料实验中肥料是有无施加作为自变量；资源可用性（3 水平）和学习动机（3 水平）在[[Factorial Design\|因子设计]]中各为自变量。
> - [[Argument_Rømer_2018_EPT\|Rømer (2018)]] — 批判可见学习中自变量的原子化还原以及自变量与因变量循环互证所构建的封闭研究牢笼。（pp. 4–6）
