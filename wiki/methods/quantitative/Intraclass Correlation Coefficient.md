---
title: Intraclass Correlation Coefficient
aliases:
  - 组内相关系数
  - 校正组内相关系数
  - 群内相关系数
  - ICC
  - Intra-class Correlation
  - Intraclass Correlation
summary: "用于度量多层嵌套或集群数据中同组观测值之间相似程度的统计量，表示总变异中可归因于群间差异的比例，是整群试验设计效应评估、有效样本量换算与聚类标准误校正的核心参数。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 8
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - method/statistical
  - method/multilevel
  - method/cluster-rct
related_concepts:
  - "[[Effective Sample Size]]"
related_theories: []
related_methods:
  - "[[Hierarchical Linear Model]]"
  - "[[Cluster Randomized Trials]]"
  - "[[Generalized Estimating Equations]]"
  - "[[Ordinary Least Squares]]"
  - "[[Standard Error]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Edovald_Nevill_2021_ROE]]"
  - "[[Argument_Wadhwa_2024_RER]]"
confidence: high
status: active
created: 2026-09-15
updated: 2026-09-15
---

# Intraclass Correlation Coefficient

---

## 定义

> [!def] 方法定义
> **组内相关系数（Intraclass Correlation Coefficient，简称 ICC，在符号中常记为 $\rho$）**最初由统计学家罗纳德·费希尔（Ronald Fisher）于 1925 年在方差分析框架下提出，是衡量具有嵌套（Nested）或群聚（Clustered）结构数据中**同属于同一群组的个体之间相似程度**的核心统计量。在现代分层线性多水平模型（[[Hierarchical Linear Model|HLM]]）中，ICC 被严格定义为**高层级组间方差占总方差的比例**。在教育实证研究与集群随机对照试验（[[Cluster Randomized Trials|Cluster RCT]]）中，ICC 捕捉了同校或同班学生因共享教师、校园文化、地理社区及同伴互动而产生的非独立性相关，是测算设计效应（Design Effect）、换算有效样本量以及消除标准误向下偏倚的生命线参数。[[Argument_Edovald_Nevill_2021_ROE|(Edovald & Nevill, 2021, pp. 52–53)]]; [[Argument_Wadhwa_2024_RER|(Wadhwa et al., 2024, pp. 8–10)]]

> [!method-scope] 方法范围
> - **研究对象** 分层嵌套于学校、班级、学区、家庭或研究机构内部的个体学业成绩、心理测量得分或行为观察数据；亦用于评估多名评分者之间的跨评价者一致性（Inter-rater Reliability）。
> - **问题类型** 数据群聚性诊断（回答“数据是否必须使用多层模型”）、试验样本量与统计功效前置规划、集群随机试验聚类标准误校正。
> - **分析单位** 包含微观个体（Level 1）与宏观集群（Level 2）的多层级系统。
> - **输出形式** ICC 点估计值（介于 0 到 1 之间）、基于 $F$ 分布或似然比检验的显著性 $p$ 值、设计效应（Design Effect）及修正有效样本量。

> [!citation-card] 组内相关系数校正在教育试验审查中的刚性门槛（Edovald & Nevill, 2021; Wadhwa et al., 2024）
> 在国际教育证据清算中心（如美国 WWC 与英国 EEF）的证据安全评级中，未校正组内相关系数（ICC）被确立为导致试验降级的致命缺陷。教育现场中随机化往往发生在学校层面，若不校正学校间 ICC（英国中小学校际考分 ICC 通常介于 0.10 至 0.20 之间），常规统计模型会将同校学生的共有变异错误视作独立观察自由度，导致标准误被系统性低估 30%–60%，制造大量的伪阳性虚假显著性。杜伦大学对 17 项 EEF 试验的二次复算推动英国全面确立了《EEF 评估统计分析指南》（*Statistical Analysis Guidance for EEF Evaluations*; The EEF, 2018），强制要求所有整群试验主效应分析必须显式建模 ICC 并校正聚类标准误。[[Argument_Edovald_Nevill_2021_ROE|(Edovald & Nevill, 2021, pp. 52–53)]]; [[Argument_Wadhwa_2024_RER|(Wadhwa et al., 2024, pp. 8–10)]]
>
> *“In education trials, pupils are clustered in classes and schools. If an analysis ignores this clustering, the effective sample size is exaggerated and the standard error is underestimated. Adjusting for the intraclass correlation coefficient is mandatory to prevent spurious statistical significance.”*

---

## 方法定位

> [!method-position] 认识论与方法定位
> - **知识观** 承认测量单位与分析单位错位（Unit of Analysis Misalignment）带来的推断风险。个体表现永远嵌于环境脉络之中，忽视群聚相关性在认识论上属于典型的生态学谬误或原子论谬误。
> - **统计功能二重性**
>   1. **作为依赖性度量** 在模型构建前作为“门禁指标”（Gatekeeper），判定群聚结构是否不可忽略（当 $\text{ICC} > 0.05$ 时，强行使用平面 OLS 会导致严重的统计结论效度危机）；
>   2. **作为功效校正系数** 在试验规划阶段通过设计效应膨胀因子直接放大所需样本量。
> - **有效性标准** ICC 的精确估计依赖于空模型（Null Model）的未受干扰性；点估计的稳定性强烈依赖于二级集群数量（学校数 $J$）。
> - **不声称回答的问题** ICC 本身不是因果效应量，不反映干预对个体的净增益，仅描述总变异的层级结构分布。

> [!contrast-table] ICC 在不同应用场景中的类型与含义对比
> | 应用场景 | 方差分解结构 | 计算公式重点 | 核心关注目的 | 典型应用范例 |
> |---|---|---|---|---|
> | **教育整群试验（Cluster RCT）** | 学校间随机截距方差 vs 学生内残差 | $\text{ICC} = \frac{\tau_{00}}{\tau_{00} + \sigma^2}$ | 评估校内同质性、计算设计效应与校正标准误 | 评估全校教学改革试验中的考分变异 |
> | **跨期重复测量（Longitudinal）** | 个体间稳定方差 vs 时间点内残差 | $\text{ICC} = \frac{\sigma_{\text{between-person}}^2}{\sigma_{\text{total}}^2}$ | 评估特质跨时间演进的稳定性与重测信度 | 跟踪学生多年认知能力演进的个体特质占比 |
> | **评分者一致性（Inter-rater）** | 评分客体间方差 vs 评分者偏差及误差 | Shrout & Fleiss (1979) 六种模型（如 ICC(2,1)） | 检验多位主观打分专家评价标准的一致性与绝对一致度 | 课堂教学观察量表教师评分信度检验 |

> [!method-stack] 方法层级
> - **研究设计** 集群随机对照试验（Cluster RCT）、多阶段分层整群抽样、纵向生长模型。
> - **数据收集** 行政考分普查数据（NPD）、大样本心理测验、结构化课堂观察评分。
> - **分析方法** 单因素随机效应方差分析（ANOVA Random Effects）、限制性极大似然法（REML）两层空模型。
> - **辅助技术** 设计效应（Design Effect）公式换算、有效样本量折算、小集群小样本置信区间构建。

---

## 研究程序

> [!proc] 通用程序
> 1. **构建两层无条件空模型（Unconditional Null Model）** 不纳入任何自变量与控制变量，仅将因变量按学校/班级层级进行自由分解。
> 2. **提取方差分量参数** 采用限制性极大似然（REML）估计获取 Level 2 截距方差 $\tau_{00}$（组间变异）与 Level 1 残差方差 $\sigma^2$（组内变异）。
> 3. **计算 ICC 点估计量** 计算 $\rho = \frac{\tau_{00}}{\tau_{00} + \sigma^2}$。
> 4. **检验组间方差统计显著性** 执行似然比检验（Likelihood Ratio Test, LRT）比较单层模型与两层模型的拟合优度，确认 ICC 是否显著大于零。
> 5. **换算设计效应与有效样本量** 结合平均集群规模 $m$，测定设计效应 $\text{Deff} = 1 + (m - 1)\rho$，评估研究的真实有效信息量。

### 量化分析模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 包含 $J$ 个独立集群（如学校），第 $j$ 所学校包含 $n_j$ 名个体，平均集群规模 $m = \frac{1}{J}\sum n_j$。
> - **核心变量**
>   - 产出变量 $Y_{ij}$：第 $j$ 所学校第 $i$ 名学生的后测标准化成绩。
>   - 集群标识符 $\text{ClusterID}_j$：学校或班级的唯一分类编码。
> - **诊断与检验** 集群规模变异系数（CV of Cluster Size）检验、极端异常集群影响诊断。

> [!formula-step] 公式步骤　空模型方差分解与 ICC 定义式
> $$Y_{ij} = \gamma_{00} + u_{0j} + \varepsilon_{ij}$$
>
> $$\text{其中 } u_{0j} \sim N(0, \tau_{00}), \quad \varepsilon_{ij} \sim N(0, \sigma^2)$$
>
> $$\text{ICC} = \rho = \frac{\tau_{00}}{\tau_{00} + \sigma^2}$$
>
> **这个公式在做什么** 在不控制任何自变量的情形下，将因变量的总变异精确剥离为两部分：学校间的宏观固有差距（$\tau_{00}$）与学校内部学生之间的微观个体差距（$\sigma^2$），并计算组间方差占总方差的相对比例。
>
> **符号说明**
> - $Y_{ij}$：第 $j$ 所学校第 $i$ 名学生的测量值。
> - $\gamma_{00}$：所有样本的总体平均基线。
> - $u_{0j}$：第 $j$ 所学校偏离总体平均水平的随机截距效应。
> - $\tau_{00}$：学校水平随机截距的方差（Between-Cluster Variance）。
> - $\sigma^2$：学生水平随机扰动的方差（Within-Cluster Residual Variance）。
>
> **数学直觉** 若所有学校的办学水平完全均质，学生考分的差异全部来自学生天资不同，则 $\tau_{00} = 0$，$\rho = 0$；若同校学生的考分高度一致，而校际之间差异巨大，则 $\tau_{00}$ 远大于 $\sigma^2$，$\rho$ 趋近于 1。
>
> **结果怎么读** 教育试验中 ICC 通常介于 0.05 至 0.20 之间：
> - $\rho < 0.05$：微弱群聚；
> - $\rho \in [0.05, 0.15]$：典型教育群聚，必须使用聚类校正或多层模型；
> - $\rho > 0.20$：高度同质集群，设计效应极大，单靠增加每校学生数无法有效提高统计功效。
>
> **注意事项** 计算基线 ICC 时必须严守未受协变量吸收的空模型；若提前纳入了强解释力协变量（如前测），得到的将是“条件残差 ICC”，两者不可混淆。

> [!formula-step] 公式步骤　设计效应（Design Effect）与有效样本量换算
> $$\text{Deff} = 1 + (m - 1)\rho$$
>
> $$N_{\text{eff}} = \frac{N}{\text{Deff}} = \frac{J \cdot m}{1 + (m - 1)\rho}$$
>
> **这个公式在做什么** 计算由于集群内部非独立性导致的抽样方差膨胀系数（设计效应），并将名义样本量折算为等效的独立简单随机抽样有效样本量。
>
> **符号说明**
> - $\text{Deff}$：设计效应（Design Effect），方差膨胀因子。
> - $m$：平均集群规模（如每校测试学生数）。
> - $N = J \cdot m$：试验名义总样本量。
> - $N_{\text{eff}}$：真实的有效样本量（Effective Sample Size）。
>
> **数学直觉** 如果每班有 31 名学生（$m = 31$），$\rho = 0.10$，则 $\text{Deff} = 1 + 30 \times 0.10 = 4.0$。这意味着整群抽样的数据方差是简单随机抽样的 4 倍！收集了 4,000 名学生的数据，其包含的统计推断信息量仅等价于 **1,000 名独立个体**。
>
> **结果怎么读** $\text{Deff}$ 直接决定了标准误的放大比例：集群试验的真实标准误为传统独立标准误乘以 $\sqrt{\text{Deff}}$。若忽略该项，实际 $t$ 统计量会被虚假放大 $\sqrt{\text{Deff}}$ 倍。
>
> **注意事项** 当集群规模不平衡时，需采用调和均值或引入变异系数校正公式（Eldridge et al., 2006）。

> [!software-impl] 软件实现
> - **推荐软件** R (`performance`, `lme4`, `ICC`), Stata (`loneway`, `estat icc`).
> - **核心命令**
>   - R (基于 lme4 提取空模型 ICC):
>     ```R
>     library(lme4)
>     null_fit <- lmer(post_score ~ 1 + (1 | school_id), data = df, REML = TRUE)
>     vars <- as.data.frame(VarCorr(null_fit))
>     tau00 <- vars[vars$grp == "school_id", "vcov"]
>     sigma2 <- vars[vars$grp == "Residual", "vcov"]
>     icc <- tau00 / (tau00 + sigma2)
>     # 或直接调用快捷包：
>     performance::icc(null_fit)
>     ```
>   - Stata:
>     ```stata
>     mixed post_score || school_id:, reml
>     estat icc
>     * 或使用方差分析快捷命令：
>     loneway post_score school_id
>     ```
> - **实现流程**
>   1. 拟合单因素随机效应模型；
>   2. 提取组间方差与组内残差方差；
>   3. 计算 ICC 与 95% 置信区间；
>   4. 结合每校平均被试数测算设计效应。
> - **报告标准** 报告 ICC 点估计值、95% 置信区间、平均集群规模 $m$、集群数量 $J$ 以及最终测算的设计效应 $\text{Deff}$。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**
>   - 任何涉及学校、班级、诊所或社区的集群随机对照试验前期功效分析与样本量测算；
>   - 判断多层嵌套数据是否有必要建立多层线性模型或广义估计方程（若 ICC 显著大于 0 则必须建立）；
>   - 行为科学与心理量表测试中评估多位观察者主观评分的一致性（跨评分者信度）。
> - **谨慎使用**
>   - 集群数量过少（$J < 15$）时，极大似然法估计的组间方差容易发生向下偏倚，导致 ICC 点估计不稳定；
>   - 集群规模极度非平衡且方差存在强烈异质性的数据。
> - **不适合使用**
>   - 严格的个体随机分配且受试者完全独立互不影响的经典实验设计；
>   - 没有任何层级聚类标记的纯横截面数据。

---

## 局限性

> [!method-limits] 方法局限
> - **抽样不确定性大** 当集群数较小时，ICC 的置信区间往往极宽，依据历史文献粗略猜测 ICC 极易导致试验先期功效设计严重失实。
> - **集群规模不平衡时的敏感性** 经典公式假定各集群规模完全相等；当各校学生人数差距悬殊时，标准设计效应公式会低估真实的方差膨胀程度。
> - **补救方式** 优先从官方大规模国家普查数据（如英格兰 NPD 归档）中提取先验 ICC；规模不均时采用加权设计效应公式（Eldridge et al., 2006）。

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] 证据清算中心的 ICC 审查门槛 vs 现场实证研究者的统计遗忘
> > 评估规范对集群偏倚的严格问责与研究实践中普遍存在的分析单位错位。
> >
> > - **证据清算规范（WWC / EEF 门槛）** 坚决执行 ICC 一票否决制。WWC 明确规定，任何集群试验若未校正 ICC，直接剥夺最高证据评级；《EEF 评估统计分析指南》（*Statistical Analysis Guidance for EEF Evaluations*; The EEF, 2018; Demack, 2019）强制要求所有试验方案在 SAP 中预注册 ICC 设定值与校正模型。
> > - **实地发表实践缺陷** [[Argument_Wadhwa_2024_RER|Wadhwa et al. (2024)]] 针对全球 12 所清算中心的元审查揭示：除 WWC 外，多数教育数据库（如 NDPC、CASEL）对 ICC 校正视而不见，大量未做校正的假阳性试验被误评为“有效”，深刻揭示了循证界内部的标准割裂。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Hierarchical Linear Model]] | 基础分析框架 | ICC 作为两层随机截距模型分解总方差所直接输出的核心统计量。 |
> | [[Cluster Randomized Trials]] | 核心应用场景 | ICC 赖以发挥设计效应换算与聚类标准误纠偏功能的主要实验设计范式。 |
> | [[Generalized Estimating Equations]] | 稳健替代模型 | GEE 工作相关矩阵中可交换相关系数所对应的群内相关实体。 |
> | [[Ordinary Least Squares]] | 偏误参照系 | 未做 ICC 校正时传统 OLS 发生标准误低估与伪显著性膨胀的根源所在。 |
> | [[Standard Error]] | 修正客体 | ICC 通过设计效应膨胀因子进行彻底纠偏的核心统计推断指标。 |
> | [[Effective Sample Size]] | 换算实体 | ICC 将名义样本量通过设计效应压缩为真实有效样本量的桥梁。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Edovald_Nevill_2021_ROE|Edovald & Nevill (2021)]] — 详述了 EEF 试验复算审计推动出台国家级《EEF 评估统计分析指南》（*Statistical Analysis Guidance for EEF Evaluations*; The EEF, 2018），确立强制采用组内相关系数（ICC）与聚类稳健标准误模型（Demack, 2019）的技术准则。
> - [[Argument_Wadhwa_2024_RER|Wadhwa et al. (2024)]] — 详析全球 12 所证据清算中心在集群随机试验审查中的分歧，批判了忽视 ICC 校正与分析单位错位导致虚假显著性的普遍现象。
