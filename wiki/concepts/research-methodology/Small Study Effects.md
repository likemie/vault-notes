---
title: Small Study Effects
aliases:
  - 小研究效应
  - small-study effects
  - 小样本研究效应
  - small sample bias
summary: "指元分析中小样本研究系统性报告比大样本研究更大效应量的经验现象，源于发表偏倚、方法学质量差异与小样本过度拟合等多重偏倚机制。"
type: concept
domain: "research-methodology"
related_count: 12
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - field/research-methodology
  - topic/quantitative-methods
  - theme/meta-analysis
related_concepts:
  - "[[Publication Bias]]"
  - "[[Sampling Error]]"
  - "[[Standard Error]]"
  - "[[Heterogeneity]]"
  - "[[Effect Size]]"
  - "[[Prediction Interval]]"
related_methods:
  - "[[Multilevel Egger's Test]]"
  - "[[Robust Variance Estimation]]"
  - "[[Correlated and Hierarchical Effects Model]]"
  - "[[Meta-meta-analysis]]"
  - "[[Meta-analysis]]"
related_arguments:
  - "[[Argument_Runco_2026_CRJ]]"
confidence: medium
status: draft
created: 2026-08-24
updated: 2026-08-24
---

# Small Study Effects

---

## 定义

> [!def] 核心定义
> [[Small Study Effects|小研究效应]]（Small-Study Effects，亦称小样本研究效应）是指在[[Meta-analysis|元分析]]与[[Meta-meta-analysis|二阶元分析]]中观察到的一种经验现象：**较小样本量（即较大[[Standard Error|标准误]]）的研究倾向于系统性报告比大样本研究更大、更具统计显著性的[[Effect Size|效应量]]。**这一现象由 Sterne et al. (2000)、Sterne & Egger (2005) 以及 [[Argument_Runco_2026_CRJ|Runco et al. (2026, pp. 5–6)]] 等研究记录。小研究效应是造成漏斗图（Funnel Plot）不对称的根本物理原因，其来源不仅包括文献[[Publication Bias|发表偏倚]]（Publication Bias），还涵盖小样本研究方法学控制不严、干预实施强度差异以及特定亚组人群选择偏差。

> [!concept-lens] 概念透镜
> - **含义** 指向实证文献库中效应量大小与研究精度（标准误）之间存在的系统性虚假依赖关系。
> - **用途** 帮助研究者警惕元分析未校正前合并值的夸大风险，通过统计建模（如[[Multilevel Egger's Test|多水平艾格回归]]）分离出无偏的大样本真实效应基准。
> - **边界** 小研究效应是一种**经验现象（Phenomenon）**而非单一特定原因；漏斗图不对称不等于必定存在学术不端或有意隐瞒阴性结果。

> [!citation-card]- 关键表述
> 采用基于 RVE 的改进多水平艾格回归检验潜在发表偏倚并检验小研究效应……截距项统计显著（p = .002），表明存在小研究效应；经偏倚校正后的二阶效应量为 0.17。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, p. 6)]]
>
> *We adopted a modified multilevel Egger's regression with RVE to examine potential publication bias... The intercept, representing the bias-corrected second-order effect size, was statistically significant (r = .17, 95% CI [.11, .22]). The slope was also significant, F(1, 10.9) = 15.7, p = .002, indicating the presence of small-study effects.*

> [!boundary]- 概念边界
> - 不等于 [[Publication Bias|发表偏倚]] — 发表偏倚（未发表阴性结果）仅是导致小研究效应的主因之一；小研究中干预执行更密集、被试依从性更高或方法学质量偏低同样会产生小研究效应。
> - 不等于常规 [[Sampling Error|抽样误差]] — 抽样误差围绕真值对称震荡，期望值为 0；小研究效应是单向右偏（夸大）的系统性统计偏倚。

---

## 概念辨析

> [!contrast-table] 小研究效应 vs 发表偏倚 vs 方法学质量缺陷
> | 比较维度 | 小研究效应（Small-Study Effects） | 发表偏倚（Publication Bias） | 方法学质量缺陷（Methodological Quality Defect） |
> |---|---|---|---|
> | **性质定位** | **可观测的统计现象（效应量与标准误正相关）** | 导致现象产生的机制之一（基于 $p$ 值筛选发表） | 导致现象产生的机制之一（缺乏双盲、随机化不足） |
> | **表现形态** | 漏斗图底部散点向有利益偏向的一侧严重倾斜 | 漏斗图左下角（小样本非显著区）数据点大面积缺失 | 小样本研究中报告的效应量因执行松散而虚高 |
> | **检测与校正手段** | **艾格回归（Egger's Test）、多水平 RVE 截距模型** | 剪补法（Trim and Fill）、选择模型（Selection Models） | AMSTAR 质量评分分层、二阶元回归调节检验 |
> | **二阶元分析表现** | 显著存在（$F = 15.7, p = .002$），校正后为 $r = 0.17$ | 经全面灰色文献检索与博硕士论文纳入得到部分控制 | AMSTAR 高质量 vs 低质量调节不显著（$p = .34$） |

---

## 核心产生机制

> [!feature] 小研究效应的三大驱动机制
> - **选择性发表机制（Selection Bias / Publication Bias）** 小样本研究由于统计功效低，只有当效应量极大时才能达到统计显著门槛（$p < .05$）从而被期刊接收；较小效应的小样本研究沉没在“抽屉”中。
> - **研究质量与设计妥协（Methodological Quality Discrepancy）** 小规模探索性实验往往在随机分组、盲法评估与实验控制上弱于大规模多中心临床/教育追踪研究，容易产生方法学假阳性增益。
> - **真实干预强度差异（Clinical / Educational Heterogeneity）** 在小规模班级实验中，研究者或一线名师能够投入极高的个别化辅导精力（高保真度实施）；而在大规模推广时干预被稀释，导致大样本效应量自然回落。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, pp. 5–6)]]

> [!logic-map]- 小研究效应在漏斗图中的偏倚机制
> ```mermaid
> flowchart TD
>     A["实证研究开展"] --> B{"样本规模 (N) 与精度 (SE)"}
>     B -- 大样本 (SE 接近 0) --> C["统计功效充足<br/>无论效应大小均能发表<br/>真实效应基准收敛于 r ≈ 0.17"]
>     B -- 小样本 (SE 较大) --> D{"效应量是否足够大<br/>以达到 p < .05?"}
>     D -- 否 (效应微弱或为负) --> E["遭遇发表偏倚 / 抽屉效应 (未被发表)"]
>     D -- 是 (效应极大或偶发异常) --> F["成功发表并被元分析纳入"]
>     F --> G["造成漏斗图底部右倾<br/>引发小研究效应 (Small-Study Effects)"]
> ```

---

## 围绕概念形成的命题

### 命题一　小研究效应要求元分析研究必须超越简单加权平均并引入截距校正

> [!concept-lens] 复合偏倚与统计校正必要性
> 探讨为何在存在小研究效应时，即使是随机效应模型的逆方差加权平均值依然会高估总体真实效果。

> [!claim] Sterne & Egger (2005); Rodgers & Pustejovsky (2021)
> **加权均值的残余偏倚** 传统的逆方差加权虽然赋予大样本研究更高权重，但由于小样本研究数量往往占绝对多数，如果存在系统性小研究效应，加权汇总值仍会受到向右拉扯；必须通过将效应量对标准误进行回归，把回归方程外推至理论上无限大样本（$\operatorname{SE} \to 0$）处的截距项，方能获得真正的无偏效应基线。

---

### 命题二　多水平艾格回归截距检验确立了创造力全领域偏倚校正后的真实效应基准

> [!concept-lens] 二阶元分析中的小研究效应确证与校正
> 探讨在大规模二阶元分析中如何运用改进艾格回归消除文献依赖与小研究偏倚。

> [!claim] [[Argument_Runco_2026_CRJ|Runco et al. (2026)]]; Pustejovsky & Rodgers (2019)
> **二阶截距偏倚校正** 在对 52 项创造力一阶元分析（164 个效应量）的二阶综合中，多水平相关与层级效应模型配合稳健方差估计（CHE + RVE）检验显示，标准误斜率项高度显著（$F(1, 10.9) = 15.7, p = .002$），确证了创造力文献库中显著存在小研究效应；经截距外推校正后，创造力全领域的真实无偏二阶效应量确立为 **$r = 0.17$**（95% [[Confidence Interval|置信区间]] $[0.11, 0.22]$），为全领域各细分构念提供了可靠的参照原点。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, pp. 5–6)]]

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **复合偏倚识别** | 小研究效应源于发表偏倚、方法学妥协与真实异质性的复合作用 | 循证研究质量评估、系统综述检验 | Sterne & Egger (2005); Sterne et al. (2000) |
> | **多水平截距校正** | 借助多水平 RVE 艾格回归外推无偏截距，确立创造力二阶基准效应（$r = 0.17$） | 二阶元分析建模、发表偏倚敏感性校正 | [[Argument_Runco_2026_CRJ|Runco et al. (2026)]]; Rodgers & Pustejovsky (2021) |
