---
title: Team Assembly Model
aliases:
  - 团队组装模型
  - 团队组建模型
  - Guimerà-Uzzi 团队组装机制
  - 团队成员装配模型
summary: "解释科研与创意团队如何从资深成员与新手组成的候选池中吸纳成员的生成性网络演化模型；通过资历参数与多样性参数量化团队成员经验累积与重复合作倾向，阐释合著网络巨连通分支的涌现机制，以及资深经验与新鲜思维配比对团队创新绩效的决定性作用。"
type: theory
theory_field: "science-policy"
theory_related_count: 11
theory_related_level: 1
theory_related_stars: "⭐"
theory_related_color: "#dbeafe"
tags:
  - theory/science-policy
  - theme/science-of-science
  - theme/team-science
  - theme/complex-networks
related_concepts:
  - "[[Coauthorship Network]]"
  - "[[Emergence]]"
  - "[[Team Science]]"
  - "[[Creativity]]"
  - "[[Heterogeneity]]"
  - "[[Giant Component]]"
  - "[[Metascience]]"
  - "[[Paradigm]]"
related_theories: []
related_methods: []
related_instruments: []
related_persons:
  - "[[Brian Uzzi]]"
  - "[[Dashun Wang]]"
  - "[[Albert-László Barabási]]"
related_facts: []
related_arguments: []
confidence: high
status: active
created: "2026-10-30"
updated: 2026-10-30
---

---

> [!theory-position] 理论定位
> - **解释对象** 学术界与创意产业中团队如何遴选成员、合署关系如何在微观层面演化生成，以及宏观[[Coauthorship Network|合著网络]]拓扑结构的[[Emergence|涌现]]规律。
> - **理论问题** 解释为何不同学科展现出截然不同的合著网络连通形态，以及为何过度熟稔的老手小圈子反而会抑制高水平创新突破。
> - **理论类型** 生成性计算网络模型（Generative Agent-Based Network Model）与中观组织社会学解释框架。
> - **知识位置** 处于复杂网络科学、[[Team Science|团队科学]]（Team Science）与创新社会学的交叉地带，是连接微观成员招募偏好与宏观知识网络拓扑的经典理论。

> [!claim] 核心判断
> 团队组建绝非孤立人才的机械拼凑，其[[Creativity|创造力]]高度依赖于资深老手与初入新秀之间的结构配比。通过团队资历参数 $p$（在任资深者比例）与重复倾向参数 $q$（资深者选聘既往合作者的概率）所构筑的生成机制表明：团队成果质量与集体经验 $p$ 呈现正相关，而与重复合作倾向 $q$ 呈现负相关；仅由新手构成的团队缺乏驾驭风险的技能，而完全由旧搭档封闭抱团的团队则因认知同质化而丧失突破能力，唯有融合老手沉淀与新锐视角的团队方能实现高水平知识产出。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 118–121, 254–256)]]

---

> [!theory-origin] 提出者如何形成理论
> - **提出者与原始文本** 罗杰·吉梅拉（Roger Guimerà）、[[Brian Uzzi|布赖恩·乌齐]]（Brian Uzzi）、丹尼尔·斯皮罗（Daniel Spiro）与路易斯·阿马拉尔（Luís A. Nunes Amaral）于 2005 年在《科学》（*Science*）发表论文 *Team Assembly Mechanisms Determine Collaboration Network Structure and Team Performance*。
> - **原初问题** 既有网络演化模型（如优先连接机制）主要关注单节点随机接入，无法解释科学家通常以“多成员团队”为单元集体入网的实证事实，更无法量化团队内部人员背景[[Heterogeneity|异质性]]对学术期刊影响力的微观机制。
> - **理论资源与材料** 汲取社会学强弱纽带理论、小世界网络模型以及社会心理学关于群体经验与创造力的实验发现；实证对照社会心理学、经济学、生态学与天文学四大基础学科的半世纪发表记录，并跨界拓展至百老汇音乐剧、电子游戏开发与爵士乐唱片全量历史数据。
> - **形成路径** 将全网学者抽象为“初入新手（Newcomers）”与“在任老手（Incumbents）”两大候选池，提炼四种不同合署连线属性，通过蒙特卡洛仿真推导微观连边概率对宏观网络[[Giant Component|巨连通分支]]生成的渗流阈值。

> [!dev-timeline] 理论演变
> - **2005 — 原始模型创立** Guimerà 等人确立 $p$ 与 $q$ 双参数生成机制，揭示微观组建规则对跨学科网络结构和团队表现的决定性作用。
> - **2014 — 创意产业跨界验证** 研究者将模型推展至全球电子游戏开发与爵士乐录音历史，证实老手与新人的动态混搭是文化与科技创意领域普遍适用的通用法则。
> - **2021 — 科学学系统化整合** [[Dashun Wang|王大顺]]与[[Albert-László Barabási|艾伯特－拉斯洛·巴拉巴西]]在《[[Metascience|科学的科学]]》专著中将该模型确立为团队科学的核心理论基石之一，系统阐明网络凝聚与认知流动之间的张力平衡。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 118–121)]]

---

> [!entry-map] 关键概念与理论构件
> | 构件 | 类型 | 在理论中的功能 |
> |:---|:---|:---|
> | **初入新手（Newcomers）** | 概念主体 | 未在合著网络中拥有连线的学术新秀，带来未经定型的新思维、异常假设与创新冲劲。 |
> | **在任老手（Incumbents）** | 概念主体 | 拥有既往发表记录与合作轨迹的资深学者，提供技术积淀、声望资源与项目执行保障。 |
> | **四类合署连边** | 结构分类 | 新手－新手、新手－老手、老手－老手、老手－既往合作老手（重复连线）。 |
> | **资历参数 $p$（Incumbency）** | 调控机制 | 决定团队自资深池中招募成员的概率；驱动网络从割裂小团伙向跨团队巨连通网络涌现。 |
> | **重复倾向参数 $q$（Diversity / Past Tie）** | 调控机制 | 老手在组建团队时优先选聘旧日合作搭档的条件概率；表征认知封闭性与网络集聚度。 |

---

> [!feature] 核心动力学与实证规律
> - **资历经验保障产出基准** 跨学科实证表明，期刊影响因子与资历参数 $p$ 显著正相关。完全由初学者构成的团队在研究设计严谨度与工程推进上面临高风险，老手经验是成果达到高学术水准的基础前提。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 119–120)]]
> - **重复抱团损害创新颠覆** 期刊影响因子与重复合作参数 $q$ 呈现稳健负相关。当资深老手反复与熟悉搭档封闭合作时，共有知识背景消除了思维摩擦，导致团队陷入同质化盲区并产出边际影响力较低的平庸成果。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, p. 120)]]
> - **网络宏观渗流相变** 当参数 $p$ 处于较低水平时，网络由海量互不重叠的孤立小团队构成；随着 $p$ 提高，频繁穿梭于多个项目的资深学者成为结构桥梁，驱动全网发生渗流相变，迅速凝聚出覆盖绝大多数科研学者的巨连通分支。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 255–256)]]

---

> [!tension-table] 团队组建两难权衡
> | 组队模式 | 核心优势 | 潜在弊端 | 实证表现 |
> |:---|:---|:---|:---|
> | **全老友熟人团队（高 $p$，高 $q$）** | 内部默契深厚，沟通效率高，执行阻力极小 | 知识库高度重叠，思维定势固化，缺乏新视角 | 能够稳定产出常规成果，但缺乏高被引重大突破 |
> | **全新手激进团队（低 $p$，低 $q$）** | 思维不受[[Paradigm\|范式]]羁绊，敢于尝试高风险假说 | 缺乏专业方法训练与协同经验，试错成本高昂 | 失败与未发表率极高，成果质量方差过大 |
> | **黄金平衡团队（高 $p$，低 $q$）** | 老手提供经验支撑，引入新成员注入创新活力 | 存在初期认知磨合成本与适度协调损耗 | 期刊影响因子与长远学术影响力达到最高峰值 |

---

