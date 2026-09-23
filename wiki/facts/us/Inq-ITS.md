---
title: Inq-ITS
aliases:
  - 探究智能导师系统
  - Inquiry Intelligent Tutoring System
summary: "美国罗格斯大学与伍斯特理工学院团队研发、NSF 资助的 AI 驱动科学探究智能导师系统，依托教育数据挖掘算法与虚拟实验室，利用智能代理 Rex 提供秒级自适应认知支架，并在长周期多任务中实现探究技能的显著远迁移"
type: fact
subtype: program
region: us
fact_region: "us"
fact_kind: "program"
fact_related_count: 21
fact_related_level: 2
fact_related_stars: "⭐⭐"
fact_related_color: "#ede9fe"
period: "2010–至今"
initiator_organization: "罗格斯大学（Rutgers University）、伍斯特理工学院（WPI）与 Apprendis 公司（获 NSF 资助）"
tags:
  - region/us
  - level/k12
  - educational-technology
  - theme/stem-education
  - inquiry-based-learning
  - artificial-intelligence
related_concepts:
  - "[[Intelligent Tutoring Systems]]"
  - "[[Inquiry-Based Learning]]"
  - "[[Learning Analytics]]"
  - "[[Formative Assessment]]"
  - "[[Class Size]]"
  - "[[Control of Variables Strategy]]"
  - "[[Avatar]]"
  - "[[Hypothesis]]"
  - "[[Computer Simulation]]"
  - "[[Variable]]"
  - "[[Dependent Variable]]"
  - "[[Scaffolding]]"
  - "[[Scientific Literacy]]"
  - "[[Construct Validity]]"
  - "[[Direct Instruction]]"
related_theories: []
related_methods:
  - "[[Effect Size]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[National Science Foundation]]"
  - "[[Institute of Education Sciences]]"
  - "[[Inq-Blotter]]"
  - "[[Web-based Inquiry Science Environment]]"
related_arguments:
  - "[[Argument_DeJong_2023_ERR]]"
confidence: high
status: active
created: 2026-09-21
updated: 2026-09-22
---

# Inq-ITS

---

## 项目背景与立项契机

> [!claim] 项目定位
> 探究[[Intelligent Tutoring Systems\|智能导师系统]]（Inquiry Intelligent Tutoring System, Inq-ITS）是由美国罗格斯大学（Rutgers University）贾妮斯·戈伯特（Janice D. Gobert）教授领衔研发、获[[National Science Foundation\|美国国家科学基金会]]（NSF）持续数千万美元重大资助的人工智能科学[[Inquiry-Based Learning\|探究学习]]与评价环境。系统致力于将前沿教育数据挖掘（[[Learning Analytics\|Educational Data Mining]], EDM）与自适应辅导算法深度融入中小学科学虚拟微世界，实现对学生探究技能与科学推理的实时自动诊断、[[Formative Assessment\|形成性评价]]与按需微观支架推送。（Gobert et al., 2013, 2023；[[Argument_DeJong_2023_ERR\|De Jong et al., 2023, p. 9]]）

> [!program-context] 项目背景
> - **立项时间 / 周期** 2010 年代初启动核心算法模型构建，2013 年确立从操作日志到评价指标的算法架构，随后创立 Apprendis 公司实现科研成果转化与全国常态化部署，持续活跃至今。
> - **发起方与资助机制** 由罗格斯大学、伍斯特理工学院（WPI）跨学科团队协同攻关，获得美国国家科学基金会（NSF）信息与智能系统处（IIS）、教育与人力资源处（EHR）以及[[Institute of Education Sciences\|美国教育部教育科学研究院]]（IES）多项重大科研基金资助。
> - **覆盖范围与对象** 覆盖全美逾千所初高中的物理、化学、生物与地球科学课堂，支持数十万名学生开展虚拟探究实验。
> - **核心问题导向** 破解传统大[[Class Size\|班额]]科学探究中教师无法分身对每名学生的探究行为进行实时精准诊断与个别化指导的痛点，依托 AI 算法实现规模化的高精度因材施教。（Luan et al., 2020）

---

## 方案设计与运行机制

> [!claim] 核心干预／机制假说
> [[Inquiry-Based Learning\|探究学习]]的有效性取决于对学生认知困难的秒级捕获与即时精准干预。通过教育数据挖掘技术实时解析学生在虚拟实验中的底层点击与操纵日志，能够精准识别学生是否具备[[Control of Variables Strategy\|控制变量策略]]（CVS）、是否能够正确解释数据，并由数字化[[Avatar\|化身]]智能代理即时推送自适应支架，显著促进高阶探究技能的内化与跨情境远迁移。（Gobert et al., 2018；Li et al., 2019）

> [!policy-design]- 方案设计
> - **平台目标** 培养中学生提出科学[[Hypothesis\|假设]]、设计对照实验、解释数据与撰写基于证据的科学论据四项核心探究素养。
> - **覆盖学科** 物理学（如碰撞平衡、摩擦力）、化学（如相变反应）、生命科学与地球系统虚拟微世界。
> - **核心技术组件**
>   1. **高保真交互式[[Computer Simulation\|计算机模拟]]微世界** 学生在开放界面中调整独立[[Variable\|变量]]并观测[[Dependent Variable\|因变量]]反馈；
>   2. **教育数据挖掘与隐马尔可夫模型算法引擎** 实时监听学生鼠标轨迹、变量控制动作与数据记录频次，在秒级内判定学生当前处于“盲目乱试”、“控制单变量”还是“有效收集数据”；
>   3. **智能代理 Rex（AI 化身数字导师）** 当算法判定学生陷入停滞或出现逻辑迷思时，虚拟形象 Rex 立即弹出针对性的微观[[Scaffolding\|脚手架]]（如提示“请观察每次实验中是否只改变了一个变量”），必要时提供即时原理解释（[[Argument_DeJong_2023_ERR\|De Jong et al., 2023, p. 9]]）；
>   4. **与 [[Inq-Blotter]] 教师仪表盘实时联动** 当学生连续三次在同一技能点受挫时，系统自动向上发送预警至教师平板，提示教师介入。

> [!citation-card] 戈伯特等论 Inq-[[Intelligent Tutoring Systems\|ITS]] 智能代理的实时支架机制
> Inq-ITS 是一个利用虚拟实验室引导学生探究过程的 AI 驱动系统。在系统内部，名为 Rex 的数字化代理根据算法检测结果，在学生需要帮助时即时提供关于各种探究技能的自适应脚手架。实证表明，这些基于人工智能的脚手架不仅能显著帮助学生掌握科学探究技能，还能促进这些技能向跨学科全新情境的长效迁移。（Gobert et al., 2023；引自 [[Argument_DeJong_2023_ERR\|De Jong et al., 2023, p. 9]]）
>
> *In Inq-ITS, an AI-based system that guides students in their inquiry process using virtual laboratories... a digital agent named Rex provides scaffolds to students on a variety of inquiry skills when Inq-ITS' algorithms detect that they need help. These AI-based scaffolds have shown demonstrable efficacy for helping students learn many inquiry skills and transfer them to other science topics over long time periods.*

---

## 推进历程与阶段演进

> [!dev-timeline] 项目推进历程
> - **2010–2013 — 算法奠基与探究技能日志挖掘验证** 研发基于贝叶斯网络与机器学习的自动化技能探测器，确立算法对中学生[[Control of Variables Strategy\|控制变量策略]]识别的准确率媲美人类专家，发表标杆论文（Gobert et al., 2013）。
> - **2014–2018 — 智能代理 Rex 上线与实时自适应支架突破** 正式引入拟人化数字导师 Rex，实现从纯后台被动评价转向前台主动按需[[Scaffolding\|脚手架]]推送，实证检验在线数据解释与实验设计干预实效（Gobert et al., 2018）。
> - **2019–2021 — 技能长周期远迁移与师机协同拓展** Li et al. (2019) 确证 AI 支架所激发的探究技能在跨学科任务中展现出长效抗衰退韧性；配套研发面向一线教师的实时预警看板 [[Inq-Blotter]]（Dickler et al., 2021）。
> - **2022–至今 — 全美规模化推广与自适应公平生态** 成立 Apprendis 进行全美大规模部署，深度整合多模态生成式技术与教师工作流，成为美国科学探究[[Intelligent Tutoring Systems\|智能导师系统]]的领跑者（Gobert et al., 2023；[[Argument_DeJong_2023_ERR\|De Jong et al., 2023, p. 9]]）。

---

## 实施架构与角色分工

> [!actor-grid] 实施协同矩阵
> - **顶层科研主导方** 罗格斯大学与伍斯特理工学院实验室，主导底层认知诊断算法与学习科学理论建构。
> - **资助与评估机构** [[National Science Foundation\|美国国家科学基金会]]（NSF）与[[Institute of Education Sciences\|教育科学研究院]]（IES），通过多轮竞争性重大专项资助并监督第三方效度检验。
> - **产品化与交付方** Apprendis LLC，负责 SaaS 云平台搭建、学校合规对接与教师专业发展培训。
> - **一线课堂执行体** 中学科学教师与在校学生；学生在系统内自主实验，教师依据预警看板提供高层次概念统整。

---

## 成效评估与实证发现

> [!finding-cards] 核心实证结论
> - **探究技能的自动化习得与长效跨情境远迁移** Li, Gobert, & Dickler (2019) 针对初中生的严格对照追踪证实：在 Inq-[[Intelligent Tutoring Systems\|ITS]] 虚拟实验室中接受 Rex 实时算法支架指导的学生，不仅在当前科学任务中显著提升了实验设计与数据解释能力，而且在数周至数月后的跨学科陌生科学任务中展现出稳定的技能远迁移（Transfer），打破了传统探究技能难以泛化的瓶颈。（[[Argument_DeJong_2023_ERR\|De Jong et al., 2023, p. 7]]）
> - **在线数据解释能力的秒级诊断与即时提升** Gobert et al. (2018) 实验表明，AI 算法能够毫秒级捕捉学生在数据图表中形成的局部片面推断，Rex 介入后，学生的正确结论提炼率提高超过 40%。（p. 9）
> - **对弱势学生的大幅补偿效应** 相比传统课堂教师无暇顾及的角落，AI 导师 Rex 为学业基础薄弱的学生提供了不设次数限制的耐心微观提示，有效缩小了不同认知起点学生之间的技能差距。

---

## 实证数据

> [!effect-table]- 原始研究实证数据
> <span class="concept-effect-table-marker" aria-hidden="true"></span>
>
> | 研究 | 比较或干预 | [[Dependent Variable\|结果变量]] | 分析样本 | 组别统计 | [[Effect Size\|效应量]] | 显著性或不确定性 | 设计与解释边界 |
> |---|---|---|---|---|---|---|---|
> | Li, Gobert, & Dickler (2019)（引自 [[Argument_DeJong_2023_ERR\|De Jong et al., 2023, p. 7]]） | Inq-[[Intelligent Tutoring Systems\|ITS]] 算法自适应支架 vs 无支架常规探究 | 探究技能（[[Control of Variables Strategy\|CVS]]）的长效跨情境远迁移 | 中学生科学虚拟实验追踪 | 自适应支架组在后续全新陌生科学探究任务中技能显著领先 | — | 迁移测验显著（$p < .01$） | 证实基于 EDM 算法的自适应支架不仅改善当前表现，更能促成跨学科的高阶思维迁移 |
> | Gobert, Moussavi, Li, Sao Pedro, & Dickler (2018)（引自 [[Argument_DeJong_2023_ERR\|De Jong et al., 2023, p. 9]]） | Inq-ITS 数字代理 Rex 实时数据解释支架介入 vs 对照 | 在线数据解读准确率与因果论证质量 | 初中物理与生命科学课堂 | 介入后学生在数据表格中辨析反直觉规律的正确率大幅跃升 | — | $p < .05$ | 课堂现场控制实验；确立教育数据挖掘驱动的即时微观脚手架对科学探究的精准促进 |
> | Gobert, Sao Pedro, Raziuddin, & Baker (2013)（引自 [[Argument_DeJong_2023_ERR\|De Jong et al., 2023, pp. 9–10]]） | 基于底层日志文件的算法技能评估 vs 人类专家人工评分 | 学生[[Scientific Literacy\|科学探究素养]][[Construct Validity\|构念效度]]与预测力 | 数百名中学生实验操作日志数据 | 算法自动评分与资深科学教师专家评分的相关系数超过 0.85 | $r > 0.85$ | $p < .001$ | 算法效度标杆研究；确立了使用非侵入式日志分析替代传统纸笔测试的可行性 |

---

## 争议、局限与经验教训

> [!debates] 核心争议
>
> > [!axis] 算法代理自主指导 vs 人类教师核心掌控
> > 争论焦点在于智能代理 Rex 是否会削弱教师的教学主导权。
> >
> > - **算法替代偏见** 批评者担忧学生过度依赖 AI 代理的提示，演变为机械应付软件而忽视真实师生对话。
> > - **人机协同融合** 研发团队明确指出，系统并非替代教师，而是由 Rex 负责微观程序性纠错，由 [[Inq-Blotter]] 看板预警赋能人类教师集中精力开展深层概念统整与价值关怀（Gobert et al., 2023）。

> [!lessons] 经验教训与启示
> - **支架必须精准且克制** 早期版本若在学生刚开始思考时频繁弹出提示，会打断学生的深度推理并诱发反感；系统优化后严格遵循“先检测停滞/试错模式、确认陷入僵局后才分级弹出支架”的非干扰性原则。
> - **兼顾多模态表达** 探究素养不仅体现在操纵滑块上，更体现在科学论证书写中；系统后续深度整合了自然语言处理（NLP）自动评阅技术。

---

## 相关条目网络

> [!entry-map]
> 
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Inq-Blotter]] | 事实 | Inq-[[Intelligent Tutoring Systems\|ITS]] 平台的配套教师端实时预警与监控看板，构成完整的师机协同闭环。 |
> | [[Intelligent Tutoring Systems]] | 概念 | Inq-ITS 是科学探究微世界中代表性的前沿智能导师系统。 |
> | [[Avatar]] | 概念 | 系统内置的数字导师 Rex 是智能代理与拟人化化身在科学教育中的标杆应用。 |
> | [[Computer Simulation]] | 概念 | 虚拟实验仿真微世界构成了 Inq-ITS 开展数据挖掘与学生探究的底层环境。 |
> | [[Web-based Inquiry Science Environment]] | 事实 | 与 WISE 并列为全美最受推崇的现代技术增强科学探究平台。 |
> | [[Control of Variables Strategy]] | 概念 | 变量控制策略是 Inq-ITS 核心算法诊断与自动[[Scaffolding\|脚手架]]推送的最主要目标技能。 |
> | [[Direct Instruction]] | 概念 | 系统在学生遇到瓶颈时适时推送即时直接讲授（Just-in-Time DI），实现协同。 |
> | [[Argument_DeJong_2023_ERR\|De Jong et al. (2023)]] | 论证 | 权威综述系统引用 Inq-ITS 作为 AI 技术化解探究与直接指导对立的典范。 |
