---
title: Hyperlink-Induced Topic Search
aliases:
  - HITS算法
  - HITS 算法
  - 枢纽与权威中心度算法
  - 枢纽与权威算法
  - Kleinberg's HITS
  - Hubs and Authorities
summary: "由 Jon Kleinberg（1999）提出的有向图节点中心度互促迭代算法。该算法将网络节点划分为两种相互依存的拓扑角色：枢纽（Hubs，指向多个高质量权威节点的节点）与权威（Authorities，被多个高质量枢纽节点所指向的节点）。在科学计量与引文网络分析中，HITS 算法被用于测度科研机构的提名与认可声誉，通过交互迭代稳定求解节点的枢纽中心度与权威中心度，揭示知识流动与学术霸权转移的拓扑结构。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 5
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/model
related_concepts:
  - "[[Placement Power]]"
  - "[[Scientific Hegemony]]"
related_theories: []
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Binary Logistic Regression]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_VonDerHeyden_Heinze_2025_PLOSONE]]"
confidence: high
status: draft
created: 2026-11-21
updated: 2026-11-21
---

---

> [!def] Hyperlink-Induced Topic Search
> 超链接诱导主题搜索算法（Hyperlink-Induced Topic Search, HITS），又称枢纽与权威算法（Hubs and Authorities），是由乔恩·克莱因伯格（Jon Kleinberg, 1999）提出的有向图节点拓扑分析算法。输入有向网络的邻接矩阵，通过枢纽值（Hub Score）与权威值（Authority Score）的相互迭代与归一化，输出刻画各节点指向质量与被指向声望的稳健特征向量。在科学社会学与科学计量学中，该方法被用于测度科研机构发出高质量推荐（Hub）与被高水平同行认可（Authority）的结构性地位。[[Argument_VonDerHeyden_Heinze_2025_PLOSONE|(von der Heyden & Heinze, 2025, pp. 6–7)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 链接 [[Placement Power]] 与 [[Scientific Hegemony]]。测度有向关系网络中节点的权威声誉与推举能力。
> - **问题类型** 网络拓扑分析、学术声誉评价与节点中心度测度。
> - **分析单位** 科研机构、大学院系、学术学者、学术期刊或网页。
> - **输入数据** 有向加权或非加权网络邻接矩阵（如机构间提名矩阵、引文链接矩阵）。
> - **输出形式** 介于 0 到 1 之间的归一化枢纽中心度向量与权威中心度向量。

> [!citation-card] 关键定义
> 有向组织提名网络的拓扑结构通过克莱因伯格的枢纽与权威中心度指标进行刻画。节点大小对应中心度取值，能够同时捕捉处于核心推举地位的提名机构（枢纽，Hubs）以及频繁接收提名的被认可机构（权威，Authorities）。这一度量能够直观展现随着全球科学领导权转移，主要科研机构在拓扑网络中的地位演进。[[Argument_VonDerHeyden_Heinze_2025_PLOSONE|(von der Heyden & Heinze, 2025, pp. 6–7, 10–11)]]
>
> *The size of the nodes (representing organizations) is proportional to Kleinberg’s hub and authority centrality measures, which capture both the role of central nominating organizations (hubs) and those that receive frequent nominations (authorities)... These findings are consistent with both hub centrality (organizations frequently nominating) and authority centrality (organizations frequently nominated) measurements.*

---

> [!method-position] 方法定位
> - **构念效度** 区别于简单的入度与出度计数，HITS 算法通过邻域节点的质量进行递归赋权，能准确识别出由于连接了重要节点而获得高阶声望的网络结构位置。
> - **研究者判断** 决定邻接矩阵的边权设定（二值化或频数加权）、迭代终止阈值 $\epsilon$ 与最大迭代轮次。
> - **有效性标准** 特征向量幂迭代的数值稳定性与节点相对位次排序的一致性。
> - **不声称回答的问题** 描述性拓扑指标不能推导出行动主体的主观动机，亦不能单独作为因果效应识别的充分证据。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis]] 与复杂网络拓扑分析。
> - **前置步骤** 机构实体消歧、历史机构合并对齐（如 1970 年法国大学重组前巴黎大学的归并处理）、构建有向邻接矩阵。
> - **变体与扩展** 包含加权 HITS（Weighted HITS）、时间衰减 HITS 以及与 PageRank 融合的双向排序模型。

> [!dev-timeline] 方法演变
> - **1999 — 算法提出** Jon Kleinberg 在 *Journal of the ACM* 提出超链接网络环境下的 Hub 与 Authority 互促递归模型。
> - **2000 年代初 — 科学计量学引入** 被广泛应用于学术评价与引文网络分析，用于识别高影响力学术期刊与核心研究团队。
> - **2025 — 科学制度史应用** von der Heyden 与 Heinze（2025）将其拓展应用于跨越 70 年的诺贝尔奖提名档案网络，揭示美德科学霸权转移中的大学拓扑地位重构。

---

> [!formula-set]- 公式链总览
> ```mermaid
> flowchart LR
>   A["有向加权/非加权邻接矩阵 A"] --> B["初始化向量 h0, a0"]
>   B --> C["互促迭代: a = A^T h, h = A a"]
>   C --> D["向量 L2 归一化"]
>   D --> E["收敛判定与特征向量输出"]
> ```

> [!formula-step] 步骤一　权威度与枢纽度的互促更新
> $$a_i^{(t)} = \sum_{j: (j, i) \in E} h_j^{(t-1)}, \quad h_i^{(t)} = \sum_{k: (i, k) \in E} a_k^{(t)}$$
>
> **这个公式在做什么** 权威度（Authority）由所有指向它的节点的枢纽度求和决定；枢纽度（Hub）由它所指向的所有节点的权威度求和决定。[[Argument_VonDerHeyden_Heinze_2025_PLOSONE|(von der Heyden & Heinze, 2025, pp. 6–7)]]
>
> **符号说明** $a_i$ 为节点 $i$ 的权威中心度；$h_i$ 为节点 $i$ 的枢纽中心度；$E$ 为网络中有向边的集合；$t$ 为当前迭代步数。
>
> **数学直觉** 优质的推荐者倾向于推举权威的候选人，而权威的候选人总是获得优质推荐者的认可，形成自洽的互促网络平衡。

> [!formula-step] 步骤二　向量归一化与矩阵特征分解
> $$\mathbf{a}^{(t)} = \frac{\mathbf{A}^T \mathbf{h}^{(t-1)}}{\|\mathbf{A}^T \mathbf{h}^{(t-1)}\|_2}, \quad \mathbf{h}^{(t)} = \frac{\mathbf{A} \mathbf{a}^{(t)}}{\|\mathbf{A} \mathbf{a}^{(t)}\|_2}$$
>
> **这个公式在做什么** 每轮迭代后对权威向量与枢纽向量进行 $L_2$ 范数归一化，防止数值发散。在矩阵形式下，$\mathbf{a}$ 和 $\mathbf{h}$ 分别对应矩阵 $\mathbf{A}^T \mathbf{A}$ 与 $\mathbf{A} \mathbf{A}^T$ 的非负主特征向量。
>
> **符号说明** $\mathbf{A}$ 为网络有向邻接矩阵；$\mathbf{A}^T$ 为其转置矩阵；$\|\cdot\|_2$ 为欧几里得范数。
>
> **数学直觉** 根据佩隆-弗罗贝尼乌斯定理（Perron-Frobenius Theorem），半正定矩阵的幂迭代在适度连通条件下必然求得唯一的非负主特征向量。

> [!example]- 手算示例
> 假设存在 3 所科研机构构成的微型有向提名网络：机构 1 提名机构 2 与机构 3；机构 2 提名机构 3。
> 1. 邻接矩阵为 $\mathbf{A} = \begin{bmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$。
> 2. 初始赋予 $\mathbf{h}^{(0)} = [1, 1, 1]^T$。
> 3. 计算权威向量 $\mathbf{a}^{(1)} = \mathbf{A}^T \mathbf{h}^{(0)} = [0, 1, 2]^T$；归一化后 $\mathbf{a}^{(1)} = [0, 0.447, 0.894]^T$。
> 4. 计算枢纽向量 $\mathbf{h}^{(1)} = \mathbf{A} \mathbf{a}^{(1)} = [1.341, 0.894, 0]^T$；归一化后 $\mathbf{h}^{(1)} = [0.832, 0.555, 0]^T$。
> 结果表明机构 3 拥有最高权威度，机构 1 拥有最高枢纽度。

> [!formula-reading] 结果解读与注意事项
> | 类型 | 要点 | 说明 |
> |---|---|---|
> | 读法 | 权威度取值 | 权威中心度数值越高，说明被越多高水平同行机构所指向，代表受公认的顶尖成果产出中心。 |
> | 读法 | 枢纽度取值 | 枢纽中心度数值越高，说明能够敏锐并集中地识别并推荐高声望候选者，代表核心推举枢纽。 |
> | 注意 | 紧密团伙异常 | 在密集互引或小团体循环互推网络中，HITS 可能出现“紧密链接团伙”（Tightly-Knit Community）偏差，使局部群体的得分被过度放大。 |

> [!software-impl] 软件实现
> - **数据来源** 机构提名档案矩阵或学术引文矩阵。
> - **核心包或命令** Python `networkx.algorithms.link_analysis.hits` 或基于 `scipy.sparse` 构造特征值求解。
> - **实现流程** 提取边列表生成有向图，调用 `hits(G, max_iter=100, tol=1e-08)`，导出节点度量字典并映射为可视化节点大小。
> - **报告标准** 报告迭代容差阈值、最大步数、自环（自提名）的处理方式以及是否采用有权边。

> [!formula] Python 计算骨架
> ```python
> import networkx as nx
> 
> # 构造有向提名网络
> G = nx.DiGraph()
> edges = [
>     ("University of Paris", "HU Berlin", 12),
>     ("Harvard University", "UC Berkeley", 8),
>     ("Columbia University", "Harvard University", 15),
> ]
> for u, v, w in edges:
>     G.add_edge(u, v, weight=w)
> 
> # 计算 HITS 枢纽与权威中心度
> hubs, authorities = nx.hits(G, max_iter=200, tol=1e-8, normalized=True)
> ```

> [!method-stack] 变量与诊断
> - **数据结构** 有向加权图，节点为机构实体，有向边为提名推荐关系。
> - **变量** 出边权重对应提名次数，入边权重对应被提名频次。
> - **识别假设** 网络具备充分的弱连通性，不存在完全孤立的双向不连通子图主导全局主特征向量。
> - **诊断与检验** 通过调整迭代容差参数进行稳定性检验，比对二值化图与加权图在核心排位上的稳健性。

---

> [!method-fit] 适用判断
> - **适合使用** 有向推荐网络、学术同行评选、科技成果引文网络以及具有非对称引用特征的高校声誉格局分析。[[Argument_VonDerHeyden_Heinze_2025_PLOSONE|(von der Heyden & Heinze, 2025, pp. 6–7)]]
> - **谨慎使用** 节点间双向互惠连接极高或自环极密集的局部网络，需剔除自荐或进行权重平滑。
> - **不适合使用** 无向合作网络（如合著网络），无向图上矩阵对称将退化为普通度中心度特征向量。

---

> [!method-limits] 方法局限
> - **团伙偏误风险** 少数机构之间的密集互荐可能垄断主特征向量，掩盖其他具有重要价值但连接分散的节点。
> - **历史消歧挑战** 历史大学重组与院系变迁（如巴黎大学与柏林洪堡大学的历史沿革）对节点归属口径高度敏感。
> - **误用风险** 将算法计算出的权威得分直接等同于客观科研学术水平，忽略了社会声望累积中的马太效应。
> - **补救方式** 结合定性历史档案分析、剔除自校自荐边、引入多元逻辑回归对外部变量进行统计控制。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Placement Power]] | 测量对象 | 枢纽度从拓扑结构角度测度了推选高质量候选者的网络能力。 |
> | [[Scientific Hegemony]] | 理论 | 解释为何权威中心度从欧洲大陆大学向北美顶尖机构发生转移。 |
> | [[Bibliometric Analysis]] | 上位方法 | HITS 属于科学计量学与学术评价的经典网络拓扑分析方法。 |
> | [[Binary Logistic Regression]] | 互补方法 | 结合拓扑网络指标与计量回归模型验证国家与机构特征的边际效应。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_VonDerHeyden_Heinze_2025_PLOSONE|von der Heyden and Heinze (2025)]] — 运用 HITS 算法计算 1901–1933 年与 1934–1969 年间欧美主要科研机构在诺贝尔物理学与化学奖提名网络中的枢纽度与权威度，绘制出全球学术声誉格局从柏林转向哈佛等北美大学的拓扑演进图景。
