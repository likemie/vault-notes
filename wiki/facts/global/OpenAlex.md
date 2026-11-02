---
title: OpenAlex
aliases:
  - OpenAlex 数据库
  - OpenAlex 开放学术图谱
  - OpenAlex 平台
  - OpenAlex 学术知识图谱
  - openalex.org
summary: "由非营利组织 OurResearch 于 2022 年启动的全球全开放学术知识图谱与元数据基础设施；作为微软学术图谱（MAG）的完全开源替代者，收录全球逾 2.5 亿篇学术论著、9000 余万名学者与数万家机构的关联网络，依托 CC0 协议与开放应用程序接口提供全量免费机器可读数据，是推动现代科学学、开放科学与负责任科研评价转型的核心数据基础设施。"
type: fact
subtype: program
region: global
fact_region: "global"
fact_kind: "program"
fact_related_count: 16
fact_related_level: 1
fact_related_stars: "⭐"
fact_related_color: "#ede9fe"
period: "2022–至今"
initiator_organization: "OurResearch / Arcadia Fund"
official_website: "https://openalex.org"
website: "https://openalex.org"
tags:
  - fact/program
  - field/science-of-science
  - theme/data-infrastructure
  - theme/scientometrics
  - theme/open-science
  - region/global
related_concepts:
  - "[[Data Infrastructure]]"
  - "[[Document]]"
  - "[[Metascience]]"
  - "[[Citation Distribution]]"
  - "[[Combinatorial Novelty]]"
  - "[[Heterogeneity]]"
related_theories: []
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Author Name Disambiguation]]"
  - "[[Record Linkage]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[Microsoft Academic Graph]]"
  - "[[Web of Science]]"
  - "[[Crossref]]"
  - "[[Dimensions]]"
  - "[[SciSciNet]]"
  - "[[COnnecting REpositories]]"
related_arguments:
  - "[[Argument_Liu_2023_NHB]]"
confidence: high
status: active
created: 2026-11-02
updated: 2026-11-02
---

---

> [!claim] 项目定位
> OpenAlex 是由美国非营利机构 OurResearch 于 2022 年 1 月正式上线运营的全球开放学术元数据图谱与数据基础设施。该项目以古代亚历山大图书馆命名，旨在继承并替代退役的微软学术图谱（Microsoft Academic Graph, MAG），依托完全开源代码、公共领域协议（CC0）与高吞吐量数据接口，编织覆盖全球出版物、科研人员、学术机构、学术载体、资助基金与知识概念的完整知识实体网络。[[Argument_Liu_2023_NHB|(Liu et al., 2023)]]

> [!program-context] 项目背景
> - **立项时间 / 周期** 2021 年 5 月在微软宣布 MAG 即将停运后紧急启动研发，2022 年 1 月 3 日正式发布服务，持续作为全球常态化公共数字基础设施迭代运营。
> - **发起方与资助机制** 由长期致力于学术交流去中心化的非营利机构 OurResearch 主导，获得阿卡迪亚慈善基金（Arcadia Fund）数百万美元专项捐赠支持，遵循开放学术基础设施原则（Principles of Open Scholarly Infrastructure, POSI）进行非营利治理。
> - **覆盖范围与对象** 收录全球超过 2.5 亿篇学术出版物、9000 余万位学者主页、10 万余家科研机构、3.5 万个期刊载体与 6.5 万个层级化知识概念标签，建立起跨学科、多语种的开放引文与科研实体映射关系。
> - **核心问题导向** 破解以 Web of Science 与 Scopus 为代表的商业引文数据库昂贵的订阅壁垒、封闭的数据黑箱以及严重的语种与地域偏倚，为全球科学共同体提供透明、可复现、低进入门槛的科研度量数据基座。[[Argument_Liu_2023_NHB|(Liu et al., 2023)]]

---

> [!claim] 核心干预／机制假说
> 通过将分散的跨国预印本、学术出版物、机构库与基金元数据以开源标准化方式汇聚于统一的多关系图谱，并以 CC0 协议向全球零成本开放全量快照与应用程序接口（API），能够从根本上破除数据获取垄断，保障科学学经验结论的可验证性与跨机构复现性。[[Argument_Liu_2023_NHB|(Liu et al., 2023)]]

> [!policy-design] 方案设计
> - **项目目标** 建立完全开放、机器可读且自主可控的全球学术知识实体图谱，替代商业垄断数据源，支撑全景科研评估与科学学大规模计算。
> - **覆盖对象** 全球自然科学、工程技术、人文社会科学领域所有公开发表的期刊学术成果、专著、预印本、数据集及其背后的学者与依托单位。
> - **干预措施** 
>   - **多源数据抽取与图谱对齐** 持续收割 Crossref、PubMed、ORCID、Research Organization Registry（ROR）、Wikidata 及各学科预印本仓储的异构元数据，执行实体对齐与自动消歧。
>   - **多层级概念网络自动标注** 部署基于大语言模型与自然语言处理的端到端概念分类器，对文献摘要与标题进行 6.5 万项知识概念的多标签多级拓扑映射。
>   - **开放数据管道供给** 提供无需身份审核的免费公共 REST API、数据过滤工具以及托管于亚马逊云（AWS S3）的定期全量数据湖快照下载。
> - **实施控制** 建立持续运行的实体识别与消歧准确率基准测试，设立开源 GitHub 议题看板供全球科研人员纠错与反馈异常，维持元数据质量的高频迭代演进。

> [!citation-card] [[Argument_Liu_2023_NHB|Liu et al. (2023)]] 论开放学术数据对科学学的价值
> 商业文献数据库普遍依赖昂贵的付费订阅，造成了学术研究中的数据获取不平等。构建像 OpenAlex 这样更为开放的科学学数据集，不仅能够显著改善经验结论的稳健性与可复现性，还能实质性降低研究者进入该领域的制度门槛。([[Argument_Liu_2023_NHB|Liu et al., 2023, p. 1047]])
>
> *Commercial datasets require paid subscriptions, which can create inequality in data access. Creating more open datasets for the science of science, such as OpenAlex, may not only improve the robustness and replicability of empirical claims but also increase entry to the field.*

---

> [!dev-timeline] 项目推进历程
> - **2021 — 应急立项与架构设计期** 微软宣布将于年底关停 MAG 后，OurResearch 获得阿卡迪亚基金会 450 万美元资助，以 MAG 数据架构为蓝本设计新一代全开放替代架构。
> - **2022 — OpenAlex 正式发布与生态扩展** 平台全面对公开放，无缝承接来自全球原 MAG 用户的量化分析工作流，实现篇级引文网络与学者消歧实体的动态每日更新。
> - **2023–2024 — 全球负责任科研评估与大学排名采纳** 荷兰莱顿大学科学技术研究中心（CWTS）宣布莱顿大学排名（Leiden Ranking）推出基于 OpenAlex 数据的完全开放版本；法国高等教育与科研部宣布国家级资助支持 OpenAlex；索邦大学宣布停订 Web of Science 全面转向 OpenAlex，标志着开放科学基础设施进入主流体制化应用阶段。

---

> [!actor-grid] 实施协同矩阵
> - **发起与运维实体** OurResearch 技术工程与数据科学核心团队，负责平台日常架构维护、ETL 数据流水线与 API 高并发吞吐。
> - **资助保障机构** 阿卡迪亚基金会（Arcadia Fund）及全球高校与科研图书馆联盟，通过捐赠与协同会员制保障项目的非营利持续运营。
> - **协同元数据网络** Crossref、DataCite、ORCID 与 ROR 等开放标识符联盟，共同维护互操作性国际标准。
> - **终端研究用户** 全球科学学、文献计量学、信息科学学者与高校科研管理决策部门，依托其开展客观的科研态势研判与因果评估。

---

> [!indicators] 评估指标体系
> - **数据广度与深度** 涵盖文献总量、学者实体数量、机构对齐率、引文边缘链接数与全文学术开放获取（OA）链接覆盖率。
> - **服务可用性与普及度** 日均 API 调用次数、全球开发者与高校机构接入数量、全量快照月度下载吞吐量。
> - **科研产出与转化** 在科学学顶级期刊与国际计量学大会中以 OpenAlex 为核心实证数据源的发表数量与可复现研究比例。

> [!finding-cards] 核心实证结论
> - **多源覆盖广度超越传统商业库** 实证研究显示，OpenAlex 在非英语文献、开放获取预印本及全球南方国家科研成果的收录规模上显著超越了传统 Web of Science 与 Scopus，有效修正了知识度量中的语种与地理不平等。
> - **实体对齐精度稳步提升** 依托 ROR 机构唯一标识符与不断优化的学者消歧机器学习算法，OpenAlex 在跨国跨学科层面的机构与学者识别准确率已与头部商业数据源达到同等可用置信度，为大规模科学学因果推断奠定了可靠的数据基础。

> [!stat-cards]- 关键实证数据
> - **250M+** 全球学术出版物与预印本收录总量。
> - **90M+** 经过机器学习消歧的学者实体画像。
> - **100%** 核心代码开源且全量数据遵循 CC0 公共领域许可协议。

---

> [!debates] 核心争议
>
> > [!axis] 数据消歧精度与商业清洗质量的取舍
> > 部分文献计量学者对开放众包与自动化算法清洗的数据纯净度提出顾虑。
> >
> > - **批评观点** 批评者指出，传统商业数据库（如 Web of Science）依靠长期人工编辑团队进行文献标引与分类，在特定细分专业领域的学者消歧与文献类型判定上具有更高的规范性；OpenAlex 高度依赖算法推理，偶有将同名学者或跨学科机构误合并的情况。
> > - **回应辩护** OpenAlex 团队与开放科学学者指出，封闭商业数据库的人工清洗规则同样存在不透明与更新滞后问题；OpenAlex 提供完全公开的源数据与消歧代码，允许全球学者自主检验、改进算法并提交修正，这种透明纠错机制在长期演进中具备更强大的自我净化能力。
