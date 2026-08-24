---
title: Meta-meta-analysis
aliases:
  - 元-元分析
  - 元元分析
  - mega-analysis
  - meta-synthesis
  - 元综合
  - super-analysis
  - super-synthesis
  - Second-Order Meta-Analysis
  - 二阶元分析
  - 二级元分析
  - SOMA
summary: "在更高层级汇总多个已发表元分析结果的统计综合方法，运用多水平层级效应与稳健方差估计处理大型证据库并探索全领域异质性来源"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 35
method_related_level: 4
method_related_stars: "⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - statistics/meta-analysis
  - theme/meta-meta-analysis
  - field/research-methodology
related_concepts:
  - "[[Document]]"
  - "[[Effect Size]]"
  - "[[Sampling Error]]"
  - "[[Construct]]"
  - "[[Heterogeneity]]"
  - "[[Interaction Effect]]"
  - "[[Confidence Interval]]"
  - "[[External Validity]]"
  - "[[Epistemology]]"
  - "[[Positivism]]"
  - "[[Standard Error]]"
  - "[[Internal Validity]]"
  - "[[Metacognition]]"
  - "[[Creativity]]"
  - "[[Paradigm]]"
  - "[[Variable]]"
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Hypothesis]]"
  - "[[Reliability]]"
  - "[[Publication Bias]]"
  - "[[Critique of Meta-meta-analysis]]"
related_theories:
  - "[[Walberg's Educational Productivity Model]]"
related_methods:
  - "[[Meta-analysis]]"
  - "[[Meta-regression]]"
  - "[[Robust Variance Estimation]]"
  - "[[Coding in Qualitative Research]]"
  - "[[Fixed-Effect and Random-Effects Models]]"
  - "[[Pearson Product-Moment Correlation]]"
  - "[[Effect Size Conversion]]"
related_instruments:
  - "[[AMSTAR]]"
related_arguments:
  - "[[Argument_Terhart_2011_JCS]]"
  - "[[Argument_Runco_2026_CRJ]]"
  - "[[Argument_Higgins_2016_RE]]"
  - "[[Argument_Wecker_2016_ZfE]]"
confidence: high
status: draft
created: 2026-05-03
updated: 2026-08-24
---

# Meta-meta-analysis

---

## 定义

> [!def] 方法定义
> [[Meta-meta-analysis|元-元分析]]（Meta-[[Meta-analysis]]，在现代统计学中亦称二阶元分析 Second-Order Meta-Analysis, SOMA，早期[[Document|文献]]称 Mega-analysis 或 Meta-synthesis）指在更高统计层级上对多个已发表[[Meta-analysis|元分析]]（Meta-analysis）结果进行系统检索、方法学质控与定量合成的方法体系。与一阶元分析综合原始主要研究不同，二阶元分析以一阶元分析提取的汇总[[Effect Size|效应量]]（及其背后的[[Sampling Error|抽样误差]]结构）为分析单位，旨在估计宏观领域效应量基准、比较不同[[Construct|理论构念]]与干预维度的相对有效性，并识别全领域效应[[Heterogeneity|异质性]]的深层来源。[[Argument_Terhart_2011_JCS|(Terhart, 2011, p. 436)]]; [[Argument_Runco_2026_CRJ|(Runco et al., 2026, p. 2)]]

> [!method-scope] 方法范围
> - **研究对象** 已发表或灰色文献中关于特定主题的系统评价与一阶元分析汇总效应量矩阵。
> - **问题类型** 评估跨领域宏观效应量强度、检验不同理论构念或干预模式的相对差异、探索出版偏倚与方法学质量的[[Interaction Effect|调节效应]]。
> - **分析单位** 纳入的一阶元分析或其报告的独立一阶效应量集群（Clusters）。
> - **输出形式** 经小研究效应偏倚校正后的二阶总体效应量点估计值（$r$ 或 $g$）、95% [[Confidence Interval|置信区间]]（CI）、95% 预测区间（PI）及多水平二阶[[Meta-regression|元回归]]调节系数。

> [!citation-card]- 关键定义
> 二阶元分析在大样本水平上整合多重一阶元分析，采用[[AMSTAR|系统评价质量评估工具]]与多水平[[Robust Variance Estimation|稳健方差估计]]，能够克服单一研究局限，提供高度稳健且具备[[External Validity|可推广性]]的效应量基准。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, pp. 2–5)]]
>
> *Second-order meta-analyses synthesize the findings of previous meta-analyses to provide a higher-order summary of evidence... controlling for dependencies through cluster-robust variance estimation.*

---

## 方法定位与层级结构

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 秉持累积性[[Positivism|实证主义]]与多水平层次证据观，认为通过对多个独立[[Meta-analysis|元分析]]的系统加权与聚类方差建模，能够逼近真实总体的宏观效应并识别理论边界。
> - **研究者角色** 研究者必须执行严格的先验检索方案（PRISMA）、独立的双人方法学[[Coding in Qualitative Research|编码]]（[[AMSTAR]]）以及对一阶[[Effect Size|效应量]]依赖结构的客观建模，避免主观证实偏差。
> - **有效性标准** 遵循统计结论效度（通过 CHE 与 [[Robust Variance Estimation|RVE]] 校正[[Standard Error|标准误]]膨胀）、[[Internal Validity|内部效度]]（检验主要研究重叠与偏倚传播）及[[External Validity|外部效度]]（大样本全领域覆盖）。
> - **不声称回答的问题** 不能脱离一阶研究的质量上限凭空消除测量偏倚；不能单凭边际效应量排名直接推断复杂教育情境中的因果充分性。

> [!contrast-table] 一阶元分析 vs 传统元综合 vs 现代多水平二阶元分析
> | 比较维度 | 一阶元分析（Meta-analysis） | 传统元综合（如早版 Hattie） | 现代多水平二阶元分析（[[Argument_Runco_2026_CRJ\|Runco et al., 2026]]） |
> |---|---|---|---|
> | **分析单位** | 原始实证研究（Primary Studies） | 已发表一阶元分析的汇总 $d$ | 一阶元分析汇总效应量及其多水平依赖集群 |
> | **质量准入** | 原始研究设计筛选 | 粗放纳入、声称不关心质量 | 严格基于 AMSTAR 12 项准则设定质量门槛（$\ge 0.75$） |
> | **统计模型** | 单级固定效应 / [[Fixed-Effect and Random-Effects Models\|随机效应模型]] | 伪固定效应模型、简单未加权平均 | 相关与层级效应工作模型（CHE）+ 稳健方差估计（RVE） |
> | **偏倚控制** | 漏斗图、经典艾格回归 | 无偏倚检验与校正 | 多水平改进艾格回归（Multilevel Egger's Test）截距校正 |
> | **核心目的** | 检验具体干预或相关关系的平均效应 | 建立宏观排名联盟表（League Table） | 估计宏观效应基准、分解全领域[[Heterogeneity\|异质性]]、检验理论调节模型 |

---

## 历史演变与范式演进

> [!phase] 二阶[[Meta-analysis|元分析]]的四个发展阶段
>
> - **早期探索与教育生产力模型检验（1980s）**
>
>   Glass 提出元分析 10 年后，Fraser, Walberg & Hattie（1987）首次综合了 226 项元分析以检验 Walberg 的[[Walberg's Educational Productivity Model|教育生产力模型]]，涵盖数千项原始研究，开创了跨元分析大规模统计汇总的先河。[[Argument_Higgins_2016_RE|(Higgins, 2016, pp. 41–42)]]
>
> - **大一统通用连续体与气压计排名（1990s–2000s）**
>
>   Hattie（1992, 2008）综合 800 多项元分析（涵盖 5 万多项研究、8000 多万学生），建立标准差单位的通用连续体（Universal Continuum），提出 $d = 0.40$ 的影响气压计关节点并生成 138 项干预排名，使二阶综合进入全球政策话语，但也因未加权平均与忽略研究重叠引发了广泛的方法论批评。[[Argument_Terhart_2011_JCS|(Terhart, 2011, pp. 427–428)]]
>
> - **理论驱动的构念精细化分类（1998）**
>
>   Marzano（1998）综合 100 多项元分析，系统批评了将不同干预成分打包为粗放品牌名（Brand-name）聚合的做法，提出按认知、[[Metacognition|元认知]]、自我系统等四层学习机制细化分类，推动元综合走向机制解释。[[Argument_Higgins_2016_RE|(Higgins, 2016, pp. 42–43)]]
>
> - **现代多水平稳健统计推断模型（2013–至今）**
>
>   Schmidt & Oh（2013）提出二阶[[Sampling Error|抽样误差]]估计理论；[[Argument_Runco_2026_CRJ|Runco et al. (2026)]]在[[Creativity|创造力]]研究中确立了由 PRISMA 检索、[[AMSTAR]] 方法学评估、[[Effect Size|效应量]]正态化转换、CHE 多水平工作模型与 [[Robust Variance Estimation|RVE]] 三明治估计量组成的现代二阶元分析规范[[Paradigm|范式]]。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, pp. 2–6)]]

---

## 现代二阶元分析研究程序

> [!proc] 现代二阶[[Meta-analysis|元分析]]六步标准操作规程
> 1. **多数据库系统检索与灰色[[Document|文献]]扩展** 检索主流学术数据库与博硕士论文库，遵循 PRISMA 声明进行四阶段筛选，严格排除缺乏定量合并矩阵的质性综述与无关系[[Effect Size|效应量]]的坐标元分析。
> 2. **[[AMSTAR]] 12 项方法学质量评估** 采用改编的 AMSTAR 准则进行双人独立[[Coding in Qualitative Research|编码]]（一致率 $\ge 95\%$），设定得分阈值（如 $\ge 0.75$）作为高质量指示[[Variable|变量]]。
> 3. **效应量标准化转换与正态化** 将不同一阶指标统一转换为[[Pearson Product-Moment Correlation|皮尔逊相关]]系数 $r$ 或标准化均值差 $g$，运用 Fisher's $z$ 变换实现方差稳定化。
> 4. **多水平 CHE 与 [[Robust Variance Estimation|RVE]] 稳健方差建模** 设定集群内相关系数（$\rho = 0.8$），运用经验残差构造三明治估计量，计算稳健[[Standard Error|标准误]]与小样本 $F$ 检验。
> 5. **多水平改进艾格回归偏倚检验与校正** 检验小研究效应并根据回归模型截距输出偏倚校正后的二阶效应量点估计值与[[Confidence Interval|置信区间]]。
> 6. **二阶[[Meta-regression|元回归]]与亚组调节变量检验** 纳入[[Construct|理论构念]]类型、[[Independent Variable|自变量]]/[[Dependent Variable|结果变量]]角色、研究设计等调节变量，全面分解效应[[Heterogeneity|异质性]]来源。

---

## 核心统计模型与数学公式

> [!formula-set] 二阶[[Meta-analysis|元分析]]统计推断与加权建模流程
> ```mermaid
> flowchart LR
>   A["一阶元分析效应量 z_ij<br/>(嵌套于一阶元分析 j)"] --> B["三水平方差分解<br/>σ²_3(研究间) + σ²_2(研究内) + V_ij(抽样)"]
>   B --> C["相关与层级效应工作模型 (CHE)<br/>设定协方差矩阵 V (ρ=0.8)"]
>   C --> D["稳健方差估计 (RVE)<br/>构造经验三明治估计量 V_R"]
>   D --> E["多水平艾格回归偏倚校正<br/>估计截距 β_0 与 95% CI/PI"]
>   E --> F["二阶元回归模型<br/>全变量调节检验 (Wald F 检验)"]
> ```

---

### 1. 固定效应二级汇总的数学等价性与方法论条件

> [!formula-step] 公式步骤　固定效应二级汇总等价性定理
> $$d_{\text{second}} = \frac{\sum_{j=1}^{m} w_j d_j}{\sum_{j=1}^{m} w_j} = \frac{\sum_{j=1}^{m} \left(\sum_{i=1}^{k_j} w_{ji}\right) d_j}{\sum_{j=1}^{m} \left(\sum_{i=1}^{k_j} w_{ji}\right)} = \frac{\sum_{\text{all } i} w_i d_i}{\sum_{\text{all } i} w_i}$$
>
> **这个公式在做什么** 证明当且仅当所有一阶元分析纳入的主要研究**互不重叠**且严格按精度反比（$w_j = 1/v_{d_j}$）加权时，二级固定效应元分析才在数学上等价于对所有原始研究直接进行的一级元分析。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 24–28)]]
>
> **推导过程与数学原理**
> 1. 第一级元分析 $j$ 对主要研究 $i$ 进行加权估计：$d_j = \frac{\sum w_{ji} d_{ji}}{\sum w_{ji}}$，其方差为 $v_{d_j} = \frac{1}{\sum w_{ji}}$。
> 2. 第二级元分析对一阶元分析 $j$ 进行加权估计：$w_j = 1/v_{d_j} = \sum_{i=1}^{k_j} w_{ji}$。
> 3. 代入二级汇总公式展开即得公式右端：$d_{\text{second}} = \frac{\sum_{\text{all } i} w_i d_i}{\sum_{\text{all } i} w_i}$。
>
> **注意事项** 若一级元分析间存在重复研究，该研究的数据被重复计数，人为压缩了[[Standard Error|标准误]]并严重扭曲点估计；因此现代二阶元分析必须采用处理聚类依赖性的多水平模型。

---

### 2. 相关与层级效应工作模型（Correlated and Hierarchical Effects Model, CHE）

> [!formula-step] 公式步骤　CHE 三水平[[Fixed-Effect and Random-Effects Models|随机效应模型]]
> $$z_{ij} = \beta_0 + \sum_{p=1}^P \beta_p X_{p,ij} + \zeta_{(3)j} + \zeta_{(2)ij} + \epsilon_{ij}$$
> $$\operatorname{Var}(\zeta_{(3)j}) = \tau_3^2, \quad \operatorname{Var}(\zeta_{(2)ij}) = \tau_2^2, \quad \operatorname{Var}(\epsilon_{ij}) = V_{ij}$$
>
> **这个公式在做什么** 将一阶[[Effect Size|效应量]] $z_{ij}$ 的总方差分解为三层：一阶元分析间变异 $\tau_3^2$（Level 3）、同一元分析内不同效应量间变异 $\tau_2^2$（Level 2）以及主要研究已知的抽样方差 $V_{ij}$（Level 1）。
>
> **推导过程与数学原理**
> 1. 考虑来自同一一阶元分析 $j$ 的多个效应量存在相关性，设定集群内相关系数为 $\rho$（通常在敏感性检验中设定 $\rho = 0.8$）。
> 2. 构建块对角已知抽样协方差工作矩阵 $V_j$，其中对角线元素为 $V_{ijj} = 1/(n_{ij}-3)$，非对角线协方差为 $\operatorname{Cov}(z_{aj}, z_{bj}) = \rho \sqrt{V_{aj} V_{bj}}$。
> 3. 采用限制极大似然法（REML）联合估计[[Heterogeneity|研究间异质性]]方差分量 $\tau_3^2$ 与 $\tau_2^2$。
>
> **结果怎么读** 异质性方差比率 $I_{(3)}^2 = \frac{\tau_3^2}{\tau_3^2 + \tau_2^2 + \bar{V}}$ 与 $I_{(2)}^2 = \frac{\tau_2^2}{\tau_3^2 + \tau_2^2 + \bar{V}}$ 分别反映二阶元分析间与元分析内的真实效应离散比例。

---

### 3. 稳健方差估计与三明治估计量（Robust Variance Estimation, RVE）

> [!formula-step] 公式步骤　聚类稳健三明治方差估计量
> $$V_R = \left( \sum_{j=1}^m X_j' W_j X_j \right)^{-1} \left( \sum_{j=1}^m X_j' W_j e_j e_j' W_j X_j \right) \left( \sum_{j=1}^m X_j' W_j X_j \right)^{-1}$$
>
> **这个公式在做什么** 在 CHE 工作模型设定的相关系数 $\rho$ 不完全准确甚至协方差结构误设的条件下，基于经验残差向量 $e_j$ 给出渐近无偏、稳健的标准误与[[Hypothesis|假设]]检验结果。
>
> **推导过程与数学原理**
> 1. 设广义最小二乘（GLS）权重矩阵为 $W_j = (\tau_3^2 I + \tau_2^2 J + V_j)^{-1}$。
> 2. 残差向量定义为 $e_j = z_j - X_j \hat{\beta}$。
> 3. 利用经验外积矩阵 $\sum X_j' W_j e_j e_j' W_j X_j$ 替代未知的真实协方差矩阵，形成经典的“面包-肉-面包”[[Robust Variance Estimation|三明治估计量]]结构。
> 4. 配合 Tipton & Pustejovsky（2015）的小样本自由度调整，采用 Hotelling $T^2$ 近似进行稳健 $F$ 检验，有效控制假阳性错误率。
>
> **结果怎么读** 即使一阶效应量之间存在未知的复杂交叉重叠，RVE 也能保证[[Confidence Interval|置信区间]]和 $p$ 值的严格可[[Reliability|信度]]。

---

### 4. 多水平偏倚校正艾格回归模型（Multilevel Egger's Test）

> [!formula-step] 公式步骤　多水平艾格回归偏倚检验
> $$z_{ij} = \beta_0 + \beta_{\text{SE}} \sqrt{V_{ij}} + \zeta_{(3)j} + \zeta_{(2)ij} + \epsilon_{ij}$$
>
> **这个公式在做什么** 检验全领域是否存在小研究效应与[[Publication Bias|发表偏倚]]（Publication Bias），并通过回归截距 $\beta_0$ 估计剔除小样本膨胀效应后的无偏二阶效应量。
>
> **数学原理与读法**
> - 若斜率系数 $\beta_{\text{SE}}$ 显著（$p < 0.05$），表明效应量大小与抽样标准误显著正相关，证实存在显著的小研究偏倚；
> - 截距项 $\beta_0$ 即代表当[[Sampling Error|抽样误差]]趋近于 0（理论无限大样本）时的二阶真实效应量估计值，通过 $\tanh(\beta_0)$ 还原为相关系数汇报。

---

## 软件实现与代码规程

> [!software-impl] R 语言多水平二阶[[Meta-analysis|元分析]]实现代码
> ```R
> library(metafor)
> library(clubSandwich)
> 
> # 1. 效应量转换与计算抽样方差（Fisher's z）
> dat <- escalc(measure = "ZCOR", ri = r_val, ni = n_sample, data = raw_data)
> 
> # 2. 构建 CHE 协方差工作矩阵（设定集群内相关系数 rho = 0.8）
> V_mat <- impute_covariance_matrix(vi = dat$vi, cluster = dat$meta_id, r = 0.8)
> 
> # 3. 拟合三水平 CHE 随机效应模型
> model_che <- rma.mv(yi, V_mat, random = ~ 1 | meta_id / effect_id, 
>                     data = dat, sparse = TRUE)
> 
> # 4. 应用 RVE 稳健方差估计（CR2 小样本校正）
> robust_res <- coef_test(model_che, vcov = "CR2", cluster = dat$meta_id)
> 
> # 5. 多水平二阶元回归调节检验
> model_reg <- rma.mv(yi ~ predictor_type + study_design + amstar_high, 
>                     V_mat, random = ~ 1 | meta_id / effect_id, data = dat)
> robust_reg <- Wald_test(model_reg, constraints = constrain_predictors(model_reg), 
>                         vcov = "CR2", cluster = dat$meta_id)
> ```

---

## 方法学局限与学术争议总览

> [!warning] 方法学局限与争议提示
> 二阶[[Meta-analysis|元分析]]虽然在统计技术上实现了多水平稳健化，但在[[Epistemology|认识论]]和证据应用层面仍面临多重系统性挑战：
> 1. **试验灵敏度混淆** [[Effect Size|效应量]]大小可能反映研究者操纵试验灵敏度的难易程度而非干预本身有效性；
> 2. **偏倚逐级复合** 一阶元分析中的错误和偏倚无法在二阶统计中被自动消除；
> 3. **因果机制距离** 宏观抽象聚合使结果远离了具体课堂情境中的实在因果机制。
>
> 完整详尽的批判脉络、数学反例、透明度重构与案例剖析详见专门理论条目：
> 🔗 **[[Critique of Meta-meta-analysis|元-元分析批判]]（Critique of Meta-meta-analysis）**。

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关联方向 | 说明 |
> |:-----|:-----|:---------|:-----|
> | [[Critique of Meta-meta-analysis]] | 概念 | 方法学反思 | 系统阐释元-[[Meta-analysis\|元分析]]在[[Epistemology\|认识论]]、测量错位与政策误用层面的理论批判。 |
> | [[Effect Size Conversion]] | 方法 | 计算前置 | 二阶元分析依赖[[Effect Size\|效应量]]转换统一不同一阶研究的量规尺度。 |
> | [[Robust Variance Estimation]] | 方法 | 核心统计 | RVE 三明治估计量是解决二阶聚类依赖性与小样本膨胀的支柱技术。 |
> | [[AMSTAR]] | 工具 | 质量控制 | 用于二阶元分析中对一阶元分析规范度进行量化评级的方法学工具。 |
> | [[Argument_Runco_2026_CRJ\|Runco et al. (2026)]] | 论证 | 典范应用 | [[Creativity\|创造力]]领域二阶元分析代表作，确立了现代六步建模与偏倚校正规程。 |
> | [[Argument_Wecker_2016_ZfE\|Wecker et al. (2016)]] | 论证 | 数学证明 | 推导二级固定效应等价性的 6 项数学要求，揭示粗糙元综合的计算失真。 |
