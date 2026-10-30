---
title: Two-Mode Network Analysis
aliases:
  - 两模网络分析
  - 二部网络分析
  - 二部从属网络分析
  - Bipartite Affiliation Network Analysis
  - Two-Mode Social Network Analysis
  - 2-Mode SNA
summary: "用于刻画并分析两类异质性行动实体（如决策人员与被调阅证据源）之间从属、咨询或参与关系的社会网络分析方法，通过构建二部图与关联发生矩阵，运用度中心度、网络密度与连通分量分解等拓扑参数，揭示循证生态中核心与边缘的结构割裂。"
type: method
method_type: mixed
method_family: "mixed"
method_related_count: 23
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#fef3c7"
cssclasses:
  - method-manual
tags:
  - method/mixed
  - data-analysis
  - theme/network
  - theme/social-relations
  - theme/research-utilization
related_concepts:
  - "[[Heterogeneity]]"
  - "[[Output-Oriented Governance]]"
  - "[[Document]]"
  - "[[Unit of Analysis]]"
  - "[[Mode 2 Knowledge Production]]"
  - "[[Epistemology]]"
  - "[[Variable]]"
  - "[[Paradigm]]"
  - "[[Co-affiliation]]"
  - "[[Surplus of Evidence]]"
  - "[[Emergence]]"
  - "[[Three Pathways of Research Utilization]]"
related_theories: []
related_methods:
  - "[[Network Analysis]]"
  - "[[Questionnaire]]"
  - "[[Internet-based Survey]]"
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[Latin American Campaign for the Right to Education]]"
  - "[[UNESCO]]"
  - "[[OECD]]"
  - "[[World Bank]]"
  - "[[UNICEF]]"
  - "[[International Institute for Educational Planning]]"
related_arguments:
  - "[[Argument_Steiner-Khamsi_2024_UNESCO]]"
confidence: high
status: draft
created: 2026-10-23
updated: 2026-10-30
---

---

> [!concept-lens] 方法透镜
> - **含义** 刻画两类互不相交的异质实体集合（如决策人员集与证据机构集）之间二元从属或咨询关系的拓扑建模方法。
> - **用途** 用于测绘复杂政策生态中的咨询行为模式，量化宏观证据生态的碎片化程度与核心—边缘分化。
> - **边界** 仅表征行动者对机构的调阅与从属拓扑，不直接度量证据被行政采纳后的实质因果干预效应。

> [!def] Two-Mode [[Network Analysis]]
> 两模网络分析（Two-Mode Network Analysis，亦称二部从属网络分析，Bipartite Affiliation Network Analysis）是社会网络分析（SNA）中用于处理两组具有[[Heterogeneity|异质性]]实体之间二元关系的数学建模与可视化方法。不同于仅包含单一同质行动者（如“学者—学者”合作）的单模网络（One-Mode Network），两模网络包含两个互不相交的节点集合（如“决策人员集”与“证据主体平台集”），边仅存在于两类不同节点之间，用于表征个人对特定组织、事件或知识资源的从属、参与或日常咨询行为。在公共政策[[Output-Oriented Governance|循证治理]]研究中，该方法被用于实证测绘决策者日常查阅证据平台的拓扑连通度，诊断宏观知识生态的离散度与核心—边缘分化格局。[[Argument_Steiner-Khamsi_2024_UNESCO|(Steiner-Khamsi, Faul, et al., 2024, pp. 22–24, 60–61)]]

> [!method-scope] 方法范围
> - **研究对象** 个人行动者与集体实体（机构、会议、政策[[Document|文献]]、证据平台）之间的从属、参与或调阅互动关系。
> - **问题类型** 适合回答两类实体之间的从属模式、知识资源的分布集中度、宏观网络的系统连通性与结构性孤立现象。
> - **[[Unit of Analysis|分析单位]]** 行动者节点（Mode 1）、实体事件节点（[[Mode 2 Knowledge Production|Mode 2]]）以及二者之间的关联边（Affiliation Ties）。
> - **输出形式** 二部图拓扑图谱、关联发生矩阵、度中心度分布表、网络密度系数与独立连通分量子图。

> [!citation-card] 两模证据咨询网络与拓扑结构
> 为识别网络中最核心的证据源，计算了每个证据源的度中心度，即提名使用该证据源的受访者总数。除拉丁美洲 [[Latin American Campaign for the Right to Education|CLADE]] 这一区域机构外，调阅频次最高的机构全为国际多边实体，体现了国际多边组织在全局视角下作为各方最大公约数的显赫地位。[[Argument_Steiner-Khamsi_2024_UNESCO|(Steiner-Khamsi, Faul, et al., 2024, pp. 23–24)]]
>
> *To identify the most central sources in the network, we calculated the degree centrality of a source, which equals the number of respondents indicating that they use the source... It may not be surprising that these most central sources were all international, except one regional source—CLADE—because international sources such as [[UNESCO]], [[OECD]], the [[World Bank]], and [[UNICEF]] are common denominators for all respondents from the global perspective.*

> [!figure]- 图 3.2　教育政策与规划中的证据来源网络拓扑图
> 基于全球[[Questionnaire|问卷调查]]（Q3：日常经常查阅的倡议、网络与平台）构建的“受访者—证据源”两模二部网络（Bipartite Affiliation Network）。图谱直观展现了全球教育证据利用生态在拓扑上的极端离散度与核心—边缘割裂格局。
>
> ![图3.2：教育政策与规划中的证据来源网络拓扑图](https://img.mylikemie.icu/sources/Steiner-Khamsi_2024_UNESCO/figures/Steiner-Khamsi_2024_UNESCO_Fig3-2_Network_Research_Evidence_Sources.jpg)

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 坚持关系性结构主义知识观，认为证据的现实政策效力由其在制度网络中的拓扑位置决定；即便科学证据具有严谨的学术价值，若其载体机构在拓扑上处于隔离子群，依然无法发挥实际政策影响力。
> - **研究者角色** 客观网络拓扑测绘者，基于行动者自我报告的真实查阅行为构建关系矩阵，排除主观声望评价的偏误。
> - **有效性标准** 数据回收的跨区域代表性、机构实体去重与名称标准化的准确性、关联发生矩阵的完备性。
> - **不声称回答的问题** 不直接回答证据本身的学术研究质量（内部有效性），亦不测量政策被实际采纳后的因果干预效应。

> [!method-stack] 数据、[[Variable|变量]]与拓扑指标
> - **两模节点构成** 
>   - 行动者集合（Mode 1）：填写日常咨询来源的 286 位全球教育决策官员与实证研究专家。
>   - 实体集合（Mode 2）：被提名的 432 个独立研究倡议、网络与证据平台（国家级 234 个、国际级 124 个、区域级 74 个）。
> - **拓扑核心参数**
>   - **度中心度（Degree Centrality）** 单个证据机构被受访者提名的总人次数，反映其在实务界的知名度与日常调阅频次。
>   - **网络密度（Network Density）** 全网实际观测到的咨询连边总数与理论最大可能连边数之比。全球调查实测密度仅为 0.006，呈现极度稀疏与分散形态。
>   - **连通分量分解（Connected Components）** 全网被分割为 121 个完全互不通达的孤立子群。其中 1 个庞大的主连通分量居于中央（由多边国际机构主导），其余 120 个离散子群孤悬在外围，多为单一受访者咨询的本土院校。

---

> [!formula-step] 公式步骤　二部图邻接矩阵与拓扑参数测算
> $$A = [a_{ij}]_{n \times m}, \quad a_{ij} \in \{0, 1\}$$
> $$\Delta_{\text{bipartite}} = \frac{\sum_{i=1}^n \sum_{j=1}^m a_{ij}}{n \times m}$$
> $$C_D(v_j) = \sum_{i=1}^n a_{ij}$$
>
> **这个公式在做什么** 构建行代表受访者（$n$）、列代表证据机构（$m$）的关联发生矩阵 $A$；测算二部图网络整体密度 $\Delta$ 与机构节点 $v_j$ 的度中心度 $C_D$。
>
> **符号说明**
> - $n$：行动者总人数（本研究为 286 人）。
> - $m$：被调阅机构总数（本研究为 432 个）。
> - $a_{ij}$：二元连边取值；若受访者 $i$ 经常查阅机构 $j$ 则记为 1，否则记为 0。
> - $\Delta_{\text{bipartite}}$：二部图网络密度，取值在 0 与 1 之间。
> - $C_D(v_j)$：机构节点 $v_j$ 的度中心度（即入度频次）。
>
> **数学直觉** 二部图网络密度衡量行动者对全部可选机构的整体激活程度；当网络密度趋近于 0（如 0.006）且包含大量孤立分量时，表明知识流动被严重割裂在相互封闭的局部回音室中。
>
> **结果怎么读** 机构度中心度越高，代表其在政策咨询中的通用性越强，成为跨国讨论的“最大公约数”；网络密度低且分量数量多，证实全球证据生态呈现高度碎片化。

---

> [!proc] 两模从属网络构建与分析程序
> 1. **行为数据采集与实体清洗** 通过[[Internet-based Survey|在线调查]]问卷搜集受访者在实操中经常查阅的具体平台名称；针对填报文本开展多语种去重、全称与缩写归一化（如合并 [[International Institute for Educational Planning|IIEP]] 与联合国教科文组织国际教育规划研究所）。[[Argument_Steiner-Khamsi_2024_UNESCO|(Steiner-Khamsi, Faul, et al., 2024, pp. 21–23, 60–61)]]
> 2. **发生矩阵构建（Incidence Matrix）** 建立 $n \times m$ 维布尔二元关联矩阵，横轴为受访者编号，纵轴为机构名称，完成从属关系赋值。
> 3. **拓扑参数测算与中心度排序** 测算各机构节点的度中心度，排列高频调阅榜单（如 UNESCO 64人、OECD 23人、世界银行 19人、UNICEF 18人）；计算全局网络密度与分量连通度。[[Argument_Steiner-Khamsi_2024_UNESCO|(Steiner-Khamsi, Faul, et al., 2024, pp. 23–24)]]
> 4. **分群与属性投影对比** 依据受访者职业背景（政府部委官员、公民社会代表、大学学者）将全局网络拆分为子网络图（如报告图 3.3 与图 3.4），对比不同利益相关方在证据调阅广度与机构层级上的显著差异。[[Argument_Steiner-Khamsi_2024_UNESCO|(Steiner-Khamsi, Faul, et al., 2024, pp. 24–25)]]
> 5. **图谱可视化布局与治理诊断** 采用力导向算法（Force-directed Layout）对二部图实施空间排布；结合节点地理层级（国际/区域/国家）配置节点颜色与尺寸，揭示全球知识流通中的结构性断裂。

---

> [!contrast-table] 网络分析方法辨析
> | 分析维度 | 两模二部网络分析（Two-Mode Affiliation SNA） | 单模社会网络分析（One-Mode SNA） | 文献计量共被引分析（Co-citation Analysis） |
> |---|---|---|---|
> | **节点性质** | 两类不同性质的节点集合（行动者与机构/事件） | 单一性质的节点集合（如学者与学者，或官员与官员） | 单一学术文献或期刊实体节点 |
> | **连边含义** | 跨异质实体的从属、参与、调阅或咨询行为 | 同类实体之间直接的人际交往、合作或通联 | 学术文献被第三方共同引用的客观计量关联 |
> | **数据源** | 调查问卷、委员会花名册、参会签到表 | 人际交往问卷、社交通讯记录、邮件往来 | 商业学术引文数据库（如 Web of Science） |
> | **核心用途** | 揭示行动者与组织制度平台的重合度及生态割裂 | 测度群体内部人际关系密度、小世界效应与小团体 | 评估学术学术界的知识演进脉络与[[Paradigm\|范式]]分化 |

---

> [!software-impl] 软件实现
> - **数据整理与矩阵转换** Python（`pandas`, `networkx`）或 R（`igraph`, `tidygraph`）读取问卷表格并生成二部邻接图。
> - **拓扑计算命令** 在 Python 中使用 `networkx.bipartite.density(B, nodes)` 计算两模密度，`bipartite.degrees(B, nodes)` 计算各节点度数。
> - **图谱布局可视化** 借助 Gephi、Cytoscape 或 NetDraw 载入发生矩阵，选用 ForceAtlas2 算法进行节点聚类展开，并按属性赋予颜色映射。

---

> [!theory-boundary] 局限性与适用边界
> - **适合分析** 政策咨询网络测绘、跨国治理机构参与模式识别、董事会[[Co-affiliation|连锁任职]]（Interlocking Directorates）分析、学术会议参会网络。
> - **适用条件** 拥有清晰界定的两类异质实体清单；具备可靠的实际从属或调阅记录，能有效防范样本自选择偏差。
> - **局限性** 受访者报告存在回忆偏误或社会赞许性偏误（倾向报告知名国际多边机构）；单纯的调阅频次无法直接等同于政策制定中的实质性采纳深度。

---

> [!entry-map] 相关条目网络
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Network Analysis]] | Method | 本方法归属的上位社会网络分析方法家族。 |
> | [[Bibliometric Analysis]] | Method | 报告中用于与本两模咨询网络进行互补对照的客观学术引文网络分析方法。 |
> | [[Surplus of Evidence]] | Concept | 本两模拓扑分析实证揭示的“海量机构[[Emergence\|涌现]]但网络极度分散”的核心概念表征。 |
> | [[Three Pathways of Research Utilization]] | Concept | 依据两模网络揭示的核心—边缘割裂格局而提出的跨层级系统治理对策。 |
