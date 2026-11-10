---
title: Citation Copy Model
aliases:
  - 引文复制模型
  - 复制模型
  - 引文连环复制机制
  - Copy Model
  - Citation Copying
summary: "解释学术引文网络中优先连接机制微观物理起源的动力学生成理论。该理论指出，学者撰写论著时无需掌握全网排行榜，仅通过顺藤摸瓜引述既有文献的参考文献列表，此种局部复制行为在全网聚合后，宏观上自发涌现严格等价的线性优先连接。辛金与罗乔杜里通过追踪文献排版错误传播规律，证实约 78% 的引文源自未查阅原始文献的连环复制（Simkin & Roychowdhury, 2003, 2005; Wang & Barabási, 2021）。"
type: theory
theory_field: "science-policy"
theory_related_count: 16
theory_related_level: 1
theory_related_stars: "⭐"
theory_related_color: "#dbeafe"
tags:
  - theme/science-of-science
  - theme/network-science
  - theme/preferential-attachment
  - theme/citation-networks
related_concepts:
  - "[[Document]]"
  - "[[Emergence]]"
  - "[[Initial Attractiveness]]"
  - "[[Primary and Secondary Documents]]"
  - "[[Literature Search]]"
  - "[[Comparative Education as a Cross-Sectional Area]]"
  - "[[Research Question]]"
related_theories:
  - "[[Bounded Rationality]]"
  - "[[Price Cumulative Advantage Model]]"
  - "[[Preferential Attachment in Academia]]"
related_methods:
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[Albert-László Barabási]]"
  - "[[Derek de Solla Price]]"
  - "[[John P. Perdew]]"
  - "[[Dashun Wang]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit09]]"
confidence: high
status: active
created: "2026-11-01"
updated: 2026-11-11
---

---

> [!theory-position] 理论定位
> - **解释对象** 复杂引文网络中优先连接机制（马太效应）的微观行为物理起源，以及学者个体在信息不对称与[[Bounded Rationality|有限理性]]下如何通过局部阅读自发催生宏观无标度拓扑。
> - **理论问题** 经典的[[Price Cumulative Advantage Model|普赖斯累积优势模型]]与[[Albert-László Barabási|巴拉巴西]]-阿尔伯特模型均假定学者在选择参考[[Document|文献]]时以正比于被引量的概率选择论著（$\Pi \propto c$），然而在心理学与行为现实中，学者不可能实时掌握全网数千万篇文献的被引排行榜。该理论回应了“去中心化学者如何仅凭局部信息自发产生全局优先连接”的理论之谜。
> - **理论类型** 微观行为动力学生成理论与局部网络搜索演化模型。
> - **知识位置** 处于统计物理学、复杂网络科学、行为科学与[[Bibliometric Analysis|科学计量学]]的前沿交叉点。

> [!claim] 核心判断
> 优先连接机制无需假定学者具备全局文献计量榜单认知；学者在阅读既有文献时以一定概率顺藤摸瓜引述其参考文献列表中的条目（引文复制），必然导致被引频次越高的文献以更高的概率被再次复制引用，从而在宏观上自发[[Emergence|涌现]]严格的线性优先连接与重尾幂律分布。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 259–261)]]

> [!formula] 引文复制动力学与宏观优先连接等价方程
> 设学者在撰写新文献时包含两种引用模式：
> 1. 以概率 $1 - p$ 在全网按关键词或议题随机独立挑选文献引用（产生泊松分布背景项）；
> 2. 以概率 $p$ 从随机选取的文献参考文献列表中“复制”一条参考文献进行引述。
> 
> 由于文献 $i$ 出现在全网既有参考文献列表中的总频次严格等于其当前累积被引数 $c_i$，从随机抽取文献的参考文献列表中命中该文献的微观概率严格满足：
> 
> $$\Pi_i^{\text{copy}} = \frac{c_i}{\sum_j c_j}$$
> 
> 全网聚合后的有效微观获引概率为：
> 
> $$\Pi_i = (1 - p) \frac{1}{N} + p \frac{c_i}{\sum_j c_j} \propto c_i + c_0$$
> 
> 该方程在数学上严格证明：无需学者掌握全局网络信息，依靠局部的顺藤摸瓜即可自发涌现带有[[Initial Attractiveness|初始吸引力]]常数 $c_0$ 的[[Derek de Solla Price|普赖斯]]线性累积优势机制。

---

> [!theory-origin] 提出者如何形成理论
> - **提出者与原始文本** 计算机科学家琼·克莱因伯格（Jon Kleinberg）与拉维·库马尔（Ravi Kumar）等在 2000 年率先提出有向图复制模型（Copying Model）；理论物理学家米哈伊尔·辛金（Mikhail V. Simkin）与瓦尼·罗乔杜里（Vwani P. Roychowdhury）于 2003 年在《复杂系统》（*Complex Systems*）发表奠基之作《阅读与引用》（*Read before you cite!*），并在 2005 年通过引文排版错误在《科学计量学》（*Scientometrics*）上形式化确立引文复制模型。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 260–261)]]
> - **原初问题** [[Preferential Attachment in Academia|优先连接理论]]被批评缺乏行为认知合理性，因为没有学者会根据被引排行榜来选择参考文献；网络科学亟需揭示富者愈富现象底层的微观认知机制。
> - **关键经验材料（[[John P. Perdew|佩尔杜]]印刷错误连环传播）** 理论物理学家约翰·佩尔杜（John P. Perdew）1992 年发表于《物理评论B》的经典成果斩获 20,000 余次引用。辛金与罗乔杜里发现该成果在早期流传中产生了一处四位数页码排版错误（一位数字印刷错误）。由于多位独立学者独立发生同一排版错误的概率微乎其微（小于 $10^{-4}$），该印刷错误在后续数十篇引文列表中的高频重复出现，为引文直接连环复制提供了无从辩驳的物理铁证。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, p. 261)]]

> [!dev-timeline] 理论版本与贡献
> - **2000 — 网络复制图模型提出** 库马尔与克莱因伯格等在万维网网页链接演化中形式化建立二项复制随机图算法。
> - **2003 — 引文未读复制假说** 辛金与罗乔杜里在学术引文网络中提出“不读即引”的引文复制假说与数学推导。
> - **2005 — 印刷错误定量测定 78% 复制率** 辛金与罗乔杜里系统统计学术引文错误谱系，测定学术界高达 78% 的引文源于未查阅[[Primary and Secondary Documents|原始文献]]的连环复制。
> - **2021 — 科学学微观物理基础整合** [[Dashun Wang|王大顺]]与巴拉巴西在《科学学》专著附录 A2.2 中将复制模型正式确立为优先连接的物理行为起源。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 259–261)]]

---

> [!entry-map] 关键概念与理论构件
>
> | 构件 | 类型 | 在理论中的功能 |
> |:-----|:-----|:--------------|
> | 顺藤摸瓜检索（Local Search） | 机制 | 学者以既有文献参考文献列表作为新知识探寻的局部跳板。 |
> | 连环引文复制（Citation Copying） | 机制 | 未阅读原始文献而直接沿用前人参考文献条目的行为复制。 |
> | 存量被引放大（Stock Amplification） | 机制 | 高被引成果在全网列表中出现概率高，成为复制引用的天然聚集地。 |
> | 宏观优先连接涌现（Macroscopic Emergence） | 推论 | 局部的随机文献复制在全网聚合后等价于纯线性优先连接。 |

---

> [!theory-proposition] 命题一｜顺藤摸瓜的文献复制行为是宏观优先连接自发涌现的微观物理起源
> 学者在撰写成果时面临巨大的文献超载压力，翻阅已读文献的参考文献并顺藤摸瓜挑选题目录入新成果是最经济的[[Literature Search|文献检索]]路径。这种行为使得高被引成果在全网参考文献列表中的曝光频次呈正比扩大，即便学者仅凭个人局部阅读随机挑一条参考文献引用，抽中高被引文献的几率也严格正比于该文献已有引用量。因此，微观上的分散复制行为无需全局信息即可在宏观上自发涌现出马太效应。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 259–261)]]

> [!example|notitle]
> 在新兴[[Comparative Education as a Cross-Sectional Area|交叉学科]]初建期，学者通过少数开创性综述的参考文献列表快速掌握领域全貌并直接引述其中的核心条目，促使这些早期被引条目在短时间内迅速成长为不可撼动的超级中枢节点。

---

> [!theory-use] 框架入口
> - **[[Research Question|研究问题]]** 解释引文网络度分布重尾的微观生成机制、量化同行引述行为中的信息级联与学术疏失。
> - **分析对象与单位** 学术成果参考文献中的排版错漏、引文变体谱系以及学者阅读与引用行为序列。
> - **需要的材料** 含有拼写错误、页码印刷错漏或非标准缩写的大规模引文网络全文数据。
> - **解释目标** 测算学术界真实的文献阅读核实率，揭示注意力集聚的无意识行为驱动力。

> [!theory-framework] 命题如何转化为分析维度
>
> | 理论依据 | 分析维度与提问 | 可观察线索与材料 | 判读规则与边界 |
> |:---|:---|:---|:---|
> | 局部引文复制假说 | 引用来源是基于原创查阅还是连环继承？ | 参考文献中是否重复出现特定历史排版错漏（如佩尔杜页码错误）。 | 同一微观罕见排版错误在多篇后继成果中反复出现支持引文复制解释。 |
> | 宏观优先连接等价性 | 局部复制能否完全解释宏观度分布指数？ | 复制概率 $p$ 与全网幂律度指数 $\gamma$ 的对应关系拟合。 | 当 $c_0 \approx m$ 时推导出 $\gamma \approx 3$，精确拟合现实经验观测。 |

---

> [!warning|limits] 理论假定与方法边界
> - 复制模型以纯引文条目复制为假定，不能简单推论学者完全未理解被引文献的核心思想；部分学者可能研读了成果的核心理论，但在著录文后参考文献时采用了简捷的复制粘贴操作。
> - 数字化引文管理软件（如 EndNote、Zotero）与 DOI 一键导入技术的普及，从技术层面显著减少了印刷错漏的连环传播，改变了现代引文差错的微观表现形态。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, p. 261)]]

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit09|Wang & Barabási (2021)]] — 在专著附录 A2.2 与 A2.3 中系统阐明引文复制模型对优先连接物理起源的解释，并引述佩尔杜代表作排版错误实证证据（pp. 259–261）。
