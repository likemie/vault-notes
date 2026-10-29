---
title: Common Language Effect Size
aliases:
  - 普通语言效应量
  - 常见语言效应量
  - CLES
  - 通用语言效应量
  - 超越概率
  - Probability of Superiority
summary: "将两组连续分布标准化均值差转化为二项超越概率的统计效应量指标，度量从实验组随机抽取个体的得分高于对照组个体的客观概率"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 22
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - statistics/effect-size
  - theme/probability
  - field/research-methodology
related_concepts:
  - "[[Variable]]"
  - "[[Scale of Measurement]]"
  - "[[Business as Usual]]"
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Dependent Variable]]"
  - "[[Visible Learning]]"
  - "[[Discourse]]"
related_methods:
  - "[[Effect Size]]"
  - "[[Random Sampling]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Confidence Interval]]"
  - "[[Sample Size Determination]]"
  - "[[Effect Size Conversion]]"
  - "[[Random Assignment]]"
  - "[[Meta-analysis]]"
  - "[[Standard Error]]"
  - "[[Meta-meta-analysis]]"
related_persons:
  - "[[John Hattie]]"
related_arguments:
  - "[[Argument_Bergeron_2017_MJE]]"
  - "[[Argument_Wecker_2016_ZfE]]"
confidence: high
status: completed
created: '2026-10-18'
updated: 2026-10-29
---

（普通语言[[Effect Size|效应量]]）

---

> [!def] Common Language Effect Size
> **普通语言[[Effect Size|效应量]]（Common Language Effect Size, CLES）**，又称超越概率（Probability of Superiority, PS），指将两组连续型[[Variable|变量]]分布的标准化均值差（如 Cohen's $d$）映射为直观二项发生概率的标准化统计量。它度量从处理组（实验组）中随机抽取的一名受试者，其得分高于从对照组中随机抽取的一名受试者的客观概率。该方法旨在消除无量纲标准化指标的技术抽象性，为教育实践者与政策制定者提供通俗直观的概率解释。[[Argument_Bergeron_2017_MJE|(Bergeron & Rivard, 2017, p. 239)]]

> [!method-scope] 方法范围
> - **研究对象** 实验组与对照组在连续[[Scale of Measurement|测量量表]]上的得分分布，或具有有序尺度的实证评价数据。
> - **问题类型** 回答干预措施在多大程度上使目标个体相较于[[Business as Usual|常规对照组]]实现学业或认知优势，提供直观的概率化相对比较。
> - **[[Unit of Analysis|分析单位]]** 独立[[Random Sampling|随机抽样]]所获取的配对个体得分观测值。
> - **输出形式** 严格落于 $(0\%, 100\%)$ 区间的百分比概率值，当两组无差异时基线严格为 $50\%$。

> [!citation-card] 概率映射公理与通俗解释初衷
> 普通语言效应量统计量旨在将连续分布的标准化均值差翻译为普通人易于理解的日常语言：即从某一群体随机抽取的个体在特定测量指标上超过另一群体随机抽取个体的几率。根据数理统计公理，其理论值域严格受限于零至百分之百之间，当两组均值相等时该概率严格等于百分之五十。[[Argument_Bergeron_2017_MJE|(Bergeron & Rivard, 2017, p. 239)]]
>
> *“The common language effect size statistic was designed to translate continuous difference measures into the probability that an individual randomly selected from one population has a higher score than an individual randomly selected from another population... Mathematically, this probability must strictly lie between 0% and 100%.”*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 认为[[Effect Size|效应量]]的统计学价值不仅在于推断总体参数的显著性，更在于向公共领域清晰传递其实质效果的相对优势概率。
> - **研究者角色** 要求研究者在正态性假设检验与非参数秩次转换之间作出严谨判定，审慎确立比较基线的方向。
> - **有效性标准** 严格依循连续概率累积分布函数的公理边界；在两组方差齐性与正态假定满足时具有最高参数效率。
> - **不声称回答的问题** 不能脱离特定研究情境断定干预的绝对绝对价值，其数值大小完全依附于对照组基线与[[Variable|变量]]测量工具的敏感度。

> [!method-stack] 方法层级
> - **研究设计** 独立双样本[[Randomised Controlled Trials|随机对照试验]]（RCT）、[[Quasi-Experimental Designs|准实验设计]]或横截面分组比较。
> - **数据要求** 连续型正态分布[[Dependent Variable|因变量]]，或可进行非参数秩次转化的有序变量。
> - **核心指标** 正态分布累积映射统计量 $\Phi(d/\sqrt{2})$、Mann-Whitney $U$ 秩次非参数估计量。
> - **配套工具** Cohen's $d$ 计算、标准正态分布累积积分函数、[[Confidence Interval|置信区间]]自助抽样法（Bootstrap）。

---

> [!formula-step] 公式步骤　正态累积映射公式
> $$\text{CLES} = P(X_E > X_C) = \Phi\left(\frac{\mu_E - \mu_C}{\sqrt{\sigma_E^2 + \sigma_C^2}}\right) \xrightarrow{\sigma_E = \sigma_C} \text{CLES} = \Phi\left(\frac{d}{\sqrt{2}}\right)$$
>
> **这个公式在做什么** 将两组独立正态总体的标准化均值差 $d$ 转化为单次随机配对抽取中实验组个体胜出的累积概率。
>
> **符号说明** $X_E, X_C$ 分别为实验组与对照组个体的随机[[Variable|变量]]；$\mu_E, \mu_C$ 为两组均值；$d$ 为标准化均值差；$\Phi(\cdot)$ 为标准正态累积分布函数。
>
> **数学直觉** 设差值随机变量 $D = X_E - X_C$。由于两独立正态变量的线性组合仍服从正态分布，差值变量的均值为 $\mu_D = \mu_E - \mu_C$，方差为 $\sigma_D^2 = \sigma_E^2 + \sigma_C^2$。对 $D > 0$ 进行标准化：
> $$Z = \frac{0 - (\mu_E - \mu_C)}{\sqrt{\sigma_E^2 + \sigma_C^2}} = -\frac{\mu_E - \mu_C}{\sqrt{\sigma_E^2 + \sigma_C^2}}$$
> 依据对称性，$P(D > 0) = 1 - \Phi(-Z) = \Phi(Z)$。当方差齐性时，分母为 $\sqrt{2}\sigma$，直接化简为 $\Phi(d/\sqrt{2})$。
>
> **结果怎么读**
> - $d = 0.00 \Longleftrightarrow \text{CLES} = \Phi(0) = 50.0\%$（完全无差异，胜出概率与抛硬币相等）；
> - $d = 0.20 \Longleftrightarrow \text{CLES} \approx 55.6\%$（小效应，胜出几率略高于均等）；
> - $d = 0.40 \Longleftrightarrow \text{CLES} \approx 61.1\%$（中等效应/教育经验基准）；
> - $d = 0.80 \Longleftrightarrow \text{CLES} \approx 71.4\%$（大效应）；
> - $d = 1.40 \Longleftrightarrow \text{CLES} \approx 83.9\%$；
> - $d = 3.00 \Longleftrightarrow \text{CLES} \approx 98.3\%$。
>
> **注意事项** 标准正态累积分布函数的值域为严格开区间 $(0, 1)$，因此 CLES 的理论概率绝不可能低于 0% 或超过 100%。

---

### 非参数秩次估计规程

在总体分布偏态或存在极端值时，参数模型会产生估计偏倚。此时采用非参数统计量（Mann-Whitney $U$）进行稳健估计：

> [!formula-step] 公式步骤　非参数概率优势估计
> $$\text{CLES}_{\text{nonparametric}} = \frac{U_E}{n_E \cdot n_C} = \frac{\sum_{i=1}^{n_E} \sum_{j=1}^{n_C} I(X_{Ei} > X_{Cj}) + 0.5 \cdot I(X_{Ei} = X_{Cj})}{n_E \cdot n_C}$$
>
> **这个公式在做什么** 直接统计所有可能的实验组与对照组被试两两配对中，实验组成绩高于对照组的实际对数比例。
>
> **符号说明** $U_E$ 为 Mann-Whitney 检验统计量；$n_E, n_C$ 为两组[[Sample Size Determination|样本量]]；$I(\cdot)$ 为指示函数。
>
> **数学直觉** 该估计量与受试者工作特征曲线下面积（Area Under Curve, AUC）完全等价，不依赖总体正态性或方差齐性假定，具有极强的分布稳健性。

---

> [!ref-table] Cohen's d 与普通语言[[Effect Size|效应量]]（CLES）标准对照表
> | Cohen's $d$ | 0.00 | 0.20 | 0.40 | 0.60 | 0.80 | 1.00 | 1.20 | 1.40 | 2.00 | 3.00 |
> |---|---|---|---|---|---|---|---|---|---|---|
> | **普通语言效应量（CLES）** | 50.0% | 55.6% | 61.1% | 66.4% | 71.4% | 76.0% | 80.2% | 83.9% | 92.1% | 98.3% |
> | **解释方差比（$R^2$）** | 0.0% | 1.0% | 3.8% | 8.3% | 13.8% | 20.0% | 26.5% | 32.9% | 50.0% | 69.2% |
>
> **图表解读** CLES 随 $d$ 呈非线性 S 型增长；在 $d=0$ 附近变化最为敏锐，当 $d > 1.5$ 之后增长显著放缓并渐近收敛于 100%。

---

> [!critique-method] 违背概率公理与缺乏专业统计咨询的灾难案例（[[Argument_Bergeron_2017_MJE|Bergeron & Rivard, 2017, pp. 238–240]]）
> - **不可能概率的数学崩溃** 在《[[Visible Learning|可见的学习]]》一书中，[[John Hattie|约翰·哈蒂]]试图将[[Effect Size Conversion|效应量转换]]为 CLES 向一线教育工作者普及成果，但在其二阶汇总附录中，竟汇报了负百分比与超过 100% 的荒谬概率（Topphol, 2012）。这一初等算术错误的长期存在，暴露了研究团队在数理逻辑与基础质控上的系统性匮乏。
> - **事后统计尸检困境** 加拿大统计学者伯杰龙与里瓦尔援引罗纳德·费希尔（Ronald Fisher, 1938）的经典论断指出：在研究方案设计和执行中缺乏专业统计学家的深度参与，实验结束后再寻求咨询往往只是请统计学家做一场事后尸检——至多只能证明该分析究竟死于何种低级数学失误。
> - **比较基线的相对性失省** [[Effect Size|效应量]]符号与 CLES 优势方向取决于隐性对照基线的设定。若基线选择反转（如从“富裕比贫困”反转为“贫困比富裕”），CLES 将从优势概率骤降为严重劣势概率。忽视基线相对性，容易使统计量异化为主观裁剪政策结论的工具。

---

> [!software-impl] 统计软件实现代码
> - **R 语言环境（参数计算与非参数 AUC 计算）**
>   ```R
>   # 参数法：从 Cohen's d 转换 CLES
>   d_to_cles <- function(d) {
>     pnorm(d / sqrt(2))
>   }
>   
>   # 非参数法：从原始样本数据直接计算经验 CLES
>   empirical_cles <- function(group_e, group_c) {
>     u_stat <- wilcox.test(group_e, group_c)$statistic
>     cles <- u_stat / (length(group_e) * length(group_c))
>     return(as.numeric(cles))
>   }
>   
>   # 验证基准
>   d_to_cles(0.40) # 产出 0.6114 (61.14%)
>   ```
> - **Python 环境（`scipy.stats`）**
>   ```python
>   import numpy as np
>   from scipy.stats import norm, mannwhitneyu
>   
>   def parametric_cles(d: float) -> float:
>       return float(norm.cdf(d / np.sqrt(2)))
>   
>   def nonparametric_cles(group_e: np.ndarray, group_c: np.ndarray) -> float:
>       u_stat, _ = mannwhitneyu(group_e, group_c, alternative='greater')
>       return float(u_stat / (len(group_e) * len(group_c)))
>   
>   # 验证基准
>   print(f"CLES for d=0.40: {parametric_cles(0.40):.4f}") # 0.6114
>   ```

---

> [!method-fit] 适用判断
> - **适合使用** 需要向非统计学专业公众、一线中小学教师或教育行政决策者直观传达干预效果相对优劣的情境。
> - **谨慎使用** 原始数据分布呈现极端双峰或显著厚尾偏态的情境；此时应优先使用基于秩次的非参数估计量，谨慎使用参数正态转换。
> - **不适合使用** 试图度量绝对知识掌握量或学业水平绝对达标率的研究设计；CLES 本质上仅度量两组随机配对的相对优势概率，不包含绝对分数信息。

> [!method-limits] 方法局限
> - **概率计算高度依附总体正态假定** 参数法严格依赖两组总体正态分布与方差相等的理论假定，一旦方差极不均齐，转换公式将产生系统性偏差。
> - **极值区间的敏感度压缩** 当 $d > 2.0$ 时，CLES 迅速逼近 $98\%–99\%$，无法敏锐反映超高[[Effect Size|效应量]]之间的细微阶梯差异。
> - **缺乏因果保证** 若主要研究本身缺乏严格的[[Random Assignment|随机分配]]或实验控制，计算出的 CLES 仅反映观测样本间的关联概率，不能外推为干预措施带来的必然因果增益。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Effect Size]] | 上位方法 | 普通语言效应量属于效应量家族中面向概率解释的核心派生测度。 |
> | [[Effect Size Conversion]] | 支撑方法 | 提供标准化均值差、相关系数与 CLES 之间跨尺度换算的完整数学模型。 |
> | [[Meta-analysis]] | 应用场景 | 二阶证据合成中将技术化统计量翻译为实践者通用[[Discourse\|话语]]的关键工具。 |
> | [[Standard Error]] | 诊断检验 | 评估 CLES 估计精度的基础抽样离散指标。 |
> | [[Argument_Bergeron_2017_MJE\|Bergeron and Rivard (2017)]] | 关键文献 | 从数理统计学视角系统审计 CLES 计算失范，揭示负概率与超额概率数学崩溃。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Bergeron_2017_MJE|Bergeron and Rivard (2017)]] — 通过对 CLES 理论值域的公理推导，实证揭露《[[Visible Learning|可见的学习]]》底层概率算法计算崩溃与伪科学特征。
> - [[Argument_Wecker_2016_ZfE|Wecker et al. (2016)]] — 在[[Meta-meta-analysis|二级元分析]]技术审计中将 CLES 计算失误列为统计失范典型案例。
