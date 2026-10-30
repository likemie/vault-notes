---
title: "Tracking Underreported Financial Flows"
aliases:
  - "未充分报告资金流追踪法"
  - "TUFF 方法"
  - "TUFF 数据搜集法"
  - "TUFF methodology"
summary: "由 AidData 开发的系统化非官方披露跨境资金流追踪方法，通过多语种公开信源搜集、独立双重交叉验证、项目生命周期四阶段界定与次国家空间地理编码，测度非 OECD-DAC 国家未系统披露的发展援助、教育基建与奖学金资助。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 15
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - theme/educational-aid
  - theme/public-diplomacy
  - theme/geocoding
related_concepts:
  - "[[Tracking]]"
  - "[[Unit of Analysis]]"
  - "[[Public Diplomacy]]"
  - "[[Epistemology]]"
  - "[[Falsification]]"
  - "[[Reliability]]"
  - "[[Causality]]"
  - "[[Grandes Ecoles]]"
  - "[[Geopolitics]]"
related_facts:
  - "[[TUFF]]"
  - "[[AidData]]"
  - "[[OECD]]"
  - "[[Luban Workshop]]"
related_arguments:
  - "[[Argument_Custer_2021_AidData]]"
related_methods:
  - "[[Triangulation]]"
confidence: high
status: active
created: 2026-10-22
updated: 2026-10-30
---

---

> [!def] Tracking Underreported Financial Flows
> 未充分报告资金流追踪法（[[Tracking]] Underreported Financial Flows, [[TUFF]]）是由威廉与玛丽学院 [[AidData]] 研究实验室开发的一套标准化量化数据搜集与空间编码方法，旨在系统收集、清洗和交叉验证非[[OECD|经济合作与发展组织]]发展援助委员会（OECD-DAC）成员国对外提供的发展金融、官方援助、教育援建与人力资源培训项目数据。[[Argument_Custer_2021_AidData|(Custer et al., 2021, pp. 77–78)]]

> [!method-scope] 方法范围
> - **研究对象** 未加入国际发展援助透明度机制的国家所实施的跨境资助、贷款、校舍援建、全额奖学金发放、职业技术培训中心及语言文化机构。
> - **问题类型** 回答跨境官方资金的投入规模测度、历时演变趋势、受援部门结构分配以及次国家空间地理集聚特征。
> - **[[Unit of Analysis|分析单位]]** 单个援助/合作项目交易记录、受援国次国家行政区（一级或二级行政区划）以及国家年份面板。
> - **输出形式** 具备经纬度地理标记、项目生命周期状态、折算为可比美元价值的项目级微观交易数据库。

> [!citation-card] 开放信源与空间三角测量
> TUFF 方法依托开放来源情报体系，综合政府公报、多语种媒体报道、使领馆公开记录与受援国议会问辩，通过多重交叉核对消除非官方申报带来的信息不透明，将发展金融与[[Public Diplomacy|公共外交]]数据精准锚定至次国家空间坐标。[[Argument_Custer_2021_AidData|(Custer et al., 2021, p. 77)]]
>
> *The TUFF methodology uses a multi-stage tracking and synthesis protocol to gather and [[Triangulation|triangulate]] open-source information about opaque financial flows, converting project records into geocoded datasets for subnational empirical analysis.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 视非透明制度环境下的跨境资金流动为可通过多源公开信息碎片重构的可观察事实，坚持开放透明与可[[Falsification|证伪]]的数据构建原则。
> - **研究者角色** 研究者通过制定严格的信源准入标准、独立背靠背双重编码与第三方复核规则，最大限度剔除单一主观报告带来的偏倚。
> - **有效性标准** 遵循测量效度与内部[[Reliability|信度]]标准，要求每个项目具备可溯源的原始凭证链接，并设置 1 至 8 级空间精度代码评估地理定位的不确定性。
> - **不声称回答的问题** 该方法本身属于描述性与空间测度工具，仅提供资金与项目分布的事实度量，不能直接作为政策效应因果识别的充分依据。

> [!method-stack] 方法层级
> - **研究设计** 观察性多源数据整合与地理空间横截面/面板数据构建。
> - **数据收集** 自动化网络抓取、多语种关键词检索、政府档案审阅与实地使领馆公告核实。
> - **分析方法** 项目生命周期四阶段分类、部门功能归类、WGS84 坐标匹配与次国家空间集聚测度。
> - **辅助技术** 货币现值折算、重合项目消歧算法以及基于 GIS 的空间权重矩阵构建。

---

> [!proc] 通用程序
> 1. 明确目标供援国、受援国范围、观察时间窗口与目标合作领域。
> 2. 构建多语种公开信源爬取索引，覆盖政府官方公报、使领馆网站与本地权威媒体。
> 3. 对抓取到的项目信息进行去重整合，提取项目名称、资助金额、实施主体与地理位置。
> 4. 执行双独立研究员背靠背交叉验证，评定项目实施状态与地理定位精度代码。
> 5. 产出标准化项目级微观数据库，支持空间自相关分析与计量经济学[[Causality|因果推断]]。

> [!method-stack] 数据结构与编码标准
> - **生命周期分类** 项目被严格界定为四个互斥状态：正式认捐（Pledged）、协议承诺（Committed）、具体实施中（Implementing）以及竣工交付（Completed）。在测度实际落地成效时，通常仅采纳后两个状态。
> - **空间精度分级** 采用 1 至 8 级地理代码：
>   - **代码 1** 精确物理坐标点（如特定[[Grandes Ecoles|大学校]]区、医院或特定[[Luban Workshop|鲁班工坊]]大楼）。
>   - **代码 2** 位于特定点状设施周边 25 公里半径内。
>   - **代码 3** 次国家二级行政区（县或自治市）。
>   - **代码 4** 次国家一级行政区（省或邦）。
>   - **代码 5** 跨多个省份的大型廊道或全国范围均质分配项目。

> [!software-impl] 软件实现与空间映射
> - **数据采集与清洗** 使用 Python 自动化脚本监控目标使领馆与教育部外事网站更新，利用正则表达式抽取金额与合同编号。
> - **地理空间匹配** 通过 OpenStreetMap API 与 GeoNames 地名词典进行次国家地理实体命名消歧，统一投影至 WGS84 坐标系。
> - **统计与空间分析** 使用 R 语言的 `sf` 与 `spdep` 程序包计算空间莫兰指数，或在 Stata 中与受援地微观人口调查数据合并进行因果识别。

---

> [!method-fit] 适用判断
> - **适合使用** 评估非 OECD-DAC 国家（如中国、俄罗斯、沙特阿拉伯等）在全球南方实施的教育基础设施援建、留学生奖学金配额、职业实训中心及医疗援助。[[Argument_Custer_2021_AidData|(Custer et al., 2021, pp. 14–16, 77)]]
> - **谨慎使用** 涉及军事防务秘密合作、短期秘密现金转移或非公开物资援助的项目，公开信源可能存在系统性截断风险。
> - **不适合使用** 试图单凭资金流规模直接推论公众态度或政策偏好的研究，必须与受援地微观民调相结合。

---

> [!method-limits] 方法局限
> - **偏误来源** 存在公开性偏误（Media Bias），资本密集型的大型地标建筑和高调仪式更容易被媒体报道，而小额基层教学耗材支持容易被遗漏。
> - **承诺落实偏差** 官方初步宣布的投资意向与实际拨付之间可能存在延迟或取消，若不区分项目生命周期阶段将导致数据虚高。
> - **精度衰减** 奖学金名额等全国统筹配额往往难以精确到次国家特定学校，在空间精度代码 5 下容易降低局部空间分析的分辨率。
> - **补救方式** 优先限定分析样本为“已实施”或“已完成”项目，并结合受援国本土统计年鉴进行第二轮审校。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[AidData]] | 事实 | 该方法的研发主体与长期数据库维护机构。 |
> | [[Geopolitics]] | 概念 | 为该方法提供的跨境资金流动与空间博弈分析提供了理论问题意识。 |
> | [[Public Diplomacy]] | 概念 | 该方法常用于测度公共外交中资金外交与文化交流的实体投向。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Custer_2021_AidData|Custer et al. (2021)]] — 运用 TUFF 方法系统追踪 2000–2017 年间中国对南亚与中亚 13 国实施的 251 项教育援助工程与 35.8 万个官方奖学金名额，并完成次国家层级空间定位。
