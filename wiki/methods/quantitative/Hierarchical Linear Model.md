---
title: Hierarchical Linear Model
aliases:
  - 分层线性模型
  - 多层线性模型
  - 多水平模型
  - HLM
  - MLM
  - Multilevel Model
  - Multilevel Linear Model
summary: "专门用于分析具有嵌套或分层结构数据的统计建模方法，通过将总方差分解为组内与组间多重随机效应分量，有效解决群聚数据中的观测非独立性与标准误低估问题。"
type: method
method_type: quantitative
tags:
  - method/quantitative
  - method/statistical
  - method/multilevel
  - method/hierarchical-modeling
related_concepts:
  - "[[Model Dependency]]"
related_theories: []
related_methods:
  - "[[Cluster Randomized Trials]]"
  - "[[Three-Level Meta-Analysis]]"
  - "[[Covariate Adjustment]]"
  - "[[Standard Error]]"
  - "[[Statistical Significance]]"
related_instruments: []
related_persons:
  - "[[Steve Higgins]]"
related_facts: []
related_arguments:
  - "[[Argument_Edovald_Nevill_2021_ROE]]"
  - "[[Argument_Wadhwa_2024_RER]]"
  - "[[Argument_Song_Choi_2026_FPSYG]]"
confidence: high
status: active
created: 2026-09-15
updated: 2026-09-15
---

# Hierarchical Linear Model

---

## 定义

> [!def] 方法定义
> **分层线性模型（Hierarchical Linear Model，简称 HLM，在统计学中亦称多层线性模型 Multilevel Linear Model, MLM，或随机效应混合模型 Mixed-Effects Model）**是一种专门用于分析具有多层嵌套（Nested / Clustered）或分层结构数据的参数化回归建模方法。在教育研究中，学生个体（Level 1）天然嵌套于班级或学校（Level 2），同校学生因共享学校师资、校园文化、社区背景或课堂教学而存在内在相似性，违背了传统[[Ordinary Least Squares|普通最小二乘法]]（OLS）所要求的“误差独立同分布（I.I.D.）”假设。HLM 通过将因变量的总变异解构为个体层级残差方差与群体层级随机效应方差，不仅能够精确计算**组内相关系数（Intraclass Correlation Coefficient, ICC）**并对抽样标准误进行彻底校正，还能显式估计宏观组织特征对微观个体产出的跨层级调节效应（Cross-level Interaction）。[[Argument_Edovald_Nevill_2021_ROE|(Edovald & Nevill, 2021, pp. 52–53)]]; [[Argument_Wadhwa_2024_RER|(Wadhwa et al., 2024, pp. 8–10)]]

> [!method-scope] 方法范围
> - **研究对象** 具有两层或三层嵌套结构的数据（如“学生-班级-学校”、“重复测量时间点-个体受试者”、“初级效应量-初级研究”）。
> - **问题类型** 集群随机试验（CRTs）干预因果效应评估、组间异质性方差分解、跨层级交互作用机制解析（如“学校办学体制是否调节了家庭经济背景对学业成绩的促进作用”）。
> - **分析单位** 微观个体（Level 1）与宏观集群（Level 2 / Level 3）同步分层建模。
> - **输出形式** 固定效应回归系数 $\gamma$（平均斜率与截距）、随机效应方差分量（$\tau_{00}, \tau_{11}, \sigma^2$）、组内相关系数（ICC / $\rho$）、模型似然比检验（LRT）与拟合优度指数（AIC/BIC）。

> [!citation-card] 多层线性模型在教育试验审计中的聚类校正与制度化定型（Edovald & Nevill, 2021; Xiao et al., 2016）
> 在杜伦大学学者齐·肖（ZhiMin Xiao）、[[Steve Higgins|史蒂夫·希金斯]]（Steve Higgins）与阿迪特·卡西姆（Adetayo Kasim）对 EEF 早期 17 项大规模教育 RCT 进行微观复算时，多层线性模型（HLM）被确立为解决群聚偏误的基准模型。复算显示，教育试验中干预往往以学校或班级为单位实施，同校学生考分表现出不容忽视的组内相关性（ICC 通常在 0.10 至 0.20 之间）。若采用忽略聚类结构的传统 OLS，有效样本量会被严重夸大，标准误大幅低估，产生大量的假阳性显著性（Type I Error）；而 HLM 通过准确建模两级随机效应，提供了诚实反映群聚不确定性的标准误与置信区间。这一研究推动 EEF 制定了《统计分析指南》，强制全英试验主效应分析必须采用多层模型或聚类校正模型。[[Argument_Edovald_Nevill_2021_ROE|(Edovald & Nevill, 2021, pp. 52–53)]]
>
> *“Cluster-level variation is ubiquitous in educational trials. Reanalyses by Xiao et al. (2016) showed that ignoring clustering in regression models inflates Type I errors. Hierarchical linear models partition variance across levels, providing accurate standard errors that reflect the true effective sample size of cluster randomised designs.”*

---

## 方法定位

> [!method-position] 认识论与方法定位
> - **知识观** 承认社会与教育现实的生态学结构（Ecological Structure）。个体不是游离在真空中的原子，而是嵌入在特定组织与环境脉络中的主体；微观行为与宏观环境之间存在相互依赖与层级穿透。
> - **统计哲学** 混合效应范式（Mixed Effects Modeling）。将参数区分为全样本共享的“固定效应（Fixed Effects）”与反映群体异质性的“随机效应（Random Effects）”，运用经验贝叶斯（Empirical Bayes）收缩估计（Shrinkage）兼顾群体均值与个体特征。
> - **有效性标准** 统计结论效度通过消除集群相关导致的虚假膨胀得到捍卫；模型拟合依赖方差分量显著性与限制性极大似然（REML）收敛性。
> - **不声称回答的问题** 不能解决非随机分配下的个体或学校层级遗漏变量混杂；若二级集群数量过少（如学校数少于 15–20 所），HLM 对层级间方差的估计可能不稳定。

> [!contrast-table] HLM vs OLS 聚类稳健标准误 vs 广义估计方程（GEE）
> | 比较维度 | 分层线性模型（HLM） | OLS 聚类稳健标准误（CRSE） | 广义估计方程（GEE） |
> |---|---|---|---|
> | **建模哲学** | 条件模型（Subject-Specific Model） | 平面边际模型外挂修正 | 群体平均边际模型（Population-Averaged） |
> | **方差分解** | 显式分解组内与组间多层方差分量 | 不分解方差，仅调整标准误协方差矩阵 | 设定工作相关矩阵，不估计随机效应方差 |
> | **跨层级交互** | 原生支持随机斜率与跨层级调节检验 | 仅能做平面交互项，无法区分层内层间斜率 | 仅关注群体平均均值响应 |
> | **小集群敏感度** | 集群数过少（$J < 20$）时组间方差易偏倚 | 集群数过少时标准误严重向下偏倚（需膨胀修正） | 集群数过少时三明治方差估计量向下偏倚 |
> | **典型应用场景** | 机制解析、探索学校异质性、CRT 主模型 | 简单政策评估、不需要分解方差时的稳健分析 | 大样本公共卫生追踪、边际干预均值比较 |

> [!method-stack] 方法层级
> - **研究设计** 集群随机对照试验（[[Cluster Randomized Trials|Cluster RCT]]）、跨国大规模测评（PISA/TIMSS）、多阶段分层抽样调查、纵向重复测量生长曲线（Growth Curve）。
> - **数据收集** 学生统考数据库（NPD）、学校督导数据库、教师问卷与学生问卷配对数据。
> - **分析方法** 零模型（Null Model / 随机截距方差分解）、随机截距模型（Random Intercept Model）、随机斜率模型（Random Slope Model）、完全条件模型（含跨层级交互）。
> - **辅助技术** 限制性极大似然估计（REML）、组均值中心化（Group-Mean Centering）、总均值中心化（Grand-Mean Centering）、设计效应（Design Effect）校正。

---

## 研究程序

> [!proc] 通用程序
> 1. **空模型估计与 ICC 测算（Null Model）** 不纳入任何预测变量，分解总方差为 Level 1 与 Level 2，计算组内相关系数 ICC。若 ICC 显著大于 0（如 $\ge 0.05$），证实必须采用多层分析。
> 2. **变量中心化处理（Centering Decision）** 依据理论假设决定自变量采用总均值中心化（便于控制宏观混杂）或组均值中心化（纯粹提取微观组内效应）。
> 3. **拟合随机截距模型（Random Intercept Model）** 引入 Level 1 学生变量（如基线前测成绩）与 Level 2 学校变量（如干预组别），固定斜率，仅允许各校截距随机变动。
> 4. **评估随机斜率与跨层级交互（Random Slope & Cross-level Interaction）** 检验干预效应是否在不同学校间存在显著异质性；若存在，引入学校特征变量解释斜率异质性。
> 5. **模型比较与残差诊断** 运用似然比检验（LRT）比较模型复杂度与拟合度，检查各层级残差的正态性与异常群聚点。

### 量化分析模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 包含 $J$ 所学校（Level 2），第 $j$ 所学校包含 $n_j$ 名学生（Level 1），总样本量 $N = \sum n_j$。
> - **核心变量**
>   - Level 1 变量：学生后测考分 $Y_{ij}$、基线前测成绩 $X_{ij}$、家庭社会经济地位等。
>   - Level 2 变量：学校干预哑变量 $W_j$（1 = 处理校，0 = 对照校）、学校办学性质或资源指标。
> - **诊断与检验** ICC 值大小、Level 2 残差 $u_{0j}$ 的正态分布检验、集群数量充足性评估（一般建议 $J \ge 30$）。

> [!formula-step] 公式步骤　空模型与组内相关系数（ICC）
> $$Y_{ij} = \beta_{0j} + \varepsilon_{ij}, \quad \beta_{0j} = \gamma_{00} + u_{0j}$$
>
> $$\text{复合形式: } Y_{ij} = \gamma_{00} + u_{0j} + \varepsilon_{ij}$$
>
> $$\text{ICC} = \rho = \frac{\tau_{00}}{\tau_{00} + \sigma^2}$$
>
> **这个公式在做什么** 在不加入任何自变量的前提下，将学生考分的总方差分解为学校间方差与学校内个体残差方差，计算组内相关系数 ICC。
>
> **符号说明**
> - $Y_{ij}$：第 $j$ 所学校第 $i$ 名学生的后测考分。
> - $\gamma_{00}$：所有学校的总平均截距（总体均值）。
> - $u_{0j}$：第 $j$ 所学校对总体均值的随机偏离，假设 $u_{0j} \sim N(0, \tau_{00})$，其中 $\tau_{00}$ 为学校间方差。
> - $\varepsilon_{ij}$：个体学生对所在学校均值的随机偏离，假设 $\varepsilon_{ij} \sim N(0, \sigma^2)$，其中 $\sigma^2$ 为学生内方差。
> - $\rho$：组内相关系数（ICC），表示总方差中可归因于学校间差异的比例。
>
> **数学直觉** 若 $\rho$ 接近 0，说明同校学生并不比不同学校的学生更相似，多层嵌套结构对数据推断影响微弱；若 $\rho = 0.15$，说明学生考分变异的 15% 来源于学校之间的固有差距。在集群试验中，设计效应 $\text{DE} = 1 + (m - 1)\rho$（其中 $m$ 为平均班级规模）会导致有效样本量急剧缩水。
>
> **结果怎么读** $\rho > 0.05$ 在教育研究中通常被视为必须使用多层线性模型的刚性门槛，否则传统 OLS 将严重虚夸有效自由度。
>
> **注意事项** 计算 ICC 时必须使用未纳入任何预测变量的空模型（Unconditional Model），否则方差分量会被外生变量吸收而导致 ICC 失真。

> [!formula-step] 公式步骤　两层随机截距协变量调整模型（CRT 主效应模型）
> $$\text{Level 1 (学生): } Y_{ij} = \beta_{0j} + \beta_{1} (X_{ij} - \bar{X}_{\cdot\cdot}) + \varepsilon_{ij}, \quad \varepsilon_{ij} \sim N(0, \sigma^2)$$
>
> $$\text{Level 2 (学校): } \beta_{0j} = \gamma_{00} + \gamma_{01} W_j + u_{0j}, \quad u_{0j} \sim N(0, \tau_{00})$$
>
> $$\text{复合模型: } Y_{ij} = \gamma_{00} + \gamma_{01} W_j + \beta_{1} (X_{ij} - \bar{X}_{\cdot\cdot}) + u_{0j} + \varepsilon_{ij}$$
>
> **这个公式在做什么** 在集群随机试验中，以两层结构同时建模学生层级的基线前测调整与学校层级的干预效应，剥离学校水平随机误差并无偏估计干预处理效应 $\gamma_{01}$。
>
> **符号说明**
> - $W_j$：学校层级干预状态指示变量（1 = 处理校，0 = 对照校）。
> - $X_{ij} - \bar{X}_{\cdot\cdot}$：经总均值中心化的学生基线前测考分。
> - $\gamma_{01}$：学校干预对学生学业产出的净平均处理效应（主效应点估计）。
> - $\beta_1$：学生前测对后测的固定效应斜率。
> - $u_{0j}$：控制了干预变量后的学校层级剩余残差。
>
> **数学直觉** 该模型巧妙地将干预分配定位在它的真实实施层级（Level 2 学校），避免了在 Level 1 将学生误作为独立试验单位的聚合偏误；同时在 Level 1 引入前测，吸收了大量的学生内残差方差 $\sigma^2$，从而兼顾了方差吸收与正确的聚类标准误估计。
>
> **结果怎么读** $\gamma_{01}$ 的统计检验直接检验学校干预是否显著改善了学生的平均学业成就；其标准误自动基于学校数量 $J$ 与残差方差构成，诚实反映了整群试验的不确定性。
>
> **注意事项** 该模型假设干预在各校的斜率一致（固定斜率）；若不同学校的干预落地效果差异巨大，需将 $\beta_{1}$ 或干预效应扩展为随机斜率项（Random Slope）。

> [!software-impl] 软件实现
> - **推荐软件** R (`lme4`, `lmerTest`), Stata (`mixed`), Python (`statsmodels.regression.mixed_linear_model.MixedLM`), HLM 8.
> - **核心命令**
>   - R (空模型计算 ICC):
>     ```R
>     null_model <- lme4::lmer(post_score ~ 1 + (1 | school_id), data = df, REML = TRUE)
>     performance::icc(null_model)
>     ```
>   - R (两层随机截距 CRT 主模型):
>     ```R
>     crt_model <- lmerTest::lmer(post_score ~ treat + pre_score_c + (1 | school_id), data = df, REML = TRUE)
>     summary(crt_model)
>     ```
>   - Stata:
>     ```stata
>     mixed post_score treat pre_score_c || school_id:, reml
>     estat icc
>     ```
> - **实现流程**
>   1. 数据整备：将数据按学校 ID 与学生 ID 排序，对前测成绩执行总均值或组均值中心化；
>   2. 拟合空模型：提取 $\tau_{00}$ 与 $\sigma^2$，计算 ICC 并检验组间差异显著性；
>   3. 拟合随机截距模型：加入干预变量与基线协变量，采用限制性极大似然法（REML）估计固定效应与方差分量；
>   4. 效应量换算：基于调整后模型提取总方差 $\sqrt{\tau_{00} + \sigma^2}$ 换算 Hedges' $g$。
> - **报告标准** 完整呈现固定效应系数、标准误（标明自由度估算方法如 Satterthwaite 或 Kenward-Roger）、$t$ 值与 $p$ 值；同时报告随机截距方差 $\tau_{00}$、残差方差 $\sigma^2$、ICC 与样本量（学校数 $J$ 与学生数 $N$）。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**
>   - 以班级或学校为单位进行随机分配的集群随机对照试验（[[Cluster Randomized Trials|Cluster RCT]]）；
>   - 评估涉及复杂组织制度、教师教学风格与学生个体背景交互作用的教育实证研究；
>   - 跨国大规模学生测评数据（如 PISA、TIMSS）中探讨国家、学校与学生三层结构的分层分析；
>   - 元分析中处理包含多个相关效应量的三层元分析（[[Three-Level Meta-Analysis]]）。
> - **谨慎使用**
>   - 高层级集群数量较少（如学校数不足 15–20 所）的研究，此时极大似然估计的组间方差容易发生向下偏倚，应启用 Kenward-Roger 小样本自由度修正；
>   - ICC 极小（$\rho < 0.01$）且似然比检验显示组间方差无统计学意义的情形。
> - **不适合使用**
>   - 严格个体随机分配且受试者之间不存在任何空间、物理、教学组织关联的完全单层数据；
>   - 观测数据中层级隶属关系模糊、存在多重交叉分类且无法构建清晰嵌套矩阵的非结构化数据。

---

## 局限性

> [!method-limits] 方法局限
> - **高层级样本量要求严苛** HLM 的统计功效主要取决于第二层集群数量（学校数 $J$），而非第一层个体数量（学生数 $N$）。即便每所学校测试数百名学生，若总共只有 10 所学校，模型估计组间方差的功效依然极低。
> - **中心化策略敏感性** 变量采用总均值中心化（Grand-Mean Centering）还是组均值中心化（Group-Mean Centering）对截距含义和斜率解释具有根本影响；若中心化方式选用不当，极易将学校间的宏观结构效应与个体间的微观效应混为一谈。
> - **高维随机斜率收敛困境** 当模型引入过多随机斜率与跨层级协方差时，限制性极大似然算法极易遭遇数值奇异（Singular Fit）或迭代无法收敛。
> - **补救方式** 采用 Kenward-Roger 自由度调整改善小集群推断；在理论指引下审慎选择中心化方案；对于收敛困难的复杂高维模型，可转向贝叶斯 MCMC 估计（如 `brms` 或 `rstanarm`）。

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] 参数化多层随机效应模型 vs 边际半参数广义估计方程（GEE）
> > 教育统计界内部在处理集群相关数据时的模型路线之争。
> >
> > - **参数化多层模型派** 坚持显式指定层级概率结构，认为只有 HLM 能够诚实拆解方差来源、揭示学校背景的调节效应，并为集群试验提供最贴近真实教育生成过程的解释力。
> > - **半参数边际模型派（GEE 倡导者）** 批评 HLM 过于依赖随机效应服从正态分布的严苛假设，一旦分布设定错误，点估计可能遭受污染；而 GEE 仅关注群体平均因果效应，对工作相关结构的设定具有稳健性，更适合纯粹评估全系统干预净收益。肖等学者（Xiao et al., 2016）的复算审计表明，在正态性较好的标准试验中两类模型结论高度接近，但在非平衡小样本试验中 HLM 提供了更严谨的方差结构保护（[[Argument_Edovald_Nevill_2021_ROE|Edovald & Nevill, 2021]]）。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Cluster Randomized Trials]] | 适用场景 | HLM 作为核心分析工具所服务的核心教育实验设计范式。 |
> | [[Ordinary Least Squares]] | 基础模型 | HLM 克服 OLS 独立同分布假设局限性后在多层嵌套领域的自然扩展。 |
> | [[Simple Difference in Means Model]] | 对照模型 | 极简双组比较模型，与 HLM 的层级方差分解形成鲜明的方法学阶梯。 |
> | [[Three-Level Meta-Analysis]] | 跨领域应用 | HLM 原理在元分析领域的经典推广，用于处理效应量多层依赖。 |
> | [[Covariate Adjustment]] | 核心技术 | 在 HLM Level 1 引入前测以压缩组内残差方差的核心统计策略。 |
> | [[Standard Error]] | 推断标尺 | HLM 通过组内相关系数（ICC）与方差分解彻底校正的关键推断量。 |
> | [[Statistical Significance]] | 决策指标 | HLM 消除群聚导致的标准误低估后纠正虚假显著性的评判标准。 |
> | [[Model Dependency]] | 风险现象 | 解释了为什么多层模型与 OLS、简单均值模型之间的选择会引发效应量与显著性剧烈漂移。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Edovald_Nevill_2021_ROE|Edovald & Nevill (2021)]] — 详述了杜伦大学齐·肖（ZhiMin Xiao）等学者对 17 项 EEF 试验开展的多层线性模型并行审计，证明了 HLM 在校正学校与班级集群效应中的不可替代性，直接倒逼出台了英国国家级试验《统计分析指南》。
> - [[Argument_Wadhwa_2024_RER|Wadhwa et al. (2024)]] — 批评了国际教育证据清算机构忽视集群随机试验中的 HLM 与 ICC 校正，指出未做多层校正会导致标准误严重低估与虚假显著性。
> - [[Argument_Song_Choi_2026_FPSYG|Song & Choi (2026)]] — 运用三层多层线性模型架构将元分析总变异分解为抽样误差、研究内效应量变异与研究间异质性三层方差。
