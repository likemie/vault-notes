---
title: Prediction Interval
aliases:
  - 预测区间
  - 95%预测区间
  - 预测区间估计
  - prediction intervals
summary: "元分析中综合了抽样误差与研究间真实异质性方差（τ²），用于估计未来单一全新实证情境下个体效应量可能分布范围的统计推断区间。"
type: concept
domain: "research-methodology"
related_count: 22
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
tags:
  - field/research-methodology
  - topic/quantitative-methods
  - theme/meta-analysis
related_concepts:
  - "[[Effect Size]]"
  - "[[Standard Error]]"
  - "[[Sampling Error]]"
  - "[[Heterogeneity]]"
  - "[[Between-Study Variance]]"
  - "[[Hypothesis]]"
  - "[[Variable]]"
  - "[[Confidence Interval]]"
  - "[[Sample Size Determination]]"
  - "[[Creativity]]"
  - "[[Independent Variable]]"
  - "[[Evidence-Based Education]]"
  - "[[Creativity Training]]"
  - "[[Dependent Variable]]"
related_methods:
  - "[[Fixed-Effect and Random-Effects Models]]"
  - "[[Meta-analysis]]"
  - "[[Meta-meta-analysis]]"
  - "[[Inverse-Variance Weighting]]"
  - "[[Correlated and Hierarchical Effects Model]]"
  - "[[Intervention Research]]"
  - "[[Robust Variance Estimation]]"
related_arguments:
  - "[[Argument_Runco_2026_CRJ]]"
confidence: medium
status: draft
created: 2026-08-24
updated: 2026-08-24
---

# Prediction Interval

---

## 定义

> [!def] 核心定义
> [[Prediction Interval|预测区间]]（Prediction Interval, PI）是指在[[Fixed-Effect and Random-Effects Models|随机效应模型]]（Random-Effects Model）的[[Meta-analysis|元分析]]与[[Meta-meta-analysis|二阶元分析]]中，**同时综合汇总[[Effect Size|效应量]]的[[Standard Error|标准误]]（[[Sampling Error|抽样误差]]）与研究间真实[[Heterogeneity|异质性]]方差（[[Between-Study Variance]], $\tau^2$）**，用以量化估计**在未来某个单一全新实证情境或特定研究总体中，真实[[Effect Size|效应量]]落入该区间的预期概率范围（通常为 95%）**的统计推断指标（Higgins et al., 2009; Borenstein et al., 2009, 2017; [[Argument_Runco_2026_CRJ|Runco et al., 2026, pp. 5, 8, 10]]）。

> [!concept-lens] 概念透镜
> - **含义** 指向元分析结论在具体实践情境中真实效果的不确定性与离散范围，而非单纯的全局平均值精度。
> - **用途** 帮助教育决策者与研究者避免将“平均效应显著为正”盲目等同于“在任何学校或课堂都能产生正向效果”，揭示具体情境对干预成败的决定性影响。
> - **边界** 预测区间要求纳入研究数量（$k$）足够充足（通常 $k \ge 10$）且真实效应服从正态分布[[Hypothesis|假设]]；当 $k$ 较小时基于 $t$ 分布自由度构建的预测区间会极其宽泛。

> [!citation-card]- 关键表述
> 必须指出，这里报告的统计量是平均值，并不必然指示在任何单一独立样本中会发现什么结果。人口背景[[Variable|变量]]的预测区间为 −0.38 至 0.49，表明真实效应量的范围可以从负相关一直跨越到正相关。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, p. 10)]]
>
> *The statistics are averages that are not necessarily indicative of what might be found in any single sample. The prediction interval for background variables was −.38 to .49, indicating that the true effect size could range from a negative correlation to a positive correlation.*

> [!boundary]- 概念边界
> - 不等于 [[Confidence Interval|置信区间]]（CI） — 置信区间衡量的是“总体均值（Mean Effect Size）”的估计精度；预测区间衡量的是“具体单一新研究真实效应”的分布广度。
> - 不等于可信区间（Credibility Interval） — 预测区间多见于经典频率学派随机效应元分析；可信区间源自贝叶斯后验分布或 Hunter-Schmidt 心理测量学元分析。

---

## 概念辨析

> [!contrast-table] [[Confidence Interval|置信区间]]（CI） vs 预测区间（PI）
> | 比较维度 | 置信区间（Confidence Interval, CI） | 预测区间（Prediction Interval, PI） |
> |---|---|---|
> | **估计目标** | 估计**全领域总体平均效应量（$\mu$）** | 估计**未来某一个具体研究情境中的真实效应量（$\theta_{\text{new}}$）** |
> | **方差构成** | 仅包含总体均值的抽样方差 $\operatorname{SE}(\hat{\mu})^2 = \frac{1}{\sum w_i}$ | 包含抽样方差 + **研究间真实异质性方差（$\operatorname{SE}^2 + \hat{\tau}^2$）** |
> | **[[Sample Size Determination|样本量]]增加的影响** | 当 $k \to \infty$ 时，CI 宽度收敛趋近于 0（精度无限提高） | 当 $k \to \infty$ 时，PI 宽度收敛于固定范围 $\pm 1.96 \tau$（反映真实固有异质性） |
> | **区间宽度关系** | **在存在真实异质性（$\tau^2 > 0$）时，CI 显著窄于 PI** | **PI 宽度必然大于或等于 CI 宽度** |
> | **实证决策价值** | 回答“该干预平均而言在宏观上是否有效？” | 回答“如果我在我的特定学校实施该干预，效果预期有多大波动？” |

---

## 核心统计模型与数学公式

> [!formula-step] [[Fixed-Effect and Random-Effects Models|随机效应模型]] 95% 预测区间计算公式
> $$\text{PI}_{95\%} = \hat{\mu} \pm t_{0.025, \, \text{df}} \sqrt{\operatorname{SE}(\hat{\mu})^2 + \hat{\tau}^2}$$
>
> **这个公式在做什么** 在汇总[[Effect Size|效应量]] $\hat{\mu}$ 的基础上，不仅加上平均值估计的[[Standard Error|标准误]]，更将研究间真实效应变异方差 $\hat{\tau}^2$ 开根号后通过自由度为 $\text{df} = k - 2$（或 Satterthwaite 近似自由度）的临界 $t$ 值进行外推扩展。（pp. 5–6）
>
> **符号说明**
> - $\hat{\mu}$：经[[Inverse-Variance Weighting|逆方差加权]]合并后的平均效应量（如费舍尔 $z$ 或相关系数 $r$）。
> - $\operatorname{SE}(\hat{\mu})$：合并效应量的标准误。
> - $\hat{\tau}^2$：研究间真实效应[[Heterogeneity|异质性]]方差估计值（通过 REML 或 [[Correlated and Hierarchical Effects Model|CHE]] 模型估计）。
> - $t_{0.025, \, \text{df}}$：双侧显著性水平 $\alpha = 0.05$ 下 $t$ 分布的临界分位数。
>
> **数学直觉** 哪怕[[Meta-analysis|元分析]]纳入了数万名被试使得 $\operatorname{SE}(\hat{\mu}) \approx 0$（[[Confidence Interval|置信区间]]极窄），如果不同学校之间的真实效果差异很大（$\tau = 0.20$），预测区间的半宽依然至少为 $1.96 \times 0.20 = 0.392$，直观反映了真实世界中的情境变异。

---

## 围绕概念形成的命题

### 命题一　预测区间是评估元分析结论生态有效性与可推广性的核心安全边界

> [!concept-lens] 生态有效性与情境[[Heterogeneity|异质性]]
> 探讨单纯依赖[[Confidence Interval|置信区间]]如何掩盖干预措施在不良情境下的潜在无效或负向风险。

> [!claim] Higgins et al. (2009); Borenstein et al. (2017)
> **均值显著性掩盖情境风险** 在高度异质性的教育与心理[[Intervention Research|干预研究]]中，经常出现“总体均值显著为正（$p < .001, \text{CI} = [0.15, 0.25]$），但 95% 预测区间跨越 0（$\text{PI} = [-0.10, 0.50]$）”的现象。这意味着尽管干预在平均水平上是有益的，但在特定教师资质、学生背景或执行偏差的学校中，干预存在产生无效甚至负面后果的真实概率。忽略预测区间会导致虚假的安全感。

---

### 命题二　二阶元分析预测区间证实创造力干预与相关因素具有强烈的具体情境依赖性

> [!concept-lens] 宏观二阶预测区间与情境调节
> 探讨全领域[[Meta-meta-analysis|二阶元分析]]各亚组预测区间跨越 0 的实证含义。

> [!claim] [[Argument_Runco_2026_CRJ|Runco et al. (2026)]]; Kraft (2020)
> **全领域预测区间的情境敏感性** 在包含 124 万被试的[[Creativity|创造力]]二阶[[Meta-analysis|元分析]]中，各亚组的 95% 预测区间均呈现出宽广且跨越 0 的特征：教育干预亚组平均效应为 $r = 0.20$（CI $[0.10, 0.29]$），但预测区间为 $[-0.20, 0.54]$；[[Independent Variable|预测变量]]亚组为 $r = 0.29$，预测区间为 $[-0.10, 0.61]$。多水平 [[Robust Variance Estimation|RVE]] 建模结果表明，尽管创造潜能与教育干预在全领域呈现出极其稳健的正向总体关联，但由于现实中教学法实施质量、学科领域与组织支持力度的巨大差异，具体教学成效高度依赖于即时情境的微观调适。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, pp. 6–10)]]

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **生态边界约束** | 预测区间结合了真实异质性 $\tau^2$，揭示具体情境下的波动风险与生态边界 | 元分析结果解读、[[Evidence-Based Education|循证教育]]政策制定 | Higgins et al. (2009); Borenstein et al. (2017) |
> | **二阶宏观情境敏感性** | 宏观二阶元分析预测区间跨越 0，证实[[Creativity Training|创造力干预]]效果对微观教学情境高度敏感 | 创造力教学实施、二阶[[Effect Size|效应量]]解释 | [[Argument_Runco_2026_CRJ|Runco et al. (2026)]]; Kraft (2020) |

---

## 元分析实证案例表

> [!ref-table] [[Argument_Runco_2026_CRJ|Runco et al. (2026)]] [[Creativity|创造力]][[Meta-meta-analysis|二阶元分析]]各亚组[[Confidence Interval|置信区间]]与预测区间对照表
>
> | 调节[[Variable|变量]]与亚组 | 汇总二阶效应量（$r$） | 95% 置信区间（CI） | 95% 预测区间（PI） | PI 跨越 0 的实践解释 |
> |---|---|---|---|---|
> | **创造力作为[[Independent Variable|预测变量]]** | **$r = 0.29$** | $[0.18, 0.41]$ | $[-0.10, 0.61]$ | 潜能平均预测力强，但在个别极端情境中预测力受限 |
> | **创造力作为[[Dependent Variable|结果变量]]** | **$r = 0.12$** | $[0.05, 0.19]$ | $[-0.25, 0.47]$ | 效标[[Heterogeneity|异质性]]导致在部分研究中未显现出关联 |
> | **教育项目与教学干预** | **$r = 0.20$** | $[0.10, 0.29]$ | $[-0.20, 0.54]$ | 干预整体效果优异，但教学法落地质量决定具体成败 |
> | **外认知心理倾向因素** | **$r = 0.14$** | $[0.06, 0.22]$ | $[-0.24, 0.49]$ | 动机与心境普遍支持创造力，但存在个体特质差异 |
> | **认知基础能力** | **$r = 0.12$** | $[0.04, 0.19]$ | $[-0.27, 0.47]$ | 智力起基础门槛作用，高分段关联呈现较大离散 |
> | **人口学与社会背景** | **$r = 0.07$** | $[-0.10, 0.25]$ | $[-0.38, 0.49]$ | 均值与预测区间均包含 0，证实创造潜能无特定人口偏向 |
