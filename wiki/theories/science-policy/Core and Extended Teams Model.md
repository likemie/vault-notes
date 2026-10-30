---
title: Core and Extended Teams Model
aliases:
  - 核心与扩展团队模型
  - 核心团队与外延团队模型
  - Milojević 团队规模演化模型
  - 核心与扩展团队机制
summary: "解释当代科学中团队规模分布从经典泊松分布向重尾幂律分布演进的双重生成模型；区分随机招募成员的小型核心团队与依赖高产学者马太效应快速聚集成员的扩展团队，揭示两类团队在长期存续性与知识生产中的互补分工。"
type: theory
theory_field: "science-policy"
theory_related_count: 10
theory_related_level: 1
theory_related_stars: "⭐"
theory_related_color: "#dbeafe"
tags:
  - theory/science-policy
  - theme/science-of-science
  - theme/team-science
  - theme/complex-networks
related_concepts:
  - "[[Emergence]]"
  - "[[Big Science]]"
  - "[[Knowledge Production]]"
  - "[[Metascience]]"
related_theories: []
related_methods:
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[Dashun Wang]]"
  - "[[Albert-László Barabási]]"
related_facts:
  - "[[National Academy of Sciences]]"
  - "[[CERN]]"
  - "[[Laser Interferometer Gravitational-Wave Observatory]]"
related_arguments: []
confidence: high
status: active
created: "2026-10-30"
updated: 2026-10-30
---

---

> [!theory-position] 理论定位
> - **解释对象** 科学界科研团队规模在过去半个世纪中经历的结构性膨胀，以及团队人数概率分布形态的根本性变迁。
> - **理论问题** 解释为何现代科学团队规模分布并非传统泊松分布的简单平移放大，而是[[Emergence|涌现]]出覆盖数十至上千名学者的重尾幂律分布。
> - **理论类型** 统计物理演化模型、生成性组织增长理论与科学学宏观动力学模型。
> - **知识位置** 处于[[Bibliometric Analysis|文献计量学]]、组织社会学与复杂网络统计动力学的交汇点，揭示[[Big Science|大科学]]时代微观团队集聚与宏观规模法则的内在机制。

> [!claim] 核心判断
> 现代科研团队的规模扩张反映了团队组建机制的根本性分化。科学[[Knowledge Production|知识生产]]并非由单一模式主导，而是由两类性质迥异的团队模式共同驱动：一类是由随机连接驱动的小型“核心团队（Core Teams）”，服从泊松分布且规模上限较低；另一类是以成员生产力为吸引基础、遵循“富者愈富”累积优势的“扩展团队（Extended Teams）”，表现为显著的幂律重尾分布。两类团队在知识产出总量中的相对份额长期保持基本恒定，印证了科研生态对敏捷探索与规模攻坚的双重依赖。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 126–127)]]

---

> [!theory-origin] 提出者如何形成理论
> - **提出者与原始文本** 信息科学与复杂网络学者斯塔莎·米洛耶维奇（Staša Milojević）于 2014 年在《[[National Academy of Sciences|美国国家科学院]]院刊》（*PNAS*）发表论文 *Principles of Cognitive Science in the Social Sciences: Principles of Organization of Research Teams, Dynamics of Team Sizes and Knowledge Production*。
> - **原初问题** 统计数据显示天文学与物理学团队平均人数从 1960 年代的 1.5 人跃升至 2010 年代的 6.7 人以上。经验分布检验表明，早期的指数衰减曲线在当代被拉伸为横跨三个数量级的幂律曲线，传统单一参数泊松分布无法拟合现代跨机构巨型团队。
> - **理论资源与材料** 借鉴统计物理中的优先连接（Preferential Attachment）累积优势理论与网络渗流动力学；比对天文学、物理学等领域数十万篇历史论著的作者规模分布演进轨迹。
> - **形成路径** 将团队生成过程解构为两个互补的动态通道：基础随机招募过程（生成核心团队）与基于既有成员学术声誉和产出率的吸附过程（生成扩展团队），进而推导出混合分布的解析解并完成实证拟合。

> [!dev-timeline] 理论演变
> - **2014 — 双模演化模型确立** Milojević 形式化区分核心团队与扩展团队机制，建立团队规模演化微分方程。
> - **2021 — 科学学系统化阐述** [[Dashun Wang|王大顺]]与[[Albert-László Barabási|艾伯特－拉斯洛·巴拉巴西]]将该模型整合入《[[Metascience|科学的科学]]》第 12 章，指出团队规模扩张本质上是协作微观动力学从纯随机向声誉吸附演化的制度表征。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 126–127)]]

---

> [!entry-map] 关键构件与动力学机制
> | 构件 | 驱动机制 | 规模分布特征 | 组织功能与生存条件 |
> |:---|:---|:---|:---|
> | **核心团队（Core Teams）** | 随机招募过程；新成员加入与在任者产出声望无强关联。 | 泊松分布（指数级快速衰减），极少出现超过 8 人的团队。 | 聚焦局域假说测试与高自由度敏捷探索；生存高度依赖成员稳定性，高流动率会导致其迅速解体。 |
> | **扩展团队（Extended Teams）** | 优先连接机制；团队依据既有成员的高产率与资源吸附力成比例滚雪球式吸收新人。 | 幂律分布（厚重重尾），涌现出数十人乃至上千人的超级大团队（如 [[CERN]]、[[Laser Interferometer Gravitational-Wave Observatory\|LIGO]]）。 | 承担资源密集型大型实验、工程攻关与海量数据采集；生存依托动态更换成员以维系环境适应性。 |

---

> [!feature] 核心动力学发现
> - **双模并行而非彼此替代** 跨学科历史数据拟合表明，由核心团队和扩展团队所产出的论文比例在长达半个世纪中保持相对平稳。大团队的崛起并没有彻底消灭小型核心团队，而是核心团队缓慢扩张与扩展团队超速膨胀并存的格局。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 126–127)]]
> - **差异化的存活寿命规律** 组织社会学生态学分析表明，团队生存受规模机制深刻调控：大型扩展团队通过不断引入新鲜血液动态调整成员构成来延长寿命；小型核心团队则在成员构成保持恒定、高度互信的情况下最为持久稳定，过度的人员更迭极易导致小团队夭折。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, p. 127)]]

---

