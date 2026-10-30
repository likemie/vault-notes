---
title: Random Sampling
aliases:
  - 随机抽样
  - probability sampling
  - 概率抽样
  - random sample
  - 随机样本
  - simple random sampling
  - 简单随机抽样
summary: "从研究总体中按非零且已知概率选取样本单元的方法论策略家族，通过消除主观选择偏倚确保样本对总体的统计代表性，包括简单随机、系统、分层、整群与多阶段抽样；在国家治理中天然支持低利害系统诊断，与高利害全员普查测评形成鲜明功能边界"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 43
method_related_level: 4
method_related_stars: "💎⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/sampling
  - quantitative-research
  - survey
related_concepts:
  - "[[External Validity]]"
  - "[[Study Population and Sample]]"
  - "[[Unit of Analysis]]"
  - "[[Sampling Error]]"
  - "[[Epistemology]]"
  - "[[Causality]]"
  - "[[Counterfactual]]"
  - "[[Internal Validity]]"
  - "[[Clinical Trial]]"
  - "[[National Large-Scale Assessments]]"
  - "[[Response Bias]]"
  - "[[Variable]]"
  - "[[Heterogeneity]]"
  - "[[Reliability]]"
  - "[[Document]]"
  - "[[Global Universities Rankings]]"
  - "[[Performance Pay]]"
  - "[[New Public Management]]"
  - "[[School Choice]]"
  - "[[Institutional Layering]]"
  - "[[Test-Based Accountability]]"
related_theories:
  - "[[Central Limit Theorem]]"
related_methods:
  - "[[Random Assignment]]"
  - "[[Sampling Frame]]"
  - "[[Confidence Interval]]"
  - "[[Standard Error]]"
  - "[[Survey Research]]"
  - "[[Cluster Sampling]]"
  - "[[Stage Sampling]]"
  - "[[Systematic Sampling]]"
  - "[[Stratified Sampling]]"
  - "[[Sample Size Determination]]"
  - "[[Questionnaire]]"
  - "[[Multi-phase Sampling]]"
  - "[[Cross-sectional Study]]"
  - "[[Intraclass Correlation Coefficient]]"
  - "[[Pilot Testing]]"
related_persons: []
related_facts:
  - "[[PISA]]"
  - "[[TIMSS]]"
  - "[[Schools for Migrant Children]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]]"
  - "[[Argument_Verger_2019_Discourse]]"
confidence: medium
status: draft
created: 2026-06-01
updated: 2026-10-30
---

---

> [!def] Random Sampling
> 随机抽样（Random Sampling），亦称概率抽样（Probability Sampling），指从明确界定的研究总体中，依据已知的非零概率（在简单随机抽样中为均等概率）抽取样本单元的方法论策略家族。核心目标是通过概率[[Random Assignment|随机化]]机制消除抽样过程中的主观选择偏倚，使样本统计量能够以可计算的误差范围无偏推断总体参数，确立研究的[[External Validity|外部效度]]（[[Argument_Cohen_Manion_Morrison_2011_Routledge|Cohen et al., 2011]], Ch8, pp. 143–145）。

> [!method-scope] 方法范围
> - **研究对象** 具备完整或可构建[[Sampling Frame|抽样框]]的[[Study Population and Sample|目标总体]]（如特定学段的学生、教师、学校或学区）。
> - **问题类型** 适合回答横截面总体参数估计、学业发展现状描述、跨群体均衡度比较及教育系统宏观监测问题。
> - **[[Unit of Analysis|分析单位]]** 个体学生、教师、班级、学校、行政学区或地域集群。
> - **输出形式** 概率样本数据矩阵、点估计值与[[Confidence Interval|置信区间]]、[[Sampling Error|抽样误差]]界限及基于复杂抽样设计的加权统计量。

> [!citation-card] [[Argument_Cohen_Manion_Morrison_2011_Routledge|Cohen et al. (2011)]] 论概率抽样的统计代表性
> 在概率抽样中，总体中的每个成员都有已知的被选中概率，抽样选择完全不受研究者主观偏好的干扰，从而支持研究者以预定的精确度从样本推断总体的真实参数。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, Ch8, pp. 143–144)]]
>
> *In probability sampling, each member of the population has an equal or known probability of selection. This randomness allows the researcher to make statistically valid inferences from the sample to the broader population.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 依托大数定律（Law of Large Numbers）与[[Central Limit Theorem|中心极限定理]]（Central Limit Theorem），坚持经验知识的统计可推论性；主张通过规范的概率机制消除抽样偏倚，实现从样本到总体的科学推断。
> - **研究者角色** 严谨的算法执行者与误差核算员。严格依循数学随机程序，杜绝任何主观偏好与便利选样干预。
> - **有效性标准** 抽样框完备度、样本对总体的结构代表性、[[External Validity|外部效度]]、可计算的抽样[[Standard Error|标准误]]以及无应答偏倚的控制水平。
> - **不声称回答的问题** 随机抽样仅保障样本对总体的统计代表性，不能单独回答因果机制问题（[[Causality|因果推断]]需要依托研究设计本身的实验控制或[[Counterfactual|反事实]]构建）；在政策问责中，基于样本的抽样监测无法直接输出针对单一学校或具体教师的微观绩效评定。

> [!contrast-table] 随机抽样 vs 随机分配
> | 比较维度 | 随机抽样（Random Sampling） | [[Random Assignment\|随机分配]]（Random Assignment） |
> |---|---|---|
> | **核心关切** | **谁**被选入样本研究（选样阶段） | 已进入样本的被试**如何**分配至各实验组（分配阶段） |
> | **效度目标** | 确保样本向总体的统计推广力（[[External Validity\|外部效度]]） | 消除组间系统性混淆变量，确立因果推断（[[Internal Validity\|内部效度]]） |
> | **独立性** | 可独立应用于[[Survey Research\|调查研究]]与宏观监测 | 可独立应用于实验室实验或真实情境[[Clinical Trial\|临床试验]] |

> [!method-stack] 方法层级
> - **研究设计** 抽样调查研究设计、国家大尺度测评（[[National Large-Scale Assessments]], NLSA）抽样监测、横截面与纵向追踪调查。
> - **数据收集** 基于电子学籍库或组织名册的随机选样、分层多阶段[[Cluster Sampling|整群抽样]]（如[[PISA|国际学生评估项目]] PISA 的两[[Stage Sampling|阶段抽样]]）。
> - **分析方法** 加权参数估计、复杂抽样方差校准（泰勒级数线性化、刀切法 Jackknife、平衡半样本法 BRR）。
> - **辅助技术** 伪随机数生成算法、抽样框加权平滑技术、无应答逆概率加权（Inverse Probability Weighting, IPW）与事后分层调整。

---

> [!proc] 通用程序
> 1. **明确目标总体与编纂抽样框** 精确定义研究对象的范围与边界，获取或整理包含全体单位的完整[[Sampling Frame|抽样框]]名录。
> 2. **确定概率抽样策略** 依据研究目标与总体分布结构，选择简单随机抽样、[[Systematic Sampling|系统抽样]]、[[Stratified Sampling|分层抽样]]、整群抽样或多阶混合设计。
> 3. **计算目标[[Sample Size Determination|样本量]]** 根据预设的置信水平（如 95%）、容许误差界限（Margin of Error）以及方差参数，结合有限总体修正公式测算理论样本量。
> 4. **运行随机抽取程序** 设定算法随机种子，生成抽样随机数并导出入选名单，锁定抽样凭据以便审计核查。
> 5. **追踪应答并执行加权校准** 统计实际[[Questionnaire|问卷]]回收率与测试参与率，开展[[Response Bias|应答偏差]]分析，运用设计权重与事后分层权重修正估计量。

> [!taxonomy] 概率抽样六种核心类型
>
> | 类型 | 英文 | 核心机制与特征 | 典型适用场景 |
> |---|---|---|---|
> | 简单随机抽样 | Simple Random Sampling | 每个总体成员享有均等、独立的被选入机会；依赖完整详尽名单 | 总体规模有限且分布集中、具备完整抽样框的小规模研究 |
> | [[Systematic Sampling\|系统抽样]] | Systematic Sampling | 随机确定起始点，按照固定间隔（$k = N/n$）等距抽取 | 具备名录清单且数据排列无周期性波动的流水式连续抽样 |
> | [[Stratified Sampling\|随机分层抽样]] | Stratified Sampling | 先按关键[[Variable\|变量]]（如城乡、公私立）分层，再在层内执行独立随机抽样 | 总体[[Heterogeneity\|异质性]]高、需确保少数边缘子群具备统计分析代表性 |
> | [[Cluster Sampling\|整群抽样]] | Cluster Sampling | 随机抽取自然群组（如学校、村落），调查群内所有最终单元 | 总体地域辽阔分散、缺乏个体名单但具备集群名录的大规模调查 |
> | [[Stage Sampling\|阶段抽样]] | Stage Sampling | 逐级分层抽取集群，并在最后一级抽取样本个体（多级随机化） | 教育系统嵌套结构（先抽区县、再抽学校、最终抽选班级或学生） |
> | [[Multi-phase Sampling\|多阶段抽样]] | Multi-phase Sampling | 在大样本中收集基础信息，随后在子样本中跟进采集深度指标 | 需要分层次开展深度测试或后续定点追踪的复杂混合调查 |

> [!method-stack] 数据、变量与模型
> - **数据结构** 包含分层标识、集群编号与个体抽样权重的层次化[[Cross-sectional Study|横截面调查]]数据库。
> - **样本与单位** 目标总体规模 $N$、实际样本量 $n$；初级抽样单位（PSU，如学校）与终极抽样单位（SSU，如学生）。
> - **核心变量** 抽样权重（设计权重、无应答调整权重、校准权重）与目标测验学业得分。
> - **诊断与检验** 抽样框覆盖误差检验、[[Intraclass Correlation Coefficient|群内相关系数]]（Intraclass Correlation Coefficient, ICC）测定与设计效应（Design Effect, DEFF）评估。

> [!formula-step] 公式步骤 均值估计的简单随机抽样样本量计算
> $$n = \frac{z^2 \sigma^2}{e^2}$$
>
> **这个公式在做什么** 计算在指定置信水平与容许误差下，准确估计总体均值所需的最小样本量。
>
> **符号说明**
> - $n$：计算得出的理论样本量。
> - $z$：对应选定置[[Reliability|信度]]（如 95% 置信度对应 $z = 1.96$）的标准正态分布临界值。
> - $\sigma$：目标指标在总体中的标准差（通常由[[Pilot Testing|预实验]]或既往[[Document|文献]]估算）。
> - $e$：研究者能够容忍的最大允许抽样误差绝对值。
>
> **数学直觉** 样本量与置信度平方和总体方差成正比，与允许误差的平方成反比；总体离散程度越高或要求的测量精度越严格，所需采集的样本量呈二次方增长。
>
> **结果怎么读** 算出的数值代表无偏推断所需的样本底线；若总体规模有限，可结合公式 $n_{adj} = \frac{n}{1 + (n-1)/N}$ 进行有限总体修正以削减冗余样本。
>
> **注意事项** 该公式假定简单随机抽样；若采用整群抽样，实际样本量必须乘以设计效应系数 $DEFF = 1 + (m-1)\rho$（$m$ 为群规模，$\rho$ 为群内相关系数），以对冲样本同质性带来的统计功效损耗。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, Ch8, p. 145)]]

> [!software-impl] 软件实现
> - **数据处理** 检查抽样框唯一标识码，剔除重复记录，按分层变量排序并计算抽样概率。
> - **推荐软件** R（`survey`、`sampling` 包）、Stata（`svyset` 模块）、Python（`statsmodels`、`scipy`）。
> - **核心命令** R 中使用 `sampling::strata()` 实施分层抽样，利用 `survey::svydesign(ids=~cluster, strata=~strata, weights=~weight, data=data)` 声明复杂抽样设计。
> - **报告标准** 完整披露抽样框来源、抽样阶段与层级结构、无应答率、设计效应值及加权后置信区间。

---

> [!method-fit] 适用判断
> - **适合使用** 
>   - 国家或国际层面的教育系统宏观监测（如 PISA、[[TIMSS]]、国家义务教育质量监测），通过代表性抽样识别区域与群体学业趋势；
>   - 具备清晰权威名单库（如学籍系统、高校教职工名录）的实证调查研究；
>   - **低利害系统诊断治理** [[Argument_Verger_2019_Discourse|Verger et al. (2019, p. 251)]] 指出，随机抽样评估适合充当国家教育系统的低利害诊断工具，通过监测宏观学业趋势帮助政策制定者识别薄弱环节并提供定向资源支持，同时天然阻断了向单一学校施加惩戒的可能。
> - **谨慎使用** 
>   - 抽样框存在严重信息滞后、漏登或重复记录时，必须先行执行清洗与覆盖率修正；
>   - 面对高拒访率的高利害敏感议题，若回收率低于 60%，样本代表性将遭受无应答偏倚破坏。
> - **不适合使用** 
>   - **微观高利害绩效问责** 当治理目标是对全量学校编制公开排位榜（[[Global Universities Rankings|League Tables]]）、挂钩校长撤职或实施教师[[Performance Pay|绩效工资]]奖惩时，随机抽样评估在制度上完全无法适用；高利害市场问责必须依托覆盖全量主体的全员普查（Census-based NLSA），抽样评估由于未覆盖全部学校，在法律与操作层面均无法用于个体奖惩。[[Argument_Verger_2019_Discourse|(Verger et al., 2019, pp. 251, 263)]]

---

> [!method-limits] 方法局限
> - **抽样框依赖与覆盖偏倚** 现实中极难构建绝对无缝的目标总体名册；边缘弱势人群（如流浪儿童、私立[[Schools for Migrant Children|打工子弟学校]]）常被正规抽样框遗漏，导致结构性系统偏差。
> - **无应答偏倚侵蚀** 即使初始抽样严格随机，后续高达 30%–50% 的拒答或失访往往具有非随机性特征，破坏最终有效样本的代表性。
> - **复杂抽样的精度损耗** 为兼顾实地考察成本而采用的整群抽样，群内成员的高度同质性会导致有效信息量缩水，产生显著的设计效应膨胀。
> - **政策治理维度的功能局限与普查挤压** Verger et al. (2019, pp. 251, 263) 揭示了抽样测评在教育治理演变中的结构性困境：随机抽样评估无法提供针对单一学校的高精度可比数据，无法满足[[New Public Management|新公共管理]]体制下家长[[School Choice|择校]]、市场竞争与优胜劣汰的要求；随着问责利害加码，许多国家经历[[Institutional Layering|制度分层]]，引入全员普查测评（Census-based assessments）补充或直接取代抽样测评，导致原本定位于系统改进与专业支持的抽样监测体系遭受边缘化或挤压。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Sampling Frame]] | 前置构件 | 实施概率抽样的物理前提，其完备度直接决定抽样质量。 |
> | [[Random Assignment]] | 辨析方法 | 随机抽样保障外部效度，随机分配保障因果识别的内部效度。 |
> | [[Stratified Sampling]] | 衍生子类 | 随机抽样家族中用于降低层内方差、保障子群体代表性的核心技术。 |
> | [[Cluster Sampling]] | 衍生子类 | 随机抽样家族中适应教育嵌套组织特征、降低跨地域调研成本的实用方法。 |
> | [[National Large-Scale Assessments]] | 应用场景 | 随机抽样在大尺度教育测评中用于国家系统诊断的核心载体。 |
> | [[Test-Based Accountability]] | 政策背景 | 考试问责强化驱动全员普查测评扩展，与抽样监测的低利害属性形成张力。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen, Manion and Morrison (2011, Ch8)]] — 系统介绍概率抽样的六大子类型、抽样框构建、样本量计算准则与偏倚风险控制。（pp. 143–155）
> - [[Argument_Verger_2019_Discourse|Verger et al. (2019)]] — 辨析国家大尺度测评中随机抽样监测与全员普查测评的治理功能分野，揭示抽样评估天然支持低利害系统诊断、而无法直接用于高利害市场问责与排位奖惩的制度边界。（pp. 250–252, 263）
