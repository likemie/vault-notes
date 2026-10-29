---
title: Relative Team Impact
aliases:
  - 相对团队影响力
  - RTI
summary: "由 Stefan Wuchty, Benjamin F. Jones 与 Brian Uzzi (2007) 提出的文献计量学指标；通过计算特定领域和年份内团队合作成果与单人成果的平均被引量比值（RTI），量化评估团队科研模式相对于个体科研模式的被引优势。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 7
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/indicator
  - theme/science-of-science
  - theme/team-science
  - bibliometrics
related_concepts:
  - "[[Team Science]]"
  - "[[Scientific Productivity]]"
related_theories:
  - "[[Burden of Knowledge]]"
related_methods:
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[Brian Uzzi]]"
  - "[[Benjamin F. Jones]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit04]]"
confidence: high
status: active
created: "2026-10-30"
updated: 2026-10-30
---

---

> [!def] Relative Team Impact
> 相对团队影响力（Relative Team Impact, RTI）是测度团队科研成果相对于单人独立成果被引优势的量化比值指标。其计算规则为：在给定的学科领域与发表年份内，将团队署名论著的算术平均被引频次除以单人署名论著的算术平均被引频次，输出一个无量纲的相对比值。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 86)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 团队合作生产模式相对于个体独立研究模式的学术影响力增益。
> - **问题类型** 比较、评价、描述与跨时序趋势测度。
> - **分析单位** 学科领域年级切片、机构或技术分类集合。
> - **输入数据** 论文或专利的作者署名人数以及对应的时间窗被引频次（剔除自引后可作为稳健性检验）。
> - **输出形式** 正实数比值（RTI）。当 $\text{RTI} = 1$ 时表示团队与单人成果平均影响力持平；$\text{RTI} > 1$ 表示团队成果具有超额影响力。

> [!citation-card] 相对团队影响力的基准定义
> 相对团队影响力（RTI）代表团队署名成果所获得的平均被引次数除以同领域单人署名成果获得的平均被引次数。比值为 1 意味着团队与单人成果具有相当的影响力。折线呈现给定年份整个领域的算术平均 RTI。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 86)]]
>
> *The relative team impact (RTI) represents the mean number of citations received by team-authored work divided by the mean number of citations received by solo-authored work in the same field. A ratio of 1 implies that team- and solo-authored work have comparable impact. The lines present the arithmetic average of RTI in a given year for the entire field.*

---

> [!method-position] 方法定位
> - **构念效度** RTI 直接反映文献计量学意义上的均值引文溢价，能够敏感捕捉宏观学术生产体系中知识组合方式对学术反响的结构性影响。
> - **研究者判断** 跨学科引文尺度的归一化基准、统计分析切片的时间窗口，以及是否剔除作者自引。
> - **有效性标准** 在剔除全部作者自引后，RTI 大于 1 的结构性优势依然保持不变，排除了多作者自引膨胀的机械性干扰。
> - **不声称回答的问题** 该指标测度的是宏观聚合层面的平均引文差异，并不直接衡量单篇具体论文的科学真理性或个别团队内部的协作质量。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis|文献计量学分析]]（Bibliometric Analysis）。
> - **前置步骤** 署名形态分类（单人 vs 多人合作）、学科分类匹配、引文窗口统计与自引清洗。
> - **变体与扩展** 极端引文倍率比值（如在被引达到 1,000 次以上的顶尖层级中团队成果相对单人成果的入选几率比）。

> [!dev-timeline] 方法演化
> - **2007 — 指标创立** 斯特凡·乌赫蒂（Stefan Wuchty）、本杰明·F·琼斯（Benjamin F. Jones）与布赖恩·乌齐（Brian Uzzi）在发表于《科学》（*Science*）的里程碑论文中建立 RTI 指标，测算 1,990 万篇科研论文与 210 万件专利，证实所有学科门类的团队论著均呈现出持续高于单人论著的引文优势。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 85–86)]]

---

> [!formula-step] 计算步骤与判定矩阵
>
> 相对团队影响力的标准计算公式为：
>
> $$\text{RTI}_{f, t} = \frac{\bar{c}_{\text{team}, f, t}}{\bar{c}_{\text{solo}, f, t}} = \frac{\frac{1}{N_{\text{team}, f, t}} \sum_{i \in \text{team}} c_i}{\frac{1}{N_{\text{solo}, f, t}} \sum_{j \in \text{solo}} c_j}$$
>
> 1. **样本分组** 将特定学科领域 $f$ 在 $t$ 年发表的全部成果按作者人数划分为单人集（$\text{solo}$，作者数等于 1）与团队集（$\text{team}$，作者数大于等于 2）。
> 2. **引文均值计算** 分别统计两组在统计窗口期内累积获得的被引频次算术均值。
> 3. **计算比值** 将团队均值除以单人均值求得 $\text{RTI}_{f, t}$。
> 4. **稳健性检验** 扣除每篇论文中全部署名作者的自引后重复上述计算，检验引文溢价是否依然成立。

---

> [!method-fit] 适用判断
> - **适合使用** 评估不同科研组织形式、学科门类、资助模式对学术成果影响力的宏观作用机制。
> - **谨慎使用** 合作模式极少、绝大多数成果为单人写作的人文学科（如部分哲学与文学研究细分领域），单人与团队样本量极度失衡可能放大统计波动。
> - **不适合使用** 微观层面上单一团队或单篇论文的横向绩效定级考核。

---

> [!method-limits] 方法局限与反思
> - **厚尾分布均值敏感性** 引文分布呈现高度偏态与重尾特征，算术均值容易受到极少数超高引论著的拉动。
> - **团队规模混淆** RTI 通常将所有二人及以上成果归入团队类，掩盖了大团队与小团队在颠覆性与渐进式创新上的内部异质性。
> - **应对策略** 结合分位数回归、引入极端高引成果（如 Top 1% 或被引破千篇目）的几率比分析，并细分团队规模梯度。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[Team Science]] | 概念 | RTI 测度对象的核心概念载体，量化展示团队科学相对于单人研究的影响力溢价。 |
> | [[Burden of Knowledge]] | 理论 | 为团队科学崛起与 RTI 持续大于 1 提供认知与分工机制层面的理论解释。 |
> | [[Bibliometric Analysis]] | 方法 | RTI 指标依托的上位文献计量学分析范式。 |
> | [[Brian Uzzi]] | 人物 | RTI 指标的共同提出者与倡导者。 |
> | [[Benjamin F. Jones]] | 人物 | RTI 指标的共同提出者与科学学经济学家。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit04|Wang & Barabási (2021)]] — 运用 RTI 评估 50 年间近 2,000 万篇论文与 210 万件专利，证实团队论著平均引文全面超越单人成果，且在科学与工程领域斩获千次以上引用的概率是单人的 6.3 倍。

## 使用此方法的研究

- [[Argument_Wang_Barabasi_2021_Cambridge_Unit04]]
