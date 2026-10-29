---
title: h-alpha Index
aliases:
  - h-alpha指数
  - 科学领导力指数
  - 资深署名h指数
  - Hirsch's h-alpha
  - Leadership-Weighted h-Index
summary: "由 Jorge E. Hirsch (2019) 提出的文献计量修正指标；在构成学者原生 h 指数的全部核心论著中，仅统计该学者为最高学术资历署名专家（即在全部合署研究人员中拥有最高原生 h 指数）的论著数量作为 hα 指数，并通过核心比值 hα / h 量化学者在科研合作网络中的实质学术主导权与独立领导力，有效甄别大型实验工程中的被动署名搭便车现象。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 10
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/indicator
  - theme/scientometrics
  - theme/research-evaluation
related_concepts:
  - "[[Research Impact]]"
  - "[[Unit of Analysis]]"
  - "[[Document]]"
  - "[[Construct Validity]]"
  - "[[Team Science]]"
  - "[[Big Science]]"
related_theories: []
related_methods:
  - "[[h-Index]]"
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[Jorge E. Hirsch]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit01]]"
confidence: high
status: draft
created: "2026-10-29"
updated: 2026-10-30
---

---

> [!def] h-alpha Index
> **科学领导力指数（h-alpha Index，记作 $h_\alpha$）** 由[[Jorge E. Hirsch|乔治·E·希尔施]]（Jorge E. Hirsch）于 2019 年提出，是针对多团队合作网络中署名搭便车与资历稀释设计的 h 指数修正指标。在学者全部贡献于原生 $h$ 指数的核心成果中，仅保留其作为“学术资历最高者”（即在全部合署人员中具备最高原生 $h$ 指数）的成果数量，重新计算得出 $h_\alpha$；比值 $h_\alpha / h$ 则量化了学者科研产出中作为实质学术领航者的纯度。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 学者在多合署成果网络中的独立学术领导力与智力自主权，对应 [[Research Impact]]。
> - **问题类型** 甄别学者是成果的真正学术领军者，还是依托名师提携或大型实验工程被动挂名的普通参与者。
> - **[[Unit of Analysis|分析单位]]** 学者个体及其完整的学术合作成果集合。
> - **输入数据** 学者全部发表[[Document|文献]]的被引次数，以及每篇文献所有合署学者的同时期原生 $h$ 指数矩阵。
> - **输出形式** 一个非负整数 $h_\alpha$（恒满足 $0 \le h_\alpha \le h$），以及无量纲连续比率 $h_\alpha / h \in [0, 1]$。

> [!citation-card] 希尔施论科研合作效应与科学领导力甄别
> 也许 h 指数最严重的短板在于它无法区分合作模式截然不同的学者。一位始终作为青年团队智力引领者的资深学者，与一位主要作为初级协助人员跟随学术权威联合发表的年轻学者，在原生 h 指数面前完全无法辨识。希尔施据此提出了 h_α 指数：在所有构成学者 h 指数的文献中，唯有其作为最具资历学者（在全部合署者中拥有最高 h 指数）的文献才计入指标。高 h 指数兼具高 h_α / h 比值，正是具备卓越科学领导力的典型标志。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]
>
> *Perhaps the greatest shortcoming of the [[h-Index|h-index]] is its inability to discriminate between authors that have very different coauthorship patterns... Hirsch proposed the hα-index to quantify an individual’s scientific leadership... a high h-index in conjunction with a high hα/h ratio is a hallmark of scientific leadership.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 敏锐击中了[[Team Science|团队科学]]大背景下资历借光与挂名膨胀的顽疾，有效剥离搭便车引文红利。
> - **研究者判断** 合署学者原生 $h$ 指数的时间动态对齐方式（以成果出版当年还是评价当年测定）对判定资历高低存在一定敏感性。
> - **不声称回答的问题** 对多学科背景完全平等的强强联合（如顶级物理学家与顶级生物学家平等跨界合作）存在系统性偏见，其中原生 $h$ 稍低一方的独立贡献会被判定为非领导成果。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis]]。
> - **基础指标** [[h-Index]]：$h_\alpha$ 建立在原生 $h$ 指数的核心文献集基础之上。
> - **同类修正** 分数分配贡献法（Fractional Counting）、第一/通讯署名位置加权法。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]

---

> [!dev-timeline] 方法演变
> - **2019 — 指标首创** 希尔施在文献计量学专业论著中正式提出 $h_\alpha$ 指数与科学领导力比率 $h_\alpha / h$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]
> - **2021 — 科学学系统化评介** 王大顺与巴拉巴西在教材中将其作为应对“合作网络搭便车扭曲”的最优解决路径。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]

---

> [!formula-step] 步骤一　基于合署资历判定的 h_alpha 测算
> $$h_\alpha = \sum_{p \in \mathcal{H}_i} \mathbb{I}\left( h_i \ge \max_{j \in \mathcal{A}_p} h_j \right)$$
>
> **这个公式在做什么** 设学者 $i$ 的原生 $h$ 指数核心成果集合为 $\mathcal{H}_i$（即被引量不低于 $h_i$ 的那 $h_i$ 篇高影响力文献）。对于其中任意一项成果 $p$，其全部合署学者集合为 $\mathcal{A}_p$。当且仅当学者 $i$ 自身拥有的原生 $h$ 指数不低于该项成果所有合署人员的最高 $h$ 值时，指示函数 $\mathbb{I}(\cdot)$ 记为 1，否则记为 0。最终对满足资历引领条件的成果求和得出 $h_\alpha$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]
>
> **符号说明**
> - $\mathcal{H}_i$：构成学者 $i$ 原生 $h$ 指数的 $h_i$ 篇核心学术成果集合；
> - $\mathcal{A}_p$：特定学术论著 $p$ 的全部署名学者集合；
> - $h_j$：合署学者 $j$ 在评价时刻的原生 $h$ 指数；
> - $h_\alpha$：学者独立发挥最高学术资历引领作用的核心文献数量；
> - $\text{Leadership Ratio} = \frac{h_\alpha}{h}$：科学领导力纯度系数。
>
> **数学直觉** 经典 $h$ 指数在文献入围时实施无差别平权赋分，使得年轻博士后仅需跟随学科顶级权威参与数个千人巨型实验项目，便可在极短时间内获得极高的原生 $h$。公式通过施加局部最大值筛选算子 $\max_{j \in \mathcal{A}_p} h_j$，剔除了学者因仰仗更高资历同行而获得的被动引流，唯有学者自身作为团队学术顶梁柱的成果才能保留在分子之中。
>
> > [!example]- 手算示例
> > 设学者 $A$ 当前原生 $h = 10$，其 10 篇核心论著的合署情况如下：
> > - 其中 7 篇文献是其带领研究生或青年学者完成，合署者最高 $h$ 均小于等于 10，指示函数记为 1；
> > - 另外 3 篇文献是其作为副手参与诺奖得主（$h=80$）领衔的国际[[Big Science|大科学工程]]，指示函数记为 0。
> > 则学者 $A$ 的 $h_\alpha$ 指数为：
> > $$h_\alpha = 7 \times 1 + 3 \times 0 = 7$$
> > 其科学领导力比率为：
> > $$\frac{h_\alpha}{h} = \frac{7}{10} = 0.70$$
> > 表明该学者 70% 的核心影响力由自身主导产出，具有稳健的独立科研领导力。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | $h_\alpha / h \to 1$ | 极高独立性：成果几乎完全由独立探索或作为最高资历导师引领完成。 |
> > | 读法 | $h_\alpha / h \to 0$ | 严重依赖性：原生 $h$ 虽然可观，但绝大部分依赖资深学者团队的附带红利。 |
> > | 注意 | 平等跨学科盲区 | 计算机专家（$h=30$）与医学教授（$h=60$）实质深度合作时，前者易被误判为非主导者。 |
>
> > [!geogebra] 动态参数模拟
> > - **横轴** 成果被引降序排名 $r$（篇）
> > - **纵轴** 单篇被引频次 $C(r)$（次）
> > - **滑块 h** 原生 $h$ 指数基准规模（蓝色，调节学者整体学术产出存量）
> > - **滑块 hα / h** 团队领导力纯度系数（绿色，调节学者作为最高资历引领者的比重）
> > - **灰色虚线框** 动态原生 $h$ 核心有效面积（$h \times h$ 正方形）
> > - **绿色实线框** 动态独立领导力 $h_\alpha$ 核心有效面积（$h_\alpha \times h_\alpha$ 正方形）
> > - **灰线** $h$ 判定对角线 $y = x$
> > - **红点与青点** 经验对照锚点（大工程挂名学者 $h=30, h_\alpha=6$ 与小团队领军学者 $h=16, h_\alpha=16$）
> >
> > 调节双滑块可直观验证希尔施的核心论断：一位参与巨型工程但缺乏独立引领的学者（如 $h=30, \alpha=0.20 \implies h_\alpha=6$），其实质科学领导力不仅远低于其表面声誉，还会被小团队独立引领者（如 $h=16, \alpha=1.00 \implies h_\alpha=16$）显著反超。
> >
> > ![[wiki/assets/geogebra/hirsch_h_alpha.ggb]]

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit01|Wang & Barabási (2021)]] — 系统评述 Hirsch (2019) 科学领导力指标对科研团队网络评价与同行声望判定的纠偏效度。
