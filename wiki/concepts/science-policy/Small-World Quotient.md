---
title: Small-World Quotient
aliases:
  - 小世界商数
  - 网络小世界参数
  - 小世界参数
  - 小世界指数
  - Small-Worldness
  - Small-World Parameter
summary: "在复杂网络分析与团队科学中度量网络小世界拓扑强度的综合标准化指标；通过将实际网络的聚集系数与特征路径长度相对于同等规模与度分布的随机网络比值进行归一化测算；实证表明协作网络的小世界参数与团队创造力及创新绩效呈现倒 U 形非线性关联，适度取值最能平衡局域沟通默契与外部异质信息流通。"
type: concept
domain: "science-policy"
related_count: 17
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - theme/science-of-science
  - theme/team-science
  - theme/complex-networks
  - concept/network-metric
related_concepts:
  - "[[Team Science]]"
  - "[[Creativity]]"
  - "[[Coauthorship Network]]"
  - "[[Innovation Ecosystem]]"
  - "[[Clustering Coefficient]]"
  - "[[Six Degrees of Separation]]"
  - "[[Big Science]]"
  - "[[Operationalization]]"
  - "[[Variable]]"
  - "[[Dependent Variable]]"
  - "[[Construct]]"
related_theories:
  - "[[Small-World Collaboration Model]]"
related_methods:
  - "[[Network Analysis]]"
related_instruments: []
related_persons:
  - "[[Brian Uzzi]]"
  - "[[Dashun Wang]]"
  - "[[Albert-László Barabási]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit04]]"
confidence: high
status: active
created: "2026-10-30"
updated: 2026-10-30
---

---

> [!def] Small-World Quotient
> 小世界商数（Small-World Quotient，常记作 $W$ 或 $Q$ / Small-Worldness）指度量复杂网络相对于同等规模与度序列的随机网络展现小世界拓扑（高局域集聚与短全局平均路径长度并存）程度的标准化网络参数。该指标由[[Brian Uzzi|布赖恩·乌齐]]（Brian Uzzi）与斯皮罗（Jarrett Spiro, 2005）引入[[Team Science|团队科学]]与组织社会学，实证确立了网络小世界参数与团队[[Creativity|创造力]]之间的倒 U 形非线性规律。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 107–108)]]

> [!concept-lens|notitle] 概念透镜
> - **含义** 刻画网络在微观局域紧密性（高集聚）与宏观全局连通性（短路径）之间拓扑张力强度的综合指标。
> - **用途** 帮助研究者克服单维度集聚或路径长度度量的不足，定量判读整个产业或跨学科[[Coauthorship Network|合著网络]]处于割裂大世界、适度小世界还是过度纠缠回音室的宏观[[Innovation Ecosystem|创新生态]]位。
> - **边界** 适用于具有稳定网络边界的全景协作拓扑；不适用于未连通子图过多、边界开放未定义或样本严重抽样有偏的局部零散数据。

> [!citation-card|notitle] 乌齐与斯皮罗论网络小世界参数与团队绩效
> 百老汇艺术家网络小世界效应示意。参数 $W$ 量化网络的小世界特性。低 $W$ 时团队之间连接稀疏割裂；随 $W$ 增加，团队间连线增多促成拓扑凝聚；在中等 $W$ 水平下，小世界网络提供最佳的连通度与凝聚力平衡；过高 $W$ 造成认知僵化与回音室。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 108)]]
>
> *Broadway artists' small-world effect. The parameter W quantifies the network's small-world properties. At low W, links between teams are sparse and isolated; as W increases, cohesion grows; at intermediate W, the network balances connectivity and cohesive trust; excessive W leads to cognitive echo chambers.*

> [!boundary]- 概念边界
> - 不等于 [[Clustering Coefficient]] — 聚集系数仅测度局域邻居节点间三角形抱团程度，缺乏与全局捷径及随机基线的标准化比对。
> - 不等于 [[Six Degrees of Separation]] — 六度分隔侧重描述全网平均分离步数的极短现象，无法单独体现局域密集群聚与同质化回音室特征。

---

> [!contrast-table|notitle] 概念辨析
> | 维度 | 小世界商数（Small-World Quotient, $W$） | 聚集系数（[[Clustering Coefficient]]） | 特征路径长度（Average Path Length） |
> |---|---|---|---|
> | **测度对象** | 全网局域群聚与全局短距并存的综合小世界强度 | 节点邻居之间彼此直接连通的概率与密度 | 网络中任意两点间测地线距离的全局算术平均 |
> | **基准依赖** | 依赖同等节点与度分布的随机网络（Random Graph）基准 | 无需随机图基准，直接基于三角关系计算 | 无需随机图基准，直接基于拓扑最短路径计算 |
> | **理论功能** | 判读团队协作网络是否处于激发创造力的最优创新区间 | 刻画局域社群的信任基础、信息冗余与社会资本 | 刻画异质信息穿越全局网络所需的传播摩擦与步数 |

---

> [!feature] 核心要素
> - **数学定义与随机图标准化** 小世界商数通过实际网络集聚系数与随机图比值除以实际路径长度与随机图比值进行标准化：
>   $$W = \frac{C / C_{\text{rand}}}{L / L_{\text{rand}}}$$
>   当网络具备真实小世界特性时，$C \gg C_{\text{rand}}$ 且 $L \approx L_{\text{rand}}$，故 $W > 1$。
> - **低小世界参数的拓扑割裂** 当 $W$ 极低时，网络呈现传统大世界状态，各个团队彼此孤立，外部异质信息流通受阻，团队创意表现普遍低迷。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 107–108)]]
> - **高小世界参数的认知回音室** 当 $W$ 极高时，所有团队深度卷入过度稠密小圈子，认知高度同质化并排斥非常规异常观点，压制颠覆性创新并引发群体盲思。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 108)]]

> [!logic-map]- 要素关系
> ```mermaid
> flowchart LR
>     A["实际网络聚集系数 C / 随机图 C_rand"] --> W["小世界商数 W = (C/C_rand) / (L/L_rand)"]
>     B["实际网络平均路径 L / 随机图 L_rand"] --> W
>     W --> C["低 W: 大世界割裂 (信息孤岛)"]
>     W --> D["中等 W: 适度小世界 (倒 U 形峰值)"]
>     W --> E["高 W: 认知回音室 (群体盲思)"]
>     D --> F["最佳团队创造力与创新突破"]
> ```

---

## 围绕概念形成的命题

---

> [!concept-proposition] 命题一｜协作网络小世界参数与团队绩效呈现倒 U 形非线性规律
> **探讨维度　宏观网络拓扑对微观团队创新的非线性调控** 检验网络连通度与凝聚力对团队[[Creativity|创造力]]的复杂非线性作用。

> [!claim] [[Brian Uzzi|Uzzi, B.]] & Spiro, J.
> **倒 U 形最优小世界区间** 分析百老汇音乐剧创作团队与跨学科[[Coauthorship Network|科学合著网络]]证实，小世界商数 $W$ 与团队商业成功及原创评分呈现显著倒 U 形关系；适度 $W$ 水平最能兼顾团队内部信任默契与跨界异质知识输入。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 107–108)]]

---

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **倒 U 形非线性机制** | 协作网络小世界参数存在激发团队创新的最优中等阈值 | 创意产业管理、跨学科团队组建与[[Big Science\|大科学]]攻关 | Uzzi and Spiro (2005); [[Argument_Wang_Barabasi_2021_Cambridge_Unit04\|Wang and Barabási (2021)]] |

---

> [!dev-timeline] 概念演变
> - **1998 — 小世界网络数理模型** 邓肯·瓦茨（Duncan Watts）与史蒂文·斯特罗加茨（Steven Strogatz）形式化高聚类与短路径并存的小世界网络模型。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 106–107)]]
> - **2005 — [[Team Science|团队科学]]小世界商数参数化** 布赖恩·乌齐（Brian Uzzi）与斯皮罗将小世界商数 $W$ [[Operationalization|操作化]]为测度团队合作网络拓扑的指标，并实证发现倒 U 形创造力规律。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 107–108)]]
> - **2021 — 科学学框架体系确立** [[Dashun Wang|王大顺]]与[[Albert-László Barabási|巴拉巴西]]在《科学学的科学》中系统阐述合著网络小世界商数 $W$ 的拓扑演进与团队创新机制。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 107–108)]]

---

> [!tension|notitle] 核心张力
> - **局域信任凝聚派（高集聚）** 强调熟人网络与高重复合作有助于建立稳固信任与默契，降低复杂协作沟通摩擦。
> - **跨界异质捷径派（短路径）** 强调必须依赖跨越圈子的弱连接与异质人员输入，避免网络退化为认知回音室。

---

> [!entry-map] 条目关联
>
> | 条目 | 类型 | 贡献 |
> |:-----|:-----|:-----|
> | [[Small-World Collaboration Model]] | 理论 | 将小世界商数与团队创新机制结合的核心理论模型。 |
> | [[Clustering Coefficient]] | 概念 | 构成小世界商数分子端局域紧密程度的度量指标。 |
> | [[Six Degrees of Separation]] | 概念 | 构成小世界商数分母端全局捷径与短路径特性的物理现象。 |
> | [[Coauthorship Network]] | 概念 | 小世界商数在学术生产中的核心经验分析对象。 |
> | [[Creativity]] | 概念 | 小世界商数作为外生拓扑调控[[Variable\|变量]]影响的最终[[Dependent Variable\|因变量]][[Construct\|构念]]。 |
> | [[Network Analysis]] | 方法 | 测算小世界商数与构建随机网络基线的图论分析方法。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit04|Wang and Barabási (2021)]] — 第 10 章第 10.2 节依托百老汇音乐剧与跨学科科研合著网络大数据，系统解析小世界商数 $W$ 的参数定义及倒 U 形团队创造力规律。
