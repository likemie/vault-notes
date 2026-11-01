---
title: SciSciNet
aliases:
  - 科学学数据湖
  - SciSciNet Data Lake
  - SciSciNet 开放数据湖
summary: "由美国西北大学科学学与创新科学中心（CSSI）于 2023 年开源发布的大规模科学学研究开放数据湖；以规范化清洗与家族去重后的微软学术图谱（MAG）1.34 亿篇核心论著为基石，整合学者、机构、引文网络与 19 个一级学科，贯通 NSF 与 NIH 上游资助及专利、临床试验等下游应用，并全量预计算颠覆性指数等指标，为科学学提供高复现、低门槛的公共实证基础设施。"
type: fact
subtype: program
region: "us"
fact_region: "us"
fact_kind: "program"
fact_related_count: 13
fact_related_level: 1
fact_related_stars: "⭐"
fact_related_color: "#ede9fe"
period: "2023–至今"
initiator_organization: "Center for Science of Science and Innovation (CSSI), Northwestern University"
official_website: "https://figshare.com/articles/dataset/SciSciNet/22198909"
website: "https://figshare.com/articles/dataset/SciSciNet/22198909"
tags:
  - fact/program
  - field/science-of-science
  - theme/data-infrastructure
  - theme/scientometrics
  - theme/open-science
  - region/us
related_concepts:
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
related_arguments:
  - "[[Argument_Lin_2023_SciData]]"
confidence: high
status: active
updated: 2026-11-01
---

---

> [!claim] 项目定位
> 由美国西北大学科学学与创新科学中心（Center for Science of Science and Innovation, CSSI）团队发起并公开维护的大规模开放科学学数据湖，旨在打破学术大数据孤岛与高昂算力壁垒，为全球科研人员提供覆盖 1.34 亿篇论著、贯通资金与转化应用的统一实证[[Data Infrastructure|数据基础设施]]。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

> [!program-context] 项目背景
> - **立项时间 / 周期** 2023 年于《科学数据》（*Scientific Data*）正式发布，常态化在 Figshare 平台开源托管与增量维护。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **发起方与资助机制** 由[[Dashun Wang|王大顺（Dashun Wang）]]教授领衔的西北大学 CSSI 团队主导研发，依托美国国家科学基金会与阿尔弗雷德·P·斯隆基金会等项目资助。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **覆盖范围与对象** 整合 134,129,188 篇学术成果、4.14 亿条学者-机构关系、15.89 亿条引文对，全面映射 19 个一级学科与 292 个子学科。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **核心问题导向** 解决科学学实证中跨库匹配难、数据清洗重复、高算力指标复现壁垒高三大难题。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

---

> [!claim] 核心干预／机制假说
> 通过建立统一规范的开放数据湖架构，将繁杂的原始图谱清洗与核心测度指标预计算收拢为公共产品，能够直接降低科研准入门槛、提升科学学实证结论的可复现性与稳健性。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

> [!policy-design] 方案设计
> - **项目目标** 建立高覆盖、高保真、贯通上下游社会经济脉络的端到端开放科研数据库。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **覆盖对象** 全球范围内的学术期刊论文、学术专著、会议论文集、学位论文及其对应的科研基金、专利与公众舆论。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **干预措施** 公布 22 张规范化 TSV 数据表，提供清洗脚本与模糊匹配算法，免费开放近 5000 万篇论文的指标预计算成果。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **实施控制** 建立针对 Dimensions 等顶尖商业数据库的双盲交叉检验，执行严格的时间窗约束与多指标一致性核验。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

> [!citation-card] 开放数据湖对科学学共同体的使能目标
> 开放数据湖旨在为学术共同体提供大规模实证基石，增强新发现的证据质量并提升研究结论的可复现性与稳健性；通过汇聚多源数据源与测度结果，大幅削减预处理重复损耗，降低准入门槛并激发新理论的多元性。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
>
> *Overall, this data lake serves as an initial but useful resource for the field, by lowering the barrier to entry, reducing duplication of efforts in data processing and measurements, improving the robustness and replicability of empirical claims, and broadening the diversity and representation of ideas in the field.*

---

> [!dev-timeline] 项目推进历程
> - **2021–2022 — 原始图谱抽取与清洗算法研发期** 锁定微软学术图谱 2021 年终版数据，研发论文家族聚合算法与闭环引文重算规程，建立 NSF 非结构化引文字符串解析流水线。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **2022–2023 — 大规模高通量指标解算与交叉验证期** 全量解算 4800 万篇论文的颠覆性得分与 4400 万篇期刊论文的共引非典型性 Z 分数，与 Dimensions 商业数据库开展跨库交叉验证。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **2023–至今 — 开放平台上线与共同体开源运营** 数据湖正式通过 Figshare 与《科学数据》对全球学术共同体免费开放，持续支持跨学科量化科学学研究。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

---

> [!actor-grid] 实施协同矩阵
> - **发起与研发团队** 西北大学科学学与创新科学中心，负责整体架构设计、算法实现、数据清洗与指标预计算。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **开源托管平台** Figshare 数据托管仓库与 GitHub 开源代码仓库，提供稳定的元数据下载与版本归档支持。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **上游基础设施提供方** 微软学术图谱（MAG）、Crossref、PubMed、NSF、NIH、USPTO 等公共机构提供基础开放数据流。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **终端口碑与研究群体** 全球科学学、文献计量学、科技政策与创新社会学研究者与高等教育量化评价团队。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

> [!pathways] 实施路径与管理
> - **纵向传导与支持** 从原始海量学术文本中抽离主论著，再向下游辐射扩展至专利引文、临床试验与社交媒体讨论。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **横向跨部门协同** 串接自然科学基金资助、医疗试验准入与专利审查等多维公共管理系统的制度数据。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **动态反馈与调整** 在发现预印本与正式发表版本共存导致引文虚高时，引入论文家族聚拢与施引-被引闭合重算机制校正统计失真。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

---

> [!indicators] 评估指标体系
> - **覆盖广度指标** 收录主论著总数（1.34 亿篇）、包含的独立学者数（1.34 亿名）及引文对规模（15.89 亿条）。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **外部对齐精度指标** 与商业数据库 Dimensions 的共有文献比对率（85.97%）、篇级引文斯皮尔曼相关系数（0.946）及 NIH 资助重合率（99.7%）。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **规律再现效度指标** 团队规模与颠覆性负相关斜率、常规与新颖组合四象限命中率梯度、WSB 动力学参数拟合误差（MAPE < 0.15）。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

> [!finding-cards] 核心实证结论
> - **极佳的商业基准一致性** 与专有商业数据库相比，开源构建的数据湖在引文测算与项目资助匹配上展现出高度一致性与更优的边缘成果捕获能力。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **经典的科学学规律重现** 在全量数据规模下稳健再现了小团队颠覆性优势、跨学科延迟唤醒与知识常规性/新颖性平衡等重大发现。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **公共资助与产业渗透的可见性** 揭示了基础科研受公共资助的持续支撑格局及其向专利和临床医疗转化的长程路径。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

> [!stat-cards]- 关键实证数据
> - **134,129,188 篇** 核心主出版物收录总量。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **1,588,739,703 条** 核心文献集内闭环引文对。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **38,740,313 条** 专利引用科学文献关联记录。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **0.991** 引文重新配赋前后的斯皮尔曼等级相关系数。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

---

> [!debates] 核心争议
>
> > [!axis] 数据范围与代表性局限
> > 针对数据湖外部数据源偏向美欧英语体系的学术审视。
> >
> > - **批评观点** 资助数据目前集中于美国 NSF 与 NIH，专利引文主要来自 USPTO 与 EPO，对非英语国家与新兴经济体的科学资助及本土专利覆盖存在结构性盲区。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> > - **回应辩护** 项目以开放架构发布，公布了全套记录对齐算法与数据接口，呼吁全球各地区研究团队协同接入本国科研资助与专利数据库进行增量扩展。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
>
> > [!axis] 开源基础设施可持续维护挑战
> > 针对微软学术图谱停更后开源数据湖长期活力的讨论。
> >
> > - **批评观点** 数据湖以 2021 年底退役的 MAG 为核心底库，若缺乏常态化的图谱更新与活跃维护机制，其时效性优势将随时间推移逐渐减弱。
> > - **回应辩护** 数据湖确立了标准化的家族聚合与外部对齐规则，可无缝迁移并对接 OpenAlex 等新一代开放学术知识图谱，持续发挥基准检验价值。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
