---
title: Coauthorship Network
aliases:
  - 合著网络
  - 科学合著网络
  - 合作出版网络
  - scientific collaboration network
summary: "依据学术论著联合署名关系构建的复杂网络；具有重尾度分布（少数超高连接度的枢纽学者）、高度密集的局域派系社区、平均路径约为 6 步的小世界特性以及涵盖 80%–90% 学者的巨连通分支等宏观统计拓扑特征。"
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
related_theories:
  - "[[Small-World Collaboration Model]]"
  - "[[Preferential Attachment in Academia]]"
related_methods:
  - "[[Network Analysis]]"
  - "[[Relative Team Impact]]"
related_instruments: []
related_persons:
  - "[[Paul Erdős]]"
  - "[[Brian Uzzi]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit04]]"
confidence: high
status: active
created: "2026-10-30"
updated: 2026-10-30
---

---

> [!def] Coauthorship Network
> 合著网络（Coauthorship Network）指以科学研究者为网络节点，以共同在正式学术期刊、会议论文集或专利上联合署名为无向连接边的复杂社会网络。该网络是科学学中量化测度科学界社会组织形态、学术交流结构与知识扩散路径的基础拓扑基底。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 102–104)]]

> [!concept-lens|notitle] 概念透镜
> - **含义** 刻画科学界实际发生的知识生产协作连线与学者社会关系图谱。
> - **用途** 帮助科学计量学与科学学研究者识别核心学术领袖（枢纽节点）、挖掘前沿交叉子群（派系发现）、测算学术隔阂距离（小世界特征），并预测未来科研合作演化机制。
> - **边界** 合著网络仅记录正式署名层面的硬性合作记录，未能穷尽非署名的学术讨论、指导建议与审稿交往等非正式连接。

> [!citation-card] 合著网络的多学科异质性与拓扑特征
> 每一个分布都呈现重尾特征，表明无论在哪个学科，几乎所有科学家都只与少数合作者共事，而极少数人积累了数量庞大的合作者。在生物学、物理学和数学这三个学科中，合著网络的度分布遵循不同的衰减规律，生物学具有更长的长尾，而数学的衰减速度最快。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 104–105)]]
>
> *Each of these distributions is fat-tailed, indicating that, regardless of their discipline, almost all scientists work with only a few coauthors, while a rare fraction accumulates an enormous number of collaborators. But, though all three distributions shown in Fig. 10.2 are fat-tailed, the curves follow distinct patterns.*

> [!boundary]- 概念边界
> - 不等于引文网络（Citation Network）：引文网络是有向的文献到文献的智识继承网络；合著网络则是无向的学者与学者之间共同工作的合作关系网络。
> - 不等于社交网络：合著网络要求有共同承担法律与学术责任的公开论著产出，连接门槛远高于一般线上互动或学术好友关注。

---

> [!contrast-table|notitle] 概念辨析
> | 维度 | 学术合著网络（Coauthorship Network） | 文献引文网络（Citation Network） | 社交互联网络（Online Social Network） |
> |------|------------------------------------|---------------------------------|--------------------------------------|
> | 节点类型 | 科学家个体（唯一学者标识符） | 单篇学术论文或专利文献 | 注册用户（包含公众与机构账户） |
> | 连接性质 | 无向边（或带权边表示共同发文篇数） | 有向边（从施引文献指向被引文献） | 有向（关注）或无向（好友） |
> | 连带强度 | 极高，需要数月乃至数年的协同实质科研 | 适中，反映理论引用、方法借鉴或观点批判 | 极低至中等，轻量化点赞、评论或关注 |
> | 演进机制 | 优先连接（趋向资深知名学者）与小世界聚集 | 累积引文吸附（马太效应）与新近性偏倚 | 算法信息流推送、同质性匹配与地理邻近 |

---

> [!feature] 核心要素
> - **重尾度分布与枢纽学者** 绝大多数科学家的合著者数量十分有限，而极少数像[[Paul Erdős|保罗·埃尔德什]]（Paul Erdős）这样的超级合作者拥有数百位共同作者，成为维系整个网络低阶连通的核心枢纽。不同学科重尾斜率不同，生物学合作者分布尾部最长，物理学次之，数学衰减最快。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 104–105)]]
> - **优先连接机制驱动网络集聚** 早期初入网络的青年学者更倾向于与导师或既有高连通度资深学者联合署名，使拥有更多合作者的学者以更快速度吸纳新连线，逐步固化为网络拓扑的核心枢纽。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 105–106)]]
> - **小世界六度分隔拓扑** 尽管科学界包含数以百万计的学者，任意两位学者之间的平均最短合著路径长度通常仅为 5 至 6 步，且与核心枢纽学者的平均距离更短（如数学家到 Erdős 的平均距离仅为 4.7 步）。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 106)]]
> - **巨连通分支的普遍性** 真实学科合著网络中 80% 至 90% 的学者被统一包含在同一个最大弱连通分支内部，证实科学界本质上是一个广泛连接的有机整体而非彼此隔绝的孤立学派。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 108–109)]]

> [!logic-map]- 要素关系
> ```mermaid
> flowchart TD
>   A["学者发表多作者学术论文"] --> B["合著网络拓扑构建"]
>   B --> C["重尾度分布 P(k) (少数超级枢纽学者)"]
>   B --> D["密集局域派系社区 (研究方向聚集)"]
>   B --> E["短平均路径长度 (小世界现象 ~6 步)"]
>   B --> F["巨连通分支 (覆盖 80%-90% 活跃学者)"]
>   C --> G["优先连接机制强化网络中心度"]
>   E --> H["跨学科思想高效交换与突破"]
>   D --> H
> ```

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit04|Wang & Barabási (2021)]] — 整合 arXiv 预印本平台及跨学科万级学者全量发表数据，解析合著网络度分布异质性、小世界拓扑与巨连通分支，阐明科学协作网络在促进思想交汇中的宏观规律。
