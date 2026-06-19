---
title: Realist Evaluation
aliases:
  - 实在论评估
  - 现实主义评估
  - Realist Evaluation
  - 实在论评估理论
  - 现实主义评估理论
  - realist appraisal
summary: "由 Ray Pawson 和 Nick Tilley 提出的科学实在论评估方法与理论，主张项目干预非机械因果，而是通过在特定背景（Context）下为受试者提供资源并激活其推理（Mechanism）来产生结果（Outcome）。"
type: theory
tags:
  - theory/evaluation
  - method/evaluation
  - paradigm/critical
related_concepts:
  - "[[Positivism]]"
  - "[[Causality]]"
  - "[[Variable]]"
  - "[[Effect Size]]"
  - "[[Emergence]]"
  - "[[Epistemology]]"
  - "[[Ontology]]"
  - "[[Interpretive Paradigm]]"
  - "[[Evidence-Based Education]]"
  - "[[Heterogeneity]]"
  - "[[Professional Judgment]]"
related_theories:
  - "[[Critical Realism]]"
related_methods:
  - "[[Meta-analysis]]"
  - "[[Meta-meta-analysis]]"
  - "[[Systematic Review]]"
  - "[[Qualitative Observation]]"
  - "[[Coding in Qualitative Research]]"
related_persons:
  - "[[Ray Pawson]]"
  - "[[Roy Bhaskar]]"
related_facts:
  - "[[Education Endowment Foundation]]"
  - "[[EU Skills Agenda]]"
related_arguments:
  - "[[Argument_Wrigley_2018_BERJ]]"
  - "[[Argument_Rambla_2022_Springer]]"
confidence: medium
status: draft
created: 2026-06-19
updated: 2026-06-19
---

# Realist Evaluation

---

## 理论定位

> [!theory-position] 理论定位
> - **解释对象**：社会政策、教育干预及改进项目在复杂社会系统中的因果实现机制。
> - **理论问题**：批判[[Positivism|实证主义]]将评估等同于单纯测量“干预是否有效”的扁平化经验规律（休谟因果观），回应“什么在什么情境中对谁有效，为什么，以及如何有效”的现实评估需求。
> - **理论类型**：社会科学评估理论与研究方法论框架。
> - **知识位置**：由 [[Ray Pawson]] 与 Nick Tilley (1997, 2006) 提出，其哲学根基为 [[Roy Bhaskar]] 的[[Critical Realism|批判实在论]]（Depth Realism）。

> [!claim] 核心主张
> 社会与教育干预不是机械的物理因果（即“注射式”干预），而是通过向受试者提供资源，并依赖受试者对这些资源的认知与行动推理（Reasoning）来发挥作用。因此，因果效应的产生是机制（Mechanism）与特定背景（Context）交互作用并导致特定结果（Outcome）的非线性过程。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 7; Pawson, 2006]])

> [!citation-card] 关键表述
> 社会项目……为受试者提供资源（物质的、社会的、认知的），而它们是否有效取决于这些个体的推理。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 7]])
>
> Social programmes ... offer resources (material, social, cognitive) to subjects, and whether they work depends on the reasoning of these individuals. (Pawson, 2006: 45)

---

## 核心命题与机制

> [!proposition-chain] 实在论评估命题链
> - **前提一：生成性因果观 (Generative [[Causality]])**：因果关系不在于观察到的恒常规则性（X 导致 Y），而在于事物内部蕴含的因果力量与机制。在开放系统（如学校）中，这些机制可能处于休眠状态，只有在适宜的环境背景中才会被激活。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 8]])
> - **前提二：推理与资源的整合**：干预项目本身不能直接“产生”变化，它只提供资源（自[[Variable|变量]]）；结果（因变量）必须经由人（受试者）的能动性与信念进行推理（中介变量）而产生。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 7]])
> - **机制：CMO 配置 (Context-Mechanism-Outcome Configuration)**：因果机制（Mechanism, M）被引入不同的社会背景（Context, C）中，会因为背景对机制的触发或抑制而导致完全不同的结果（Outcome, O）。即：\(C + M \rightarrow O\)。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 8; [[Argument_Rambla_2022_Springer|Rambla, 2022, p. 165]]]])
> - **结果判断：去情境化统计聚合的失效**：将不同情境的研究混为一谈并计算“平均[[Effect Size|效应量]]”（如在[[Meta-analysis|元分析]]中）是盲目的经验主义。这种“洗涤过程”抹杀了关键机制与背景，无法指导任何具体的教育改进。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 13]])

> [!mechanism-map]- CMO 机制激活图
> ```mermaid
> flowchart TD
>     subgraph Open ["开放社会系统 (Open System)"]
>         C1["背景情境 A (Context A)"] -->|激活| M["因果机制 (Mechanism)"]
>         C2["背景情境 B (Context B)"] -->|抑制/阻碍| M
>         M -->|产生| O1["结果 A (Outcome A)"]
>         M -.->|失效/无效果| O2["结果 B (Outcome B)"]
>     end
>     
>     R["提供资源 (Resources)"] --> M
>     S["受试者推理 (Reasoning)"] --> M
> ```

> [!exegesis]- 教学助理 (TA) 的 CMO 配置分析例子
> [[Education Endowment Foundation|EEF]] Toolkit 的[[Meta-meta-analysis|元-元分析]]将教学助理（TA）项目评为“低影响、高成本”（效应量仅 $+0.08$），导致许多学校计划裁撤 TA。实在论评估则对这一结果进行解构，展现不同的 CMO 配置：
> - **配置 A（低效）**：学校缺乏预留时间让教师与 TA 沟通（背景 C1） + 学校系统性地将低成就学生甩给 TA，剥夺其接受合格教师授课的机会（背景 C2） + TA 感到被孤立且缺乏方向（机制 M1 抑制） \(\rightarrow\) 学生成绩无提升（结果 O1）。
> - **配置 B（高效）**：学校为 TA 提供协同备课时间与专业培训（背景 C3） + 教师与 TA 在课堂上有明确的教学分工（背景 C4） + TA 能够提供精准支架并激发学生信心（机制 M2 激活） \(\rightarrow\) 学习成果显著改善（结果 O2）。
> 扁平的平均效应量过滤掉了上述结构性机制，导致了极其误导性的政策决策。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 12]])

---

## 关键概念与理论构件

> [!theory-components] 理论构件
> - **背景 (Context)**：项目实施的社会环境、制度特征、人际关系和当事人的个人经历，决定了因果机制是否能被激活。
> - **机制 (Mechanism)**：社会干预中所包含的因果力量以及受试者对资源的心理/行动推理。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 7]])
> - **结果 (Outcome)**：在特定背景中激活特定机制后产生的非线性[[Emergence|涌现]]结果。
> - **实在论综合 (Realist Synthesis)**：一种[[Systematic Review|系统综述]]方法，旨在通过探究不同研究中的 CMO 配置来综合出关于“干预如何工作”的中层理论，而非对[[Effect Size|效应量]]进行数学平均。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 14]])

---

## 认识论与方法含义

> [!theory-stance] [[Epistemology|认识论]]与方法含义
> - **[[Ontology|本体论]]**：深度实在论（Depth Realism）。世界是分层的，结构和机制是真实的，且其因果力量独立于我们的观察。
> - **认识论**：[[Interpretive Paradigm|反实证主义]]/经验主义。知识是概念中介的；[[Causality|因果关系]]不等于恒常规则性，而是机制在开放系统中的复杂[[Emergence|涌现]]。
> - **方法含义**：方法论多元主义（Methodological Pluralism）。结合[[Qualitative Observation|质性观察]]、历史分析、行动研究和统计分析，重在追踪和验证机制的运作，而非单纯估计[[Effect Size|效应量]]。
> - **不能直接推出的东西**：不能直接推导出放之四海而皆准的“最佳实践”处方，或独立于情境的绝对平均效应值。

---

## 分析框架与使用方式

> [!theory-use] 如何用于研究
> - **作为理论框架**：替代传统的 [[Evidence-Based Education|EBE]] “什么有效”框架，分析政策在不同地域、学校或班级中实施时产生的[[Heterogeneity|异质性]]结果。
> - **作为分析工具**：在评估具体教育项目（如项目制学习、合成拼读）时，构建 CMO 矩阵，[[Coding in Qualitative Research|编码]]并提取影响效果的深层组织和交互因素。
> - **报告方式**：撰写内容丰富的机制叙事报告，向决策者解释“为什么”此干预在此处成功而在彼处失败，而非仅提供一个[[Effect Size|效应量]]数字。

> [!logic-map]- 实在论综合研究流程图
> ```mermaid
> flowchart LR
>     T1["构建中层因果理论"] --> S1["筛选多源文献(质性/量化)"]
>     S1 --> E1["提取背景(C)与机制(M)证据"]
>     E1 --> A1["比对和验证 CMO 配置"]
>     A1 --> T2["修正并输出解释性政策模型"]
> ```

---

## 适用边界

> [!theory-boundary] 适用边界
> - **适合解释**：复杂的、涉及多层利益相关者互动、高度依赖情境的政策与教育改革评估。
> - **谨慎使用**：在纯粹物理或生理参数控制极严的封闭系统实验评估中。
> - **不适合解释**：寻求单一、标准化、可完全复制的机械操作规程。
> - **常见误用**：将实在论评估误解为完全排斥量化数据；或者仅将“C-M-O”作为静态的分类标签，而未能动态揭示它们之间的因果推理生成关系。

---

## 发展脉络

> [!dev-timeline] 发展脉络
> - **1997 — Pawson & Tilley (Realistic Evaluation)**：奠定实在论评估的理论基石，提出 C-M-O 框架。
> - **2006 — Pawson (Evidence-based Policy: A Realist Guide)**：将实在论评估扩展到[[Systematic Review|系统综述]]领域，提出“实在论综合（Realist Synthesis）”方法，系统批判经验主义循证政策。
> - **2018 — 教育研究批评 ([[Argument_Wrigley_2018_BERJ|Wrigley, 2018]])**：Wrigley 在 BERJ 中将实在论评估和[[Critical Realism|批判实在论]]作为解构 [[Evidence-Based Education|EBE]] 统计聚合（Hattie、[[Education Endowment Foundation|EEF]] Toolkit）的主要方法论武器。

---

## 争议与批评

> [!tension] 争议焦点
> - **操作的极高复杂性**：由于需要深入追踪每个情境下的机制，实在论评估和综合在实操中极其耗费时间和精力，且难以标准化。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 15]])
> - **对决策者的沟通障碍**：政策制定者更青睐直观、简化的[[Effect Size|效应量]]排行榜或“几个月额外进步”的数字，实在论评估所提供的复杂情境叙事难以提供瞬间的决策支持。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 15]])

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wrigley_2018_BERJ|Wrigley (2018)]] — 用实在论评估的因果机制观，深度解构了 [[Education Endowment Foundation|EEF]] Fresh Start 拼读项目和教学助理项目由于去情境化聚合导致的政策误导。
> - [[Argument_Rambla_2022_Springer|Rambla (2022)]] — 将实在论评估框架应用于剖析[[EU Skills Agenda|欧盟技能议程]]政策，分析特定政策干预在特定情境中激活的因果机制。

---

## 应用领域

> [!case] 应用领域索引
> - [[Professional Judgment]] — 实在论评估对个体推理和能动性的强调，为重构和确立教师在循证实践中的专业判断力提供了理论支撑。
