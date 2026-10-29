---
title: Effect Size Conversion
aliases:
  - 效应量转换
  - 效应量换算
  - 效应量指标转换
  - 效应量公式转换
  - 效应量推导
  - Effect Size Transformation
summary: "在元分析与证据合成中，将不同实证设计所报告的效应指标（如 Cohen d、Hedges g、Pearson r 及比值比等）统一换算为同一统计量系的标准化计算方法与数学推导模型"
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
  - theme/effect-size
  - field/research-methodology
related_concepts:
  - "[[Institutional Conversion]]"
  - "[[Variable]]"
  - "[[Scale of Measurement]]"
  - "[[Unit of Analysis]]"
  - "[[Sampling Error]]"
  - "[[Dependent Variable]]"
  - "[[Concept Mapping]]"
  - "[[Visible Learning]]"
  - "[[Commensuration]]"
  - "[[Direct Instruction]]"
  - "[[Zone of Desired Effects]]"
  - "[[Creativity]]"
  - "[[Floor and Ceiling Effects]]"
  - "[[Primary and Secondary Documents]]"
  - "[[Category Mistake]]"
related_methods:
  - "[[Effect Size]]"
  - "[[Meta-analysis]]"
  - "[[Pearson Product-Moment Correlation]]"
  - "[[Descriptive Analysis]]"
  - "[[Sample Size Determination]]"
  - "[[Meta-regression]]"
  - "[[Standard Error]]"
  - "[[Inverse-Variance Weighting]]"
  - "[[Common Language Effect Size]]"
  - "[[Correlational Research]]"
  - "[[Meta-meta-analysis]]"
  - "[[Robust Variance Estimation]]"
  - "[[Covariate Adjustment]]"
related_persons:
  - "[[Gene Glass]]"
  - "[[Jacob Cohen]]"
  - "[[John Hattie]]"
related_arguments:
  - "[[Argument_Runco_2026_CRJ]]"
  - "[[Argument_Wecker_2016_ZfE]]"
  - "[[Argument_Bergeron_2017_MJE]]"
confidence: high
status: draft
created: 2026-08-24
updated: 2026-10-29
---

---

> [!def] Effect Size Conversion
> [[Effect Size Conversion\|效应量转换]]（[[Effect Size]] [[Institutional Conversion|conversion]]）指在[[Meta-analysis\|元分析]]（Meta-analysis）与定量证据合成中，运用数学统计模型将来自不同研究设计、测量工具与数据类型（如实验组对照组均值差、相关系数、独立样本 $t$ 检验、二分[[Variable\|变量]]联列表等）的原始统计量，统一转换为可比较的标准化[[Effect Size\|效应量]]指标（如[[Pearson Product-Moment Correlation\|皮尔逊相关]]系数 $r$、标准化均值差 $d$ 或 $g$）的系统化计算程序与数学推导体系。[[Argument_Runco_2026_CRJ\|(Runco et al., 2026, p. 5)]]

> [!method-scope] 方法范围
> - **研究对象** 原始实证研究所汇报的各类[[Descriptive Analysis\|描述统计]]量与推断统计量（如均值、标准差、相关系数、[[Sample Size Determination\|样本量]]、$t$ 值、$F$ 值、卡方值、比值比等）。
> - **问题类型** 解决跨研究设计与跨[[Scale of Measurement\|测量尺度]]间统计量不可比的问题，为多水平建模与[[Meta-regression\|元回归]]提供统一的输入矩阵。
> - **[[Unit of Analysis\|分析单位]]** 纳入元分析的主要实证研究（Primary Studies）或一阶效应量。
> - **输出形式** 统一的标准化效应量点估计值及其对应的抽样方差（Sampling Variance）与[[Standard Error\|标准误]]。

> [!citation-card] 关键定义
> 为了在统一尺度上进行元分析聚合，所有提取的一阶效应量均统一转换为皮尔逊相关系数 $r$，并进一步通过费舍尔 $z$ 变换实现方差稳定化与正态化。[[Argument_Runco_2026_CRJ\|(Runco et al., 2026, p. 5)]]
>
> *All effect sizes were converted to Pearson’s r to maintain consistency across studies... and Fisher’s z transformation was applied to normalize the distribution.*

---

> [!formula-set]- [[Effect Size\|效应量]]转换与正态化处理全流程
> ```mermaid
> flowchart LR
>   A["原始研究数据<br/>(均值差/t值/r/OR)"] --> B["标准化均值差<br/>Cohen's d"]
>   B -->|"小样本偏倚校正 J(df)"| C["无偏估计量<br/>Hedges' g"]
>   B & C -->|"方差分解转换 a=N²/n₁n₂"| D["皮尔逊相关系数<br/>Pearson's r"]
>   E["二分类比值比<br/>Odds Ratio (OR)"] -->|"Logit 尺度变换 √3/π"| B
>   D -->|"Fisher's z 变换 arctanh(r)"| F["方差稳定化指标<br/>Fisher's z (V=1/(n-3))"]
>   F -->|"元分析加权聚合"| G["二阶合并效应量 ẑ"]
>   G -->|"逆双曲正切 tanh(ẑ)"| H["最终汇报效应量 r̂"]
> ```

---

### 1. Cohen's $d$ 到 Hedges' $g$ 的小样本无偏性推导

> [!formula-step] 公式步骤　Cohen's $d$ 到 Hedges' $g$ 的小样本偏倚校正
> $$g = J(df) \times d = \left[ \frac{\Gamma(df/2)}{\sqrt{df/2} \cdot \Gamma((df-1)/2)} \right] d \approx \left( 1 - \frac{3}{4df - 1} \right) d$$
>
> **这个公式在做什么** 消除小样本条件下 Cohen's $d$ 对总体效应量 $\delta$ 的系统性高估偏倚，产出无偏估计量 Hedges' $g$。
>
> **符号说明** $d$ 为原始标准化均值差；$g$ 为校正后无偏效应量；$df = n_1 + n_2 - 2$ 为自由度；$J(df)$ 为基于伽马函数的纠偏系数。
>
> **推导过程与数学原理**
> 1. 设实验组与对照组独立同分布：$X_{1i} \sim N(\mu_1, \sigma^2)$，$X_{2j} \sim N(\mu_2, \sigma^2)$。
> 2. 合并样本方差 $S_{\text{pooled}}^2 = \frac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{df}$，其[[Sampling Error\|抽样分布]]满足 $\frac{df \cdot S_{\text{pooled}}^2}{\sigma^2} \sim \chi^2(df)$。
> 3. 均值差 $\bar{X}_1 - \bar{X}_2 \sim N\left(\mu_1 - \mu_2, \sigma^2\left(\frac{1}{n_1} + \frac{1}{n_2}\right)\right)$，与 $S_{\text{pooled}}$ 相互独立。
> 4. 计算 $d = \frac{\bar{X}_1 - \bar{X}_2}{S_{\text{pooled}}}$ 的数学期望：
>    $$E[d] = E[\bar{X}_1 - \bar{X}_2] \cdot E\left[\frac{1}{S_{\text{pooled}}}\right] = (\mu_1 - \mu_2) \cdot \frac{1}{\sigma} E\left[\frac{1}{\sqrt{\chi^2(df)/df}}\right] = \delta \cdot \sqrt{\frac{df}{2}} \frac{\Gamma((df-1)/2)}{\Gamma(df/2)}$$
> 5. 易知当 $df < \infty$ 时，$\sqrt{\frac{df}{2}} \frac{\Gamma((df-1)/2)}{\Gamma(df/2)} > 1$，表明 $E[d] > \delta$，即 $d$ 存在向上的正向抽样偏倚。
> 6. 定义校正因子 $J(df) = \frac{\Gamma(df/2)}{\sqrt{df/2}\Gamma((df-1)/2)}$，则 $E[g] = E[J(df) \cdot d] = \delta$。
> 7. 利用泰勒级数展开得到极高精度的一阶近似公式：$J(df) \approx 1 - \frac{3}{4df - 1} = 1 - \frac{3}{4(n_1 + n_2) - 9}$。
>
> **结果怎么读**
> - 当总[[Sample Size Determination\|样本量]]较大（$N > 50$）时，$J(df) \to 1$，$g \approx d$；
> - 当总样本量极小（$N < 20$）时，$J(df) < 1$（如 $N = 10$ 时系数约为 $0.90$），$g$ 会比 $d$ 收缩约 10%，校正小样本研究点估计的正向偏倚；研究在元分析中的权重仍由抽样方差决定，与此校正无关。
>
> **注意事项** 现代[[Meta-analysis\|元分析]]（如 Cochrane 协作网与 Campbell 协作网的综述）通常以 Hedges' $g$ 作为组间比较的标准化均值差指标。

---

### 2. 标准化均值差 $d$ 与点二列相关系数 $r$ 的方差分解推导

> [!formula-step] 公式步骤　均值差 $d$ 与相关系数 $r$ 的相互转换
> $$r = \frac{d}{\sqrt{d^2 + \frac{(n_1 + n_2)^2}{n_1 n_2}}} \xrightarrow{n_1 = n_2} r = \frac{d}{\sqrt{d^2 + 4}}$$
> $$d = \frac{r\sqrt{a}}{\sqrt{1 - r^2}},\quad a = \frac{(n_1 + n_2)^2}{n_1 n_2} \xrightarrow{n_1 = n_2} d = \frac{2r}{\sqrt{1 - r^2}}$$
>
> **这个公式在做什么** 实现两组实验干预效应（标准化均值差）与连续[[Variable\|变量]]关联程度（[[Pearson Product-Moment Correlation\|皮尔逊相关]]系数）之间的双向无缝换算。
>
> **推导过程与数学原理**
> 1. 将实验分组定义为二分指示变量 $X \in \{0, 1\}$，[[Dependent Variable\|因变量]]为连续变量 $Y$。点二列相关系数 $r_{pb}$ 平方等于组间方差占总方差的解释比例（$R^2$ 或 $\eta^2$）：
>    $$r^2 = \frac{SS_{\text{between}}}{SS_{\text{total}}} = \frac{t^2}{t^2 + df}$$
> 2. 独立样本等方差 $t$ 检验统计量与标准化均值差 $d$ 的关系为：
>    $$t = \frac{\bar{X}_1 - \bar{X}_2}{S_{\text{pooled}} \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} = d \sqrt{\frac{n_1 n_2}{n_1 + n_2}}$$
> 3. 将 $t^2 = d^2 \cdot \frac{n_1 n_2}{n_1 + n_2}$ 代入 $r^2$ 表达式，设总样本量 $N = n_1 + n_2$，自由度 $df = N - 2 \approx N$：
>    $$r^2 = \frac{d^2 \frac{n_1 n_2}{N}}{d^2 \frac{n_1 n_2}{N} + N} = \frac{d^2}{d^2 + \frac{N^2}{n_1 n_2}}$$
> 4. 开方即得通用转换公式：$r = \frac{d}{\sqrt{d^2 + a}}$，其中样本分配平衡常数 $a = \frac{(n_1 + n_2)^2}{n_1 n_2}$。
> 5. 当两组样本量严格平衡时（$n_1 = n_2 = N/2$），$a = \frac{N^2}{(N/2)^2} = 4$，简化为经典公式 $r = \frac{d}{\sqrt{d^2 + 4}}$。
> 6. 反向求解 $d$：由 $r^2(d^2 + a) = d^2 \implies a r^2 = d^2(1 - r^2) \implies d = \frac{r\sqrt{a}}{\sqrt{1 - r^2}}$；两组等量时 $a = 4$，即 $d = \frac{2r}{\sqrt{1 - r^2}}$。
>
> **结果怎么读**
> - $d = 0.20 \Longleftrightarrow r = \frac{0.2}{\sqrt{0.04 + 4}} \approx 0.10$（$d$ 的小效应基准）；
> - $d = 0.41 \Longleftrightarrow r = \frac{0.41}{\sqrt{0.168 + 4}} \approx 0.20$（介于 $d$ 的小与中等基准之间，常被引作教育干预基准）；
> - $d = 0.80 \Longleftrightarrow r = \frac{0.8}{\sqrt{0.64 + 4}} \approx 0.37$（$d$ 的大效应基准；按 $r$ 的基准仅属中等偏大）。
>
> **注意事项** 两组样本量不平衡时 $a > 4$（例如 $n_1 = 10, n_2 = 100$ 时 $a = 12.1$）。此时若仍用 $a = 4$ 的简化式，会高估由 $d$ 换算出的 $r$，反向则低估由 $r$ 换算出的 $d$；必须代入实际的 $a$。

---

### 3. 二分类比值比（Odds Ratio）到连续均值差 $d$ 的 Logit 变换推导

> [!formula-step] 公式步骤　比值比 $OR$ 与均值差 $d$ 的转换
> $$d = \frac{\ln(OR)}{\pi / \sqrt{3}} \approx \frac{\ln(OR)}{1.814}, \quad \ln(OR) = \frac{\pi}{\sqrt{3}} d \approx 1.814 d$$
>
> **这个公式在做什么** 将医学与流行病学中广泛使用的二分类比值比（Odds Ratio, $OR$）转换为教育学与心理学通用的连续标准化均值差 $d$。
>
> **推导过程与数学原理**
> 1. 假设二分类结果（如“达标/未达标”）背后存在一个服从 Logistic 分布的潜变量 $Y^*$。
> 2. 标准 Logistic 分布的概率密度函数为 $f(y) = \frac{e^{-y}}{(1 + e^{-y})^2}$，其理论均值为 $0$，理论方差为 $\sigma^2 = \frac{\pi^2}{3}$，标准差为 $\sigma = \frac{\pi}{\sqrt{3}} \approx 1.8138$。
> 3. 对数比值比 $\ln(OR)$ 在数学上严格对应于两个 Logistic 隐变量分布在对数发生比（Logit）尺度上的均值差位移：
>    $$\ln(OR) = \mu_{\text{logit}, 1} - \mu_{\text{logit}, 2}$$
> 4. 将该位移除以标准差 $\sigma = \pi/\sqrt{3}$ 进行标准化，即得到等价的 Cohen's $d$：
>    $$d = \frac{\ln(OR)}{\pi / \sqrt{3}} = \frac{\ln(OR)}{1.814}$$
>
> **结果怎么读**
> - $OR = 1.00 \Longleftrightarrow \ln(OR) = 0 \Longleftrightarrow d = 0.00$（无干预效应）；
> - $OR = 1.44 \Longleftrightarrow \ln(OR) \approx 0.365 \Longleftrightarrow d = 0.20$（小效应）；
> - $OR = 2.10 \Longleftrightarrow \ln(OR) \approx 0.742 \Longleftrightarrow d = 0.41$（介于小与中等之间）；
> - $OR = 4.27 \Longleftrightarrow \ln(OR) \approx 1.452 \Longleftrightarrow d = 0.80$（大效应）。
>
> **注意事项** 该转换（Hasselblad & Hedges, 1995）基于潜在变量服从 Logistic 分布的假设。另有两种常用替代：Cox 法 $d_{\text{Cox}} = \ln(OR) / 1.65$；Probit 法 $d_{\text{Probit}} = \Phi^{-1}(p_1) - \Phi^{-1}(p_2)$，即两组比例对应正态分位数之差。Sánchez-Meca et al. (2003) 的模拟显示，在两组方差相等时 Cox 法与 Probit 法偏差最小；方差不等时各指标均有明显负偏。能取得二分前的连续数据时，应直接计算 $d$。

---

### 4. Fisher's $z$ 正态化与方差稳定化推导（Delta Method）

> [!formula-step] 公式步骤　Fisher's $z$ 变换与方差稳定化
> $$z = \frac{1}{2} \ln \left( \frac{1 + r}{1 - r} \right) = \operatorname{arctanh}(r), \quad V_z = \operatorname{Var}(z) \approx \frac{1}{n - 3}$$
> $$r = \frac{e^{2z} - 1}{e^{2z} + 1} = \tanh(z)$$
>
> **这个公式在做什么** 消除相关系数 $r$ 在边界附近的严重偏态，使其抽样方差完全独立于未知总体参数 $\rho$，实现元分析多水平加权建模的最优正态化。
>
> **推导过程与数学原理**
> 1. 根据大样本理论与 Delta 方法，样本相关系数 $r$ 的渐近方差强烈依赖于未知总体参数 $\rho$：
>    $$\operatorname{Var}(r) \approx \frac{(1 - \rho^2)^2}{n}$$
> 2. 当 $\rho \to \pm 1$ 时，$\operatorname{Var}(r) \to 0$ 且抽样分布严重左偏或右偏，直接进行线性[[Inverse-Variance Weighting\|逆方差加权]]会造成巨大估计偏倚。
> 3. 构造方差稳定化变换函数 $g(r)$，使得变换后变量的方差为常数。由 Delta 方法一阶近似：
>    $$\operatorname{Var}(g(r)) \approx \left[ g'(\rho) \right]^2 \operatorname{Var}(r) \approx \left[ g'(\rho) \right]^2 \frac{(1 - \rho^2)^2}{n} = \text{常数}$$
> 4. 令 $g'(\rho) \propto \frac{1}{1 - \rho^2}$，积分求解该一阶常微分方程：
>    $$g(r) = \int \frac{1}{1 - r^2} dr = \frac{1}{2} \ln \left( \frac{1 + r}{1 - r} \right) = \operatorname{arctanh}(r)$$
> 5. 经过二阶修正后，变换后统计量 $z$ 的抽样方差极度稳定为：
>    $$V_z = \frac{1}{n - 3}, \quad SE_z = \frac{1}{\sqrt{n - 3}}$$
> 6. 统计合并后，利用双曲正切函数的反函数还原：$r = \tanh(z) = \frac{e^{2z}-1}{e^{2z}+1}$。
>
> **结果怎么读**
> - $r = 0.10 \Longleftrightarrow z = 0.1003$；
> - $r = 0.20 \Longleftrightarrow z = 0.2027$；
> - $r = 0.50 \Longleftrightarrow z = 0.5493$；
> - $r = 0.80 \Longleftrightarrow z = 1.0986$（当 $r$ 越大，$z$ 增幅越剧烈，成功拉伸了高相关区间的压缩尺度）。
>
> **注意事项** 在样本量极小（$n < 10$）时，需使用 Hotelling 二阶修正：$E[z] \approx \operatorname{arctanh}(\rho) + \frac{\rho}{2(n-1)}$。

---

### 5. 三大均值差测度（Glass' $\Delta$、Cohen's $d$ 与 Hedges' $g$）的分母辨析与统一换算

> [!formula-step] 公式步骤　三大组间均值差指标的分母设定与换算
> $$\text{Glass' } \Delta = \frac{\bar{X}_1 - \bar{X}_2}{S_2}, \quad \text{Cohen's } d = \frac{\bar{X}_1 - \bar{X}_2}{S_{\text{pooled}}}, \quad \text{Hedges' } g = J(df) \times d$$
> $$S_{\text{pooled}} = \sqrt{\frac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{n_1 + n_2 - 2}}, \quad d = \Delta \times \frac{S_2}{S_{\text{pooled}}}$$
>
> **这个公式在做什么** 厘清元分析中三类标准化均值差指标对总体方差假设的本质差异，纠正跨研究提取时混用除数所导致的数值扭曲。
>
> **推导过程与数学原理**
> 1. **[[Gene Glass|吉恩·格拉斯]]（Gene Glass）的 Glass' $\Delta$** 完全依赖对照组样本标准差 $S_2$（Control Group SD）作为除数。当干预措施可能改变实验组方差、或两组方差齐性假定被严重违背时，Glass' $\Delta$ 避免以受干预影响的方差作分母，因而较为稳健；但它同样存在小样本正向偏倚（可用 $J(n_2 - 1)$ 校正），且由于舍弃了实验组方差信息，其抽样方差较大。
> 2. **[[Jacob Cohen|雅各布·科恩]]（Jacob Cohen）的 Cohen's $d$** 假定两组总体方差齐性（$\sigma_1^2 = \sigma_2^2$），采用合并加权标准差 $S_{\text{pooled}}$ 作为除数，充分利用了两组样本信息以提高估计精度。
> 3. **拉里·赫奇斯（Larry Hedges）的 Hedges' $g$** 在 Cohen's $d$ 基础上引入伽马函数近似纠偏因子 $J(df) \approx 1 - \frac{3}{4(n_1+n_2)-9}$，消除了小样本条件下的正向高估偏倚。
>
> **方法学失范与警示案例**
> [[Argument_Wecker_2016_ZfE|Wecker et al. (2016, pp. 26–27)]] 指出，未经核算与转换直接混用三者属于严重的分析失范。例如在[[Concept Mapping|概念图]]（Concept Mapping）元分析中，Nesbit and Adesope (2006) 汇报的是以对照组标准差作除数的 Glass' $\Delta$，而 Horton et al. (1993) 汇报的是以合并标准差作除数的 Cohen's $d$；二者除数口径差异悬殊，[[John Hattie|哈蒂]]在《[[Visible Learning|可见的学习]]》中未做任何标准化转换便直接混入同一数据池求均值，违背了计量统计的[[Commensuration|通约]]性公理。

---

### 6. 标准误（SE）与标准差（SD）的换算关系与除数混淆灾难

> [!formula-step] 公式步骤　[[Standard Error|标准误]]与标准差的数学换算及除数混淆纠偏
> $$\text{SD} = \text{SE} \times \sqrt{n}, \quad \text{SE} = \frac{\text{SD}}{\sqrt{n}}$$
> $$d_{\text{correct}} = \frac{\bar{X}_1 - \bar{X}_2}{\text{SD}_{\text{pooled}}} = \frac{\bar{X}_1 - \bar{X}_2}{\text{SE}_{\text{pooled}} \times \sqrt{n}} = \frac{d_{\text{error}}}{\sqrt{n}}$$
>
> **这个公式在做什么** 确立样本离散度指标（标准差 SD）与均值抽样精度指标（标准误 SE）之间的严格换算规则，防范元分析数据提取中最具破坏性的除数混淆灾难。
>
> **除数混淆的量级灾难与案例重构**
> 在标准化均值差计算公式中，分母必须是样本标准差（SD）。若数据提取时将原始报告的均值标准误（SE）误作标准差代入分母作除数，计算出的效应量将被虚假放大 $\sqrt{n}$ 倍。
> - **Eisenstaedt et al. (1990) 极端案例重构** Gijbels et al. (2005, p. 56) 在纳入该项关于医学考试成绩的研究时，对照组均值 $80.21$、标准误 $\text{SE} = 1.65$（$n = 107$），实验组均值 $66.53$、标准误 $\text{SE} = 2.74$。数据提取误将标准误 $1.65$ 代入分母：
>   $$d_{\text{error}} = \frac{66.53 - 80.21}{1.65} = -8.291$$
> - **规范还原与纠偏** 由 $\text{SD} = \text{SE} \times \sqrt{n} = 1.65 \times \sqrt{107} \approx 17.07$，真实效应量仅为：
>   $$d_{\text{correct}} = \frac{66.53 - 80.21}{17.07} \approx -0.80$$
> - **实质后果** 除数缩小了逾 10 倍，导致效应量被虚构放大了逾 10 倍（$-0.80 \to -8.291$）；该极端异常值未经核对直接进入宏观数据库，严重扭曲了总体合并结果。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, p. 27)]]

---

### 7. 伪标准误的构造失范（$\text{SD}_d / \sqrt{k}$ 误区）

> [!formula-step] 公式步骤　离散标准差与估计标准误的范畴界定
> $$\text{SE}_{\text{pseudo}} = \frac{\text{SD}_d}{\sqrt{k}} \quad (\text{严重失范}), \quad \text{SE}_{\text{true}} = \sqrt{v_d} = \sqrt{\frac{n_1 + n_2}{n_1 n_2} + \frac{d^2}{2(n_1 + n_2)}}$$
>
> **这个公式在做什么** 揭示以一级主要研究效应量的离散度硬造二阶标准误的算法错误，阐明效应量跨研究变异与点估计抽样精度之间的本质区别。
>
> **方法学机制批判与案例**
> 在缺乏一级元分析合并方差时，部分研究者（如 Hattie）直接拿主要研究效应量的样本标准差（$\text{SD}_d$）除以纳入研究数量的平方根 $\sqrt{k}$ 硬算所谓标准误。[[Argument_Wecker_2016_ZfE|Wecker et al. (2016, pp. 29–30)]] 严正指出：
> 1. $\text{SD}_d$ 反映的是不同研究之间因具体情境、师资或学生差异导致的实质离散度（Between-study dispersion）；
> 2. 合并效应量的标准误（SE）衡量的是均值估计的统计抽样不确定性（Sampling variance），必须基于底层各主要研究的样本量（$N$）和组别方差推算；
> 3. **案例后果** 在[[Direct Instruction|直接教学]]元分析（Haas, 2005）中，该元分析包含 19 个效应量，$\text{SD}_d = 0.59$。哈蒂硬算 $\text{SE}_{\text{Hattie}} = 0.59 / \sqrt{19} \approx 0.135$（赋予权重 $W \approx 54.9$）；而根据真实样本量推算的真实标准误为 $0.092$（对应权重 $W \approx 118.1$）。这一拼凑使直接教学在总体排名中的统计权重被直接腰斩了 53.5%。

---

### 8. 普通语言效应量（Common Language Effect Size, CLES）换算与概率边界规范

> [!formula-step] 公式步骤　标准化均值差到二项[[Common Language Effect Size|超越概率]]的映射
> $$\text{CLES} = \Phi\left(\frac{d}{\sqrt{2}}\right), \quad \text{CLES} \in (0\%, 100\%)$$
>
> **这个公式在做什么** 将连续标准化均值差转换为公众和教师直观可读的概率表述，即从实验组随机抽取一名个体的得分高于从对照组随机抽取个体的概率（McGraw & Wong, 1992；详见 [[Common Language Effect Size]]）。
>
> **数学边界与算法失范**
> - **理论边界** 由于标准正态累积分布函数 $\Phi(z)$ 的值域严格位于 $(0, 1)$ 区间，CLES 在数学上绝不可能出现负值或大于 100% 的情况（当 $d = 0$ 时，$\text{CLES} = 50\%$；当 $d = 0.80$ 时，$\text{CLES} \approx 71.4\%$）。
> - **算法崩溃案例** [[Argument_Wecker_2016_ZfE|Wecker et al. (2016, p. 35, Note 4)]] 与 [[Argument_Bergeron_2017_MJE|Bergeron and Rivard (2017, p. 239)]] 均严正指出，哈蒂在《可见的学习》中采用了一套系统错误的 CLES 换算公式，竟算出了低于 0% 和高于 100% 的不可能概率（如 $-12\%$ 或 $108\%$）；这一低级算法崩溃在德语修订版（Beywl & Zierer, 2015b, p. XVII）中才被强制重算更正。[[Argument_Bergeron_2017_MJE|Bergeron and Rivard (2017)]] 进一步给出了严格的 $d$ 与 CLES 规范映射基准。

---

### 9. 相关向均值差换算的极值发散与弱相关虚增机制

> [!formula-step] 公式步骤　相关系数向 Cohen's d 换算的极值发散与敏感度特征
> $$d = \frac{2r}{\sqrt{1 - r^2}}, \quad \lim_{r \to 1^-} d = +\infty$$
>
> **这个公式在做什么** 接收两变量间的[[Pearson Product-Moment Correlation|皮尔逊相关]]系数 $r$，映射为两组间标准化均值差 $d$（Borenstein et al., 2009）。
>
> **数学直觉与边界** 当相关系数 $r$ 趋向于 1.0 时，分母迅速趋近于零，促使 $d$ 值产生爆炸性发散。$r$ 较小时 $d \approx 2r$，换算本身近似线性；问题在于 $d$ 与 $r$ 的数值尺度和解释基准不同，换算后的 $d$ 容易被按干预效应的基准误读。
>
> **实证误导与因果混淆**
> - **微弱相关跨入[[Zone of Desired Effects|期望效应区]]** 仅仅需要 $r = 0.196$ 的微弱关联，代入公式即可产出 $d = 0.40$，跨入哈蒂所谓的[[Zone of Desired Effects|期望效应区]]。然而在一元线性回归模型中，$r = 0.196$ 对应的决定系数仅为 $R^2 = 0.0385$，意味着仅能解释 3.85% 的变异，剩余 96.15% 属于完全未解释的随机噪声（[[Argument_Bergeron_2017_MJE|Bergeron & Rivard, 2017, p. 242]]）。
> - **横向相关混同干预增量** 将横向[[Correlational Research|相关性研究]]（如智商与[[Creativity|创造力]]测验的得分相关，或学生自我预期成绩与期末实际成绩的自相关）套用此公式硬性转换为 $d$，直接抹除了实验对照与时间先后维度，将相关性错误包装为强效的因果教学干预。

---

### 10. 受控数值模拟反证：三类合法公式导致完全相反排名

> [!row-contrast] 三类技术有效公式对同一受控实验数据的计算结果比对（[[Argument_Bergeron_2017_MJE|Bergeron & Rivard, 2017, pp. 242–245]]）
> | 教学方法组别 | 公式 (a) 与对照组比较（组间） | 公式 (b) 前后比较（组内） | 公式 (c) 相关系数转换为 $d$ |
> |---|---|---|---|
> | **标准对照组（方法 0）** | 0.00 | N/A | $\infty$（无穷大） |
> | **教学方法 1** | 0.14 | 1.00 | 10.00 |
> | **教学方法 2** | 0.27 | 1.00 | 5.00 |
> | **教学方法 3** | 0.39 | 1.00 | 3.33 |
> | **方法优劣排名** | **$3 > 2 > 1 > 0$** | **$1 = 2 = 3$** | **$0 > 1 > 2 > 3$** |
>
> **受控数值模拟反证** 设定四个独立学生组具有相同的初始成绩分布（$\mu=75, \sigma=5$），实施不同教学法，组 0 为标准对照组（增量为 0，$\sigma=0$），方法 1、2、3 分别增加 1、2、3 分，增加值的标准差分别为 1、2、3：
> 1. **公式 (a) 组间比较** 测量新方法相对于标准方法的组间增量，分母为跨组总变异，准确反映真实教学效果梯度（$3 > 2 > 1 > 0$）。
> 2. **公式 (b) 组内前后比较** 测量组内成绩变化与其自身离散度的相对比值。当教学法在提升平均分的同时成比例放大学生间变异时，相除操作直接消除了关键度量维度，导致异质干预被抹平为相同数值（$1 = 2 = 3$）。
> 3. **公式 (c) 相关系数转换** 转化后实质测量线性一致性。对照组成绩完全未变（变异为 0），自相关为 1.0，转换后直接导致 $d \to \infty$；成绩提升越显著但变异越大的干预，相关性反而越弱，换算后效应量垫底（$0 > 1 > 2 > 3$）。
> 4. **方法论裁定** 三种公式各自具有合理的数学基础，但在[[Meta-meta-analysis|二级元分析]]中不加区分地直接混合取均值，导致排行榜反映的只是原始研究碰巧采纳的特定计算公式，证明跨研究设计的通用效应量标尺缺乏统计实体意义。

---

## 经典经验换算对照表

基于两组[[Sample Size Determination|样本量]]平衡（$n_1 = n_2$）的理论换算基准如下表所示：

> [!ref-table]- 经典[[Effect Size|效应量]]数值换算对照表
> | 效应强度参照 | Pearson $r$ | Cohen's $d$ / Hedges' $g$ | 比值比（$OR$） | 解释方差比（$R^2$ / $\eta^2$） |
> |---|---|---|---|---|
> | **微弱效应** | $0.05$ | $0.10$ | $1.20$ | $0.25\%$ |
> | **小效应（$d$ 基准 0.2；$r$ 基准 0.1）** | **$0.10$** | **$0.20$** | **$1.44$** | **$1.00\%$** |
> | **教育干预基准（Runco, 2026）** | **$0.20$** | **$0.41$** | **$2.10$** | **$4.00\%$** |
> | **中等效应（$d$ 基准 0.5）** | **$0.24$** | **$0.50$** | **$2.48$** | **$5.88\%$** |
> | **中等效应（$r$ 基准 0.3）** | **$0.30$** | **$0.63$** | **$3.13$** | **$9.00\%$** |
> | **大效应（$d$ 基准 0.8）** | **$0.37$** | **$0.80$** | **$4.27$** | **$13.7\%$** |
> | **大效应（$r$ 基准 0.5）** | **$0.50$** | **$1.15$** | **$8.12$** | **$25.0\%$** |
>
> Cohen (1988) 对 $d$ 与 $r$ 分别给出基准（$d$：0.2 / 0.5 / 0.8；$r$：0.1 / 0.3 / 0.5），两套基准换算后并不对应，引用时须说明依据哪一套。

> [!tip] 经验换算速算规则
> 在 $r \le 0.30$ 的常见范围内，$d$ 与 $g$ 的数值约为相关系数 $r$ 的 **$2.0$ 至 $2.1$ 倍**；$r = 0.50$ 时约为 $2.3$ 倍；解释方差比等于 $r^2$。

---

> [!software-impl] 统计软件实现代码
> - **R 语言环境（推荐 `metafor` 与 `esc` 包）**
>   ```R
>   library(metafor)
>   library(effectsize)  # d_to_r()；esc 包对应函数为 convert_d2r()
>   
>   # 1. 从均值与标准差计算 Cohen's d 并转为 Hedges' g
>   d_calc <- escalc(measure = "SMD", m1i = m1, sd1i = sd1, n1i = n1,
>                    m2i = m2, sd2i = sd2, n2i = n2, data = dat)
>   
>   # 2. 从 d / g 转换为 r 及 Fisher's z
>   r_val <- d_to_r(d = 0.41)
>   z_val <- transf.rtoz(r_val)
>   
>   # 3. 从 Fisher's z 逆转换为 r
>   r_back <- transf.ztor(z_val)
>   ```
> - **Python 环境（`scipy.stats` 与 `numpy`）**
>   ```python
>   import numpy as np
>   from scipy.special import gamma
>   
>   def hedges_g(d, n1, n2):
>       df = n1 + n2 - 2
>       j = 1 - (3 / (4 * df - 1))
>       return j * d
>   
>   def d_to_r(d, n1, n2):
>       a = ((n1 + n2) ** 2) / (n1 * n2)
>       return d / np.sqrt(d ** 2 + a)
>   
>   def fisher_z(r):
>       return np.arctanh(r)
>   
>   def inv_fisher_z(z):
>       return np.tanh(z)
>   ```

---

> [!warning] 局限与方法学边界
> 1. **总体分布形态假设限制** $d$ 与 $r$ 的数学转换基于两组数据服从正态分布且方差齐性的假定；若原始数据存在极端偏态或[[Floor and Ceiling Effects|天花板效应]]，转换后关联系数可能产生失真。
> 2. **人工二分[[Variable|变量]]导致的衰减偏倚** 将原本连续的变量人为划分为二分类（如高低分组）计算 $d$ 再转为 $r$ 时，会系统性低估真实的相关强度（需运用连续校正公式进行矫正）。
> 3. **群聚依赖效应（Clustering Dependency）** 若单项研究报告多个非独立[[Effect Size|效应量]]，直接进行公式转换会造成抽样方差低估，必须结合[[Robust Variance Estimation|稳健方差估计]]（RVE）进行协方差修正。
> 4. **分母除数混淆与伪[[Standard Error|标准误]]滥用风险** 必须严格审查[[Primary and Secondary Documents|原始文献]]汇报的离散量是标准差（SD）还是均值标准误（SE），防止除数混淆引发 $\sqrt{n}$ 倍量级灾难；严禁直接拿效应量跨研究离散度 $\text{SD}_d / \sqrt{k}$ 拼凑伪标准误。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, p. 27)]]
> 5. **测度分母不可直接[[Commensuration|通约]]风险** Glass' $\Delta$、Cohen's $d$ 与 Hedges' $g$ 具有不同的分母假设，在未统一转换前直接混入同一池求平均属于范畴通约失范。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, p. 26)]]
> 6. **换算公式选择依赖与排序颠倒风险** 均值差效应量换算高度依赖具体的[[Covariate Adjustment|协变量控制]]与标准差选择模型。在受控数值实验中，针对同一组多条件实证数据，选择不同的合法换算公式不仅会导致数值巨幅波动，甚至会诱发排名的完全颠倒（如从严格递增逆转为严格递减）。研究者不得在未检验公式适用边界的前提下进行跨研究排序。[[Argument_Bergeron_2017_MJE|(Bergeron & Rivard, 2017, p. 242)]]

---

> [!entry-map] 条目关联
>
> | 条目 | 类型 | 关联方向 | 说明 |
> |:-----|:-----|:---------|:-----|
> | [[Effect Size]] | 概念 | 上位概念 | 效应量转换是实现效应量跨设计比较的基础计算工具。 |
> | [[Common Language Effect Size]] | 方法 | 概率化衍生 | 将连续均值差效应量 $d$ 映射为二元随机抽样胜率的非标准化表达，在违背正态假定或极端效应下存在概率崩溃风险。 |
> | [[Meta-analysis]] | 方法 | 应用场景 | 元分析依赖效应量转换构建统一的数据矩阵。 |
> | [[Robust Variance Estimation]] | 方法 | 统计进阶 | 效应量转换后常需结合 RVE 校正依赖数据的方差结构。 |
> | [[Category Mistake]] | 概念 | 方法学批判 | 未作标准化转换直接混用异质分母测度构成范畴[[Commensuration\|通约]]失范。 |
> | [[Argument_Runco_2026_CRJ\|Runco et al. (2026)]] | 论证 | 实证应用 | 在创造力二阶元分析中将 164 个一阶效应量统一转换为 $r$ 并行 Fisher's $z$ 变换。 |
> | [[Argument_Wecker_2016_ZfE\|Wecker et al. (2016)]] | 论证 | 方法学批判与审计 | 系统揭示[[Standard Error\|标准误]]当作标准差导致效应量虚增十倍、三大均值差测度混用以及伪标准误拼凑失范等典型灾难案例。 |
> | [[Argument_Bergeron_2017_MJE\|Bergeron and Rivard (2017)]] | 论证 | 数理审计与反例反证 | 揭示 CLES 负概率失范，并以数值实验证实 $r \to d$ 极值爆炸及三类公式导致完全矛盾排名。 |
