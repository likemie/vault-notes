---
title: Clique Percolation Method
aliases:
  - 团渗流算法
  - 派系渗流算法
  - 团渗流法
  - 重叠社区发现算法
  - CPM 算法
  - Clique Percolation
  - CPM
summary: "由 Gergely Palla et al. (2005) 提出的复杂网络重叠社区发现算法；基于 $k$-团相邻（共享 $k-1$ 个节点）的渗流思想，将相互连通的局部紧密完全子图聚合成宏观社群。该方法突破了传统图分割算法强行将节点归入单一孤立组的局限，精准刻画学者在合著网络中同时嵌入多个专业合作圈与跨界学科派系的重叠从属特征。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 10
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/algorithm
  - theme/science-of-science
  - theme/network-science
  - theme/coauthorship-networks
related_concepts:
  - "[[Coauthorship Network]]"
  - "[[Invisible College]]"
  - "[[Giant Component]]"
  - "[[Team Science]]"
  - "[[Clustering Coefficient]]"
related_theories:
  - "[[Small-World Collaboration Model]]"
related_methods:
  - "[[Network Analysis]]"
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[Mark Newman]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit04]]"
confidence: high
status: active
created: "2026-10-30"
updated: 2026-10-30
---

---

> [!def] Clique Percolation Method
> 团渗流算法（Clique Percolation Method, CPM）是一种用于在无向复杂网络中识别重叠社区结构（Overlapping Communities）的图论拓扑算法。该算法首先在全局网络中检索所有大小为 $k$ 的全连通子图（$k$-clique），定义两个共享 $k-1$ 个节点的 $k$-团互为相邻；随后通过图遍历将所有相互可达的相邻 $k$-团连通成一个连续子图（$k$-团渗流集团，即一个社区）。由于单个节点可同时从属于属于不同渗流集团的多个 $k$-团，算法输出允许节点具有多重社区从属身份的重叠社群划分方案。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 104)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 刻画 [[Coauthorship Network]] 中的局域学派派系社区结构与学者跨界嵌入特征。
> - **问题类型** 复杂网络拓扑模式识别、重叠社群结构划分与网络社群动态演进追踪。
> - **分析单位** 网络节点（学者/科研人员）、连边（合署合作关系）以及局域全连通子图（$k$-团）。
> - **输入数据** 无向无权或加权网络邻接矩阵、合著关系列表或科研项目联合署名元数据。
> - **输出形式** 若干由节点构成的重叠社区集合、每个社区包含的节点清单，以及识别出的未嵌入任何显著派系的游离节点。

> [!citation-card] 关键定义
> 为了在科研合作网络中清晰凸显紧密互联的科研群体，可以应用专门识别全连通派系（cliques）的社区发现算法，并依据学者是否属于可识别的派系为节点赋予颜色标签。网络中绝大多数节点都被赋予了明确的色彩，证实绝大多数科研人员都从属于至少一个明确可辨的合作社区；仅有极少数孤立散落的黑点未归入任何社区。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 104)]]
>
> *Second, the network consists of densely connected cliques of authors or communities. To highlight these communities, we can apply to this network a community-finding algorithm designed to identify cliques, and color the nodes based on whether they belong to a clearly identifiable clique... the vast majority of nodes take up a color, indicating that most scientists belong to at least one identifiable community.*

---

> [!method-position] 方法定位
> - **构念效度** 传统模块度优化算法基于严格互斥划分假设，强行将每个学者划入唯一样本组，遮蔽了跨学科通才与多课题组兼职的客观现实。团渗流法以局部完全图为凝聚核心，准确还原了现实科研组织多重从属性与跨界桥接的实质拓扑。
> - **研究者判断** 核心参数 $k$（团的节点规模阈值）的选择由研究者决定。$k$ 取值过小时（如 $k=3$ 即三角形），社区容易发生过度渗流而合并为一个庞大巨集团；$k$ 取值过大时（如 $k \ge 6$），门槛过高导致绝大多数节点无法成团而沦为未分类黑点。通常依据网络度分布与渗流相变临界点选取中等参数（如 $k=3$ 或 $k=4$）。
> - **有效性标准** 内部子图完全连通性（团内密度为 1）、社区重叠度、渗流集团稳定性以及对学科实际学派构成的解释效度。
> - **不声称回答的问题** 该算法属于纯拓扑结构划分工具，不能直接度量社区内部思想共识的深浅，亦无法依据社区规模直接推断学派的学术影响力高低或因果突破能力。

> [!method-stack] 方法层级
> - **上位方法** [[Network Analysis]]（复杂网络分析）中的社区发现方法族（Community Detection Algorithms）。
> - **前置步骤** 学者实体消歧（Author Name Disambiguation）、合著邻接矩阵构建、极大完全子图（Maximal Cliques）搜索算法。
> - **变体与扩展** 加权团渗流算法（Weighted CPM，引入边权重门槛过滤低频合作）、二部图团渗流算法（处理学者与论著附属网络）、动态演化团渗流算法（Sequential CPM，追踪学派随时间的产生、分裂与消亡）。

---

> [!dev-timeline] 方法演变
> - **1973 — 图论极大团搜索算法建立** 科恩·布朗（Coen Bron）与约普·克博斯（Joep Kerbosch）提出 Bron-Kerbosch 深度优先分支定界算法，确立了在无向图中枚举全部极大团的标准计算框架。
> - **2005 — 团渗流算法提出并确立重叠社区范式** 盖尔盖伊·保洛（Gergely Palla）、伊姆雷·德雷尼（Imre Derényi）、伊勒什·法尔卡什（Illés Farkas）与陶马什·维切克（Tamás Vicsek）在《自然》（*Nature*）刊发奠基性成果，正式提出团渗流算法，开创了重叠社区发现的全局拓扑分析范式。
> - **2007 — 社群动态演进追踪模型** Palla 等人在《自然》（*Nature*）将团渗流法扩展至时间序列，通过康奈尔大学 arXiv 物理学逾 3 万名学者合著网络实测，揭示出大型科研群体的渐进代谢与微型研究小组的剧烈存亡动力学。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Palla et al., 2005; Wang & Barabási, 2021, p. 104)]]

---

> [!formula-set]- 公式链总览
> ```mermaid
> flowchart LR
>   A["合著无向网络 G=(V, E)"] --> B["枚举所有 k-团 (k-cliques)"]
>   B --> C["构建 k-团邻接矩阵 (共享 k-1 个节点)"]
>   C --> D["连通子图遍历 (渗流聚类)"]
>   D --> E["输出重叠社区集合与游离节点"]
> ```

> [!formula-step] 步骤一　$k$-团相邻性判定
> $$A_{ij}^{(k)} = \begin{cases} 1, & \text{若 } |V(C_i) \cap V(C_j)| = k-1 \\ 0, & \text{其他} \end{cases}$$
>
> **这个公式在做什么** 计算两个大小为 $k$ 的完全连通子图 $C_i$ 与 $C_j$ 是否在拓扑上互为“相邻团”，构建团水平的高阶邻接矩阵。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 104)]]
>
> **符号说明**
> - $C_i, C_j$：网络中任意两个包含 $k$ 个节点的完全连通子图（$k$-clique），即子图内任意两节点之间均存在连边。
> - $V(C_i)$：子图 $C_i$ 包含的节点集合。
> - $|V(C_i) \cap V(C_j)|$：两个 $k$-团共享的共同节点数量。
> - $A_{ij}^{(k)}$：团邻接矩阵元素，当且仅当两团恰好共享 $k-1$ 个节点时取值为 1。
>
> **数学直觉** 阈值截断与高阶连续性。普通网络连接基于点和边；团渗流法将包含 $k$ 个节点的密实小圈子视为基本单元，只有当两个小圈子重叠了绝大部分成员（$k-1$ 人）时，信息与规范才能顺畅横跨，构成具有凝聚力的高阶通道。
>
> > [!example]- 手算示例
> > 设定参数 $k=3$（即三角形完全图）。
> > 假定学者团队存在两个三角形小圈子：
> > - 圈子 1：学者 $\{A, B, C\}$ 之间两两互有合署发表；
> > - 圈子 2：学者 $\{B, C, D\}$ 之间两两互有合署发表。
> > 计算共同学者集合：$\{A, B, C\} \cap \{B, C, D\} = \{B, C\}$，交集规模为 $2 = 3 - 1$。
> > 判定两团相邻，$A_{12}^{(3)} = 1$。学者 $\{A, B, C, D\}$ 由此合并构成同一个 3-团社区，学者 $B$ 与 $C$ 充当内部连通骨架。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 相邻充分性 | 两个 $k$-团即便只有 1 个节点不同，只要共享 $k-1$ 个节点，即可形成平滑渗流过渡。 |
> > | 注意 | 节点多重归属 | 若学者 $D$ 同时属于另一个仅与学者 $D$ 相连的 3-团 $\{D, E, F\}$，学者 $D$ 将同时属于两个社群，具备双重社区身份。 |

---

> [!formula-step] 步骤二　渗流集团合并与社区节点集合输出
> $$\mathcal{C}_m = \bigcup_{C_i \in \mathcal{K}_m} V(C_i)$$
>
> **这个公式在做什么** 对团邻接图中的每个极大连通分支 $\mathcal{K}_m$，取其包含的所有 $k$-团节点的并集，输出第 $m$ 个重叠社区的全部成员集合 $\mathcal{C}_m$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 104)]]
>
> **符号说明**
> - $\mathcal{K}_m$：团邻接网络经过图遍历识别出的第 $m$ 个极大连通子图（连通分支）。
> - $\mathcal{C}_m$：第 $m$ 个重叠社区所囊括的学者节点全集。
> - $\bigcup$：并集运算，将连通团集内的所有成员去重合并。
>
> **数学直觉** 集合论意义上的并集凝聚。通过将紧密相扣的连通团连续铺展，形成像水滴渗流般蔓延的社群边界，未被任何 $k$-团覆盖的边缘孤立节点则被排除在所有社区之外。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 社区重叠度 | 当存在学者 $u \in \mathcal{C}_p \cap \mathcal{C}_q$（$p \neq q$）时，学者 $u$ 即为跨越两个学派社群的交叉学科桥梁纽带。 |
> > | 注意 | 参数临界敏感性 | 若 $k$ 选得过低，全部 $k$-团容易发生巨连通相变，导致不同学派被机械融合成一个无法辨识局域特征的超大集团。 |

> [!software-impl] 软件实现
> - **官方原生程序** 原创团队开发的独立开源软件 **CFinder**（提供 C++ 核心算法引擎与跨平台 Java 图形界面，原生支持无向、加权、有向网络的 $k$-团渗流与社群演化追踪）。
> - **核心包或命令** Python (`networkx.algorithms.community.k_clique_communities`)、R (`linkcomm`, `igraph`)、C++ (SNAP 复杂网络库)。
> - **实现流程** 提取合著边列表并构建无向图；调用 `k_clique_communities(G, k)` 获得各重叠社区的节点集合；比对节点在各集合中的出现频次，分离出跨学科桥梁学者与外围游离节点。
> - **报告标准** 明确汇报团规模参数 $k$ 的选取依据（如 $k=3$ 或 $k=4$）、网络极大连通分支覆盖率、识别出的社区总数、重叠节点比例以及未成团游离节点的统计占比。

> [!formula] Python 计算骨架
> ```python
> import networkx as nx
> from typing import List, Set, Dict, Any
> 
> def detect_overlapping_communities_cpm(
>     edge_list: List[tuple], 
>     k: int = 3
> ) -> Dict[str, Any]:
>     """使用团渗流算法 (CPM) 识别无向合著网络中的重叠社区。
>     
>     参数:
>         edge_list: 合作关系边列表，形如 [("Scholar_A", "Scholar_B"), ...]
>         k: 团的节点规模阈值 (k >= 3，默认为 3 即三角形完全子图)
>     """
>     # 1. 构建无向科研合署网络
>     G = nx.Graph()
>     G.add_edges_from(edge_list)
>     
>     # 2. 调用 NetworkX 内置团渗流算法枚举相邻 k-clique 连通组件
>     communities_gen = nx.algorithms.community.k_clique_communities(G, k)
>     communities = [set(c) for c in communities_gen]
>     
>     # 3. 统计各学者的社群从属度，识别跨界桥梁学者与游离节点
>     node_membership: Dict[str, List[int]] = {node: [] for node in G.nodes()}
>     for comm_id, comm_nodes in enumerate(communities):
>         for node in comm_nodes:
>             node_membership[node].append(comm_id)
>             
>     overlapping_scholars = {
>         node: comms for node, comms in node_membership.items() if len(comms) > 1
>     }
>     isolated_scholars = {
>         node for node, comms in node_membership.items() if len(comms) == 0
>     }
>     
>     return {
>         "total_communities": len(communities),
>         "communities": communities,
>         "overlapping_scholars": overlapping_scholars,
>         "isolated_scholars": isolated_scholars
>     }
> ```

---

> [!method-fit] 适用判断
> - **适合使用**
>   - 科研合著网络中识别跨学科交叉学者与多重学派从属结构。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 104)]]
>   - 蛋白质相互作用网络中识别多功能蛋白质复合物。
>   - 追踪学术共同体随时间推移的演化轨迹（合并、分裂与新生）。
> - **谨慎使用**
>   - 极其稀疏的网络（因高阶完全子图极难自发形成，算法容易将绝大多数节点误判为游离节点）。
>   - 包含超大规模完全子图的极稠密网络（极大团枚举是 NP-hard 问题，时间复杂度在极端稠密子图中较高）。
> - **不适合使用**
>   - 必须得到严格无重叠分块矩阵的传统层次聚类任务。
>   - 有向有权且强调严格层级因果传导的流程网络。

---

> [!method-limits] 方法局限
> - **计算复杂度瓶颈** 全图枚举所有 $k$-团受制于团搜索算法的高阶计算开销，面对数百万节点的极稠密大图需依赖近似剪枝策略。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 104)]]
> - **低度边缘节点的过度排斥** 该方法要求至少形成三节点完全互联结构（$k \ge 3$），仅有单线合作的年轻学者或边缘研究者会被直接标记为无派系的孤立黑点，难以刻画其微观外围演进。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 104)]]
> - **参数选择的主观依赖** 最优 $k$ 缺乏统一的自动化统计判据，研究者往往依赖试错法比对渗流集团规模分布，给跨学科比较引入了参数敏感性。

---

> [!evidence-grid-a|notitle] 典型应用研究
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit04|Wang & Barabási (2021)]] — 第 10.1 节引介团渗流算法在分析 arXiv 预印本平台（cond-mat）逾 3 万名物理学者合著网络中的应用，直观图示物理学界局域紧密互联的多彩派系社区拓扑（图 10-1，p. 104）。
