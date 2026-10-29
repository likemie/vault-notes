---
title: Contemporary h-Index
aliases:
  - 当代h指数
  - 当代 h 指数
  - Sidiropoulos 当代指数
  - hc-Index
  - hc 指数
summary: "由 Antonis Sidiropoulos et al. (2007) 提出的时间加权文献计量指标；通过为单篇论著引入发表年资幂律衰减因子，对近期新产出赋予更高权重并衰减陈旧引用，解决传统 h 指数只增不减、难以捕捉学者近期真实科研活跃度的时滞缺陷。"
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
  - theme/scientometrics
  - theme/research-evaluation
related_concepts:
  - "[[Unit of Analysis]]"
  - "[[Construct Validity]]"
  - "[[Document]]"
related_theories: []
related_methods:
  - "[[h-Index]]"
  - "[[Bibliometric Analysis]]"
  - "[[m-Quotient]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit01]]"
confidence: high
status: draft
created: "2026-10-30"
updated: 2026-10-30
---

---

> [!def] Contemporary h-Index
> **当代 h 指数（Contemporary [[h-Index]]，记作 $h^c$）** 由 Antonis Sidiropoulos、Dimitrios Katsaros 和 Yannis Manolopoulos 于 2007 年提出，是针对 $h$ 指数时间单调性缺陷开发的时间衰减修正指标。其数学规则定义为：**通过为学者发表的每项论著按其距今出版年限赋予幂律时间衰减权重，重算该项研究的“当代得分”，并求取满足加权得分不低于名次序号的最大论著篇数**。该指标用于动态奖励活跃产出，削减历史远期既有引用的累积优势。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 学者在近期时间窗口内的实际学术活跃度与持续知识供给能力，对应带有时间维度的动态 学术影响力。
> - **问题类型** 评估学者的当代科研生命力，校正资深学者因历史旧作累积形成的年资惯性优势。
> - **[[Unit of Analysis|分析单位]]** 学者个体科研产出全集。
> - **输入数据** 学者各项论著的发表年份、累计被引频次以及评估当期基准年份。
> - **输出形式** 一个正整数 $h^c$。

> [!citation-card] 希尔施指数的时间依赖性与当代修正
> 如第 2.2 节所述，h 指数具有强烈的时间依赖性。在对比处于不同职业生涯阶段的科学家时，研究者可以使用希尔施 m 商数，或者采用当代 h 指数。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]
>
> *Time dependence. As we discussed in Chapter 2.2, the h-index is time dependent. When comparing scientists in different career stages, one can use the m quotient, or contemporary h-index.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 引入显式时间折扣函数，使长期停滞产出或仅依赖数十年历史旧作维系高引的学者指标自然回落，凸显正在产生新知识贡献的活跃学者。
> - **研究者判断** 衰减参数 $\gamma$（基准倍数）与 $\delta$（衰减幂律指数）通常分别预设为 4 与 1，但特定学科知识老化周期的差异可能需要重新率定参数。
> - **不声称回答的问题** 指标依然基于单篇成果的聚合累加，未解决跨学科引用密度差异与合著署名贡献分割问题。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis]]。
> - **基础指标** [[h-Index]]：当代 $h$ 指数保留了 $h$ 型指标的对角线平衡逻辑，但将静态被引代换为时间折扣得分。
> - **同类时间修正方案** [[m-Quotient]]：$m$ 商数通过除以总年资 $t$ 进行全局线性归一化，而 $h^c$ 在微观单项成果层面逐篇实施非线性时间衰减。

---

> [!dev-timeline] 方法演变
> - **2007 年 — 理论提出** Sidiropoulos 等人在 *Information Processing & Management* 提出广义希尔施指数族（Generalized Hirsch Indexes），正式定义当代 $h^c$ 指数。
> - **2021 年 — 科学学系统化梳理** 王大顺与巴拉巴西在专著中将 $h^c$ 指数与 $m$ 商数并列，作为解决传统 $h$ 指数时间累积偏差的代表性经典工具。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]

---

> [!formula-step] 步骤一　单项论著当代得分计算
> $$S^c(i) = \gamma \cdot (Y^{\text{now}} - Y_i + 1)^{-\delta} \cdot C_i$$
>
> **这个公式在做什么** 对学者名下的第 $i$ 项论著，计算其经过时间衰减折算后的有效引用贡献度 $S^c(i)$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]
>
> **符号说明**
> - $Y^{\text{now}}$：当前进行[[Document|文献]]计量评估的自然年份；
> - $Y_i$：第 $i$ 项论著的正式出版年份；
> - $C_i$：第 $i$ 项论著截至当期获得的原始被引总频次；
> - $\gamma$：时间加权放大系数（经典设定 $\gamma = 4$）；
> - $\delta$：时间衰减指数（经典设定 $\delta = 1$）。
>
> **数学直觉** 当一项成果刚在当年发表时（$Y^{\text{now}} - Y_i = 0$），分母为 1，其每次新增引用被赋予 $\gamma = 4$ 倍的高权重视图；而当成果发表已满 4 年时，分母为 $4+1=5$，单次引用权重降至 $4/5 = 0.8$；随着时间推移，陈旧文献的历史引用贡献被逐步压低。

---

> [!formula-step] 步骤二　当代加权排序与最大截断点判定
> $$h^c = \max \{ k \in \mathbb{N} \mid S^c(k) \ge k \}$$
>
> **这个公式在做什么** 将学者所有成果按当代得分 $S^c(i)$ 降序排列 $S^c(1) \ge S^c(2) \ge \dots \ge S^c(N)$，提取满足加权得分不小于位次编号 $k$ 的最大整数 $h^c$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]
>
> > [!example]- 手算示例
> > 设当前评估年份 $Y^{\text{now}} = 2026$，参数取 $\gamma = 4, \delta = 1$。某学者有 3 项代表作：
> > - 成果 A（2025 年出版，距今 1 年，原始引用 10 次）：
> >   $$S^c(A) = 4 \times (2026 - 2025 + 1)^{-1} \times 10 = 4 \times \frac{1}{2} \times 10 = 20$$
> > - 成果 B（2021 年出版，距今 5 年，原始引用 30 次）：
> >   $$S^c(B) = 4 \times (2026 - 2021 + 1)^{-1} \times 30 = 4 \times \frac{1}{6} \times 30 = 20$$
> > - 成果 C（2006 年出版，距今 20 年，原始引用 100 次）：
> >   $$S^c(C) = 4 \times (2026 - 2006 + 1)^{-1} \times 100 = 4 \times \frac{1}{21} \times 100 \approx 19.05$$
> >
> > 降序排列后得分分别为 20、20、19.05，均满足得分 $\ge 3$，故该学者当代 $h^c = 3$。二十年前被引 100 次的老旧代表作折算后与去年被引 10 次的新作相当，体现了强烈的当代性约束。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 动态升降 | 与传统 $h$ 指数单调不减不同，若学者停止活跃发表新成果，随着时间流逝，既往论著的当代得分将持续衰减，其 $h^c$ 指数可能发生回落。 |
> > | 注意 | 衰减敏感性 | 新发表的高引突破会因 $\gamma$ 放大因子迅速拉升 $h^c$，适合用于捕捉上升期学术新星。 |
>
> > [!geogebra] 动态参数模拟与时效衰减效应
> > - **横轴** 论著降序名次 $k$（篇）
> > - **纵轴** 原始被引与当代得分 $S^c$
> > - **滑块 h** 原始 $h$ 指数规模（蓝色，调节学者中枢产出体量）
> > - **滑块 Δt** 核心成果平均出版年资（橙色，调节成果陈旧度与老化周期）
> > - **灰虚线** 判定基准对角线 $y = x$
> > - **灰细线** 原始被引曲线 $C(k)$（无时间衰减基准）
> > - **绿实线** 当代加权得分曲线 $S^c(k) = w(\Delta t) \cdot C(k)$
> > - **蓝点** 传统 $h$ 指数截断点 $(h, h)$
> > - **绿点** 当代 $h^c$ 指数截断点 $(h^c, h^c)$
> > - **紫粗线段** 时效修正位移区间 $\Delta = h^c - h$
> > - **青点与红点** 经验对照锚点（活跃学术新星 $h^c > h$ 与停滞资深学者 $h^c \ll h$）
> >
> > 拖动滑块 $\Delta t$ 可直观验证时间折现机制：当成果距今 $\le 3$ 年时，$w(\Delta t) \ge 1.0$，当代曲线抬升超过原始线，展现对活跃产出的动态激励；当成果老化（$\Delta t > 3$ 年）时，$w(\Delta t)$ 急剧压低得分曲线，使指标随时间推移自然回落，有效破除传统 $h$ 指数终身单调不减的时滞缺陷。
> >
> > ![[wiki/assets/geogebra/sidiropoulos_contemporary_h_index.ggb]]

> [!software-impl] 软件实现
> - **输入数据** 论著发表年份列表与对应引用次数列表。
> - **计算流程** 向量化计算单篇 $S^c$ 得分后排序提取截断点。

> [!formula] Python 计算骨架
> ```python
> def calculate_contemporary_h_index(
>     publications: list[dict], current_year: int, gamma: float = 4.0, delta: float = 1.0
> ) -> int:
>     scores = []
>     for pub in publications:
>         pub_year = pub["year"]
>         cites = pub["citations"]
>         age = current_year - pub_year + 1
>         weight = gamma * (age ** (-delta))
>         scores.append(weight * cites)
>     scores.sort(reverse=True)
>     hc = 0
>     for rank, score in enumerate(scores, start=1):
>         if score >= rank:
>             hc = rank
>         else:
>             break
>     return hc
> ```

---

> [!method-fit] 适用判断
> - **适合使用** 招聘、青年人才选拔或评审需要精准考量近 5–10 年内活跃学术贡献的场景。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]
> - **不适合使用** 终身成就奖等旨在表彰历史奠基性终身贡献的荣誉评定。

> [!method-limits] 方法局限
> - **参数先验设定** 衰减系数对不同学科引用周期的适应性不同，例如生物医学成果衰减快，数学成果半衰期长，统一参数跨学科比较存在偏差。
> - **新发文献噪声** 刚发表 1–2 年的成果引用仍在孕育期，时间权重放大可能放大偶然引用的波动。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[h-Index]] | 基础指标 | 当代 $h$ 指数通过引入单篇发表年限时间衰减因子修正传统 $h$ 指数。 |
> | [[m-Quotient]] | 同类方案 | 两者均针对 $h$ 指数时间累积偏倚，但 $m$ 商数做全局归一，当代 $h$ 指数做逐篇微观衰减。 |
> | [[Bibliometric Analysis]] | 上位方法 | 属于文献计量学中的动态时效性测度方法。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit01|Wang & Barabási (2021)]] — 将当代 $h$ 指数与 $m$ 商数并列，阐述文献计量学针对 $h$ 指数时间依赖性缺陷所采取的微观加权修正方案。
