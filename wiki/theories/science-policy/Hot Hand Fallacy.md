---
title: Hot Hand Fallacy
aliases:
  - 热手错觉
  - 手感发热谬误
  - 热手效应论争
  - Hot Hand
  - 连胜错觉
summary: "认知科学、行为经济学与科学学中关于个体在经历连续成功后是否具备持续高成功概率的经典理论争论；托马斯·吉洛维奇与阿莫斯·特沃斯基等人（1985）将其定性为小数定律引发的认知偏误；米勒与桑胡尔霍（2018）在数理统计上证明传统样本计算存在系统性负偏误，证实真实手感在统计上客观存在；该争论直接启迪了科学学探究学术创造力是否存在真实的爆发期机制。"
type: theory
theory_field: "science-policy"
theory_related_count: 5
theory_related_level: 0
theory_related_stars: "☆"
theory_related_color: "#e5e7eb"
tags:
  - theme/science-of-science
  - theme/hot-hand
  - theme/cognitive-bias
  - theme/scientific-career
  - theme/hot-streaks
related_concepts:
  - "[[Hot Streak]]"
related_theories:
  - "[[Hot-Streak Model]]"
  - "[[Random Impact Rule]]"
  - "[[Burstiness in Human Activities]]"
related_methods: []
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit03]]"
confidence: high
status: active
created: "2026-10-30"
updated: 2026-10-30
---

---

> [!theory-position] 理论定位
> - **解释对象** 人类个体在体育竞技、金融决策与科学艺术创新中，连续成功事件之间是否存在正向时间相关性（连胜手感）。
> - **理论问题** 厘清感知中的“状态正佳/手感火热”究竟属于小样本认知错觉，还是服从特定统计机制的客观状态转移。
> - **理论类型** 行为认知理论与时间序列非平稳动力学争论。
> - **知识位置** 横跨认知心理学、行为经济学、数理统计学与科学学，是驱动学者探究学术生涯是否存在[[Hot-Streak Model|爆发期]]的理论触媒。

> [!claim] 核心判断
> 关于连胜状态的学术认知经历了两波深刻演进：1985 年认知心理学将投篮连中判定为由小数定律造成的“热手错觉”（主张命中序列与独立抛硬币几率无异）；2018 年数理统计学纠正了经典研究中的小样本条件概率选择性偏误，证实真实世界中客观存在统计显著的热手效应。科学学研究将这一机制引入学术产出，通过联合概率矩阵证实科学家代表作同样存在局域紧密成簇的客观爆发期。[[Argument_Wang_Barabasi_2021_Cambridge_Unit03|(Wang & Barabási, 2021, pp. 71–72)]]

---

> [!theory-origin] 提出者如何形成理论与半世纪论争
> - **1985 年经典定性：热手错觉假说** 托马斯·吉洛维奇（Thomas Gilovich）、罗伯特·瓦隆（Robert Vallone）与阿莫斯·特沃斯基（Amos Tversky）分析美国职业篮球（NBA）连续投篮数据，指出人们将纯随机序列中的集群现象过度拟合为心理因果，认为所谓手感纯属人类大脑对小样本随机波动的系统性误判。
> - **2018 年统计纠偏：错觉本身的抽样偏误** 统计学家马修·米勒（Matthew Miller）与亚当·桑胡尔霍（Adam Sanjurjo）发现经典文献存在严重的条件概率抽样偏误：在有限长度序列中，前一次命中后下一次命中的真实期望值受制于样本耗尽效应，必然系统性低于无偏概率；校正该偏误后，经验数据有力证实了正向热手效应的客观存在。
> - **科学学的迁移与验证** 王大顺与巴拉巴西以此争论切入科学创造力：如果学术发表严格服从[[Random Impact Rule|随机影响规律]]，则重大突破后理应由于均值回归而回归平庸；但实证数据显示最佳代表作与次佳代表作紧邻出现的概率达随机预期的 1.57 倍，证实科研领域同样存在真实的热手状态。[[Argument_Wang_Barabasi_2021_Cambridge_Unit03|(Wang & Barabási, 2021, pp. 71–74)]]

---

> [!entry-map] 关键概念与理论构件
>
> | 构件 | 类型 | 在理论中的功能 |
> |:-----|:-----|:--------------|
> | 热手错觉（Hot Hand Fallacy） | 心理认知偏误 | 假定人类误将独立的随机波动解读为因果连续性的传统心理学假说。 |
> | 抽样选择偏误 | 统计机制缺陷 | 揭示传统小样本条件概率估计中对连续发生事件计算产生的负向数学偏差。 |
> | 代表作联合概率矩阵 $\phi(N^\ast, N^{\ast\ast})$ | 科学学检验工具 | 量化科研成果序列中头号高峰与次席高峰相对时序共现强度的判定工具。 |
> | [[Hot Streak|学术爆发期]] | 实质状态 | 科学学确立的创造力真实热手形态，体现为数年内代表作的密集落地。 |
> | [[Hot-Streak Model]] | 衍生模型 | 将热手现象在科研全生命周期中形式化表达的动态演化模型。 |
> | [[Random Impact Rule]] | 统计基准 | 热手错觉争论所依托的独立同分布随机零假设。 |
> | [[Burstiness in Human Activities]] | 物理基础 | 为热手成簇提供非泊松时间序列解释的突发动力学理论。 |

---

> [!theory-proposition] 命题一｜抽样选择偏差的修正确立了连胜机制的数理真实性
> **解释** 米勒与桑胡尔霍在数理上证明，在有限投掷试验中，限定前次成功的条件子样本规模必然受到序列截断压制；修正该负偏差后，实际命中概率显著高于独立随机假设，为手感现象提供了坚实的统计学立论基础。[[Argument_Wang_Barabasi_2021_Cambridge_Unit03|(Wang & Barabási, 2021, pp. 71–72)]]

> [!theory-proposition] 命题二｜科研产出的局域时空自相关展现出确凿的爆发期
> **解释** 爱因斯坦 1905 年奇迹年连发 4 篇划时代论著，以及各学科代表作前后脚紧邻诞生的实测数据，证实科研创造力在激发状态下呈现出确凿的真实爆发期，超越了独立无记忆过程的理论预期。[[Argument_Wang_Barabasi_2021_Cambridge_Unit03|(Wang & Barabási, 2021, pp. 71–74)]]

---

> [!theory-boundary] 局限性与适用边界
> - **适合分析** 涉及连续成功感知、有限序列条件概率估计与科研成果成簇涌现的认知/统计争议。
> - **成立条件** 必须依托全样本无偏观测序列与小样本截断偏差修正公式。
> - **不能直接推出** 局部爆发期的客观存在不能直接推翻长期全局维度的均值回归与随机影响基准。

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit03|Wang & Barabási (2021)]] — 结合篮球热手统计偏差修正公案，引申检验科学创造力中的代表作成簇现象。
