---
title: Cognitive Load Theory
aliases:
  - 认知负荷理论
  - 认知负荷论
  - Sweller's Cognitive Load Theory
summary: "由 John Sweller 于 1988 年创立的经典学习与教学设计理论，以人类工作记忆容量有限与长时记忆图式无限为核心架构，解构内在负荷、外在负荷与相关负荷，主张通过减少外在负荷、优化内在负荷以促进图式建构和自动化。"
type: theory
theory_field: "learning-science-cognitive-science"
theory_related_count: 34
theory_related_level: 4
theory_related_stars: "⭐⭐⭐⭐"
theory_related_color: "#fce7f3"
tags:
  - theory/learning-science
  - theory/cognitive-psychology
  - theory/instructional-design
  - field/educational-technology
related_concepts:
  - "[[Task Structure]]"
  - "[[Working Memory]]"
  - "[[Construct]]"
  - "[[Interaction Effect]]"
  - "[[Graphic Organizer]]"
  - "[[Direct Instruction]]"
  - "[[AI Agent in Education]]"
  - "[[Epistemology]]"
  - "[[Theoretical Standpoint]]"
  - "[[Ontology]]"
  - "[[Positivism]]"
  - "[[Independent Variable]]"
  - "[[Intelligent Tutoring Systems]]"
  - "[[Creativity Training]]"
  - "[[Avatar]]"
  - "[[Metacognition]]"
  - "[[Document]]"
  - "[[Hypothesis]]"
  - "[[Policy Network]]"
  - "[[Higher-Order Thinking Skills]]"
  - "[[Screening Off]]"
  - "[[Procedural Skill]]"
  - "[[Externalization]]"
  - "[[Reflexivity]]"
related_theories:
  - "[[Bounded Rationality]]"
related_methods:
  - "[[Meta-analysis]]"
  - "[[Randomised Controlled Trials]]"
related_persons:
  - "[[John Sweller]]"
related_facts:
  - "[[Community Innovation Survey]]"
  - "[[Education Endowment Foundation]]"
  - "[[Australian Education Research Organisation]]"
related_arguments:
  - "[[Argument_Lei_Ding_Chiu_2026_ERR]]"
  - "[[Argument_Liu_2026_CHBR]]"
  - "[[Argument_Skourdoumbis_2024_AER]]"
confidence: high
status: completed
created: 2026-06-06
updated: 2026-08-31
---

# Cognitive Load Theory

---

## 理论定位

> [!theory-position] 理论定位
> - **解释对象** 人类认知架构在处理新信息与复杂任务时的心智负荷分配机制，以及教学信息呈现与[[Task Structure|任务结构]]对知识内化效能的影响。
> - **理论问题** 传统教学往往忽视人类[[Working Memory|工作记忆]]的物理容量限制，导致学习者面临认知超载（Cognitive Overload）；探究式自由探索如何影响初学者的认知建构。
> - **理论类型** 认知心理学理论、学习科学模型与教学设计规范框架。
> - **知识位置** 由澳大利亚教育心理学家 [[John Sweller]] 于 1988 年系统创立，后与 Fred Paas、Jeroen van Merriënboer 及 Richard E. Mayer 的多媒体学习理论深度融合，构成当代微观教学设计的认知主义基石。

> [!claim] 核心主张
> 人类认知架构的核心特征是狭窄有限的工作记忆（Working Memory, WM）与容量庞大持久的长时记忆（Long-Term Memory, LTM）之间的不对称性；教学设计的最优目标在于通过精细解构教学任务，消除不必要的外在认知负荷（Extraneous Load），优化由元素交互性决定的内在认知负荷（Intrinsic Load），并释放宝贵的心智资源转化为关联认知负荷（Germane Load），以促进长时记忆中知识图式（Schemas）的建构与自动化提取。[[Argument_Lei_Ding_Chiu_2026_ERR|(Lei et al., 2026, pp. 1–3)]]; [[Argument_Liu_2026_CHBR|(Liu et al., 2026, pp. 2, 10)]]

> [!citation-card]- 关键表述
> 认知负荷理论将人类认知架构作为教学设计的出发点。其基本前提是：在处理新信息时，工作记忆在广度和持续时间上均受到严格限制；而长时记忆则储存着大量在复杂度与数量上均无上限的图式单元。学习的实质就是将多个离散信息元素组织为单一高级图式，并在反复演练中达到自动化运作。（Sweller, 1988, 1998, 2021）
>
> *Cognitive Load Theory is based on a cognitive architecture that consists of a limited working memory and an unlimited long-term memory. The central purpose of instructional design is to manipulate the extraneous and intrinsic cognitive loads so that working memory capacity is freed to [[Construct]] and automate cognitive schemas in long-term memory.*

---

## 关键概念与理论构件

> [!entry-map]
>
> | 构件 | 类型 | 在理论中的功能 |
> |:-----|:-----|:--------------|
> | **[[Working Memory\|工作记忆（Working Memory, WM）]]** | 认知结构 | 意识加工与即时信息处理的核心瓶颈，未加工新信息的瞬时容量仅为 $4 \pm 1$ 个离散元素，持续时间仅数秒。 |
> | **长时记忆（Long-Term Memory, LTM）** | 认知结构 | 永久性知识沉淀库，以网状层次结构储存海量认知图式，容量与保存时长在实践中是无上限的。 |
> | **知识图式（Schemas）** | 知识表征 | 将多个低阶信息元素压缩归并为单一认知意义单元的心理结构；提取时仅占用工作记忆的一个加工槽位。 |
> | **内在认知负荷（Intrinsic Load）** | 负荷维度 | 由学习材料本身的内在复杂度与元素交互性（Element Interactivity）所决定的基础负荷，取决于任务难度与学习者先验知识。 |
> | **外在认知负荷（Extraneous Load）** | 负荷维度 | 由不良教学设计、混乱信息呈现或无效认知搜索导致的额外无益负荷，对图式建构无助益，应尽可能消除。 |
> | **关联认知负荷（Germane Load）** | 负荷维度 | 学习者将释放出的工作记忆资源主动投入到图式建构、组织整合与深度反思等加工过程中所消耗的有效负荷。 |
> | **元素交互性（Element Interactivity）** | 结构特征 | 衡量任务中各知识元素间相互依赖程度的指标；高交互性任务必须在工作记忆中同时激活多个元素，负荷极高。 |
> | **生物初级与次级知识（Primary vs. Secondary Knowledge）** | 进化划分 | 初级知识（如母语口语、人脸识别）依托进化机制自发习得；次级知识（如阅读、代数、编程）必须依赖显性指导教学。（Sweller, 2021） |
> | **专业反转效应（Expertise Reversal Effect）** | [[Interaction Effect\|交互效应]] | 对新手高效的详尽指导与步骤脚手架，在面对已有高水平图式的专家时反而会转化为冗余的外在负荷。 |

---

## 核心命题与机制

> [!proposition-chain] 核心命题一｜人类认知架构的狭窄[[Working Memory|工作记忆]]瓶颈与图式自动化压缩机制
> - **前提一** 新信息的加工必须通过工作记忆通道，其瞬时注意力资源极其匮乏，无法同时处理过多相互独立的非关联信息元素（Sweller, 1988）。
> - **前提二** 长时记忆通过构建图式将复杂多元信息打包为一个单一组块（Chunk）；图式一旦经过充分练习达到自动化，无需意识监控即可顺畅执行。
> - **推导** ① 学习的本质是从无图式的零散信息处理转变为高阶图式的自动化提取；② 教学设计的核心使命是防止初学者在图式形成前遭遇工作记忆超载。

> [!proposition-chain] 核心命题二｜教学设计的经典效应群与外在负荷消除机制
> - **前提一** 学习者在特定时刻的总认知负荷等于内在负荷、外在负荷与关联负荷之和（$\text{Total Load} = \text{Intrinsic} + \text{Extraneous} + \text{Germane} \le \text{WM Capacity}$）。
> - **机制推导（教学效应群）**
>   - **样例效应（Worked Example Effect）** 相比盲目尝试解题，为初学者提供详细拆解的完整解答步骤能显著降低外在搜索负荷；
>   - **分心效应（Split-Attention Effect）** 将空间或时间上割裂的图文信息物理整合，避免视线往返切换带来的工作记忆消耗；
>   - **通道效应（Modality Effect）** 利用听觉与视觉双通道同时呈现互补信息（如动画配旁白），有效扩展工作记忆等效容量；
>   - **冗余效应（Redundancy Effect）** 避免同时呈现完全重复的多模态信息（如同屏朗读一模一样的文本字幕）。
> - **实证佐证** 在[[Graphic Organizer|图形组织器]][[Meta-analysis|元分析]]中，空间拓扑图示通过将零散事实整合为可视化网络，显著降低了学生的瞬时检索与外在负荷（$g = 0.778$）。[[Argument_Lei_Ding_Chiu_2026_ERR|(Lei et al., 2026, pp. 1–3)]]

> [!proposition-chain] 核心命题三｜生物次级知识获取的明确指导依赖与最小指导反思
> - **前提一** 科学、数学、学术读写等属于文化创造的生物次级知识，缺乏进化预设的自发习得脑神经回路（Sweller, 2021）。
> - **前提二** 缺乏先验知识的新手若置身于未加结构化指导的纯探究或发现学习情境中，工作记忆会瞬间被随机试错搜索塞满，导致图式建构失败。
> - **推导** 针对初学者的教学必须依托[[Direct Instruction|直接教学]]（Direct Instruction）与强结构化脚手架；而在引入人工智能（Artificial Intelligence, AI）等自适应技术时，AI [[AI Agent in Education|智能体]]必须通过分步解题提示、即时纠错与动态支架衰减来分担外在负荷，释放心智资源以支持深层推理。[[Argument_Liu_2026_CHBR|(Liu et al., 2026, pp. 2, 10–11)]]

> [!mechanism-map]- 认知负荷理论心智加工与教学优化架构图
> ```mermaid
> flowchart LR
>   subgraph Input["外部教学信息呈现 (Instructional Input)"]
>     direction TB
>     I1["多模态信息流 (文本/图像/语音)"]
>     I2["任务结构与问题情境 (Task Structure)"]
>   end
> 
>   subgraph WM["工作记忆加工瓶颈 (Working Memory, 4±1 槽位)"]
>     direction TB
>     L1["<b>外在负荷 (Extraneous Load)</b><br>混乱呈现、无序搜索、界面繁琐<br><i>[教学设计目标：极小化消除]</i>"]
>     L2["<b>内在负荷 (Intrinsic Load)</b><br>元素交互性、材料固有复杂度<br><i>[教学设计目标：分步化调控]</i>"]
>     L3["<b>关联负荷 (Germane Load)</b><br>主动推理、意义建构、反思整合<br><i>[教学设计目标：最优化激活]</i>"]
>   end
> 
>   subgraph LTM["长时记忆知识沉淀 (Long-Term Memory)"]
>     direction TB
>     S1["认知图式建构 (Schema Construction)"]
>     S2["规则程序自动化 (Schema Automation)"]
>   end
> 
>   Input -->|双通道感知输入| WM
>   L3 -->|沉淀与存储| LTM
>   S2 -->|组块化反向提取 (仅占1槽位)| WM
> ```

---

## 理论立场与使用方式

> [!theory-stance] [[Epistemology|认识论]]与[[Theoretical Standpoint|理论立场]]
> - **[[Ontology|本体论]]** 秉持心智计算主义立场，将人脑视为[[Bounded Rationality|有限理性]]的符号加工与信息处理系统。
> - **[[Epistemology|认识论]]** [[Positivism|实证主义]]（Positivism）与机制还原主义；主张通过严格控制[[Independent Variable|自变量]]的[[Randomised Controlled Trials|随机对照实验]]（Randomised Controlled Trials, RCT）测量瞳孔反应、双重任务反应时或主观量表，量化心智负荷指标。
> - **不能直接推出的东西** 认知负荷理论不能直接推导宏观教育价值与伦理关怀；不能推导所有阶段都必须使用单一讲授教学；无法涵盖社会文化情境中的意义共建。

> [!theory-use] 如何用于研究
> - **作为微观教学设计与多媒体课件开发准则** 指导课件排版、多模态音画配置与样例分步呈现。
> - **作为技术赋能实证研究的机制解释桥梁** 在评估[[Intelligent Tutoring Systems|智能导师系统]]（Intelligent Tutoring Systems, ITS）、[[Graphic Organizer|图形组织器]]或生成式 AI [[AI Agent in Education|智能体]]时，解释分步微提示如何降低程序性练习的外在负荷，释放[[Working Memory|工作记忆]]以赋能解题与技能自动化。[[Argument_Lei_Ding_Chiu_2026_ERR|(Lei et al., 2026)]]; [[Argument_Liu_2026_CHBR|(Liu et al., 2026)]]
> - **作为教育政策批判的分析客体** 批判性考察认知负荷理论如何被官方智库工具化为推行单一保守教学大纲的话语武器。[[Argument_Skourdoumbis_2024_AER|(Skourdoumbis & Rowe, 2024)]]

---

## 适用边界

> [!theory-boundary] 适用边界
> - **适合解释** 良构领域（如数学运算、物理定律、外语语法、计算机编程语法）的初学者概念习得与程序性解题技能训练。
> - **谨慎使用** 开放性[[Creativity Training|创造力培养]]、发散性艺术创作与复杂社会劣构问题解决，其非线性探究特征难以完全用机械负荷加减法简化。
> - **不适合解释** 具身沉浸式体验、师生情感共鸣、文[[Avatar|化身]]份认同及宏观教育不平等机制。
> - **常见误用** 机械套用新手策略指导高水平专家（忽视专业反转效应）；将所有探究式学习一概斥为有害，忽视带结构化脚手架的高阶探究对深层反思的促进价值。[[Argument_Liu_2026_CHBR|(Liu et al., 2026, pp. 10–11)]]

---

## 发展脉络

> [!dev-timeline] 认知负荷理论的发展演进
> - **1988 年 理论创立与[[Working Memory|工作记忆]]瓶颈确立** [[John Sweller]] 在《Cognitive Science》发表奠基性论文，提出手段—目的分析会带来过载的外在认知负荷，确立样例学习优于盲目解题的理论基石。
> - **1990年代 三元负荷模型与主观测量标准化** Paas 与 Van Merriënboer 等人提出三[[Metacognition|元认知]]负荷划分（内在、外在、关联负荷），并开发 9 点李克特主观心理负荷量表，使负荷测度标准化。
> - **1998 年 经典综合与教学效应群确立** Sweller、van Merriënboer 与 Paas 联合发表经典[[Document|文献]]，系统总结了分心效应、通道效应、冗余效应与专业反转效应。
> - **2000年代 多媒体学习认知理论的交叉融合** Richard E. Mayer 将双通道[[Hypothesis|假设]]、有限容量假设与主动加工假设融合，构建多媒体学习认知理论（Cognitive Theory of Multimedia Learning, CTML）。
> - **2010年代至2020年代 进化心理学转向与政策工具化争议** Sweller 引入生物初级与次级知识划分，发表《为什么探究式学习有害学生学习》（Sweller, 2021），引发全球关于[[Direct Instruction|直接教学]]与探究学习的激烈论战，并在英澳等国官方大纲中被[[Policy Network|政策网络]]深度采纳。[[Argument_Skourdoumbis_2024_AER|(Skourdoumbis & Rowe, 2024)]]

---

## 争议与批评

> [!debates] 理论与政策争议
>
> > [!axis] 明确[[Direct Instruction|直接教学]]与引导探究学习之争
> > 学界对初学者是否完全不适宜探究式学习存在长期对立。
> >
> > - **强直接教学立场** Sweller（2021）等主张未加指导的探究是对初学者认知资源的浪费，必须坚持教师主导的明确教学。
> > - **结构化探究立场** 学习科学学者（如 Hmelo-Silver et al., 2007）指出，带有丰富脚手架与反思引导的探究式学习能够有效管理认知负荷，并促进深层[[Higher-Order Thinking Skills|高阶思维]]与知识迁移。[[Argument_Liu_2026_CHBR|(Liu et al., 2026)]]

> [!critique]- 批评索引
> - [[Argument_Skourdoumbis_2024_AER|Skourdoumbis & Rowe (2024)]] 深入批判了认知负荷理论在澳大利亚《强劲开端》教师教育改革中被保守智库（[[Community Innovation Survey|CIS]]）与官方证据中介（[[Education Endowment Foundation|EEF]]、[[Australian Education Research Organisation|AERO]]）工具化的现象；指出将学生学业差距简单还原为大脑神经负荷存在赤字思维（Deficit Tropes）与生物还原主义风险，系统性[[Screening Off|屏蔽]]了教育的社会历史与文化关系维度。

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Liu_2026_CHBR|Liu et al. (2026)]] 借助认知负荷理论解释 AI [[AI Agent in Education|智能体]]对 K-12 学生[[Procedural Skill|程序技能]]（$g = 0.391$）与[[Higher-Order Thinking Skills|高阶思维]]（$g = 0.540, p = .066$）的差异化赋能机制，阐明自适应微提示如何通过分担外在负荷促进图式内化。
> - [[Argument_Lei_Ding_Chiu_2026_ERR|Lei et al. (2026)]] 依托认知负荷理论论证[[Graphic Organizer|图形组织器]]如何通过空间结构[[Externalization|外化]]信息关系、降低瞬时[[Working Memory|工作记忆]]负荷，并报告了对高阶思维的显著促进效应（$g = 0.778$）。
> - [[Argument_Skourdoumbis_2024_AER|Skourdoumbis & Rowe (2024)]] 考察认知负荷理论与脑科学话语如何在[[Policy Network|政策网络]]中被编排为强制性教师教育核心认证标准，揭示其[[Positivism|实证主义]][[Epistemology|认识论]]对教育专业[[Reflexivity|反思性]]的挤压。
> - [[Argument_Li_2026_CEAI|Li et al. (2026)]] 运用认知负荷理论解释 ChatGPT 在高等教育中的双向认知效应：结构化脚手架有助于减少外在负荷以释放工作记忆投入批判与创造性探究；而非结构化使用则触发有害的[[Cognitive Offloading|认知卸载]]，导致深层图式建构停滞。
