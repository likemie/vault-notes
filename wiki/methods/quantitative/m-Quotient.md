---
title: m-Quotient
aliases:
  - 赫希m商数
  - m商数
  - 学术增长速率斜率
  - Hirsch's m-Quotient
  - m-Index
  - m-Parameter
summary: "由 Jorge E. Hirsch (2005) 提出的文献计量指标；基于 h 指数随学术生涯时间线性累积模型 h = mt，定义斜率 m = h / t，通过学术年资（自首篇论著发表以来的年数 t）对 h 指数进行时间归一化，用于跨学术年龄阶段对比学者长程学术影响力增长速率（物理学界晋升副教授 m ≈ 1，正教授 m ≈ 2，院士级 m ≈ 3）。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 11
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
  - "[[Scientific Productivity]]"
  - "[[Research Impact]]"
  - "[[Unit of Analysis]]"
  - "[[Document]]"
  - "[[Research Universities]]"
  - "[[Construct Validity]]"
  - "[[Paradigm]]"
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

> [!def] m-Quotient
> **赫希 m 商数（Hirsch's m-Quotient）** 由[[Jorge E. Hirsch|乔治·E·希尔施]]（Jorge E. Hirsch）于 2005 年提出，是基于 h 指数的时间归一化速率指标。通过将学者的 $h$ 指数除以其学术生涯总年限 $t$（自首次公开发表学术成果以来的年数），导出线性增长斜率 $m = h / t$。该指标用于消除 $h$ 指数天生向资深科研人员倾斜的年资优势，衡量学者在单位学术时间内的知识贡献加速度。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 18–20)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 学者在学术生涯周期内的科研产出与被引增长综合速率，对应 [[Scientific Productivity]] 与 [[Research Impact]]。
> - **问题类型** 跨学术年资阶段横向对比学者的学术卓越增速与前瞻潜力。
> - **[[Unit of Analysis|分析单位]]** 学者个体科研全生命周期。
> - **输入数据** 学者当期的 $h$ 指数数值，以及首篇同行审阅学术[[Document|文献]]出版至今的自然年数 $t$。
> - **输出形式** 一个连续型正实数 $m$，通常取值在 $0.5$ 至 $3.0$ 区间。

> [!citation-card] 希尔施论时间归一化 m 参数与学者卓越速率
> 如果学者的 h 指数随学术生涯时间大致呈线性增长，则其增长斜率 m 构成了衡量学术卓越程度的关键指标。m 取决于年发文量 n 与篇均年被引量 c，数值越高代表学者在同辈群体中越具前瞻影响力。在主流[[Research Universities|研究型大学]]物理学界，m ≈ 1 代表可授予长聘副教授的典型基准，m ≈ 2 代表杰出正教授，而 m ≈ 3 则代表极为罕见顶尖领军学者。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 19–20)]]
>
> *If a scientist’s [[h-Index|h-index]] increases roughly linearly with time, then its speed of growth is an important indicator of her eminence... characterized by the slope, m... a value of m ≈ 1 characterizes successful scientists at major research universities, m ≈ 2 characterizes outstanding scientists, and m ≈ 3 characterizes truly unique individuals.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 成功剥离了被动的时间累积存量，将静态总成就转化为单位时间动量；但在生涯早期（$t < 5$ 年）因样本时间窗口过短易产生数值过大波动。
> - **研究者判断** 学术生涯起点的界定方式（以首篇发表年份还是博士毕业年份起算）会对年轻学者的 $m$ 值产生显著影响。
> - **不声称回答的问题** 不能直接用于跨学科对比，因为不同学科的基础文献被引速率存在系统性鸿沟；亦无法反映中途转换研究方向或经历学术休假的非线性轨迹。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 19, 26)]]

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis]]。
> - **基础指标** [[h-Index]]：$m$ 是对 $h$ 指数引入时间分母 $t$ 后的线性导数估计。
> - **同类修正** 当代 $h$ 指数（Contemporary $h$-index）：对近期发表的新成果赋予时间衰减权重。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]

---

> [!dev-timeline] 方法演变
> - **2005 — 原始提出** 乔治·希尔施在 PNAS 奠基论著中提出 $h$ 指数的同时导出线性累积模型 $h = mt$ 与 $m$ 商数。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 18–20)]]
> - **2021 — 科学学系统化梳理** 王大顺与巴拉巴西在专著中将 $m$ 商数作为解决 $h$ 指数“时间依赖性”缺陷的核心标准[[Paradigm|范式]]。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 19, 26)]]

---

> [!formula-step] 步骤一　基于线性模型的 m 商数推导
> $$m = \frac{h}{t} = \frac{1}{\frac{1}{c} + \frac{1}{n}} = \frac{cn}{c + n}$$
>
> **这个公式在做什么** 希尔施假定学者平均每年产出 $n$ 篇经过评审的论著，且每篇论著在发表后每年平均稳定新增 $c$ 次引用。据此推导可知，学者的 $h$ 指数随从影年数 $t$ 呈线性增长，其增长速率斜率 $m$ 严格受制于年发文率 $n$ 与篇均年被引率 $c$ 的调和均值结构。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 18–19)]]
>
> **符号说明**
> - $h$：学者当前的 $h$ 指数；
> - $t$：学者自发表首篇文献以来的学术生涯年数；
> - $n$：学者平均每年发表的论著篇数；
> - $c$：学者已发表论著平均每年获取的新增引用次数；
> - $m$：$h$ 指数的时间累积速率斜率。
>
> **数学直觉** $m$ 的倒数等于生产力倒数与影响力倒数之和（$\frac{1}{m} = \frac{1}{n} + \frac{1}{c}$），这意味着 $m$ 的上限严格受到发文速度 $n$ 与被引速度 $c$ 中较短那一根短板的制约。单纯高产而无引用的学者（$n$ 极大但 $c \to 0$）或单篇爆款而后沉寂的学者（$c$ 极大但 $n \to 0$），其 $m$ 值均趋近于零。唯有兼具持续发表与持续获引双重素质，方能维持高水平的 $m$ 斜率。
>
> > [!example]- 手算示例
> > 设一名学者学术年资 $t = 10$ 年，当前 $h = 15$。其经验 $m$ 值为：
> > $$m = \frac{15}{10} = 1.5$$
> > 根据希尔施物理学评估基线，$m=1.5$ 处于优秀长聘副教授至正教授水平之间。若该学者年均发表 $n = 3$ 篇论著，篇均每年新增 $c = 3$ 次引用，理论预测斜率为 $m = \frac{3 \times 3}{3 + 3} = 1.5$，与实测吻合。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | $m \approx 1$ | 达到主要研究型大学长聘教职（Tenure）或副教授晋升的典型基准线。 |
> > | 读法 | $m \approx 2$ | 达到国家级知名学术带头人、全职正教授或顶级学会会士（Fellow）水平。 |
> > | 读法 | $m \ge 3$ | 极度罕见的顶尖学者，往往在职业生涯中长期保持超常产出与巨额引用。 |
> > | 注意 | 年资下限假设 | 仅对学术年资 $t \ge 5$ 年的学者具备稳健预测效度；青年早期随机扰动过大。 |
>
> > [!geogebra] 动态参数模拟与基准参照
> > - **横轴** 学术年资 $t$（年）
> > - **纵轴** $h$ 指数
> > - **滑块 n** 年均发文篇数（绿色）
> > - **滑块 c** 篇均年新增引（红色）
> > - **滑块 t** 当前学术年资（紫色）
> > - **红线** 实际学术增长轨迹 $h(t) = m \cdot t$
> > - **三条基准射线** 绿虚线（$m \approx 1$ 副教授）、蓝虚线（$m \approx 2$ 正教授）、紫虚线（$m \approx 3$ 顶尖学者）
> >
> > 拖动滑块 $n$ 与 $c$ 可直观验证调和平均瓶颈效应：单方面极大增加发文量（如 $n=10$）而缺乏引用（如 $c=1$），$m$ 值将被牢固锁死在 $1.0$ 以下；唯有发文与被引双轮驱动，方能跨入杰出教授区间。
> >
> > ![[wiki/assets/geogebra/hirsch_m_quotient.ggb|480]]

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit01|Wang & Barabási (2021)]] — 结合 Hirsch (2005) 理论推导与凝聚态物理学者实证追踪，系统检验 $m$ 商数在人才前瞻预测中的效能。
