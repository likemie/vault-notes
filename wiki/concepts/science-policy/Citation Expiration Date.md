---
title: Citation Expiration Date
aliases:
  - 引文失效期
  - 文献失效期
  - 学术影响力失效期
  - 引文饱和稳态
  - Expiration Date
summary: "指学术文献在历经发表初期两到三年的跳跃衰减后，增量被引速率趋近于零、累积引文分布趋向确定性饱和稳态的历史时间截断界限。斯特林格等通过对专门期刊1991年与1993年论著队列的15年追踪实证证实，文献在经历特定年限后完全停止吸纳新引文，引文时序分布趋于完全等同；该构念确立了文献学术影响力的有限生命周期边界（Stringer et al., 2008; Wang & Barabási, 2021）。"
type: concept
domain: "science-policy"
related_count: 11
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - theme/science-of-science
  - theme/citation-dynamics
  - theme/scientific-impact
  - theme/scientometrics
related_concepts:
  - "[[Citation Aging]]"
  - "[[Ultimate Impact]]"
  - "[[Citation Distribution]]"
  - "[[Citation Disparity]]"
  - "[[Variable]]"
related_theories:
  - "[[WSB Model]]"
related_methods:
  - "[[Journal Impact Factor]]"
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[Dashun Wang]]"
  - "[[Albert-László Barabási]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit09]]"
confidence: high
status: active
created: "2026-11-02"
updated: 2026-11-02
---

---

> [!def] Citation Expiration Date
> 引文失效期（Citation Expiration Date，或称文献失效期 / 影响力有效期限）是指学术成果在发表后经历初期的跳跃式爬坡达峰与随后的指数衰减，最终在特定时间节点停止吸纳新增被引、其累积引文时序分布完全进入稳态饱和的客观时间界限。该构念由迈克尔·斯特林格（Michael J. Stringer）等人在 2008 年基于期刊引文动力学提出，并在王大顺与巴拉巴西的《科学学》专著中系统阐述，用于解答“科学成果是否具有丧失学术共同体相关性的有效期限”这一核心理论与实践问题。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 204–206)]]

> [!concept-lens|notitle] 概念透镜
> - **含义** 标识单篇学术论著从活跃引述状态向长程智识归档状态过渡的物理时间截断点。
> - **用途** 用于界定学术评价考核的时间窗口，为计算成果全生命周期终极影响（[[Ultimate Impact]]）提供稳态饱和判据。
> - **边界** 适用于解释遵循单峰跳跃衰减规律的绝大多数常规科学出版物；不适用于发生[[Second Act in Science|二次激活]]或[[Sleeping Beauty in Science|睡美人复苏]]的非典型成果。

> [!citation-card] 成果失效期与引文分布稳态
> 科学文献是否具有一个失效期，在此之后便失去了对学术共同体的现实相关性？考虑论著发表后每年的新增获引速率，它呈现出清晰的跳跃衰减形态：获引速率在发表后两到三年迅速迎来峰值，随后开始急剧滑落。绝大多数论著在发表后的前几年便完成了自身绝大部分的影响力释放；随着时间推移，成果的累积被引在若干年后走向平稳饱和。例如至 2006 年，发表于 1991 年与 1993 年的成果其引文分布在统计上已完全等同，表明成果已达到了特定稳态，新增被引变得微不足道。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 204–206)]]
>
> *Do papers have an expiration date, after which they lose their relevance to the scientific community? As Fig. 19.4 shows, citations follow a jump-decay pattern... a paper's cumulative citations do not increase indefinitely, but saturate after a few years. For example, by 2006 the citation distributions of papers published in 1991 or 1993 were statistically indistinguishable... From that point on, the number of new citations a paper garners becomes negligible.*

> [!boundary]- 概念边界
> - 不等于引文半衰期（Citation Half-Life）。半衰期衡量引文累积达到最终总量 50% 所需的时间跨度，是过程性时序中位数；引文失效期则是文献完全停止获得新增引用、增量微乎其微的渐近截断边界。
> - 不等同于科学思想的客观消亡。成果到达引文失效期仅表明其文本不再被显式直接引述，其核心概念往往已被内化为教科书常识或领域默认公理（即被知识整合所吸收）。

---

> [!contrast-table|notitle] 概念辨析
> | 维度 | 引文失效期（[[Citation Expiration Date]]） | 引文半衰期（Citation Half-Life） | 终极学术影响力（[[Ultimate Impact]]） |
> |---|---|---|---|
> | 测度属性 | 增量被引速率降为零的饱和时间截断点 | 累积被引达到终身总量 50% 的时间尺度 | 全生命周期累积被引的绝对总量极限值 |
> | 数理表现 | 引文时序分布达到稳定不变状态的时刻 | 时序积分方程的中位数点 $t_{1/2}$ | $t \to \infty$ 时的渐近闭式解 $c_\infty$ |
> | 核心功能 | 判定文献活跃生命周期的终结边界 | 比较不同学科知识周转与更新速率 | 提供脱离载文期刊光环的长期质量评价标尺 |
> | 经验表现 | 1991 年与 1993 年成果 15 年后分布重合 | 生命科学约 3–5 年，数学学科约 8–10 年 | Cell、PNAS 与 PRB 成果 20 年后均等趋同 |

---

> [!feature] 核心要素
> - **跳跃衰减峰值（Jump-Decay Peak Window）** 成果在面世后 2–3 年内迎来年度新增引用的最高峰，构成了期刊影响因子（JIF）采用两年计算窗口的内在客观机理。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 205–206)]]
> - **15 年队列分布等同律（15-Year Distribution Invariance）** 实证追踪表明，成果发表 15 年后，相邻年份出版的不同论著队列其累积引文分布完全重合，确证其增量引文流已彻底停滞。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Stringer et al., 2008, via Wang & Barabási, 2021, p. 206)]]
> - **学科与期刊特异性（Disciplinary Heterogeneity）** 失效期到达的快慢因载文期刊及学科门类而异：高迭代应用工程学科失效期较早（5–8 年），基础理论与数学学科失效期相对漫长（10–15 年以上）。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, p. 206)]]
> - **终极稳态饱和（Steady-State Saturation）** 越过失效期后，成果的被引总量达到理论预测的饱和天花板，增量变动对长期评价排序不再产生显著影响。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, p. 206)]]

> [!logic-map]- 要素关系
> ```mermaid
> flowchart LR
>     A["发表初期 (0–2年): 迅速爬坡"] --> B["迎来峰值 (2–3年): Jump 阶段"]
>     B --> C["注意力衰减 (3–5年): Decay 阶段"]
>     C --> D["增量大幅滑落，逼近饱和边界"]
>     D --> E["跨越失效期 (Expiration Date, 约10-15年)"]
>     E --> F["新增获引趋于零，分布达到终身稳态"]
> ```

---

> [!concept-proposition] 命题一｜学术文献具有客观有效期限，跨越失效期后引文分布进入确定性稳态
> **探讨维度　引文饱和动力学与有限注意力窗口** 探讨科学文献在时间轴上的影响力持续时间与终身稳态边界。

> [!claim] [[Argument_Wang_Barabasi_2021_Cambridge_Unit09|Stringer et al. (2008)]]
> **引文稳态饱和命题** 斯特林格等通过实证检验表明，科学论著不会无限期获得同行关注；在发表经历特定年限后，文献必然抵达失效期；跨越失效期后，论著的引文分布呈现稳态特征，其相对影响力排位不再发生实质改变。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Stringer et al., 2008, via Wang & Barabási, 2021, pp. 205–206)]]

---

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **引文失效期命题** | 论著在发表特定年限后完全停止获取新引文，分布达到终身稳态 | 科研成果代表作评价、终身学术成就测度与引文时序拟合 | Stringer et al. (2008); [[Argument_Wang_Barabasi_2021_Cambridge\|Wang and Barabási (2021)]] |

---

> [!dev-timeline] 概念演变
> - **1950s — 图书馆空间剔旧** 信息学家观察到纸本期刊借阅量随年代呈几何级数衰减，为腾退书架空间设定剔旧期限。
> - **2008 — 失效期经验测定** 斯特林格等人在《公共科学图书馆·综合》（*PLoS ONE*）发表经典研究，首次量化证明 15 年后不同年份论著引文分布高度重合并提出有效期限度。
> - **2013 — WSB 模型终身解对接** 王大顺等将失效期之后的总累积引用形式化求解为闭式终极影响 $c_\infty$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang et al., 2013)]]
> - **2021 — 科学学系统化确立** 王大顺与巴拉巴西在专著中系统阐明跳跃衰减形态与引文失效期的内在机理。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 204–206)]]

---

> [!debates] 学术争议
>
> > [!axis] 静态失效期假定 vs 数字化长尾持续唤醒
> > 学界围绕随着数字化学术搜索引擎的普及，科学文献是否依然存在严格的引文失效期展开讨论。
> >
> > - **有限注意力支持者** 坚持人类科研群体的总注意力存在硬性容量瓶颈，绝大部分常规研究不可避免地在数年内走向沉寂与失效。
> > - **长尾经典激活派** 指出谷歌学术与数字全文检索大幅拉长了学术记忆，使得高价值成果在十年后仍能保持微弱但稳定的长程获引流，对机械设定的统一失效期阈值提出质疑。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 203–204)]]

> [!warning|limits] 适用局限
> 引文失效期是一个基于统计聚合的平均化构念，不能排除个别重大颠覆性突破在数十年后被重新引爆；失效期时间跨度受细分学科范式迭代节奏强烈调节，跨学科不可机械统一套用。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, p. 206)]]

---

> [!empirical-divider]

> [!ref-table]- 其他实证结果（无效应量）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | 变量或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Wang_Barabasi_2021_Cambridge_Unit09\|Stringer et al. (2008)]] | 1991 年与 1993 年发表于专门期刊（如《生物化学杂志》）的论著队列 | 追踪 15 年长周期累积引文分布对比分析 | 发表后 15 年（截至 2006 年）的累积被引分布曲线重合度 | 1991 年论著与 1993 年论著截至 2006 年的累积引文分布在统计学上**完全无法区分**（图 19-5） | 经验分布高度一致 | 证实常规出版物存在确定性的注意力失效期，增量被引在此后归于停滞 |
> | [[Argument_Wang_Barabasi_2021_Cambridge_Unit09\|Wang & Barabási (2021)]] | 1950 年至 1990 年跨年代发表的跨学科科学论著全样本 | 历时跳跃衰减时序经验拟合 | 发表后各年度新增获引速率峰值与衰减速率 | 论著在发表后 **2–3 年**迎来新增获引峰值；绝大部分引用集中在前 **5 年**；随后以对数正态形态迅速滑落（图 19-4） | 跨年代队列普适重现 | 确立跳跃衰减形态构成了引文失效期与期刊影响因子时间窗口的底层物理机理 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit09|Wang & Barabási (2021)]] — 在专著第 19 章第 4 节系统讨论“文献失效期（Your Expiration Date）”，展示跳跃衰减特征与 15 年稳态分布检验（pp. 204–206）。
