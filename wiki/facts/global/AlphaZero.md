---
title: AlphaZero
aliases:
  - 阿尔法零
  - DeepMind AlphaZero
summary: "英国 DeepMind 于 2017 年研发的无人类先验数据深度强化学习系统；完全脱离人类历史对局棋谱与手工规则，仅依据棋盘规则通过纯粹的自我博弈与深层残差网络迭代，在数小时内相继攻克国际象棋、将棋与围棋并击败全部世界顶级专有程序与人类棋手，展现了在封闭规则空间内独立演化出超越人类文明积累的异质策略与非人类直觉的能力。"
type: fact
subtype: program
region: global
fact_region: "global"
fact_kind: "program"
fact_related_count: 8
fact_related_level: 0
fact_related_stars: "☆"
fact_related_color: "#ede9fe"
period: "2017–2018"
initiator_organization: "DeepMind Technologies"
tags:
  - fact/program
  - theme/artificial-intelligence
  - theme/reinforcement-learning
  - theme/cognitive-science
  - region/global
related_concepts:
  - "[[Refined Mastery]]"
  - "[[Paradigm]]"
  - "[[Epistemology]]"
related_theories: []
related_methods:
  - "[[Reinforcement Learning]]"
  - "[[Supervised Learning]]"
related_instruments: []
related_persons:
  - "[[Dashun Wang]]"
  - "[[Albert-László Barabási]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit10]]"
confidence: high
status: draft
created: 2026-11-02
updated: 2026-11-11
---

---

> [!claim] 项目定位
> **AlphaZero（阿尔法零）** 是 DeepMind 于 2017 年开发的通用棋类[[Reinforcement Learning|强化学习]]系统。系统采取纯粹白板学习（Tabula Rasa）理念，在零人类历史数据输入的条件下，完全通过自我反复博弈与深层残差网络自主构建最优评估策略，在极短时间内超越了国际象棋、将棋与围棋领域的所有既有顶尖人类知识与传统计算算法。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 234–235)]]

> [!program-context] 项目背景
> - **立项时间 / 周期** 2017 年立项并于同年 12 月发布预印本成果，2018 年在《科学》（*Science*）正式发表终期成果。
> - **研发主体与算力支持** DeepMind 团队，依托谷歌第二代云端张量处理器（TPU）集群展开高速自我对弈与参数梯度更新。
> - **计算领域里程碑对标** 从 1997 年深蓝计算机依赖人类专家规则穷举剪枝，到 2016 年 AlphaGo 依赖数十万局人类专业棋谱[[Supervised Learning|监督学习]]，AlphaZero 彻底摆脱了对人类历史认知经验的依赖。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 234–235)]]
> - **核心认知探索导向** 探索在规则完备但状态空间近乎无限的封闭复杂系统中，机器是否能够摆脱人类思维定势与认知偏见的束缚，完全自主演化出全局最优的智能决策逻辑。

---

> [!claim] 核心干预／机制假说
> 仅输入基础博弈规则，通过单一深层卷积残差神经网络整合走子概率与局面评估，结合蒙特卡洛树搜索（MCTS）进行端到端自我博弈迭代，实现策略的自主演进。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 234–235)]]

> [!policy-design] 方案设计
> - **零人类知识先验初始化** 不使用任何人类对局记录、手工开局库或残局库，从完全随机落子开始探索。
> - **单网络残差架构** 取代以往策略网络与价值网络分离的做法，使用统一深层残差网络同时输出走法概率向量与胜负标量评估。
> - **强化学习自激对弈** 在自我交锋中以胜负结果作为唯一奖励信号，不断用表现更优的新模型替代旧模型生成新的训练博弈，形成正向自激演化。

> [!citation-card] AlphaZero 彻底摆脱人类认知束缚
> AlphaZero 从零外部数据输入起步，仅供给基础规则，完全通过自我反复博弈迭代演化最优表征；系统在 4 小时内攻克国际象棋、8 小时[[Refined Mastery|精通]]围棋，展现出超越人类直觉的全局大局观，彻底摆脱了人类认知偏倚的深刻羁绊。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 234–235)]]
>
> *AlphaZero starts with no domain knowledge beyond basic rules... It took four hours of training to master chess, and eight hours to master Go. AlphaZero displays a distinct playing style that does not conform to human traditions, illustrating how machines can generate counterintuitive strategies unburdened by human biases.*

---

> [!dev-timeline] 项目推进历程
> - **2017-10 — AlphaGo Zero 问世** 在围棋领域确立纯自我博弈[[Paradigm|范式]]，脱离人类棋谱以 100:0 击败 AlphaGo Lee。
> - **2017-12 — AlphaZero 通用化拓展** 拓展至国际象棋与将棋，宣布在短时间内战胜所有棋类顶尖专有引擎。
> - **2018-12 — 科学里程碑正式确立** 在《科学》（*Science*）正式刊发成果，被国际学术界广泛视为强化学习演化智能的代表性成果。

---

> [!actor-grid] 实施协同矩阵
> - **DeepMind 核心算法组** 负责设计 MCTS 搜索策略、残差网络结构与强化学习更新算法。
> - **谷歌 TPU 硬件工程中心** 提供高吞吐矩阵运算算力，支持数千万局棋谱的高速自我对局生成。
> - **国际顶级棋手与特级大师** 参与对局复盘评估，分析系统输出的异质走法与非人类认知形态。

---

> [!indicators] 评估指标体系
> - **Elo 竞技等级分（Elo Rating）** 衡量算法对抗历史版本与世界顶级引擎的战力标准。
> - **训练耗时** 从随机初始参数到超越人类顶级水平所需的绝对物理训练小时数。
> - **每秒局面评估量** 每秒评估棋盘位态数量（仅需数万步，远低于传统引擎的数千万步）。

> [!finding-cards] 核心实证结论
> - **超高速泛化与学习能力** 在零人类经验输入下，仅耗费 4 小时国际象棋对弈、2 小时将棋对弈与 8 小时围棋对弈，即全面击败该领域最顶尖的专用计算机程序（Stockfish、elmo 与 AlphaGo Lee）。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, p. 235)]]
> - **创造超越人类传统的异质直觉** 国际特级大师复盘证实，AlphaZero 频繁走出突破数百年人类围棋与国际象棋定式原则的招法，表现出主动牺牲子力以换取动态位置优势的非人类策略美学。
> - **机器假说空间的自主拓展范式** 证明在目标函数与规则边界确凿的封闭空间中，机器探索无需依赖人类历史数据的平庸输入，甚至能主动规避人类经验中固有的认知死角与偏误。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 234–235)]]

> [!stat-cards]- 关键实证数据
> 训练时间：国际象棋 4 小时、将棋 2 小时、围棋 8 小时；对战国际象棋世界冠军引擎 Stockfish 取得 28 胜 72 平 0 负（胜率 100% 不败）；每秒评估局面仅 6 万步，而传统引擎需评估 6000 万步。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 234–235)]]

---

> [!debates] 核心争议
>
> > [!axis] 封闭棋盘求解 vs 真实世界开放科学的适用边界
> > 强化学习在规则离散博弈中的成功能否直接外推至自然科学研究。
> >
> > - **自主探索乐观论** 认为 AlphaZero 证明了只要为机器设定好基础规则与评估指标，机器即可在无需人类干预的情况下穷尽所有可能假说并找到全局最优解。
> > - **开放前沿有限论** 汪大胜（[[Dashun Wang]]）与阿尔伯特-拉斯洛·[[Albert-László Barabási|巴拉巴西]]（Albert-László Barabási）指出，棋类属于规则明确、信息完全且无外界扰动的有限离散博弈；而科学探索处于信息高度不完备、规则待定义且涉及价值权衡的开放未知领域，纯自我博弈范式无法直接推演为自主科学发现。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 238–239)]]

---

> [!evidence-grid-a|notitle] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit10|Wang & Barabási (2021)]] — 详述 AlphaZero 脱离人类棋谱纯靠自我博弈攻克棋类的演化历程，阐明其摆脱人类认知偏见但在开放科学中仍受窄域智能边界约束的[[Epistemology|认识论]]定位。
