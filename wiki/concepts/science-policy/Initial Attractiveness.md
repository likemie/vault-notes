---
title: Initial Attractiveness
aliases:
  - 初始吸引力
  - 初始吸引力参数
  - 初始获引概率
  - 基底吸引力
  - 零引用门槛
summary: "指学术文献在发表之初、尚未获得任何引用时所内生具备的基础获引几率常数 c₀。该构念由德里克·德索拉·普赖斯基于波利亚罐子机制引入，修正了纯优先连接模型中新成果因零被引而永远无法获得首引的冷启动困境，并推导出稳态幂律分布指数 γ = 2 + c₀/m；严希范与福图纳托实证测定 c₀ ≈ 7 为学术界富者愈富机制全面开启的客观临界门槛（Price, 1976; Eom & Fortunato, 2011; Wang & Barabási, 2021）。"
type: concept
domain: "science-policy"
related_count: 12
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - theme/science-of-science
  - theme/network-science
  - theme/preferential-attachment
  - theme/scientometrics
related_concepts:
  - "[[Citation Distribution]]"
  - "[[Citation Disparity]]"
  - "[[Variable]]"
  - "[[Document]]"
related_theories:
  - "[[Price Cumulative Advantage Model]]"
  - "[[Preferential Attachment in Academia]]"
  - "[[WSB Model]]"
related_methods:
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[Derek de Solla Price]]"
  - "[[Albert-László Barabási]]"
  - "[[Dashun Wang]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit09]]"
confidence: high
status: active
created: "2026-11-01"
updated: 2026-11-01
---

---

> [!def] Initial Attractiveness
> 初始吸引力（Initial Attractiveness，常表征为参数 $c_0$）是指新发表的学术论著在被引频次为零（$c_i = 0$）的冷启动阶段，所内生具备的被同行学者发现并引用的基础基底概率。该构念由德里克·德索拉·普赖斯（Derek J. de Solla Price）在 1976 年创立累积优势模型时提出，旨在解决纯优先连接假定（$\Pi_i \propto c_i$）在现实中导致的先有鸡还是先有蛋的数理死循环（catch-22）：若成果获引几率严格正比于已有引用，则零被引成果将永远无法获得初次引用。通过引入初始吸引力修正项，模型形式化打通了文献从零被引向累积优势正反馈过渡的微观动力学路径。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 257–259)]]

> [!concept-lens|notitle] 概念透镜
> - **含义** 标识文献在脱离马太效应支配时，完全由议题兴趣、关键词搜索与外生随机性赋予的基础曝光几率。
> - **用途** 用于界定学术网络从随机吸附向优先连接切换的临界阈值，构建可解析的厚尾幂律生成模型。
> - **边界** 适用于解释新文献在发表初期的冷启动行为；不直接反映学者个人的终身声望资本。

> [!citation-card] 初始吸引力与优先连接启动阈值
> 纯粹的优先连接会导致一个怪圈：若成果尚未获得任何引用（$c_i = 0$），它将永远无法吸引新的引用。我们可以通过承认每篇新论著都具备一个有限的初始被引概率来解决这一困境，这一参数被称为成果的“初始吸引力” $c_0$。严希范与福图纳托的经验测量表明，富者愈富效应全面启动的临界拐点大约在 $c_0 \approx 7$。换言之，在一篇论著累积获得 7 次引用之前，它的获引过程就像优先连接完全不存在一样；只有一旦跨越了这 7 次引用的门槛，优先连接的正反馈才全面启动。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 258–259)]]
>
> *Preferential attachment leads to a catch-22: If a paper has no citations yet, it can not attract new citations. We can resolve this by acknowledging that each new paper has a finite initial probability of being cited for the first time, called the initial attractiveness of a paper, c0... finding that the tipping point for preferential attachment is around c0 ≈ 7. That is, before a paper acquires 7 citations, its citations accumulate as though preferential attachment does not apply.*

> [!boundary]- 概念边界
> - 不等于文献的内在相对适应度 $\lambda$。初始吸引力 $c_0$ 是对所有成果统一设立的基底平移常数（均质外生随机性），而适应度刻画成果内在科学价值与竞争力的篇际异质性。
> - 不等于早期引文冲刺。初始吸引力发挥作用的区间局限于累积被引极低的萌芽阶段（$c < 7$），一旦越过门槛，系统即转入由被引存量主导的优先连接轨道。

---

> [!contrast-table|notitle] 概念辨析
> | 维度 | 初始吸引力（[[Initial Attractiveness]]） | 成果内在适应度（Fitness） | 优先连接概率（Preferential Attachment） |
> |---|---|---|---|
> | 变量性质 | 全局均质基底常数（$c_0 \approx 7$） | 单篇文献特异性参数（$\lambda_i$ 或 $\eta_i$） | 随文献被引存量动态递增的概率函数 |
> | 支配阶段 | 零引用至 7 次被引的冷启动萌芽期 | 全生命周期各阶段（决定终极天花板） | 突破 7 次被引后的马太效应加速期 |
> | 数理作用 | 消除分母与分子为零的数理死循环 | 调节文献在同等被引存量下的增长斜率 | 生成无标度厚尾幂律拓扑分布 |

---

> [!feature] 核心要素
> - **零被引冷启动困境化解（Resolving Zero-Citation Deadlock）** 将优先连接概率从 $\Pi \propto c$ 修正为 $\Pi \propto c + c_0$，使得新发表成果天然享有获得首引的初始入场券。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, p. 258)]]
> - **稳态幂律指数解析决定（Determining Power-Law Exponent）** 该参数直接参与解析决定全网稳态引文分布的幂律指数：$\gamma = 2 + c_0/m$。当经验常数满足 $c_0 \approx m$ 时，幂律指数精确等于经验普遍观测到的 $\gamma \approx 3$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, p. 259)]]
> - **7 次被引激活临界点（7-Citation Tipping Point）** 严希范与桑托·福图纳托（Eom & Fortunato, 2011）实证测定 $c_0 \approx 7$；当被引小于 7 次时，获引主要由外生随机检索支配；一旦跨过 7 次被引，富者愈富机制全面激活，获引速率转为严格正比于累积被引。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 258–259)]]

> [!logic-map]- 要素关系
> ```mermaid
> flowchart LR
>     A["新成果发表 (c = 0)"] --> B["初始吸引力 c_0 支配阶段 (c < 7)"]
>     B --> C["外生随机引用与小范围同行阅读"]
>     C --> D{"累积被引是否突破 7 次？"}
>     D -- "否" --> B
>     D -- "是" --> E["优先连接机制全面激活 (c >= 7)"]
>     E --> F["获引速率严格线性正比于被引存量"]
>     F --> G["宏观生成指数为 γ = 2 + c_0/m 的重尾幂律"]
> ```

---

> [!concept-proposition] 命题一｜学术引文网络存在分段激活机制，7 次被引是马太效应开启的客观门槛
> **探讨维度　优先连接的微观临界转换** 探讨成果获引速率如何从低被引随机状态切换至线性优先连接状态。

> [!claim] [[Argument_Wang_Barabasi_2021_Cambridge_Unit09|Eom & Fortunato (2011)]]
> **初始吸引力参数与分段状态转换实证** 严希范与桑托·福图纳托基于大规模物理学引文网络实测不同被引区间的年度获引速率，证实成果在累积被引跨越 $c_0 \approx 7$ 之前，获引速率几乎与既有被引无关，呈现平台期特征；唯有越过 7 次被引的临界门槛后，优先连接的正反馈才全面启动，获引速率转为严格线性正比于累积被引（图 A2-1）。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Eom & Fortunato, 2011, via Wang & Barabási, 2021, pp. 258–259)]]

---

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **临界门槛命题** | 7 次被引是引文网络开启富者愈富正反馈的经验分界点 | 青年学者成果扶持、早期学术传播评估与引文增长建模 | Price (1976); Eom and Fortunato (2011); [[Argument_Wang_Barabasi_2021_Cambridge\|Wang and Barabási (2021)]] |

---

> [!dev-timeline] 概念演变
> - **1976 — 波利亚罐子模型与初始常数** 普赖斯在经典著述中引入基底常数 $c_0 = 1$，建立累积优势的数学推导。
> - **2011 — 7 次被引经验门槛测定** 严希范与福图纳托利用物理学大数据测定实际初始吸引力 $c_0 \approx 7$。
> - **2021 — 科学学系统化整合** 王大顺与巴拉巴西在专著附录 A2.1 中将其确立为解决零被引怪圈并连接微观复制与宏观优先连接的关键纽带。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 257–259)]]

---

> [!debates] 学术争议
>
> > [!axis] 纯优先连接 vs 带初始吸引力修正
> > 网络科学早期曾争论是否需要引入初始吸引力参数。
> >
> > - **BA 纯无标度模型派** 采用简单的入网初始度假定，忽略零被引初期的特殊性。
> > - **科学计量学实证派** 证明真实引文数据中存在显著的低被引平坦区，必须通过初始吸引力 $c_0 \approx 7$ 才能消除数理怪圈并准确拟合现实幂律指数 $\gamma \approx 3$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 258–259)]]

> [!warning|limits] 适用局限
> 7 次被引门槛是基于《物理评论》等自然科学核心文献库的经验测定；在引用容量极低的某些人文细分领域，或者人均参考文献数极高的高能物理与基因组学领域，临界门槛 $c_0$ 的实际数值会发生相应缩放。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, p. 259)]]

---

> [!empirical-divider]

> [!ref-table]- 其他实证结果（无效应量）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | 变量或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Wang_Barabasi_2021_Cambridge_Unit09\|Eom & Fortunato (2011)]] | 《物理评论》（PR）全量引文网络与不同发表年限成果队列 | 获引速率与累积被引存量的非线性拟合分析 | 成果获引速率从平坦外生随机性转向线性正比的临界拐点 $c_0$ | 临界吸引力参数精确为 **$c_0 \approx 7$**；在 $c < 7$ 时获引曲线平缓，在 $c \ge 7$ 时严格满足线性正比 $\Pi \propto c$（图 A2-1） | 大样本全量数据拟合一致 | 证实真实学术界存在明确的 7 次被引激活门槛，低于此阈值优先连接不生效 |
> | [[Argument_Wang_Barabasi_2021_Cambridge_Unit09\|Wang & Barabási (2021)]] | Web of Science 涵盖自然科学与工程技术的主流学科引文分布 | 普赖斯修正模型与稳态分布实测值比对 | 幂律度指数 $\gamma = 2 + c_0/m$ 与实测指数吻合度 | 当经验参数取 $c_0 \approx m$ 时，推导得出的幂律指数精确等于广泛实测观测值 **$\gamma \approx 3$** | 跨学科实测一致 | 验证了带初始吸引力的累积优势模型在解释真实世界无标度引文分布时的数理完备性 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit09|Wang & Barabási (2021)]] — 在专著附录 A2.1 中系统介绍初始吸引力概念、数理方程及严希范与福图纳托测定的 7 次被引经验门槛（pp. 257–259）。
