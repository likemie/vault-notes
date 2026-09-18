---
title: Cluster Analysis
aliases:
  - 聚类分析
  - K-Means Cluster Analysis
  - k均值聚类分析
  - 类别分析
summary: "一种用于将异质性样本依据多维变量特征相似度划分为若干同质子群体的无监督统计分类方法，在教育治理与领导力研究中常用于构建行动者偏好或实践模式的经验形态学。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 22
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - method/classification
  - method/clustering
related_concepts:
  - "[[Variable]]"
  - "[[Heterogeneity]]"
  - "[[Research Question]]"
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Dialogue in Education]]"
  - "[[Dependent Variable]]"
  - "[[Flow]]"
  - "[[Output-Oriented Governance]]"
  - "[[Evidence-Based School Development]]"
related_methods:
  - "[[Questionnaire]]"
  - "[[Intraclass Correlation Coefficient]]"
  - "[[Survey Research]]"
  - "[[Likert Scale]]"
  - "[[Analysis of Variance]]"
  - "[[Effect Size]]"
  - "[[Sample Size Determination]]"
  - "[[Standard Error]]"
  - "[[Split-Half Reliability]]"
  - "[[Cluster Sampling]]"
  - "[[Correlational Research]]"
related_arguments:
  - "[[Argument_Altrichter_2019_ZfB]]"
confidence: high
status: draft
created: 2026-09-18
updated: 2026-09-18
---

# Cluster Analysis

---

## 定义

> [!def] 方法定义
> **聚类分析（Cluster Analysis）** 是一种无监督多元统计分类方法，旨在依据观测对象在多个特征[[Variable|变量]]上的相似度或距离测度，将未经标注的[[Heterogeneity|异质性]]样本划分为若干个互不重叠或层次嵌套的同质子群体（即数据簇）。其核心操作原则在于追求簇内相似度最大化与簇间差异度最大化。在教育治理与学校组织研究中，聚类分析常被用于从复杂的态度[[Questionnaire|问卷]]或行为调查中识别出具有典型表征的行动者类型学。[[Argument_Altrichter_2019_ZfB|(Altrichter et al., 2019, p. 27)]]

> [!method-scope] 方法范围
> - **研究对象** 个体行动者（如校长、教师、学生）、学校组织、区域教育行政单元或国家/国际评价指标体系的多维特征分布。
> - **问题类型** 适合回答潜藏分类、类型学构建、人群异质性探索与组间特征对比等探索性[[Research Question|研究问题]]。
> - **[[Unit of Analysis|分析单位]]** 个体、学校、地区或多指标观测单元。
> - **输出形式** 聚类归属类别变量、聚类中心剖面向量、各变量对分群贡献的判别指标（如[[Intraclass Correlation Coefficient|组内相关系数]]）以及后续组间差异检验结果。

> [!citation-card] 聚类分析的类型构建功能
> 聚类分析是一种用于构建类型学的方法，其使得同一聚类内部的单元具有显著高于不同聚类之间的相似性。[[Argument_Altrichter_2019_ZfB|(Altrichter et al., 2019, p. 27)]]
>
> *Die Clusteranalyse ist ein Verfahren zur Konstruktion von Typologien, wobei Einheiten innerhalb eines Clusters deutlich größere Ähnlichkeit untereinander aufweisen als zwischen verschiedenen Clustern.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 认为复杂社会与教育现象中的个体并非均质分布，而是存在受潜在结构与价值倾向所塑造的自然聚集形态；经验数据内部蕴含客观的几何邻近与模式结构。
> - **研究者角色** 在距离测度选取（如欧几里得距离、曼哈顿距离）、聚类算法（层次聚类 vs 划分式聚类）、聚类数目 $K$ 的界定以及对最终聚类轮廓的理论诠释中，高度依赖研究者的专业理论判断与实质性概念[[Dialogue in Education|对话]]。
> - **有效性标准** 依靠统计指标（如组内误差平方和下降拐点、轮廓系数（Silhouette Coefficient）、组间方差比）与理论可解释性的双重收敛进行效度检验。
> - **不声称回答的问题** 聚类分析纯属探索性描述分类工具，不能推导因果机制；分群结果高度依赖所选取的指标[[Variable|变量]]集与尺度变换方法。

> [!method-stack] 方法层级
> - **研究设计** [[Survey Research|调查研究]]、评价数据挖掘、横截面实证分析。
> - **数据收集** 多维度[[Likert Scale|李克特量表]][[Questionnaire|问卷]]、行政追踪数据、大规模测试背景问卷。
> - **分析方法** $k$ 均值聚类（$k$-Means Clustering）、系统层次聚类（Hierarchical Clustering）、潜类别分析（Latent Class Analysis, LCA）。
> - **辅助技术** 变量标准化（$Z$-Score）、[[Intraclass Correlation Coefficient|组内相关系数]]（Intraclass Correlation Coefficient, ICC）判别检验、单因素[[Analysis of Variance|方差分析]]（Analysis of Variance, ANOVA）与事后两两检验（Post-hoc Test）。

---

## 研究程序

> [!proc] 通用程序
> 1. **明确分类目标与理论[[Variable|变量]]** 选取具有实质理论关联的测量指标构建特征空间，剔除高度共线性的冗余变量。
> 2. **数据标准化与距离度量** 对量纲不一的特征变量进行标准化处理，计算样本点间的几何距离（如欧几里得距离）。
> 3. **聚类数试验与最优解判定** 预先设定多种群组数量方案（例如测试 2 至 5 个群组），综合统计拟合优度与理论可诠释性确定最优聚类数目。
> 4. **算法迭代与中心收敛** 运用迭代优化算法交替更新聚类归属与聚类中心，直至收敛条件满足。
> 5. **群组特征提炼与效度验证** 绘制聚类剖面图（Profile Plot），计算各变量在群组间的区分度指标，并引入外部[[Dependent Variable|效标变量]]进行跨组单因素[[Analysis of Variance|方差分析]]检验。

### 量化方法模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 横截面连续型或定序多变量矩阵（$N \times P$）。
> - **样本与单位** $N$ 个观测样本（如学校校长），每个样本包含 $P$ 项特征得分。
> - **变量或指标** 态度评价题项、行为频次指标、时间分配比例等连续或准连续变量。
> - **模型或统计量** 簇内误差平方和（Sum of Squared Errors, SSE）、[[Intraclass Correlation Coefficient|组内相关系数]]（ICC）、单因素方差分析 $F$ 检验、[[Effect Size|效应量]] $\omega^2$ 与 Cohen's $d$。
> - **诊断与检验** 极端值清理、局部最优陷阱排查（多次随机初始中心点）、组间方差分析及轮廓稳定性检验。

> [!formula-step] 公式步骤　$k$ 均值目标函数（簇内误差平方和）
> $$SSE = \sum_{k=1}^{K} \sum_{x_i \in C_k} \|x_i - \mu_k\|^2$$
>
> **这个公式在做什么** 计算所有样本点到其所属聚类中心点的欧几里得距离平方和，算法通过不断重新指派样本归属以使该总误差平方和最小化。
>
> **符号说明**
> - $K$ 为预先设定的聚类总数。
> - $C_k$ 为第 $k$ 个聚类集合。
> - $x_i$ 为第 $i$ 个观测样本的多维特征向量。
> - $\mu_k$ 为第 $k$ 个聚类的中心均值向量（Centroid）。
>
> **数学直觉** 将多维空间中的数据点划分至距离最近的中心，通过最小化总体离散度实现聚类的高紧凑性。
>
> **结果怎么读** $SSE$ 随着 $K$ 的增加而单调递减；在碎石图（Scree Plot）中寻找边际递减幅度显著减缓的肘部拐点（Elbow）作为选择适宜聚类数的重要参考。
>
> **注意事项** $k$ 均值聚类假定各簇具有凸集形状与均等方差，容易对极端异常值敏感，且容易收敛至局部最优解，故通常需多次随机启动以保证稳定性。

> [!software-impl] 软件实现
> - **数据处理** 变量标准化、缺失值填补或剔除。
> - **推荐软件** R（`stats::kmeans`、`cluster`）、Python（`scikit-learn.cluster.KMeans`）、SPSS（`K-Means Cluster`）。
> - **核心操作流程** 设置随机数种子保证可复现性；运行多组 $K$ 值解并输出各簇均值与方差分析表；结合方差解释率与理论清晰度确定最终解。
> - **报告标准** 完整报告[[Sample Size Determination|样本量]] $N$、聚类前处理规程、聚类算法参数、各簇样本占比、各题项在各簇的均值与[[Standard Error|标准误]]、组内相关系数（ICC）以及外部关联变量的方差检验结果。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 探索无先验标签的复杂样本形态，例如根据教师对不同教学策略的态度将其划分为教学观念亚群，或根据学校资源与效能配置提炼学校发展模式。[[Argument_Altrichter_2019_ZfB|(Altrichter et al., 2019, pp. 27–28)]]
> - **谨慎使用** [[Variable|变量]]之间存在极端高度相关（强多重共线性）时，会导致特定维度在聚类中被隐性赋予双倍或多倍权重；变量间量纲差异极大且未做标准化时亦会扭曲距离空间。
> - **不适合使用** 旨在检验严格因果假说、或[[Sample Size Determination|样本量]]极小以至于无法稳定估计聚类中心的实证设计。

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源** 初始中心点选择偏差（易陷入局部最优）、定序[[Variable|变量]]当做连续变量度量欧氏距离引入的度量误差、以及样本自选择偏误。
> - **适用边界** 聚类解的非唯一性：不同聚类数目方案各有统计优劣，最终选取往往带有研究者的理论主观色彩。
> - **误用风险** 将数据挖掘生成的经验群组直接实体化为本质主义的刚性人群标签，忽略群组边界处样本的不确定性。
> - **补救方式** 采用分半交叉验证（[[Split-Half Reliability|split-half]] Validation）、引入潜类别分析（LCA）等基于概率模型的稳健性检验工具，并在正文中透明呈现竞争性聚类数方案的统计对比。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Output-Oriented Governance]] | 理论概念 | 治理理论为聚类分析中的态度特征维度提供分类依据与实质性解释框架。 |
> | [[Cluster Sampling]] | 相关方法 | 抽样层面的群集划分方法，与观测特征空间的后验样本聚类在统计原理上形成空间与实体区分。 |

---

## 使用此方法的研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Altrichter_2019_ZfB|Altrichter et al. (2019)]] — 运用 $k$ 均值聚类分析对奥地利 362 名中小学校长对 22 项治理工具的态度进行分群，从 2 至 5 个聚类方案中选定具有最高方差分离度与理论解释力的 3 聚类解（[[Evidence-Based School Development|循证学校发展]]型、资源驱动发展型与弱发展取向型）。
