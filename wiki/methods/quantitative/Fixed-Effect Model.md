---
title: Fixed-Effect Model
aliases:
  - 固定效应模型
  - 固定效应
  - Fixed-Effect Models
  - Fixed Effect Model
  - Fixed Effect
summary: "假定所有纳入研究共享同一个恒定真实效应的统计合成模型，依据抽样精度倒数实施逆方差加权，具备两级固定效应代数等价性与抽样独立性约束"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 34
method_related_level: 3
method_related_stars: "💎"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - statistics/meta-analysis
  - statistical-model
  - fixed-effect-model
  - methodology
related_concepts:
  - "[[Sampling Error]]"
  - "[[Construct]]"
  - "[[Unit of Analysis]]"
  - "[[Document]]"
  - "[[Epistemology]]"
  - "[[Implementation Fidelity]]"
  - "[[Heterogeneity]]"
  - "[[Clinical Trial]]"
  - "[[Visible Learning]]"
  - "[[Web-Based Learning]]"
  - "[[Critical Thinking]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Research Synthesis]]"
  - "[[Effect Size]]"
  - "[[Inverse-Variance Weighting]]"
  - "[[Confidence Interval]]"
  - "[[Standard Error]]"
  - "[[Experimental Research]]"
  - "[[Random-Effects Model]]"
  - "[[Between-Study Variance]]"
  - "[[Prediction Interval]]"
  - "[[Random Sampling]]"
  - "[[Meta-meta-analysis]]"
  - "[[Sample Size Determination]]"
  - "[[Cochran's Q Test]]"
  - "[[I-squared Statistic]]"
  - "[[Robust Variance Estimation]]"
related_instruments: []
related_persons:
  - "[[Christof Wecker]]"
  - "[[John Hattie]]"
related_facts: []
related_arguments:
  - "[[Argument_Higgins_2016_ROE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17]]"
  - "[[Argument_Wecker_2016_ZfE]]"
  - "[[Argument_Simpson_2017_JEdPolicy]]"
  - "[[Argument_Abrami_2015_RER]]"
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit11]]"
confidence: high
status: completed
created: 2026-06-08
updated: 2026-10-31
---

---

> [!def] Fixed-Effect Model
> 固定效应模型（Fixed-Effect Model）是[[Meta-analysis|元分析]]与[[Research Synthesis|证据综合]]中最基础的统计加权合成模型。该模型建立在强同质性假定之上：假定所有纳入分析的独立初级研究都在估计同一个唯一且恒定不变的总体真实[[Effect Size|效应量]] $\theta$，观测到的跨研究效应量变异完全源于受试者随机[[Sampling Error|抽样误差]]（Sampling Error）。在此假设下，模型通过[[Inverse-Variance Weighting|逆方差加权法]]（Inverse-Variance Weighting, IVW）以各研究抽样方差的倒数赋权（$w_i = 1/v_i$），实现合成估计量方差的最小化。[[Argument_Higgins_2016_ROE|(Higgins, 2016, p. 39)]]; [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|(Cohen et al., 2011, Ch. 17)]]

> [!method-scope] 方法范围
> - **研究对象** [[Construct|构念]]定义完全一致、实验干预标准化且受试人群同质的独立初级实证研究效应量矩阵。
> - **问题类型** 估计特定研究集合共享的单一平均真实效应量，检验初级研究真实效应量是否完全同质。
> - **[[Unit of Analysis|分析单位]]** 独立实验样本、初级研究报告的标准化均数差（Cohen's $d$, Hedges' $g$）或相关系数。
> - **输出形式** 固定效应加权合并效应量点估计值（$\hat{\theta}_{\text{FE}}$）、95% [[Confidence Interval|置信区间]]（95% CI）、合并[[Standard Error|标准误]]（$SE_{\text{FE}}$）及 Cochran's $Q$ 同质性检验统计量。

> [!citation-card] 固定效应模型核心假定
> 固定效应模型假定所有纳入研究共享同一个真实的总体效应量，研究之间的变异纯粹由抽样误差导致；该模型的推断严格局限于所分析的特定研究集合。[[Argument_Higgins_2016_ROE|(Higgins, 2016, p. 39)]]
>
> *The fixed-effect model assumes that all studies share a single true effect size, with observed differences arising solely from sampling error.*

> [!citation-card] 两级固定效应代数等价性定理
> 二级固定效应元分析在数学上等价于单级直接合成，其充要条件是各一级元分析纳入的样本完全独立且互不重叠；一旦存在重复[[Document|文献]]，经典方差公式失效且标准误会被严重低估。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 24–25)]]
>
> *Unter der Annahme eines festen Effekts entspricht die zweistufige Metaanalyse algebraisch der einstufigen direkten Synthese aller Primärstudien, vorausgesetzt, die Studienmengen überschneiden sich nicht.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 预设外部世界存在唯一的“客观真实效应”（One True Effect），经验研究的变异被视为随机干扰噪声，追求对普遍常数的高精度逼近。
> - **研究者角色** 要求研究者严格核实纳入研究的[[Construct|理论构念]]一致性与[[Experimental Research|实验设计]]可比性；在二级[[Research Synthesis|证据综合]]中必须逐一核查底层主要研究的完全独立性。
> - **有效性标准** 统计推断有效性依赖于同质性检验假设成立（Cochran's $Q$ 检验不显著且 $I^2 \approx 0\%$）；统计推论严格封闭于纳入的 $k$ 项特定研究本身，不得向广义超总体推论。
> - **不声称回答的问题** 无法解释或容纳因教学情境、[[Implementation Fidelity|实施保真度]]与被试群体[[Heterogeneity|异质性]]导致的真实[[Effect Size|效应量]]离散。
> - **计量经济学对等视角与内生性局限** 在面板数据计量分析中，固定效应模型用于吸收不随时间变化的不可测个体异质性；但王大顺与巴拉巴西指出，该方法仅对特定可测或时间恒定特征有效，无法消除随时间演化的不可观测混杂变量，因而无法完全替代准实验或随机实验设计。[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|(Wang & Barabási, 2021, p. 248)]]

> [!contrast-table] 固定效应模型 vs [[Random-Effects Model|随机效应模型]]核心参数与假设对比
> | 比较维度 | 固定效应模型（Fixed-Effect Model） | 随机效应模型（[[Random-Effects Model]]） |
> |:---|:---|:---|
> | **核心哲学假设** | 存在唯一的“单一真实效应”（One True Effect） | 存在一个“真实效应量分布”（Distribution of True Effects） |
> | **变异来源分解** | 仅抽样方差（Within-study variance, $v_i$） | 抽样方差 $v_i$ + [[Between-Study Variance\|研究间方差]] $\tau^2$ |
> | **权重分配特征** | 严格按抽样精度倒数赋权（$w_i = 1/v_i \propto N_i$），高度偏向超大样本研究 | 权重趋于平均化（$w_i^* = \frac{1}{v_i + \tau^2}$），大样本优势被 $\tau^2$ 稀释 |
> | **[[Confidence Interval\|置信区间]]宽度** | 通常较窄（[[Standard Error\|标准误]]较小，统计推断激进且敏感） | 较宽（标准误较大，充分反映异质性不确定性） |
> | **[[Prediction Interval\|预测区间]]（PI）** | 无法构建预测区间（模型预设异质性方差为 0） | 可计算 95% [[Prediction Interval\|预测区间]]评估单项新情境真实效应范围 |
> | **统计推断边界** | 仅限外推至与纳入研究特征完全相同的封闭集合 | 面向未来同类研究的广义“超总体”（Super-population） |
> | **适用现实情境** | 实验室严格物理化复现、高纯度同质[[Clinical Trial\|临床试验]] | 复杂课堂教学、教育政策改革、社会科学跨情境干预 |

---

> [!formula-set]- 固定效应模型推导与两级合成流程
> ```mermaid
> flowchart LR
>   A["步骤 1：单级固定效应模型基准<br/>预设单一真实效应与研究内抽样方差"] --> B["步骤 2：最优逆方差加权<br/>以研究精度倒数赋权最小化合并方差"]
>   B --> C["步骤 3：两级分组展开表达<br/>将多项元分析映射至底层主要研究池"]
>   C --> D["步骤 4：跨层代数等价定理<br/>两级加权等价于一级全池逆方差合并<br/>(充要条件：原始研究完全无重叠)"]
>   D --> E["步骤 5：独立性假设破产诊断<br/>文献重叠导致协方差非零与假阳性膨胀"]
> ```

---

### 公式步骤一　单级固定效应统计模型与最优逆方差加权

> [!formula-step] 公式步骤　单级固定效应合成模型
> $$y_i = \theta + \epsilon_i, \quad \epsilon_i \sim N(0, v_i)$$
>
> **这个公式在做什么** 表达第 $i$ 项独立初级研究观测到的[[Effect Size|效应量]] $y_i$ 等于全体研究共享的唯一真实效应量 $\theta$ 加上[[Sampling Error|抽样误差]]扰动项 $\epsilon_i$。抽样误差服从均值为 0、方差为 $v_i$ 的正态分布。[[Argument_Higgins_2016_ROE|(Higgins, 2016, p. 39)]]
>
> **最优逆方差权重与合并估计量**
> $$w_i = \frac{1}{v_i}$$
> $$\hat{\theta}_{\text{FE}} = \frac{\sum_{i=1}^k w_i y_i}{\sum_{i=1}^k w_i}, \quad \text{Var}(\hat{\theta}_{\text{FE}}) = \frac{1}{\sum_{i=1}^k w_i}, \quad \text{SE}(\hat{\theta}_{\text{FE}}) = \sqrt{\frac{1}{\sum_{i=1}^k w_i}}$$
>
> **数学直觉** 根据高斯-马尔可夫定理，以方差倒数（$w_i = 1/v_i$）赋权构成了线性无偏估计量中方差最小的最佳线性无偏估计（BLUE）。大样本研究（$v_i$ 小）获得决定性权重，小样本研究权重微弱。

---

### 公式步骤二　两级固定效应二级元分析的代数等价性定理

在《[[Visible Learning|可见的学习]]》等宏观二阶综合项目中，研究者常对已发表的一级[[Meta-analysis|元分析]]进行二次固定效应合并。[[Christof Wecker|克里斯托夫·韦克尔]]（Christof Wecker）等人严格推导了两级固定效应合成与一级全池直接合并之间的代数等价性：

> [!formula-step] 公式步骤　两级固定效应代数等价性证明
> $$d_j = \frac{\sum_{i=1}^{k_j} w_{ji} d_{ji}}{\sum_{i=1}^{k_j} w_{ji}}, \quad v_{d_j} = \frac{1}{\sum_{i=1}^{k_j} w_{ji}} \tag{一级元分析内部加权}$$
> $$D = \frac{\sum_{j=1}^m W_j d_j}{\sum_{j=1}^m W_j}, \quad W_j = \frac{1}{v_{d_j}} = \sum_{i=1}^{k_j} w_{ji} \tag{二级跨层[[Inverse-Variance Weighting|逆方差加权]]}$$
>
> 将一级效应量 $d_j$ 与二级权重 $W_j$ 代入二级公式，分子分母完美展开相约：
> $$D = \frac{\sum_{j=1}^m \left(\sum_{i=1}^{k_j} w_{ji}\right) \left[\frac{\sum_{i=1}^{k_j} w_{ji} d_{ji}}{\sum_{i=1}^{k_j} w_{ji}}\right]}{\sum_{j=1}^m \left(\sum_{i=1}^{k_j} w_{ji}\right)} = \frac{\sum_{j=1}^m \sum_{i=1}^{k_j} w_{ji} d_{ji}}{\sum_{j=1}^m \sum_{i=1}^{k_j} w_{ji}} = \bar{d}$$
> $$v_D = \frac{1}{\sum_{j=1}^m W_j} = \frac{1}{\sum_{j=1}^m \sum_{i=1}^{k_j} w_{ji}} = v_{\bar{d}}$$
>
> **这个公式在做什么** 严格证明在固定效应模型下，对各一级元分析按方差倒数加权得到的二级综合效应量 $D$ 及其理论方差 $v_D$，在代数上完全恒等于将全体主要研究直接汇总到同一证据池中所计算的一级合并效应量 $\bar{d}$ 与总方差 $v_{\bar{d}}$。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 25, 37–38)]]
>
> **充要条件** 该代数等价性成立的唯一充要条件是各一级元分析纳入的底层主要研究**完全独立且互不重叠（$\forall j_1 \neq j_2, \text{Studies}(j_1)** \cap \text{Studies}(j_2) = \emptyset$）。

> [!math-principle] 固定效应模型的统计数学公理与协方差失效机理
> - **单一真实效应公理（Homogeneity Axiom）** 假定所有研究变异纯粹由被试层面的[[Random Sampling|随机抽样]]误差导致，不承认干预效果在不同教师、学校和课程之间存在真实本质差异。
> - **最佳线性无偏估计公理（BLUE Property）** 必须严格遵循逆方差加权（$w_i = 1/v_i$）；直接对各研究取简单未加权算术平均会破坏 BLUE 性质，导致估计效率严重受损。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, p. 25)]]
> - **代数等价性公理（Two-level Equivalence Axiom）** 只有在原始主要研究互斥无重叠的前提下，二级固定效应合成才在数学上等价于单级直接综合。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 25, 37–38)]]
> - **协方差失效公理（Covariance Breakdown Axiom）** 一旦不同元分析重复纳入相同文献，跨元分析的一级效应量之间产生未知正协方差（$\operatorname{Cov}(d_{j_1}, d_{j_2}) > 0$），导致传统方差公式失效。计算出的联合方差远低于真实方差，[[Standard Error|标准误]]虚窄，统计检验假阳性率急剧膨胀。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 25, 29–30)]]

---

> [!proc] 固定效应模型五步操作规程（Wecker et al., 2016 规范准则）
> 1. **[[Effect Size|效应量]]与标准差精确核验** 从各主要研究中提取均值差并除以合并标准差（$\text{SD}$），统一转换为 Hedges' $g$；严格辨别标准差与[[Standard Error|标准误]]（$\text{SE}$），严防误把标准误当除数导致效应量虚增十倍（如 Eisenstaedt 案例）。
> 2. **前置同质性检验与模型抉择** 计算 Cochran's $Q$ 统计量与 $I^2$ 指数；只有当 $p \ge .10$ 且 $I^2 \approx 0\%$、有充分理论依据确信研究高度同质时方可采用固定效应模型；若[[Heterogeneity|异质性]]显著，必须改用[[Random-Effects Model|随机效应模型]]。
> 3. **严格逆方差精度赋权** 依据各研究抽样方差倒数（$w_i = 1/v_i$）分配权重，严禁任何形式的简单未加权算术平均。
> 4. **底层文献独立性与重叠排查** 详细比对各研究（尤其在[[Meta-meta-analysis|二级元分析]]中）的样本来源；若存在重复发表或文献重叠，必须剔除重复项或引入相关性校正，防范协方差失效。
> 5. **联合参数推断与局部解释** 依据精度累加法则计算联合标准误（$SE = \sqrt{1/\sum w_i}$）与 95% [[Confidence Interval|置信区间]]；结论声明严格限制在当前特定研究集合内，不做无边界的总体外推。

---

> [!warning] 固定效应模型在教育研究中的系统性失配
> 1. **教育现实[[Heterogeneity|异质性]]导致核心假设破产** 教学研究涉及不同年级、学科、教师能力与课堂文化，真实[[Effect Size|效应量]]天然处于动态离散状态。强行套用固定效应模型假定“单一恒定真值”，必然严重低估实际[[Standard Error|标准误]]，产生虚假的极窄[[Confidence Interval|置信区间]]与高假阳性率（[[Argument_Simpson_2017_JEdPolicy|Simpson, 2017]]；[[Argument_Wecker_2016_ZfE|Wecker et al., 2016]]）。
> 2. **两级综合中文献重叠导致数理崩溃** 在大型[[Meta-meta-analysis|二级元分析]]中，多个一级[[Meta-analysis|元分析]]高度共享经典底层文献（例如 Olson & Wisher 与 Sitzmann 存在 93.3% 重叠），抽样独立性充要条件荡然无存，导致固定效应等价性定理彻底失效。
> 3. **大样本研究独裁偏差** 由于权重正比于[[Sample Size Determination|样本量]]（$w_i \propto N_i$），少数超大规模研究（即使其[[Implementation Fidelity|实施保真度]]较差）往往垄断整个合并结果，压制小样本但高质量的创新性试验。
> 4. **实践中的简单平均退化** 许多粗放综合项目（如[[John Hattie|哈蒂]]早期工作及部分传统综述）宣称采用固定效应模型，但在实际操作中却违背[[Inverse-Variance Weighting|逆方差加权]]规则，直接对不同效应量甚至标准误取简单算术平均，造成双重方法学失范。

---

> [!case] 关键案例重构：[[Argument_Wecker_2016_ZfE|Wecker et al. (2016)]] 对固定效应模型违背与排名雪崩的审计
> - **宣称模型与实际操作背离** [[John Hattie|哈蒂]]在《[[Visible Learning|可见的学习]]》中声明采用固定效应模型（Hattie, 2009, p. 12），假定所有研究估计同一个恒定效应。
> - **文献重叠与等价性瓦解** 在[[Web-Based Learning|网络学习]]领域，纳入的 Olson and Wisher (2002) 包含 15 项研究，其中 14 项（重叠率达 93.3%）与另一项纳入的 Sitzmann et al. (2006) 完全重复。固定效应独立性假定被彻底破坏。
> - **简单平均与排名雪崩** 哈蒂忽略重叠且放弃[[Inverse-Variance Weighting|逆方差加权]]，直接取简单算术平均，得出综合[[Effect Size|效应量]] $d = 0.59$（全书高居第 26 位）；经[[Christof Wecker|韦克尔]]等人剔除重复文献并执行规范逆方差加权后，真实综合效应量暴跌至 $d = 0.23$，在 138 个因素中的排位由第 26 位雪崩至第 98 位，大幅跌落 72 名并跌破 $0.40$ 关节点，实证证实了固定效应模型违规操作对政策排名的误导性。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 29–30)]]

> [!case] 关键案例重构：Levie and Lentz (1982) 违背固定效应加权规范
> - **未加权平均操作** Levie and Lentz (1982, p. 198) 在综合关于图文配合学习效果的 24 项[[Experimental Research|实验研究]]时，宣称呈现总体效应，但其汇报的合并值 $0.55$ 实际上是对 24 项研究效应量的简单算术平均值。
> - **统计后果** 该操作完全未按各主要研究的[[Sample Size Determination|样本量]]与抽样方差赋予权重，严重破坏了最佳线性无偏估计（BLUE）性质，低估了[[Standard Error|标准误]]并扭曲了真实精度。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, p. 28)]]

---

> [!software-impl] R 语言固定效应模型拟合代码
> ```R
> library(metafor)
> 
> # 1. 效应量与抽样方差计算 (标准化均值差 Hedges' g)
> dat <- escalc(measure = "SMD", 
>               m1i = m_exp, sd1i = sd_exp, n1i = n_exp,
>               m2i = m_ctl, sd2i = sd_ctl, n2i = n_ctl, 
>               data = raw_data)
> 
> # 2. 拟合固定效应模型 (method = "FE")
> fit_fe <- rma(yi, vi, data = dat, method = "FE")
> summary(fit_fe)
> 
> # 输出包含：
> # - 合并效应量点估计值 (estimate)
> # - 联合标准误 (se) 与 95% 置信区间 (ci.lb, ci.ub)
> # - Cochran's Q 同质性检验统计量与 p 值
> ```

---

> [!entry-map] 相关理论与方法
> | 条目 | 类型 | 关系说明 |
> |:---|:---|:---|
> | [[Random-Effects Model]] | 替代方法 | 随机效应模型纳入研究间异质性方差（$\tau^2$），是克服固定效应模型局限的标准替代方案。 |
> | [[Inverse-Variance Weighting]] | 核心算法 | 固定效应模型以抽样方差倒数（$w_i = 1/v_i$）赋权，是实现最小方差估计的数理基石。 |
> | [[Standard Error]] | 核心参数 | 固定效应模型的联合标准误由精度累加公式推导，严禁直接取算术均值。 |
> | [[Cochran's Q Test]] | 诊断检验 | 检验各研究真实效应量是否完全同质（$H_0: \tau^2 = 0$）的前置统计检验。 |
> | [[I-squared Statistic]] | 诊断指标 | 量化总变异中真实异质性占比；$I^2 > 0$ 提示固定效应模型假设面临挑战。 |
> | [[Meta-meta-analysis]] | 上位方法 | 二阶[[Meta-analysis\|元分析]]在固定效应下具备代数等价性，但高度依赖文献完全无重叠的前提。 |
> | [[Robust Variance Estimation]] | 补救方法 | 在存在文献重叠导致协方差失效时，运用经验残差校正被低估的标准误。 |
> | [[Argument_Wecker_2016_ZfE\|Wecker et al. (2016)]] | 论证 | 严格推导两级固定效应代数等价定理，揭示文献重叠导致方差公式失效的机理。 |
> | [[Argument_Higgins_2016_ROE\|Higgins (2016)]] | 论证 | 系统阐述固定效应与随机效应在[[Research Synthesis\|证据综合]]中的哲学假设与推论边界差异。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wecker_2016_ZfE|Wecker et al. (2016)]] — 从固定效应数学公理严格推导两级[[Meta-analysis|元分析]]代数等价性定理（$D = \bar{d}, v_D = v_{\bar{d}}$），实证审计了[[John Hattie|哈蒂]]因违反抽样独立性假定（93.3% 重叠）与滥用简单平均导致网络学习排名自第 26 位雪崩至第 98 位的严重失范。
> - [[Argument_Higgins_2016_ROE|Higgins (2016)]] — 比较固定效应与[[Random-Effects Model|随机效应模型]]的哲学假设，指出固定效应模型假定存在唯一的单一真值，其推论严格封闭于纳入研究集合。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen, Manion & Morrison (2011, Ch. 17)]] — 系统介绍元分析[[Inverse-Variance Weighting|逆方差加权]]固定效应合成规程与[[Heterogeneity|异质性]]检验决策门槛。
> - [[Argument_Abrami_2015_RER|Abrami et al. (2015)]] — 在[[Critical Thinking|批判性思维]]教学干预综合中对比固定与随机效应模型，因真实情境异质性显著而全面转向随机效应模型。
> - [[Argument_Simpson_2017_JEdPolicy|Simpson (2017)]] — 批判在异质性教育干预中机械套用固定效应模型导致的[[Confidence Interval|置信区间]]虚窄与假阳性检验膨胀。
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit11|Wang & Barabási (2021)]] — 阐明固定效应虽能控制时间恒定的个体特征，但无法完全消除不可测混杂，仍需实验设计支持严格因果识别（p. 248）。
