---
title: Begg and Mazumdar Rank Correlation
aliases:
  - Begg and Mazumdar's Rank Correlation Test
  - Begg's Test
  - Begg-Mazumdar Test
  - 秩相关检验
  - Begg-Mazumdar 秩相关
summary: "由 Colin Begg 与 Madhuchhanda Mazumdar（1994）提出的一种用于检验元分析中发表偏倚的非参数统计方法。通过计算调整后的标准化效应量与各研究方差估计值之间的等级相关系数，判断是否存在小样本研究系统性报告更高效应量的漏斗图不对称现象。"
type: method
domain: research-methodology
method_type: quantitative
method_family: "quantitative"
method_related_count: 15
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - statistics/meta-analysis
  - statistics/publication-bias
  - field/research-methodology
related_concepts:
  - "[[Publication Bias]]"
  - "[[Small Study Effects]]"
  - "[[Effect Size]]"
  - "[[Standard Error]]"
  - "[[Study Population and Sample]]"
  - "[[Hypothesis]]"
  - "[[Epistemology]]"
  - "[[Critical Thinking]]"
  - "[[Problem-Based Learning]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Meta-meta-analysis]]"
  - "[[Trim and Fill Method]]"
  - "[[Fail-Safe N]]"
  - "[[Multilevel Egger's Test]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Erdem_2026_SHE]]"
confidence: high
status: draft
created: 2026-08-24
updated: 2026-08-24
---

# Begg and Mazumdar Rank Correlation

---

## 定义

> [!def] 方法定义
> Begg and Mazumdar Rank Correlation（Begg 与 Mazumdar 秩相关检验，常简称为 Begg's Test）是由统计学家 Colin Begg 与 Madhuchhanda Mazumdar 于 1994 年提出的一种用于检验[[Meta-analysis|元分析]]中[[Publication Bias|发表偏倚]]（及[[Small Study Effects|小研究效应]]）的经典非参数统计方法。该方法通过计算各独立研究的“标准化[[Effect Size|效应量]]（Standardized Effect Sizes）”与其“抽样方差（Sampling Variances）”之间的 **Kendall's tau（$\tau$）等级相关系数**；若相关显著（$p < .05$），表明样本量较小（方差较大）的研究系统性地报告了更大的效应量，即存在发表偏倚导致的漏斗图不对称。[[Argument_Erdem_2026_SHE|(Erdem et al., 2026, pp. 960–961)]]

> [!method-scope] 方法范围
> - **研究对象** 元分析中纳入的各独立研究效应量点估计值及其抽样方差/[[Standard Error|标准误]]。
> - **问题类型** 检验效应量大小是否与[[Study Population and Sample|研究样本]]量/估计精度存在单调相关，以识别选择性发表偏倚。
> - **分析单位** 包含 $k$ 个效应量的元分析或[[Meta-meta-analysis|二阶元分析]]数据集。
> - **输出形式** Kendall's tau 秩相关系数值、检验统计量 $Z$ 值与双尾显著性 $p$ 值。

> [!citation-card]- 关键定义
> Begg 秩相关检验通过检验标准化效应估计与对应抽样方差之间的 Kendall's tau 秩相关，提供了一种不受正态性[[Hypothesis|假设]]限制的发表偏倚非参数诊断指标（Begg & Mazumdar, 1994; Borenstein et al., 2021）。[[Argument_Erdem_2026_SHE|(Erdem et al., 2026, p. 960)]]
>
> *The Begg and Mazumdar rank correlation test examines the correlation between standardized effect sizes and their variances using Kendall's tau, serving as a nonparametric test for publication bias (Begg & Mazumdar, 1994).*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 基于非参数秩次原理，假定在无偏倚情况下[[Effect Size|效应量]]的大小与其方差应彼此独立。
> - **研究者角色** 评估证据库中是否存在由于非显著结果未发表而导致的小样本效应膨胀。
> - **有效性标准** 若 Kendall's $\tau$ 接近 0 且 $p > .05$，表明无显著等级相关，未提示[[Publication Bias|发表偏倚]]。
> - **不声称回答的问题** 与 Egger 检验相比在中小样本（$k < 25$）时统计功效（Statistical Power）相对较低；无法直接校正效应量点估计值。

> [!method-stack] 方法层级
> - **研究设计** [[Meta-analysis|元分析]]偏倚诊断检验
> - **数据输入** 各研究效应量 $y_i$ 与方差 $v_i$
> - **分析方法** Kendall's tau 秩相关、正态近似 $Z$ 检验
> - **辅助技术** 与 Egger 线性回归、[[Trim and Fill Method|剪补法]]、[[Fail-Safe N|失安全系数]] 交叉互补

---

## 计算规程与数学原理

> [!formula-step] 公式步骤　Begg 秩相关检验标准化与计算
> 1. **计算标准化[[Effect Size|效应量]]（Standardized Effect）**
>    $$y_i^* = \frac{y_i - \bar{y}_{\text{fixed}}}{\sqrt{v_i - \frac{1}{\sum w_i}}}$$
>    其中 $\bar{y}_{\text{fixed}}$ 为固定效应加权平均，$v_i$ 为研究 $i$ 的抽样方差。
> 2. **计算 Kendall's tau 秩相关**
>    $$\tau = \frac{P - Q}{\frac{1}{2} k (k - 1)}$$
>    其中 $P$ 为 $y_i^*$ 与 $v_i$ 秩次同序对数，$Q$ 为异序对数，$k$ 为纳入研究数量。
> 3. **计算大样本近似 $Z$ 检验**
>    $$Z = \frac{\tau}{\sqrt{\frac{2(2k + 5)}{9k(k - 1)}}}$$
>    依据标准正态分布计算双尾显著性 $p$ 值。

---

## 经典应用案例

> [!example] [[Argument_Erdem_2026_SHE|Erdem et al. (2026)]] 高等教育[[Critical Thinking|批判性思维]][[Meta-meta-analysis|二阶元分析]][[Publication Bias|发表偏倚]]互补诊断
> 在探讨[[Problem-Based Learning|问题本位学习]]对高等教育学生产出影响的二阶[[Meta-analysis|元分析]]中，作者采用了四重互补偏倚检验：
> - **Begg 秩相关结果** Kendall's $\tau = -0.01, Z = 0.12, p = .89$，未提示存在显著发表偏倚；
> - **Egger 回归结果** $t(45) = 5.53, p < .001$，提示可能存在轻微小研究效应；
> - **[[Trim and Fill Method|剪补法]]校正** 建议补入 6 个负向[[Effect Size|效应量]]，调整后效应量从 $ES = 0.68$ 微降至 $ES = 0.60$；
> - **结论研判** Begg 秩相关与剪补法互补证实，即使在最保守校正下，干预对批判性思维的促进效应依然高度显著稳健。[[Argument_Erdem_2026_SHE|(Erdem et al., 2026, pp. 960–961)]]

---

## 优缺点与与其他检验方法对比

> [!contrast-table] Begg 秩相关与 Egger 回归对比
> | 比较维度 | Begg 秩相关检验 (Begg & Mazumdar, 1994) | Egger 回归检验 ([[Multilevel Egger's Test|Egger et al., 1997]]) |
> |---|---|---|
> | 统计原理 | **非参数秩相关（基于等级次序 Kendall's tau）** | **参数线性回归**（精度加权残差回归） |
> | 正态性[[Hypothesis|假设]] | **无需**正态分布假设，对极端异常值不敏感 | 假设回归残差服从正态分布 |
> | 统计检验功效 | 在样本量较小（$k < 25$）或中等异质性时功效较低 | 检验功效通常显著高于 Begg 检验 |
> | 适用推荐 | 偏态严重、存在离群点或大样本[[Meta-analysis|元分析]] | 元分析标准常规报告（配合多水平扩展） |

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Erdem_2026_SHE|Erdem et al. (2026)]] — [[Meta-meta-analysis|二阶元分析]]，将 Begg 秩相关检验（$\tau = -0.01, p = .89$）与 Egger 回归及[[Trim and Fill Method|剪补法]]并用，系统评估高等教育中干预措施对[[Critical Thinking|批判性思维]]提升的证据稳健性。
