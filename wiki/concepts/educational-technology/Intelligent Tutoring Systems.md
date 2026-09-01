---
title: Intelligent Tutoring Systems
aliases:
  - 智能导师系统
  - ITS
  - 智能辅导系统
  - 智能教学系统
  - Intelligent Tutoring System
  - Intelligent Tutoring Systems (ITS)
summary: "利用人工智能算法对学习者认知状态、知识掌握与解题步骤进行细粒度建模并提供自适应个性化教学指导的计算机系统，由领域模型、学生模型、教学模型与交互界面四大经典构件组成。"
type: concept
domain: "educational-technology"
related_count: 13
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - educational-technology
  - ai-in-education
  - instruction/adaptive-learning
  - learning-science
related_concepts:
  - "[[Procedural Skill]]"
  - "[[Zone of Proximal Development]]"
  - "[[Educational Robotics]]"
  - "[[AI Agent in Education]]"
  - "[[Dialogue in Education]]"
  - "[[Metacognition]]"
  - "[[Dependent Variable]]"
  - "[[Effect Size]]"
related_theories: []
related_methods:
  - "[[Time Series Design]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Meta-analysis]]"
related_persons:
  - "[[Socrates]]"
related_facts: []
related_arguments:
  - "[[Argument_Liu_2026_CHBR]]"
confidence: high
status: completed
created: 2026-08-25
updated: 2026-08-25
---

# Intelligent Tutoring Systems

---

## 定义

> [!def] 核心定义
> 智能导师系统（Intelligent Tutoring Systems, ITS）是指利用人工智能（Artificial Intelligence, AI）技术模拟人类优秀教师一对一辅导行为的计算机教学系统。该系统能够对学习者的实时解题步骤与认知状态进行细粒度追踪，在无需人类教师即时干预的情况下，自适应地推演学习者的认知阻碍、动态调整教学策略并提供即时、逐级的矫正反馈与线索脚手架。[[Argument_Liu_2026_CHBR|(Liu et al., 2026, pp. 2, 6–7)]]

> [!concept-lens] 概念透镜
> - **含义** 区别于单向预设内容的静态课件，ITS 是基于动态推断学习者内在认知状态（心理表征与技能掌握度）的闭环人机教学中介。
> - **用途** 为大规模班级教学环境提供低成本、高保真的个性化一对一辅导，重点突破数学运算、编程语法与自然科学等良构领域的[[Procedural Skill|程序性技能]]训练。
> - **边界** 传统 ITS 强于良构规则推演与确定性错误归因，但在开放性审美创造、发散性哲学思辨及劣构复杂社会问题上的自适应建模能力相对有限。

> [!citation-card]- 关键表述
> 智能导师系统通过将领域知识图谱与动态学生认知状态模型相结合，能够实时感知学习者的每一步解题操作，精准在[[Zone of Proximal Development|最近发展区]]内提供分步提示与自适应变式演练。（[[Argument_Liu_2026_CHBR|Liu et al., 2026, pp. 2–3]]）
>
> *Intelligent Tutoring Systems leverage domain knowledge graphs and dynamic learner models to track step-by-step problem-solving operations, delivering adaptive scaffolding and individualized hints within the learner's zone of proximal development.*

> [!boundary]- 概念边界
> - 不等于**计算机辅助教学（Computer-Assisted Instruction, CAI）** 传统 CAI 采用静态分支跳转逻辑，无法根据学习者的细粒度认知状态进行动态概率推断。
> - 不等于**通用大型语言模型聊天机器人** ITS 具有确定性的学科领域知识模型与显式的教学策略模型，强调基于规则或概率图模型的系统化纠错，而非单纯的概率文本生成。

---

## 概念辨析

> [!contrast-table] 概念辨析
> | 维度 | 智能导师系统（[[Time Series Design\|ITS]]） | [[Educational Robotics\|教育机器人]]（Educational Robotics） | 生成式[[AI Agent in Education\|教育智能体]]（GenAI Agent） |
> |---|---|---|---|
> | **核心架构** | 领域模型 + 学生模型 + 教学模型 + 界面 | 物理具身/虚拟拟人实体 + 多模态交互 | 大语言模型提示工程 + 检索增强 + 工具调用 |
> | **交互机制** | 步骤级确定性诊断与逐级结构化提示 | 语音、面部表情、手势动作与触控伴读 | 自然语言多轮追问、代码生成与开放式头脑风暴 |
> | **优势领域** | 数学、代数几何、编程语法等良构技能 | 学前与低小学段语言认读、伴读情感激励 | 开放式写作润色、高阶反思、跨学科探究 |
> | **典型促学效应** | $g = 0.540$（细粒度自适应提示） | $g = 0.474$（多模态具身激励） | $g = 0.421$（反思性支架共创） |

---

## 核心要素与系统架构

> [!feature] 智能导师系统四大经典构件
> 1. **领域模型（Domain / Expert Model）** 储存教学学科的事实、概念、规则与解题推演逻辑，代表领域专家的知识结构体系。
> 2. **学生模型（Student / Learner Model）** 动态追踪学习者当前知识点掌握概率与错误认知偏差，常用贝叶斯知识追踪（Bayesian Knowledge Tracing, BKT）或深度知识追踪（Deep Knowledge Tracing, DKT）进行动态更新。
> 3. **教学模型（Pedagogical / Tutor Model）** 依据学生模型与领域模型的差异，决定何时干预、提供何种层级的脚手架（微提示、中提示或完整解答）以及何时撤回支架（Fading）。
> 4. **用户界面（User Interface）** 提供直观的解题操作工作区、多模态图式表征与即时反馈展示面板。

> [!logic-map]- 智能导师系统自适应教学闭环工作流
> ```mermaid
> flowchart LR
>   subgraph Input["学习者交互输入"]
>     direction TB
>     U1["题目作答 / 代码编写 / 步骤推演"]
>   end
> 
>   subgraph Engine["ITS 核心决策中枢"]
>     direction TB
>     D1["领域模型 (Domain Model)<br>标准知识图谱与正确解题路径"]
>     S1["学生模型 (Student Model)<br>BKT 动态评估知识掌握状态"]
>     P1["教学模型 (Tutor Model)<br>自适应选择提示层级与干预时机"]
>   end
> 
>   subgraph Output["自适应反馈输出"]
>     direction TB
>     F1["Level 1: 指向性微提示 (定向线索)"]
>     F2["Level 2: 概念解释与中间步骤引导"]
>     F3["Level 3: 底线解析与变式强化题推送"]
>   end
> 
>   Input --> S1
>   D1 --> S1
>   S1 --> P1
>   P1 --> Output
>   Output -->|调控认知负荷| Input
> ```

---

## 理论演进与发展脉络

> [!timeline] 智能导师系统的演进历程
> - **1970年代 规则推理系统发轫** SCHOLAR 与 WHY 等早期系统探索利用语义网络进行[[Socrates|苏格拉底]]式问答辅导。
> - **1980年代至1990年代 认知导师（Cognitive Tutors）成型** 约翰·安德森（John R. Anderson）基于 ACT-R 认知架构开发代数与几何认知导师，确立基于产生式规则（Production Rules）的精细步骤诊断模型。
> - **2000年代 贝叶斯知识追踪与数据驱动转型** Corbett 与 Anderson 提出的 BKT 模型广泛应用于 Carnegie Learning 与 Khan Academy，实现了对技能掌握概率的定量拟合。
> - **2010年代 约束基辅导（Constraint-Based）与[[Dialogue in Education|对话]]式 ITS 扩展** 引入自然语言交互（如 AutoTutor）与多模态眼动/生理情绪感知，增强[[Metacognition|元认知]]监控。
> - **2020年代 [[Generative Artificial Intelligence|生成式 AI]] 与大模型赋能的动态 ITS** 融合大语言模型（LLM）的开放语义理解与传统 ITS 的确定性规则校验，实现秒级高精度个性化答疑与解题路径可视化。[[Argument_Liu_2026_CHBR|(Liu et al., 2026)]]

---

## 实证数据

> [!effect-table]- 原始研究结果
> <span class="concept-effect-table-marker" aria-hidden="true"></span>
>
> | 研究 | 比较或干预 | [[Dependent Variable\|结果变量]] | 分析样本 | 组别统计 | [[Effect Size\|效应量]] | 显著性或不确定性 | 设计与解释边界 |
> |---|---|---|---|---|---|---|---|
> | Chen et al. (2025)，引自 [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 历史多源事实导学 ITS vs. 传统课堂讲授 | 历史事实识记与时间线图式构建 | $N = 84$ | — | Hedges' $g = 0.52$ | $p < .01$ | 准实验设计；ITS 自适应支架有效提升人文历史事实知识掌握度 |
> | Tasdelen & Bodemer (2025)，引自 [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 自适应分步微提示 ITS vs. 传统纸笔解题 | 小学数学长除法步骤解题技能 | $N = 114$（干预 $n = 57$, 控制 $n = 57$） | — | Hedges' $g = 0.21$ | $p < .05$ | 准实验设计；基于认知负荷理论的分步微提示降低外在负荷 |
> | Khazanchi et al. (2025)，引自 [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 代数几何智能导师 vs. 常规教学 | 中学几何辅助线推导与代数解题 | $N = 96$ | — | Hedges' $g = 0.05$ | $p > .05$ | [[Quasi-Experimental Designs\|准实验设计]]；高抽象度几何证明任务中短期干预效应较温和 |

> [!ma-table]- 一阶[[Meta-analysis|元分析]]互补维度亚组
> <span class="concept-meta-moderator-table-marker" aria-hidden="true"></span>
>
> | 一阶元分析 | 当前概念角色 | 对应亚组 | 证据规模 $k$ / $N$ | 亚组汇总效应与 95% CI | 正式组间检验 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素（[[AI Agent in Education\|智能体]]技术类型） | 智能导师系统（ITS） | $k = 10$ / — | $g = 0.540$ $[0.241, 0.839]$ | 智能体类型间检验 $Q_B = 0.069, p = .793$ | 聚焦基础教育理科解题与规则引导场景，在四大技术形态中汇总点估计最高 |

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Liu_2026_CHBR|Liu et al. (2026)]] — 在 AI [[AI Agent in Education|智能体]]促学[[Meta-analysis|元分析]]中将智能导师系统作为核心技术形态之一，证实其对 K-12 认知表现具有中等偏强促进效应（$g = 0.540$），通过步骤级自适应线索显著降低外在认知负荷并促进[[Procedural Skill|程序技能]]内化。
