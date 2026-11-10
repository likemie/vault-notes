---
title: Reinforcement Learning
aliases:
  - 强化学习
  - 深度强化学习
  - 试错学习
summary: "智能体通过与动态环境交互试错、以最大化长期累积奖励为目标的机器学习范式；在无人类历史先验知识输入的条件下，依托马尔可夫决策过程、价值网络与策略优化自主演进出超越人类经验的全局最优决策，在通用博弈求解（如 AlphaZero）中展现出摆脱人类认知定势的探索能力，但在规则不完备的开放科学领域面临样本效率与奖励设计的硬性边界。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 9
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/algorithm
  - theme/artificial-intelligence
  - theme/machine-learning
  - theme/science-of-science
related_concepts:
  - "[[AI Agent in Education]]"
  - "[[Unit of Analysis]]"
  - "[[Refined Mastery]]"
  - "[[Construct Validity]]"
  - "[[Paradigm]]"
related_theories: []
related_methods:
  - "[[Supervised Learning]]"
related_instruments: []
related_persons:
  - "[[Albert-László Barabási]]"
related_facts:
  - "[[AlphaZero]]"
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit10]]"
confidence: high
status: draft
created: 2026-11-02
updated: 2026-11-11
---

---

> [!def] Reinforcement Learning
> **强化学习（Reinforcement Learning, RL）** 指[[AI Agent in Education|智能体]]（Agent）在状态空间明确的离散或连续环境中，通过自主采取动作并接收环境即时反馈的数值奖励信号，以最大化长期累积折扣收益为目标迭代优化动作策略的计算方法。该方法输入环境状态转移模型或经验交互序列，通过策略梯度与价值函数更新，输出各状态下的最优行为策略分布。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 234–235)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 动态序列决策中的状态价值函数 $V(s)$、动作价值函数 $Q(s, a)$ 以及最优策略映射 $\pi^*(a|s)$。
> - **问题类型** 序列决策优化、博弈博弈求解、控制规划与假说空间自主搜索。
> - **[[Unit of Analysis|分析单位]]** 单步离散交互时间步 $t$、完整对局回合轨迹（Episode）或多智能体博弈局态。
> - **输入数据** 状态转移概率规程、即时奖励函数 $R(s, a)$，或纯通过环境模拟器自主试错生成的状态转移四元组 $(s_t, a_t, r_t, s_{t+1})$。
> - **输出形式** 最优动作概率分布向量 $\pi(a|s)$ 或针对当前环境局面的期望胜率估值。

> [!citation-card] 汪大胜与[[Albert-László Barabási|巴拉巴西]]论纯自我博弈强化学习的认知超越
> 与高度依赖数十万盘人类棋谱进行监督训练的传统系统不同，基于纯强化学习的 [[AlphaZero]] 系统从零外部数据起步，仅供给棋盘网格与基础走子规则。系统从随机探索起步，完全通过自我反复对弈演化最优表征，在极短时间内[[Refined Mastery|精通]]顶级棋类博弈；这种完全脱离人类先验输入的机制，展现了机器智能摆脱人类历史偏好与认知定势的探索潜能。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 234–235)]]
>
> *AlphaZero starts with no domain knowledge beyond basic rules... Starting from random play, and with only the board and rules, AlphaZero was trained solely by self-play reinforcement learning, completely unburdened by human biases or traditions.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 强化学习输出的决策策略是在预设奖励函数与特定虚拟规则约束下的最优数值解；其策略的有效性取决于仿真模拟对现实物理规律的还原忠实度。
> - **研究者判断** 奖励函数标量权重的设定、探索与利用（Exploration vs Exploitation）平衡参数的选择、折扣因子 $\gamma$ 的截断。
> - **有效性标准** 累积期望总回报、对抗基线算法的胜率等级分（Elo Rating）、样本采样效率与策略稳定性。
> - **不声称回答的问题** 强化学习在规则离散封闭的博弈空间内表现出极强算力，但无法自行定义现实中模糊多变的社会价值取向或开辟未经形式化的全新科学领域。

> [!method-stack] 方法层级
> - **上位方法** 动态规划（Dynamic Programming）、马尔可夫决策过程（Markov Decision Process, MDP）。
> - **核心构件** 深度残差策略网络、价值评估网络、蒙特卡洛树搜索（MCTS）、经验回放池。
> - **下游应用** 通用博弈计算（[[AlphaZero]]）、自驱动机器人实验室实验路径规划、自动化分子逆合成分析。

> [!dev-timeline] 方法演变
> - **1980s–1990s — 时序差分与 Q 学习奠基** 萨顿（Richard Sutton）等学者确立马尔可夫决策框架与 Q-Learning 理论基础。
> - **2010s — 深度强化学习崛起** 结合深层卷积网络的 DQN 在 Atari 游戏中展现出超越人类能力，AlphaGo 融合人类[[Supervised Learning|监督学习]]与强化学习攻克围棋。
> - **2017 — 纯自我博弈[[Paradigm|范式]]确立** [[AlphaZero]] 彻底废弃人类数据输入，在完全自主对弈中达成超人类表现，为理解不受人类偏见污染的智能探索提供了典型范式。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 234–235)]]

---

> [!formula-set]- 强化学习自适应策略优化流程
> ```mermaid
> flowchart LR
>   A["智能体当前策略 π(a|s)<br>执行探索动作 a_t"] --> B["环境状态转移 s_t+1<br>反馈即时奖励 r_t"]
>   B --> C["时序差分评估<br>累积期望回报估计 G_t"]
>   C --> D["策略梯度反向更新<br>调整参数以提升高奖动作概率"]
>   D --> A
> ```

---

> [!formula-step] 步骤一　状态价值与贝尔曼期望方程
> 在马尔可夫决策过程中，智能体从状态 $s$ 出发、依策略 $\pi$ 采取行动所能获得的长期累积折扣回报定义为：
> $$G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}$$
>
> 对应的状态价值函数满足贝尔曼期望方程：
> $$V^\pi(s) = \mathbb{E}_\pi \left[ R_{t+1} + \gamma V^\pi(S_{t+1}) \mid S_t = s \right]$$
>
> **这个公式在做什么** 将无限时间维度的远期收益递归折算为即时奖励与下一状态期望价值之和，使得智能体在评估当前操作时能够具备全局大局观，防止陷入局部短期贪婪。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 234–235)]]
>
> **符号说明**
> - $\gamma \in [0, 1)$：远期收益折扣因子。
> - $R_{t+1}$：执行动作后环境给予的即时反馈数值。
> - $\mathbb{E}_\pi[\cdot]$：在策略 $\pi$ 引导下的概率期望。

---

> [!formula-step] 步骤二　策略梯度反向更新
> 通过参数化策略 $\pi_\theta(a|s)$，依据策略梯度定理最大化目标性能指标 $J(\theta) = \mathbb{E}_{\pi_\theta}[G_0]$：
> $$\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \nabla_\theta \ln \pi_\theta(A_t \mid S_t) Q^{\pi_\theta}(S_t, A_t) \right]$$
>
> **这个公式在做什么** 沿着提升高期望价值动作发生概率的方向持续调整网络参数 $\theta$，促使模型不断淘汰低效行为，实现策略在自主试错中的演化进阶。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 234–235)]]
>
> **符号说明**
> - $\nabla_\theta$：策略参数梯度算子。
> - $Q^{\pi_\theta}(S_t, A_t)$：在当前局态采取特定操作后的期望回报估计值。

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit10|Wang & Barabási (2021)]] — 详述纯强化学习驱动 AlphaZero 在数小时内攻克多种复杂棋类的计算机制，并深入探讨该范式在开放科学探索中的能力边界。
