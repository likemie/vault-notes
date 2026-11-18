---
title: Cluster Sampling
aliases:
  - 整群抽样
  - cluster sample
  - 整群抽样法
summary: "当总体规模庞大且地理分布广泛时，将总体划分为若干自然群组并对所选整群内所有成员进行全查的概率抽样方法；以行政可行性换取统计精度，需通过扩大群数量并结合分层抽样以缓解群内同质性偏误。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 8
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/sampling
  - quantitative-research
related_concepts:
  - "[[Unit of Analysis]]"
  - "[[Homophily]]"
  - "[[Industrial District]]"
  - "[[Effective Sample Size]]"
related_theories: []
related_methods:
  - "[[Random Sampling]]"
  - "[[Linear Probability Model]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]]"
  - "[[Argument_Phyo_2025_SocSci]]"
confidence: high
status: completed
created: 2026-06-22
updated: 2026-11-19
---

---

> [!def] Cluster Sampling
> 整群抽样（Cluster Sampling）是将大规模或地理分散的总体划分为若干具有自然聚集特征的初级抽样单元（群，Clusters，如学校、村庄、行政街区），随机抽取部分群并对被选群内全部个体或子样本展开调查的概率抽样方法。该方法以一定的统计精度损失换取现实调查的可行性，有效解决了大范围田野调查中无法建立全量个体抽样框的行政瓶颈。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, Ch. 8, pp. 147–148)]]

> [!method-scope] 方法范围
> - **研究对象** 地理、组织或行政上自然聚集的群体，如学校、班级、村落、社区住户等。
> - **问题类型** 适合全国性或跨国大范围教育、人口与健康宏观调查等需要大规模覆盖但行政资源有限的研究。
> - **[[Unit of Analysis|分析单位]]** 初级抽样单元为群（Cluster），最终观测单元为群内个体成员或住户。
> - **输出形式** 具备宏观总体代表性但带有群聚相关性的概率样本数据集及其对应的抽样权重。

> [!citation-card] 关键定义
> 当总体庞大且高度分散时，采取简单随机抽样往往面临不可逾越的行政与后勤障碍。整群抽样通过选择地理或组织上界限清晰的群组，并在选定群内展开全员或两阶段测量，成为大规模实证调查的可行进路。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, Ch. 8, p. 147)]]
>
> *When the population is large and widely dispersed, gathering a simple random sample poses immense administrative and logistical hurdles. Cluster sampling addresses this by selecting geographically or organisationally bounded groups, sampling everyone within selected clusters.*

---

> [!method-position] 认识论与方法定位
> - **知识观** 承认社会与教育现实中个体的空间群聚性与组织嵌套性；样本代表性依赖于群间异质性与抽选随机性。
> - **研究者角色** 研究者需在调查设计阶段审慎平衡行政成本与统计效能，决定群的数量规模、每群抽样率以及分层变量设定。
> - **有效性标准** 统计有效性取决于设计效应（Design Effect, DEFF）的控制水平及整群稳健标准误（Cluster-Robust Standard Errors）的修正质量。
> - **不声称回答的问题** 单纯整群抽样无法自发消除群内同质性导致的有效样本量缩水，亦不能用于替代对极端特殊异质微小群体的定向过抽样。

> [!method-stack] 方法层级
> - **研究设计** 大规模横截面住户调查（如 DHS、MICS）、教育行政普查与多阶段分层整群抽样。
> - **数据收集** 结构化问卷、面对面入户访谈、标准化测验或学校现场考察。
> - **分析方法** 纳入抽样权重与集群固定效应的计量回归（如含地区固定效应的[[Linear Probability Model|线性概率模型]]）、多层线性模型。
> - **辅助技术** 概率比例规模抽样（Probability Proportional to Size, PPS）、分层抽样权重构建、聚类方差调整。

---

> [!proc] 通用程序
> 1. **界定初级抽样单元（PSU）** 依据地理区划或行政隶属明确群的物理边界，确保总体中每个个体唯一归属于特定群。
> 2. **建立抽样框与分层设定** 编制全量群清单，通常结合城乡区位或经济发展水平进行事前分层以提高代表性。
> 3. **多阶段抽选群与个体** 第一阶段依据概率比例规模抽样抽取特定数量的群，第二阶段在被选群内列出住户或学生并随机抽取最终样本。[[Argument_Phyo_2025_SocSci|(Phyo & Ilie, 2025, pp. 6–7)]]
> 4. **计算抽样权重与方差校正** 测算基准抽样概率、无应答校正权重及群内相关系数（ICC）。
> 5. **加权统计推断与参数报告** 在统计分析中全面应用抽样权重，采用整群稳健标准误检验假设并报告估计结果。

> [!method-stack] 数据与变量
> - **数据结构** 具有明显空间或组织嵌套结构的大样本截面调查数据。
> - **样本与单位** 包含数十至数千个初级抽样单元（PSU）以及成千上万名微观受访个体。
> - **变量或测量** 个体教育与人口学特征变量、家庭财富资产指数、所在群编码及抽样权重。

---

> [!method-fit] 适用判断
> - **适合使用** 总体规模极大且地理分散，缺乏全量个体花名册但具备群清单的大型跨国或全国性调查。[[Argument_Phyo_2025_SocSci|(Phyo & Ilie, 2025, pp. 6–7)]]
> - **谨慎使用** 群间异质性极高且可抽取的群数量较少的情形；若群内同质性过强，少数群容易造成严重的样本偏倚。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, p. 147)]]
> - **不适合使用** 样本规模微小且追求最高统计精度的实验室实验或受控干预设计。

---

> [!method-limits] 方法局限
> - **群内同质性与方差膨胀** 同一社区或学校内的个体往往共享相似的社会经济背景，导致整群样本的信息冗余，其实际[[Effective Sample Size|有效样本量]]远低于表面名义样本量。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, p. 147)]]
> - **误用风险** 在后续统计建模中忽略整群抽样设计，误将样本按独立同分布简单随机样本处理，导致标准误严重低估并产生大量假阳性推断。
> - **补救方式** 遵循多抽群、每群少抽的优化原则；在统计估计中严格纳入整群稳健标准误与分层固定效应。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Random Sampling]] | 替代方法 | 统计精度最高但行政执行成本高昂的经典独立概率抽样基准。 |
> | [[Effective Sample Size]] | 概念 | 整群抽样中受设计效应与群内相关性影响后的实际等效独立样本量。 |
> | [[Linear Probability Model]] | 补充方法 | 分析大样本整群抽样调查数据时常用于检验条件概率的计量模型。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen, Manion & Morrison (2011, Ch. 8)]] — 系统阐述整群抽样的行政可行性优势、实施规程与群内同质性偏误风险。
> - [[Argument_Phyo_2025_SocSci|Phyo and Ilie (2025)]] — 依托二阶段分层整群抽样的 DHS 与 MICS 大样本调查数据，运用全样本抽样权重与聚类稳健回归考察东南亚八国教育获得不平等。
