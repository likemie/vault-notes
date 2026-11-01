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
fact_related_count: 15
fact_related_level: 1
fact_related_stars: "⭐"
fact_related_color: "#ede9fe"
period: "2023–至今"
initiator_organization: "Center for Science of Science and Innovation (CSSI), Northwestern University"
official_website: "https://figshare.com/collections/SciSciNet_A_large-scale_open_data_lake_for_the_science_of_science_research/6076908"
website: "https://doi.org/10.6084/m9.figshare.c.6076908.v1"
repository: "https://github.com/kellogg-cssi/SciSciNet"
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
  - "[[Literature Search]]"
  - "[[Patent Citation]]"
  - "[[Clinical Trial]]"
  - "[[Document]]"
related_theories:
  - "[[WSB Model]]"
related_methods:
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[Dashun Wang]]"
  - "[[Albert-László Barabási]]"
related_facts:
  - "[[National Science Foundation]]"
  - "[[National Institutes of Health]]"
  - "[[Microsoft Academic Graph]]"
  - "[[Education Policy Outlook]]"
related_arguments:
  - "[[Argument_Lin_2023_SciData]]"
confidence: high
status: active
updated: 2026-11-02
---

---

> [!claim] 项目定位
> 由美国西北大学科学学与创新科学中心（Center for [[Metascience|Science of Science]] and Innovation, CSSI）团队发起并公开维护的大规模开放科学学数据湖，旨在消除学术数据孤岛并降低算力门槛，为全球科研人员提供覆盖 1.34 亿篇论著、贯通资金与转化应用的统一实证[[Data Infrastructure|数据基础设施]]。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

> [!program-context] 项目背景
> - **立项时间 / 周期** 2023 年于《科学数据》（*Scientific Data*）正式发布，常态化在 Figshare 平台（数据集合网址：https://doi.org/10.6084/m9.figshare.c.6076908.v1 ；数据集网址：https://figshare.com/articles/dataset/SciSciNet/22198909 ）与 GitHub 开源代码仓库（https://github.com/kellogg-cssi/SciSciNet ）开源托管与增量维护。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **发起方与资助机制** 由[[Dashun Wang|王大顺]]（Dashun Wang）教授领衔的西北大学 CSSI 团队主导研发，依托[[National Science Foundation|美国国家科学基金会]]与阿尔弗雷德·P·斯隆基金会等项目资助。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **覆盖范围与对象** 整合 134,129,188 篇学术成果、4.14 亿条学者-机构关系、15.89 亿条引文对，全面映射 19 个一级学科与 292 个子学科。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **核心问题导向** 攻克科学学实证研究中跨库匹配困难、数据清洗重复劳动繁重、高算力指标复现门槛高三大难题。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

---

> [!claim] 核心干预／机制假说
> 通过建立统一规范的开放数据湖架构，将繁杂的原始图谱清洗与核心测度指标预计算收拢为公共产品，能够直接降低科研准入门槛、提升科学学实证结论的可复现性与稳健性。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

> [!policy-design] 方案设计
> - **项目目标** 建立高覆盖、高保真、贯通上下游社会经济脉络的综合开放科研数据库。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **覆盖对象** 全球范围内的学术期刊论著、学术专著、会议录、学位成果及其对应的科研基金、专利与公众舆论。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **干预措施** 公布 22 张规范化数据表（制表符分隔值，Tab-Separated Values, TSV），提供清洗脚本与模糊匹配算法，免费开放近 5000 万篇论著的指标预计算成果。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **实施控制** 建立针对 Dimensions 等主流商业数据库的基准交叉检验，执行严格的时间窗约束与多指标一致性核验。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

> [!case] 跨源关联个案追踪：从单一成果穿透至 [[National Institutes of Health|NIH]] 资助全景
> 以焦点论著《遗传性痉挛性截瘫基因定位研究》（PaperID: `246319838`）为例：
> - 在数据湖主表中可调取其基础元数据与全量被引计数。
> - 在 `SciSciNet_Link_NIH` 关联表中可映射至 3 项核心美国国立卫生研究院（National Institutes of Health, NIH）项目编号：`R01NS033645`、`R01NS036177` 与 `R01NS038713`。
> - 研究者可直接在 NIH RePORTER 官方平台调取该成果关联课题的立项时间、总资助金额与课题负责人信息，完整呈现公共资助向学术突破转化的实证链条。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

> [!citation-card] 降低准入门槛与提升实证可复现性
> 科学学开放数据湖为学术共同体提供大规模实证基石，增强新发现的证据质量并提升研究结论的可复现性与稳健性；通过汇聚多源数据源与测度结果，大幅削减预处理重复投入，降低准入门槛并激发新理论的多元性。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
>
> *Overall, this data lake serves as an initial but useful resource for the field, by lowering the barrier to entry, reducing duplication of efforts in data processing and measurements, improving the robustness and replicability of empirical claims, and broadening the diversity and representation of ideas in the field.*

---

> [!dev-timeline] 项目推进历程
> - **2021–2022 — 原始图谱抽取与清洗算法研发期** 锁定[[Microsoft Academic Graph|微软学术图谱]] 2021 年终版数据，研发成果家族聚合算法与内部引文重算规程，建立美国国家科学基金会（National Science Foundation, NSF）非结构化引文字符串解析流水线。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **2022–2023 — 大规模高通量指标解算与交叉验证期** 全量解算 4800 万篇论著的颠覆性得分与 4400 万篇期刊成果的共引非典型性 Z 分数，与 Dimensions 商业数据库开展跨库交叉验证。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **2023–至今 — 开放平台上线与共同体开源运营** 数据湖正式通过 Figshare 与《科学数据》对全球学术共同体免费开放，持续支持跨学科量化科学学研究。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

---

> [!actor-grid] 实施协同矩阵
> - **发起与研发团队** 西北大学科学学与创新科学中心，负责整体架构设计、算法实现、数据清洗与指标预计算。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **开源托管平台** Figshare 数据托管仓库（集合主页：https://doi.org/10.6084/m9.figshare.c.6076908.v1 ）与 GitHub 开源代码仓库（https://github.com/kellogg-cssi/SciSciNet ），提供稳定的元数据下载与版本归档支持。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **上游基础设施提供方** 微软学术图谱（Microsoft Academic Graph, MAG）、Crossref、PubMed、NSF、NIH、美国专利商标局（United States Patent and Trademark Office, USPTO）等公共机构提供基础开放数据流。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **终端口碑与研究群体** 全球科学学、[[Bibliometric Analysis|文献计量学]]、科技政策与创新社会学研究者与高等教育量化评价团队。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

> [!pathways] 实施路径与管理
> - **纵向传导与支持** 从原始海量学术文本中抽离主论著，再向下游辐射扩展至[[Patent Citation|专利引文]]、[[Clinical Trial|临床试验]]与社交媒体讨论。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **横向跨部门协同** 串接自然科学基金资助、医疗试验准入与专利审查等多维公共管理系统的制度数据。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **动态反馈与调整** 在发现预印本与正式发表版本共存导致引文虚高时，引入成果家族聚拢与施引-被引范围重算机制校正统计失真。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

---

> [!indicators] 评估指标体系
> - **覆盖广度指标** 收录主论著总数（1.34 亿篇）、包含的独立学者数（1.34 亿名）及引文对规模（15.89 亿条）。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **外部对齐精度指标** 与商业数据库 Dimensions 的共有[[Document|文献]]比对率（85.97%）、篇级引文斯皮尔曼相关系数（0.946）及 NIH 资助重合率（99.7%）。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **规律再现效度指标** 团队规模与颠覆性负相关斜率、常规与新颖组合四象限命中率梯度、王-宋-[[Albert-László Barabási|巴拉巴西]]引文动力学模型（[[WSB Model|Wang-Song-Barabási Model]], WSB 模型）拟合参数的平均绝对百分比误差（Mean Absolute Percentage Error, MAPE < 0.15）。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

> [!finding-cards] 核心实证结论
> - **极佳的商业基准一致性** 与专有商业数据库相比，开源构建的数据湖在引文测算与项目资助匹配上展现出高度一致性与更优的边缘成果捕获能力。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **经典的科学学规律重现** 在全量数据规模下稳健再现了小团队颠覆性优势、跨学科延迟唤醒与知识常规性/新颖性平衡等重大发现。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **公共资助与产业渗透的可见性** 揭示了基础科研受公共资助的持续支撑格局及其向专利和临床医疗转化的长程路径。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

> [!stat-cards]- 关键实证数据
> - **134,129,188 篇** 核心主出版物收录总量。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **1,588,739,703 条** 核心文献集内部引文对。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **38,740,313 条** 专利引用科学文献关联记录。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **0.991** 引文重新配赋前后的斯皮尔曼等级相关系数。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

---

> [!debates] 核心争议
>
> > [!axis] 数据范围与代表性局限
> > 针对数据湖外部数据源偏向美欧英语体系的学术审视。
> >
> > - **批评观点** 资助数据目前集中于美国 NSF 与 NIH，专利引文主要来自 USPTO 与欧洲专利局（European Patent Office, [[Education Policy Outlook|EPO]]），对非英语国家与新兴经济体的科学资助及本土专利覆盖存在结构性盲区。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> > - **回应辩护** 项目以开放架构发布，公布了全套记录对齐算法与数据接口，呼吁全球各地区研究团队协同接入本国科研资助与专利数据库进行增量扩展。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
>
> > [!axis] 开源基础设施可持续维护挑战
> > 针对微软学术图谱停更后开源数据湖长期活力的讨论。
> >
> > - **批评观点** 数据湖以 2021 年底退役的 MAG 为核心底库，若缺乏常态化的图谱更新与活跃维护机制，其时效性优势将随时间推移逐渐减弱。
> > - **回应辩护** 数据湖确立了标准化的家族聚合与外部对齐规则，可无缝迁移并对接 OpenAlex 等新一代开放学术知识图谱，持续发挥基准检验价值。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
