---
title: Control of Variables Strategy
aliases:
  - 变量控制策略
  - 控制变量策略
  - CVS
  - control of variables
summary: "科学探究与实验设计中的核心过程技能，指在检验因果假设时仅系统改变一个焦点自变量并保持其他所有潜在混杂变量恒定，以确立无混淆因果推论。"
type: concept
domain: "instruction-pedagogy"
related_count: 25
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
tags:
  - concept/inquiry-skill
  - theme/science-education
  - method/experimental-design
  - level/k12
related_concepts:
  - "[[Variable]]"
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Teaching Assistant]]"
  - "[[Direct Instruction]]"
  - "[[Inquiry-Based Learning]]"
  - "[[Counterfactual]]"
  - "[[Interaction Effect]]"
  - "[[Working Memory]]"
  - "[[Scaffolding]]"
  - "[[Problem Solving]]"
  - "[[Reflexivity]]"
  - "[[Discovery Learning]]"
  - "[[Causality]]"
  - "[[Emergence]]"
  - "[[Heterogeneity]]"
related_theories: []
related_methods:
  - "[[Factorial Design]]"
  - "[[Meta-analysis]]"
  - "[[Intervention Research]]"
  - "[[Pre-test and Post-test]]"
  - "[[Prediction Interval]]"
  - "[[Confidence Interval]]"
  - "[[Pilot Testing]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_DeJong_2023_ERR]]"
confidence: high
status: active
created: 2026-09-20
updated: 2026-09-21
---

# Control of Variables Strategy

---

## 定义

> [!def] 核心定义
> [[Variable|变量]]控制策略（Control of Variables Strategy, CVS）指在科学实验与实证探究中，为了确定某一因素对结果的因果效应，学习者或研究者仅系统操纵单一焦点[[Independent Variable|自变量]]（Focal Variable），同时保持所有其他可能产生影响的外部变量（Extraneous Variables）严格恒定的程序性策略。该策略旨在消除实验中的混淆因素（Confounding），从而使观察到的[[Dependent Variable|因变量]]变化能够被唯一地归因于目标自变量。[[Argument_DeJong_2023_ERR|(De Jong et al., 2023, p. 4)]]

> [!concept-lens] 概念透镜
> - **含义** 指向科学推理与实验设计中最基本的因果分离程序，即通过成对对比消除竞争性解释。
> - **用途** 帮[[Teaching Assistant|助教]]学设计者诊断学习者在科学探究中的逻辑推理水平，并作为[[Direct Instruction|直接教学]]与[[Inquiry-Based Learning|探究式学习]]相对效能争论的关键基准任务。
> - **边界** 仅适用于能够进行正交变量分离的良构实验系统，难以直接套用于高度复杂、多变量非线性交互或非实验性的社会观察领域。

> [!citation-card] 变量控制策略的核心内涵
> 掌握变量控制策略是学生从直觉探索走向系统科学探究的里程碑。然而，是否必须通过显性规则讲授来习得该策略，长期以来是教学心理学的重要分歧。[[Argument_DeJong_2023_ERR|(De Jong et al., 2023, pp. 4–5)]]
>
> *Acquiring CVS can be accomplished well in the context of experimentation, especially with regard to long-term effects. Studies that explicitly taught a CVS rule had effect sizes no different from studies in which CVS rules were not explicitly taught.*

> [!boundary]- 概念边界
> - 不等于普通观察记录 — 变量控制策略要求主动对物理或虚拟实验条件进行正交设计与对照比较，而非被动记录现象变化。
> - 不等于机械执行实验规程 — 真正掌握该策略要求学生理解“为何必须控制变量”的因果[[Counterfactual|反事实]]逻辑，而非仅仅照搬“一次只变一个”的操作口诀。

---

## 概念辨析

> [!contrast-table] [[Variable|变量]]控制策略与相关概念辨析
> | 维度 | 变量控制策略（CVS） | 试误探索（Trial and Error） | 全因素[[Factorial Design\|析因设计]]（Factorial Design） |
> |---|---|---|---|
> | 变量操纵特征 | 单次仅改变一个目标变量，其余严格保持恒定 | 随机或依据直觉同时调整多个变量 | 系统组合多个[[Independent Variable\|自变量]]的所有水平进行交叉测试 |
> | 因果推论效力 | 高，能明确单一变量的独立主效应 | 极低，变量之间严重混淆，无法确立因果归因 | 极高，不仅能检验主效应，还能精确识别[[Interaction Effect\|交互效应]] |
> | 认知负荷要求 | 中等，需要[[Working Memory\|工作记忆]]监控非目标变量的状态 | 低至极高，缺乏系统策略导致记忆混乱与无效重复 | 高，要求复杂的统计规划与高阶变量协调能力 |

---

## 核心要素

> [!feature] 核心要素
> - **确定因果焦点** 明确探究问题中所关心的单一核心[[Independent Variable|预测变量]]（如斜面坡度或摆锤重量）。
> - **正交成对对比（Orthogonal Comparison）** 构建两组或多组实验，使其仅在目标焦点[[Variable|变量]]的水平上存在差异，其余属性完全相同。
> - **潜在混杂排除（Confound Elimination）** 识别并冻结所有可能影响结果的非目标变量，防止虚假关联与过度推论。
> - **有效性评价（Evaluation of Validity）** 能够识别并批判他人设计的未控制变量实验，指出其因果推论的无效性。[[Argument_DeJong_2023_ERR|(De Jong et al., 2023, pp. 4–5)]]

> [!logic-map]- 变量控制策略的操作流程
> ```mermaid
> flowchart LR
>     A["界定目标假设与焦点变量"] --> B["识别潜在混杂变量"]
>     B --> C["构建正交成对实验组"]
>     C --> D["固定非目标变量状态"]
>     D --> E["比较因变量产出与归因"]
> ```

---

## 围绕概念形成的命题

---

### 命题一　变量控制策略的习得机制无需单一依赖显性规则灌输

> [!concept-lens] 规则讲授与探究体验的习得效能
> 围绕[[Variable|变量]]控制策略应通过直接显性规则传授抑或通过探究实践内生建构，学界展开了长达数十年的实证检验，[[Meta-analysis|元分析]]证据表明两种路径在策略掌握上并无统计显著差异。

> [!claim] Schwichow et al.
> **显性规则教学与探究发现的等效性** 针对 72 项探讨学生如何学习变量控制策略的[[Intervention Research|干预研究]]进行的元分析表明，显性传授变量控制规则的教学干预，在促进策略习得方面并未表现出优于非显性规则探究的相对优势。学习者在具有合理支持的实验探究环境中同样能够有效归纳并掌握该策略。[[Argument_DeJong_2023_ERR|(De Jong et al., 2023, pp. 4–5)]]

> [!claim] Dean & Kuhn
> **长期保持与迁移中的探究优势** 尽管[[Direct Instruction|显性直接教学]]在短期[[Pre-test and Post-test|后测]]中能够促使学生迅速复现规则，但通过持续自主实验与探究发现习得变量控制策略的学生，在延迟后测以及向复杂真实情境的知识迁移中展现出更为持久的保持效果与深层策略理解。[[Argument_DeJong_2023_ERR|(De Jong et al., 2023, p. 4)]]

---

### 命题二　教学支架与前置指导在复杂变量空间中具有时序等价性

> [!concept-lens] 支架介入时机与策略习得
> 探究情境中变量维度的复杂性对学习者的[[Working Memory|工作记忆]]构成挑战，教学干预的关键在于提供有效支架，而非必须将显性规则前置。

> [!claim] Lazonder & Egberink
> **前置规则指导与过程中支架的等价性** 在学生开展科学探究之前显性讲授变量控制策略，与在探究进行过程中通过系统[[Scaffolding|脚手架]]（如提示卡、引导性提问与即时反馈）引导学生发现并维持变量控制，对最终的探究技能发展具有完全同等的促进效果。教学设计的关键不在于是否“前置讲授”，而在于探究全周期中是否获得了精准的认知支持。[[Argument_DeJong_2023_ERR|(De Jong et al., 2023, p. 9)]]

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **习得路径等效性** | 显性规则讲授与指导式实验探究在策略习得上整体效能相当 | 中小学基础科学实验与科学推理教学 | Schwichow et al. (2016); [[Argument_DeJong_2023_ERR\|De Jong et al. (2023)]] |
> | **长效保持与迁移** | 自主探究更有利于策略的深度内化、跨任务迁移与长周期保持 | 延迟效果评估与[[Problem Solving\|复杂问题解决]]任务 | Dean & Kuhn (2007) |
> | **支架介入时序** | 前置直接讲授与探究过程中嵌入动态支架效果一致 | 计算机虚拟实验与课堂科学探究 | Lazonder & Egberink (2014) |

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] [[Direct Instruction|直接教学]]倡导者与[[Inquiry-Based Learning|探究学习]]学派关于 CVS 习得机制的争论
> > 直接教学派（如 Klahr 等早期研究）主张[[Variable|变量]]控制策略是高度不透明的人为规则，儿童无法自发发现，必须由教师直接讲授并示范；而探究派与认知发展学者（如 Kuhn 等）认为过早灌输规则会导致表层仪式性模仿，剥夺学生在认知冲突中进行[[Reflexivity|反思性]]概括的机会。
> >
> > - **Klahr & Nigam (2004)** 主张直接教学在让儿童快速习得变量控制策略方面显著快于[[Discovery Learning|纯发现学习]]，且能在后续设计中产生迁移。
> > - **[[Argument_DeJong_2023_ERR\|De Jong et al. (2023)]]** 指出 Klahr 等研究所采用的“直接教学”并非仅是单向讲读，而是包含了让学生主动设计、评估实验并获得针对性反馈的探究要素；大规模[[Meta-analysis|元分析]]已证明显性规则教学并无普遍优越性。（p. 4）

> [!warning] 适用局限
> 变量控制策略主要聚焦于单因素线性[[Causality|因果关系]]的离散变量系统。面对现实世界中普遍存在的非线性交互系统、复杂自适应网络或[[Emergence|涌现]]现象时，机械坚持“单一变量控制”可能诱发还原论偏误，难以解释多元动态平衡。[[Argument_DeJong_2023_ERR|(De Jong et al., 2023, p. 8)]]

---

## 实证数据

> [!ma-table]- 一阶[[Meta-analysis|元分析]]总体结果
> <span class="concept-meta-analysis-table-marker" aria-hidden="true"></span>
>
> | 一阶元分析 | 当前概念角色与总体结果 | $k$ / $N$ | 效应指标与模型 | 汇总效应与 95% CI | [[Heterogeneity\|异质性]]与[[Prediction Interval\|预测区间]] | 关键解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_DeJong_2023_ERR\|De Jong et al. (2023)]]<br>（引述 Schwichow et al., 2016） | [[Dependent Variable\|结果变量]]：探讨显性规则教学对比非显性探究对[[Variable\|变量]]控制策略（CVS）掌握的总体效果 | $k = 72$ / — | Hedges' $g$，随机效应 | 显性教学组 $g = 0.58$ [0.46, 0.70]；非显性探究组 $g = 0.65$ [0.51, 0.79] | 原文两组[[Confidence Interval\|置信区间]]重叠，组间无显著差异 | 涵盖 72 项干[[Pilot Testing\|预实验]]，推翻了单项研究关于显性讲授 CVS 具有绝对优越性的断言 |

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - **[[Argument_DeJong_2023_ERR|De Jong et al. (2023)]]** 系统梳理受控实验与[[Meta-analysis|元分析]]证据，引用 Schwichow et al. (2016) 的 72 项干预研究元分析反驳 Zhang et al. (2022) 的断言，指出在[[Variable|变量]]控制策略的习得中，显性规则讲授（$g = 0.58$）与[[Inquiry-Based Learning|探究式教学]]（$g = 0.65$）效果相当，强调探究中结合动态支架在长效保持上的关键价值。
