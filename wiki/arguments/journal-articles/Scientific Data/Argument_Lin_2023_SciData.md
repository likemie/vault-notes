---
summary: "论证构建覆盖 1.34 亿篇文献的大规模开放科学学数据湖 SciSciNet，通过规范化清洗、成果家族聚合与多源记录链接贯通上游科研资助与下游专利及临床应用，并预计算颠覆性指数、非典型引文组合与引文动力学等核心指标，有效降低实证准入门槛并提升研究可复现性。"
type: argument
authors:
  - "Lin, Z."
  - "Yin, Y."
  - "Liu, L."
  - "Wang, D."
source_language: en
citation: "Lin, Z., Yin, Y., Liu, L., & Wang, D. (2023). SciSciNet: A large-scale open data lake for the science of science research. Scientific Data, 10, Article 315. https://doi.org/10.1038/s41597-023-02198-9"
year: 2023
doi: "https://doi.org/10.1038/s41597-023-02198-9"
citation_aliases:
  - "Lin et al., 2023"
  - "Lin et al. (2023)"
tags:
  - field/science-of-science
  - theme/data-infrastructure
  - theme/scientometrics
  - theme/open-science
  - theme/record-linkage
  - method/quantitative
related_concepts:
  - "[[Variable]]"
  - "[[Construct]]"
  - "[[Metascience]]"
  - "[[Data Infrastructure]]"
  - "[[Sleeping Beauty in Science]]"
  - "[[Combinatorial Novelty]]"
related_theories:
  - "[[WSB Model]]"
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Author Name Disambiguation]]"
  - "[[Disruption Index]]"
  - "[[Combinatorial Novelty Measurement]]"
  - "[[Record Linkage]]"
related_instruments: []
related_persons:
  - "[[Dashun Wang]]"
related_facts:
  - "[[Microsoft Academic Graph]]"
  - "[[SciSciNet]]"
related_arguments: []
sources:
  - "[[sources/Lin_2023_SciData/Lin_2023_SciData|Lin_2023_SciData]]"
status: active
subtype: journal-article
publication_type: journal-article
title: "Argument_Lin_2023_SciData"
argument_key: "Argument_Lin_2023_SciData"
argument_display_title: "SciSciNet: A large-scale open data lake for the science of science research"
argument_kind: "journal-article"
argument_related_count: 15
argument_related_level: 1
argument_related_stars: "⭐"
argument_related_color: "#dbeafe"
journal: Scientific Data
---

---

> [!question]
> 科学学（Science of Science）与[[Metascience|元科学]]的实证研究长期面临三重结构性瓶颈：
> 1. **数据源分散孤立与缺乏互联** 学术出版物、学者、机构、科研资助、发明专利、临床试验与公众媒体数据散落于数十个独立平台，缺乏跨域统一标识符，使得全景追踪科学向社会经济转化的研究严重受限。
> 2. **预处理决策隐蔽与规则不透明** 原始海量图谱中混杂着预印本多版本重复、撤稿、非学术产出以及统计畸变，各研究团队往往依靠私有脚本进行即兴清洗，清洗过程因缺乏公开规范而不可复现。
> 3. **前沿测度指标计算成本极其高昂** 颠覆性指数、引文网络重组新颖性、WSB 动力学参数等前沿指标涉及全库零模型置换与复杂非线性拟合，巨大的算力门槛导致学界产生严重的重复计算与准入壁垒。

> [!claim] 核心主张
> 构建大规模开放学术数据湖 [[SciSciNet]]，以规范化清洗与成果家族去重后的 134,129,188 篇核心主出版物为支柱，依托多源[[Record Linkage|记录链接]]打通上游公共资助与下游专利、临床及媒体应用网络，并全量预计算科学学经典前沿测度指标，能够显著降低实证准入门槛，消除共同体在数据预处理中的无谓重复损耗，为科学学研究提供兼具高复现性、高可靠性与高拓展性的公共实证[[Data Infrastructure|数据基础设施]]。

> [!concept-lens] 阅读透镜
> - **对象** 全球跨学科多源科研大数据，涵盖 134,129,188 篇学术出版物、4.14 亿条学者-机构关系、15.89 亿条引文对、上游资助与下游社会经济应用关联。
> - **张力** 商业封闭数据库（如 WoS、Scopus、Dimensions）高昂访问成本与黑箱清洗规则，与开源学术共同体对透明、可复现、低门槛公共数据基础设施迫切需求之间的张力。
> - **贡献** 开源发布包含 22 张规范化数据表（TSV 格式）的完整科学学数据湖，公布可复现的预处理与模糊记录匹配算法，并预计算颠覆性、新颖性、引文动力学等多维指标。

---

> [!contrast-table] 科学学主流数据源特性与开放度对比
> | 数据源类别 | 代表性数据库 | 收录核心特征 | API 支持 | 数据倾倒（Data Dump） | 核心局限与研究摩擦 |
> |:---|:---|:---|:---:|:---:|:---|
> | **文献与引文开放元数据** | Crossref, OpenCitations, CORE, Unpaywall | 聚焦带 DOI 出版物元数据、开放获取标签与开放引文网络 | ✓ | ✓ | 缺乏资助明细与细粒度指标计算，无跨机构实体消歧 |
> | **综合开放学术图谱** | [[Microsoft Academic Graph\|MAG]]（已退役）, OpenAlex, AMiner | 覆盖数亿篇文献、学者与机构消歧网络，支持学科自动分类 | ✓ | ✓ | 原始数据噪声大，预印本多版本导致引文虚高，缺乏指标预计算 |
> | **商业学术文献数据库** | Web of Science, Scopus, Dimensions | 专家审定源刊，提供严谨引文索引与部分资助对齐 | — | — | 订阅费用高昂，算法黑箱，严禁大规模全量数据再分发 |
> | **上游基金与政策数据库** | NIH RePORTER, NSF Awards, Overton | 收录公共研发项目拨款明细或政策引文 | ✓ | ✓ | 与外部学术发表缺乏直接结构化链接，多为非结构化文本 |
> | **下游应用与转化数据** | PatentsView, Marx & Fuegi, ClinicalTrials.gov | 覆盖专利文本、专利对科学引文与全球临床试验注册 | ✓ | ✓ | 独立运作，与基础科学论著存在跨域数据壁垒 |
> | **统一开放科学学数据湖** | [[SciSciNet]] | 整合核心论著、学者性别推断、基金资助、专利与全量预计算指标 | ✓ | ✓ | 以开源公共品形态降低实证门槛，保障跨研究完全可复现 |

---

> [!framework-table] 理论工具箱
> | 理论工具 | 解释功能 |
> |---|---|
> | **元科学知识网络理论**<br>[[Metascience]] | 将科学发展理解为由学者、出版物、资助机制与技术应用交织而成的演化网络，为跨源数据湖实体的关系抽取与指标设计提供本体论支撑。 |
> | **WSB 引文动力学模型**<br>[[WSB Model]] | 整合指数增长、优先连接、适应度与对数正态衰老四大机制，预测单篇文献终极被引量并提供跨学科通用动力学参数。 |

> [!warrant]- 理论如何支撑论证
> 元科学知识网络视角将科学成果的生命历程扩展至“输入资助—学术生产—知识网络扩散—社会经济转化”的完整链条，要求实证数据基础设施必须突破传统期刊引文数据库的单一封闭边界；借助 WSB 模型、颠覆性指数等经同行检验的经典量化机制，数据湖的指标预计算能够直接对接科学学核心理论命题，并在宏观尺度验证数据湖清洗质量与统计有效性。

---

### 核心变量与操作化编码表

> [!index-table] 核心变量操作化定义与编码规程
> | [[Variable\|变量]]维度与分类 | [[Construct\|理论构念]]与操作化定义 | 核心教学规程、典型测量工具与纳入案例 |
> |---|---|---|
> | **学术影响力与知识扩散**<br>（Citation Impact & Diffusion） | 衡量成果在科学共同体内部的累积传播广度与长期持久度。 | 5 年引文数（C5）、10 年引文数（C10）、总被引频次，以及基于 [[WSB Model\|WSB 模型]] 拟合的即时性参数 $\mu$、衰老参数 $\sigma$ 与终极影响力预测值 $c_\infty$。 |
> | **范式革新与知识组合特征**<br>（Disruption & Combinatorial Novelty） | 衡量成果开辟全新研究轨道或实现罕见跨学科知识融合的拓扑性质。 | [[Disruption Index\|颠覆性指数]] $D \in [-1, 1]$（Wu et al., 2019）；基于 [[Combinatorial Novelty Measurement\|期刊共引对非典型度分析]] 计算的中位数 Z 分数（常规性基底）与第 10 百分位数 Z 分数（尾部新颖性）（Uzzi et al., 2013）。 |
> | **长周期延迟认可**<br>（Delayed Recognition） | 衡量成果在经历长期休眠后爆发被引的非典型演化轨迹。 | [[Sleeping Beauty in Science\|睡美人现象]] 系数 $B$ 与唤醒时间 $T$（Ke et al., 2015），结合学科外施引比例刻画知识的跨领域延迟激活。 |
> | **多源跨界应用转化**<br>（Socioeconomic Linkage） | 衡量基础科学向上游公共资金与下游产业、医疗及公共舆论的渗透程度。 | 美国国家科学基金会（National Science Foundation, NSF）与美国国立卫生研究院（National Institutes of Health, NIH）资助项目关联；USPTO/EPO 专利引用；ClinicalTrials.gov 临床试验引用；Crossref 媒体与社交媒体提及。 |
>
> **图表解读** 本表系统界定了 SciSciNet 核心数据表覆盖的理论构念、操作化指标与计算规程，为宏观科学学计算实验提供统一基准。

---

> [!index-table] SciSciNet 核心数据表架构与记录规模总览
> | 表文件名 | 数据行数（Lines） | 数据类型与字段结构 | 核心分析功能与关联说明 |
> |:---|---:|:---|:---|
> | `SciSciNet_Papers` | 134,129,188 | `PaperID, DOI, DocType, Year, Date, JournalID, ConferenceSeriesID, Reference_Count, Citation_Count, C5, C10, Disruption, Atyp_Median_Z, Atyp_10pct_Z, Atyp_Pairs, WSB_mu, WSB_sigma, WSB_Cinf, SB_B, SB_T, Team_Size, Institution_Count, Patent_Count, Newsfeed_Count, Tweet_Count, NCT_Count, NIH_Count, NSF_Count` | 数据湖核心主出版物总表，存储主键、基础元数据与全量预计算指标 |
> | `SciSciNet_PaperAuthorAffiliations` | 413,869,501 | `PaperID, AuthorID, AffiliationID, AuthorSequenceNumber` | 成果-学者-机构关联表，记录署名顺序 |
> | `SciSciNet_PaperReferences` | 1,588,739,703 | `Citing_PaperID, Cited_PaperID` | 核心主出版物集内部引文对网络 |
> | `SciSciNet_Authors_Gender` | 134,197,162 | `AuthorID, Author_Name, H-index, Productivity, Average_C10, Average_LogC10, Inference_Sources, Inference_Counts, P(gf)` | 学者档案总表，整合科研产出、影响力指标与性别推断概率 |
> | `SciSciNet_Affiliations` | 26,998 | `AffiliationID, Affiliation_Name, GridID, Official_Page, ISO3166Code, Latitude, Longitude, H-index, Productivity, Average_C10, Average_LogC10` | 科研机构表，整合地理坐标、GRID ID 与机构层级产出与影响力 |
> | `SciSciNet_Fields` | 311 | `FieldID, Field_Name, Field_Type` | 学科分类字典，含 19 个一级顶级学科（Top）与 292 个二级子领域（Sub） |
> | `SciSciNet_PaperFields` | 277,494,994 | `PaperID, FieldID` | 论著与学科分类多对多映射表 |
> | `SciSciNet_Journals` | 49,066 | `JournalID, Journal_Name, ISSN, Publisher, Webpage` | 期刊字典表，记录标准刊名、ISSN 与出版商信息 |
> | `SciSciNet_ConferenceSeries` | 4,551 | `ConferenceSeriesID, Abbr_Name, ConferenceSeries_Name` | 学术会议系列字典表 |
> | `SciSciNet_PaperDetails` | 136,726,948 | `PaperID, DOI, DocType, PaperTitle, BookTitle, Year, Date, Publisher, JournalID, ConferenceSeriesID, OriginalVenue, Volume, Issue, FirstPage, LastPage` | 成果详细信息表，保留家族附属版本与撤稿成果的篇名及卷期页码 |
> | `SciSciNet_Link_NSF` | 1,309,518 | `PaperID, NSF_Award_Number, Type, Diff_ZScore` | 论著与 NSF 资助对齐表（区分 Exact 与 Fuzzy 匹配类型） |
> | `SciSciNet_Link_NIH` | 6,013,187 | `PaperID, NIH_Project_Number` | 论著与 NIH 资助项目对齐表 |
> | `SciSciNet_Link_Patents` | 38,740,313 | `PaperID, PatentID, Type` | 论著与专利引文关联表（Type=1 为 USPTO，0 为 EPO） |
> | `SciSciNet_Link_ClinicalTrials` | 438,220 | `PaperID, NCT_Number` | 论著与 ClinicalTrials.gov 临床试验引用关联表 |
> | `SciSciNet_Link_Twitter` | 55,846,550 | `PaperID, TweetID` | 论著与推特社交媒体讨论对齐表 |
> | `SciSciNet_Link_Newsfeed` | 595,241 | `PaperID, NewsfeedID` | 论著与全球主流媒体新闻报道提及对齐表 |
> | `SciSciNet_Link_NobelLaureates` | 87,316 | `PaperID, LaureateID, Type` | 诺贝尔奖得主学术生涯产出表（Type=1 为获奖代表作，0 为其他论著） |
> | `SciSciNet_NSF_Metadata` | 489,446 | `NSF_Award_Number, Title, Publication_Research, Date` | NSF 资助项目元数据原始表（从 NSF.gov 爬取并解析） |
> | `SciSciNet_Twitter_Metadata` | 59,593,281 | `TweetID, Occurred_Time, ObjectID, Subject_Infomation` | 推特提及事件原始元数据 |
> | `SciSciNet_Newsfeed_Metadata` | 947,160 | `NewsfeedID, Occurred_Time, ObjectID, Subject_Infomation` | 新闻报道提及事件原始元数据 |

---

> [!method-panel] 研究设计
> | 模块 | 材料与处理方式 |
> |---|---|
> | **原始图谱过滤与家族整合**<br>[[Bibliometric Analysis]] | 以微软学术图谱（Microsoft Academic Graph, MAG）2021 年 12 月 6 日终版（2.7 亿条记录）为底库，剔除专利与无 DOI/类别记录，按预印本-正式出版等成果家族聚合主论著，重算 134,129,188 篇文献的引文分布。 |
> | **跨源多模态记录链接**<br>[[Record Linkage]] | 采用多级对齐方案：DOI 精确对齐、题名标准化精确对齐、基于 Elasticsearch 的置换零模型检索与双 Z 分数差异模糊匹配，辅以发表年份时间窗约束（$t-1 \le t_{\text{pub}} \le t+5$）与 Crossref 基金数据补充。 |
> | **指标规模化工程计算**<br>High-throughput Metric Computation | 依托分布式计算管道全量解算近 5000 万篇论著的颠覆性得分、共引非典型性 Z 分数、睡美人指数与 WSB 动力学拟合参数。 |
> | **双盲交叉实证检验**<br>Benchmark Cross-Validation | 以商业数据库 Dimensions 为外部基准，从文献重合率、引文相关性、资助匹配度等维度建立混淆矩阵与相关分析，检验数据完整性与可靠性。 |

> [!sample-panel]- 样本与材料快照
> | 样本层面 | 构成 |
> |---|---|
> | **核心出版物样本** | 134,129,188 篇独立主论著（期刊论著 90,764,813 篇，学术专著 4,629,342 部，图书章节 3,932,366 篇，会议录成果 5,123,597 篇，学位成果 5,998,509 篇，其他带 DOI 成果 20,451,018 篇）。 |
> | **实体关系网络** | 413,869,501 条学者-机构-论著关系；1,588,739,703 条论著间引文对；134,197,162 名学者（附带性别推断指标）；311 个学科领域（19 个顶级领域与 292 个子领域）。 |
> | **外部应用链接样本** | 1,309,518 条 NSF 资助关联；6,013,187 条 NIH 资助关联；38,740,313 条专利引文关联；438,220 条临床试验引用；56,441,791 条新闻与推特社交提及。 |

---

> [!logic-map]- 核心论证逻辑链
> ```mermaid
> flowchart LR
>     A["科学学实证研究面临的三重瓶颈"] --> B["数据湖本体设计与核心表库构建"]
>     B --> C["步骤一：合并多重版本并重算引文网络"]
>     C --> D["步骤二：多层文本匹配串联经费与转化"]
>     C --> E["步骤三：亿级数据测算复现经典科学学定律"]
>     D --> F["步骤四：对标 Dimensions 商业库交叉核验"]
>     E --> G["步骤四：验证预计算指标高度可靠"]
>     F --> H["确立开放低门槛高可靠实证数据基础设施"]
>     G --> H
> ```

---

> [!claim|step] 论证步骤一　合并成果多重版本并重算引文才能还原真实学术网络
> 原始学术大数据中同一项研究常常以工作手稿、预印本、会议报告与期刊发表等多种形态分散存在，既导致文献总量虚标，又导致引用计数被分割或重复计算。必须先将同属一项研究的多重版本聚拢为唯一定位的主出版物，再在统一边界内重算所有引文连接，才能消除虚假引文膨胀并奠定高保真的分析基准。

> [!sub-claim] 1. 聚合预印本与正式发表等多重版本能消除文献重复计算
> 微软学术图谱（MAG）终版包含 2.7 亿条记录，但混杂了大量未授权专利、缺少核心属性标签的无效记录，以及同一科研产出跨形态流转形成的“成果家族”。若直接以原始行作为分析单元，会把同一项研究重复计为多篇成果。为此实施两步清理：第一步剔除所有专利类型及无 DOI 的未分类行；第二步依据成果家族标识，将从预印本、工作手稿到最终正式发表的所有关联条目归并为唯一的主出版物，并将撤稿记录与附属版本剥离至明细附表。这一聚合规程将数据规模从 2.7 亿条去重精炼为 134,129,188 篇独立主出版物，彻底清除了体量虚胖与版本割裂。

> [!sub-claim] 2. 在核心文献集内重算引文能纠正版本合并带来的虚假引用
> 聚拢主出版物后必然引发引用网络的拓扑失真。若沿用旧库的引文计数，会出现引用相加导致的虚高，或大量引用指向已被吸纳的次级版本。为此必须在 1.34 亿篇核心出版物范围内对所有施引与被引关系执行严格的逐条重查，剔除同家族成果之间的内部自引与重复连线，重新构建出严格定位于核心集内部的 1,588,739,703 条真实引文对。重算前后的斯皮尔曼等级相关系数在被引频次上达到 0.991，在参考文献数上达到 0.994，既忠实保留了真实的学术引用格局，又纠正了因版本合并导致的虚高失真。

> [!figure]- 图 1：SciSciNet 实体关系图
> ![](https://img.mylikemie.icu/sources/Lin_2023_SciData/figures/Lin_2023_SciData_Fig1_Entity_Relationship_Diagram.jpg)
> *以 `SciSciNet_Papers` 主表为核心枢纽，通过 `PaperID` 贯通学者、机构、学科、会议、引文对与上下游应用链接的多维星型实体关系图。*

> [!figure]- 图 3：SciSciNet 科学出版物汇总统计分布
> ![](https://img.mylikemie.icu/sources/Lin_2023_SciData/figures/Lin_2023_SciData_Fig3_Summary_Statistics_Publications.jpg)
> *(a) 19 个一级学科出版物规模分布，(b) 1900 年至 2020 年出版物总量的指数扩张曲线，(c) 各学科合著团队平均规模随年代的稳步增长趋势。*

---

> [!claim|step] 论证步骤二　分层文本匹配能跨越数据库边界串联科研经费与技术转化
> 追踪公共研发投入如何催生科学突破、再如何向专利发明与临床医疗扩散，是揭示创新规律的关键。面对不同管理机构之间缺乏统一编码的壁垒，开发由精确碰撞到模糊搜索的分层记录匹配算法，能有效攻克非结构化文本的噪声干扰，打通贯通上游投入与下游转化的实证网络。

> [!sub-claim] 1. 结合题名模糊检索与年份约束能精准锁定基金支持的文献
> 美国国家科学基金会（NSF）自 1959 年以来的 489,446 项资助涉及 135 万篇科研产出的纯文本报告，缺少标准的数字对象标识符（DOI）。针对这一非结构化文本瓶颈，研发了四阶段匹配规程：
> 1. **DOI 精确匹配** 直接提取文本中的标准 DOI 进行跨库碰撞，去重后确定 350,611 条高置信度记录（占比 26.0%）。
> 2. **题名规整精确匹配** 对其余文本中的论著题名实施小写转换并剔除标点与异常空格，精确对齐 246,701 条记录（占比 18.3%）。
> 3. **Elasticsearch 零模型评分与启发式模糊匹配** 将全部主论著建立倒排索引，输入 NSF 文本提取排名前两位的候选文献。以第二候选得分分布作为零模型基准，若第一候选得分显著超越次优分布的右侧阈值（$P = 0.05$）则判定为精准匹配，保守锁定 467,159 条记录（占比 34.6%）；对剩余部分计算成对 Z 分数差值，将得分显著占优的 178,877 条记录归入启发式模糊匹配集。
> 4. **Crossref 基金外部数据互证** 抽取 Crossref 基金库记录通过 DOI 补齐 305,314 条资助关系。
> 
> 整个流水线共汇总出 1,309,518 条 NSF 资助链接，将 148,148 项 NSF 基金课题与 929,258 篇学术成果严密锚定。

> [!sub-claim] 2. 统一文献标识能完整追踪科研成果向专利、临床与媒体的转化扩散
> 依托统一的主文献标识，实现了多领域下游应用数据的端到端贯通：
> - **医药基金穿透** 借助经清洗的 PubMed 唯一标识符（PMID）桥梁，将美国国立卫生研究院（NIH）40 年间的 37.9 万项立项课题与 263.6 万篇医学成果精确对接（生成 6,013,187 条资助关系，原始匹配率超 98.9%）。
> - **产业技术外溢** 整合 Marx & Fuegi 专利引用库，将附属版本的专利引用全部归并至主出版物，获取美欧专利局的 38,740,313 条专利引用记录。
> - **临床医疗与公众讨论** 串接 ClinicalTrials.gov 的 438,220 条临床试验引用，并通过 Crossref Event API 接入 5584 万条推特讨论与 59.5 万条新闻报道提及，完整还原了基础研究向产业技术与社会公众扩散的客观足迹。

> [!case] 跨源关联个案追踪：遗传性痉挛性截瘫论著的资助与产出全景穿透
> 以焦点论著《遗传性痉挛性截瘫基因定位研究》（Primary PaperID: `246319838`）为例：
> - 在 `SciSciNet_Papers` 与 `SciSciNet_PaperDetails` 中可直接检索到该论著的标准题名、发表刊物、卷期页码及其累计收获的被引频次。
> - 在 `SciSciNet_Link_NIH` 表中，该 `PaperID` 精确对齐至 3 项核心 NIH 资助项目编号：`R01NS033645`、`R01NS036177` 与 `R01NS038713`。
> - 研究者可无缝跳转至 NIH RePORTER 官方系统，调取这三项资助课题的项目全称、主要研究者（PI）资历、历年拨付金额与所属学术机构，完整穿透“公共财政拨款—实验室研究产出—学术网络扩散”的全生命周期。

> [!figure]- 图 2：NSF 资助参考引文字符串与 MAG 记录匹配流程
> ![](https://img.mylikemie.icu/sources/Lin_2023_SciData/figures/Lin_2023_SciData_Fig2_Matching_NSF_Reference_Strings.jpg)
> *(a) Elasticsearch 检索中第一候选与第二候选得分的 Z 分数分布，红虚线标出第二候选右尾截断点（$P = 0.05$）；(b) 得分未越过截断点但两候选得分差异显著的成对 Z 分数差值分布。*

> [!figure]- 图 4：科学出版物与社会经济制度机构关联分布
> ![](https://img.mylikemie.icu/sources/Lin_2023_SciData/figures/Lin_2023_SciData_Fig4_Linking_Publications_Socioeconomic_Institutions.jpg)
> *(a) 推特提及分布，(b) 新闻提及分布，(c) NIH 资助项目分布，(d) 专利引用分布，(e) 临床试验引用分布，(f) NSF 资助项目分布。*

---

> [!claim|step] 论证步骤三　在亿级文献上复现经典规律证明了指标预计算的可靠性
> 衡量学术数据基础设施实用价值的核心标准在于能否直接赋能定量研究。颠覆性指数、引文网络重组新颖性与引文动力学拟合等指标涉及海量置换零模型与非线性迭代，普通研究者难以承担全库解算的巨大算力。预先解算核心指标并在数千万篇文献规模上高保真再现学术界公认的经典实证规律，既免除了学界的重复劳动，又在宏观尺度验证了指标算法的准确性与稳健性。

> [!sub-claim] 1. 全库测算颠覆性指数确证了小团队更容易开辟新方向
> 对库内 48,581,274 篇具有完整引证关系的出版物全量解算了颠覆性指数（$D = \frac{n_i - n_j}{n_i + n_j + n_k}$）。复现分析显示：
> - 随着成果合著团队规模从单人递增至数十人，成果的颠覆性百分位呈现严格的单调持续下降，而平均被引量则同步攀升。
> - 跻身全库前 5% 高颠覆性的成果绝大多数由微型团队产出，而大团队成果跻身前 5% 高引序列的概率随团队扩张显著增加。
> - 该模式在近 5000 万篇文献的超大样本上确证了 Wu et al. (2019) 提出的“小团队开拓颠覆、大团队巩固发展”的组织分工规律。

> [!sub-claim] 2. 全量测算引文共现指标确证了常规与新颖结合最容易产生高引突破
> 针对 44,143,650 篇期刊出版物全量计算了基于引文置换零模型的期刊共引对 $z$ 分数，提取常规性中位数与第 10 百分位数新颖性：
> - 针对 1950 年至 2000 年间论著的四象限分析证实：同时兼具高常规性与高尾部新颖性的成果，跻身同期同领域前 5% 高被引顶尖成果的概率高达 7.32%，显著超越随机基线（5%）。
> - 低常规且低新颖成果的顶尖命中率仅为 3.55%，低常规高新颖成果与高常规低新颖成果的命中率分别为 6.48% 与 4.18%。
> - 这在大规模全学科样本中精准再现了 Uzzi et al. (2013) 提出的“立足成熟常规基底与注入非典型跨界新颖”的双重平衡法则。

> [!sub-claim] 3. 动力学拟合与休眠指标确证了引文衰老规律与跨学科唤醒机制
> 深入微观与长周期维度测算经典动力学指标：
> - **WSB 动力学拟合** 选取 1960 年代发表且 30 年内被引超 30 次的 36,802 篇物理学论著，利用 [[WSB Model|WSB 最小引文模型]] 拟合参数 $\mu$、$\sigma$ 与 $\lambda$。将真实引文轨迹依据拟合参数无量纲重标度后，所有文献的年度引文曲线完美坍缩至标准正态累积分布主曲线上；基于 15 年训练期对外推预测，10 年内与 20 年内的平均绝对百分比误差（MAPE）分别严格低于 0.10 与 0.15。
> - **睡美人现象普查** 针对 52,699,363 篇论著计算[[Sleeping Beauty in Science|睡美人现象]]系数 $B$ 与唤醒时间 $T$。极大似然拟合表明 $B$ 值的生存函数高度服从幂律分布（幂律指数 $\alpha = 2.40$，$B_m = 23.59$）；学科交叉引用分析证实，高 $B$ 值的长周期休眠成果在唤醒阶段显著依赖于跨学科外部引用的注入，呼应了 Ke et al. (2015) 的实证结论。

> [!figure]- 图 5：SciSciNet 常用测度指标宏观分布
> ![](https://img.mylikemie.icu/sources/Lin_2023_SciData/figures/Lin_2023_SciData_Fig5_Commonly_Used_Metrics.jpg)
> *(a) 4858 万篇文献颠覆性指数分布，(b) 4414 万篇期刊论著常规性与新颖性 Z 分数累积分布，(c) 学者平均 10 年被引对数分布与对数正态拟合，(d) 5270 万篇文献睡美人系数幂律分布，(e) 物理学长周期论著依据 WSB 模型实现的引文动力学主曲线重标度坍缩。*

> [!figure]- 图 7：科学学经典实证规律复现验证
> ![](https://img.mylikemie.icu/sources/Lin_2023_SciData/figures/Lin_2023_SciData_Fig7_Validation_Measurements_Literature.jpg)
> *(a) 团队规模与颠覆性百分位负相关及被引量正相关，(b) 顶尖 5% 颠覆性成果与顶尖 5% 高被引成果随团队规模的发生概率分化，(c) 睡美人文献系数与其跨学科外部引用比例的正相关，(d) 常规性与新颖性四象限划分下的顶尖高被引命中率对比。*

---

> [!claim|step] 论证步骤四　对标主流商业数据库证实开源数据湖的收录与匹配高度可靠
> 学术界长期对开源学术数据的质量与完整性存有疑虑，担忧其落后于成熟的专有商业引文索引。将 SciSciNet 的文献体量、引文计数与基金匹配表现同业界顶尖的商业数据库 Dimensions 开展客观的双盲交叉对比，能够以确凿的统计一致性消除学界的质量担忧，证明开源公共产品同样能够具备第一流的学术信度。

> [!sub-claim] 1. 篇级引文高度吻合证实文献收录质量达到商业数据库水准
> 将 SciSciNet 核心文献集与顶尖商业学术数据库 Dimensions（收录 106,517,016 篇带 DOI 论著）进行 DOI 级精确对齐，结果显示 SciSciNet 收录 98,795,857 篇带 DOI 文献，二者共享多达 84,936,278 篇共同文献，占 Dimensions 总量的 79.74% 与 SciSciNet 的 85.97%；在共同匹配的 8490 万篇文献中，SciSciNet 篇均记录 16.75 次被引，略高于 Dimensions 的 14.64 次，两者篇级被引计数斯皮尔曼相关系数达到 0.946，一致性系数（Lin's concordance coefficient）高达 0.940，证明其文献覆盖广度与引文完整度处于业界第一梯队。

> [!sub-claim] 2. 基金成果关联高度重合并补充了商业数据库遗漏的长尾项目
> 在 2000 年至 2020 年窗口内，比对两数据库在 NSF 与 NIH 项目-成果对上的收录情况。混淆矩阵核验表明：
> - **NIH 资助** Dimensions 收录 5,620,771 对资助-成果关联，SciSciNet 收录 5,371,809 对，两库共有对达 5,356,652 对。Dimensions 中 95.3% 的记录以及 SciSciNet 中 99.7% 的记录完全吻合，项目级关联成果数的斯皮尔曼相关系数高达 0.973。
> - **NSF 资助** 面临模糊文本解析瓶颈，Dimensions 收录 670,770 对关联，SciSciNet 收录 632,568 对，两库共有 529,382 对（分别占 Dimensions 的 78.9% 与 SciSciNet 的 83.7%），项目级篇数斯皮尔曼相关系数达 0.714。SciSciNet 独立挖掘出商业库未收录的 103,186 对有效资助对，展现出更强的长尾与非结构化挖掘能力。

> [!contrast-table] NSF 与 NIH 项目-成果关联混淆矩阵对比（2000–2020）
> | 资助机构与匹配状态 | 在 SciSciNet 中收录（In SciSciNet） | 未在 SciSciNet 中收录（Not in SciSciNet） | 合计（Dimensions 总量） |
> |:---|---:|---:|---:|
> | **NSF 资助：收录于 Dimensions** | 529,382 对（两库共有匹配） | 141,388 对（商业库独有） | 670,770 对 |
> | **NSF 资助：未收录于 Dimensions** | 103,186 对（SciSciNet 开源独有） | — | 103,186 对 |
> | **NIH 资助：收录于 Dimensions** | 5,356,652 对（两库共有匹配） | 264,119 对（商业库独有） | 5,620,771 对 |
> | **NIH 资助：未收录于 Dimensions** | 15,157 对（SciSciNet 开源独有） | — | 15,157 对 |

> [!figure]- 图 6：SciSciNet 与 Dimensions 数据库关联交叉验证
> ![](https://img.mylikemie.icu/sources/Lin_2023_SciData/figures/Lin_2023_SciData_Fig6_Validation_Data_Linkages_Dimensions.jpg)
> *(a) Dimensions 与 SciSciNet 匹配至每项 NIH 资助的项目篇数分布，(b) 每项 NSF 资助的项目篇数分布，(c) 对应 NIH 项目篇数的散点相关图（$r = 0.973$），(d) 对应 NSF 项目篇数的散点相关图（$r = 0.714$）。*

---

> [!finding-cards] 核心发现
> 1. **核心学术版图清洗提炼** 经过规范化过滤与家族聚合，从 MAG 2.7 亿条原始记录中提炼出包含 134,129,188 篇主论著与 15.89 亿条真实引文对的高纯度学术网络，彻底消除预印本与多版本引起的虚假引文膨胀。
> 2. **上游资助与下游应用贯通** 借助多源模糊记录链接，成功匹配 131 万条 NSF 资助关联、601 万条 NIH 资助关联、3874 万条专利引用与 43.8 万条临床试验链接，确立了基础科学向社会经济转化的立体数据网络。
> 3. **核心测度指标规模化预解算** 完成近 5000 万篇文献的颠覆性得分、非典型性 Z 分数、WSB 动力学参数与睡美人系数解算，高保真复现了小团队颠覆性优势、常规与新颖组合红利及引文普适坍缩等里程碑科学学规律。
> 4. **对标商业基准的高保真品质** 与 Dimensions 商业数据库的比对证实，两者在 8490 万篇共同文献上的引文斯皮尔曼相关系数达 0.946，NIH 资助关联重合率达 95.3% 以上，确立了开源数据湖不逊于专有商业库的基准可信度。

> [!stat-cards]- 核心数据
> - **134,129,188 篇** SciSciNet 核心主出版物数量（包含 9076 万篇期刊论著与 463 万部图书）。
> - **1,588,739,703 条** 核心文献集内部引文关系对。
> - **48,581,274 篇** 全量解算颠覆性指数（Disruption score）的文献规模。
> - **44,143,650 篇** 全量解算期刊共引非典型性（Atypicality Z-scores）的期刊论著规模。
> - **0.946** SciSciNet 与 Dimensions 在 8490 万篇共有文献上的篇级引文斯皮尔曼相关系数。
> - **7.32%** 高常规性与高尾部新颖性兼备成果跻身前 5% 高被引顶尖行列的命中率（对照双低组 3.55%）。

---

> [!citation-card] 开放科研数据湖的核心使能价值
> 科学学界将科学方法应用于科学自身，帮助人们以量化方式理解科学进步的核心机制。然而，随着数据集体量日益膨胀，追踪分散来源与跨数据源关联变得极其艰难。构建跨领域开放数据湖不仅能降低新进入者的科研壁垒、减少共同体在数据预处理与基础测量上的重复损耗，更能显著提升实证论断的稳健性与可复现性，进而拓宽学术界新思想的多元性与代表性。
>
> *Overall, this data lake serves as an initial but useful resource for the field, by lowering the barrier to entry, reducing duplication of efforts in data processing and measurements, improving the robustness and replicability of empirical claims, and broadening the diversity and representation of ideas in the field.*

> [!citation-card] 成果家族聚合与引文重新配赋准则
> 数据库中每项科学出版物可能以不同实体形式呈现（例如预印本与会议成果），在微软学术图谱中表现为成果家族。为避免重复计算，所有归属于同一家族的成果均被聚合为单一主论著。撤稿成果与家族附属成果被分流记录至明细表。为维持统计口径严格一致，引文与参考文献计数在 1.34 亿篇核心主论著子集中重新计算，确保每项施引与被引关系均可在此选定子集中溯源。
>
> *Each scientific publication in the database may be represented by different entities (e.g., preprint and conference), indicated as a paper 'family' in MAG. To avoid duplication, we aggregate all papers in the same family into one primary paper... For consistency, we recalculate the citation and reference counts within the subset of 134 M primary papers, such that each citation or reference record is also included in this subset and can be found in 'SciSciNet_PaperReferences'.*

---

> [!warning] 自述局限
> 资助-成果链接当前主要聚焦于美国的 NSF 与 NIH 项目，未完全覆盖其他国家资助体系；专利引用主要局限于 USPTO 与 EPO 专利数据库；临床试验引用主要来自 ClinicalTrials.gov，存在国家间入组与注册申报的地理异质性；基于学者姓名的性别推断模型具有内在算法局限与统计误差，在细分领域分析时须审慎校准；数据湖当前指标集聚焦于经典测度，尚待共同体进一步拓展更丰富的分析维度。

---

## 来源

- [[sources/Lin_2023_SciData/Lin_2023_SciData|Lin_2023_SciData]]
