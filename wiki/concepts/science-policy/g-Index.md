---
title: g-Index
aliases:
  - g指数
  - Egghe's g-index
  - 艾格指数
summary: "由 Leo Egghe (2006) 提出的文献计量评价指标，界定为学者至多有 g 项成果累计获得至少 g^2 次引用的最大整数；旨在修正 h 指数对极端突破性成果的统计钝感，赋予划时代重磅文献应有的长尾评价权重。"
type: concept
domain: "science-policy"
related_count: 6
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - theme/science-policy
  - theme/scientometrics
  - theme/research-evaluation
  - theme/scientific-career
related_concepts:
  - "[[h-Index]]"
  - "[[Scientific Productivity]]"
  - "[[Predictive Validity]]"
  - "[[Document]]"
related_theories: []
related_methods:
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit01]]"
confidence: high
status: draft
created: "2026-10-29"
updated: 2026-10-29
---

---

> [!def] g-Index
> 里奥·艾格（Leo Egghe, 2006）提出的文献计量指标。将学者所有论著按被引频次降序排列，**被引最高的 $g$ 项成果累计获引总数至少达到 $g^2$ 次的最大整数 $g$（$\sum_{i=1}^g c_i \ge g^2$）**。该指标专门用于补足 $h$ 指数对超级离群高被引突破成果的钝感缺陷。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]

> [!concept-lens] 概念透镜
> - **含义** 通过平方累积和测度学者核心代表作集群的极端影响力深度，属于二阶非线性文献计量评价工具。
> - **用途** 帮助科学计量学识别那些发表篇数偏少但单篇产出划时代突破的卓越学者，避免重磅成果在离散阈值截断中被抹平。
> - **边界** 仍受制于学科引文基准落差，不能脱离学科直接做绝对数值的跨领域比对。

> [!citation-card] 极端突破性成果的计量修正
> 该指标的核心优势在于其数值不会被孤立的偶发成功所绑架，但这同时也意味着它彻底忽略了研究者最具影响力的标志性工作。一旦单篇成果被引次数越过 $h$ 门槛，其后续超额贡献在 $h$ 指数中就完全不可见了。为此，学界提出了 $g$ 指数等一系列变体方案以弥补这一系统性偏差。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 25)]]
>
> *The main advantage of the h-index is that its value is not boosted by a single runaway success. Yet this also means that it neglects the most impactful work of a researcher. Indeed, once a paper’s citations get above h, its relative importance becomes invisible to the h-index. Many remedies have been proposed to correct for this, including the g-index.*

> [!boundary]- 概念边界
> - 不等于 [[h-Index]]：$h$ 指数要求前 $h$ 篇论著每篇至少获引 $h$ 次，对超出 $h$ 的超额引用完全脱敏；$g$ 指数采用前 $g$ 篇累计被引达 $g^2$ 次的标准，允许极高引用的超级单篇成果拉动整体指数上升。
> - 不适用于微观单篇评价：$g$ 指数依然是学者个人或科研团队整体生涯的代表作集总统计指标，不适用于评价单项论著的独立学术价值。

---

> [!contrast-table] 核心科研成果评价计量指标属性对比
> | 维度 | [[h-Index|h 指数]] | [[g-Index|g 指数]] | o 指数（Dorogovtsev & Mendes, 2015） |
> |---|---|---|---|
> | **数学形式** | $c_i \ge h$（针对第 $i$ 篇，单篇独立门槛） | $\sum_{i=1}^g c_i \ge g^2$（前 $g$ 篇累积总和门槛） | $o = \sqrt{c^* h}$（最高单篇被引 $c^*$ 与 $h$ 的几何均值） |
> | **统计灵敏度** | 对 $h$ 阈值之上的超额引用完全不敏感 | 对前列极端高被引单篇成果高度敏感 | 仅由最高单篇极值与核心成果规模共同决定 |
> | **典型适用画像** | 持续产出中等高被引成果的稳健多产学者 | 拥有颠覆性爆发成果的开拓型学者 | 兼具单篇重磅代表作与稳健底盘的领军学者 |

---

> [!feature] 核心要素
> - **平方累积阈值准则** 将学者的论著按被引频次自高向低排列后计算累积和，找到满足 $\sum_{i=1}^g c_i \ge g^2$ 的最大截断秩次 $g$。数学上必然恒满足 $g \ge h$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]
> - **长尾离群值的权重恢复** 彻底解决了爱因斯坦（Albert Einstein, $h=67$）或彼得·希格斯（Peter Higgs, $h=8$）这类单篇获引数千乃至数万次但篇数受限的奠基科学家被常规门槛严重低估的问题。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 18–19, 25)]]
> - **抗碎片化灌水稳健性** 保持了对低质量碎片化发文的抵御能力；若后续成果被引极低，新增发文并不能有效推高 $\sum c_i$ 使其跨越增长更快的 $g^2$ 门槛。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 25)]]

---

## 围绕概念形成的命题

### 命题一　g 指数通过引入平方累积被引结构恢复了科学史上划时代重大突破成果的评价权重

> [!concept-lens] 离群突破成果与科学评价的理论冲突
> 探讨科学史中由少数极端重磅发现推动学科范式转移的客观事实，与常规文献计量工具对离群值机械剔除之间的内在矛盾。

> [!claim] Egghe (2006)
> **突破性发现的权重修复** 科学发展史本质上由少数打破常规的突破性成果所定义。常规 $h$ 指数为了抑制虚胖而设定的硬性截断，无意中抹杀了重磅代表作最核心的知识溢出价值。$g$ 指数通过累积求和与二次方阈值匹配，允许超级顶尖成果的多余被引向次高引论著溢出，在兼顾学者发文稳健性的同时，给予划时代原创贡献以充分的制度度量支持。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]

---

### 命题二　评价体系若脱离学科引用密度与团队规模而单独依赖 g 指数仍会导致新的跨领域系统性失真

> [!concept-lens] 复合指标的领域生态与合作规模边界
> 考察二阶累积指标在面对不同学科天然引文规模以及超大型国际协作论著时的鲁棒性边界。

> [!claim] [[Argument_Wang_Barabasi_2021_Cambridge|Wang and Barabási (2021)]]
> **学科生态与协作偏误** 尽管 $g$ 指数有效补足了极端高被引的缺失，但其依旧建立在原始引用总和之上，并未化解分子生物学、高能物理与数学之间天然的引用量级鸿沟。此外，在拥有数百乃至数千名共同署名者的超大型科学工程中，单篇高引成果会被所有成员同等继承，直接导致全体合作研究成员 $g$ 指数同步非理性攀升。必须辅以学科归一化或署名贡献率拆分，方能实现公正同行比较。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]

---

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **突破权重修复** | 恢复超级离群高被引成果在评价体系中的核心地位 | 学术终身成就奖评选与顶尖领军人才代表作鉴定 | Egghe (2006) |
> | **跨领域偏误警示** | 累积求和结构无法自然消除学科天然落差与搭便车现象 | 跨学科科研基金分配与大型国际合作团队成员考核 | [[Argument_Wang_Barabasi_2021_Cambridge\|Wang and Barabási (2021)]] |

---

> [!dev-timeline] 概念演变
> - **2005 — h 指数确立基准** 希尔施提出 $h$ 指数，以双向门槛平衡数量与质量，迅速成为全球科研评价主流。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 17–20)]]
> - **2006 — g 指数正式提出** 里奥·艾格针对 $h$ 指数对超级爆款成果完全失明的缺陷，正式提出 $g$ 指数数学定义与证明。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]
> - **2015 — 极值互补指标涌现** 多罗戈夫采夫与门德斯（Dorogovtsev & Mendes, 2015）提出 $o$ 指数（$o = \sqrt{c^* h}$），进一步丰富了针对离群顶尖成果的评价工具箱。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]

---

> [!warning] 适用局限
> - 无法脱离学科基准进行横向直接比对，高能物理、生物化学领域学者的 $g$ 指数常态化显著高于纯数学或理论计算机领域。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]
> - 在存在千人署名的实验物理大团队中，单篇极端引用会被所有挂名成员同等享受，可能诱发更为隐蔽的搭便车效应。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 25)]]

---

> [!empirical-divider]

> [!ref-table]- 其他实证结果（无效应量）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | 变量或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Wang_Barabasi_2021_Cambridge_Unit01\|Wang & Barabási (2021)]] | 微软学术图谱全量物理学巨擘引文数据 | 典型代表性案例对比 | $h$ 指数与单篇极端最高引用的对比失真 | 爱因斯坦发表 248 篇论著，$h = 67$；希格斯发表 25 篇论著，$h = 8$ | 该书全量实证分析 | 证实基础 $h$ 阈值截断对产出篇数极少但具备划时代极高引突破学者的系统性失真 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit01|Wang & Barabási (2021)]] — 梳理文献计量学中修正 h 指数无视超级突破成果的代表性衍生指标，系统阐明 g 指数与 o 指数的数学原理与应用场景。
