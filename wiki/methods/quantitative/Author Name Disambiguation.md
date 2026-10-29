---
title: Author Name Disambiguation
aliases:
  - 著者姓名消歧
  - 姓名消歧
  - 作者消歧
  - 学者身份消歧
  - Name Disambiguation
  - Author Disambiguation
summary: "文献计量学、科学学与计算社会科学领域的基础计算与数据清洗方法；旨在从海量学术文献索引中准确识别特定学者所撰写的全部论著并区分同名异人与同人异名现象，系统化解拼写异体与更名、同名同姓重合、出版元数据缺失以及超大规模多机构多学者合著等四大核心数据识别瓶颈。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 12
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/data-cleaning
  - theme/scientometrics
  - theme/computational-social-science
related_concepts:
  - "[[Document]]"
  - "[[Unit of Analysis]]"
  - "[[Scientific Productivity]]"
  - "[[Epistemology]]"
  - "[[Paradigm]]"
  - "[[Big Science]]"
  - "[[Research Topic]]"
related_theories: []
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[h-Index]]"
  - "[[g-Index]]"
  - "[[o-Index]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit01]]"
confidence: high
status: draft
created: "2026-10-29"
updated: 2026-10-29
---

---

> [!def] Author Name Disambiguation
> **著者姓名消歧（Author Name Disambiguation）** 是[[Bibliometric Analysis|文献计量学]]、科学计量学与学术知识图谱构建中的基础数据工程与计算方法。其核心任务是**将海量学术[[Document|文献]]中的署名文本精准映射至真实世界的唯一物理学者实体**，同时化解“同人异名”（同一学者以不同拼写、变体或改名发表）与“同名异人”（多个独立学者共享完全相同的文字署名）的双向混淆难题，为微观个体科研轨迹追踪与宏观科学学生产力计量提供高保真的底层数据基座。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 16)]]

> [!method-scope] 方法范围
> - **研究对象** 学术文献数据库中的署名字符串、机构归属文本、学科分类标签、引用关系图谱以及学者数字标识档案（如 ORCID、Scopus ID、ResearcherID）。
> - **问题类型** 数据清洗、无监督聚类、图结构实体匹配与自然语言记录链接（Record Linkage）。
> - **[[Unit of Analysis|分析单位]]** 单篇文献中的署名节点、跨文献的学者个体发表档案。
> - **输出形式** 经去重与聚类后的标准化学者标识符及其完整归属的论著产出序列集合。

> [!citation-card] 著者消歧是追踪科学生产力的先决条件
> 准确追踪个体[[Scientific Productivity|科研生产力]]的能力，高度依赖于能否精准识别撰写某篇成果的具体学者以及归属于该学者的所有其他学术工作。这项表面简易的任务在科学计量学中属于重大的未决难题，受到同人异名、同名同姓、元数据缺失以及超多机构交叉合著等四大瓶颈的制约。高产资深学者因拥有长周期的发表记录往往较易消歧，而产出极少的新兴学者则面临更严重的不确定性。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 16)]]
>
> *Our ability to accurately track individual productivity relies on our skill to identify the individual(s) who wrote a paper and all other work that belongs to that individual. This seemingly simple task represents a major unsolved problem, limited by four challenges... In general, it is easier to disambiguate productive scientists, who have a long track record of papers, compared with those who have authored only a few publications.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 科学学中的“学者个体”属于通过出版元数据与引文拓扑网络推断重构而成的计算实体。
> - **研究者角色** 在算法工程中平衡精准率（Precision，避免将异人误合）与召回率（Recall，避免将同一人的多产轨迹碎片化分割）的参数权衡。
> - **有效性标准** 基于权威黄金标准标注集（Gold Standard Datasets）的宏观 F1 值、成对聚类纯度与引文网络拓扑一致性。
> - **不声称回答的问题** 姓名消歧算法仅负责成果与学者实体的客观物理归属，不能直接判断署名背后的实质学术贡献权重或合著搭便车行为。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis]]（文献计量分析）、计算社会科学数据预处理。
> - **核心算法[[Paradigm|范式]]** 基于规则与启发式过滤（同机构与同合作网络匹配）、基于文本特征的无监督图聚类算法、基于大语言模型与深度图神经网络的实体消歧表征学习。
> - **下游应用工具** [[h-Index]]、[[g-Index]] 与 [[o-Index]] 的精确求解；学术职业生涯流动性与微观团队演化追踪。

---

> [!feature] 著者姓名消歧的四大系统性挑战
> - **同人异名与拼写变异（Spelling & Orthographic Variants）** 单一学者在出版记录中常呈现多重变体，涵盖中英文拼写差异、缩写习惯（如 J. Smith 与 John Smith）、婚姻变动更名、宗教更名、性别重置以及笔名发表。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 16)]]
> - **同名同姓的实体碰撞（Common Name Conflicts）** 常见姓名被巨量独立物理学者共享，特别在东亚姓名（如 Wei Wang、Li Zhang）或英美高频姓氏中，导致简单字符匹配必然产生极端聚类膨胀。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 16)]]
> - **出版元数据严重缺失（Incomplete Metadata）** 早期期刊出版物与传统引文数据库常未记录学者的全名、二级所属院系机构、地理区位或电子邮箱，剥夺了传统消歧算法依赖的核心辅助特征。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 16)]]
> - **超多署名与跨学科[[Big Science|大科学]]协作（Hyperauthorship & Interdisciplinary Collaborations）** 现代科研日益呈现数百乃至数千名学者联合署名的大团队特征，多学科与多机构的深度交织使得成功消歧其中部分署名人员无法自然延伸推断其余合作研究人员的真实身份。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 16)]]

---

> [!proc] 通用消歧计算程序
> 1. **元数据标准化与字符阻断（Blocking）** 提取全部论著中的署名拼写、合作研究网络、期刊学科门类与年代信息；按照标准化姓氏结合首字母实施分块阻断，缩减两两比对的计算规模。
> 2. **多维特征工程构建** 计算两篇待比对论著在共有合作学者重叠度、共同参考文献引证链、所属机构地理语义相似度以及[[Research Topic|研究主题]]词向量余弦距离等多维特征向量。
> 3. **图模型聚类与链接预测** 将文献署名实例构建为加权网络图，以综合相似度作为连边权重，运用层次聚类、马尔可夫聚类或社区发现算法划分学者实体簇。
> 4. **外部权威实体知识图谱锚定** 对接 ORCID 注册数据库、维基数据（Wikidata）与科研基金资助项目历史记录，对边缘不确定簇进行半监督纠偏与实体合并。
> 5. **消歧效度审计与敏感性检验** 抽样核验高产顶尖学者与低产边缘学者的纯度指标，评估残差消歧错误对下游生产力指数拟合的影响幅度。

---

> [!method-fit] 适用判断
> - **适合使用** 构建国家级科研管理数据库、全球大学科研产出全量引文网络清洗、诺贝尔奖与战略科学家完整学术履历复原。
> - **不适合使用** 仅包含极短时期或极小样本（如单次研讨会十余篇收稿）的场景，此时人工核对效率与准确率远超复杂自动化消歧流水线。

> [!method-limits] 方法局限与科学学系统偏倚
> - **非对称的识别能力偏差** 算法对长期持续高产的资深知名学者拥有极其丰富的上下文先验信息，极易完成可靠精准的消歧识别；而对于学术起步阶段、仅发表过一两篇论著的新生代青年学者，由于缺乏合作网络与学术特征锚点，算法错配与漏配率显著偏高。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 16)]]
> - **文献计量宏观分布扭曲风险** 未完全消歧的数据库往往倾向于将常见姓名学者的产出机械合并为超高产超级巨星（人为加剧右偏幂律），或将频繁跨单位变动学者的产出割裂为数个单篇发表者，从而系统性误导科学计量学生产力模型的实证估计。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 16)]]

---

> [!entry-map] 条目关联
>
> | 条目 | 类型 | 贡献 |
> |:-----|:-----|:-----|
> | [[Scientific Productivity]] | 概念 | 著者姓名消歧为测度真实学者个体科研生产力提供不可或缺的前提数据清洗保障。 |
> | [[Bibliometric Analysis]] | 方法 | 构成一切微观与中观文献计量实证分析流程中的前置底层工序。 |
> | [[Big Science]] | 概念 | 大科学时代的多机构协作与超多署名工程直接放大了姓名消歧的复杂性。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit01|Wang & Barabási (2021)]] — 设立专栏“姓名消歧”，系统总结限制个体生产力追踪的四大核心技术瓶颈，并指明其对后文生产力统计结论构成的潜在约束。
