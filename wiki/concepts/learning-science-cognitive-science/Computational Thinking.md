---
title: Computational Thinking
aliases:
  - 计算思维
  - 计算思维能力
  - 算法思维
  - Computational Thinking Ability
  - Algorithmic Thinking
summary: "涵盖问题分解、模式识别、抽象表征与算法设计等心智操作的问题解决能力体系，是从程序性技能向高阶认知进阶的基础枢纽。"
type: concept
domain: "learning-science-cognitive-science"
related_count: 24
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
tags:
  - learning-science
  - cognitive-psychology
  - computational-thinking
  - educational-technology
  - higher-order-thinking
related_concepts:
  - "[[Reflexivity]]"
  - "[[Dependent Variable]]"
  - "[[Procedural Skill]]"
  - "[[Logic Model]]"
  - "[[Construct]]"
  - "[[Critical Thinking]]"
  - "[[Higher-Order Thinking Skills]]"
  - "[[Hypothesis]]"
  - "[[Metacognition]]"
  - "[[AI Agent in Education]]"
  - "[[Effect Size]]"
  - "[[Generative AI Agent in Education]]"
  - "[[Self-Efficacy]]"
  - "[[Variable]]"
  - "[[Questionnaire]]"
  - "[[Creativity]]"
  - "[[Construct Validity]]"
related_theories: []
related_methods:
  - "[[Coding in Qualitative Research]]"
  - "[[Meta-analysis]]"
  - "[[Meta-meta-analysis]]"
related_instruments:
  - "[[Computational Thinking Scale]]"
  - "[[Watson-Glaser Critical Thinking Appraisal]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Liu_2026_CHBR]]"
  - "[[Argument_Unal_2026_JECR]]"
confidence: high
status: completed
created: 2026-08-25
updated: 2026-08-25
---

# Computational Thinking

---

## 定义

> [!def] 核心定义
> 计算思维（Computational Thinking, CT）由周以真（Jeannette M. Wing, 2006）界定为运用计算机科学的基础概念进行问题求解、系统设计以及人类行为理解等一系列心智活动与认知过程。它不仅是计算机从业者的专业技能，更是一种面向全体学习者的通用素养与认知工具箱，核心涵盖**问题分解（Decomposition）**、**模式识别（Pattern Recognition）**、**抽象表征（Abstraction）**与**算法设计（Algorithm Design）**四大心智操作。[[Argument_Liu_2026_CHBR|(Liu et al., 2026, pp. 2–3)]]

> [!concept-lens] 概念透镜
> - **含义** 强调利用可计算的逻辑、规则序列与[[Reflexivity|反思性]]迭代去形式化和解决复杂良构及劣构问题，沟通了低阶规则操作与高阶批判创造。
> - **用途** 在基础教育与高等教育中作为评价 STEM/STEAM 教育、编程教学及 AI 自适应学习成效的核心[[Dependent Variable|因变量]]。
> - **边界** 计算思维不等同于单纯的代码语法记忆（Coding），脱离了问题分解与算法反思的机械[[Coding in Qualitative Research|编码]]只属于低水平的[[Procedural Skill|程序性技能]]。

> [!citation-card]- 关键表述
> 计算思维表征了学习者将复杂现实挑战转化为可算法化求解形式的高阶认知能力。在智能教学技术干预中，通过自适应步骤提示与反思量规引导，学生的算法设计与调试推理能力获得显著提升。（[[Argument_Liu_2026_CHBR|Liu et al., 2026, pp. 2]], 6–7）
>
> *Computational thinking encompasses the cognitive processes involved in formulating problems and their solutions so that the solutions are represented in a form that can be effectively carried out by an information-processing agent.*

---

## 核心维度与心智操作模型

```mermaid
flowchart LR
    subgraph InputStage ["问题输入阶段"]
        direction TB
        I1["复杂现实挑战 / 劣构任务"]
        I2["多模态领域情境数据"]
    end

    subgraph Operations ["四大核心心智操作 (CT Core)"]
        direction TB
        O1["问题分解 (Decomposition: 模块拆解)"]
        O2["模式识别 (Pattern Recognition: 共性提取)"]
        O3["抽象表征 (Abstraction: 过滤冗余要素)"]
        O4["算法设计 (Algorithm Design: 分步规则构建)"]
    end

    subgraph Execution ["执行与反思调试"]
        direction TB
        E1["代码/模型自动化执行"]
        E2["错误归因与逻辑调试 (Debugging)"]
        E3["反思优化与泛化迁移"]
    end

    subgraph Outcomes ["认知高阶进阶"]
        direction TB
        R1["复杂系统问题解决能力"]
        R2["计算创造力与逻辑推理"]
    end

    InputStage --> Operations
    Operations --> Execution
    Execution --> Outcomes
```

> [!feature] 计算思维四大核心心智维度
> 1. **问题分解（Decomposition）** 将庞大、繁复的综合问题拆解为若干细小、独立且易于管理与解决的子模块。
> 2. **模式识别（Pattern Recognition）** 在不同子问题或历史情境中观察相似性、共性趋势与规则重复，加速认知图式的检索。
> 3. **抽象表征（Abstraction）** 识别并聚焦解决问题所必需的关键信息，剥离无关的具象细节，建立通用的数学或[[Logic Model|逻辑模型]]。
> 4. **算法设计（Algorithm Design）** 制定一套清晰、有序、可重复执行的分步操作指南或产生式规则序列（IF-THEN），以求得问题的确定性解答。

---

## 概念辨析

> [!contrast-table] 计算思维与相关认知[[Construct|构念]]辨析
> | 维度 | **计算思维（Computational Thinking）** | [[Procedural Skill|程序性技能（Procedural Skill）]] | [[Critical Thinking|批判性思维（Critical Thinking）]] | [[Higher-Order Thinking Skills|通用高阶思维（HOTS）]] |
> |---|---|---|---|---|
> | **核心关切** | **问题形式化与算法化求解** | 熟练执行特定良构操作序列 | 审视论据真伪与逻辑偏误 | 跨情境深度分析、综合与创造 |
> | **典型心智操作** | 分解、模式识别、抽象、算法设计 | 规则匹配、自动化计算、语法编写 | [[Hypothesis|假设]]识别、论点评价、推论验证 | 劣构问题表征、[[Metacognition|元认知]]反思、方案重构 |
> | **技术中介作用** | 借助 AI [[AI Agent in Education|智能体]]/编程环境进行动态调试 | 借助自适应提示进行分步刻意练习 | 借助多重视角对比工具进行反思审视 | 借助脚手架与探究量规促进深度建构 |
> | **主要测评工具** | [[Computational Thinking Scale|计算思维量表（CTS）]]、Bebras 测验 | 代码测试通过率、步骤得分、WCPM | [[Watson-Glaser Critical Thinking Appraisal|WGCTA 测验]]、CCTDI 量表 | 开放项目评审、质性表现量规 |

---

## 实证数据

> [!effect-table]- 原始研究结果
> <span class="concept-effect-table-marker" aria-hidden="true"></span>
>
> | 研究 | 比较或干预 | [[Dependent Variable|结果变量]] | 分析样本 | 组别统计 | [[Effect Size|效应量]] | 显著性或不确定性 | 设计与解释边界 |
> |---|---|---|---|---|---|---|---|
> | Fang et al. (2025)，引自 [[Argument_Liu_2026_CHBR|Liu et al. (2026)]] | [[Generative AI Agent in Education|生成式 AI 辅导]]+显性反思量规 vs. 传统编程教学 | Python 计算思维与代码调试表现 | $N = 92$（干预 $n = 46$, 控制 $n = 46$） | — | Hedges' $g = 0.40$ | $p < .05$ | 准实验设计；证实显性反思支架有助于将生成式 AI 转化为计算思维增益 |
> | Ye et al. (2025)，引自 [[Argument_Liu_2026_CHBR|Liu et al. (2026)]] | 编程[[AI Agent in Education|智能体]]即时语法纠错 vs. 传统讲授教学 | 代码逻辑结构与算法设计表现 | $N = 78$ | — | Hedges' $g = 0.16$ | $p < .05$ | 实验设计；即时线索提示辅助基础算法规则内化 |
> | Yilmaz & Karaoglan Yilmaz (2023)，引自 [[Argument_Liu_2026_CHBR|Liu et al. (2026)]] | 提示词驱动生成式 AI 支架 vs. 独立编程对照组 | 大学生计算思维技能与编程[[Self-Efficacy|自我效能]] | $N = 86$ | — | Hedges' $g = 0.58$ | $p < .01$ | 准实验设计；提示词工程训练显著提升算法思维水平 |

> [!ref-table]- 其他实证结果（无效应量）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable|变量]]或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | Korkmaz et al. (2017)，见 [[Computational Thinking Scale]] | 土耳其大学生与中学生样本（$N = 1{,}041$） | [[Questionnaire|问卷调查]]与量表编制研究 | [[Computational Thinking Scale|计算思维量表（CTS）]] 5 维度结构 | 探索性与验证性因子分析（$CFI = .93, RMSEA = .054$） | 总量表 Cronbach's $\alpha = .86$ | 确立了[[Creativity|创造力]]、算法思维、协作性、[[Critical Thinking|批判性思维]]与问题解决 5 维度[[Construct Validity|构念效度]] |

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Liu_2026_CHBR|Liu et al. (2026)]] — 在 AI [[AI Agent in Education|智能体]][[Meta-analysis|元分析]]中将计算思维与代码调试作为关键认知[[Dependent Variable|因变量]]，证实结合反思量规的自适应教学支架能有效提升中小学生的算法设计表现。
> - [[Argument_Unal_2026_JECR|Ünal et al. (2026)]] — 在 AI 教育[[Meta-meta-analysis|二阶元分析]]中探讨计算机科学与算法思维教学的独特干预效应，证实计算机科学学科获得显著的促学收益（$ES = 0.72$）。
