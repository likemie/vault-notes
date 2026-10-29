---
title: Eddington Number
aliases:
  - 埃丁顿数
  - 骑行埃丁顿数
  - Eddington 数
  - E-Number
  - Eddington's Number
summary: "由英国天体物理学家 Arthur Eddington 提出的离散累加成就指标，定义为个体一生中单日骑行里程不少于 E 英里的天数达到 E 天的最大整数 E；因其数学结构与文献计量学中的 h 指数严格同构，在科学学中作为阐明非线性门槛累积与长程战略储备机制的经典参照模型。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 8
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
  - "[[Scientific Productivity]]"
  - "[[Unit of Analysis]]"
  - "[[Construct Validity]]"
related_theories: []
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[h-Index]]"
related_instruments: []
related_persons:
  - "[[Arthur Eddington]]"
  - "[[Jorge E. Hirsch]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit01]]"
confidence: high
status: draft
created: "2026-10-30"
updated: 2026-10-30
---

---

> [!def] Eddington Number
> **埃丁顿数（Eddington Number）** 最初由英国天体物理学家[[Arthur Eddington|亚瑟·爱丁顿]]（Sir Arthur Eddington）提出，用于衡量长途自行车骑行成就。其数学规则定义为：**若一名骑行者一生中有 $E$ 天的单日骑行里程均不少于 $E$ 英里，则其埃丁顿数为 $E$**。该指标在数学结构上与[[Bibliometric Analysis|文献计量学]]中的 $h$ 指数严格同构，在科学学中常作为阐释高门槛非线性累积动力学的经典物理隐喻。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 20)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 离散行为个体的极限稳态表现与高阶成就门槛，在科学学中对应 [[Scientific Productivity|科研生产力]] 与单次产出强度的交叉测度。
> - **问题类型** 衡量个体在长期生涯中兼顾频次与强度的极限累积水平。
> - **[[Unit of Analysis|分析单位]]** 个人全生命周期活动记录。
> - **输入数据** 个体所有单次活动的数值序列（如每日骑行英里数列表）。
> - **输出形式** 一个非负整数 $E$。

> [!citation-card] 爱丁顿数与科研 h 指数的同构性
> 科学家的 h 指数与自行车手的埃丁顿数完全对应。若某人一生中有 70 天单日骑行至少 70 英里，则其埃丁顿数为 70。跨越更高数值极为艰难，例如将数值从 70 提升至 75，往往需要远多于 5 次新的长途骑行，因为所有低于 75 英里的既往记录均不再计入。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 20)]]
>
> *The [[h-Index|h-index]] for scientists is analogous to the Eddington number for cyclists, named after Sir Arthur Eddington (1882–1944)... The Eddington number, E, is the number of days in your life when you have cycled more than E miles. Hence an Eddington number of 70 would mean that the person in question has cycled at least 70 miles a day on 70 occasions. Achieving a high Eddington number is difficult, since jumping from, say, 70 to 75 may require more than 5 new long-distance rides.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 准确捕捉“长程高强度稳健产出”，有效过滤大量低强度的平庸次数堆砌，同时剔除偶发单次极端峰值的影响。
> - **研究者判断** 测量单位的选择（如英里与公里）会对离散数值判定产生显著阶梯差异。
> - **不声称回答的问题** 指标不反映超越门槛之后的超额溢出总量，亦不反映具体产出分布在时间轴上的集中或离散形态。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis]]（作为概念参照与测度同构模型）。
> - **孪生指标** [[h-Index]]：两者仅在应用域上区分（发文篇数与被引频次映射至骑行天数与英里数），底层排序求交算法完全一致。

---

> [!dev-timeline] 方法演变
> - **1940 年代 — 概念形成** 亚瑟·爱丁顿在其晚年系统记录个人自行车长途骑行日志，至 1944 年去世前达到 $E = 87$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 20)]]
> - **2005 年 — 科学计量学同构映射** [[Jorge E. Hirsch|乔治·希尔施]]提出 $h$ 指数后，学界将其算法源流追溯至爱丁顿数。
> - **2021 年 — 科学学系统化阐述** 王大顺与巴拉巴西在专著中将埃丁顿数作为解析 $h$ 指数“阶梯上升阻力”与“长程战略规划”的核心参照。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 20)]]

---

> [!formula-step] 步骤一　降序排序与阈值判定
> $$E = \max \{ k \in \mathbb{N} \mid M_k \ge k \}$$
>
> **这个公式在做什么** 将个体历史所有单日活动表现按数值从高到低排列为 $M_1 \ge M_2 \ge \dots \ge M_N$，寻找序列编号 $k$ 与其对应活动表现 $M_k$ 的最大相交索引点。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 20)]]
>
> **符号说明**
> - $M_k$：按强度由高到低排序后第 $k$ 次活动的记录数值（例如骑行英里数）；
> - $k$：活动的序数位次（秩次）；
> - $E$：最终测定的离散阈值整数。
>
> **数学直觉** 构造一条斜率为 1 的对角线 $y = x$，曲线 $y = M_k$ 与该对角线的最后一个交点横坐标即为指标值，体现了频次与强度的严格均衡。
>
> > [!example]- 手算示例
> > 设一名骑行者的历史单日骑行记录降序排列如下（单位：英里）：
> > - 第 1 次：85 英里（$\ge 1$）
> > - 第 2 次：80 英里（$\ge 2$）
> > - 第 3 次：78 英里（$\ge 3$）
> > - 第 4 次：75 英里（$\ge 4$）
> > - 第 5 次：20 英里（$\ge 5$）
> > - 第 6 次：15 英里（不满足 $\ge 6$）
> >
> > 此时满足 $M_k \ge k$ 的最大位次为 $k = 5$（第 5 次骑行为 20 英里 $\ge 5$），故该骑行者的埃丁顿数为 $E = 5$。若其希望冲击 $E = 6$，下一次骑行必须达到至少 6 英里，且第 6 次记录需达到 6 英里以上。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 跨门槛边际成本递增 | 当基数较高时（如从 $E=70$ 到 $75$），此前积累的所有 70–74 英里记录在提升至 75 时被全部归零过滤，必须补充满足新门槛的极端产出。 |
> > | 注意 | 早期储备依赖 | 提升最终指标必须尽早布局满足更高强度标准的产出，依赖短期零星产出无法跨越长期积累门槛。 |
>
> > [!geogebra] 动态参数模拟与非线性阶梯阻力
> > - **横轴** 骑行累计天数 / 活动降序秩次 $k$（天）
> > - **纵轴** 单日骑行里程 $M(k)$（英里）
> > - **滑块 E** 当前埃丁顿数（蓝色，调节当前生涯达标水平）
> > - **滑块 E\*** 目标冲刺门槛（橙色，调节拟挑战的高阶门槛）
> > - **灰虚线** 判定基准对角线 $y = x$
> > - **蓝实线** 单日里程降序分布曲线 $M(k)$
> > - **蓝色方块** 当前埃丁顿核心有效面积（$E \times E$）
> > - **橙色虚框** 目标冲刺门槛边界（$E^* \times E^*$）
> > - **橙粗线段** 阶梯提升阻力区间 $\Delta E$
> > - **金星锚点** 亚瑟·爱丁顿毕生纪录（$E = 87$，1944 年晚年记录）
> >
> > 拖动滑块可直观验证非线性棘轮机制：当试图将数值从 $E=70$ 提升至 $75$ 时，不仅需要累计 75 天达到新门槛，且此前所有处于 70–74 英里的既有骑行记录均被全部归零过滤，必须补充满足 $\ge 75$ 英里的全新高强度表现，直观展现了高阶成就指标在后期边际成本呈阶梯式剧增的内在动力学。
> >
> > ![[wiki/assets/geogebra/eddington_number.ggb]]

> [!software-impl] 软件实现
> - **输入要求** 一维数值列表或数组。
> - **实现逻辑** 降序排列后，通过单次遍历比较数值与索引下标。

> [!formula] Python 计算骨架
> ```python
> def calculate_eddington_number(records: list[float]) -> int:
>     sorted_records = sorted(records, reverse=True)
>     e_number = 0
>     for rank, val in enumerate(sorted_records, start=1):
>         if val >= rank:
>             e_number = rank
>         else:
>             break
>     return e_number
>
> # 示例调用
> rides = [85.0, 80.0, 78.0, 75.0, 20.0, 15.0]
> print(calculate_eddington_number(rides))  # 输出 5
> ```

---

> [!method-fit] 适用判断
> - **适合使用** 评估具有长尾分布与高强度要求的个人全生涯极限累积水平。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 20)]]
> - **不适合使用** 衡量短期阶段性绩效波动，或需要精细度量超额极值总量的分析情境。

> [!method-limits] 方法局限
> - **计量单位敏感性** 英里制与公里制得出的数值不同，换算并不具备尺度不变性。
> - **平庸截断** 门槛之下的所有产出无论规模多大均被完全忽略，门槛之上的超额产出亦不获得附加权重。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[h-Index]] | 孪生指标 | 两者在离散排序和对角线截断算法上完全同构。 |
> | [[Scientific Productivity]] | 测量对象 | 在科学计量隐喻中表征学者的生产力与影响力兼备程度。 |
> | [[Bibliometric Analysis]] | 上位方法 | 埃丁顿数作为算法源流启发了现代文献计量学个体评价指标的设计。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit01|Wang & Barabási (2021)]] — 将自行车手的埃丁顿数作为 $h$ 指数的同构参照，阐释高门槛阶梯提升阻力与长程战略积累逻辑。
