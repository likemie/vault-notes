---
title: Clustering Coefficient
aliases:
  - 集聚系数
  - 聚类系数
  - 聚集系数
summary: "复杂网络分析中量化节点局部连边紧密程度与三元互联倾向的核心拓扑度量；定义为某个节点的邻居节点之间实际存在的连边数占可能最大连边数的比例；在科学合著网络中实测值高达 0.1–0.3（比同阶随机网络高出几个数量级），刻画了学者倾向于在小圈子、研究团队与学术学派中形成高内聚协同的局域特征。"
type: concept
domain: "science-policy"
related_count: 7
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - theme/science-of-science
  - theme/network-science
  - theme/coauthorship
  - theme/graph-theory
related_concepts:
  - "[[Coauthorship Network]]"
  - "[[Giant Component]]"
  - "[[Erdős Number]]"
  - "[[Six Degrees of Separation]]"
related_theories:
  - "[[Small-World Collaboration Model]]"
related_methods:
  - "[[Network Analysis]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit04]]"
confidence: high
status: active
created: 2026-10-30
updated: 2026-10-30
---

---

> [!def] Clustering Coefficient
> 集聚系数（Clustering Coefficient，亦称聚类系数、聚集系数）指复杂网络中量化某个节点的相邻节点对之间也相互连接（形成三元闭包）的条件概率。在局部层面，节点 $i$ 的集聚系数 $C_i$ 定义为该节点所有相邻节点之间实际存在的连边数与理论上最大可能连边数之比；网络全局集聚系数为全网所有节点集聚系数的均值，是判定网络是否具备“小世界”局域高抱团特性的基准指标。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 105–106)]]

> [!concept-lens|notitle] 概念透镜
> - **含义** 刻画网络中“朋友的朋友也是朋友”或“伙伴的伙伴也在共同开展研究”的局域三元互联倾向。
> - **用途** 用于合著网络分析中识别局部学术学派、师承网络与合作圈子的内聚密度，并与全局最短路径结合评估小世界网络的创新效能。
> - **边界** 高集聚系数反映局域信任与协同成熟度，但过高的集聚度容易阻断外源异质知识的输入，诱发认知僵化与回音室效应。

> [!citation-card] 合著网络中远超随机基准的高集聚系数
> 在随机网络中，节点的邻居相互连接的概率与全网连边密度相当，数值趋近于零。然而在真实的科学家合著网络中，集聚系数高达 0.1 至 0.3，比同等规模随机网络高出几个数量级，清楚地揭示出科学共同体内部高度成簇、学派密集抱团的社会学特征。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 105–106)]]
>
> *In a random network, the clustering coefficient is near zero. Yet in real scientific collaboration networks, clustering coefficients are orders of magnitude higher, reflecting tightly knit local groups and cohesive intellectual circles.*

> [!boundary]- 概念边界
> - 不等于网络密度（Network Density）：网络密度衡量的是全网所有节点间实际边数与最大可能边数之比；集聚系数关注的是节点邻域内的局部子图三元互联密度。
> - 不等于度中心度（Degree Centrality）：度中心度关注的是节点直接拥有的科研伙伴总数，而集聚系数关注这些伙伴彼此之间是否认识并共同发表。

---

> [!contrast-table|notitle] 概念辨析
> | 维度 | 高集聚系数网络（High Clustering） | 随机拓扑网络（Random Network） | 星型放射网络（Star Network） |
> |------|-----------------------------------|-------------------------------|-----------------------------|
> | 三元连通结构 | 大量三元三角形态，伙伴彼此共同发文 | 连边纯随机生成，三元互联极其罕见 | 完全不存在三元连通，仅由中心对外放射 |
> | 典型数值 | 真实合著网络实测约为 $0.1$ 至 $0.3$ | 随规模衰减，$C \approx \langle k \rangle / N \to 0$ | $C = 0$（叶子节点互不相连） |
> | 学术生态 | 形成稳定的合作派系与师承共同体 | 毫无学术传承与师门体系的混沌碰撞 | 围绕单一权威导师运转、团队成员互不合作的小组 |
> | 创新特征 | 内部协同默契高，需警惕认知同质化 | 缺乏长期积累与学术信任，协同成本过高 | 极度依赖单一核心权威，抗风险与自组织能力差 |

---

> [!feature] 核心要素
> - **代数计算公式** 节点 $i$ 的局部集聚系数表达为：
>   $$C_i = \frac{2 e_i}{k_i (k_i - 1)}$$
>   其中 $k_i$ 为学者 $i$ 的合著伙伴数量（度数），$e_i$ 为该学者的 $k_i$ 位伙伴之间相互合著的实际连边数。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 105–106)]]
> - **显著超越随机图的数量级差距** 真实自然科学与社会科学合著网络的集聚系数通常在 0.10 至 0.30 之间，相比节点数相同且度分布相仿的随机零模型高出上千倍，表明科学合作具有强烈的局域三角自愈与三元组织动力学。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 106)]]
> - **小世界网络构建的两大支柱之一** 邓肯·瓦茨（Duncan Watts）与史蒂文·斯特罗加茨（Steven Strogatz）的小世界网络模型表明，“高集聚系数”与“短平均路径”的有机结合，使得网络既能维系局域深度知识积累，又能实现跨领域思想的超快速跳跃。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 105–107)]]

> [!logic-map]- 要素关系
> ```mermaid
> flowchart TD
>   A["学者开展学术合作署名"] --> B["合著者之间展开相互二次合作"]
>   B --> C["三元闭包形成 (Triadic Closure)"]
>   C --> D["高局部集聚系数 Ci = 2ei / [ki(ki-1)]"]
>   D --> E["真实合著网络实测 C ≈ 0.1 - 0.3"]
>   E --> F["相比同规模随机图高出数千倍"]
>   E --> G["学术小圈子与紧密师门学派凝结"]
>   G --> H["适度集聚保障协同信任与科研默契"]
>   G -.->|过度集聚| I["诱发认知僵化与回音室陷阱"]
> ```

---

> [!concept-proposition] 命题一｜合著网络的高集聚系数揭示学术协作具有强烈的局域内聚属性
> **探讨维度　学术合作的微观组织结构** 探讨科学家之间是随机碰撞合作还是在特定强关系小圈子中深度结网。

> [!claim] Wang, D. & Barabási, A.-L.
> **局域信任与三元闭包涌现** 科学合作网络的集聚系数较同等规模随机图高出数千倍；极高的高阶三元连通概率证实，学者优先在成熟的合作小团体与学术网络深耕，局域信任是维系复杂团队生产的社会资本基础。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 105–106)]]

---

> [!concept-proposition] 命题二｜适度的小世界集聚构成孵化突破性创新的最佳拓扑环境
> **探讨维度　网络嵌入性与团队创造力** 剖析局部紧密聚类与全局远距捷径对知识生产与创新产出的非线性影响。

> [!claim] Uzzi, B. & Spiro, J.
> **集聚度的倒 U 形效应** 百老汇演艺网络与学术合著网络的经验实测表明，当集聚系数维持适度水平（小世界参数居中）时，团队既拥有充足的内部默契，又未陷入封闭的回音室，最具几率产出突破性精品成果。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 106–107)]]

---

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **局域内聚性** | 衡量科学家合著网络三元闭包概率远超随机零模型的微观倾向 | 学术合著网络与师承团队分析 | Wang & Barabási |
> | **创新倒 U 形** | 适度集聚兼顾默契与异质思想输入，催生突破性创新 | 团队网络结构与创造力产出分析 | Uzzi & Spiro; Wang & Barabási |

---

> [!evidence-grid-a|notitle] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit04|Wang & Barabási (2021)]] — 第 10 章第 10.2 节测算合著网络集聚系数，探讨小世界拓扑与百老汇音乐剧倒 U 形创新机制。

---

> [!entry-map] 条目关联
>
> | 条目 | 类型 | 贡献 |
> |:-----|:-----|:-----|
> | [[Coauthorship Network]] | 概念 | 集聚系数度量所依托的科研合著者无向图载体。 |
> | [[Giant Component]] | 概念 | 与集聚系数共同构成小世界网络全局拓扑骨架。 |
> | [[Erdős Number]] | 概念 | 测度与核心枢纽拓扑跳数的互补距离指标。 |
> | [[Six Degrees of Separation]] | 概念 | 与高集聚系数并列作为小世界网络判定的两大核心准则。 |
> | [[Small-World Collaboration Model]] | 理论 | 将高集聚与短距离整合为团队合作动力学模型的理论框架。 |
> | [[Network Analysis]] | 方法 | 计算节点三元闭包与全网平均集聚系数的基础图论分析工具。 |
