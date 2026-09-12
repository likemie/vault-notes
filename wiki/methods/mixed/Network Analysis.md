---
title: Network Analysis
aliases:
  - 网络分析
  - social network analysis
  - SNA
  - 社会网络分析
summary: "通过识别行动者、关系、节点和连接来测量社会关系结构与动态的混合方法，广泛应用于课堂人际互动、学校组织协作及跨国政策中介网络的结构解析。"
type: method
method_type: mixed
method_family: "mixed"
method_related_count: 31
method_related_level: 3
method_related_stars: "⭐⭐⭐"
method_related_color: "#fef3c7"
tags:
  - method/mixed
  - data-analysis
  - theme/social-relations
  - theme/network
  - theme/knowledge-mobilisation
related_concepts:
  - "[[Unit of Analysis]]"
  - "[[Hypothesis]]"
  - "[[Epistemology]]"
  - "[[Emergence]]"
  - "[[Reliability]]"
  - "[[Construct Validity]]"
  - "[[Construct]]"
  - "[[Research Question]]"
  - "[[Educational Brokerage Agency]]"
  - "[[Gatekeepers]]"
  - "[[Structural Holes]]"
  - "[[Knowledge Mediation]]"
  - "[[Policy Brokerage]]"
  - "[[Boundary Spanner]]"
  - "[[Causality]]"
  - "[[Ontology]]"
  - "[[Knowledge Mobilisation]]"
related_theories:
  - "[[Complexity Theory]]"
related_methods:
  - "[[Mixed Methods Research]]"
  - "[[Questionnaire]]"
  - "[[In-depth Interview]]"
  - "[[Accounts]]"
  - "[[Sociometry]]"
  - "[[Data Transformation]]"
  - "[[Qualitative Observation]]"
  - "[[Qualitative Interview]]"
  - "[[Triangulation]]"
  - "[[Participant Observation]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[EU Evidence-Informed Education Policy Initiatives]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch22]]"
  - "[[Argument_Burns_Schuller_2022_BrokerageAgencies]]"
confidence: high
status: active
created: 2026-07-22
updated: 2026-09-13
---

# Network Analysis

---

## 定义

> [!def] 方法定义
> 网络分析（Network Analysis / Social Network Analysis, SNA）是一门用于测量、绘制和解释社会情境中**行动者及其连接关系结构规律性**的混合研究方法（Knoke & Yang, 2008, p. 4）。其核心理论假定认为，行动者在网络中的位置与连接形态（即宏观-结构关系）比年龄、性别、阶级等个体传统属性能够更深刻地解释其社会行为与认知流动，且网络关系具有高度的情境特定性（Context-Specific）与时间演进动态性（Dynamic）（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch22|Cohen et al., 2011, pp. 625–626]]）。

> [!method-scope] 方法范围
> - **研究对象** 社会与组织网络中的行动者（Actors / 节点 Nodes）、关系与纽带（Relations / 连接 Ties），以及网络整体的拓扑结构特征。
> - **适用问题** 识别核心关键行动者（中心度）、分析信息与资源流动阻滞点、探测凝聚子群（小集团 / 派系 Cliques）、评估跨组织中介与边界跨越效应。
> - **[[Unit of Analysis|分析单位]]** 个体层次（自我中心网络 Ego-Network） $\to$ 对偶层次（Dyads） $\to$ 三元闭包层次（Triads） $\to$ 完整跨组织/宏观系统网络（Whole Network）（Knoke & Yang, 2008, pp. 13–15）。
> - **典型输出** 社会关系网络图（Sociograms）、邻接矩阵（Adjacency Matrices）、中心性指数、网络密度、核心-边缘结构模型（Core-Periphery Models）。

> [!citation-card]- 关键定义：社会网络分析的结构解释力
> 社会网络分析试图测量和绘制社会实体之间关系的规律模式。其基本理论前提是，解释人们行为的关键不在于其孤立的个体属性，而在于其所嵌入的社会网络结构规律。
>
> *"Social network analysis seeks to measure and map the structural regularities of relationships among social entities... The core [[Hypothesis]] is that these macro-structural relations explain people’s behaviour more powerfully than traditional individual categories."*（Knoke & Yang, 2008，引于 [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch22|Cohen et al., 2011, p. 625]]）

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 关系实在论（Relational Realism）。认为社会现实是由相互联系的纽带构成的系统，整体网络具有超越个体属性之和的[[Emergence|涌现]]特征（Emergent Properties），与[[Complexity Theory|复杂性理论]]深度契合。
> - **研究者角色** 兼具客观测度与质性解释：量化提取网络拓扑结构指标，结合田野访谈解释关系背后的信任、权力、专业互助或资源交换意图。
> - **有效性标准** 边界界定的完整性与合理性、关系数据重测一致性（[[Reliability]]），以及关系测度与真实社会互动的[[Construct Validity|建构效度]]（[[Construct]] Validity）。
> - **不声称回答的问题** 不能从静态网络拓扑结构截面数据中直接推断确定性因果方向；每个分析层次的涌现规律不能完全简化还原为低层次个体的心理偏好。

> [!method-stack] 方法层级
> - **研究设计** [[Mixed Methods Research|混合方法]]社会网络分析（Mixed-Methods SNA）、全网络纵向追踪、多层自我中心网络设计。
> - **数据收集** 关系名录调查[[Questionnaire|问卷]]（如“你在日常教学中会向谁寻求专业咨询？”）、数字化沟通交互日志提取、[[In-depth Interview|深度访谈]]与[[Accounts|陈述法]]（[[Accounts]]）。
> - **分析方法** [[Sociometry|社会计量学]]测度、中心度与中介度计算、网络密度分析、QAP 关系[[Hypothesis|假设]]检验、块模型（Blockmodeling）。
> - **辅助软件** UCINET、NetDraw、Gephi、Pajek，以及 R 语言扩展包（`igraph`、`tidygraph`、`sna`）、Python（`networkx`）。

---

## 研究程序

> [!proc] 通用研究规程
> 1. **界定[[Research Question|研究问题]]与网络边界** 明确分析对象为班级同伴、学校教研网络还是跨国[[Educational Brokerage Agency|知识中介机构]]网络，采用名录列表法（Roster）或自由提名滚雪球法确定网络边界。
> 2. **确定关系形式与内容维度** 明确连接的实质内容：寻求专业建议、资源共享、政策咨询或情感支持；界定有向（Directed）或无向（Undirected）、二元（0/1）或赋权（Weighted）连接。
> 3. **构建关系矩阵与清洗数据** 将收集的关系[[Data Transformation|数据转换]]为 $N \times N$ 的邻接矩阵，处理对称性与缺失节点。
> 4. **计算网络拓扑测度** 计算网络整体密度、传递性、各节点度数与中介中心度，探测子群聚类。
> 5. **混合质性情境化解释** 结合访谈与[[Qualitative Observation|田野观察]]，解释高中心度节点的领导力成因及孤立边缘节点的结构性阻隔。

### 量化分析与核心测度公式

> [!formula-step] 公式步骤一　点度中心度（Degree Centrality）
> $$C_D(n_i) = d(n_i) = \sum_{j=1}^{g} x_{ij}$$
>
> **这个公式在做什么** 计算网络中与特定节点 $n_i$ 直接相连的邻居节点总数（在有向图中拆分为点入度 In-Degree 与点出度 Out-Degree）。
>
> **符号说明** $n_i$ 为目标节点；$x_{ij}$ 为节点 $i$ 与节点 $j$ 之间的连接值（1 为有连接，0 为无连接）；$g$ 为网络中的节点总规模。
>
> **数学直觉** 衡量节点在网络中的直接可达性与活跃程度。
>
> **结果怎么读** 在教师教研网络中，点入度高代表该教师被大量同行视为专业求助对象（教学权威或核心顾问）；点出度高代表该行动者对外寻求信息的积极度。

> [!formula-step] 公式步骤二　中介中心度（Betweenness Centrality）
> $$C_B(n_i) = \sum_{j < k} \frac{g_{jk}(n_i)}{g_{jk}}$$
>
> **这个公式在做什么** 测算目标节点 $n_i$ 位于网络中其他所有节点对最短路径（Geodesic Paths）上的频率，量化其扮演“信息[[Gatekeepers|把关人]]”与“桥梁”的能力。
>
> **符号说明** $g_{jk}$ 为节点 $j$ 与节点 $k$ 之间的最短路径总数；$g_{jk}(n_i)$ 为包含节点 $n_i$ 的最短路径条数。
>
> **数学直觉** 捕捉处于“[[Structural Holes|结构洞]]”（Structural Holes）关键位置的节点对跨网络信息流动的控制力。
>
> **结果怎么读** 在跨组织[[Knowledge Mediation|知识中介]]网络中，中介中心度高的组织（如跨国元中介）承担连接不同学术子网络与实践群体的关键中介功能（[[Argument_Burns_Schuller_2022_BrokerageAgencies|Burns & Schuller, 2022, pp. 67–68]]）。

> [!formula-step] 公式步骤三　网络密度（Network Density）
> $$\Delta = \frac{2L}{g(g-1)}$$
>
> **这个公式在做什么** 计算无向网络中实际存在的连接总数 $L$ 与理论上可能存在的最大连接数之比。
>
> **符号说明** $L$ 为网络实际拥有的边数；$g$ 为网络节点总数。
>
> **数学直觉** 衡量整体网络的连通紧密度与关系丰富程度，取值介于 0 到 1 之间。
>
> **结果怎么读** 密度过低意味着网络松散碎片化，存在大量孤岛；密度过高则可能引发信息同质化与小集团壁垒。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 
>   - 分析学校内部教师专业学习社群中的“同行建议寻求”网络结构；
>   - 解析跨区域、跨国教育[[Policy Brokerage|政策中介]]机构（如 [[EU Evidence-Informed Education Policy Initiatives|EIPPEE]]）之间的合作与资源共享拓扑；
>   - 识别教育改革推进中的关键“[[Boundary Spanner|知识经纪人]]”（Knowledge Brokers）与孤立学校；
>   - 测度在线教师研修社区中的社会互动与知识共建质量。
> - **谨慎使用** 参与者流动频繁的临时项目网络；网络边界模糊且难以界定纳入排除标准的社会群体。
> - **不适合使用** 纯粹关注个体心理认知属性而脱离人际互动的实验心理学研究；样本规模极小（小于 5 人）难以形成拓扑结构的情境。

---

## 局限性

> [!method-limits] 方法局限与反思
> - **边界界定偏差（Boundary Specification Problem）** 人为划定网络边界极易切断跨界连接，导致边缘节点被误判为结构性孤立。
> - **静态截面与[[Causality|因果推断]]陷阱** 传统横截面网络图往往忽略动态演化；将中心度高直接等同于因果影响力可能产生内生性偏差（如高威望导致的连接集中，而非连接带来威望）。
> - **自报告关系的数据敏感性** 询问“你最信任谁/向谁求助”容易引发社会赞许偏差（Social Desirability Bias）或防范心理，导致关键隐性网络漏报。
> - **应对策略** 引入纵向多期网络动态模型（如 SIENA 模型），并结合深度[[Qualitative Interview|质性访谈]]进行[[Triangulation|三角互证]]。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[Sociometry]] | 前置方法 | 莫雷诺（Moreno, 1934）社会计量学是社会网络分析的奠基之源，确立了点线图基石。 |
> | [[Accounts]] | 补充质性方法 | 陈述法为量化网络拓扑提供行动者主观动机与情境意义的质性透镜。 |
> | [[Complexity Theory]] | 对应理论基础 | 网络[[Emergence\|涌现]]属性与复杂自适应系统论为网络分析提供了[[Ontology\|本体论]]支撑。 |
> | [[Educational Brokerage Agency]] | 研究应用对象 | 网络分析用于解析多国教育中介机构之间的横向协作与知识流转。 |
> | [[Knowledge Mediation]] | 研究应用领域 | 网络分析是测度[[Knowledge Mobilisation\|知识动员]]中多方主体社会关系互动的核心工具。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch22]] — 系统梳理社会网络分析的方法论源流、五大分析维度、七大关系类型学及矩阵图形展示技术。
> - [[Argument_Burns_Schuller_2022_BrokerageAgencies|Burns & Schuller (2022)]] — 运用[[Participant Observation|参与观察]]与网络分析方法，深入剖析欧洲 23 国 36 家机构构成的 [[EU Evidence-Informed Education Policy Initiatives|EIPPEE]] 跨国教育[[Knowledge Mediation|知识中介]]网络，提炼元中介协同维系机制与制度张力。
