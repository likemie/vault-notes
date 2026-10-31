---
title: Bibliometric Analysis
aliases:
  - 文献计量分析
  - 文献计量学
  - 科学计量分析
  - 科学计量学
  - Bibliometrics
  - Scientometrics
  - 共被引网络分析
summary: "运用数学与统计学方法对学术文献外部特征、引文网络与文本共现进行量化测度的实证研究方法，广泛用于测绘学科知识图谱、追踪理论演进与识别知识共同体结构。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 25
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/bibliometrics
  - theme/scientometrics
  - theme/knowledge-production
related_concepts:
  - "[[Document]]"
  - "[[Scientific Productivity]]"
  - "[[Unit of Analysis]]"
  - "[[Research Problem]]"
  - "[[Paradigm]]"
  - "[[Champ]]"
  - "[[Epistemology]]"
  - "[[Knowledge Production]]"
  - "[[Literature Search]]"
  - "[[Literature Review]]"
  - "[[Causality]]"
  - "[[Variable]]"
  - "[[Research Utilization]]"
  - "[[Citation Disparity]]"
related_theories: []
related_methods:
  - "[[Systematic Review]]"
  - "[[Network Analysis]]"
  - "[[Survey Research]]"
  - "[[Questionnaire]]"
  - "[[Disruption Index]]"
  - "[[Relative Citation Normalization]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Steiner-Khamsi_2024_UNESCO]]"
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit05]]"
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit01]]"
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit07]]"
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit09]]"
confidence: high
status: active
created: 2026-10-22
updated: 2026-10-31
---

---

> [!def] Bibliometric Analysis
> [[Document|文献]]计量分析（Bibliometric Analysis）是运用数学与统计学方法对已发表学术文献的载体特征、学者合作网络、关键词共现频率以及引文网络展开量化建模的实证研究方法。该方法主要用于呈现特定学科领域的宏观演进趋势、核心研究前沿、学科分支结构以及学者共同体的引证关联格局。[[Argument_Steiner-Khamsi_2024_UNESCO|(Steiner-Khamsi, Faul, et al., 2024, p. 64)]]; [[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 117–118)]]

> [!method-scope] 方法范围
> - **研究对象** 同行评审期刊刊载成果、学术专著、会议文献、专利报告、[[Systematic Review|系统综述]]与引文索引数据库记录。
> - **问题类型** 适合回答[[Scientific Productivity|学术生产力]]增长率测算、高影响力学者与成果识别、学科知识基础追踪、跨学科引用模式比较以及概念演化路径分析。
> - **[[Unit of Analysis|分析单位]]** 单篇文献、科研人员、研究机构、国家、出版期刊、学科领域或引文网络中的节点与聚类。
> - **输出形式** 历年发文量增长曲线、引文频次分布、高被引文献排行榜、共被引网络聚类图谱、关键词共现网络及主题演化流向图。

> [!citation-card] 科学图谱与文献计量的计算定位
> 文献计量分析旨在运用文本分析与引文分析计算技术，生成研究领域的全景图景。该方法是识别核心[[Research Problem|研究议题]]并利用计算途径呈现学术宏观图景的标准化[[Paradigm|范式]]。通过关键词分析识别核心主题演进，借助共被引分析生成学科领域全景并提取知识聚类。[[Argument_Steiner-Khamsi_2024_UNESCO|(Steiner-Khamsi, Faul, et al., 2024, p. 64)]]
>
> *Bibliometric analysis aims to generate a picture of a research [[Champ|field]] using both text analysis and citation analysis. It is a way of identifying core research topics and illustrating an academic landscape using a computational approach. Here, we used a keyword analysis to identify important themes in education and public health research and how those have changed over time. We also used a co-citation analysis to generate an overview of the field and to extract research clusters.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 视学术成果的引用关系与发表记录为[[Knowledge Production|知识生产]]、流动与合法化过程的物质化痕迹；认为文献之间的引证关联反映了概念亲缘性、学术认同与范式分化。
> - **研究者角色** 研究者在检索式设计、数据库选择、停用词清洗、共被引阈值设定及聚类算法挑选过程中扮演裁量角色，需要结合领域专长对计算图谱进行实质性质性解读。
> - **有效性标准** 遵循[[Literature Search|文献检索]]策略的全面性与可复现性、数据清洗与实体对齐的严谨度、网络拓扑统计量（中心度、模块化指数）的稳健性，以及定性[[Literature Review|文献综述]]与定量计量图谱之间的互证度。
> - **不声称回答的问题** 不能仅凭被引频次高低直接推断单篇文献的内在真理性或方法严谨性，也不能从共引关联直接确立两派学者之间存在直接的思想师承[[Causality|因果关系]]。

> [!method-stack] 方法层级
> - **研究设计** 描述性文献计量调查、共被引网络拓扑分析、知识图谱测绘、跨时期比较研究、时序引文动力学建模。
> - **数据收集** Web of Science 核心合集、Scopus、Dimensions、PubMed 等标准化引文数据库全记录导出，以及预印本与专利数据库采集。
> - **分析方法** 频次统计与增长率测算、布拉德福文献离散分析、共词分析（Co-word Analysis）、文献共被引分析（Co-citation Analysis）、引文关联分析（Bibliographic Coupling）、社区发现聚类算法（如 Louvain 算法、InfoMap），以及引文年龄分布测算（Citation Age Analysis）与知识热点四象限分析（Knowledge Hotspots）。
> - **辅助技术** 关键词同义词映射与停用词清洗、学者同名异义消歧算法、网络节点度与中介中心度计算、VOSviewer 与 CiteSpace 拓扑可视化。

---

> [!proc] 通用程序
> 1. **检索策略与样本界定** 构建布尔逻辑检索式，明确文献类型、发表时段、语言及学科分类边界，完整导出带引文信息的文献题录全记录。
> 2. **数据清洗与规范化** 去除重复记录，合并同义关键词与同名异义学者姓名，清洗参考文献缩写歧义，建立停用词表。
> 3. **基础计量特征统计** 测算发文时序增长趋势、发文国家与机构分布、核心期刊离散度，识别核心学者与高影响力文献。
> 4. **引文与共现网络建模** 提取文献共被引矩阵或关键词共现矩阵，设定节点连接与共引阈值，剔除孤立节点与微弱连接。
> 5. **聚类提取与拓扑分析** 应用网络社团结构探测算法划分知识子群，计算关键节点的中心度指标，识别桥接不同聚类的枢纽节点。
> 6. **质性研读与理论阐释** 调取各聚类中的高被引文献展开精读，结合学科制度史对量化图谱揭示的学派分化与演进机制进行实质阐述。

> [!method-stack] 数据与[[Variable|变量]]
> - **数据结构** 纵向时间序列文献题录数据、非对称引文有向网络、对称共引/共词无向加权网络。
> - **样本与单位** 经检索式筛选的全部目标成果记录；分析单位为单篇论著、学者、机构或关键词。
> - **变量或测量** 历年发文量、发文年均复合增长率、被引频次、相对引文影响因子、参考文献平均年龄 $\langle T \rangle$、年龄离散系数 $\sigma_T$、节点度中心度、中介中心度、模块度（Modularity $Q$ 值）。

---

> [!method-fit] 适用判断
> - **适合使用** 适合测绘特定跨学科领域或政策议题的知识全貌，评估两门相邻学科在知识生产规模与理论自足性上的结构差异，以及辨识特定理论在学术网络中的扩散轨迹。[[Argument_Steiner-Khamsi_2024_UNESCO|(Steiner-Khamsi, Faul, et al., 2024, pp. 29–32)]]
> - **谨慎使用** 文献量过小（少于 100 篇）的微观冷门领域网络连通性差，难以形成具有统计意义的稳健聚类，需结合手工滚雪球综述。
> - **不适合使用** 无法用于解答微观课堂实践中具体教学干预的有效性因果推断问题，亦不适合评估未被引文数据库收录的草根民间政策文本与非正式会议口述材料。

---

> [!method-limits] 方法局限
> - **偏误来源** 国际商业引文数据库存在明显的英语中心主义倾向与全球北方出版物偏好；学术引用行为包含赞同、借鉴、仪式性堆叠或批判反驳等多种动机，不能简单将引用等同于正面认可。
> - **发表前夭折团队的幸存者数据盲区** 文献计量分析立足于通过同行评审并正式发表的成果数据库，无法直接观测在手稿出版前因沟通破裂、协调成本过高而中途夭折的团队，导致对团队合作与多样性红利的评估存在前置幸存者偏差。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 117–118, 133)]]
> - **适用边界** 严重依赖成熟的引文索引网络，对著作出版物或引文稀疏的人文艺术领域解释力受限；存在新近成果被引偏低的时滞马太效应。
> - **误用风险** 将文献计量指标直接等同于个体的学术水平或聘任晋升标准，诱发功利性互引联盟或碎化成果灌水。
> - **补救方式** 结合定性系统文献综述进行交叉互证，采用学科与年代归一化算法（如相对引文百分位）校正发表时延偏误。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Network Analysis]] | 基础分析技术 | 复杂网络分析为共被引与共词网络提供中心度、凝聚子群及拓扑结构算法。 |
> | [[Systematic Review]] | 互补综述方法 | 系统综述提供透明严谨的文献检索与质量评价规程，为计量分析提供样本底库。 |
> | [[Survey Research]] | 经验补充方法 | [[Questionnaire\|问卷调查]]法可直接收集科研人员与实践者对领域前沿与[[Research Utilization\|证据使用]]的直接感知。 |
> | [[Disruption Index]] | 衍生测度指标 | 颠覆性指数在引文网络基础上测度成果开启新方向与巩固既有范式的拓扑倾向。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Steiner-Khamsi_2024_UNESCO|Steiner-Khamsi, Faul, et al. (2024, pp. 29–32)]] — 运用文献计量分析比对公共卫生与教育循证政策研究发文增长率，揭示教育证据社群自指与碎片化的结构特征。
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit01|Wang & Barabási (2021)]] — 测定科研生产力分布（Unit 01），反思流产团队幸存者盲区（Unit 05），解构引文差距与相对标准化（[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|Unit 07]]），并在 [[Argument_Wang_Barabasi_2021_Cambridge_Unit09|Unit 09]] 建立引文动力学模型与知识热点架构。
