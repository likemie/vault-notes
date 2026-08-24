---
title: I-squared Statistic
aliases:
  - I² 统计量
  - I2 统计量
  - I-squared
  - 异质性百分比
  - Higgins I2
summary: "元分析中衡量跨研究总变异中由真实异质性而非抽样误差所解释比例的标准化相对指标，常用 25%、50%、75% 判定低、中、高度异质性"
type: concept
domain: "research-methodology"
related_count: 15
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - statistics/meta-analysis
  - heterogeneity
  - methodology
related_concepts:
  - "[[Heterogeneity]]"
  - "[[Effect Size]]"
  - "[[Sampling Error]]"
  - "[[Scale of Measurement]]"
  - "[[Study Population and Sample]]"
  - "[[Between-Study Variance]]"
  - "[[Prediction Interval]]"
  - "[[Research Utilization]]"
  - "[[Critical Thinking]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Cochran's Q Test]]"
  - "[[Meta-regression]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Higgins_2016_RE]]"
  - "[[Argument_Abrami_2015_RER]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17]]"
confidence: high
status: draft
created: 2026-08-25
updated: 2026-08-25
---

# I-squared Statistic

---

## 定义

> [!def] 核心定义
> I² 统计量（I-squared Statistic，亦称[[Heterogeneity|异质性]]百分比 / Higgins' I²）是由 Julian Higgins & Simon Thompson (2002) 提出并在 Higgins et al. (2003) 中确立规范的无量纲相对异质性指标。它衡量的是[[Meta-analysis|元分析]]中观察到的各初级研究[[Effect Size|效应量]]总变异中，**由跨研究的真实异质性（Between-study heterogeneity）而非偶然[[Sampling Error|抽样误差]]（Sampling error）所解释的方差百分比**。[[Argument_Higgins_2016_RE|(Higgins, 2016, p. 38)]]

> [!concept-lens] 概念透镜
> - **含义** 将观察到的总变异标准化为 $0\%–100\%$ 的百分比比率，直观反映研究间离散有多少比例属于“真实差异”。
> - **用途** 为读者和实践者提供一个直观、不受效应量[[Scale of Measurement|测量尺度]]影响的跨领域异质性严重程度参考标准。
> - **边界** $I^2$ 反映的是相对比例而非绝对变异幅度；初级[[Study Population and Sample|研究样本]]量越大，抽样误差越小，$I^2$ 会自然趋向膨胀，因此不能单纯依赖 $I^2$ 替代 [[Between-Study Variance|研究间方差]] $\tau^2$ 与 [[Prediction Interval|预测区间]]。

---

## 数学原理与计算公式

> [!formula-step] I² 计算公式与方差比率模型
> 基于 Cochran's [[Cochran's Q Test|Q 统计量]] 的经典计算公式为：
>
> $$I^2 = \max\left(0, \; \frac{Q - (k - 1)}{Q}\right) \times 100\%$$
>
> 其中：
> - $Q$ 为加权离差平方和统计量；
> - $k$ 为纳入研究数，$k - 1$ 为同质性假定下的期望离差。
>
> **方差分解等价表述**（Higgins & Thompson, 2002）：
> $$I^2 = \frac{\tau^2}{\tau^2 + s^2} \times 100\%$$
> 其中 $\tau^2$ 为 [[Between-Study Variance|研究间真实方差]]，$s^2$ 为各初级研究抽样方差的典型典型均值（Typical within-study variance）。

---

## 判定基准与等级划分

> [!tip] Higgins et al. (2003) 经验分级标准
> - **$I^2 = 0\%–25\%$（低度[[Heterogeneity|异质性]] / Low Heterogeneity）** 绝大部分变异由抽样随机性造成，各研究结果高度一致；
> - **$I^2 = 25\%–50\%$（中度异质性 / Moderate Heterogeneity）** 存在适度的跨研究实质性差异；
> - **$I^2 = 50\%–75\%$（高度异质性 / Substantial Heterogeneity）** 真实变异占主导地位，必须重点开展亚组分析或[[Meta-regression|元回归]]；
> - **$I^2 = 75\%–100\%$（极高度异质性 / Considerable Heterogeneity）** 结果极度离散，单纯汇报全局平均[[Effect Size|效应量]]可能具有误导性，需慎重探讨合成的合法性。

---

## 核心优势与常见误区

> [!feature] 核心优势
> - **无量纲通用性** 不依赖具体[[Research Utilization|研究使用]]的[[Scale of Measurement|测量量表]]（如百分制、5点量表、二分类比值比），可在不同学科和主题之间进行横向比较。
> - **克服 $k$ 敏感性** 与 [[Cochran's Q Test|Q 检验]] 极度依赖研究数量不同，$I^2$ 在纳入研究数量 $k$ 变化时保持相对稳健。

> [!warning] 关键误区与局限性（Borenstein et al., 2017; [[Argument_Higgins_2016_RE|Higgins, 2016]]）
> - **误区一：将 $I^2$ 等同于“绝对离散范围”** $I^2 = 90\%$ 仅说明总方差中 90% 来自真实差异，并不代表真实效应在数值上波动剧烈——若初级[[Study Population and Sample|研究样本]]量均极大（抽样方差 $s^2 \to 0$），即使真实效应仅在 $0.49–0.51$ 极窄范围内波动，$I^2$ 也会高达 $99\%$。
> - **误区二：脱离 $\tau^2$ 与[[Prediction Interval|预测区间]]做判断** 评估临床或教育实践中的干预风险时，必须同时汇报绝对尺度参数 $\tau^2$ 与能够反映个体情境效应分布的 95% 预测区间。

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Higgins_2016_RE|Higgins (2016)]] — 系统阐述 $I^2$ 统计量的提出背景、在证据本位实践中的应用及对传统检验的改进。
> - [[Argument_Abrami_2015_RER|Abrami et al. (2015)]] — 在 341 项[[Critical Thinking|批判性思维]]干预实证中系统报告组内 $I^2$（多数在 $60\%–75\%$ 之间）以论证混合效应调节分析的必要性。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen, Manion & Morrison (2011, Ch17)]] — 介绍[[Heterogeneity|异质性]]量化指标在教育[[Meta-analysis|元分析]]中的解读准则。
