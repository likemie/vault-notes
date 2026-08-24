---
title: Effect Size Conversion
aliases:
  - 效应量转换
  - 效应量换算
  - 效应量指标转换
  - 效应量公式转换
  - Effect Size Transformation
summary: "在元分析与证据合成中，将不同实证设计所报告的效应指标（如 Cohen d、Hedges g、Pearson r 及比值比等）统一换算为同一统计量系的标准化计算方法与数学模型"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 0
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - statistics/meta-analysis
  - theme/effect-size
  - field/research-methodology
confidence: high
status: draft
created: 2026-08-24
updated: 2026-08-24
---

# Effect Size Conversion

---

## 定义

> [!def] 方法定义
> [[Effect Size Conversion|效应量转换]]（Effect Size Conversion）指在[[Meta-analysis|元分析]]（Meta-analysis）与定量证据合成中，运用数学统计模型将来自不同研究设计、测量工具与数据类型（如实验组对照组均值差、相关系数、独立样本 $t$ 检验、二分变量联列表等）的原始统计量，统一转换为可比较的标准化[[Effect Size|效应量]]指标（如皮尔逊相关系数 $r$、标准化均值差 $d$ 或 $g$）的系统化计算程序。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, p. 5)]]

> [!method-scope] 方法范围
> - **研究对象** 原始实证研究所汇报的各类描述统计量与推断统计量（如均值、标准差、相关系数、样本量、$t$ 值、$F$ 值、卡方值、比值比等）。
> - **问题类型** 解决跨研究设计与跨测量尺度间统计量不可比的问题，为多水平建模与元回归提供统一的输入矩阵。
> - **分析单位** 纳入元分析的主要实证研究（Primary Studies）或一阶效应量。
> - **输出形式** 统一的标准化效应量点估计值及其对应的抽样方差（Sampling Variance）与标准误。

> [!citation-card]- 关键定义
> 为了在统一尺度上进行元分析聚合，所有提取的一阶效应量均统一转换为皮尔逊相关系数 $r$，并进一步通过费舍尔 $z$ 变换实现方差稳定化与正态化。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, p. 5)]]
>
> *All effect sizes were converted to Pearson’s r to maintain consistency across studies... and Fisher’s z transformation was applied to normalize the distribution.*

---

## 核心指标与数学换算矩阵

### 1. Cohen's $d$ 与 Hedges' $g$ 的小样本偏倚校正

Cohen's $d$ 表示两组均值差相对于合并标准差的倍数：

$$d = \frac{\bar{X}_1 - \bar{X}_2}{S_{\text{pooled}}}, \quad S_{\text{pooled}} = \sqrt{\frac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{n_1 + n_2 - 2}}$$

在小样本条件下（样本量 $N < 20$），$d$ 会系统性高估总体效应量。Hedges & Olkin (1985) 引入基于自由度 $df = n_1 + n_2 - 2$ 的校正因子 $J(df)$ 得到无偏估计量 Hedges' $g$：

$$g = J(df) \times d$$

常用的一阶极高精度近似计算公式为：

$$J(df) \approx 1 - \frac{3}{4df - 1} = 1 - \frac{3}{4(n_1 + n_2) - 9}$$

- **大样本（$N > 50$）** $J(df) \to 1$，$g \approx d$；
- **小样本（$N < 20$）** $J(df) < 1$（如 $N = 10$ 时约为 $0.90$），$g$ 略小于 $d$ 以剔除样本向上偏倚。

---

### 2. 标准化均值差（$d$ / $g$）与相关系数（$r$）的相互转换

#### 从均值差 $d$ 转换为相关系数 $r$

$$r = \frac{d}{\sqrt{d^2 + a}}$$

其中参数 $a$ 反映两组样本量的平衡程度：

$$a = \frac{(n_1 + n_2)^2}{n_1 n_2}$$

- **两组样本量相等的理想平衡设计（$n_1 = n_2$）** 参数 $a = 4$，公式简化为：

$$r = \frac{d}{\sqrt{d^2 + 4}}$$

- **从 Hedges' $g$ 直接近似转换** 在样本量非极度不平衡时，$r \approx \frac{g}{\sqrt{g^2 + 4}}$。

#### 从相关系数 $r$ 转换为均值差 $d$

在两组样本量相等时：

$$d = \frac{2r}{\sqrt{1 - r^2}}$$

若组间样本量不平衡（$n_1 \ne n_2$），则：

$$d = \frac{r}{\sqrt{1 - r^2}} \cdot \sqrt{\frac{n_1 + n_2}{n_1 n_2}}$$

---

### 3. 比值比（Odds Ratio, $OR$）与连续均值差 $d$ 的转换

在二分类结果变量（如通过/未通过）研究中，比值比 $OR$ 可通过 logit 变换与标准正态分布 Logistic 尺度参数转换：

$$d = \frac{\ln(OR)}{\pi / \sqrt{3}} \approx \frac{\ln(OR)}{1.814}$$

反之：

$$\ln(OR) = \frac{\pi}{\sqrt{3}} d \approx 1.814 d$$

---

### 4. 费舍尔 $z$ 正态化与方差稳定化转换（Fisher's $z$ Transformation）

皮尔逊相关系数 $r$ 的取值受限于 $[-1, 1]$，其抽样分布在远离 0 时偏态严重且方差依赖于总体参数 $\rho$。元分析在统计加权前必须进行费舍尔 $z$ 变换：

$$z = \frac{1}{2} \ln \left( \frac{1 + r}{1 - r} \right) = \operatorname{arctanh}(r)$$

- **抽样方差** 变换后 $z$ 的方差仅取决于样本量 $n$：

$$V_z = \frac{1}{n - 3}, \quad SE_z = \frac{1}{\sqrt{n - 3}}$$

- **逆变换** 在多水平加权合并并完成偏倚校正后，通过反双曲正切函数还原为 $r$ 呈现：

$$r = \frac{e^{2z} - 1}{e^{2z} + 1} = \tanh(z)$$

---

## 经典经验换算对照表

基于两组样本量平衡（$n_1 = n_2$）的理论换算基准如下表所示：

> [!ref-table]- 经典效应量数值换算对照表
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

## 换算操作化规程

> [!proc] 元分析效应量标准化处理四步法
> 1. **原始数据分类提取** 区分各原始研究的设计类型（实验比较前后测组间差 vs 自然状态相关关联）。
> 2. **组内与组间样本量校正** 计算组间样本量分配比率参数 $a = \frac{(n_1 + n_2)^2}{n_1 n_2}$，避免非平衡样本导致的转换失真。
> 3. **统一转换至目标指标** 将所有 $d$、$g$、$t$ 值及 $F$ 值转换为相关系数 $r$（或统一转为 $g$）。
> 4. **正态化变换与逆转换输出** 进行 Fisher's $z$ 变换后运用逆方差权重法进行随机效应建模，汇总后再逆转换为 $r$ 呈现。

---

## 局限与方法学边界

> [!warning]
> 1. **总体分布形态假设限制** $d$ 与 $r$ 的数学转换基于两组数据服从正态分布且方差齐性的假定；若原始数据存在极端偏态或天花板效应，转换后关联系数可能产生失真。
> 2. **人工二分变量导致的衰减偏倚** 将原本连续的变量人为划分为二分类（如高低分组）计算 $d$ 再转为 $r$ 时，会系统性低估真实的相关强度（需运用连续校正公式进行矫正）。
> 3. **群聚依赖效应（Clustering Dependency）** 若单项研究报告多个非独立效应量，直接进行公式转换会造成抽样方差低估，必须结合稳健方差估计（RVE）进行协方差修正。

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关联方向 | 说明 |
> |:-----|:-----|:---------|:-----|
> | [[Effect Size]] | 概念 | 上位概念 | 效应量转换是实现效应量跨设计比较的基础计算工具。 |
> | [[Meta-analysis]] | 方法 | 应用场景 | 元分析依赖效应量转换构建统一的数据矩阵。 |
> | [[Robust Variance Estimation]] | 方法 | 统计进阶 | 效应量转换后常需结合 RVE 校正依赖数据的方差结构。 |
> | [[Argument_Runco_2026_CRJ|Runco et al. (2026)]] | 论证 | 实证应用 | 在创造力二阶元分析中将 164 个一阶效应量统一转换为 $r$ 并行 Fisher's $z$ 变换。 |
