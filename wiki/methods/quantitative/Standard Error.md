---
title: Standard Error
aliases:
  - 标准误
  - standard error of the mean
  - 均值的标准误
  - standard error of proportions
  - 效应量标准误
summary: "度量样本统计量抽样分布离散度与估计精度的核心统计量，作为构建置信区间、显著性检验、元分析逆方差加权与元科学数据审计的数理基石"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 27
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - statistics/sampling
  - statistics/meta-analysis
  - field/research-methodology
related_concepts:
  - "[[Sampling Error]]"
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Publication Bias]]"
  - "[[Variable]]"
  - "[[Document]]"
  - "[[Primary and Secondary Documents]]"
  - "[[Direct Instruction]]"
  - "[[Inquiry-Based Learning]]"
related_theories:
  - "[[Central Limit Theorem]]"
related_methods:
  - "[[Effect Size]]"
  - "[[Random Sampling]]"
  - "[[Confidence Interval]]"
  - "[[Meta-analysis]]"
  - "[[Inverse-Variance Weighting]]"
  - "[[Statistical Significance]]"
  - "[[Sample Size Determination]]"
  - "[[Forest Plot]]"
  - "[[Causal Modeling]]"
  - "[[Experimental Research]]"
  - "[[Fixed-Effect Model]]"
  - "[[Research Synthesis]]"
  - "[[Robust Variance Estimation]]"
  - "[[Meta-meta-analysis]]"
related_persons:
  - "[[John Hattie]]"
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]]"
  - "[[Argument_Wecker_2016_ZfE]]"
confidence: high
status: completed
created: 2026-06-22
updated: 2026-10-30
---

---

> [!def] Standard Error
> 标准误（Standard Error, SE）是样本统计量（如均值、比例、回归系数、标准化均数差[[Effect Size|效应量]]）在理论[[Sampling Error|抽样分布]]上的标准差，度量样本估计值围绕总体真实参数的理论变异离散程度。它是[[Central Limit Theorem|中心极限定理]]的直接推论，量化了从样本推断总体时的[[Random Sampling|随机抽样]]不确定性幅度。SE 是构建[[Confidence Interval|置信区间]]（$CI = \text{点估计} \pm Z \times SE$）、执行假设检验以及[[Meta-analysis|元分析]][[Inverse-Variance Weighting|逆方差加权]]（$w = 1/SE^2$）的核心数理基石。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, Ch. 8, pp. 150–151)]]; [[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 25–27)]]

> [!method-scope] 方法范围
> - **研究对象** 样本均值、比例、相关系数、标准化均数差（Cohen's $d$, Hedges' $g$）及两级元分析合并效应量的抽样分布。
> - **问题类型** 量化点估计精度、检验[[Statistical Significance|统计显著性]]、构建参数置信区间、确定证据加权权重与规划目标[[Sample Size Determination|样本量]]。
> - **[[Unit of Analysis|分析单位]]** 随机抽样样本、实验处理组与对照组被试集群、纳入元分析的主要研究。
> - **输出形式** 标准误数值（$SE$）、95% 置信区间（95% CI）、逆方差统计权重（$W = 1/SE^2$）及标准误[[Forest Plot|森林图]]误差线。

> [!citation-card] 均值标准误的抽样变异性
> 抽样分布的标准差是抽样误差的度量，称为均值的标准误（[[Causal Modeling|SEM]]）。抽样误差取决于总体的变异性和样本量：总体变异性越小，抽样误差越小；样本量越大，抽样误差越小。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, Ch. 8, pp. 150–151)]]
>
> *The standard deviation of the theoretical distribution of sample means is a measure of sampling error and is called the standard error of the mean (SEM).*

> [!citation-card] 审查中的标准误混淆诊断
> 显然不是标准差的标准误。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, p. 27)]]
>
> *Offenbar wurde hier der Standardfehler statt der Standardabweichung verwendet.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** SE 度量的是从有限经验样本推断广义总体时固有的客观[[Random Sampling|随机抽样]]波动，体现了实证科学推断知识的概率性与渐近性。
> - **研究者角色** 要求研究者根据具体数据结构（单样本均值、分类比例、独立双组[[Experimental Research|实验设计]]或两级[[Meta-analysis|元分析]]）严密推导对应方差公式，严格防范将标准误与标准差（SD）混淆作为除数的计量事故。
> - **有效性标准** 满足大样本渐近正态性、无偏性、与[[Sample Size Determination|样本量]]方差相容性；在两级汇总中满足抽样独立性。
> - **不声称回答的问题** SE 仅度量随机[[Sampling Error|抽样误差]]，完全不能反映选择偏倚、测量工具系统误差或[[Publication Bias|发表偏倚]]等非随机性系统扭曲。

> [!contrast-table] 标准误（SE）与邻近概念多维辨析
> | 比较维度 | 标准误（Standard Error, SE） | 标准差（Standard Deviation, SD） | 抽样误差（Sampling Error） | 残差标准误（Residual Standard Error） |
> |:---|:---|:---|:---|:---|
> | **描述对象** | 样本统计量（均值、[[Effect Size\|效应量]]）抽样分布的离散度 | 原始观测样本数据点的经验离散度 | 样本估计值与总体真实参数之间的实际绝对差距 | 回归模型中观测值偏离拟合回归线的变异度 |
> | **数学公式** | $\text{SE} = \text{SD}/\sqrt{N}$ 或 $\text{SE}_d = \sqrt{v_d}$ | $\text{SD} = \sqrt{\frac{\sum(x_i - \bar{x})^2}{n-1}}$ | $e = \lvert \bar{x} - \mu \rvert$ | $\text{RSE} = \sqrt{\frac{\sum e_i^2}{n - p - 1}}$ |
> | **随样本量 $N$ 变化** | 随 $N$ 增大而以反比例 $1/\sqrt{N}$ 持续减小 | 随 $N$ 增大保持稳定收敛于总体标准差 $\sigma$ | 概率意义上随 $N$ 增大逐渐趋向于 0 | 随 $N$ 增大收敛于不可解释的随机扰动方差 |
> | **核心用途** | 构建参数 [[Confidence Interval\|置信区间]]、显著性检验、[[Inverse-Variance Weighting\|逆方差加权]] | 描述群体多样性、计算[[Effect Size\|效应量]]分母除数 | 评估抽样代表性与理论估计误差界限 | 评价回归方程模型拟合优度与预测带宽 |

---

> [!formula-set]- 标准误的四维公式演进与应用谱系
> ```mermaid
> flowchart LR
>   A["单样本均值标准误 SEM<br/>样本均值抽样分布精度评定"] --> B["分类比例标准误<br/>二项分布与有限总体校正"]
>   B --> C["双组效应量标准误<br/>标准化均数差抽样方差"]
>   C --> D["元分析联合标准误<br/>逆方差加权与多研究精度累加"]
> ```

---

### 公式步骤一　均值的标准误（SEM）与边际收益递减

> [!formula-step] 公式步骤　单样本均值的标准误
> $$\text{[[Causal Modeling|SEM]]} = \frac{\text{SD}_s}{\sqrt{N}}$$
>
> **这个公式在做什么** 接收样本数据的离散标准差 $\text{SD}_s$ 与[[Sample Size Determination|样本量]] $N$，计算样本均值[[Sampling Error|抽样分布]]的理论标准差，输出样本均值的估计精度。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, Ch. 8, pp. 150–151)]]
>
> **数学直觉** $N$ 位于分母开方位置。样本量扩大 4 倍，SEM 减半；样本量扩大 100 倍，SEM 缩小至十分之一。从小样本到大样本的初期精度收益巨大，后期呈现明显的边际效益递减规律。
>
> **结果解读与决策准则**
> - 少于 30 例的样本处于统计高危区间，允许过大的抽样误差存在；
> - 样本量超过约 80 例后，进一步单纯增加 $N$ 对压缩 SEM 的边际贡献显著放缓；
> - 总体变异性（$\sigma$）越大的[[Variable|变量]]（如智商 IQ 测验），将 SEM 压制在同一精度区间所需样本量远大于低变异变量。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, p. 152)]]

---

### 公式步骤二　分类比例的标准误与有限总体校正

> [!formula-step] 公式步骤　分类比例的标准误与有限总体校正（fpc）
> $$\text{SE}_p = \sqrt{\frac{P \times Q}{N}} \times \sqrt{\frac{N_{\text{pop}} - N}{N_{\text{pop}} - 1}}$$
>
> **这个公式在做什么** 接收分类二项分布比例 $P$（如合格率）、反面比例 $Q = 1 - P$、抽样量 $N$ 以及总体规模 $N_{\text{pop}}$，输出百分比估计值的抽样标准误。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, Ch. 8, p. 152)]]
>
> **数学直觉** 比例分布的抽样方差取决于 $P(1-P)$ 的乘积，在 $P = 0.5$ 时方差达到理论最大峰值；后一项为有限总体校正因子（finite population correction, fpc）。
>
> **结果解读与注意事项**
> - 当抽样比例较小（$N / N_{\text{pop}} < 5\%$）时，fpc 趋近于 1，可直接简写为 $\sqrt{PQ/N}$；
> - 当抽样量占总体比例超过 5% 时，fpc 显著小于 1，能够适度缩小 SE 并避免过度保守的区间估计。

---

### 公式步骤三　标准化均数差效应量（Cohen's d / Hedges' g）的抽样标准误

> [!formula-step] 公式步骤　独立双组实验[[Effect Size|效应量]]的抽样标准误
> $$\text{SE}_d = \sqrt{v_d} = \sqrt{\frac{n_E + n_C}{n_E \cdot n_C} + \frac{d^2}{2(n_E + n_C)}}$$
>
> **这个公式在做什么** 接收实验组与对照组样本量（$n_E, n_C$）及计算出的标准化均数差效应量 $d$，输出该效应量点估计的理论标准误 $\text{SE}_d$ 与抽样方差 $v_d$。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, p. 25)]]
>
> **数学直觉** 前项 $\frac{n_E + n_C}{n_E n_C}$ 度量均值差异的抽样方差；后项 $\frac{d^2}{2(n_E + n_C)}$ 度量合并标准差自身因抽样波动引入的附加二阶方差。
>
> **注意事项**
> - 该公式严格适用于**独立组间设计（Between-Subject Design）**；若属于重复测量或匹配组内设计，必须依据测量前后相关系数 $r$ 修正公式，严禁直接混用；
> - 当样本较小时，需乘上 Hedges 小样本校正因子 $J$ 转化为 Hedges' $g$，其对应方差公式亦随之按 $J^2$ 缩减。

---

### 公式步骤四　元分析联合标准误与精度累加法则

> [!formula-step] 公式步骤　两级[[Fixed-Effect Model|固定效应]][[Meta-analysis|元分析]]联合标准误
> $$\text{SE}_D = \sqrt{v_D} = \sqrt{\frac{1}{\sum_{j=1}^m W_j}} = \sqrt{\frac{1}{\sum_{j=1}^m \frac{1}{\text{SE}_j^2}}}$$
>
> **这个公式在做什么** 接收各纳入元分析（或主要研究）的方差倒数权重 $W_j = 1/v_{d_j} = 1/\text{SE}_j^2$，输出跨[[Research Synthesis|研究综合]]效应量 $D$ 的联合标准误 $\text{SE}_D$。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 25, 37–38)]]
>
> **数学直觉** 依据精度累加公理，当纳入的独立研究增多时，总信息量（精度之和 $\sum W_j$）持续单调增加，其倒数的平方根 $\text{SE}_D$ 必然严格小于任何单个纳入研究的标准误。
>
> **充要条件与注意事项**
> - 该公式成立的唯一充要条件是纳入的所有底层主要研究**完全独立且互不重叠**；
> - 严禁对纳入[[Document|文献]]的标准误直接取简单算术平均，否则将严重违反信息累加原理并得出荒谬的膨胀误差。

> [!math-principle] 标准误的统计数学公理与常见误用机理
> - **精度累加公理** 在合法元分析中，联合标准误必小于最小子项：$\text{SE}_D < \min(\text{SE}_j)$。若合并后的标准误反而大于某单项高精度研究，证明发生了算术平均违背。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, p. 30)]]
> - **除数敏感性公理** 效应量公式 $d = (M_E - M_C)/\text{SD}$ 必须以标准差为除数；若将标准误代入除数，因 $\text{SE} = \text{SD}/\sqrt{n}$，效应量将被人为虚假放大 $\sqrt{n}$ 倍。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, p. 27)]]
> - **协方差失效公理** 若[[Primary and Secondary Documents|初级文献]]存在重叠，$\operatorname{Cov}(d_1, d_2) > 0$，传统联合方差公式失效，计算出的名义标准误远低于真实标准误，导致[[Confidence Interval|置信区间]]虚窄与假阳性率急剧膨胀。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, p. 25)]]

---

> [!proc] 标准误在实证研究与[[Research Synthesis|证据综合]]中的四步质控规程
> 1. **原始数据提取与除数严格核实** 审查[[Primary and Secondary Documents|初级文献]]报告的均值变异参数，严格区分 $\text{SD}$ 与 $\text{SE}$；若文献仅报告 $\text{SE}$，必须利用 $\text{SD} = \text{SE} \times \sqrt{n}$ 还原真实标准差后再行计算标准化[[Effect Size|效应量]]，杜绝除数混淆灾难。
> 2. **独立效应量方差精确建模** 提取实验组与对照组精确[[Sample Size Determination|样本量]]（$n_E, n_C$），代入组间无偏方差公式计算抽样标准误 $\text{SE}_d$；对于小样本研究执行 Hedges 校正。
> 3. **逆方差权重分配与联合推断** 二阶汇总必须以方差倒数赋权（$W = 1/\text{SE}^2$），严禁按样本量离散度硬造伪标准误，严禁设定武断下限；由精度累加公式精确推算联合标准误并输出 95% [[Confidence Interval|置信区间]]。
> 4. **依赖结构排查与稳健方差校正** 针对文献重叠与多重测量依赖，弃用传统独立性假设下的单层方差公式，采用[[Robust Variance Estimation|稳健方差估计]]（RVE / 三明治估计量）自动修正低估的标准误。

---

> [!case] 混淆标准差与标准误致[[Effect Size|效应量]]虚增十倍（Eisenstaedt 案例）
> - **原始数据提取** Gijbels et al. (2005, p. 56) 纳入 Eisenstaedt et al. (1990) 单科成绩，对照组均值 $80.21$、标准误 $\text{SE} = 1.65$（$n = 107$），实验组均值 $66.53$、标准误 $\text{SE} = 2.74$。
> - **除数混淆失误** [[Meta-analysis|元分析]]作者误将标准误 $1.65$ 当作标准差代入分母：
>   $$d_{\text{error}} = \frac{66.53 - 80.21}{1.65} = -8.291$$
> - **规范矫正与后果** 依标准差（$\text{SD} = 1.65 \times \sqrt{107} \approx 17.07$）正确计算后真实效应量仅为 $d \approx -0.80$。因除数缩水，效应量被虚假放大逾 10 倍并直接污染后续宏观证据库。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, p. 27)]]

> [!case] 根据离散度硬造伪标准误致核心教学法权重腰斩（Haas 案例）
> - **伪造标准误过程** Haas (2005) [[Direct Instruction|直接教学]]元分析报告 19 个效应量，离散标准差 $\text{SD} = 0.59$。宏观综合在缺失关键[[Sample Size Determination|样本量]]时，拿离散标准差除以 $\sqrt{19}$ 硬造伪标准误：$\text{SE} = 0.59/\sqrt{19} \approx 0.135$。
> - **权重腰斩后果** 依原始样本量推算的真实标准误为 $0.092$。虚假扩大的标准误导致其逆方差权重仅获 $W = 1/(0.135)^2 \approx 54.9$；而真实权重应为 $W = 1/(0.092)^2 \approx 118.1$，直接教学在总库中的分量被削减了 53.5%。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 29–30)]]

> [!case] 对标准误取算术平均致合并误差反向膨胀三倍（[[Inquiry-Based Learning|探究式学习]]案例）
> - **算术平均操作** [[John Hattie|哈蒂]]在综合两项探究式学习元分析时，其报告的合并标准误 $0.092$ 竟是对两篇文献的标准误 $0.154$ 与 $0.030$ 取算术平均 $(0.154+0.030)/2$。
> - **违背精度累加** 依逆方差精度累加法则，合并标准误应严格小于任何单项研究（$\text{SE}_D < 0.030$）；直接平均使合并误差比高精度单项大 3 倍，直接颠覆了统计合成提高精度的数学前提。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, p. 30)]]

> [!case] 武断设定标准误下限压制大样本研究（0.05 阈值扭曲）
> - **人为设定截断** 哈蒂在数据提取中人为规定标准误下限为 $0.05$（方差下限 $0.0025$）。
> - **大样本惩罚后果** 这一武断设定导致大样本高精度研究的方差被人为拔高至 $0.018$，真实统计权重被残酷压缩达 7 倍，破坏了[[Inverse-Variance Weighting|逆方差加权]]的无偏最优性。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 29–30)]]

---

> [!software-impl] R 语言中的标准误计算与提取实现
> ```R
> # 1. 单样本均值标准误（SEM）计算
> sem <- function(x) sd(x, na.rm = TRUE) / sqrt(sum(!is.na(x)))
> 
> # 2. 效应量 Cohen's d 及其标准误精确提取 (metafor)
> library(metafor)
> dat <- escalc(measure = "SMD", 
>               m1i = m_exp, sd1i = sd_exp, n1i = n_exp,
>               m2i = m_ctl, sd2i = sd_ctl, n2i = n_ctl)
> # dat$yi 为效应量 d，dat$vi 为抽样方差，sqrt(dat$vi) 即为 SE_d
> 
> # 3. 固定效应模型联合标准误合成
> fit_fe <- rma(yi, vi, data = dat, method = "FE")
> # 提取联合估计值标准误：fit_fe$se (等于 sqrt(1 / sum(1/dat$vi)))
> 
> # 4. 文献重叠聚类稳健方差校正（clubSandwich）
> library(clubSandwich)
> fit_rob <- coef_test(fit_fe, vcov = "CR2", cluster = dat$cluster_id)
> # 输出经经验残差修正后的稳健标准误（Robust SE）
> ```

---

> [!warning] 标准误的统计局限与推断风险
> 1. **大样本渐近正态依赖** 传统 SE 公式严重依赖[[Central Limit Theorem|中心极限定理]]与正态分布假设，在[[Sample Size Determination|样本量]]极小（$N < 30$）或分布严重偏态时估计严重失效。
> 2. **数据依赖结构破坏** 一旦原始研究存在重叠或组内重复测量相关，传统独立性标准误公式会产生严重低估，虚假收窄[[Confidence Interval|置信区间]]。
> 3. **作为除数时的杠杆风险** 严禁将 SE 代替 SD 充当标准化除数；在小样本下较小的 SE 误差会造成[[Effect Size|效应量]]呈数量级畸变。
> 4. **无法度量系统性偏差** SE 仅能反映[[Random Sampling|随机抽样]]扰动，不能反映研究设计缺陷、测量工具污染与[[Publication Bias|发表偏倚]]等根本性偏误。

---

> [!entry-map] 相关理论与方法
> | 条目 | 类型 | 关系说明 |
> |:---|:---|:---|
> | [[Central Limit Theorem]] | 理论 | 为均值[[Sampling Error\|抽样分布]]呈正态性及标准误公式推导提供数理极限支撑。 |
> | [[Confidence Interval]] | 方法 | 标准误是构建参数置信区间（点估计 $\pm Z \times SE$）的核心构建材料。 |
> | [[Inverse-Variance Weighting]] | 方法 | 以方差倒数（$w = 1/SE^2$）进行加权，是元分析达到 BLUE 最优估计的基础算法。 |
> | [[Effect Size]] | 方法 | 效应量的推断统计检验与区间估计严格依赖其抽样标准误 $\text{SE}_d$。 |
> | [[Sample Size Determination]] | 方法 | 根据研究目标容许的标准误界限反推实验或调查所需样本量。 |
> | [[Meta-analysis]] | 方法 | 元分析通过加权合成各主要研究的标准误以提高总体估计精度。 |
> | [[Meta-meta-analysis]] | 方法 | 二阶综合通过精度累加确定联合标准误，需严格避免算术平均。 |
> | [[Robust Variance Estimation]] | 方法 | 在文献重叠与聚类依赖下提供渐近无偏的稳健标准误校正。 |
> | [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]] | 论证 | 奠定均值标准误（[[Causal Modeling\|SEM]]）、比例标准误及有限总体校正的经典统计规范。 |
> | [[Argument_Wecker_2016_ZfE\|Wecker et al. (2016)]] | 论证 | 严格揭示元分析审查中混淆 SE 与 SD、硬造伪标准误及对标准误取均值的实证灾难。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen, Manion & Morrison (2011, Ch. 8)]] — 系统推导均值的标准误（[[Causal Modeling|SEM]]）与分类比例标准误的计算公式，确立[[Confidence Interval|置信区间]]构建与大样本边际收益递减准则。
> - [[Argument_Wecker_2016_ZfE|Wecker et al. (2016)]] — 从[[Fixed-Effect Model|固定效应]]数学公理推导联合标准误计算规范，实证揭示将标准误误作标准差导致[[Effect Size|效应量]]虚增十倍（Eisenstaedt 案例）、根据离散度硬造伪标准误使[[Direct Instruction|直接教学]]权重腰斩 53.5% 以及对标准误取算术平均等系统性计量灾难。
