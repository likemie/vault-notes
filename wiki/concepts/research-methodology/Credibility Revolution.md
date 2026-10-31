---
title: Credibility Revolution
aliases:
  - 可信性革命
  - 可信度革命
  - 经验微观计量革命
summary: "经验微观计量经济学与实证社会科学由观察性关联描述转向外生因果识别的方法论转型，依托随机对照试验与准实验反事实设计消除不可观测混杂偏误"
type: concept
domain: "research-methodology"
related_count: 0
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - theme/research-methodology
  - theme/causal-inference
  - theme/econometrics
related_concepts: []
related_theories: []
related_methods: []
related_instruments: []
related_persons: []
related_facts: []
related_arguments: []
confidence: high
status: draft
created: 2026-10-31
updated: 2026-10-31
---

---

> [!def] Credibility Revolution
> 可信性革命（Credibility Revolution）是指自 20 世纪 80 年代末至 90 年代起，在微观计量经济学与实证社会科学领域兴起的一场以因果识别（Causal Identification）为核心的方法论转型（Angrist & Pischke, 2010）。该转型针对传统观察性研究依赖多元回归固定效应却无法有效控制不可观测混杂因素（如个人坚毅品质、机构潜在偏好）的缺陷，主张借助[[Randomised Controlled Trials|随机对照试验]]（RCT）与外生制度门槛激发的[[Quasi-Experimental Designs|准实验]]（如[[Regression Discontinuity Design|断点回归]]、双重差分等），在明确的反事实框架下识别干预的净因果效应（[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|Wang & Barabási, 2021, pp. 248–251]]）。这一范式大幅提升了实证研究的内部效度，但面临确定性与外部可推广性之间的内在张力。

> [!concept-lens|notitle] 概念透镜
> - **含义** 从依赖统计控制的观察性相关分析，转向依托外生随机变异建立因果推断的研究范式转变。
> - **用途** 为公共政策干预与科研资助评价提供严谨的反事实对照，避免将内生选择偏误误读为真实处理效果。
> - **边界** 因果识别设计往往依托局部边界外生冲击，估算的是局部平均处理效应（LATE）；其结论向更广泛异质总体的外推面临外部效度约束。

> [!citation-card] 可信性革命的识别策略与效度权衡
> 过去三十年中，微观经济学者发展了一系列经验技术，被称为可信性革命。这些方法依靠两项基本策略：其一是利用随机对照试验（RCT），通过随机分配确保干预组与对照组在基线完全同质，将试验后的组间差异唯一归因于干预本身；其二是利用自然实验或准实验，寻找随机发生的外生分界事件作为截断点，检验截断前后的变化。确定性伴随着代价：因果关系明确的问题往往覆盖较窄的议题范围，小问题可以确信回答，宏观重大问题则面临更高不确定性。[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|(Wang & Barabási, 2021, pp. 249–251)]]
>
> *Over the last three decades, micro-economists have developed a series of techniques that can provide fairly reliable answers to some empirical questions. These methods, collectively known as the credibility revolution, rely on two basic tricks. The first trick is utilizing a randomized controlled trial (RCT)... Find a randomly occurring event, use it as a cutoff, and examine what happens before and after... As such, RCTs and other causal identification methods highlight an essential tension between certainty and generalizability: Small, limited questions can be answered with confidence, but bigger questions are subject to much more uncertainty.*

> [!boundary]- 概念边界
> - 不等于常规多元线性回归分析 常规观察性回归仅能在模型中控制已记录的可观测变量；可信性革命强调必须依托外生分配或准实验截断，化解不可观测变量带来的内生性混淆。
> - 不等于全盘否定观察性研究 科学探索需要观察性研究与因果实验的共生生态。大规模观察数据擅长描摹系统全景宏观规律，因果识别技术深挖关键微观机制，二者相互支撑补充。

---

> [!contrast-table|notitle] 概念辨析
> | 维度 | 传统观察性控制研究 | 随机对照试验（RCT） | 准实验设计（QED） |
> |---|---|---|---|
> | **外生性来源** | 假设控制所有可观测变量后误差项外生 | 由研究者通过物理或算法随机化强制分配 | 现实中外生政策截断、行政划线或自然偶发事件 |
> | **混杂因素控制** | 仅能消除可观测变量，无法防范不可观测遗漏 | 理论上在组间平衡所有可观测与不可观测特征 | 在临界点或特定平行趋势假设下消除不可观测偏误 |
> | **因果效应性质** | 条件相关系数，易受遗漏变量偏差污染 | 总体平均处理效应（ATE）或意向治疗效应（ITT） | 断点附近的局部平均处理效应（LATE） |
> | **适用边界** | 样本易获取，涵盖范围广，但因果推断可信度弱 | 成本高昂且面临伦理法律限制，适用题域窄 | 依赖特定制度截断的存在，外部推广需审慎 |

---

> [!feature] 核心要素
> - **克服不可观测变量困境** 打破常规回归必须假定“遗漏变量无关”的脆弱假设，通过设计识别机制排除个体坚毅、隐性动机等不可测因素的干扰（[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|Wang & Barabási, 2021, pp. 248–249]]）。
> - **双轨因果识别工具箱** 整合前瞻干预型随机对照试验（以微观干预为主）与回顾型外生政策截断准实验，形成多元互补的因果验证路径（[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|Wang & Barabási, 2021, pp. 249–250]]）。
> - **确定性与可推广性的张力** 因果识别的高确定性建立在严格受限的样本与局部情境之上，局域因果效应无法直接外推至不同制度或人口学背景（[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|Wang & Barabási, 2021, pp. 250–251]]）。
> - **观察与实验的生态共生** 宏观系统性社会议题（如全球气候治理或全学科科技体制演进）无法完全套用微观实验工具，需要观察性建模与实验识别紧密结合（[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|Wang & Barabási, 2021, p. 251]]）。

> [!logic-map]- 可信性革命因果识别范式
> ```mermaid
> flowchart LR
>     A["传统观察性研究<br>多元回归控制可测变量"] --> B["不可观测变量混淆<br>遗漏特征导致伪相关"]
>     B --> C["可信性革命方法论转型"]
>     C --> D["策略一：随机对照试验（RCT）<br>人为随机化平衡组间潜质"]
>     C --> E["策略二：准实验与自然实验<br>利用行政断点构建外生反事实"]
>     D & E --> F["严格因果识别判定<br>高内部效度与确凿因果结论"]
>     F --> G["核心效度张力权衡<br>局部确定性 vs 全局推广性"]
>     G --> H["构建观察与实验共生的科学学生态"]
> ```

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit11|Wang & Barabási (2021)]] — 阐述微观计量经济学可信性革命对科学学研究范式的深刻影响，梳理随机对照试验与准实验断点反事实两大识别策略，剖析因果确定性与外部可推广性之间的内在张力（pp. 248–251）。
