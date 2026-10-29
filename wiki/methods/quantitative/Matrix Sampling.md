---
title: Matrix Sampling
aliases:
  - 矩阵抽样
  - 矩阵抽样设计
  - Matrix Sampling Design
  - Multiple Matrix Sampling
  - 平衡不完全区组设计
  - Balanced Incomplete Block Design
summary: "大规模教育评估与心理测量中的试卷分本与抽样分配方法，通过将庞大的测验题库拆分为若干相互重叠的试卷模块，并随机分配给被试样本，使每位受试者仅作答题库的一小部分，在控制作答负荷与测验时长的前提下，实现对群体宏观素养分布与题目全域参数的无偏估计。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 26
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - statistics/psychometrics
  - theme/sampling-design
  - theme/large-scale-assessment
related_concepts:
  - "[[Construct]]"
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Variable]]"
  - "[[Commensuration]]"
  - "[[Technical Rationality]]"
related_theories:
  - "[[Governing at a Distance]]"
related_methods:
  - "[[Item Response Theory]]"
  - "[[Plausible Values]]"
  - "[[Cluster Sampling]]"
  - "[[Item Analysis]]"
  - "[[Sample Size Determination]]"
  - "[[Standard Error]]"
  - "[[Experimental Research]]"
  - "[[Differential Item Functioning]]"
  - "[[Imputation Methods]]"
related_instruments: []
related_facts:
  - "[[PISA]]"
  - "[[TIMSS]]"
  - "[[PIRLS]]"
  - "[[National Assessment of Educational Progress]]"
  - "[[Gaokao]]"
  - "[[Australian Council for Educational Research]]"
  - "[[Educational Testing Service]]"
  - "[[OECD]]"
related_persons: []
related_arguments:
  - "[[Argument_Grek_2009_JEdPolicy]]"
  - "[[Argument_Morgan_Shahjahan_2014_CE]]"
confidence: high
status: draft
created: 2026-10-21
updated: 2026-10-29
---

---

> [!def] Matrix Sampling
> **矩阵抽样（Matrix Sampling）（在试验设计中常体现为平衡不完全区组设计，Balanced Incomplete Block Design, BIBD；亦称多重矩阵抽样，Multiple Matrix Sampling）** 是大规模教育监测与心理测量中结合题库抽样与受试者抽样的试卷编配方法。该方法将待测领域的全部题目划分为若干预设题簇或测试模块（Blocks / Clusters），再依据平衡组合规则将这些模块组合为多套相互重叠且难度均衡的测试卷本（Test Booklets），随机或螺旋式分配给被试作答。其核心特征在于每位受试者仅作答整个测验题库中的一小部分题目，但通过聚合全体受试者的作答反应与重叠锚题网络，能够推断宏观群体在整个领域[[Construct|构念]]上的能力分布参数与题库全域参数。[[Argument_Grek_2009_JEdPolicy|(Grek, 2009, pp. 26–27)]]; [[Argument_Morgan_Shahjahan_2014_CE|(Morgan & Shahjahan, 2014, pp. 197–198)]]

> [!method-scope] 方法范围
> - **研究对象** 大规模测验题库结构、试题模块组合配置、受试者反应矩阵及题目参数估计。
> - **问题类型** 解决大规模教育评估中广阔测评构念覆盖度与受试者答题时间负荷之间的结构性矛盾。
> - **[[Unit of Analysis|分析单位]]** 测验题簇模块、测试卷本、学校与学生抽样样本、宏观受试群体。
> - **输出形式** 平衡试卷配置方案、模块配对平衡矩阵、群体层面能力分布参数估计。

> [!citation-card] 国际大规模测验中的抽样哲学
> 大规模跨国测验的目的在于描述国家或区域教育系统的整体质量与分布特征，评估教育系统是否有效帮助青年一代为成年社会与劳动力市场奠定胜任力基础，通过将题库矩阵化拆分与群体统计建模，无需依赖单个学生的完整作答即可准确刻画总体参数。[[Argument_Grek_2009_JEdPolicy|(Grek, 2009, pp. 26–27)]]
>
> *The technical design of [[PISA]] broke with national curricula to measure broader competences for adult life... through complex statistical matrix sampling and item response modelling, the assessment produces population-level estimates without imposing prohibitive testing burdens on individual students.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 矩阵抽样建立在现代概率测量与抽样理论基础之上，认为测量目标是宏观总体的潜在能力分布，而非测定特定个体的分数；群体统计特性的推断效度优先于个体诊断的完备性。
> - **研究者角色** 测量统计学家通过数学规划确定模块长度、交叠比例与卷本平衡度，直接控制题库覆盖广度与项目参数估计精度。
> - **有效性标准** 模块间平衡配对性、位置次序效应（Position Effects）控制度、全域题目参数的可识别性与连通性。
> - **不声称回答的问题** 矩阵抽样不向单个学生提供可靠的个人分数；单名学生仅作答少量题目，测量误差极大，严禁直接使用原始卷面得分对个人开展选拔、排位或升学决策。

> [!method-stack] 方法层级
> - **研究设计** 大规模横断面抽样调查、纵向追踪监测研究设计。
> - **数据收集** 模块化试卷编制、多版本测试手册印刷与标准化实地分发。
> - **分析方法** 结合[[Item Response Theory|项目反应理论]]（IRT）开展参数并发标定、结合[[Plausible Values|似真值]]技术开展群体潜在分布估计。
> - **辅助技术** 平衡不完全区组算法、试卷随机螺旋发放技术（Spiralling）、多重插补算法。

---

> [!proc] 通用程序
> 1. **界定测验全域与题量规模** 依据评估框架确定阅读、数学、科学等各学科子领域的[[Construct|构念]]跨度与所需题目总量（例如 100 至 200 道题目）。
> 2. **划分题目模块（Item Blocks）** 将题目按认知要求与内容领域平衡分组，形成若干个时长相等、难度相仿且互不重叠的核心题簇（如 13 到 16 个模块）。
> 3. **编制平衡试卷组合（Booklet Assembly）** 采用平衡不完全区组设计，将模块以循环或拉丁方结构分配至不同卷本，确保任意两个模块在至少一个卷本中共同出现，且每个模块在卷本各位置（如第 1、2、3、4 单元）出现的频次完全均衡。
> 4. **样本螺旋分配（Spiralling）** 在考场现场将不同卷本按流水号顺序轮流分发给抽样学生，保证各版本试卷在班级和学校内部达到随机均匀分布。
> 5. **联合参数校准与数据聚合** 依托各卷本间的重叠公共题网络，运用 [[Item Response Theory|IRT]] 边缘极大似然估计实现所有题目参数在统一连续量尺上的无缝锚定。

> [!method-stack] 数据、[[Variable|变量]]与模型
> - **数据结构** 包含高度系统性计划缺失数据（Planned Missing Data）的稀疏作答矩阵。
> - **样本与单位** 分层两阶段[[Cluster Sampling|整群抽样]]学生样本（通常每国数千至上万人）。
> - **关键配置参数** 题库总题目数 $I$、划分的模块数 $B$、每个卷本包含的模块数 $k$、编制的试卷总数 $M$。
> - **模型基础** 结合 Rasch 模型或两参数逻辑斯蒂模型（2PL）进行跨卷本等值标定。

> [!formula-step] 公式步骤一　平衡不完全区组设计约束条件
> $$M \cdot k = B \cdot r, \quad \lambda (B - 1) = r (k - 1)$$
>
> **这个公式在做什么** 计算平衡矩阵抽样设计中试卷总数、模块重复度与任意两模块共同出现次数的数学平衡约束关系。
>
> **符号说明**
> - $B$：测验划分的题目模块总数（Blocks）。
> - $k$：每套测试卷本中所容纳的题目模块数。
> - $M$：最终装配生成的测试试卷总版本数（Booklets）。
> - $r$：每个题目模块在所有试卷中重复出现的总次数。
> - $\lambda$：任意两个不同题目模块在同一套试卷中两两成对出现的恒定次数。

> [!formula-step] 公式步骤二　位置效应与疲劳校正
> $$P(X_{vij} = 1 \mid \theta_j, b_i, \gamma_p) = \frac{1}{1 + e^{-(\theta_j - b_i - \gamma_p)}}$$
>
> **这个公式在做什么** 在传统题目反应模型中纳入卷本位置衰减参数，剔除后半段作答产生的疲劳效应。
>
> **符号说明**
> - $\gamma_p$：模块处于卷本中第 $p$ 个位置时产生的系统性认知负荷偏差参数（通常后部位置 $\gamma_p < 0$）。

---

> [!method-fit] 适用判断
> - **适合使用**
>   1. **跨国大规模教育评估（[[PISA]]、[[TIMSS]]、[[PIRLS]]）** 必须全面覆盖广阔的学科素养[[Construct|构念]]，但受试学生课堂答题时间严格受限于 2 小时之内。
>   2. **国家级学业质量监测（[[National Assessment of Educational Progress|NAEP]]、中国义务教育质量监测）** 评估省市或学区宏观表现，不要求向个人出具升学高利害成绩单。
>   3. **超大型专业题库标定** 新研发数百道测验试题，需在同一批参考群体中预试标定[[Item Analysis|题目难度]]与区分度参数。
> - **谨慎使用**
>   - [[Sample Size Determination|样本量]]不足以支持稀疏矩阵算法稳定估计的小型区域调查（受试人数少于 1000 人时，各卷本作答人数过少会导致 IRT 参数估计极不稳定）。
> - **不适合使用**
>   - 高利害个人选拔性考试（如中考、[[Gaokao|高考]]、职业资格认证）；由于考生作答题目不同，直接分数的不可比性会严重破坏考试公平性与社会接受度。

---

> [!method-limits] 方法局限与风险
> - **个体分数的完全不可用** 单个学生作答题量过少导致[[Standard Error|标准误]]极大，无法作为个体诊断依据，极易导致公众、家长与一线教师对测验功能的误读。
> - **位置效应与题目上下文干扰** [[Experimental Research|实验研究]]表明，同一模块置于试卷开头与末尾时的通过率存在系统性差异；后置题目受到学生疲劳度、作答动机衰退与猜题策略的显著干扰。
> - **试题长文本情境对模块划分的制约** 具有复杂背景长阅读材料或多步探究任务的试题组难以随意拆解，限制了模块在不同卷本间的自由搭配与重组。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Item Response Theory]] | 方法 | 矩阵抽样下处理非完全重叠作答数据并标定统一参数的核心统计模型。 |
> | [[Plausible Values]] | 方法 | 针对矩阵抽样下个体测量误差问题、用于恢复群体潜在能力无偏分布的技术。 |
> | [[Differential Item Functioning]] | 方法 | 用于检验不同卷本或不同群体间特定题目功能差异的技术。 |
> | [[PISA]] | 事实 | 矩阵抽样技术应用最为广泛的全球标志性教育监测工程。 |
> | [[National Assessment of Educational Progress]] | 事实 | 率先在国家教育评估中系统引入矩阵抽样与群体推断的先驱项目。 |
> | [[Australian Council for Educational Research]] | 事实 | 长期为 PISA 设计平衡不完全区组试卷架构的核心技术承包机构。 |
> | [[Educational Testing Service]] | 事实 | 开创矩阵抽样与似真值[[Imputation Methods\|插补方法]]论体系的专业测量机构。 |
> | [[Argument_Grek_2009_JEdPolicy\|Grek (2009)]] | 论证 | 剖析 PISA 脱离课程体系、依托矩阵抽样与数理建模构建跨国治理权威的文献。 |
> | [[Argument_Morgan_Shahjahan_2014_CE\|Morgan and Shahjahan (2014)]] | 论证 | 剖析[[OECD\|经合组织]]如何将矩阵试卷研发外包给 ACER 并固定技术规程的文献。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Grek_2009_JEdPolicy|Grek (2009)]] — 揭示[[OECD|经合组织]] [[PISA]] 项目如何依托矩阵抽样与高级心理测量模型，将异质教育传统化约为技术上可[[Commensuration|通约]]的群体指标，实现跨国[[Governing at a Distance|远程治理]]。
> - [[Argument_Morgan_Shahjahan_2014_CE|Morgan and Shahjahan (2014)]] — 追踪经合组织如何通过将试题生产与平衡试卷编制外包给专业测量财团，确立国际测评的官僚管理与[[Technical Rationality|技术理性]]威权。
