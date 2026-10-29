---
title: h-Index
aliases:
  - h指数
  - Hirsch index
  - 希尔施指数
summary: "由 Jorge E. Hirsch (2005) 提出的文献计量指标，以学者至多有 h 篇论著各被引至少 h 次界定其累积学术影响；计算简便、对单篇偶然高被引稳健，并对未来产出影响有较强预测效度，但不能跨学科直接比较，也看不到超额引用与团队分工。"
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
  - "[[Predictive Validity]]"
  - "[[Research Universities]]"
related_theories:
  - "[[Shockley's Multiplicative Hurdle Model]]"
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[g-Index]]"
related_instruments: []
related_persons:
  - "[[Jorge E. Hirsch]]"
related_facts:
  - "[[National Academy of Sciences]]"
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit01]]"
  - "[[Argument_Wang_Barabasi_2021_Cambridge]]"
confidence: high
status: draft
created: "2026-10-29"
updated: 2026-10-29
---

---

> [!def] h-Index
> **h 指数（h-Index）** 由物理学家[[Jorge E. Hirsch|乔治·E·希尔施]]（Jorge E. Hirsch）于 2005 年提出，用于测度学者个人的累积学术影响。一名学者的指数为 $h$，当且仅当其全部论著中至多有 $h$ 篇各获得至少 $h$ 次引用，其余论著的被引次数均未达到 $h$。计算时把论著按被引次数降序排列，找出排名不超过自身被引次数的最大名次，即为 $h$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 17–18)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 学者成果的数量与被引影响的联合水平，对应 [[Scientific Productivity]] 与 [[Research Impact]] 两个构念。
> - **问题类型** 描述与评价学者的累积学术成就，并预测其未来产出的影响。
> - **分析单位** 学者个人；也可用于团队、机构或期刊的论著集合。
> - **输入数据** 学者全部论著的逐篇被引次数，需完成作者姓名消歧。
> - **输出形式** 一个非负整数 $h$；配合年资可得增长斜率 $m$。

> [!citation-card] 希尔施论 h 指数的优势
> h 指数的关键优势在于它避开了上述各项指标的全部缺点，能简便而相对准确地估计个人的整体科学成就。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 21–22)]]
>
> *The key advantage of the h-index is that it sidesteps all of the disadvantages of the metrics... it gives an easy but relatively accurate estimate of an individual's overall scientific achievements.*

---

> [!method-position] 方法定位
> - **构念效度** $h$ 只计入同时满足数量与被引门槛的核心成果，代表学者持续产出受关注成果的能力；越过门槛之后的超额引用、门槛以下的成果以及教学、指导、评审等非文献贡献都不进入数值。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–27)]]
> - **研究者判断** 选择哪个数据库、统计哪些成果类型、是否剔除自引、如何消歧，都会改变 $h$ 的数值。
> - **有效性标准** 预测效度是主要支撑。希尔施（Hirsch, 2007）对凝聚态物理学者 24 年发表记录的追踪显示，在预测未来累积引用与新作影响时，前 12 年的 $h$ 优于发文总量、总被引与篇均被引。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 21–23)]]
> - **不声称回答的问题** 不能比较不同学科学者的高低，不能识别合著中的实际贡献，也不能单独证明某项成果的原创性。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis]]。
> - **前置步骤** 作者姓名消歧、论著去重、被引次数采集。
> - **变体与扩展**
>   - [[g-Index]]（Egghe, 2006）：前 $g$ 篇累计被引至少 $g^2$ 次，恢复高被引论著的权重。
>   - $o$ 指数（Dorogovtsev & Mendes, 2015）：$o=\sqrt{c^{*}h}$，$c^{*}$ 为单篇最高被引。
>   - $h_g$ 指数（Radicchi et al., 2008）：按同领域同年份论著的被引基准归一化。
>   - $m$ 商（Hirsch, 2005）：$m=h/t$，扣除年资影响。
>   - $h_\alpha$ 指数（Hirsch, 2019）：只计入学者在合著者中 $h$ 最高的论著，识别团队中的学术引领者。

> [!dev-timeline]- 方法演变
> - **2003 — 初次构想** 希尔施手动测算身边物理学家的 $h$ 值，发现排序与同行声誉高度一致。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 24–25)]]
> - **2005 — 正式提出** 手稿上传 arXiv 并投稿《美国国家科学院院刊》（Proceedings of the National Academy of Sciences, PNAS），同时给出线性增长模型与物理学职称参照值。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 17–20, 24–25)]]
> - **2006–2008 — 修正指标出现** $g$ 指数针对高被引钝感，$h_g$ 指数针对学科基准差异。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]
> - **2007 — 预测效度检验** 希尔施以 24 年纵向数据检验 $h$ 对未来表现的预测力。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 21–23)]]
> - **2019 — 合著修正** 希尔施提出 $h_\alpha$ 指数。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]

---

> [!formula-set]- 公式链总览
> ```mermaid
> flowchart LR
>   A["论著与逐篇被引"] --> B["按被引降序排列"]
>   B --> C["找 c_i ≥ i 的最大名次"]
>   C --> D["h 值"]
>   D --> E["除以年资得 m"]
>   E --> F["对照同学科参照值"]
> ```

> [!formula-step] 步骤一　计算 h 值
> $$h=\max\{\,i : c_i \ge i\,\}$$
>
> **这个公式在做什么** 输入按被引降序排列的论著被引次数 $c_1 \ge c_2 \ge \dots$，输出满足条件的最大名次 $h$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 17–18)]]
>
> **符号说明** $i$ 为论著排名；$c_i$ 为第 $i$ 篇的被引次数。
>
> **数学直觉** 名次 $i$ 逐个加一，被引次数 $c_i$ 逐个下降，两者相遇的位置就是 $h$。几何上即被引曲线与 45 度对角线 $y=x$ 的交点。
>
> > [!example]- 手算示例
> > 示例：某学者 6 篇论著的被引降序为 25、8、5、4、3、0。第 4 篇被引 4 次，满足 $4 \ge 4$；第 5 篇被引 3 次，不满足 $3 \ge 5$。所以 $h=4$。第 1 篇从 25 次涨到 2500 次，$h$ 仍为 4。
>
> > [!result-reading]- 结果怎么读
> > $h$ 越大，表示被引至少 $h$ 次的论著越多。$h$ 低可能是论著少，也可能是被引少，两种情况要回到原始数据区分。希格斯（Peter Higgs）发表 25 篇、$h=8$，爱因斯坦（Albert Einstein）发表 248 篇、$h=67$，说明 $h$ 偏向持续多产者。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 18–19)]]
>
> > [!method-limits] 参数与注意事项
> > - **超额引用不可见** 论著被引一旦超过 $h$，增加的引用对 $h$ 没有贡献。
> > - **只增不减** $h$ 随时间单调不降，学者停止产出后数值仍保持。

> [!formula-step] 步骤二　线性增长与年资校正
> $$h(t)\approx mt,\qquad m=\frac{1}{1/c+1/n}=\frac{cn}{c+n}$$
>
> **这个公式在做什么** 假设学者每年发表 $n$ 篇论著、每篇每年新增 $c$ 次引用，推出 $h$ 随学术年资 $t$ 线性增长，斜率为 $m$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 18–19)]]
>
> **符号说明** $t$ 为自首篇发表以来的年数；$n$ 为年均发文数；$c$ 为单篇年均新增被引；$m$ 为增长斜率。
>
> **数学直觉** $m$ 是 $c$ 与 $n$ 的调和平均式，小于两者中较小的一个。只提高发文量或只依靠少数高被引论著，都无法明显抬高 $m$。
>
> > [!example]- 手算示例
> > 示例：$n=4$、$c=4$ 时 $m=16/8=2$，10 年后 $h\approx20$；$n=12$、$c=1$ 时 $m=12/13\approx0.9$，10 年后 $h\approx9$。
>
> > [!result-reading]- 结果怎么读
> > 用 $m=h/t$ 可比较不同年资的学者。希尔施给出的物理学经验值为：一般学者 $m\approx1$，优秀学者 $m\approx2$，顶尖学者 $m\approx3$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 18–20)]]
>
> > [!method-limits] 参数与注意事项
> > 模型假设 $n$ 与 $c$ 长期稳定，对中途转向、停顿或早期爆发后停滞的学者不成立。
>
> **动态参数模拟（GeoGebra）** 横轴为年资 $t$，纵轴为 $h$；绿色滑块为 $n$，红色滑块为 $c$，红线为 $h(t)=mt$。拖动滑块可看到 $m$ 受 $n$ 与 $c$ 中较小一方限制。
>
> ```geogebra
> file: wiki/assets/geogebra/hirsch_h_index_v2.ggb
> height: 480
> toolbar: false
> ```

> [!software-impl] 软件实现
> - **数据来源** Web of Science、Scopus、Google Scholar 覆盖范围不同，同一学者的 $h$ 会不同，报告时须注明数据库与检索日期。
> - **消歧** 同名作者合并或拆分错误会直接改变 $h$，需要人工核对作者档案。
> - **核心包或命令** Python `pandas`；R `bibliometrix`。
> - **报告标准** 注明数据库、时间窗、成果类型、是否含自引，以及使用 $h$ 还是年资校正后的 $m$。

> [!formula] Python 计算骨架
> ```python
> def h_index(citations):
>     c = sorted(citations, reverse=True)
>     return sum(1 for i, x in enumerate(c, start=1) if x >= i)
>
> h_index([25, 8, 5, 4, 3, 0])  # 4
> ```

> [!method-stack] 数据口径
> - **数据来源** 不同数据库算出的 $h$ 不可混用。
> - **时间与范围** 生涯全部论著或指定时间窗；是否计入会议论文、专著、预印本。
> - **清洗与归属** 去重、作者消歧、自引处理；合著论著对所有作者等同计入。
> - **标准化** 跨学科比较前需按学科基准归一化，例如 $h_g$ 指数。

---

> [!method-fit] 适用判断
> - **适合使用** 同一学科、相近年资学者之间的累积影响比较，以及对未来产出影响的辅助预测。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 21–23)]]
> - **谨慎使用** 职称晋升与人才评审中作为参照值，须与同行评议和代表作评价结合。
> - **不适合使用** 跨学科直接比较；评价论著很少但有奠基性突破的学者；评价大型合作团队中个人的贡献。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 18–19, 25–26)]]

> [!ref-table]- 参照基准与阈值
> | 情境 | 参照值 | 来源 |
> |---|---|---|
> | 美国主要[[Research Universities\|研究型大学]]物理学长聘副教授 | $h\approx12$ | [[Argument_Wang_Barabasi_2021_Cambridge_Unit01\|Wang & Barabási (2021, pp. 19–20)]] |
> | 同上，正教授 | $h\approx18$ | [[Argument_Wang_Barabasi_2021_Cambridge_Unit01\|Wang & Barabási (2021, pp. 19–20)]] |
> | 美国物理学会会士（APS Fellow） | $h\approx15$–$20$ | [[Argument_Wang_Barabasi_2021_Cambridge_Unit01\|Wang & Barabási (2021, pp. 19–20)]] |
> | [[National Academy of Sciences\|美国国家科学院]]院士 | $h\ge45$ | [[Argument_Wang_Barabasi_2021_Cambridge_Unit01\|Wang & Barabási (2021, pp. 19–20)]] |

---

> [!method-limits] 方法局限
> - **高被引钝感** 超过 $h$ 的引用不计入，奠基性单篇成果被低估。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 25)]]
> - **学科基准差异** 分子生物学的常见 $h$ 高于物理学，物理学又高于数学。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]
> - **偏向资深学者** $h$ 只增不减，年轻学者天然处于劣势。
> - **合著失真** 不区分领衔者、参与者与挂名者，大型团队成员可获得虚高的 $h$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]
> - **误用风险** 把单一指标当作人事决策依据，会忽略教学、指导、评审等无法量化的贡献。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 27)]]
> - **补救方式** 按学科归一化，使用 $m$ 商校正年资，配合 [[g-Index]] 或 $h_\alpha$ 指数，并保留同行评议。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Scientific Productivity]] | 测量对象 | $h$ 把发文数量纳入门槛，反映持续产出能力。 |
> | [[Research Impact]] | 测量对象 | $h$ 以被引次数代表论著的学术影响。 |
> | [[Shockley's Multiplicative Hurdle Model]] | 理论 | 解释科研产出为何高度偏斜，说明 $h$ 的个体差异为何很大。 |
> | [[g-Index]] | 变体 | 以累计被引门槛恢复高被引论著的权重。 |
> | [[Bibliometric Analysis]] | 上位方法 | $h$ 是文献计量分析中的个体层面指标。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit01|Wang & Barabási (2021)]] — 介绍 h 指数的定义、线性增长模型与物理学参照值，用希尔施的纵向数据评估其预测效度，并梳理各类修正指标。
