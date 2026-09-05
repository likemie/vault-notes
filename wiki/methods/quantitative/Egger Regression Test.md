---
title: Egger Regression Test
aliases:
  - "Egger's Test"
  - "Egger's Linear Regression"
  - "Egger Test"
  - "艾格回归检验"
  - "艾格检验"
summary: "由 Matthias Egger 等人（1997）提出的参数化发表偏倚与漏斗图不对称性检验方法。通过对标准化效应量与其精度（标准误的倒数）建立线性回归方程，根据截距项是否显著偏离零来诊断小研究效应与发表偏倚。"
type: method
domain: "research-methodology"
method_type: quantitative
method_family: "quantitative"
method_related_count: 24
method_related_level: 3
method_related_stars: "⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - "method/quantitative"
  - "statistics/meta-analysis"
  - "statistics/publication-bias"
  - "field/research-methodology"
related_concepts:
  - "[[Publication Bias]]"
  - "[[Small Study Effects]]"
  - "[[Effect Size]]"
  - "[[Hypothesis]]"
  - "[[Standard Error]]"
  - "[[Funnel Plot]]"
  - "[[Variable]]"
  - "[[Sample Size Determination]]"
  - "[[Cooperative Learning]]"
  - "[[Problem-Based Learning]]"
  - "[[Critical Thinking]]"
  - "[[Creativity]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Meta-meta-analysis]]"
  - "[[Multilevel Egger's Test]]"
  - "[[Umbrella Review]]"
  - "[[Robust Variance Estimation]]"
  - "[[Fail-Safe N]]"
  - "[[Trim and Fill Method]]"
  - "[[Experimental Research]]"
  - "[[Three-Level Meta-Analysis]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Gungor_2026_CP]]"
  - "[[Argument_Erdem_2026_SHE]]"
  - "[[Argument_Park_2026_TSC]]"
confidence: high
status: draft
created: 2026-08-24
updated: 2026-08-24
---

# Egger Regression Test

---

## 定义

> [!def] 方法定义
> Egger Regression Test（Egger 回归检验 / 艾格回归检验，由流行病学与医学统计学家 Matthias Egger 等人于 1997 年提出）是一种用于检验[[Meta-analysis|元分析]]中[[Publication Bias|发表偏倚]]与**[[Small Study Effects|小研究效应]]（Small-Study Effects）**的经典参数化统计方法。该方法通过将各独立研究的“标准化[[Effect Size|效应量]]（Standardized Effect Size, $Z_i = y_i / \text{SE}_i$）”对“估计精度（Precision, $1 / \text{SE}_i$）”进行加权最小二乘线性回归；若回归方程的**截距项（Intercept）显著偏离零（$p < .05$）**，则表明漏斗图存在显著的单侧不对称性，即小样本研究系统性地报告了相比大样本研究更夸大的效应量。[[Argument_Gungor_2026_CP|(Güngör et al., 2026, pp. 6–8)]]; [[Argument_Erdem_2026_SHE|(Erdem et al., 2026, pp. 960–961)]]

> [!method-scope] 方法范围
> - **研究对象** [[Hypothesis|假设]]抽样相互独立的单水平元分析数据集（包含各研究效应量 $y_i$ 及其[[Standard Error|标准误]] $\text{SE}_i$）。
> - **问题类型** 检验是否存在小样本研究系统性高估效应量的[[Funnel Plot|漏斗图]]不对称与选择性发表偏倚。
> - **分析单位** 包含 $k$ 个独立效应量的一阶元分析或去重后的[[Meta-meta-analysis|二阶元分析]]。
> - **输出形式** 截距估计值（Intercept $a$）、$t$ 统计量、自由度 $df$ 与双尾显著性 $p$ 值。

> [!citation-card]- 关键定义
> Egger 回归检验通过对标准化效应量与精度建立线性模型，定量测定漏斗图不对称程度；截距显著不为零表明小样本研究的效应量系统性偏大（Egger et al., 1997; Borenstein et al., 2021）。[[Argument_Gungor_2026_CP|(Güngör et al., 2026, p. 8)]]
>
> *The Egger regression asymmetry test detects publication bias by regressing the standardized effect size against its precision, where a non-zero intercept indicates funnel plot asymmetry (Egger et al., 1997).*

---

## 经典单水平 Egger 回归 vs 现代多水平 Multilevel Egger's Test

> [!contrast-table] 经典单水平 Egger 回归与第三代多水平 Egger 检验的代际演进对比
> | 比较维度 | 经典单水平 Egger 回归 (Egger et al., 1997) | 现代多水平 Egger 检验 ([[Multilevel Egger's Test\|Rodgers & Pustejovsky, 2021]]) |
> |---|---|---|
> | 方法代际 | 第二代标准[[Meta-analysis\|元分析]]与[[Umbrella Review\|伞状综述]]规范方法 | 第三代现代多水平与集群稳健元分析方法 |
> | 数据依赖结构 | 假定每项研究/[[Effect Size\|效应量]]**完全相互独立** | 允许存在**同一研究多重产出依赖**与**跨元分析嵌套集群（Cluster-Dependence）** |
> | 回归方程设定 | $\frac{y_i}{\text{SE}_i} = a + b \left(\frac{1}{\text{SE}_i}\right) + \epsilon_i$ | $y_{ij} = \beta_0 + \beta_{\text{SE}} \text{SE}_{ij} + \zeta_{(3)j} + \zeta_{(2)ij} + \epsilon_{ij}$ |
> | 方差分解 | 单水平普通/加权残差方差 | **三水平方差分解（Level 1 抽样 / Level 2 簇内 / Level 3 簇间）** |
> | [[Standard Error\|标准误]]校正 | 经典理论模型标准误（聚类数据下会严重低估） | 结合 **[[Robust Variance Estimation\|稳健方差估计（RVE）]]** 提供渐近无偏三明治标准误 |
> | 偏倚校正效应量 | 仅输出偏倚检验显著性 $t$ 值，**不直接输出无偏真实效应量** | **截距项 $\beta_0$ 直接作为剔除样本量偏倚后的“无偏基准效应量”** |

---

## 数学原理与判断标准

> [!formula-step] 公式步骤　经典 Egger 线性回归方程
> $$\frac{y_i}{\text{SE}_i} = a + b \left(\frac{1}{\text{SE}_i}\right) + \epsilon_i$$
>
> **这个公式在做什么**
> 1. 左侧 $\frac{y_i}{\text{SE}_i}$ 为标准化[[Effect Size|效应量]]（相当于标准正态 $Z$ 分数）；
> 2. 右侧解释[[Variable|变量]] $\frac{1}{\text{SE}_i}$ 为估计精度（[[Sample Size Determination|样本量]]越大，精度越高）；
> 3. $b$ 为精度斜率（代表真实潜在效应的平均水平）；
> 4. **截距项 $a$** 为偏倚指标：在无[[Publication Bias|发表偏倚]]时，回归线应穿过原点（即 $a = 0$）；若 $a \neq 0$ 且统计显著，证实存在小研究不对称偏倚。

> [!tip] Egger 检验的判断标准与决策阈值
> - **$p \ge .05$** 截距项未显著偏离 0，判定[[Funnel Plot|漏斗图]]对称，**未检出显著发表偏倚**；
> - **$p < .05$ 且 $a > 0$** 截距显著为正，提示[[Small Study Effects|小样本研究效应]]系统性偏大，**存在显著发表偏倚/小研究效应**。

---

## 经典应用案例

> [!example] [[Argument_Gungor_2026_CP|Güngör et al. (2026)]] [[Cooperative Learning|合作学习]][[Meta-meta-analysis|二阶元分析]]
> 在纳入 23 个[[Effect Size|效应量]]的合作学习二阶[[Meta-analysis|元分析]]中，作者运行经典 Egger 线性回归得出：
> - $t = 2.08, p = .05$（处于不显著与临界交界处），结合[[Fail-Safe N|经典失安全数]]（$N_{\text{fs}} = 4954$）与[[Trim and Fill Method|剪补法]]（$k_{\text{miss}} = 0$），综合判定全库证据稳健无偏倚。[[Argument_Gungor_2026_CP|(Güngör et al., 2026, p. 8)]]

> [!example] [[Argument_Erdem_2026_SHE|Erdem et al. (2026)]] 高等教育[[Problem-Based Learning|问题本位学习]]二阶元分析
> 在探讨问题本位学习对高等教育学生[[Critical Thinking|批判性思维]]等产出影响中：
> - 经典 Egger 回归检验报告 $t(45) = 5.53, p < .001$，提示可能存在小研究代表性不足；作者进一步结合剪补法进行敏感性补入，证实调整后效应量仍高度稳健。[[Argument_Erdem_2026_SHE|(Erdem et al., 2026, pp. 960–961)]]

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Gungor_2026_CP|Güngör et al. (2026)]] — [[Meta-meta-analysis|二阶元分析]]，采用经典 Egger 线性回归（$t = 2.08, p = .05$）检验[[Cooperative Learning|合作学习]]对学习产出的干预效应偏倚。
> - [[Argument_Erdem_2026_SHE|Erdem et al. (2026)]] — 二阶[[Meta-analysis|元分析]]，运用经典 Egger 回归（$t(45) = 5.53, p < .001$）对高等教育 PBL [[Experimental Research|实验研究]]进行偏倚敏感性检验。
> - [[Argument_Park_2026_TSC|Park et al. (2026)]] — [[Three-Level Meta-Analysis|三水平元分析]]，采用经典 Egger 回归（$t(149) = 0.29, p = 0.771$）结合等高线增强[[Funnel Plot|漏斗图]]，检验[[Creativity|创造力]]与[[Critical Thinking|批判性思维]]相关的[[Publication Bias|发表偏倚]]。
