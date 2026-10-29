---
title: Price's Law
aliases:
  - 普赖斯定律
  - 普赖斯平方根定律
  - 普莱斯定律
  - Price's Square Root Law
  - Square Root Law of Scientific Productivity
summary: "由 Derek de Solla Price (1963) 在《小科学，大科学》中提出的科学计量学经验分布定律；指出在特定学术共同体中，全部学术文献的 50% 由总学术人口的平方根（k = √N）贡献，揭示了科研知识生产中极端精英集中的平方根分布特征与学术分层结构。"
type: theory
theory_field: "science-policy"
theory_related_count: 13
theory_related_level: 1
theory_related_stars: "⭐"
theory_related_color: "#dbeafe"
tags:
  - theme/science-policy
  - theme/scientometrics
  - theme/productivity
  - theory/scientific-career
related_concepts:
  - "[[Document]]"
  - "[[Scientific Productivity]]"
  - "[[Comparative Education as a Cross-Sectional Area]]"
  - "[[Big Science]]"
  - "[[Knowledge Production]]"
  - "[[Heterogeneity]]"
related_theories:
  - "[[Lotka's Law]]"
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Shockley's Multiplicative Hurdle Model]]"
related_instruments: []
related_persons:
  - "[[Derek de Solla Price]]"
  - "[[Alfred J. Lotka]]"
related_facts:
  - "[[The Royal Society]]"
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit01]]"
confidence: high
status: draft
created: "2026-10-29"
updated: 2026-10-30
---

---

> [!theory-position] 理论定位
> - **解释对象** 解释全学科领域中科学共同体内部发表成果的极端分层与[[Document|文献]]集中度，揭示知识产出高度凝聚于微小精英子集的人口学规律。
> - **理论问题** 回应[[Scientific Productivity|学术生产力]]在学科规模扩张过程中如何分布的实证测算问题，判定总人口增长是否伴随高产群体的同步扩张。
> - **理论类型** 文献计量经验分布定律、宏观产出平方根模型。
> - **知识位置** 处于[[Bibliometric Analysis|科学计量学]]、科学社会学与科研人力资源政策的[[Comparative Education as a Cross-Sectional Area|交叉领域]]，与[[Lotka's Law|洛特卡定律]]及[[Shockley's Multiplicative Hurdle Model|肖克利乘法跨栏模型]]共同构成学术生产力分布的核心理论矩阵。

> [!claim] 核心判断
> 在特定学科或学术共同体内，若有效发表成果的学者总人数为 $N$、产出的文献总量为 $M$，则生产全部文献半数（$0.5M$）的核心高产学者规模 $k$ 近似等于总人数的平方根：
> $$k \approx \sqrt{N}$$
> 这一规律意味着当科研人口随[[Big Science|大科学]]时代指数级膨胀时，贡献主要科学进展的核心精英群体仅按平方根速率低速增长，绝大多数研究人员终生处于长尾边缘。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 10)]]

> [!geogebra] [[Derek de Solla Price|普赖斯]]平方根定律与精英规模演化模拟
> - **横轴** 总学术人口 $N$（人）
> - **纵轴** 生产半数文献的核心学者规模 $k$（人）
> - **滑块 N** 调节学科或机构总学术人口（从 100 增至 2500）
> - **青线** 普赖斯平方根定律曲线 $k = \sqrt{N}$
> - **灰虚线** 10% 线性等比参照线
>
> 调节滑块可直观验证：当学术人口从百人小科学膨胀至数千人大科学时，生产半数文献的核心精英规模仅按平方根低速增长，其在总体人口中的相对比重从 10% 迅速稀释至 2%，印证大科学时代人均核心产出的结构性稀释。
>
> ![[wiki/assets/geogebra/price_law_elite.ggb|480]]

---

> [!theory-origin] 提出者如何形成理论
> - **提出者与原始文本** 由科学计量学奠基人德里克·约翰·德索拉·普赖斯（Derek de Solla Price）于 1963 年在哥伦比亚大学出版的奠基著作《小科学，大科学》（*Little Science, Big Science*）中正式提出。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 10)]]
> - **原初问题** 普赖斯关注 20 世纪科学事业由小规模业余探索转向国家级建制化大科学过程中，科学家队伍呈现指数级扩张的同时，人均产出与核心精英规模如何演变的数量规律。
> - **理论资源与材料** 普赖斯以[[The Royal Society|皇家学会]]会刊长期产出记录及《伦敦皇家学会科学文献目录》（Catalogue of Scientific Papers）为经验样本，并结合[[Alfred J. Lotka|洛特卡]]反平方幂律分布的积分连续化推导。
> - **形成路径** 通过对发文频次曲线在高端产出区间进行积分求和，普赖斯推导出高产学者群体对总量贡献的临界截断点，提炼出半数文献产出对应 $\sqrt{N}$ 核心人数的紧凑平方根法则。

---

> [!entry-map] 关键概念与理论构件
>
> | 构件 | 类型 | 在理论中的功能 |
> |:-----|:-----|:--------------|
> | [[Scientific Productivity]] | 概念 | 界定考察对象为学者在特定统计周期内发表的经过同行评议的学术文献总量。 |
> | 学科总人口规模（$N$） | 参数 | 表征特定学科或机构内至少发表过一篇学术文献的全部有效研究人员总数。 |
> | 平方根核心群体（$k = \sqrt{N}$） | 阈值 | 界定生产该领域半数学术文献的领军研究者集体的规模边界。 |
> | 50% 产出集中度截断点 | 机制 | 建立产出累积份额与人力构成的定量分割基准，反映[[Knowledge Production\|知识生产]]的精英化程度。 |

---

> [!theory-proposition] 命题一｜学术文献半数产出由总科研人口的平方根精英群体所主导
> **解释** 普赖斯通过实证拟合证明，科学知识生产呈现极度的不对称性。在总体规模为 $N$ 的科研领域中，将全部学者按发表总量降序排列，排名前 $k = \sqrt{N}$ 的学者累计产出达到全部文献量的 $50\%$。例如在拥有 10,000 名有效发表学者的学科内，仅需约 100 位核心顶尖学者即可产出半数学术论著，而其余 9,900 名学者共同分摊剩余的 $50\%$ 产出。该命题确立了学术共同体内知识生产的高度集中特征。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 10)]]
>
> **应用实例** 在高校与国家实验室编制规划中，普赖斯定律说明试图通过盲目扩招普通科研人员来实现学科生产力成倍增长的边际效益递减，建设具有高生产力引领力的领军团队是提升机构核心产出的关键支撑。

> [!theory-proposition] 命题二｜学术共同体规模膨胀导致人均高阶贡献率的结构性稀释
> **解释** 普赖斯定律表明，随着科学共同体总体规模 $N$ 的扩张，核心领军学者群体 $k$ 的增长速度严格受制于平方根函数 $\sqrt{N}$。当学科总人口扩大 100 倍时，核心贡献者队伍仅扩大 10 倍，导致核心精英占总人口的相对比重从 $\frac{1}{\sqrt{N}}$ 持续下行。这一结构性矛盾表明，大科学时代科研队伍的指数增长并未伴随等比例的顶尖产出者扩充，绝大多数学术后继者主要承担细分验证、方法完善与长尾补充性工作。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 10)]]
>
> **应用实例** 在新兴学科布局中，新设学位点与研究生招生规模的爆发式扩张如果缺乏相应顶尖导师团队的支撑，会导致毕业生与青年学者中单篇发文边缘群体的堆积，拉低人均学术产出指标。

---

> [!tension] 普赖斯定律与洛特卡定律的模型关系
> - **洛特卡反平方幂律** 侧重描述全样本学者发文频次的连续概率分布形态 $P(N) = C / N^\alpha$（$\alpha \approx 2$），强调底层单篇发表者占比约 $60\%$ 的微观结构。
> - **普赖斯平方根定律** 侧重提供宏观决策截断指标，将洛特卡分布在高端产出区间进行累积积分，转化为 $k = \sqrt{N}$ 贡献 $50\%$ 成果的简洁运营法则，更直接服务于科研人力评估与文献资源采购策略。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 10–12)]]

---

> [!theory-boundary] 局限性与适用边界
> - **适合分析** 适用于具有成熟发表规范、单兵探索或小团队署名为主的传统学科基础研究产出统计。
> - **成立条件** 依赖于大规模历史文献样本库（通常要求 $N \ge 100$）且学科边界界定清晰。
> - **解释不足** 在当今高能物理、基因组测序等跨国超大型科研协作项目中，单篇文献署名人员成百上千，简单的单人发文计数无法反映真实的知识产权归属，导致平方根定律在巨型团队协作中出现测算偏差。

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit01|Wang & Barabási (2021)]] — 结合近百年 5,300 万研究者与 9,000 万篇文献大数据，重估普赖斯定律在现代科学体系中的有效性与学科[[Heterogeneity|异质性]]。
