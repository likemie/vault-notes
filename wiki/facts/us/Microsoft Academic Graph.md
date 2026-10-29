---
title: Microsoft Academic Graph
aliases:
  - 微软学术图谱
  - MAG
  - Microsoft Academic
  - 微软学术知识图谱
summary: "由微软研究院于 2015 年推出的超大规模异构学术知识图谱与开放计量数据库；收录全球超 2.6 亿篇学术论著、2.7 亿名学者与 14 亿条引文网络，以全量开源机器可读数据支撑了科学学对学术生涯、突破创新与团队科学的里程碑实证研究，于 2021 年底退役后直接催生了 OpenAlex 等新一代开放科学基础设施。"
type: fact
subtype: program
region: "us"
fact_region: "us"
fact_kind: "program"
fact_related_count: 8
fact_related_level: 0
fact_related_stars: "☆"
fact_related_color: "#ede9fe"
period: "2015–2021"
initiator_organization: "Microsoft Research"
official_website: "https://www.microsoft.com/en-us/research/project/microsoft-academic-graph/"
website: "https://www.microsoft.com/en-us/research/project/microsoft-academic-graph/"
tags:
  - fact/program
  - field/science-of-science
  - theme/scientometrics
  - theme/data-infrastructure
  - theme/open-science
  - region/us
related_concepts:
  - "[[Metascience]]"
  - "[[Team Science]]"
  - "[[Data Infrastructure]]"
  - "[[Scientific Productivity]]"
related_theories:
  - "[[Q-Model]]"
related_methods:
  - "[[Author Name Disambiguation]]"
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit01]]"
confidence: high
status: draft
created: "2026-10-30"
updated: "2026-10-30"
---

---

> [!claim] 项目定位
> 微软学术图谱（Microsoft Academic Graph, MAG）是由微软研究院（Microsoft Research）主导开发的大型知识图谱与学术文献元数据库。项目以跨学科机器可读网络形式整合全球科研实体，为计算文献计量学、跨学科知识流动分析以及现代[[Metascience|科学学]]（Science of Science）的实证研究提供公共数据基座。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 8–9, 136)]]

> [!program-context] 项目背景
> - **官方门户与项目存档** 官方项目归档主页为 [Microsoft Academic Graph (Project Archive)](https://www.microsoft.com/en-us/research/project/microsoft-academic-graph/)；社区继任开放数据门户为 [OpenAlex](https://openalex.org/)。
> - **立项时间与生命周期** 2015 年由微软研究院正式发布上线，持续按周/月周期进行全量知识更新，直至 2021 年 12 月 31 日正式停止运营并退役。
> - **发起方与研发团队** 微软研究院（雷德蒙德与北京两地团队深度协作），核心架构师包括王冠三（Kuansan Wang）、亚历克斯·韦德（Alex Wade）等。
> - **覆盖规模与实体跨度** 涵盖全球逾 2.6 亿篇学术出版物、2.7 亿名科研人员、2.6 万所研究机构，收录 14 亿条双向引用关系，覆盖自然科学、医学工程与人文社科全部主流领域。
> - **技术动因与科学需求** 传统商业数据库（Web of Science、Scopus）受限于高昂订阅门槛与严格数据导出条目配额，无法支持整网尺度的复杂网络图挖掘；MAG 旨在通过工业级图计算架构构建全开放机器可读图谱。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 8–9)]]

---

> [!claim] 核心干预／机制假说
> 微软学术图谱通过构建包含成果、学者、机构、出版物与学科概念的多模态异构信息网络，利用图表示学习实现自动化大规模[[Author Name Disambiguation|姓名消歧]]与主题分类，克服封闭商业引文索引的规模瓶颈与访问壁垒。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 8–9, 169)]]

> [!policy-design] 方案设计
> - **多层级异构图结构** 核心图谱由六大类一阶实体节点构成：出版物（Papers）、学者（Authors）、所属机构（Affiliations）、出版载体（Venues）、六级层级主题概念树（Fields of Study）与资助项目（Grants）。
> - **自动化知识抽取与消歧管线** 依托 Bing 搜索引擎的全球网页爬网能力，结合自然语言处理与图嵌入算法对同名学者与机构变体开展动态消歧。
> - **多通道数据分发架构** 提供开放数据公共许可协议（ODC-BY），通过微软 Azure 云存储向全球学术机构免费开放数百吉字节（GB）的完整全量离线数据库转储（Data Dump），并开放语义检索 API 接口。
> - **语义概念多标签投影** 构建包含数十万个跨学科概念的多标签分类树，通过网络拓扑传播实现论著内容主题的自动标注。

> [!citation-card] 大数据科学学对全量图谱的依赖
> 对跨越一个世纪的 5,300 万名研究者与近 9,000 万篇文献的量化追踪证实，文献总量与科研人员规模同步呈指数级扩张。学界依托微软学术图谱与科学引文索引等全量数据库，才得以首次在宏观尺度上确证：个体学者的年均发文量百年来始终维持在每年约两篇的认知稳态，宏观爆炸完全由科研队伍扩张驱动。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 8–9, 169)]]
>
> *Tracking 53 million scientists and nearly 90 million papers over the past century confirms that the exponential growth in the number of scientific papers has gone hand-in-hand with an exponential increase in the number of scientists... confirming that scientists’ individual productivity has remained remarkably constant over the past century.*

---

> [!dev-timeline] 项目推进历程
> - **2015 年 — 系统架构发布与全量开源** 微软研究院在国际学术会议上正式公开微软学术知识图谱技术规范，向科研界免费开放全量原始数据压缩包下载。
> - **2016–2020 年 — 科学学黄金时代的实证基座** MAG 成为计算社会科学与物理学界研究科学学的基础数据源，直接支撑了关于职业生涯稳态（Sinatra et al., 2016）、创造力迸发（Liu et al., 2018）及团队规模与颠覆性创新（Wu et al., 2019）等里程碑突破。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 8–9)]]
> - **2021 年 — 宣布退役与向开放科学社区移交** 微软官方于 2021 年 5 月宣布项目将在年底停运；全球开放科学组织依托其最后一版全量数据（截至 2021 年 12 月 31 日）启动数据归档与继任基础设施建设。
> - **2022 年至今 — 衍生 OpenAlex 开放生态** 非营利机构 OurResearch 承接 MAG 的实体拓扑模式与唯一标识符体系，无缝推出全开源学术基础设施 [OpenAlex](https://openalex.org/)，使 MAG 的数据遗产得以长期维系。

---

> [!actor-grid] 实施协同矩阵
> - **主导研发方** 微软研究院（负责分布式知识挖掘系统搭建、必应索引集成与大规模算力保障）。
> - **学术验证与合作网络** 北大西洋两岸各大高校计算社会科学与网络科学实验室（如东北大学复杂网络研究中心、西北大学科学与创新科学中心）。
> - **开源社区接棒组织** OurResearch（非营利数据托管方）以及 Semantic Scholar（艾伦人工智能研究所学术搜索引擎）。
> - **最终科研受益群体** 全球文献计量学学者、科学学研究人员、高教政策制定机构与科技战略智库。

> [!pathways] 实施路径与管理
> - **跨模态管道集成** 依托必应海量网页抓取学术预印本、期刊官网、学术简历与机构主页，提取结构化元数据。
> - **云端共享与可重现机制** 借助 Azure 云平台提供统一数据下载，科研团队可利用分布式计算集群（如 Apache Spark）直接挂载分析，解决了以往大规模文献计量难以在本地单机复现的硬件瓶颈。
> - **数据开放性承诺** 采用高度宽松的 ODC-BY 协议，允许研究人员在署名来源的前提下任意分发、再加工或商业化衍生，为科学计量学研究建立了公开共享的数据公地。

---

> [!indicators] 数据覆盖与规模指标
> - **文献实体覆盖量** 超 2.6 亿篇学术成果，时间跨度从 1800 年代延伸至 2021 年底。
> - **学者与机构网络规模** 覆盖全球 2.7 亿名学者实体与 2.6 万所学术机构。
> - **引文边数与图拓扑密度** 包含超过 14 亿条文献间定向引用边，构建起密集且动态生长的复杂网络。
> - **消歧准召率表现** 在公开评测集中，算法对学者和机构归属的综合 F1 值超过 90%，显著超越传统启发式规则匹配。

> [!finding-cards] 核心实证贡献
> - **科学队伍与产出宏观演化确证** 证实近一个世纪以来学术文献以约 10–15 年翻倍的指数速率增长，且该扩张由科研从业人员基数的同构膨胀主导，学者人均年发文量长期稳定在约 2 篇。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 8–9, 169)]]
> - **科研团队模式变迁的实证映射** 通过分析长周期合署变迁，揭示单篇成果署名学者人数从 1900 年的均值 1 人稳步增至 2015 年的 3.5 人以上，证实知识探索已由独行侠模式彻底转向[[Team Science|团队科学]]主导。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 8–9)]]
> - **个体学术造诣非随机性解构** 为 $Q$ 模型提供了全生命周期出版时间序列，证实科学家的单篇影响力符合能力因子与选题价值的乘法卷积，终身保持恒定。

> [!stat-cards]- 关键实证数据
> 覆盖历史 200 余年跨度；全景追踪 5,300 万名长期科研人员；实体节点超 5 亿个；引文网络连接逾 14 亿条。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 8–9, 143, 169)]]

---

> [!debates] 核心争议与现实局限
>
> > [!axis] 商业企业单方运维与公共基础设施脆弱性争议
> > 科技巨头主导的大型基础设施面临企业商业战略调整带来的骤停风险。
> >
> > - **批评观点** 微软单方面宣布终止运营 MAG，导致大量依赖其月度更新的科研项目和分析管线陷入停摆，暴露出依赖营利性科技巨头维系科研公共产品的不稳定性。
> > - **回应辩护** 微软在停运前提前数月公开通告，并发布最终完备全量转储，更以开放版权直接促成非营利继承者 OpenAlex 的建立，完成了从企业孵化向社区自治的范式交接。
>
> > [!axis] 爬网元数据噪声与文献类型边界争议
> > 相比 WoS 等严格人工筛选数据库，全网自动化爬取的元数据在部分非英语文献中存在漏标或错标。
> >
> > - **局限指出** 自动化消歧在处理中文、日文等多音字同名学者时存在一定合并偏差，且部分非正式报告与博文偶有混入。
> > - **实证应对** 科学学研究通常设置发表于同行评议期刊或权威会议的过滤门槛，结合引文网络拓扑结构过滤边缘低质节点。

> [!lessons] 经验教训与启示
> - **知识公地的不可逆价值** MAG 的实践证明，开放共享的底层数据基础设施能为一门新兴学科（科学学）的爆发式发展提供强大的动力源泉。
> - **向非营利公共事业转型的必要性** 基础科学数据基础设施必须逐步脱离单一商业实体的资金与战略绑定，依托高校联合体或基金会构建具备长期持久性的去中心化治理结构。

---

> [!entry-map] 相关条目网络
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Data Infrastructure]] | Concept | MAG 是文献计量与科学学领域具有代表性的大型开放数据基础设施。 |
> | [[Scientific Productivity]] | Concept | 依托 MAG 全量学者档案，科学学系统确证了学者微观发文率的百年稳态。 |
> | [[Team Science]] | Concept | MAG 的合署网络完整映射了科学从个体走向团队协作的宏观变迁。 |
> | [[Q-Model]] | Theory | MAG 的高精度学者时间序列为个体能力与选题随机性理论提供了核心实证支撑。 |
> | [[Bibliometric Analysis]] | Method | MAG 充当现代大数据计算文献计量分析的核心数据源。 |
> | [[Author Name Disambiguation]] | Method | MAG 的异构图嵌入消歧模型代表了学术身份解析的前沿水准。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit01|Wang & Barabási (2021)]] — 将微软学术图谱作为核心实证基座，系统测定科学文献膨胀、科研人员增长与人均生产力百年稳态规律（pp. 8–9, 136, 169）。
