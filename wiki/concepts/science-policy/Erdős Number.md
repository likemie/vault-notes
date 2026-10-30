---
title: Erdős Number
aliases:
  - 埃尔德什数
  - 埃尔德斯数
  - Erdos Number
summary: "在科学合著网络中测度学者与高产数学家保罗·埃尔德什之间最短合作拓扑距离的图论指标；埃尔德什本人的值为 0，其直接合著者为 1，与合著者合作过者为 2，以此类推；数学界中位数约为 5，绝大多数学者聚集在 2 至 5 之间，生动体现了科学界的异质性度分布与小世界近距连通特性。"
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
  - "[[Coauthorship Network]]"
  - "[[Giant Component]]"
  - "[[Clustering Coefficient]]"
  - "[[Team Science]]"
related_theories:
  - "[[Small-World Collaboration Model]]"
  - "[[Preferential Attachment in Academia]]"
related_methods:
  - "[[Network Analysis]]"
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[Paul Erdős]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit04]]"
confidence: high
status: active
created: 2026-10-30
updated: 2026-10-30
---

---

> [!def] Erdős Number
> 埃尔德什数（Erdős Number）指在无向科学合著网络中，任意学者与高产数学家[[Paul Erdős|保罗·埃尔德什]]（Paul Erdős）之间最短路径的连边数（合作跳数）。保罗·埃尔德什本人的埃尔德什数定义为 0；与其直接联合署名发表过论著的学者其值为 1；与值为 1 的学者合作过但未与埃尔德什本人合作过的学者其值为 2，以此类推。若某学者与埃尔德什之间不存在有限连通路径，则其值定义为无穷大（$\infty$）。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 102–104)]]

> [!concept-lens|notitle] 概念透镜
> - **含义** 刻画学者在全局学术合著拓扑中与核心超级枢纽学者的图论拓扑距离。
> - **用途** 用于网络科学与科学学量化合著网络的局部连通性、探索小世界导航特性，并展示科研协作的跨界渗透深度。
> - **边界** 埃尔德什数仅度量二元连通步数，不反映研究成果质量、引用影响力或实质贡献大小；仅存在于包含埃尔德什的巨连通分支内的学者拥有有限数值。

> [!citation-card] 埃尔德什数的文化与拓扑意涵
> 许多科学家在个人简历和个人主页上列出这一标志性数字已屡见不鲜。埃尔德什数表明，科学家的合著者彼此编织进了一张遍及全领域的巨型互联网络，超越了局域封闭小圈子的边界。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 104)]]
>
> *The very existence of the Erdős number demonstrates how scientists’ coauthors do not form isolated cliques; instead, they are woven into a vast interconnected network spanning disciplines.*

> [!boundary]- 概念边界
> - 不等于引用距离：埃尔德什数严格基于共同署名的合著事实，不同于文献间的施引与被引关系。
> - 不等于学术声望指标：拥有极小的埃尔德什数仅说明合作链条临近核心枢纽，不能直接等同于该学者具有等同于埃尔德什的学术造诣或学术地位。

---

> [!contrast-table|notitle] 概念辨析
> | 维度 | 埃尔德什数（Erdős Number） | 培肯数（Bacon Number） | 贝肯－埃尔德什数（Erdős-Bacon Number） |
> |------|--------------------------|-----------------------|--------------------------------------|
> | 节点定义 | 科学研究学者 | 电影演员与影视从业者 | 跨界兼具学术发表与影视出演双重身份的个体 |
> | 连边性质 | 共同署名发表学术论著或专利 | 共同出演同一部公映电影或电视作品 | 科学合著路径与演艺共演路径的算术求和 |
> | 网络中心 | 数学家保罗·埃尔德什（Erdős = 0） | 好莱坞演员凯文·贝肯（Bacon = 0） | 两个独立社会网络的双重中心节点 |
> | 主要用途 | 测度科学合著网络的拓扑凝聚力 | 流行文化中验证演艺圈六度分隔效应 | 衡量个体跨越科学共同体与大众娱乐的跨界连通度 |

---

> [!feature] 核心要素
> - **阶梯式递推定义** 拓扑距离严格遵循图论最短路径算法：埃尔德什本人为 0，直系合著者为 1，二级合著者为 2，三级合著者为 3，若处于未连通分支则为 $\infty$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 102–104)]]
> - **钟形偏态分布特征** 全球数学界实测的埃尔德什数呈现出中位数约为 5 的单峰分布，绝大多数活跃数学家落入 2 至 5 的狭窄区间，极少有人超过 10，实证体现了学术网络的低平均路径长度。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 104; 图 10.2)]]
> - **跨学科全域渗透** 现代团队科学推动跨学科交叉，使得物理学、计算机科学、经济学乃至生物医学学者通过统计学、复杂系统或博弈论桥梁与埃尔德什相连，形成广泛的有限数值覆盖。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 107–108)]]

> [!logic-map]- 要素关系
> ```mermaid
> flowchart TD
>   A["保罗·埃尔德什 (Erdős = 0)"] --> B["512 位直接合著者 (Erdős = 1)"]
>   B --> C["数万名二级合著者 (Erdős = 2)"]
>   C --> D["数十万名三级合著者 (Erdős = 3)"]
>   D --> E["全域数学界分布中位数 ~5 步"]
>   E --> F["合著网络小世界六度分隔拓扑"]
>   E --> G["超级枢纽学者对网络全局紧凑性的收敛效应"]
> ```

---

## 围绕概念形成的命题

---

> [!claim|step] 命题一　埃尔德什数的存在揭示科学合作具有高度全局凝聚力，展现整体性连通格局
> 科学家的合著网络依托少数超级枢纽节点的辐射形成紧密的拓扑缝合；数学界全域平均距离不足 5 步，表明现代学术界具有由短程连接构成的紧密协作体。（[[Argument_Wang_Barabasi_2021_Cambridge|Wang & Barabási, 2021, pp. 102–104]]）

> [!claim|step] 命题二　超级高产学者的跨学科合作充当了科学知识跨界扩散的拓扑高速公路
> 埃尔德什庞大的合著规模不仅串联了纯数学领域，更通过与物理、计算机及生物信息学者的交叉合作，使非数学领域学者同样具备了极小的埃尔德什数，为跨学科思想交换提供了低摩擦的结构通道。（[[Argument_Wang_Barabasi_2021_Cambridge|Wang & Barabási, 2021, pp. 107–108]]）

---

## 关联概念与理论

- 基础结构：[[Coauthorship Network]]
- 拓扑基底：[[Giant Component]]
- 局域组织：[[Clustering Coefficient]]
- 理论机制：[[Small-World Collaboration Model]]、[[Preferential Attachment in Academia]]
