---
title: Exploratory Factor Analysis
aliases:
  - 探索性因子分析
  - EFA
  - 主轴因子分析
  - Principal Axis Factoring
summary: "一种无监督或半监督的多变量统计降维技术，用于在未预设确定性测度关系的前提下，从一组观测变量的相关矩阵中提取出少数潜在公共因子，以揭示潜在构念并实现数据降维。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 20
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - method/factor-analysis
  - method/dimensionality-reduction
  - method/psychometrics
related_concepts:
  - "[[Variable]]"
  - "[[Hypothesis]]"
  - "[[Construct]]"
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Simplicity of Knowledge]]"
  - "[[Output-Oriented Governance]]"
related_theories: []
related_methods:
  - "[[Questionnaire]]"
  - "[[Sample Size Determination]]"
  - "[[Scale Development]]"
  - "[[Confirmatory Factor Analysis]]"
  - "[[Correlational Research]]"
  - "[[KMO and Bartlett's Test of Sphericity]]"
  - "[[Cluster Analysis]]"
  - "[[Likert Scale]]"
related_instruments:
  - "[[Schommer's Modified Epistemological Questionnaire]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Bergeron_2015_TeachingTOK]]"
  - "[[Argument_Lodewyk_2007_EP]]"
  - "[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO]]"
  - "[[Argument_Altrichter_2019_ZfB]]"
confidence: high
status: draft
created: 2026-08-17
updated: 2026-09-18
---

# Exploratory Factor Analysis

---

## 定义

> [!def] 方法定义
> **探索性因子分析（Exploratory Factor Analysis, EFA）** 是一种用于识别多变量数据底层结构的多元统计降维技术。它在未预先指定具体测量题项与潜在维度一一对应关系的探索性前提下，通过对一组观测[[Variable|变量]]之间的协方差或相关矩阵进行分解，将原始变量分解为少数几个共同解释大部分协方差的**潜在公共因子（Common Factors）**与各个变量特有的**独特性方差与测量误差（Unique Factors）**，从而揭示潜藏于可观测数据背后的理论[[Construct|构念]]维度。[[Argument_Altrichter_2019_ZfB|(Altrichter et al., 2019, p. 24)]]

> [!method-scope] 方法范围
> - **研究对象** 新开发的态度与行为[[Likert Scale|李克特量表]][[Questionnaire|问卷]]数据、尚未确立成熟维度结构的测评指标体系、多重连续或类别观测变量。
> - **问题类型** 回答海量观测题项背后潜藏着几个独立或相关的实质特质维度，每个题项在各维度上的贡献强度与归属分布，以及如何精简变量集合以作为后续分类或因果建模的输入特征。
> - **[[Unit of Analysis|分析单位]]** 个体行动者（如教师、校长、学生）、学校组织或区域测量单元。
> - **输出形式** 因子提取数量、特征值（Eigenvalues）、方差贡献率、碎石图（Scree Plot）、因子载荷矩阵（Factor Loadings Matrix）、因子间相关矩阵（Factor Correlation Matrix）以及标准化因子得分（Factor Scores）。

> [!citation-card] 探索性因子分析对潜在治理维度的提取功能
> 探索性因子分析（采用主轴提取法与斜交 Promax 旋转）能够从学校领导者对复杂治理工具的零散评价中提炼出潜在的价值信念结构，为后续识别校长群体的经验形态学提供稳健的输入指标。[[Argument_Altrichter_2019_ZfB|(Altrichter et al., 2019, p. 24)]]
>
> *Zur Identifikation der latenten Dimensionen der Steuerungshaltung wurde eine Hauptachsenanalyse mit Promax-Rotation gerechnet, um die empirische Struktur der 22 Governance-Instrumente aufzudecken.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 假定人类复杂的心理特质、制度态度与组织行为并非孤立存在，而是受深层不可直接观测的潜在构念（Latent Constructs）所驱动；观测指标是潜在构念在现实中的不完全投影并伴生测量误差。
> - **研究者角色** 在因子提取方法（主轴因子 vs 最大似然）、因子的保留数目判定准则（Kaiser 准则、碎石图、平行分析）、旋转方式（正交 vs 斜交）以及最终维度的理论命名中，研究者兼具统计裁决者与理论阐释者的双重角色。
> - **有效性标准** 遵循统计拟合准则（KMO 抽样适度检验、Bartlett 球形检验显著性、因子的方差累积解释率）与理论构念可解释性的双重收敛。
> - **不声称回答的问题** EFA 本身不提供全模型整体拟合优度的卡方或结构方程显著性检验（此为[[Confirmatory Factor Analysis|验证性因子分析]]的职能）；亦不能确定变量间的定向因果影响。

> [!method-stack] 方法层级与技术谱系
> - **研究设计** [[Scale Development|量表开发]]、实证调查研究、潜在维度挖掘。
> - **数据收集** 多维度态度问卷、大规模测验背景问卷。
> - **提取方法** 主轴因子法（Principal Axis Factoring, PAF，注重公共方差，对非多元正态数据较为稳健）、最大似然法（Maximum Likelihood, ML，允许模型显著性检验，要求多元正态分布）、主成分法（PCA，严格意义上为数学降维而非因子分析）。
> - **旋转方法** 正交旋转（Varimax，假定因子间严格不相关）、斜交旋转（Promax / Direct Oblimin，允许因子间存在现实理论相关，在社会与教育科学中更为吻合实际）。
> - **下游衔接** 计算因子得分后，可直接作为[[Cluster Analysis|聚类分析]]（构建人群类型学）或多元回归/结构方程模型的连续前置变量。

---

## 研究程序

> [!proc] 通用操作程序
> 1. **数据适用性诊断** 计算 [[KMO and Bartlett's Test of Sphericity|KMO 抽样适度系数]]（要求 $\text{KMO} > 0.70$）与 Bartlett 球形检验（要求 $p < .05$），确保变量相关矩阵非恒等矩阵且变量间存在充足公共方差。
> 2. **因子提取与维数决定** 运用主轴因子法或最大似然法提取因子，结合特征值大于 1（Kaiser 准则）、碎石图肘部拐点（Scree Plot Elbow）以及平行分析（Parallel Analysis），审慎确定保留的因子数目。
> 3. **因子旋转以提升可解释性** 若理论上假设潜在维度相互独立，采用最大方差正交旋转（Varimax）；若各维度同属于广义态度或能力构念且彼此相关，采用斜交旋转（如 Promax 算法），获得模式矩阵（Pattern Matrix）与结构矩阵（Structure Matrix）。
> 4. **题项精简与载荷清洗** 根据预设准则逐步剔除不良题项：主载荷偏低（通常 $< 0.40$ 或 $< 0.35$）、跨载荷严重（在两个或多个因子上的载荷差绝对值 $< 0.15$）、或题项内容与所属因子缺乏理论相容性。
> 5. **因子命名与信度检验** 依据高载荷题项的核心语义对提取出的公共因子赋予学术命名，并分别计算各分维度的内部一致性信度（Cronbach's $\alpha$）。

### 量化方法模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 大样本横截面观测矩阵（$N \times P$），通常建议样本量与题项比至少为 $5:1$ 至 $10:1$，且绝对样本量 $N \ge 200$。
> - **变量或指标** 多个定序（如李克特 4–7 点量表）或连续观测题项。
> - **核心统计量** 特征值、因子载荷系数（$\lambda_{ij}$）、共同度（Communality, $h_i^2$）、因子间相关系数（$r_f$）、累积方差贡献率。

> [!formula-step] 公式步骤　公共因子模型（Common Factor Model）
> $$\mathbf{x} = \boldsymbol{\mu} + \boldsymbol{\Lambda} \mathbf{f} + \boldsymbol{\epsilon}$$
> 
> 对单个观测变量 $x_i$ 展开为：
> $$x_i = \mu_i + \lambda_{i1} f_1 + \lambda_{i2} f_2 + \dots + \lambda_{im} f_m + \epsilon_i$$
>
> **这个公式在做什么** 将每个观测变量 $x_i$ 的方差严格分解为两大部分：受 $m$ 个潜在公共因子 $f_1, \dots, f_m$ 共同作用的**公共方差（Common Variance，即共同度 $h_i^2 = \sum_{j=1}^m \lambda_{ij}^2$）**，以及该变量特有的**独特方差（Unique Variance，包含特异变异与随机测量误差 $\epsilon_i$）**。
>
> **符号说明**
> - $\mathbf{x}$ 为 $p$ 维观测变量向量；$\boldsymbol{\mu}$ 为观测变量均值向量。
> - $\boldsymbol{\Lambda}$ 为 $p \times m$ 阶因子载荷矩阵（Factor Loadings），$\lambda_{ij}$ 表示第 $j$ 个潜在因子对第 $i$ 个观测变量的回归权重。
> - $\mathbf{f}$ 为 $m$ 维公共潜在因子向量（$m \ll p$）。
> - $\boldsymbol{\epsilon}$ 为 $p$ 维特异方差与误差向量，假定 $\text{Cov}(\mathbf{f}, \boldsymbol{\epsilon}) = \mathbf{0}$。
>
> **数学直觉** 观测变量之间的相关性完全由底层的公共因子 $\mathbf{f}$ 产生；一旦控制了这几个公共因子，观测变量之间的残差方差相互独立。这与单纯进行几何旋转重组的总方差主成分分析（PCA）具有本质认识论区别。

> [!formula-step] 公式步骤　KMO 样本充分性度量
> $$ \text{KMO} = \frac{\sum_{i \neq j} \sum r_{ij}^2}{\sum_{i \neq j} \sum r_{ij}^2 + \sum_{i \neq j} \sum a_{ij}^2} $$
>
> **这个公式在做什么** 检验变量间的简单相关与偏相关比例，评估观测数据是否满足因子提取的先决条件。
>
> **符号说明** $r_{ij}$ 为变量 $i$ 与 $j$ 的简单零阶相关系数；$a_{ij}$ 为控制其他所有变量影响后的偏相关系数（Partial Correlation）。
>
> **数学直觉** 若观测题项共享潜在公共因子，排除共同因子影响后的变量间净偏相关 $a_{ij}$ 应当极小，公式分母与分子趋同，$\text{KMO}$ 逼近 1；反之若变量间彼此孤立，偏相关较大，$\text{KMO}$ 趋近于 0。
>
> **判断标准** 评价阶梯：$> 0.90$ 极佳（Marvelous）；$0.80 - 0.89$ 良好（Meritorious）；$0.70 - 0.79$ 中等适宜（Middling）；$0.60 - 0.69$ 勉强可接受（Mediocre）；$< 0.50$ 不适宜进行因子分析。

> [!software-impl] 软件实现与报告规范
> - **数据处理** 缺失值多重插补或成列剔除、定序多分类变量在非正态严重时考虑多分格相关矩阵（Polychoric Correlation Matrix）。
> - **推荐软件** R（`psych::fa` 包）、SPSS（`Analyze -> Dimension Reduction -> Factor`）、SAS（`PROC FACTOR`）、Python（`factor_analyzer` 库）。
> - **操作流程** 选取主轴因子提取；指定斜交 Promax 旋转（通常 $\kappa = 4$）；设定载荷绝对值阈值（如载荷 $< 0.30$ 在输出表格中抑制显示）；输出因子得分用于后续建模。
> - **报告标准** 必须完整报告 KMO 系数与 Bartlett 检验卡方及显著性、提取方法与旋转算法、各因子的初始特征值与旋转后方差解释百分比、清洗后的模式载荷矩阵、各题项共同度、以及各分量表的 Cronbach's $\alpha$ 信度。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**
>   - 编制新问卷量表并初步探查理论构念的维度划分。
>   - 治理研究中面对海量政策工具评价（如几十项改革举措），通过因子分析降维提取出核心政策价值维度，并为后续基于因子得分的聚类类型学（Cluster Analysis）提供指标基础。[[Argument_Altrichter_2019_ZfB|(Altrichter et al., 2019, pp. 24–27)]]
> - **谨慎使用**
>   - 变量间相关性极弱（多数相关系数 $< 0.30$）或 KMO 低于 0.60，强行提取会导致因子碎裂且无理论意义。
> - **不适合使用**
>   - 理论构念已具有非常成熟且经严格验证的测度模型；此时应直接采用[[Confirmatory Factor Analysis|验证性因子分析]]（CFA）进行模型拟合优度检验。

---

## 局限性

> [!method-limits] 方法局限与方法论风险
> - **与主成分分析（PCA）的混淆误用** 统计软件（如 SPSS）常将 PCA 作为默认选项。PCA 是对变量总方差进行全量无损旋转压缩，不区分公共方差与测量误差，容易虚高因子载荷并产生概念膨胀；建构心理或教育特质测量时必须选用真正的公共因子模型（如主轴因子法 PAF 或最大似然法 ML）。
> - **旋转与维数判定的主观裁量性** 不同的因子保留准则（Kaiser 准则在变量多时容易高估因子数，碎石图带有主观肉眼判断偏差）和旋转方式可能产生不同的维度切分方案，依赖研究者的专业理论把关。
> - **缺乏跨样本恒常性检验** EFA 生成的因子结构属于数据驱动结果，极易受特定样本特征扰动；规范研究通常要求在样本分割或收集全新独立样本后，执行 CFA 结构验证与跨群体测量等值性（Measurement Invariance）检验。

---

## 实证数据

> [!ref-table]- 关键实证测量与因子结构
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究文献 | 样本规模与抽取范围 | 提取与旋转方法 | 检验参数 | 提取出的因子构念与测量题项 | 因子信度与方差解释 | 治理实务应用 |
> |---|---|---|---|---|---|---|
> | [[Argument_Altrichter_2019_ZfB\|Altrichter et al. (2019, p. 24)]] | 奥地利施泰尔马克州普通公立义务教育学校校长（$N = 362$） | 主轴因子法（Principal Axis Factoring, PAF）结合斜交 Promax 旋转 | $\text{KMO} = 0.81$（良好）；Bartlett 球形检验 $p < .001$ | **从 22 项治理工具中提取出 5 个公共因子**（剔除 3 项低载荷题项）：<br>1. **学校督导与质量对话（Schulaufsicht / SQA）**（4 题）<br>2. **产出监控与循证规制（Evidenzbasierte Steuerung）**（5 题）<br>3. **治理资源追加与自主权（Ressourcen / Autonomie）**（3 题）<br>4. **校内协同与人事发展（Interne Kooperation）**（4 题）<br>5. **专业进修与跨校网络（Fortbildung / Netzwerke）**（3 题） | 累积方差解释率 $42.1\%$；各因子 Cronbach's $\alpha$ 介于 $0.60$ 至 $0.74$ | 提炼出指标标准化因子得分，作为后续 $k$ 均值聚类分析（Cluster Analysis）的直接输入特征，成功将校长分化为循证型、资源型与弱发展型三类群体 |

---

## 使用此方法的研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Altrichter_2019_ZfB|Altrichter et al. (2019)]] — 运用主轴因子分析结合 Promax 斜交旋转，在 $\text{KMO} = 0.81$ 支持下将奥地利校长对 22 项教育治理工具的态度降维提炼为 5 个核心政策维度（解释 42.1% 方差），并为后续聚类分析奠定了特征向量基础。
> - [[Argument_Bergeron_2015_TeachingTOK|Bergeron & Rogers (2015)]] — 量化部分利用探索性因子分析（EFA，带主成分提取）检验了包含 11 道题的教学信心量表结构，确认其单一维度结构并解释了 35.03% 的累积方差。
> - [[Argument_Lodewyk_2007_EP|Lodewyk (2007)]] — 对 447 名十年级中学生的 Schommer 修订版[[Epistemology|认识论]][[Questionnaire|问卷]]（[[Schommer's Modified Epistemological Questionnaire|SMEQ]]）52 个题项进行主轴探索性因子分析与方差最大旋转，提取出固定与快速学习能力（FQAL）、[[Simplicity of Knowledge|简单知识]]（SK）和确定知识（CK）三个核心因子（解释 16.81% 方差）。
> - [[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|Kazancı Tınmaz & Sezgin (2023)]] — 对 310 名中小学教师的 56 个初测题项进行主轴因子提取法（Principal Axis Factoring, PAF）与方差最大正交旋转（Varimax Rotation），经矫正题总相关与载荷准则逐题筛选，在 [[KMO and Bartlett's Test of Sphericity|KMO 系数]]（$\text{KMO} = 0.966$）支持下，最终提取出涵盖技能、态度、使用与意识的 4 因子 20 题结构（解释 62.602% 累积方差）。
