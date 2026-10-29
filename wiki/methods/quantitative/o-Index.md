---
title: o-Index
aliases:
  - o指数
  - Dorogovtsev-Mendes o-Index
  - 几何被引指数
summary: "由 Sergey N. Dorogovtsev 与 José F. F. Mendes (2015) 提出的文献计量指标；定义为学者单篇最高被引次数 c* 与 h 指数的几何均值 o = √(c* · h)，旨在直接恢复划时代极端最高被引突破成果在学者学术评价中的核心权重，兼顾成果影响深远度与产出累积基础。"
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
  - "[[Document]]"
  - "[[Research Impact]]"
  - "[[Unit of Analysis]]"
  - "[[Construct Validity]]"
related_theories: []
related_methods:
  - "[[g-Index]]"
  - "[[h-Index]]"
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[Michael Gove]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit01]]"
confidence: high
status: draft
created: "2026-10-29"
updated: 2026-10-29
---

---

> [!def] o-Index
> **o 指数（o-Index）** 由统计物理学与网络计量学者谢尔盖·N·多罗[[Michael Gove|戈夫]]采夫（Sergey N. Dorogovtsev）与若泽·F·F·门德斯（José F. F. Mendes）于 2015 年提出，是量化测度学者累积学术影响的复合[[Document|文献]]计量指标。其计算规则为学者单篇最高被引频次 $c^*$ 与其 $h$ 指数的几何平均值 $o = \sqrt{c^* \cdot h}$，通过将超级离群峰值与中枢成果群规模卷积合成，直接修复 $h$ 指数对划时代最高被引代表作视而不见的结构性缺陷。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 25)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 学者顶级代表作学术突破力度与多产稳健性的复合学术影响，对应 [[Research Impact]]。
> - **问题类型** 评估与比较拥有划时代单篇高被引突破成果学者的学术成就。
> - **[[Unit of Analysis|分析单位]]** 学者个体，或独立实验室团队。
> - **输入数据** 学者全部学术论著的逐篇被引频次集合，要求已完成著者身份数据消歧。
> - **输出形式** 连续正实数 $o$（通常四舍五入为一位小数或整数），由于 $c^* \ge h$，恒有 $o \ge h$。

> [!citation-card] 最高被引成果对学术生涯的定义力
> h 指数的主要优势在于其数值不会被单次偶发成功所抬高，但这也意味着它完全忽视了研究者最具影响力的标志性工作。一旦论著被引量跨越 h 门槛，其超额重要性在 h 指数中彻底隐形。然而，离群代表作往往定义了学者的整个职业生涯，更在实质上定义了科学探索本身。为此学界提出了 g 指数以及结合最高被引量与 h 指数几何均值的 o 指数等指标加以修正。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 25)]]
>
> *Outlier papers frequently define careers, they arguably are what define science itself. Many remedies have been proposed to correct for this, including the [[g-Index|g-index]] and the o-index (the geometric mean of the number of citations gleaned by a scientist's highest cited papers c* and her [[h-Index|h-index]]: o = sqrt(c* · h)).*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 采用几何均值将单篇最高被引 $c^*$ 纳入评价，保留了极值代表作的突破信息，同时借助开方衰减抑制纯粹偶然单篇爆款对整体指标的过度拉升。
> - **研究者判断** 学科引文环境校正方式、合著署名贡献折算比例以及数据库收录时间窗口。
> - **有效性标准** 区分少产突破型学者（如仅有 25 篇论著但包含划时代希格斯玻色子理论的学者）与高产平庸型学者的鉴别效度。
> - **不声称回答的问题** 不能直接替代同行评议对学术代表作实质创新的研读，亦不能跨越不同学科天然的引文体量鸿沟直接进行绝对数值排序。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis]]。
> - **基础指标** [[h-Index]]：作为表征学者中枢代表作规模的基准输入项。
> - **同构衍生指标** [[g-Index]]（累积平方求和阈值修正）、$h_\alpha$ 指数（资深学术引领力修正）。

---

> [!formula-step] 计算 o 指数
> $$o = \sqrt{c^* \cdot h}$$
>
> **这个公式在做什么** 接收学者全部发表论著中的单篇最高引用次数 $c^*$ 与根据引文序列计算得到的 $h$ 指数，计算两者的几何乘积平方根，输出复合评价指数 $o$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 25)]]
>
> **符号说明**
> - $c^*$：学者毕生发表论著中单篇最高被引频次；
> - $h$：学者基于全部论著计算所得的标准 $h$ 指数；
> - $o$：多罗戈夫采夫-门德斯复合影响指数。
>
> **数学直觉** 几何均值在量纲上等同于边长为 $\sqrt{c^* \cdot h}$ 的正方形面积等价边长。若仅依赖算术平均，万次引用的单篇文献会彻底淹没中枢产出；开方运算对极端值施加对数尺度的压缩，使单篇突破的极端优势能够以可控比例反馈到学术造诣测度中。
>
> > [!example]- 手算示例
> > 示例对比两类典型科研人员：
> > - **类型 A（少产但有划时代突破）** 学者发表 25 篇论著，由于篇数有限，$h = 8$；但其代表作单篇最高被引高达 $c^* = 14,000$ 次（如 Peter Higgs 案例）。其 $o$ 指数为：
> >   $$o_A = \sqrt{14000 \times 8} = \sqrt{112000} \approx 334.7$$
> > - **类型 B（多产但缺乏顶级突破）** 学者发表 150 篇论著，$h = 25$；但单篇最高被引仅为 $c^* = 100$ 次。其 $o$ 指数为：
> >   $$o_B = \sqrt{100 \times 25} = \sqrt{2500} = 50.0$$
> > 
> > 传统 $h$ 指数判定 $B > A$（$25$ 远高于 $8$），彻底掩盖了学者 A 取得诺贝尔奖级奠基突破的事实；而 $o$ 指数判定 $A > B$（$334.7$ 远高于 $50.0$），公允体现出顶级离群突破在科学演进中的主导地位。
>
> > [!formula-reading] 结果解读与注意事项
> > | 维度 | 判读要点 | 说明 |
> > |---|---|---|
> > | **比值 $o / h$** | 突破离群度诊断 | $o / h = \sqrt{c^* / h}$；比值显著大于 1 表明学者存在远超中枢水平的超级突破代表作；比值接近 1 表明学者产出均衡平缓。 |
> > | **单篇依赖风险** | 偶然合著爆款干扰 | 若学者仅在大科学国际工程中挂名一篇超高引论著，而自身独立产出极少，单独报告 $o$ 指数会产生虚高偏误。 |

> [!formula] Python 计算骨架
> ```python
> import math
> 
> def o_index(citations):
>     """计算学者引文序列的 o 指数"""
>     if not citations:
>         return 0.0
>     c_sorted = sorted(citations, reverse=True)
>     # 计算 h 指数
>     h = 0
>     for i, cit in enumerate(c_sorted, start=1):
>         if cit >= i:
>             h = i
>         else:
>             break
>     c_star = c_sorted[0]
>     return round(math.sqrt(c_star * h), 2)
> 
> # Higgs 示例：单篇 14000 引，h 指数 8
> print(o_index([14000] + [8]*7 + [5]*17))  # 334.66
> ```

---

> [!method-fit] 适用判断
> - **适合使用** 顶尖学术荣誉遴选、终身成就奖评选与科学突破型人才遴选；与 $h$ 指数形成互补双轴，防范对精耕细作但成果较少学者的误杀。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 24–25)]]
> - **不适合使用** 常态化高校青年教师日常绩效评估，或直接跨学科横向划定经费资助门槛。

> [!method-limits] 方法局限
> - **极端值鲁棒性相对较弱** 相较于 $h$ 指数对单篇成果的完全免疫，$o$ 指数直接绑定单篇极值 $c^*$，容易受单篇偶发性高被引论著（如争议性撤稿成果或大型协作组挂名）的冲击。
> - **学科引用密度落差** 生物医学与高能物理学界的单篇峰值引文动辄数万，而数学与理论物理峰值通常在数百量级，未归一化的 $o$ 指数在学科交叉比较时存在系统性偏差。

---

> [!entry-map] 条目关联
>
> | 条目 | 类型 | 贡献 |
> |:-----|:-----|:-----|
> | [[h-Index]] | 基础指标 | 作为 $o$ 指数公式的组成部分与中枢生产力标尺。 |
> | [[g-Index]] | 同行指标 | 共同构成文献计量学修复 $h$ 指数忽略超额被引的两大经典数学方案。 |
> | [[Research Impact]] | 测量对象 | $o$ 指数将学术影响力测度由中枢均衡拓展至极端重大突破维度。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit01|Wang & Barabási (2021)]] — 在系统评述 h 指数局限性的专节中，将 o 指数与 g 指数并列引述为恢复极端突破成果权重的代表性衍生计量模型。
