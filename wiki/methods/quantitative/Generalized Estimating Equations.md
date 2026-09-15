---
title: Generalized Estimating Equations
aliases:
  - 广义估计方程
  - 广义估计方程模型
  - GEE
  - Generalized Estimating Equations Model
summary: "用于分析纵向追踪与群聚相关数据的半参数半回归方法，采用准似然估计和三明治稳健方差，在工作相关矩阵结构可能误设的情况下仍能获得群体平均效应的无偏一致估计。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 6
method_related_level: 0
method_related_stars: ""
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - method/statistical
  - method/longitudinal
  - method/clustered-data
related_concepts:
  - "[[Model Dependency]]"
related_theories: []
related_methods:
  - "[[Hierarchical Linear Model]]"
  - "[[Ordinary Least Squares]]"
  - "[[Simple Difference in Means Model]]"
  - "[[Cluster Randomized Trials]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Edovald_Nevill_2021_ROE]]"
confidence: high
status: active
created: 2026-09-15
updated: 2026-09-15
---

# Generalized Estimating Equations

---

## 定义

> [!def] 方法定义
> **广义估计方程（Generalized Estimating Equations，简称 GEE）**是由生物统计学家孔英·梁（Kung-Yee Liang）与斯科特·泽格（Scott L. Zeger）于 1986 年开创的一种用于处理纵向重复测量（Longitudinal Data）与群聚分层数据（Clustered Data）的半参数化回归估计方法。GEE 是广义线性模型（GLM）在非独立相关数据领域的扩展，其核心特征是**群体平均模型（Population-Averaged / Marginal Model）**。该方法不假定因变量的完全联合概率分布，仅指定结果变量的边际均值与方差函数，并引入一个“工作相关矩阵”（Working Correlation Matrix）来近似组内相关结构；即便该工作相关结构被错误设定，GEE 依托 Huber-White 三明治经验方差估计量，依然能够保证大样本下回归参数的一致性与标准误的渐进有效性。[[Argument_Edovald_Nevill_2021_ROE|(Edovald & Nevill, 2021, pp. 52–53)]]

> [!method-scope] 方法范围
> - **研究对象** 包含集群内部相关性的多层数据（如嵌套于学校或班级的学生考分）以及针对同一受试者的多期纵向追踪面板。
> - **问题类型** 群体平均处理效应（Average Treatment Effect, ATE）评估、非独立数据的边际关联分析与因果推断协变量控制。
> - **分析单位** 微观个体（测量单位）及其所属的独立集群（集群单位，如学校、学区）。
> - **输出形式** 群体平均回归系数向量 $\boldsymbol{\beta}$、基于模型与三明治经验修正的两组标准误、Wald 统计量及 95% 置信区间。

> [!citation-card] 广义估计方程在教育试验审计中的半参数稳健性（Edovald & Nevill, 2021; Xiao et al., 2016）
> 在杜伦大学学者针对英国 EEF 早期 17 项大规模教育 RCT 开展的四模型并行复算中，广义估计方程（GEE）作为应对学校群聚偏误的重要备选模型接受了全面审计。复算显示，GEE 与多层线性模型（HLM）均能有效吸收校内组内相关性，避免了标准 OLS 产生的虚假显著性膨胀；由于 GEE 聚焦于“干预对全系统平均学生的净效益”，无需对学校间未观测异质性施加严格的正态分布假设，因而在集群规模充足的教育试验中展现出极佳的边际效应稳健性。[[Argument_Edovald_Nevill_2021_ROE|(Edovald & Nevill, 2021, pp. 52–53)]]
>
> *“In their reanalyses of 17 EEF trials, Xiao et al. (2016) tested generalized estimating equations alongside multilevel models. GEE models the population-averaged response while treating clustering as a nuisance parameter, providing robust standard errors that protect against misspecification of the correlation structure.”*

---

## 方法定位

> [!method-position] 认识论与方法定位
> - **知识观** 边际群体平均哲学。GEE 认为宏观政策与教育干预的核心决策目标是评估群体整体响应的平均位移，而非解构每一个特定学校的微观随机截距。因此将群聚依赖性视为“干扰参数（Nuisance Parameter）”，着力于在相关性干扰下提取纯净的一致点估计。
> - **半参数属性** GEE 仅需要指定一阶矩（条件均值 $\mu_{ij} = g^{-1}(\mathbf{X}_{ij}'\boldsymbol{\beta})$）与二阶矩（方差函数 $V(\mu_{ij})$），完全回避了高阶完全联合似然函数的严苛正态分布假定。
> - **有效性标准** 内部效度取决于外生性设定；统计推断效度依赖三明治方差估计量的大样本渐进正态性（要求独立集群数 $J \ge 30 \sim 50$）。
> - **不声称回答的问题** GEE 无法直接输出特定单个学校或班级的随机效应方差分量，亦不能像 HLM 那样直接提供组内相关系数（ICC）的解析方差比例，不适合用于纯粹探究学校间组织异质性的机制研究。

> [!contrast-table] GEE vs 多层线性模型（HLM） vs OLS 聚类稳健标准误
> | 比较维度 | 广义估计方程（GEE） | 分层多层模型（HLM） | OLS 聚类稳健标准误（CRSE） |
> |---|---|---|---|
> | **模型类型** | 边际模型（Population-Averaged） | 条件/混合模型（Subject-Specific） | 平面回归外挂三明治方差修正 |
> | **分布假定** | 半参数（仅需指定均值与方差函数） | 全参数（假定随机效应服从正态分布） | 古典正态残差（点估计无需，推断依赖大样本） |
> | **群聚处理机制** | 引入工作相关矩阵，由三明治方差吸收 | 引入组间随机截距 $u_{0j}$ 显式分解方差 | 忽略相关性直接拟合，仅事后校正协方差矩阵 |
> | **参数解释** | 全样本群体的平均边际效应 | 控制了特定学校潜变量后的条件效应 | 全样本平均效应 |
> | **非线性连接** | 完美支持二元（Logit）、计数（Poisson） | 非线性时需复杂的数值积分（GLMM） | 线性模型有效，非线性下易受限 |
> | **对误设的稳健性** | 极高（工作矩阵误设仍能保证无偏一致） | 较低（随机效应分布误设可能污染参数） | 极高（仅依赖独立同分布外生性） |

> [!method-stack] 方法层级
> - **研究设计** 集群随机对照试验（Cluster RCT）、纵向多轮追踪调查、多阶段分层抽样评估。
> - **数据收集** 学业连续考分、二分类及格率、多期缺勤计数、学校常态行政普查。
> - **分析方法** 准似然估计（Quasi-Likelihood）、迭代加权广义最小二乘法（IRLS）、三明治稳健方差校正。
> - **辅助技术** 独立工作相关（Independence）、可交换工作相关（Exchangeable）、一阶自回归工作相关（AR-1）与无结构工作相关（Unstructured）模型拟合比较。

---

## 研究程序

> [!proc] 通用程序
> 1. **定义边际均值模型与连接函数** 依据因变量类型（连续、二元、计数）选定适宜的连接函数 $g(\cdot)$（如恒等连接、Logit 连接或 Log 连接）。
> 2. **界定集群结构与独立聚类单位** 明确高层级独立集群标识符（如学校 ID 或学区 ID），确认集群间彼此独立。
> 3. **选取工作相关矩阵（Working Correlation Matrix）** 结合数据生成机制预设相关结构（教育集群试验通常选用可交换相关结构 Exchangeable，假设同校任意两名学生相关度相同）。
> 4. **执行准似然迭代求解** 利用广义估计方程算法迭代计算回归参数向量 $\hat{\boldsymbol{\beta}}$。
> 5. **提取并汇报稳健标准误** 无论模型基于工作相关矩阵输出的模型标准误为何，最终结论必须汇报基于三明治估计量的经验稳健标准误（Robust Standard Errors）。

### 量化分析模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 包含 $J$ 个独立学校集群（$j = 1, \dots, J$），第 $j$ 所学校包含 $n_j$ 名学生（$i = 1, \dots, n_j$），每个观测拥有预测变量向量 $\mathbf{X}_{ij}$ 与因变量 $Y_{ij}$。
> - **核心变量**
>   - 因变量 $Y_{ij}$：后测连续学业考分或及格达标二元哑变量。
>   - 处理状态 $T_j$：学校层级干预指示变量（1/0）。
>   - 控制变量 $\mathbf{Z}_{ij}$：学生基线前测成绩与背景人口学特征。
> - **诊断与检验** QIC（Quasi-Likelihood Information Criterion）模型拟合准则、集群数量充分性检验（$J \ge 40$）。

> [!formula-step] 公式步骤　GEE 准似然得分方程与参数估计
> $$\mathbf{S}(\boldsymbol{\beta}) = \sum_{j=1}^{J} \mathbf{D}_j' \mathbf{V}_j^{-1} (\mathbf{Y}_j - \boldsymbol{\mu}_j) = \mathbf{0}$$
>
> $$\text{其中 } \mathbf{V}_j = \phi \mathbf{A}_j^{1/2} \mathbf{R}_j(\boldsymbol{\alpha}) \mathbf{A}_j^{1/2}$$
>
> **这个公式在做什么** 通过在所有独立学校集群上累加由工作协方差矩阵加权的残差向量，建立准似然无偏估计方程并求解群体平均回归参数 $\boldsymbol{\beta}$。
>
> **符号说明**
> - $\mathbf{Y}_j$：第 $j$ 所学校全部学生因变量构成的 $n_j \times 1$ 维响应向量。
> - $\boldsymbol{\mu}_j$：对应的边际条件均值向量，$\mu_{ij} = g^{-1}(\mathbf{X}_{ij}'\boldsymbol{\beta})$。
> - $\mathbf{D}_j = \partial \boldsymbol{\mu}_j / \partial \boldsymbol{\beta}$：均值关于回归系数的一阶导数导数矩阵。
> - $\mathbf{R}_j(\boldsymbol{\alpha})$：由相关参数 $\boldsymbol{\alpha}$ 决定的 $n_j \times n_j$ 维工作相关矩阵。
> - $\mathbf{A}_j$：对角线上为边际方差函数 $V(\mu_{ij})$ 的对角方差矩阵，$\phi$ 为尺度离散参数。
>
> **数学直觉** GEE 是加权广义最小二乘法向非线性非独立数据的精妙拓展。它利用工作相关矩阵 $\mathbf{R}_j(\boldsymbol{\alpha})$ 为同校学生的残差赋予恰当的非对角协方差权重，使估计方程在数学期望上恒等于零，从而提纯出全系统的无偏边际因果效应。
>
> **结果怎么读** $\hat{\beta}_{\text{treat}}$ 反映了若全系统所有学校均接受干预，相比全系统均未接受干预，学生整体平均产出的净位移量。
>
> **注意事项** 该方程的无偏性完全不依赖于工作相关矩阵 $\mathbf{R}_j(\boldsymbol{\alpha})$ 是否完全真实；即便相关结构假设存在偏差，只要均值模型设定正确，$\hat{\boldsymbol{\beta}}$ 仍然具备大样本一致性。

> [!formula-step] 公式步骤　Huber-White 三明治经验稳健协方差估计量
> $$\text{Var}_{\text{robust}}(\hat{\boldsymbol{\beta}}) = \mathbf{M}_0^{-1} \mathbf{M}_1 \mathbf{M}_0^{-1}$$
>
> $$\mathbf{M}_0 = \sum_{j=1}^{J} \mathbf{D}_j' \mathbf{V}_j^{-1} \mathbf{D}_j, \quad \mathbf{M}_1 = \sum_{j=1}^{J} \mathbf{D}_j' \mathbf{V}_j^{-1} (\mathbf{Y}_j - \hat{\boldsymbol{\mu}}_j)(\mathbf{Y}_j - \hat{\boldsymbol{\mu}}_j)' \mathbf{V}_j^{-1} \mathbf{D}_j$$
>
> **这个公式在做什么** 利用两片基于模型的“面包”（$\mathbf{M}_0^{-1}$）夹住一片由样本经验残差叉积构成的“肉”（$\mathbf{M}_1$），构建对相关结构误设免疫的稳健协方差矩阵。
>
> **符号说明**
> - $\mathbf{M}_0$：模型理论信息矩阵（外部面包层）。
> - $\mathbf{M}_1$：基于集群样本实际经验残差向量外积计算的方差核（肉质夹心层）。
> - $\text{Var}_{\text{robust}}(\hat{\boldsymbol{\beta}})$：最终用于假设检验与构建置信区间的稳健协方差矩阵。
>
> **数学直觉** 即使工作矩阵 $\mathbf{V}_j$ 猜错了真实相关模式，样本经验残差 $(\mathbf{Y}_j - \hat{\boldsymbol{\mu}}_j)(\mathbf{Y}_j - \hat{\boldsymbol{\mu}}_j)'$ 依然诚实记录了集群内部真实的变异波动。通过三明治架构的代数抵消，模型误设带来的偏误在渐进意义上被完全吸收。
>
> **结果怎么读** 从该对角线开方得到的标准误即为三明治稳健标准误，用以计算诚实可靠的 $z$ 统计量与 $p$ 值。
>
> **注意事项** 三明治估计量的优良性质建立在集群数量 $J \to \infty$ 的大样本渐进理论上；若学校集群数量少于 30–40 所，三明治方差倾向于系统性向下偏倚，导致假阳性错误率上升。

> [!software-impl] 软件实现
> - **推荐软件** R (`geepack`), Stata (`xtgee`), Python (`statsmodels.genmod.generalized_estimating_equations`).
> - **核心命令**
>   - R:
>     ```R
>     library(geepack)
>     gee_model <- geeglm(post_score ~ treat + pre_score + sen + fsm,
>                         id = school_id,
>                         data = df,
>                         family = gaussian(link = "identity"),
>                         corstr = "exchangeable")
>     summary(gee_model)
>     ```
>   - Stata:
>     ```stata
>     xtset school_id
>     xtgee post_score treat pre_score sen fsm, family(gaussian) link(identity) corr(exchangeable) vce(robust)
>     ```
> - **实现流程**
>   1. 数据组织：指定聚类变量 `id`（学校 ID），按集群排序；
>   2. 设定参数：设定分布族（高斯/二项）、连接函数与工作相关结构（默认 exchangeable）；
>   3. 提取结果：导出群体平均参数、三明治稳健标准误、Wald 统计量与置信区间；
>   4. 敏感性检验：尝试替换相关结构为 `ar1` 或 `independence`，对比系数稳定性。
> - **报告标准** 必须汇报独立集群数量 $J$、所采用的工作相关矩阵类型、未经修正的模型标准误以及最终决定的三明治稳健标准误与 Wald $\chi^2$ 检验。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**
>   - 学校或班级集群数量充足（$J \ge 40$）的大规模整群随机对照试验（Cluster RCT）；
>   - 评估干预对全系统平均学生的净成效（如国家教育部门关心的整体普惠政策增益）；
>   - 因变量为非正态分布（如学生是否及格的二元达标率、违纪行为发生次数的计数变量）的嵌套数据；
>   - 多期追踪面板数据中处理受试者重复测量的自相关问题。
> - **谨慎使用**
>   - 学校集群数量较少（如 $J < 20 \sim 30$）的试验，三明治方差估计量会发生明显偏倚，需外挂小样本修正（如 Kauermann-Carroll 或 Fay-Graubard 校正）；
>   - 试验数据中存在严重集群非平衡且缺失机制非随机的情形。
> - **不适合使用**
>   - 核心研究问题聚焦于解构各学校自身组织文化差异与特定学校异质性截距的情境（应选用多层线性模型 HLM）；
>   - 意在检验复杂跨层级随机斜率交互作用（Cross-level Random Slope Interaction）的研究。

---

## 局限性

> [!method-limits] 方法局限
> - **小集群三明治方差向下偏倚** 当集群数量不足 30 所时，经验三明治方差对真实方差的估计存在系统性低估，导致第一类错误（假阳性）虚高。
> - **缺失数据处理严苛** GEE 默认仅在数据完全随机缺失（Missing Completely at Random, MCAR）时保持无偏；若数据属于随机缺失（MAR），必须引入逆概率加权（IPW-GEE），否则估计量可能产生偏误（相比之下，全参数 HLM 在 MAR 条件下依然无偏）。
> - **无法进行受试特异性预测** GEE 估计的是宏观边际效应，无法为具体某所学校预测其实际潜在产出值。
> - **补救方式** 采用小样本纠偏算法；在 MAR 缺失下联合倾向得分赋权；或与 HLM 进行并行双重模型验证（Xiao et al., 2016）。

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] 群体平均边际视角 vs 混合效应主体特异性视角
> > 统计学与方法论学者在分析教育嵌套数据时的流派争论。
> >
> > - **边际模型（GEE）阵营** 强调政策制定的公共属性。宏观教育决策者关心的是“推行该教学法能让全系统平均学童提高多少分”，而非某个特定学校潜变量是多少。GEE 无需强加正态随机效应假定，对工作矩阵误设具有免疫力，是最诚实稳健的政策评估工具。
> > - **多层模型（HLM）阵营** 强调教育实践的生态分层属性。批评 GEE 将宝贵的学校间方差视作无用噪声（Nuisance），丢弃了理解学校组织差异与跨层级教学机制的机会。肖等学者（Xiao et al., 2016）利用 NPD 归档数据的复算表明，在教育试验样本充足且正态性良好的场景下，两类模型的点估计极为接近，共同构成了捍卫实验公信力的双重防火墙（[[Argument_Edovald_Nevill_2021_ROE|Edovald & Nevill, 2021]]）。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Hierarchical Linear Model]] | 对偶模型 | 与 GEE 并列处理集群数据的两大主流模型，分别代表条件混合与边际平均视角。 |
> | [[Ordinary Least Squares]] | 基础参照 | GEE 在考虑群聚工作协方差与三明治方差校正后对传统 OLS 的稳健扩展。 |
> | [[Simple Difference in Means Model]] | 基准模型 | 零协变量时的最简比较模型，与 GEE 构成控制方差与群聚特征的演进阶梯。 |
> | [[Intraclass Correlation Coefficient]] | 关联参数 | GEE 可交换工作相关矩阵中的关联系数参数对应概念。 |
> | [[Cluster Randomized Trials]] | 核心应用场景 | GEE 作为解决整群依赖、校正标准误的核心分析工具所服务的试验形态。 |
> | [[Model Dependency]] | 风险现象 | 解释了四模型复算中因模型底层哲学差异而引发的效应量敏感性。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Edovald_Nevill_2021_ROE|Edovald & Nevill (2021)]] — 综述了齐·肖（ZhiMin Xiao）等杜伦大学学者利用 NPD 归档数据开展的 17 项 EEF 试验四模型并行复算，将 GEE 作为应对集群相关性的代表性边际模型，揭示出统计模型选择对效应量与置信区间的颠覆性影响。
