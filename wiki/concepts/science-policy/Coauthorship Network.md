---
title: Coauthorship Network
aliases:
  - 合著网络
  - 科学合著网络
  - 合作出版网络
  - scientific collaboration network
summary: "依据学术论著联合署名关系构建的复杂拓扑网络；具有跨学科异质性的重尾度分布、少数超级枢纽节点、平均路径约为 6 步的小世界特性以及覆盖 80%–90% 活跃学者的巨连通分支，是刻画科学共同体知识重组与协同演化的基础网络结构。"
type: concept
domain: "science-policy"
related_count: 10
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - theme/science-of-science
  - theme/network-science
  - theme/coauthorship
  - theme/scientometrics
related_concepts:
  - "[[Team Science]]"
  - "[[Invisible College]]"
  - "[[Peer Effects in Science]]"
  - "[[Scientific Productivity]]"
  - "[[Creativity]]"
related_theories:
  - "[[Small-World Collaboration Model]]"
  - "[[Preferential Attachment in Academia]]"
related_methods:
  - "[[Network Analysis]]"
  - "[[Relative Team Impact]]"
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[Paul Erdős]]"
  - "[[Brian Uzzi]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit04]]"
confidence: high
status: active
created: 2026-10-30
updated: 2026-10-30
---

---

> [!def] Coauthorship Network
> 合著网络（Coauthorship Network）指以科学研究人员为网络节点，以共同在正式学术期刊、会议文集或专利上联合署名为无向连接边的复杂社会拓扑网络。该网络是科学学中量化测度科学界社会组织形态、学术交流拓扑与知识协同扩散的基础结构基底。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 102–104)]]

> [!concept-lens|notitle] 概念透镜
> - **含义** 刻画科学界实际发生的实质知识生产协作连线与学者社会关系图谱。
> - **用途** 帮助科学计量学与网络科学研究者识别核心学术领袖（枢纽节点）、挖掘前沿交叉派系、测算学科隔阂距离（小世界特征），并预测科研合作演化机制。
> - **边界** 合著网络仅记录正式署名层面的硬性出版记录，未能完全穷尽非署名的学术研讨、指导建议与同行审稿等非正式交往。

> [!citation-card] 合著网络的多学科异质性与拓扑特征
> 每一个分布都呈现重尾特征，表明无论在哪个学科，几乎所有科学家都只与少数合作学者共事，而极少数人积累了数量庞大的合作学者。在生物学、物理学和数学这三个学科中，合著网络的度分布遵循不同的衰减规律，生物学具有更长的长尾，而数学的衰减速度最快。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 104–105)]]
>
> *Each of these distributions is fat-tailed, indicating that, regardless of their discipline, almost all scientists work with only a few coauthors, while a rare fraction accumulates an enormous number of collaborators. But, though all three distributions shown in Fig. 10.2 are fat-tailed, the curves follow distinct patterns.*

> [!boundary]- 概念边界
> - 不等于引文网络（Citation Network）：引文网络是有向的文献到文献的智识继承网络；合著网络则是无向的学者与学者之间共同工作的合作关系网络。
> - 不等于社交网络：合著网络要求有共同承担学术与法律责任的公开出版成果，连接门槛远高于一般线上互动或学术社交关注。

---

> [!contrast-table|notitle] 概念辨析
> | 维度 | 学术合著网络（Coauthorship Network） | 文献引文网络（Citation Network） | 社交互联网络（Online Social Network） |
> |------|------------------------------------|---------------------------------|--------------------------------------|
> | 节点类型 | 科学家个体（唯一学者标识符） | 单篇学术成果或专利文献 | 注册用户（包含公众与机构账户） |
> | 连接性质 | 无向边（或带权边表示共同发文篇数） | 有向边（从施引文献指向被引文献） | 有向（关注）或无向（好友） |
> | 连带强度 | 极高，需要数月乃至数年的协同实质科研 | 适中，反映理论引用、方法借鉴或观点批判 | 极低至中等，轻量化点赞、评论或关注 |
> | 演进机制 | 优先连接（趋向资深知名学者）与小世界聚集 | 累积引文吸附（马太效应）与新近性偏倚 | 算法信息流推送、同质性匹配与地理邻近 |

---

> [!feature] 核心要素
> - **重尾度分布与超级枢纽节点** 绝大多数科学家的合著学者数量十分有限，而极少数像[[Paul Erdős|保罗·埃尔德什]]（Paul Erdős）这样的超级合作学者拥有数百位合著者，成为维系整个网络低阶连通的核心枢纽。生物学尾部最长，物理学次之，数学衰减最快。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 104–105)]]
> - **优先连接机制驱动网络集聚** 早期初入网络的青年学者更倾向于与导师或既有高连通度资深学者联合署名，使拥有更多学术伙伴的学者以更快速度吸纳新连线，逐步固化为网络拓扑的核心枢纽。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 105–106)]]
> - **小世界六度分隔拓扑** 尽管科学界包含数以百万计的学者，任意两位学者之间的平均最短合著路径长度通常仅为 5 至 6 步，且与核心枢纽学者的平均距离更短（如数学家到 Erdős 的平均距离仅为 4.7 步）。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 106)]]
> - **巨连通分支的普遍覆盖** 真实学科合著网络中 80% 至 90% 的学者被统一包含在同一个最大弱连通分支内部，证实科学界本质上是一个广泛连接的有机整体而非彼此隔绝的孤立派系。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 108–109)]]

> [!logic-map]- 要素关系
> ```mermaid
> flowchart TD
>   A["学者发表多作者学术成果"] --> B["合著网络拓扑构建"]
>   B --> C["重尾度分布 P(k) (超级枢纽学者)"]
>   B --> D["密集局域派系社区 (研究方向聚集)"]
>   B --> E["短平均路径长度 (小世界拓扑 ~6 步)"]
>   B --> F["巨连通分支 (覆盖 80%-90% 活跃学者)"]
>   C --> G["优先连接机制强化网络中心度"]
>   E --> H["跨学科思想高效交换与突破"]
>   D --> H
> ```

---

## 围绕概念形成的命题

---

> [!concept-proposition] 命题一｜合著网络展现跨学科异质性的重尾度分布与超级枢纽结构
> **探讨维度　科研合作网络的拓扑微观异质性** 探讨不同知识生产范式下合著网络连接度衰减速率的学科差异。

> [!claim] Barabási, A.-L.
> **学科劳动分工决定网络连接长尾** 当代生物医学湿实验的大规模分工拉长了度分布极值尾部，物理学的大科学团队与中等理论团队并存，而纯理论数学的合著规模分布衰减最陡峭，高度协作型个体在数学界极度稀缺。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 104–106)]]

---

> [!concept-proposition] 命题二｜适度小世界拓扑在维持群体凝聚力与吸纳异质新颖性之间取得最优平衡
> **探讨维度　网络拓扑对集体创造力与绩效的调控** 探讨合作网络松紧程度与团队创新表现之间的非线性因果机制。

> [!claim] Uzzi, B.
> **小世界商数与团队创造力的倒 U 形关联** 百老汇百年创作网络实证表明，网络过于稀疏阻碍外部知识流动，过度紧密纠缠引发同质化认知回音室，唯有适度小世界网络兼具局域信任与外部异质思想，产出最高的商业与艺术绩效。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 107–108)]]

---

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **拓扑微观异质性** | 学科分工模式决定合著网络重尾与枢纽结构 | 跨学科合著网络度分布测度 | Newman (2001); Barabási et al. (2002) |
> | **小世界倒 U 形创造力** | 适度小世界拓扑平衡内部默契与外部异质性 | 创意团队与前沿科研网络演化 | Uzzi and Spiro (2005); [[Argument_Wang_Barabasi_2021_Cambridge_Unit04\|Wang and Barabási (2021)]] |

---

> [!dev-timeline] 概念演变
> - **1990 — 六度分隔文学表达** 剧作家约翰·盖尔（John Guare）在百老汇戏剧中写下著名台词，指出全人类由平均六个人隔开。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 107)]]
> - **1998 — 小世界网络数理形式化** 邓肯·瓦茨（Duncan Watts）与史蒂文·斯特罗加茨（Steven Strogatz）形式化定义高聚类与短路径并存的小世界网络模型。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 106–107)]]
> - **2001–2002 — 科学合著网络实证奠基** 纽曼（Mark Newman）与巴拉巴西等将合著网络作为复杂网络真实样本，测定其无标度与小世界拓扑属性。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 104–106)]]
> - **2005 — 小世界协作倒 U 形模型确立** 乌齐（Brian Uzzi）与斯皮罗以百老汇创作网络确立小世界商数 $W$ 与团队绩效的倒 U 形机制。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 107–108)]]

---

> [!tension|notitle] 核心张力
> - **适度小世界凝聚（蓝方）** 密集局域社群通过适度比例的跨界捷径形成全局贯通，既维系信任默契又源源不断引入外部异质创意。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 108)]]
> - **过度纠缠回音室（红方）** 团队过密纠缠在高度重叠的紧密小圈子中，容易催生群体盲思，排斥非共识颠覆性新思想。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 108)]]

---

> [!empirical-divider]

> [!empirical-table] 学科合著网络核心拓扑实证基准表
> | 学科领域 / 样本 | 核心拓扑测度 | 实证量化参数 | 结构含义 | 证据力度 |
> |:---|:---|:---|:---|:---|
> | 数学合著网络（Erdős 项目） | 到核心枢纽 Paul Erdős 的距离 | 平均分离步数 4.7 步 | 超级枢纽极大地压缩了全网平均路径长度 | 极高（数学家全样本） |
> | 生物学、物理学与数学 | 巨连通分支（GCC）覆盖率 | 80% 至 90% 活跃学者处于同一分支 | 证实科学界在拓扑上构成了紧密相连的有机整体 | 极高（三大自然科学全网） |
> | 凝聚态物理（arXiv cond-mat） | 局域派系重叠社区 | 团识别方法探测出紧密交叠社群 | 既有密集局域研究范式，又有跨方向长程连带 | 高（数万名活跃物理学者） |
> | 百老汇创作网络（1889–1989） | 小世界商数 $W$ 与收益/评分 | 倒 U 形非线性显著（$p < 0.01$） | 中等 $W$ 下团队商业票房与艺术评分达到双峰值 | 高（整整一个世纪创作大数据） |

---

> [!entry-map] 条目关联
>
> | 条目 | 类型 | 贡献 |
> |:-----|:-----|:-----|
> | [[Small-World Collaboration Model]] | 理论 | 形式化合著网络的小世界特性及其对团队创造力的非线性调控机制。 |
> | [[Preferential Attachment in Academia]] | 理论 | 阐释合著网络中超级枢纽学者与重尾度分布形成的优先连接动力学。 |
> | [[Team Science]] | 概念 | 合著网络是团队科学在文献联合署名维度形成的宏观复杂图谱。 |
> | [[Invisible College]] | 概念 | 无形学院构成了合著网络背后更深层次的思想与概念互动网络。 |
> | [[Relative Team Impact]] | 方法 | 测度合著网络中多节点协同产出相较于孤立节点的引文溢价水平。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit04|Wang and Barabási (2021)]] — 解析合著网络重尾度分布、埃尔德什数、小世界倒 U 形绩效与巨连通分支，揭示科学共同体的宏观拓扑结构。
