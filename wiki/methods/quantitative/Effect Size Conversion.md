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
method_related_count: 15
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - statistics/meta-analysis
  - theme/effect-size
  - field/research-methodology
related_concepts:
  - "[[Effect Size]]"
  - "[[Variable]]"
  - "[[Descriptive Analysis]]"
  - "[[Sample Size Determination]]"
  - "[[Scale of Measurement]]"
  - "[[Standard Error]]"
  - "[[Sampling Error]]"
  - "[[Dependent Variable]]"
  - "[[Hypothesis]]"
related_methods:
  - "[[Meta-analysis]]"
  - "[[Pearson Product-Moment Correlation]]"
  - "[[Meta-regression]]"
  - "[[Inverse-Variance Weighting]]"
  - "[[Robust Variance Estimation]]"
related_arguments:
  - "[[Argument_Runco_2026_CRJ]]"
confidence: high
status: draft
created: 2026-08-24
updated: 2026-08-24
---

# Effect Size Conversion

---

## 定义

> [!def] 方法定义
> [[Effect Size Conversion|效应量转换]]（[[Effect Size]] Conversion）指在[[Meta-analysis|元分析]]（Meta-analysis）与定量证据合成中，运用数学统计模型将来自不同研究设计、测量工具与数据类型（如实验组对照组均值差、相关系数、独立样本 $t$ 检验、二分[[Variable|变量]]联列表等）的原始统计量，统一转换为可比较的标准化[[Effect Size|效应量]]指标（如[[Pearson Product-Moment Correlation|皮尔逊相关]]系数 $r$、标准化均值差 $d$ 或 $g$）的系统化计算程序与数学推导体系。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, p. 5)]]

> [!method-scope] 方法范围
> - **研究对象** 原始实证研究所汇报的各类[[Descriptive Analysis|描述统计]]量与推断统计量（如均值、标准差、相关系数、[[Sample Size Determination|样本量]]、$t$ 值、$F$ 值、卡方值、比值比等）。
> - **问题类型** 解决跨研究设计与跨[[Scale of Measurement|测量尺度]]间统计量不可比的问题，为多水平建模与[[Meta-regression|元回归]]提供统一的输入矩阵。
> - **分析单位** 纳入元分析的主要实证研究（Primary Studies）或一阶效应量。
> - **输出形式** 统一的标准化效应量点估计值及其对应的抽样方差（Sampling Variance）与[[Standard Error|标准误]]。

> [!citation-card]- 关键定义
> 为了在统一尺度上进行元分析聚合，所有提取的一阶效应量均统一转换为皮尔逊相关系数 $r$，并进一步通过费舍尔 $z$ 变换实现方差稳定化与正态化。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, p. 5)]]
>
> *All effect sizes were converted to Pearson’s r to maintain consistency across studies... and Fisher’s z transformation was applied to normalize the distribution.*

---

## 公式推导流程与核心族系转换

> [!formula-set] [[Effect Size|效应量]]转换与正态化处理全流程
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
> 2. 合并样本方差 $S_{\text{pooled}}^2 = \frac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{df}$，其[[Sampling Error|抽样分布]]满足 $\frac{df \cdot S_{\text{pooled}}^2}{\sigma^2} \sim \chi^2(df)$。
> 3. 均值差 $\bar{X}_1 - \bar{X}_2 \sim N\left(\mu_1 - \mu_2, \sigma^2\left(\frac{1}{n_1} + \frac{1}{n_2}\right)\right)$，与 $S_{\text{pooled}}$ 相互独立。
> 4. 计算 $d = \frac{\bar{X}_1 - \bar{X}_2}{S_{\text{pooled}}}$ 的数学期望：
>    $$E[d] = E[\bar{X}_1 - \bar{X}_2] \cdot E\left[\frac{1}{S_{\text{pooled}}}\right] = (\mu_1 - \mu_2) \cdot \frac{1}{\sigma} E\left[\frac{1}{\sqrt{\chi^2(df)/df}}\right] = \delta \cdot \sqrt{\frac{df}{2}} \frac{\Gamma((df-1)/2)}{\Gamma(df/2)}$$
> 5. 易知当 $df < \infty$ 时，$\sqrt{\frac{df}{2}} \frac{\Gamma((df-1)/2)}{\Gamma(df/2)} > 1$，表明 $E[d] > \delta$，即 $d$ 存在向上的正向抽样偏倚。
> 6. 定义校正因子 $J(df) = \frac{\Gamma(df/2)}{\sqrt{df/2}\Gamma((df-1)/2)}$，则 $E[g] = E[J(df) \cdot d] = \delta$。
> 7. 利用泰勒级数展开得到极高精度的一阶近似公式：$J(df) \approx 1 - \frac{3}{4df - 1} = 1 - \frac{3}{4(n_1 + n_2) - 9}$。
>
> **结果怎么读**
> - 当总[[Sample Size Determination|样本量]]较大（$N > 50$）时，$J(df) \to 1$，$g \approx d$；
> - 当总样本量极小（$N < 20$）时，$J(df) < 1$（如 $N = 10$ 时系数约为 $0.90$），$g$ 会比 $d$ 收缩约 10%，有效防止小样本研究在元分析中过度加权。
>
> **注意事项** 现代[[Meta-analysis|元分析]]（尤其 Cochrane 协作网与 Campbell 协作网）均以 Hedges' $g$ 作为组间比较的标准分析单位。

---

### 2. 标准化均值差 $d$ 与点二列相关系数 $r$ 的方差分解推导

> [!formula-step] 公式步骤　均值差 $d$ 与相关系数 $r$ 的相互转换
> $$r = \frac{d}{\sqrt{d^2 + \frac{(n_1 + n_2)^2}{n_1 n_2}}} \xrightarrow{n_1 = n_2} r = \frac{d}{\sqrt{d^2 + 4}}$$
> $$d = \frac{r}{\sqrt{1 - r^2}} \sqrt{\frac{n_1 + n_2}{n_1 n_2}} \xrightarrow{n_1 = n_2} d = \frac{2r}{\sqrt{1 - r^2}}$$
>
> **这个公式在做什么** 实现两组实验干预效应（标准化均值差）与连续[[Variable|变量]]关联程度（[[Pearson Product-Moment Correlation|皮尔逊相关]]系数）之间的双向无缝换算。
>
> **推导过程与数学原理**
> 1. 将实验分组定义为二分指示变量 $X \in \{0, 1\}$，[[Dependent Variable|因变量]]为连续变量 $Y$。点二列相关系数 $r_{pb}$ 平方等于组间方差占总方差的解释比例（$R^2$ 或 $\eta^2$）：
>    $$r^2 = \frac{SS_{\text{between}}}{SS_{\text{total}}} = \frac{t^2}{t^2 + df}$$
> 2. 独立样本等方差 $t$ 检验统计量与标准化均值差 $d$ 的关系为：
>    $$t = \frac{\bar{X}_1 - \bar{X}_2}{S_{\text{pooled}} \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} = d \sqrt{\frac{n_1 n_2}{n_1 + n_2}}$$
> 3. 将 $t^2 = d^2 \cdot \frac{n_1 n_2}{n_1 + n_2}$ 代入 $r^2$ 表达式，设总样本量 $N = n_1 + n_2$，自由度 $df = N - 2 \approx N$：
>    $$r^2 = \frac{d^2 \frac{n_1 n_2}{N}}{d^2 \frac{n_1 n_2}{N} + N} = \frac{d^2}{d^2 + \frac{N^2}{n_1 n_2}}$$
> 4. 开方即得通用转换公式：$r = \frac{d}{\sqrt{d^2 + a}}$，其中样本分配平衡常数 $a = \frac{(n_1 + n_2)^2}{n_1 n_2}$。
> 5. 当两组样本量严格平衡时（$n_1 = n_2 = N/2$），$a = \frac{N^2}{(N/2)^2} = 4$，简化为经典公式 $r = \frac{d}{\sqrt{d^2 + 4}}$。
> 6. 反向求解 $d$：由 $r^2(d^2 + 4) = d^2 \implies 4r^2 = d^2(1 - r^2) \implies d = \frac{2r}{\sqrt{1 - r^2}}$。
>
> **结果怎么读**
> - $d = 0.20 \Longleftrightarrow r = \frac{0.2}{\sqrt{0.04 + 4}} \approx 0.10$（小效应）；
> - $d = 0.41 \Longleftrightarrow r = \frac{0.41}{\sqrt{0.168 + 4}} \approx 0.20$（中等效应/教育干预基准）；
> - $d = 0.80 \Longleftrightarrow r = \frac{0.8}{\sqrt{0.64 + 4}} \approx 0.37$（大效应）。
>
> **注意事项** 若原始研究两组样本量极不平衡（例如 $n_1 = 10, n_2 = 100$），必须使用带样本权重 $a$ 的完整公式，否则会严重低估转换后的相关系数 $r$。

---

### 3. 二分类比值比（Odds Ratio）到连续均值差 $d$ 的 Logit 变换推导

> [!formula-step] 公式步骤　比值比 $OR$ 与均值差 $d$ 的转换
> $$d = \frac{\ln(OR)}{\pi / \sqrt{3}} \approx \frac{\ln(OR)}{1.814}, \quad \ln(OR) = \frac{\pi}{\sqrt{3}} d \approx 1.814 d$$
>
> **这个公式在做什么** 将医学与流行病学中广泛使用的二分类比值比（Odds Ratio, $OR$）转换为教育学与心理学通用的连续标准化均值差 $d$。
>
> **推导过程与数学原理**
> 1. [[Hypothesis|假设]]二分类结果（如“达标/未达标”）背后存在一个服从 Logistic 分布的潜变量 $Y^*$。
> 2. 标准 Logistic 分布的概率密度函数为 $f(y) = \frac{e^{-y}}{(1 + e^{-y})^2}$，其理论均值为 $0$，理论方差为 $\sigma^2 = \frac{\pi^2}{3}$，标准差为 $\sigma = \frac{\pi}{\sqrt{3}} \approx 1.8138$。
> 3. 对数比值比 $\ln(OR)$ 在数学上严格对应于两个 Logistic 隐变量分布在对数发生比（Logit）尺度上的均值差位移：
>    $$\ln(OR) = \mu_{\text{logit}, 1} - \mu_{\text{logit}, 2}$$
> 4. 将该位移除以标准差 $\sigma = \pi/\sqrt{3}$ 进行标准化，即得到等价的 Cohen's $d$：
>    $$d = \frac{\ln(OR)}{\pi / \sqrt{3}} = \frac{\ln(OR)}{1.814}$$
>
> **结果怎么读**
> - $OR = 1.00 \Longleftrightarrow \ln(OR) = 0 \Longleftrightarrow d = 0.00$（无干预效应）；
> - $OR = 1.44 \Longleftrightarrow \ln(OR) \approx 0.365 \Longleftrightarrow d = 0.20$（小效应）；
> - $OR = 2.10 \Longleftrightarrow \ln(OR) \approx 0.742 \Longleftrightarrow d = 0.41$（中等效应）；
> - $OR = 4.27 \Longleftrightarrow \ln(OR) \approx 1.452 \Longleftrightarrow d = 0.80$（大效应）。
>
> **注意事项** 该转换基于潜在变量服从 Logistic 分布的假设；若假设潜在变量服从标准正态分布（Probit 模型），除数常数变为 $\pi / \sqrt{3} \approx 1.65$。Hasselblad & Hedges (1995) 证明 Logistic 转换在多数情境下具有更优的稳健性。

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
> 2. 当 $\rho \to \pm 1$ 时，$\operatorname{Var}(r) \to 0$ 且抽样分布严重左偏或右偏，直接进行线性[[Inverse-Variance Weighting|逆方差加权]]会造成巨大估计偏倚。
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

## 经典经验换算对照表

基于两组[[Sample Size Determination|样本量]]平衡（$n_1 = n_2$）的理论换算基准如下表所示：

> [!ref-table]- 经典[[Effect Size|效应量]]数值换算对照表
> | 效应强度等级（Cohen, 1988） | Pearson $r$ | Cohen's $d$ / Hedges' $g$ | 比值比（$OR$） | 解释方差比（$R^2$ / $\eta^2$） |
> |---|---|---|---|---|
> | **微弱效应（Negligible）** | $0.05$ | $0.10$ | $1.20$ | $0.25\%$ |
> | **小效应（Small）** | **$0.10$** | **$0.20$** | **$1.44$** | **$1.00\%$** |
> | **中等效应（Medium）** | **$0.20$** | **$0.41$** | **$2.10$** | **$4.00\%$** |
> | **教育干预基准（Runco, 2026）** | **$0.20$** | **$0.41$** | **$2.10$** | **$4.00\%$** |
> | **大效应门槛（Medium-to-Large）** | **$0.30$** | **$0.63$** | **$3.14$** | **$9.00\%$** |
> | **大效应（Large）** | **$0.37$** | **$0.80$** | **$4.27$** | **$13.7\%$** |
> | **极大效应（Very Large）** | **$0.50$** | **$1.15$** | **$8.06$** | **$25.0\%$** |

> [!tip] 经验换算速算规则
> 在教育与心理学实证研究中，$d$ 与 $g$ 的数值通常约为相关系数 $r$ 的 **$2.0$ 至 $2.1$ 倍**；解释方差比约为 $r^2$。

---

## 软件实现与代码规程

> [!software-impl] 统计软件实现代码
> - **R 语言环境（推荐 `metafor` 与 `esc` 包）**
>   ```R
>   library(metafor)
>   library(esc)
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

## 局限与方法学边界

> [!warning]
> 1. **总体分布形态[[Hypothesis|假设]]限制** $d$ 与 $r$ 的数学转换基于两组数据服从正态分布且方差齐性的假定；若原始数据存在极端偏态或天花板效应，转换后关联系数可能产生失真。
> 2. **人工二分[[Variable|变量]]导致的衰减偏倚** 将原本连续的变量人为划分为二分类（如高低分组）计算 $d$ 再转为 $r$ 时，会系统性低估真实的相关强度（需运用连续校正公式进行矫正）。
> 3. **群聚依赖效应（Clustering Dependency）** 若单项研究报告多个非独立[[Effect Size|效应量]]，直接进行公式转换会造成抽样方差低估，必须结合[[Robust Variance Estimation|稳健方差估计]]（RVE）进行协方差修正。

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关联方向 | 说明 |
> |:-----|:-----|:---------|:-----|
> | [[Effect Size]] | 概念 | 上位概念 | 效应量转换是实现效应量跨设计比较的基础计算工具。 |
> | [[Meta-analysis]] | 方法 | 应用场景 | 元分析依赖效应量转换构建统一的数据矩阵。 |
> | [[Robust Variance Estimation]] | 方法 | 统计进阶 | 效应量转换后常需结合 RVE 校正依赖数据的方差结构。 |
> | [[Argument_Runco_2026_CRJ\|Runco et al. (2026)]] | 论证 | 实证应用 | 在创造力二阶元分析中将 164 个一阶效应量统一转换为 $r$ 并行 Fisher's $z$ 变换。 |
