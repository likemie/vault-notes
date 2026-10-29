---
title: h-Index
aliases:
  - h指数
  - Hirsch index
  - 希尔施指数
summary: "由 Jorge E. Hirsch (2005) 提出的文献计量评价指标，界定为至多有 h 项成果分别获得至少 h 次引用；通过非线性卷积生产力与被引频次平衡发文总量与长远学术影响，并对学者未来累积成就与新产出成果展现出较强预测效度。"
type: concept
domain: "science-policy"
related_count: 12
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - theme/science-policy
  - theme/scientometrics
  - theme/research-evaluation
  - theme/scientific-career
related_concepts:
  - "[[Scientific Productivity]]"
  - "[[Predictive Validity]]"
  - "[[Research Universities]]"
  - "[[Document]]"
  - "[[Reliability]]"
  - "[[Variable]]"
related_theories: []
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Effect Size]]"
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
> **h 指数（h-Index）**，亦称**希尔施指数（Hirsch index）**，是由物理学家[[Jorge E. Hirsch|乔治·E·希尔施]]（Jorge E. Hirsch）于 2005 年提出的量化测度学者个体累积学术成就的[[Bibliometric Analysis|文献计量学]]指标。一名学者的指数为 $h$，当且仅当在其发表的全部学术论著中，至多有 $h$ 项成果分别获得了至少 $h$ 次学术引用，而其余所有论著的单篇被引次数均未达到 $h$。该指标通过将学者的科研产出数量（生产力）与其论著的被引频次（影响力）进行非线性卷积，旨在克服单纯依赖发文总量或总被引频次所引发的评价偏倚。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 17–18)]]

> [!concept-lens] 概念透镜
> - **含义** $h$ 指数刻画的是学者学术成果中“同时兼具多产性与高关注度”的核心成果集合的边界阈值，在几何图景上对应于按被引频次降序排列的论著位次曲线与 45 度角对角线的交点坐标。
> - **用途** 充当科研管理、终身教职晋升（Tenure）、学会会士当选与院士遴选等人才评审决策中相对客观且稳健的量化参考标尺，并在同行评议中提供学者未来产出卓越度的长程预测线索。
> - **边界** $h$ 指数无法反映突破 $h$ 阈值之后的极端厚尾奠基性成果的额外价值，亦不能自动消除学科领域间由发表规模与引用密度所决定的自然基准落差，更难以单独识别学者在大型科研团队合著成果中的实质智力贡献与学术领导力。

> [!citation-card] 希尔施论科研成就指标的综合建构
> 传统的学术成果评价往往在发文数量与被引总量之间摇摆，前者忽略了成果的实质质量与影响，后者容易受到少数非代表性合著论著或高被引综述的严重扭曲。h 指数通过界定兼具数量与质量的稳健阈值，成功避开了常规指标的内生缺陷，为量化衡量不同学者整体学术成就提供了简明而高效的基准工具。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 21–22)]]
>
> *The key advantage of the h-index is that it sidesteps all of the disadvantages of the metrics... it gives an easy but relatively accurate estimate of an individual's overall scientific achievements.*

> [!boundary]- 概念边界
> - 不等于 发文总量（$N$）— 发文总量仅反映学者的[[Scientific Productivity|科研生产力]]与知识释放速度，完全脱离了学术共同体对成果的后续检验与引用反馈。
> - 不等于 总被引频次（$C$）— 总被引频次反映学者的名义总影响，但极端依赖少数爆款论著，且极易因挂名合著高被引综述而被人为放大。
> - 不等于 篇均被引频次（$C/N$）— 篇均被引频次对低产但在单篇爆发的年轻学者过度优待，在长程科研追踪中是预测未来表现最不可靠的指标。

---

> [!contrast-table] 核心评价指标的多维辨析
> | 评价指标 | 测度维度 | 核心优势 | 结构缺陷与扭曲风险 |
> |---|---|---|---|
> | **h 指数（h-Index）** | 生产力与影响力的非线性卷积 | 兼顾稳健性与产出质量，不为单篇偶然爆款所左右 | 忽视超过 $h$ 的极端突破贡献，无法反映团队分工 |
> | **发文总量（$N$）** | 纯粹科研生产速率 | 直观反映学者工作负荷与知识增殖节奏 | 忽视成果质量，易诱发切香肠式碎化发表与挂名搭便车 |
> | **总被引频次（$C$）** | 学术成果累积名义影响 | 捕捉成果在学术网络中的总体传播广度 | 易受单篇超高被引成果过度拉抬，掩盖常态平庸 |
> | **篇均被引频次（$C/N$）** | 成果平均影响强度 | 消除学术年资与发文数量带来的累积不均等 | 样本基数过小易出现极端偏倚，长期[[Predictive Validity\|预测效度]]最差 |

---

> [!feature] 核心要素
> - **几何交点与非线性卷积界定** 将学者全部出版物按照被引次数从高到低排列绘制曲线，该单调递减曲线与第一象限 45 度角平分线（$y = x$）的交点整数即为 $h$ 值。低于 $h$ 次被引的尾部成果以及高于 $h$ 次的超额被引均不改变该数值。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 17–18)]]
> - **时间演化线性生长模型** 假定学者年均产出 $n$ 项成果且每项每年获得 $c$ 次新引用，则随学术年资 $t$ 推进的指标服从线性关系 $h(t) \approx mt$，斜率 $m = \frac{1}{1/c + 1/n}$ 综合表征了学者的学术精进速率。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 18–19)]]
> - **职业生涯晋升的经验标尺** 在北美[[Research Universities|研究型大学]]物理学界，晋升长聘副教授的典型参考阈值对应 $h \approx 12$；正教授晋升对应 $h \approx 18$；当选美国物理学会会士通常需达到 $h \approx 15–20$；当选[[National Academy of Sciences|美国国家科学院]]院士的门槛通常在 $h \ge 45$ 以上。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 19–20)]]
> - **厚尾高被引修正指标** 针对 $h$ 指数无视顶尖突破成果的缺陷，学界提出了 $g$ 指数（至多 $g$ 项成果累计被引达 $g^2$ 次）、$o$ 指数（最高被引单篇被引量 $c^*$ 与 $h$ 的几何平均值 $o = \sqrt{c^* h}$）以及 $a$ 指数等变体进行补充。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]
> - **团队学术引领力修正（$h_\alpha$ 指数）** 针对团队科研中合著搭便车现象，希尔施提出的 $h_\alpha$ 指数限定仅统计学者作为合著团队中拥有最高 $h$ 指数的资深领军者代表作，高 $h$ 伴随高 $h_\alpha/h$ 比例构成了学术领导力的量化标志。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]

---

## 围绕概念形成的命题

### 命题一　h 指数通过非线性卷积发文量与被引量克服了单纯生产力或单一高被引成果的统计偏误

> [!concept-lens] 评价指标的稳健性与抗噪机制
> 围绕单项[[Document|文献]]计量指标能否兼顾学者的常态化产出与实质知识贡献展开，学界倾向于通过非线性交叉抑制极端离群值的干扰。

> [!claim] Hirsch (2005)
> **多维卷积与抗干扰性** 科学家的学术造诣体现为科研生产力与长远影响力的深度复合。单纯发文量忽视了研究的实质质量，而总被引量容易被少数合著爆款或综述论著严重扭曲。$h$ 指数要求入选的核心成果群必须同时具备数量和引用双重门槛，既排除了发表大量低影响碎片成果造成的生产力虚胖，又过滤掉了学者偶然参与单篇热门研究所带来的虚假学术繁荣，为衡量学者的持续学术贡献提供了稳健评价基准。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 17–18, 21–22)]]

---

### 命题二　h 指数随学术年资呈现线性增长且能有效预测未来长期累积引用与新增产出成就

> [!concept-lens] 指标的动态演化与长期[[Predictive Validity|预测效度]]
> 探讨早期学术计量指标对学者在职业中期与成熟期学术表现的预测能力，实证检验表明 $h$ 指数在长期预测效度上显著超越传统竞争指标。

> [!claim] Hirsch (2007)
> **前瞻预测效度与线性演化** 在学者个体年均产出与年均单篇被引增量相对稳定的假设下，$h$ 指数随职业年限呈现出清晰的线性上升态势。对凝聚态物理学者开展的长达 24 年的前后对比追踪表明，在学者生涯前 12 年的各项计量指标中，$h$ 指数不仅对未来 24 年的累积总引用表现出极高的统计相关性，更在预测学者未来 12 年内纯新产出成果的影响力时击败了发文总量、总引用量和篇均引用量，成为科研资助机构与高校聘任委员会预判学者未来产出卓越度的最佳指标。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 21–23)]]

---

### 命题三　跨学科引用基准差异与团队科研合著模式对 h 指数的跨领域比较构成结构性制约

> [!concept-lens] 指标的跨领域移植边界与[[Reliability|信度]]衰减
> 考察文献计量指标在跨学科资源配置与复杂科研协作环境中的结构性失真，指出未经学科归一化或未剥离挂名效应的直接比对会产生严重系统性偏倚。

> [!claim] [[Argument_Wang_Barabasi_2021_Cambridge|Wang and Barabási (2021)]]
> **学科与团队制约** $h$ 指数不具备跨学科直接可比性，分子生物学等高引用领域的常态 $h$ 值普遍显著高于物理学，物理学又显著高于数学。跨学科直接比对会系统性惩罚发表周期长或引文基数小的基础学科。此外，随着现代科学加速迈向大规模团队协同，传统 $h$ 指数无法有效鉴别学者在成果署名中的实质贡献，初级研究者与资深名誉挂名者获得同等指标增量，必须结合学科归一化模型（如 $h_g$ 指数）与团队引领力权重（如 $h_\alpha$ 指数）方能恢复其评价信度。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]

---

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **稳健评价机制** | 卷积产出数量与被引频次以规避单维偏误 | 学者常态化同行评议与代表作评估 | Hirsch (2005) |
> | **长期预测效度** | 线性演化斜率能有效预测未来新增成果价值 | 终身教职评审与科研基金青年资助甄选 | Hirsch (2007) |
> | **情境制约边界** | 学科基准落差与团队合著搭便车削弱指标有效性 | 跨学科资源竞争与多学者协作团队绩效考核 | [[Argument_Wang_Barabasi_2021_Cambridge\|Wang and Barabási (2021)]] |

---

> [!dev-timeline] 概念演变
> - **2005 — 原始模型提出** 希尔施发表奠基性论著，正式提出 $h$ 指数数学定义与 $h(t) \approx mt$ 线性生长模型，给出物理学长聘与院士经验标尺。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 17–20)]]
> - **2006–2008 — 缺陷修正与变体爆发** 针对厚尾高被引成果的 $g$ 指数（Egghe, 2006）、$o$ 指数，以及针对跨学科引文密度的学科归一化 $h_g$ 指数（Radicchi et al., 2008）相继问世。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]
> - **2007 — 长期预测效度验证** 希尔施基于凝聚态物理学家长达 24 年的纵向引文数据，证实 $h$ 指数对未来新增成果学术影响力的预测效度位居各指标之首。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 21–23)]]
> - **2019 — 合著领导力修正** 希尔施提出 $h_\alpha$ 指数，通过过滤非第一或非资深学者署名成果，专门测度学者在大型团队科研网络中的学术引领地位。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 26)]]

---

> [!warning] 适用局限
> - 绝对指标受到学科引文生态的深刻制约，绝不能跨越生物、物理、工程与人文社会学科直接进行数值横向比较。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 25–26)]]
> - 指数对发表数量极少但单篇具有划时代革命性贡献的巨擘（如仅发表 25 篇论著且 $h = 8$ 的诺贝尔物理学奖得主彼得·希格斯）存在系统性低估。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 18–19)]]
> - 单一量化指标完全无法衡量学者在教学育人、教材编纂、研究生指导、同行评议以及学术社团建设等非文献维度的核心贡献。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 27)]]

---

> [!empirical-divider]

> [!ref-table]- 其他实证结果（无[[Effect Size|效应量]]）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable\|变量]]或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Wang_Barabasi_2021_Cambridge_Unit01\|Wang & Barabási (2021)]] | 凝聚态物理学者样本（前后各 12 年发表记录） | 纵向预测追踪设计 | 指标对未来 12 年总被引量 $C(t_2)$ 及新增成果引用的预测能力 | $h(t_1)$ 与前 12 年总被引 $C(t_1)$ 预测力最强，发文量 $N(t_1)$ 较弱，篇均被引 $C/N$ 表现最差 | 文献报告相关系数散点拟合 | 限于物理学科样本，证实 $h$ 指数对未来产出成就的前瞻预测力 |
> | [[Argument_Wang_Barabasi_2021_Cambridge_Unit01\|Wang & Barabási (2021)]] | 美国[[Research Universities\|研究型大学]]物理学教研人员 | 经验分位数测算与晋升档案追踪 | 职业关键节点对应的 $h$ 阈值 | 长聘副教授 $h \approx 12$；正教授 $h \approx 18$；APS 会士 $h \approx 15–20$；NAS 院士 $h \ge 45$ | 经验经验阈值区间 | 限于北美研究型大学物理学专业，不可直接外推至人文社科 |
> | [[Argument_Wang_Barabasi_2021_Cambridge_Unit01\|Wang & Barabási (2021)]] | 微软学术图谱全量文献库 | 科学家终身计量特征比对 | 卓越科学家代表作被引与终身 $h$ 指数对比 | 爱因斯坦发表 248 篇论著，$h = 67$；希格斯发表 25 篇论著，$h = 8$ | 该书全量数据提取 | 证实 $h$ 指数无法充分表征单篇划时代突破学者的学术地位 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit01|Wang & Barabási (2021)]] — 建立 h 指数的随时间演化生长模型，系统评估其对物理学者未来科研成就的预测效度，并梳理针对厚尾高被引、跨学科基准与团队合著模式的拓展变体。
