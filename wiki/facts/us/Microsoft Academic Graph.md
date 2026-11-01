---
title: Microsoft Academic Graph
aliases:
  - 微软学术图谱
  - MAG
  - Microsoft Academic
  - 微软学术知识图谱
summary: "由微软研究院于 2015 年推出的超大规模异构学术知识图谱与开放计量数据库；收录全球超 2.6 亿篇学术论著、2.7 亿名学者与 14 亿条引文网络，以全量开源机器可读数据支撑了科学学对学术生涯、突破创新与团队科学的里程碑实证研究，于 2021 年底退役后直接催生了 OpenAlex 与 SciSciNet 等新一代开放科学基础设施。"
type: fact
subtype: program
region: "us"
fact_region: "us"
fact_kind: "program"
fact_related_count: 16
fact_related_level: 1
fact_related_stars: "⭐"
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
  - "[[Document]]"
  - "[[Metascience]]"
  - "[[Tracking]]"
  - "[[Creativity]]"
  - "[[Open-Mindedness]]"
  - "[[Team Science]]"
  - "[[Paradigm]]"
  - "[[Data Infrastructure]]"
  - "[[Scientific Productivity]]"
related_theories:
  - "[[Q-Model]]"
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Author Name Disambiguation]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[Web of Science]]"
  - "[[SciSciNet]]"
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit01]]"
  - "[[Argument_Lin_2023_SciData]]"
confidence: high
status: active
created: "2026-10-30"
updated: 2026-11-02
---

---

> [!claim] 项目定位
> 微软学术图谱（Microsoft Academic Graph, MAG）是由微软研究院（Microsoft Research）主导开发的大型异构知识图谱与开放计量数据库。项目以跨学科机器可读网络形式整合全球科研实体，为计算[[Bibliometric Analysis|文献计量学]]、跨学科知识流动分析以及现代科学学（[[Metascience|Science of Science]]）的实证研究提供公共[[Data Infrastructure|数据基础设施]]。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 8–9, 136)]]

> [!program-context] 项目背景
> - **立项时间 / 周期** 2015 年由微软研究院正式上线，按周与月度周期进行知识更新与全量转储，直至 2021 年 12 月 31 日正式停止运营并归档退役。
> - **发起方与资助机制** 由微软公司全额资助并由微软研究院（雷德蒙德与北京团队）主导研发，核心架构师包括王冠三（Kuansan Wang）与亚历克斯·韦德（Alex Wade）。
> - **覆盖范围与对象** 收录全球逾 2.6 亿篇学术出版物、2.7 亿名科研人员、2.6 万所研究机构与 14 亿条双向引用关系，覆盖自然科学、医学工程与人文社科领域。
> - **核心问题导向** 攻克传统商业引文数据库（Web of Science、Scopus）高昂订阅门槛与严格数据导出条目配额限制，为科学学提供支持全网图计算的开放机器可读图谱。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 8–9)]]

---

> [!claim] 核心干预／机制假说
> 通过构建包含出版物、学者、机构、期刊与学科概念的异构图谱，并结合工业级图嵌入与自然语言处理算法实现大规模自动化[[Author Name Disambiguation|姓名消歧]]与开放许可转储，能够打破专有封闭数据库壁垒，激发宏观大规模量化科学学研究。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 8–9, 169)]]

> [!policy-design] 方案设计
> - **项目目标** 建立覆盖全球科研产出的超大规模机器可读异构知识图谱，支撑前沿科学学实证推演与学术语义挖掘。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 8–9)]]
> - **覆盖对象** 全球学术期刊论文、预印本、学术专著、专利文献、学术会议录及其关联学者与学术机构。
> - **干预措施** 依托必应爬网引擎自动化抽取学术文本元数据，构建六大核心实体异构拓扑网络，并按开放数据协议（ODC-BY）通过云端免费分发全量转储文件与语义检索 API。
> - **实施控制** 应用多任务图嵌入与多层语义树模型校准学者和机构实体消歧精度，结合同行评议来源过滤低质抓取噪声。

> [!citation-card] 大数据科学学对全量图谱的依赖
> 对跨越一个世纪的 5,300 万名研究者与近 9,000 万篇文献的量化追踪证实，文献总量与科研人员规模同步呈指数级扩张。学界依托微软学术图谱与科学引文索引等全量数据库，才得以首次在宏观尺度上确证：个体学者的年均发文量百年来始终维持在每年约两篇的认知稳态，宏观爆炸完全由科研队伍扩张驱动。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 8–9, 169)]]
>
> *[[Tracking]] 53 million scientists and nearly 90 million papers over the past century confirms that the exponential growth in the number of scientific papers has gone hand-in-hand with an exponential increase in the number of scientists... confirming that scientists’ individual productivity has remained remarkably constant over the past century.*

---

> [!dev-timeline] 项目推进历程
> - **2015 年 — 系统架构发布与全量开源** 微软研究院在国际学术会议上正式公开微软学术知识图谱技术规范，向科研界免费开放全量原始数据压缩包下载。
> - **2016–2020 年 — 科学学黄金时代的实证基座** MAG 成为计算社会科学与物理学界研究科学学的基础数据源，直接支撑了关于职业生涯稳态（[[Argument_Sinatra_2016_Science|Sinatra et al., 2016]]）、[[Creativity|创造力]]迸发（Liu et al., 2018）及团队规模与颠覆性创新（Wu et al., 2019）等里程碑突破。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 8–9)]]
> - **2021 年 — 宣布退役与向开放科学社区移交** 微软官方于 2021 年 5 月宣布项目将在年底停运；全球开放科学组织依托其最后一版全量数据（截至 2021 年 12 月 31 日）启动数据归档与继任基础设施建设。
> - **2022 年至今 — 衍生 OpenAlex 开放生态** 非营利机构 OurResearch 承接 MAG 的实体拓扑模式与唯一标识符体系，无缝推出全开源学术基础设施 OpenAlex，使 MAG 的数据遗产得以长期维系。
> - **2023 年 — SciSciNet 承接数据清洗与深化扩展** 西北大学 CSSI 团队以 MAG 2021 年终版为底库，解决其预印本-正式出版成果家族重复与未分类记录噪声问题，重算 1.34 亿篇文献引文分布并贯通 NSF/NIH 资助与专利转化，建立 SciSciNet 开源数据湖。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

---

> [!actor-grid] 实施协同矩阵
> - **发起与资助方** 微软公司与微软研究院，负责分布式知识挖掘系统搭建、必应索引集成与大规模算力保障。
> - **研发与数据中心** 微软研究院认知服务与自然语言计算组，主导异构图谱模式设计与图表示学习算法研发。
> - **一线执行机构** 全球各大学计算社会科学实验室（如东北大学复杂网络研究中心、西北大学科学学与创新科学中心）参与算法评估与需求反馈。
> - **受试与受益对象** 全球文献计量学学者、科学学研究人员、高校科技政策制定部门与科研智库。

> [!pathways] 实施路径与管理
> - **纵向传导与支持** 依托必应海量网页抓取学术预印本、期刊官网、学术简历与机构主页，提取结构化元数据。
> - **横向跨部门协同** 借助 Azure 云平台提供统一数据下载，科研团队可利用分布式计算集群直接挂载分析，免除单机算力瓶颈。
> - **动态反馈与调整** 采用宽松的 ODC-BY 协议，允许研究人员在署名来源前提下任意分发、再加工或商业化衍生，为科学计量学研究建立了公开共享的数据公地。

---

> [!indicators] 评估指标体系
> - **投入指标** 实体节点总规模（超 5 亿个节点）、跨学科覆盖范围（涵盖 19 个一级学科及六级分类概念树）。
> - **过程与依从性指标** 必应爬网抓取频率（周更与月更）、实体消歧综合 F1 值（在公开评测集中超 90%）。
> - **产出与结果指标** 文献收录总量（2.6 亿篇）、引文网络拓扑连接数（14 亿条双向引用边）、衍生里程碑论文引用频次。

> [!finding-cards] 核心实证结论
> 1. **科学队伍与产出宏观演化确证** 证实近一个世纪以来学术文献以约 10–15 年翻倍的指数速率增长，且该扩张由科研从业人员基数的同构膨胀主导，学者人均年发文量长期稳定在约 2 篇。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 8–9, 169)]]
> 2. **科研团队模式变迁的实证映射** 通过分析长周期合署变迁，揭示单篇成果署名学者人数从 1900 年的均值 1 人稳步增至 2015 年的 3.5 人以上，证实知识探索已由独行侠模式彻底转向[[Team Science|团队科学]]主导。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 8–9)]]
> 3. **个体学术造诣非随机性解构** 为 $Q$ 模型提供了全生命周期出版时间序列，证实科学家的单篇影响力符合能力因子与选题价值的乘法卷积，终身保持恒定。
> 4. **底库清洗与成果家族聚拢对引文精度的修正** 林子敬等针对 MAG 终版数据的实证检视表明，MAG 存在预印本与期刊版本割裂导致施引/被引割裂的系统误差；通过家族聚合与引文重新配赋，不仅消除了跨版本引文重复计算，更证实了清洗前后引文等级相关系数高达 0.991，确证了 MAG 宏观引文分布的稳健性。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

> [!stat-cards]- 关键实证数据
> - **2.6 亿篇** 原始收录学术出版物总量。
> - **134,129,188 篇** 经成果家族聚拢与学术清洗后的核心文献集合（SciSciNet）。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **14 亿+ 条** 原始定向引用边数。
> - **0.991** MAG 原始引文与清洗配赋后引文分布的斯皮尔曼等级相关系数。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

---

> [!debates] 核心争议与现实局限
>
> > [!axis] 商业企业单方运维与公共基础设施脆弱性争议
> > 科技巨头主导的大型基础设施面临企业商业战略调整带来的骤停风险。
> >
> > - **批评观点** 微软单方面宣布终止运营 MAG，导致大量依赖其月度更新的科研项目和分析管线陷入停摆，暴露出依赖营利性科技巨头维系科研公共产品的不稳定性。
> > - **回应辩护** 微软在停运前提前数月公开通告，并发布最终完备全量转储，更以开放版权直接促成非营利继承者 OpenAlex 的建立，完成了从企业孵化向社区自治的[[Paradigm|范式]]交接。
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
> | [[Web of Science]] | Fact (Program) | 科学学专有商业引文数据库代表，与 MAG 构成封闭商业与全量开源的互补对照。 |
> | [[SciSciNet]] | Fact (Program) | 衍生学术数据湖，以 MAG 终版为基础清洗构建跨源实证基础设施。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Lin_2023_SciData|Lin et al. (2023)]] — 以 MAG 2021 年终版为底库，通过成果家族聚拢与引文重新配赋提炼 1.34 亿篇核心出版物，开源构建连接外部资助与转化的 SciSciNet 数据湖。
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit01|Wang & Barabási (2021)]] — 将微软学术图谱作为核心实证基座，系统测定科学文献膨胀、科研人员增长与人均生产力百年稳态规律（pp. 8–9, 136, 169）。
