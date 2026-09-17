---
title: Difference-in-Differences
aliases:
  - 双重差分法
  - DID
  - 双重差分
  - 倍差法
  - Difference in Differences
  - Diff-in-Diff
summary: "一种用于评估公共政策或教育干预因果效应的准实验方法，通过比较处理组与对照组在政策实施前后的双重变化差异，有效消除不随时间变化的时间不变未观测混杂因素。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 34
method_related_level: 4
method_related_stars: "⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/difference-in-differences
  - method/quantitative
  - method/causal-inference
  - method/quasi-experiment
related_concepts:
  - "[[Unit of Analysis]]"
  - "[[Paradigm]]"
  - "[[Epistemology]]"
  - "[[Counterfactual]]"
  - "[[Causality]]"
  - "[[Variable]]"
  - "[[Heterogeneity]]"
  - "[[Hypothesis]]"
  - "[[Dependent Variable]]"
  - "[[Internal Validity]]"
  - "[[Performance Indicators]]"
  - "[[School Choice]]"
  - "[[Reliability]]"
  - "[[Educational Evidence Clearinghouses]]"
  - "[[Document]]"
related_theories: []
related_methods:
  - "[[Random Assignment]]"
  - "[[Standard Error]]"
  - "[[Confidence Interval]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Propensity Score Matching]]"
  - "[[Regression Discontinuity Design]]"
  - "[[Matching]]"
  - "[[Pre-test and Post-test]]"
  - "[[Fixed-Effect and Random-Effects Models]]"
  - "[[Multiple Regression]]"
  - "[[Effect Size]]"
  - "[[Ordinary Least Squares]]"
  - "[[Covariate Adjustment]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[Education Endowment Foundation]]"
  - "[[Researching School Choices]]"
  - "[[National Pupil Database]]"
related_arguments:
  - "[[Argument_Edovald_Nevill_2021_ECNUROE]]"
confidence: high
status: active
created: 2026-09-15
updated: 2026-09-17
---

# Difference-in-Differences

---

## 定义

> [!def] 方法定义
> **双重差分法（Difference-in-Differences，简称 DID）**是计量经济学与实证教育政策研究中最核心的准实验因果识别方法之一。其基本思想是：在缺乏人为[[Random Assignment|随机分配]]的情况下，利用外生政策冲击在时间维度与人群维度的自然差异，分别计算处理组在政策出台前后的纵向变动量，以及对照组在同期内的纵向变动量，进而通过**两次做差（差分的差分）**剥离宏观时间趋势与固有群体差异，识别出政策本身的净因果效应（Net Causal Effect）。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 55–56)]]

> [!method-scope] 方法范围
> - **研究对象** 经历政策冲击或制度改革的学校、学区、地区或学生群体的纵向面板数据（Panel Data）或多时期重复截面数据（Repeated Cross-sections）。
> - **问题类型** 因果效应评估问题（回答“某项宏观结构性政策、办学体制转型或教育经费改革对学生成就平均带来多大净变化”）。
> - **[[Unit of Analysis|分析单位]]** 学生个体、学校、多学院信托（MAT）、学区或地方行政区。
> - **输出形式** 平均处理效应（ATT）、动态事件研究时间路径系数、政策交互项回归估计值 $\beta_{\text{DID}}$ 及其[[Standard Error|标准误]]与[[Confidence Interval|置信区间]]。

> [!citation-card] [[Quasi-Experimental Designs|准实验设计]]与宏观教育政策评估的[[Paradigm|范式]]拓展（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021]]）
> 面对学校宏观办学机制转型等无法强行人为随机化的现实难题，英国 [[Education Endowment Foundation|EEF]] 设立了“[[Researching School Choices|研究学校选择]]”（Researching School Choices）专属资助流。该资助流不再依赖传统 [[Randomised Controlled Trials|RCT]]，而是依托[[National Pupil Database|国家学生数据库]]（NPD）详实的纵向普查大数据，采用双重差分法（DID）、[[Propensity Score Matching|倾向得分匹配]]（PSM）与回归断点设计（[[Regression Discontinuity Design|RDD]]）等严密的准实验架构，科学评估真实教育生态下的宏观治理决策。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 55–56)]]
>
> *“In 2019, the EEF opened the 'Researching School Choices' funding stream... exploiting naturally occurring policy changes and variations using longitudinal data from the National Pupil Database (NPD). Quasi-experimental designs, including difference-in-differences and propensity score [[Matching]], enable rigorous evaluation where randomisation is not feasible.”*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与因果识别定位
> - **知识观** 遵循[[Counterfactual|反事实]][[Causality|因果推断]]框架。认为虽然非实验数据中存在不可忽视的遗漏[[Variable|变量]]偏误，但只要未观测的混杂因素在时间维度上保持恒定（Time-Invariant Unobserved [[Heterogeneity]]），便可通过组间横向差异与组内时间纵向差异的代数正交消除偏误。
> - **核心识别假定** **平行趋势假定（Parallel Trends Assumption）**，即反事实[[Hypothesis|假设]]：在未发生政策干预的情形下，处理组的[[Dependent Variable|结果变量]]将沿着与对照组完全相同的轨迹演进。
> - **有效性标准** [[Internal Validity|内部效度]]取决于平行趋势检验（Pre-trend Testing）与政策外生性；统计推断效度需严谨校正群聚[[Standard Error|标准误]]（Cluster-Robust Standard Errors）。
> - **不声称回答的问题** DID 不能直接消除随时间动态变化的未观测混杂偏误（Time-Varying Confounders），亦不能在缺乏前[[Pre-test and Post-test|后测]]数据的横截面中推断因果。

> [!contrast-table] 因果识别策略对比：DID vs [[Randomised Controlled Trials|RCT]] vs [[Regression Discontinuity Design|RDD]] vs [[Propensity Score Matching|PSM]]
> | 评估方法 | 样本分配机制 | 核心识别假定 | 数据结构要求 | 宏观政策适用性 |
> |---|---|---|---|---|
> | **双重差分法（DID）** | 政策外生冲击或自发选择 | **平行趋势假定**（无随时间变化的未观测干扰） | 至少两期前后面板或重复截面 | **极高**（最适合评估全校改革、拨款调整等自然政策） |
> | **随机对照试验（RCT）** | 研究者人为[[Random Assignment\|随机分配]] | 初始完全无偏可比性 | 实验前后测 | 较低（宏观体制与重大组织选择难以人为强行[[Random Assignment\|随机化]]） |
> | **回归断点设计（RDD）** | 连续运行变量阈值切分 | 阈值附近局部随机性（连续性假定） | 连续变量与跨阈值数据 | 中等（严格受限于是否存在刚性分流分界线） |
> | **倾向得分匹配（PSM）** | 可观测变量匹配 | 条件独立性（无任何未观测混杂） | 截面或面板丰富协变量 | 中等（无法解决不可观测的动机与学校文化偏误） |

> [!method-stack] 方法层级
> - **研究设计** 自然实验（Natural Experiments）、[[Quasi-Experimental Designs|准实验设计]]（[[Quasi-Experimental Designs|QED]]）、多期交错采纳设计（Staggered Adoption Design）。
> - **数据收集** 行政普查大数据（如英国[[National Pupil Database|国家学生数据库]]）、学校历年督导报告、区域长期学业追踪数据。
> - **分析方法** 双向[[Fixed-Effect and Random-Effects Models|固定效应模型]]（TWFE）、事件研究法（Event Study）、合成双重差分（Synthetic DID）、群组聚合估计（Callaway & Sant'Anna, 2021）。
> - **辅助技术** 安慰剂检验（Placebo Test）、反事实合成匹配、组聚标准误调整（Wild Cluster Bootstrap）。

---

## 研究程序

> [!proc] 通用程序
> 1. **界定政策冲击与组别边界** 明确政策发布的具体时间节点（或不同学校分批采纳的时间表），清晰界定受政策影响的处理组与未受影响的潜在对照组。
> 2. **组建纵向长面板数据库** 链接政策出台前若干年（建议至少 3 期以上）与出台后的微观学业产出及学校控制[[Variable|变量]]。
> 3. **前置平行趋势检验（事前动态分析）** 运用事件研究法估计政策实施前各期的动态交互项，检验事前趋势是否在统计上不显著异于零。
> 4. **拟合双向固定效应双重差分模型** 纳入个体/学校固定效应与时间固定效应，加入时变协变量矩阵，估计政策净因果效应 $\beta_{\text{DID}}$。
> 5. **稳健性与[[Heterogeneity|异质性]]诊断** 执行安慰剂政策时间检验、伪处理组伪造检验，并针对多时期交错实施检查负权重与异质性处理效应偏误。

### 量化分析模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 包含 $i$ 个个体（或学校）在 $t$ 个时间周期的平衡或非平衡面板数据。
> - **核心变量**
>   - 产出变量 $Y_{it}$：学校或学生层面的标准化考试成绩、出勤率或全纳[[Performance Indicators|教育指标]]。
>   - 处理状态变量 $T_i$：个体是否属于处理组（1 = 处理组，0 = 对照组）。
>   - 时期虚拟变量 $\text{Post}_t$：政策冲击前后（1 = 实施后，0 = 实施前）。
>   - 政策交互变量 $D_{it} = T_i \times \text{Post}_t$：当个体属于处理组且处于政策实施期时取值为 1，否则为 0。
>   - 控制变量 $\mathbf{X}_{it}$：随时变化的学童背景、学校生源构成及师资流动特征。

> [!formula-step] 公式步骤　标准 2x2 双重差分模型
> $$\beta_{\text{DID}} = (\bar{Y}_{T,\text{post}} - \bar{Y}_{T,\text{pre}}) - (\bar{Y}_{C,\text{post}} - \bar{Y}_{C,\text{pre}})$$
>
> **这个公式在做什么** 计算处理组从政策实施前到实施后的平均变化幅度，并从中减去对照组在同一时期内的平均变化幅度，双重剥离初始差距与自然演进趋势。
>
> **符号说明**
> - $\bar{Y}_{T,\text{post}}, \bar{Y}_{T,\text{pre}}$：处理组在政策出台后与出台前的均值产出。
> - $\bar{Y}_{C,\text{post}}, \bar{Y}_{C,\text{pre}}$：对照组在政策出台后与出台前的均值产出。
> - $\beta_{\text{DID}}$：标准双重差分因果估计量。
>
> **数学直觉** [[Hypothesis|假设]]处理组的变化包含“政策真实效应 + 时间演进趋势”，而对照组的变化仅包含“时间演进趋势”。在平行趋势成立的条件下，两者相减即完全抵消了共有时间趋势，提纯出纯粹由政策带来的增量。
>
> **结果怎么读** $\beta_{\text{DID}} > 0$ 表明政策使处理组取得了超越常规自然趋势的净正向产出；若接近 0 则表明两组的变化步调与未受干预的基线完全一致。
>
> **注意事项** 必须确保对照组在干预期间未受到其他具有排他性外生冲击的干扰。

> [!formula-step] 公式步骤　双向固定效应面板回归模型（TWFE）
> $$Y_{it} = \alpha_i + \lambda_t + \beta_{\text{DID}} D_{it} + \mathbf{X}_{it}' \boldsymbol{\gamma} + \varepsilon_{it}$$
>
> **这个公式在做什么** 在多时期面板数据中，通过控制个体固定效应 $\alpha_i$（吸收所有不随时间变化的主体特征）与时间固定效应 $\lambda_t$（吸收所有影响所有个体的同期宏观冲击），以政策暴露哑变量 $D_{it}$ 的回归系数估计平均处理效应。
>
> **符号说明**
> - $\alpha_i$：个体或学校固定效应，消除固有的生源基础、地理区位与历史校风等恒定偏误。
> - $\lambda_t$：时间固定效应，消除统考难度波动、国家宏观通胀等全系统共有时间效应。
> - $D_{it}$：政策指示变量（处理组且进入政策期时为 1，否则为 0）。
> - $\boldsymbol{\gamma}$：时变控制变量系数向量。
>
> **数学直觉** TWFE 是 2x2 DID 在[[Multiple Regression|多元回归]]框架下的标准推广，能够灵活引入个体层面的动态协变量，同时通过在学校层面聚类[[Standard Error|标准误]]（Cluster at School Level）克服面板自相关问题。
>
> **注意事项** 近年方法学研究（Goodman-Bacon, 2021; Sun & Abraham, 2021）证实：当不同样本在不同时期交错进入政策（Staggered Rollout）且处理效应存在异质性时，TWFE 估计量可能赋予部分组别负权重，从而产生严重偏误。在此情形下需采用 Callaway & Sant'Anna (2021) 等异质性稳健估计量。

> [!software-impl] 软件实现
> - **推荐软件** R (`fixest`, `did`), Stata (`reghdfe`, `csdid`), Python (`linearmodels`).
> - **实现流程**
>   1. 数据准备：构建包含个体 `id`、年份 `year`、处理标识 `treat`、政策期 `post` 的平衡面板。
>   2. 标准 TWFE 估计：
>      - Stata: `reghdfe score i.treat##i.post covars, absorb(school_id year) vce(cluster school_id)`
>      - R: `feols(score ~ i(treat, post, ref = 0) + covars | school_id + year, cluster = ~school_id, data = df)`
>   3. 动态事件研究法（平行趋势检验）：
>      - R: `feols(score ~ i(event_time, treat, ref = -1) + covars | school_id + year, cluster = ~school_id, data = df)`
> - **报告标准** 必须报告政策前至少 3 期动态系数图、平行趋势 $F$ 检验 $p$ 值、聚类群组数与主效应[[Confidence Interval|置信区间]]。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**
>   - 宏观体制与办学机制变革（如英格兰学校转制为多学院信托 MAT、公立学校特许化改革）；
>   - 区域性或全国分批落地的重大教育财政、生均拨款调整（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021]]）；
>   - 无法实施人为[[Random Assignment|随机分配]]，但能获取国家级纵向普查面板大数据的评估课题。
> - **谨慎使用**
>   - 政策出台前两组已呈现显著发散趋势的研究（严重违反平行趋势假定）；
>   - 样本出现大规模跨组流动、学生跨区[[School Choice|择校]]逃离处理组的情形（构成严重的成分变动偏误）。
> - **不适合使用**
>   - 仅有单一年份横截面截面数据；
>   - 政策实施覆盖率达到 100% 且全系统在同一瞬间完全暴露、没有任何未受影响对照组的全国性法定考试改革。

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源**
>   - **时变未观测混杂（Time-Varying Confounders）** 若处理组在政策落地的同时遭遇了其他未被观测到的外部扶持或生源变动，DID 会将此额外冲击误判为政策效应。
>   - **交错实施负权重偏误（Negative Weighting Bias）** 在交错 DID 中，较早接受处理的样本可能被作为后续处理样本的对照组，若处理效应随时间动态递增，会导致估计值符号反转。
> - **适用边界** 结论依赖于平行趋势假定的[[Counterfactual|反事实]]可[[Reliability|信度]]，且识别出的[[Effect Size|效应量]]通常是局部平均处理效应。
> - **误用风险** 忽视事前趋势发散而强行汇报 TWFE 回归系数；或忽视序列自相关导致[[Standard Error|标准误]]严重低估。
> - **补救方式** 绘制事件研究动态路径图；采用最新的[[Heterogeneity|异质性]]稳健估计量（如 Callaway & Sant'Anna 方法）；联合[[Propensity Score Matching|倾向得分匹配]]构建匹配双重差分（PSM-DID）。

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] [[Random Assignment|随机分配]]纯粹性 vs 准实验田野真实性
> > [[Educational Evidence Clearinghouses|证据清算中心]]与循证资助者对 DID 证据等级的定位争辩。
> >
> > - **实验至上派观点** 严格认为准实验始终建立在不可验证的平行趋势[[Hypothesis|假设]]之上，任何微小的时变遗漏[[Variable|变量]]都会摧毁[[Causality|因果性]]，因此在挂锁评级中通常只赋予中等信用（3 把锁上限）。
> > - **田野决策派抗辩** 现实世界中绝大多数重大战略决策（如学区兼并、校长负责制、学费减免）根本不可能进行人为随机试验。[[Education Endowment Foundation|EEF]] 创立“[[Researching School Choices|研究学校选择]]”资助流，正是承认 DID 等准实验是连接循证科学与真实宏观教育决策的生命线（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021]]）。
>
> > [!axis] 传统面板 TWFE vs [[Heterogeneity|异质性]]稳健估计革命
> > 近年来计量经济学界对过去几十年发表的交错 DID [[Document|文献]]的系统反思。
> >
> > - **传统回归习惯** 研究者习惯简单运行含双向固定效应的 [[Ordinary Least Squares|OLS]] 交互项回归。
> > - **新计量[[Paradigm|范式]]确立** 学界已达成共识：在交错落地政策中必须弃用传统 TWFE，全面转向异质性稳健估计量以根除负权重风险。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Quasi-Experimental Designs]] | 上位分类 | DID 所属的核心[[Causality\|因果推断]]准实验设计框架。 |
> | [[Propensity Score Matching]] | 互补方法 | 常与 DID 组合构成 PSM-DID，通过匹配改善处理组与对照组基线平行性。 |
> | [[Regression Discontinuity Design]] | 替代方法 | 当存在明确准入切分点时适用的另一种高[[Internal Validity\|内部效度]]准实验方法。 |
> | [[Randomised Controlled Trials]] | 参照[[Paradigm\|范式]] | 因果识别的黄金标准，DID 是在 RCT 无法实施时的首选替代方案。 |
> | [[Fixed-Effect and Random-Effects Models]] | 计量基础 | TWFE 面板回归为 DID 提供了参数化估计与[[Covariate Adjustment\|协变量控制]]的统计支架。 |
> | [[National Pupil Database]] | 数据基础 | 英国支撑长周期 DID 政策评估的国家级微观行政纵向普查库。 |
> | [[Researching School Choices]] | 实践载体 | [[Education Endowment Foundation\|EEF]] 设立的依托 DID 等准实验评估宏观学校办学决策的重大资助流。 |

---

## 使用此方法的研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill (2021)]] — 详述了英国 [[Education Endowment Foundation|EEF]] 突破对单一 [[Randomised Controlled Trials|RCT]] 的教条依赖，设立“[[Researching School Choices|研究学校选择]]”资助流，依托[[National Pupil Database|国家学生数据库]]运用双重差分法与[[Propensity Score Matching|倾向得分匹配]]评估学校宏观体制选择的因果成效。
