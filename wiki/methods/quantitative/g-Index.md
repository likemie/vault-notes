---
title: g-Index
aliases:
  - g指数
  - Egghe's g-index
  - 艾格指数
summary: "由 Leo Egghe (2006) 提出的文献计量指标，以被引最高的 g 篇论著累计被引至少 g² 次界定学者影响；用于弥补 h 指数对高被引论著的钝感，仍受学科基准与合著归属的限制。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 4
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
  - "[[Research Impact]]"
related_theories: []
related_methods:
  - "[[h-Index]]"
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
> **g 指数（g-Index）** 由里奥·艾格（Leo Egghe）于 2006 年提出，是 [[h-Index|h 指数]]的修正指标。把学者论著按被引次数降序排列，被引最高的 $g$ 篇累计被引至少 $g^2$ 次的最大整数即为 $g$。它允许高被引论著的超额引用进入数值，补足 $h$ 指数对奠基性成果的钝感。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 学者核心论著的累积学术影响，对应 [[Research Impact]]。
> - **问题类型** 描述与评价学者的累积学术成就，尤其是有高被引代表作的学者。
> - **分析单位** 学者个人，或团队、机构的论著集合。
> - **输入数据** 学者全部论著的逐篇被引次数，需完成作者姓名消歧。
> - **输出形式** 一个非负整数 $g$，且恒有 $g \ge h$。

> [!citation-card] 高被引成果在 h 指数中不可见
> h 指数的主要优势是它的数值不会被单次偶然成功抬高，但这也意味着它忽视了研究者最有影响力的工作。论著被引一旦超过 h，其相对重要性在 h 指数中就不可见了。为此学界提出了 g 指数等多种补救方案。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 25)]]
>
> *The main advantage of the h-index is that its value is not boosted by a single runaway success. Yet this also means that it neglects the most impactful work of a researcher. Indeed, once a paper’s citations get above h, its relative importance becomes invisible to the h-index. Many remedies have been proposed to correct for this, including the g-index.*

---

> [!method-position] 方法定位
> - **构念效度** 用累计被引代替逐篇门槛，高被引论著的影响得以计入；代价是对少数极高被引论著更敏感。
> - **研究者判断** 数据库、成果类型、自引处理与消歧方式都会改变 $g$。
> - **不声称回答的问题** 不能跨学科直接比较，不能识别合著中的个人贡献，也不用于评价单篇论著。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis]]。
> - **基础指标** [[h-Index]]：$g$ 在同一排序上改用累计门槛。
> - **同类修正** $o$ 指数（Dorogovtsev & Mendes, 2015）：$o=\sqrt{c^{*}h}$，$c^{*}$ 为单篇最高被引。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]

---

> [!formula-step] 计算 g 值
> $$g=\max\Big\{\,k : \sum_{i=1}^{k} c_i \ge k^2\,\Big\}$$
>
> **这个公式在做什么** 输入按被引降序排列的逐篇被引次数，输出前 $k$ 篇累计被引不低于 $k^2$ 的最大 $k$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]
>
> **符号说明** $c_i$ 为第 $i$ 篇的被引次数；$k$ 为候选名次。
>
> **数学直觉** $h$ 要求每一篇都过门槛；$g$ 只要求前 $k$ 篇的平均被引至少为 $k$，高被引论著多出的引用可以补给排名靠后的论著。由于逐篇满足 $c_i \ge h$ 必然使累计和不少于 $h^2$，所以 $g \ge h$。
>
> > [!example]- 手算示例
> > 示例：被引降序为 25、8、5、4、3、0。累计和依次为 25、33、38、42、45、45，对应门槛 1、4、9、16、25、36，前 6 篇都满足，$g=6$；同一组数据 $h=4$。第 1 篇若只有 5 次引用，累计和 5、13、18、22、25、25，在 $k=5$ 时 $25 \ge 25$、$k=6$ 时 $25<36$，$g$ 降为 5。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 与 $h$ 的差距 | $g$ 与 $h$ 差距越大，学者的影响越集中在少数高被引论著上；两者接近，说明被引分布较均匀。 |
> > | 注意 | 篇数不足 | 论著篇数少于 $g$ 时，部分文献补零篇被引为 0 的虚拟论著再计算，结果会不同，报告时需说明采用哪种做法。 |

> [!formula] Python 计算骨架
> ```python
> def g_index(citations):
>     c = sorted(citations, reverse=True)
>     total, g = 0, 0
>     for k, x in enumerate(c, start=1):
>         total += x
>         if total >= k * k:
>             g = k
>     return g
>
> g_index([25, 8, 5, 4, 3, 0])  # 6
> ```

---

> [!method-fit] 适用判断
> - **适合使用** 与 $h$ 并用，识别论著不多但有奠基性高被引成果的学者。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 18–19, 25)]]
> - **不适合使用** 跨学科直接比较；评价大型合作团队中的个人贡献。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]

> [!method-limits] 方法局限
> - **学科基准差异** 高能物理、生物化学等领域的 $g$ 普遍高于数学。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]
> - **合著失真** 千人署名论著的高被引对全部合作者等同计入，搭便车效应比 $h$ 更明显。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 25)]]
> - **补救方式** 按学科归一化，按署名贡献拆分引用，并与 $h$ 同时报告。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[h-Index]] | 基础指标 | $g$ 针对 $h$ 忽视超额引用的缺陷而提出。 |
> | [[Research Impact]] | 测量对象 | $g$ 以累计被引代表核心论著的学术影响。 |
> | [[Bibliometric Analysis]] | 上位方法 | $g$ 是文献计量分析中的个体层面指标。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit01|Wang & Barabási (2021)]] — 把 g 指数和 o 指数作为 h 指数忽视高被引论著的修正方案加以介绍。
