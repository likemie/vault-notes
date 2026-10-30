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
method_related_count: 23
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
  - "[[Heterogeneity]]"
  - "[[Research Utilization]]"
  - "[[Predictive Validity]]"
related_theories: []
related_methods:
  - "[[Systematic Review]]"
  - "[[Network Analysis]]"
  - "[[Survey Research]]"
  - "[[Questionnaire]]"
related_instruments: []
related_persons:
  - "[[Derek de Solla Price]]"
related_facts: []
related_arguments:
  - "[[Argument_Steiner-Khamsi_2024_UNESCO]]"
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit01]]"
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit03]]"
confidence: medium
status: draft
created: 2026-10-22
updated: 2026-10-30
---

---

> [!def] Bibliometric Analysis
> [[Document|文献]]计量分析（Bibliometric Analysis）是运用数学与统计学方法对已发表学术文献的载体特征、学者合作网络、关键词共现频率以及引文网络展开量化建模的实证研究方法。该方法主要用于呈现特定学科领域的宏观演进趋势、核心研究前沿、学科分支结构以及学者共同体的引证关联格局。

> [!method-scope] 方法范围
> - **研究对象** 同行评审期刊刊载成果、学术专著、会议文献、专利报告、[[Systematic Review|系统综述]]与引文索引数据库记录。
> - **问题类型** 适合回答[[Scientific Productivity|学术生产力]]增长率测算、高影响力学者与文献识别、学科知识基础追踪、跨学科引用模式比较以及概念演化路径分析。
> - **[[Unit of Analysis|分析单位]]** 单篇文献、科研人员、研究机构、国家、出版期刊、学科领域或引文网络中的节点与聚类。
> - **输出形式** 历年发文量增长曲线、引文频次分布、高被引文献排行榜、共被引网络聚类图谱、关键词共现网络及主题演化流向图。

> [!citation-card] 科学图谱与文献计量的计算定位
> 文献计量分析旨在运用文本分析与引文分析计算技术，生成研究领域的全景图景。该方法是识别核心[[Research Problem|研究议题]]并利用计算途径呈现学术宏观图景的标准化[[Paradigm|范式]]。通过关键词分析识别核心主题演进，借助共被引分析生成学科领域全景并提取知识聚类。[[Argument_Steiner-Khamsi_2024_UNESCO|(Steiner-Khamsi, Faul, et al., 2024, p. 64)]]
>
> *Bibliometric analysis aims to generate a picture of a research [[Champ|field]] using both text analysis and citation analysis. It is a way of identifying core research topics and illustrating an academic landscape using a computational approach. Here, we used a keyword analysis to identify important themes in education and public health research and how those have changed over time. We also used a co-citation analysis to generate an overview of the field and to extract research clusters.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 视学术文献的引用关系与发表记录为[[Knowledge Production|知识生产]]、流动与合法化过程的物质化痕迹；认为文献之间的引证关联反映了概念亲缘性、学术认同与范式分化。
> - **研究者角色** 研究者在检索式设计、数据库选择、停用词清洗、共被引阈值设定及聚类算法挑选过程中扮演裁量角色，需要结合领域专长对计算图谱进行实质性质性解读。
> - **有效性标准** 遵循[[Literature Search|文献检索]]策略的全面性与可复现性、数据清洗与实体对齐的严谨度、网络拓扑统计量（中心度、模块化指数）的稳健性，以及定性[[Literature Review|文献综述]]与定量计量图谱之间的互证度。
> - **不声称回答的问题** 不能仅凭被引频次高低直接推断单篇文献的内在真理性或方法严谨性，也不能从共引关联直接确立两派学者之间存在直接的思想师承[[Causality|因果关系]]。

> [!method-stack] 数据、[[Variable|变量]]与模型
> - **数据来源** Web of Science 核心合集、Scopus、Dimensions、PubMed 等标准化引文数据库，以及跨学科预印本库。
> - **核心变量** 历年发文总量、发文年均复合增长率、篇均被引频次、相对引文影响因子、节点度中心度（Degree Centrality）、中介中心度（Betweenness Centrality）。
> - **分析模型** [[Derek de Solla Price|普赖斯]]文献增长模型、布拉德福文献离散定律、共词分析（Co-word Analysis）、文献共被引分析（Co-citation Analysis）、引文关联分析（Bibliographic Coupling）及社区发现聚类算法（如 Louvain 算法、InfoMap）。
> - **可视化技术** 知识图谱网络图、密度热力图、时间线叠加图谱，通过节点尺寸表征被引权重，通过连线粗细表征共现强度。

---

> [!proc] 量化分析程序
> 1. **检索策略与样本界定** 构建布尔逻辑检索式，明确文献类型、发表时段、语言及学科分类边界，完整导出带引文信息的文献题录全记录。
> 2. **数据清洗与规范化** 去除重复记录，合并同义关键词与同名异义学者姓名，清洗参考文献缩写歧义，建立停用词表。
> 3. **基础计量特征统计** 测算发文时序增长趋势、发文国家与机构分布、核心期刊离散度，识别核心学者与高影响力文献。
> 4. **引文与共现网络建模** 提取文献共被引矩阵或关键词共现矩阵，设定节点连接与共引阈值，剔除孤立节点与微弱连接。
> 5. **聚类提取与拓扑分析** 应用网络社团结构探测算法划分知识子群，计算关键节点的中心度指标，识别桥接不同聚类的枢纽节点。
> 6. **质性研读与理论阐释** 调取各聚类中的高被引文献展开精读，结合学科制度史对量化图谱揭示的学派分化与演进机制进行实质阐述。

---

> [!method-fit] 适用判断
> - **适合使用** 适合测绘特定跨学科领域或政策议题的知识全貌，评估两门相邻学科在知识生产规模与理论自足性上的结构差异，以及辨识特定理论在学术网络中的扩散轨迹。
> - **谨慎使用** 文献量过小（少于 100 篇）的微观冷门领域网络连通性差，难以形成具有统计意义的稳健聚类，需结合手工滚雪球综述。
> - **不适合使用** 无法用于解答微观课堂实践中具体教学干预的有效性因果推断问题，亦不适合评估未被引文数据库收录的草根民间政策文本与非正式会议口述材料。

---

> [!method-limits] 方法局限
> - **数据库收录偏误** 国际商业引文数据库存在明显的英语中心主义倾向与全球北方出版物偏好，可能系统性低估全球南方本土语言文献的生产力与知识贡献。
> - **引用动机[[Heterogeneity|异质性]]** 学术引用行为包含赞同、借鉴、仪式性堆叠、批判反驳或学术结盟等多种复杂动机，简单将引用等同于正面学术认可易产生误判。
> - **马太效应与时滞效应** 新近发表的高质量前沿成果由于积累时间短而处于被引低位，早期奠基文献容易因引证滚雪球效应形成垄断性高被引表象。
> - **补救方式** 结合定性系统文献综述进行交叉验证，采用标准化加权算法校正发表时延偏误，并在检索阶段补充区域性学术数据库。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Network Analysis]] | 基础分析技术 | 社会网络分析为共被引与共词网络提供中心度、凝聚子群及拓扑结构算法。 |
> | [[Systematic Review]] | 互补综述方法 | 系统综述提供透明严谨的文献检索与质量评价规程，为计量分析提供样本底库。 |
> | [[Survey Research]] | 经验补充方法 | [[Questionnaire\|问卷调查]]法可直接收集科研人员与实践者对领域前沿与[[Research Utilization\|证据使用]]的直接感知。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Steiner-Khamsi_2024_UNESCO|Steiner-Khamsi, Faul, et al. (2024, pp. 29–32)]] — 运用文献计量分析比对公共卫生与教育循证政策研究的发文增长率（30.5% vs 23.6%）与共被引网络，揭示教育证据研究社群高度自指与分散碎片的结构特征。
> - [[Argument_Wang_Barabasi_2021_Cambridge|Wang and Barabási (2021)]] — 基于大数据文献计量分析测定科研生产力稳态分布与 h 指数预测效度，并依托十年引文窗口与共现矩阵建模个体能力稳态与学术爆发期规律。
