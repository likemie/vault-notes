---
title: i10-Index
aliases:
  - i10指数
  - i10 指数
  - Google Scholar i10 指数
  - i10-Metric
summary: "由 Google Scholar 于 2011 年推出的文献计量指标，定义为学者名下发表成果中被引频次不少于 10 次的论著总篇数；计算轻便透明且对学术生涯早期积累敏感，与 h 指数并行呈现，但受限于固定的绝对阈值而存在学科不均衡与年资累积偏倚。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 9
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
  - "[[Author Name Disambiguation]]"
  - "[[h-Index]]"
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[Dashun Wang]]"
  - "[[Albert-László Barabási]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit01]]"
confidence: high
status: draft
created: "2026-10-30"
updated: 2026-10-30
---

---

> [!def] i10-Index
> **i10 指数（i10-Index）** 由学术搜索引擎 Google Scholar 于 2011 年推出，是针对学者个人学术影响力的简易阈值测度指标。其数学规则定义为：**学者所有公开发表的学术成果中，累计被引频次不低于 10 次的论著总篇数**。该指标被集成于 Google Scholar 学术个人主页，用于反映学者具备中等实质学术反响的核心论著规模。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 学者达到基础同行认可门槛的有影响力成果规模，对应 [[Scientific Productivity|科研生产力]] 与 学术影响力 的初阶结合。
> - **问题类型** 测度个体具备有效学术反响的研究发表规模。
> - **[[Unit of Analysis|分析单位]]** 学者个体科研产出全集。
> - **输入数据** 学者经过[[Author Name Disambiguation|姓名消歧]]后的论著发表记录及对应的独立被引频次。
> - **输出形式** 一个非负整数。

> [!citation-card] Google Scholar 独家采用的 i10 指数
> 除了 h 指数的各种变体外，学界还发展了其他用于量化个别科学家整体成就的指标，包括由 Google Scholar 独家采纳的 i10 指数，该指标计算学者名下每项被引至少达到 10 次的论著数量。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]
>
> *In addition to these variations of the [[h-Index|h-index]], there are other metrics to quantify the overall achievement of individual scientists, including the i10-index, used exclusively by Google Scholar, which computes the number of articles with at least 10 citations each.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 相比单纯发文量，有效过滤了零引用与边缘成果；相比 $h$ 指数，对处于学术积累初期的青年学者更为敏感，计算规则透明直观。
> - **研究者判断** 阈值 10 为人工设定的固定常数，并未依据不同学科的引用基准进行动态校准。
> - **不声称回答的问题** 无法反映超越 10 次阈值后的高被引长尾分布，一项被引 10 次的成果与被引 1000 次的成果在权重上等同计为 1。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis]]。
> - **同类基准指标** [[h-Index]]：两者在 Google Scholar 个人档案中共同列为主流评估标尺，一者反映动态均衡点，一者反映固定阈值篇数。

---

> [!dev-timeline] 方法演变
> - **2011 年 — 官方推出** Google Scholar 推出学者引文个人主页（Google Scholar Citations/Profiles），首次将 i10 指数与总被引频次、h 指数共同作为三大官方标准指标。
> - **2021 年 — 科学学系统化归纳** [[Dashun Wang|王大顺]]与[[Albert-László Barabási|巴拉巴西]]在专著中评述当前学术评价指标体系，确认其作为工业界大规模采纳的少数标准化代表指标之一。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]

---

> [!formula-step] 步骤一　固定阈值计数
> $$i10 = \sum_{i=1}^N \mathbb{I}(c_i \ge 10)$$
>
> **这个公式在做什么** 对学者全部 $N$ 篇发表论著进行遍历，若第 $i$ 篇论著的被引频次 $c_i \ge 10$，指示函数 $\mathbb{I}$ 取值为 1，否则取值为 0，最终求和得出有效论著篇数。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]
>
> **符号说明**
> - $N$：学者名下经消歧确认的论著总篇数；
> - $c_i$：第 $i$ 篇论著获取的累计被引次数；
> - $\mathbb{I}(\cdot)$：指示函数；
> - $i10$：最终输出的有效达标论著总篇数。
>
> **数学直觉** 采用固定的常数截断门槛，将连续长尾的被引分布二值化为“有效成果”与“未达标成果”，通过伯努利累加实现轻量级评价。
>
> > [!example]- 手算示例
> > 设一名青年学者的论著被引频次降序排列如下：
> > - 成果 1：45 次（$\ge 10$）
> > - 成果 2：28 次（$\ge 10$）
> > - 成果 3：12 次（$\ge 10$）
> > - 成果 4：9 次（$< 10$）
> > - 成果 5：3 次（$< 10$）
> >
> > 满足被引 $\ge 10$ 的论著共有 3 篇，故其 $i10 = 3$。该学者若要提升该指标，须推动第 4 项成果新增 1 次被引使其跨过 10 次门槛。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 成果有效规模 | 数值直接代表学者产生稳定学术反响的论著数量，适合用于观察青年学者的早期学术成长。 |
> > | 注意 | 学科硬门槛失真 | 在生物医学等高引领域达到 10 次引用较为容易，而在纯数学或人文学科达到 10 次引用往往需要数年，跨学科可比性较低。 |
>
> > [!geogebra] 动态参数模拟与绝对门槛截断
> > - **横轴** 论著降序名次 $r$（篇）
> > - **纵轴** 单篇被引频次 $C(r)$（次）
> > - **滑块 h** 中枢 $h$ 指数规模（蓝色，调节学者核心成果体量）
> > - **滑块 a** 顶尖引文峰值与产出丰度（绿色，调节长尾饱和度）
> > - **橙虚线** Google Scholar 绝对门槛水平线 $y = 10$
> > - **灰虚线** 判定基准对角线 $y = x$
> > - **蓝实线** 论著被引降序分布曲线 $C(r)$
> > - **蓝点** $h$ 指数动态平衡交点 $(h, h)$
> > - **橙点** $i10$ 指数固定截断点 $(i10, 10)$
> > - **紫粗线段** 中游有效成果缓冲区间 $|i10 - h|$
> >
> > 拖动滑块可直观验证指标分流机制：当 $h > 10$ 时，引文曲线先与对角线 $y=x$ 相交再延伸至水平门槛 $y=10$，此时恒有 $i10 \ge h$，横轴紫色区间清晰反映被引落在 $[10, h)$ 范围的中游稳健成果规模；反之当青年学者 $h < 10$ 时，曲线先截断于 $y=10$，展示了固定门槛与自适应动态门槛的结构性差异。
> >
> > ![[wiki/assets/geogebra/google_scholar_i10_index.ggb]]

> [!software-impl] 软件实现
> - **输入数据** 学者论著被引频次序列。
> - **实现逻辑** 单行列表解析或向量化统计。

> [!formula] Python 计算骨架
> ```python
> def calculate_i10_index(citations: list[int]) -> int:
>     return sum(1 for c in citations if c >= 10)
>
> # 示例调用
> paper_citations = [45, 28, 12, 9, 3]
> print(calculate_i10_index(paper_citations))  # 输出 3
> ```

---

> [!method-fit] 适用判断
> - **适合使用** 评估同领域青年学者或中初级科研人员的起步期学术反响规模。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]
> - **不适合使用** 区分顶尖学术带头人之间的突破性贡献，或直接进行跨学科横向学术排名。

> [!method-limits] 方法局限
> - **绝对门槛刻板** 10 次被引的标准缺乏统计分布自适应性，无法应对学科引用密度的结构性差异。
> - **高引钝感** 无法识别单篇成百上千次的里程碑式重大发现，缺乏对长尾深度的分辨力。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[h-Index]] | 互补指标 | 与 $h$ 指数共同构成 Google Scholar 的标准影响力评估体系。 |
> | [[Scientific Productivity]] | 测量对象 | 表征跨过基础被引门槛的有效科研生产规模。 |
> | [[Bibliometric Analysis]] | 上位方法 | i10 指数是文献计量学中基于阈值计数的微观指标。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit01|Wang & Barabási (2021)]] — 将 i10 指数作为区别于 $h$ 指数自适应截断、由大型索引平台独家应用的单值评估指标进行归纳。
