---
title: Fail-Safe N
aliases:
  - "失安全系数"
  - "失安全N"
  - "Rosenthal's Fail-Safe N"
  - "经典失安全数"
  - "Fail-Safe Number"
summary: "由 Robert Rosenthal（1979）提出的经典发表偏倚敏感性分析方法。通过计算将元分析汇总效应量拉低至统计不显著水平所需的无效应（零效应）未发表研究数量，评估元分析结论对抗抽屉文件效应（File Drawer Effect）的稳健性。"
type: method
domain: "research-methodology"
method_type: quantitative
method_family: "quantitative"
method_related_count: 16
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
tags:
  - "method/quantitative"
  - "statistics/meta-analysis"
  - "statistics/publication-bias"
  - "field/research-methodology"
related_concepts:
  - "[[Publication Bias]]"
  - "[[Effect Size]]"
  - "[[Document]]"
  - "[[Counterfactual]]"
  - "[[Hypothesis]]"
  - "[[Epistemology]]"
  - "[[Funnel Plot]]"
  - "[[Cooperative Learning]]"
  - "[[Confidence Interval]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Meta-meta-analysis]]"
  - "[[Trim and Fill Method]]"
  - "[[Multilevel Egger's Test]]"
  - "[[PRISMA]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Gungor_2026_CP]]"
  - "[[Argument_Liu_2026_CHBR]]"
confidence: high
status: draft
created: 2026-08-24
updated: 2026-08-25
---

# Fail-Safe N

---

## 定义

> [!def] 方法定义
> Fail-Safe N（失安全系数 / 失安全数，又称 Rosenthal's Fail-Safe N）是由心理统计学家 Robert Rosenthal 于 1979 年提出的一种用于评估[[Meta-analysis|元分析]]中[[Publication Bias|发表偏倚]]（抽屉文件问题，File Drawer Problem）严重程度的经典敏感性分析方法。该方法通过计算在现有纳入研究的基础上，还需要多少项[[Effect Size|效应量]]为零（$ES = 0$）的未发表潜在研究才能将当前显著的汇总效应量拉低至无统计学显著性（即 $p > .05$），以定量测度元分析结论的抗偏倚稳健度。[[Argument_Gungor_2026_CP|(Güngör et al., 2026, pp. 6–8)]]

> [!method-scope] 方法范围
> - **研究对象** 元分析中已纳入的 $k$ 项独立实证研究的检验统计量（$Z$ 值）或平均效应量及其方差。
> - **问题类型** 评估元分析汇总效应量对未发表阴性[[Document|文献]]潜在威胁的抵抗力与稳健性边界。
> - **分析单位** 元分析数据集（一阶元分析池或[[Meta-meta-analysis|二阶元分析]]汇总集）。
> - **输出形式** 理论所需的临界文献数量 $N_{\text{fs}}$（整型数值）及经验安全门槛（$5k + 10$ 准则）。

> [!citation-card]- 关键定义
> 经典失安全数通过构建极端[[Counterfactual|反事实]][[Hypothesis|假设]]，测算抵消当前显著发现所需的零效应隐藏研究规模；当失安全数远大于经验安全门槛（$N_{\text{fs}} \gg 5k + 10$）时，表明该元分析结论受发表偏倚逆转的概率极低（Rosenthal, 1979; Borenstein et al., 2021）。[[Argument_Gungor_2026_CP|(Güngör et al., 2026, p. 8)]]
>
> *The classic fail-safe N represents the number of non-significant (null) studies that would have to be added to the meta-analysis to reduce the overall effect to a non-significant level (Rosenthal, 1979).*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 基于频数统计学[[Hypothesis|假设]]检验框架，将[[Publication Bias|发表偏倚]]建模为未发表阴性研究的“抽屉堆积”。
> - **研究者角色** 通过设定临界显著性水平（$\alpha = .05$），对潜在缺失[[Document|文献]]的极端情形进行逆向推导。
> - **有效性标准** 若计算得出的 $N_{\text{fs}} > 5k + 10$（Rosenthal 准则），则判定结论具备高度稳健性。
> - **不声称回答的问题** 不能识别[[Funnel Plot|漏斗图]]不对称的具体机制，也不能直接修正有偏的[[Effect Size|效应量]]点估计值。

> [!method-stack] 方法层级
> - **研究设计** [[Meta-analysis|元分析]]偏倚敏感性分析
> - **数据输入** 各独立研究的 $Z$ 统计量或标准化均值差
> - **分析方法** 经典 Rosenthal 公式法、Orwin 效应量基准失安全法
> - **辅助技术** 与[[Trim and Fill Method|剪补法]]、Egger 回归截距检验协同使用

---

## 研究程序与数学原理

> [!formula-step] 公式步骤　Rosenthal 经典失安全数计算公式
> $$N_{\text{fs}} = \frac{\left(\sum_{i=1}^k Z_i\right)^2}{2.706} - k$$
>
> **这个公式在做什么**
> 1. $\sum Z_i$ 为纳入的 $k$ 项研究的标准正态 $Z$ 值代数和；
> 2. 常数 $2.706 = 1.645^2$（对应单尾显著性水平 $\alpha = .05$ 的临界临界值平方）；
> 3. $N_{\text{fs}}$ 即为将总体 $Z$ 分数拉低至 $1.645$ 以下所必需的 $Z = 0$ 的隐藏研究数量。

> [!tip] Rosenthal 经验判定门槛（$5k + 10$ 准则）
> - **安全标准** 若 $N_{\text{fs}} > 5k + 10$，表明抽屉中需要存在的未发表阴性研究数量远超合理预期，[[Publication Bias|发表偏倚]]极难颠覆当前结论。
> - **应用案例**在 Güngör et al. (2026) [[Cooperative Learning|合作学习]][[Meta-meta-analysis|二阶元分析]]中，纳入 $k = 23$ 个[[Effect Size|效应量]]，计算所得经典失安全系数高达 **$N_{\text{fs}} = 4954$**，远超安全门槛（$5 \times 23 + 10 = 125$），确凿排除了发表偏倚对二阶中等促进效应（$ES = 0.71$）的潜在干扰。[[Argument_Gungor_2026_CP|(Güngör et al., 2026, p. 8)]]

---

## 优缺点与方法局限

> [!contrast-table] 经典失安全数的优势与局限
> | 维度 | 经典失安全数 (Rosenthal Fail-Safe N) | 现代偏倚校正法 ([[Trim and Fill Method\|剪补法]] / [[Multilevel Egger's Test\|Egger检验]]) |
> |---|---|---|
> | 直观性 | 极高，以“缺失研究篇数”输出直观常识指标 | 较低，输出漏斗图、拟合截距或虚拟填补[[Effect Size\|效应量]] |
> | [[Hypothesis\|假设]]现实性 | 极差（假定所有未发表[[Document\|文献]]效应量严格等于 0） | 较好（基于[[Funnel Plot\|漏斗图]]不对称形态建模） |
> | 效应量校正 | **无法校正效应量点估计**，仅提供假设检验门槛 | 能够提供**偏倚校正后的真实效应量**点估计与[[Confidence Interval\|置信区间]] |
> | 现代定位 | 仅作为辅助性参考与极端情境压力测试 | 循证研究与 [[PRISMA]] 推荐的标准报告工具 |

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Liu_2026_CHBR|Liu et al. (2026)]] — 在 AI 代理促进 K-12 认知表现的[[Meta-analysis|元分析]]中，综合运用经典失安全数（$N_{\text{fs}} = 378$，大于 $5k + 10 = 180$ 门槛）与 Orwin 失安全数（需 $2{,}876$ 篇未发表零效应研究才能将 $g = 0.404$ 拉低至 $0.01$），系统确立了汇总[[Effect Size|效应量]]的抗偏倚稳健度。
> - [[Argument_Gungor_2026_CP|Güngör et al. (2026)]] — 在[[Meta-meta-analysis|二阶元分析]]中综合运用经典失安全系数（$N_{\text{fs}} = 4954$）、Egger 回归截距检验与[[Trim and Fill Method|剪补法]]，全面证实[[Cooperative Learning|合作学习]]宏观干预效应的稳健性。
