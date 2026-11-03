---
title: Citation Aging
aliases:
  - 引文老化
  - 文献老化
  - 知识老化
  - 科学文献老化
  - Obsolescence of Scientific Literature
  - Citation Obsolescence
summary: "指学术文献被同行学术共同体关注并引述的倾向随发表时间的流逝而自然衰减的客观演化规律，表征科学知识的生命周期、注意力半衰期与失效期。早期文献计量学多采用纯指数衰减近似，而现代大数据实证表明带有指数截断的对数正态分布拟合最佳；王-宋-巴拉巴西引文模型由此形式化建立对数正态存活概率函数。实证追踪同时揭示了数字化搜索与同行评议制度对知识老化的显著延缓与逆转趋势（Wang & Barabási, 2021）。"
type: concept
domain: "science-policy"
related_count: 11
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - theme/science-of-science
  - theme/citation-dynamics
  - theme/scientometrics
  - theme/knowledge-decay
related_concepts:
  - "[[Citation Distribution]]"
  - "[[Citation Disparity]]"
  - "[[Sleeping Beauty in Science]]"
  - "[[Literature Search]]"
  - "[[Document]]"
related_theories:
  - "[[WSB Model]]"
related_methods:
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[Dashun Wang]]"
  - "[[Albert-László Barabási]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit09]]"
  - "[[Argument_Fortunato_2018_Science]]"
confidence: high
status: active
created: "2026-11-01"
updated: 2026-11-03
---

---

> [!def] Citation Aging
> 引文老化（Citation Aging，或称文献老化 / 科学知识老化）是指学术出版物在发表之后，随着时间推移其被同行引述的频次与活跃度经历峰值后逐步衰减、直至丧失现实引用价值的动态演化现象。该构念起源于早期文献计量学中关于馆藏期刊剔旧空间的实用考量，并在现代科学学中被形式化提升为刻画学术共同体集体记忆半衰期与知识陈旧更迭速率的基础核心构念。引文老化揭示出科学界显著的“近视性”（myopia）：多数成果在发表两至三年内达到引用高峰并迅速滑落，最终步入几乎不再产生新增引用的“失效期”（expiration date）。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 197–199, 206–207)]]

> [!concept-lens|notitle] 概念透镜
> - **含义** 标识科学成果在时间轴上所遭遇的注意力衰退、知识吸收饱和与范式替代过程。
> - **用途** 用于测定学科知识更新周期、优化高校图书馆数字馆藏资源配置，并在引文分析中消除发表年限造成的积累时滞偏差。
> - **边界** 适用于科技文献全集的宏观统计特征；不能排除经历数十年休眠后突然复苏的“睡美人”非典型反转案例，亦不代表过时文献中所包含的历史经验失去思想价值。

> [!citation-card|notitle] 关键表述
> 科学文献展现出显而易见的近视特征：绝大多数参考文献都指向发表于两到三年之前的近期成果。尽管人们可能认为这是因为近年发表的文献绝对体量远多于早期年代，但即便剔除掉文献指数增长的影响，文献的获引概率依然随时间发生急剧衰减。尽管学者们偶尔会引述发表于二十年以上的历史经典，但引用比这更早研究的几率滑落得极快。这种引文年龄分布生动刻画了科学家的集体信息觅食行为：既严重依赖最新资讯，又偶有节制地依托经受时间检验的经典知识。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 198–199)]]
>
> *The distribution vividly documents the myopic nature of science: most references point to works published just two to three years earlier... even when we account for the exponential growth of literature, the distribution nonetheless decays rapidly with time. While scholars do regularly reach back to "vintage" knowledge more than 20 years old, the likelihood of citing research older than that decays rather quickly.*

> [!boundary]- 概念边界
> - 不等于文献的物理损毁或不可查阅。数字化时代所有历史论著均可随时获取，但其在学术共同体中的实质引证行为依然受到注意力衰减支配。
> - 不等于单纯由发表年限决定的机械折旧。不同学科引文半衰期差异极大，且特定开创性成果会长期维持甚至反弹增长（如睡美人文献）。
> - 区别于成果的“学术错误”。引文老化的核心原因是前沿知识已被后续综述或更简捷的标准工具书“吸纳同化”，同行直接引用更近期的派生成果而不再上溯源头。

---

> [!contrast-table|notitle] 概念辨析
> | 维度 | 引文老化（[[Citation Aging]]） | 引文半衰期（Citation Half-Life） | 引文失效期（Expiration Date） |
> |---|---|---|---|
> | 概念属性 | 描述注意力与引用概率衰退的连续演化过程 | 测度引用量累积达最终总量 50% 的时间尺度 | 判定成果在稳态下停止吸纳新增引用的临界阈值 |
> | 数学模型 | 带有指数截断的对数正态存活分布 $P(t)$ | 累积分布中位数点或经验统计半衰期 | 增量获引率趋近于零的稳态渐近边界 |
> | 核心应用 | 解释注意力衰竭机理与动力学模拟 | 跨学科比较知识周转速率与学科成熟度 | 测定成果全生命周期终极影响的结算窗口 |

---

> [!feature] 核心要素
> - **跳跃衰减形态（Jump-Decay Dynamic）** 成果在发表初期由于同行评议通过与出版传播迅速达峰（2–3 年），随后呈现向下的长尾衰减。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 198, 206)]]
> - **回溯性与前瞻性测度双重视角（Dual Measurement Perspectives）**
>   - **回溯性测量** 以当年度施引论著为锚点统计其参考文献的年龄分布，反映当前学者回溯汲取历史知识的视野深度；
>   - **前瞻性测量** 以发表队列为锚点追踪其在后续年份的新增获引时序，反映学术界遗忘该特定成果的速率。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 204–205)]]
> - **截断对数正态分布拟合（Lognormal with Exponential Cutoff）** 尹良与王大顺（Yin & Wang, 2017）证明，相较于传统纯指数模型，带有指数截断的对数正态分布最能精确拟合全量科技出版物的引文年龄演变。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, p. 199)]]
> - **动力学参数重标度与主曲线坍缩（Dynamic Rescaling & Master Curve Collapse）** 福图纳托等（[[Argument_Fortunato_2018_Science|Fortunato et al., 2018]]）指出，微观层面成果引文老化轨迹呈现异质形态（暴增衰减、延迟达峰、匀速或加速累积），但通过内在适合度 $\lambda_i$、即时性 $\mu_i$ 与衰减寿命 $\sigma_i$ 三参数重标度后，不同学科成果的引文时序曲线完全折叠在跨学科统一的累积分布主曲线上；唯有滞后数十年觉醒的“睡美人”成果突破常规老化预测（pp. 4–5）。
> - **数字化与同行评议的逆转效应（Digital Counter-Aging Effect）** 1967 年同行评议普及与 2000 年代数字全文搜索兴起，显著拉长了学术界的历史搜索深度，促使十年以上老文献的被引份额持续走高。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 203–204)]]

> [!logic-map]- 要素关系
> ```mermaid
> flowchart LR
>     A["文献发表"] --> B["前 2-3 年达峰: 跳跃上升"]
>     B --> C["注意力衰减: 对数正态衰老 P(t)"]
>     C --> D["引文失效期: 停止吸纳新增被引"]
>     E["数字化检索与搜索引擎普及"] --> F["逆转老化: 10 年以上老文献被引份额大幅攀升"]
>     G["同行评议制度引入 (1967)"] --> F
> ```

---

> [!concept-proposition] 命题一｜学术文献获引概率服从带有指数截断的对数正态老化分布
> **知识生命周期函数与时间衰减机理** 探讨微观层面学者注意力的自然消退与宏观引文分布的拟合函数。

> [!claim] [[Argument_Wang_Barabasi_2021_Cambridge_Unit09|Yin & Wang (2017)]]
> **对数正态老化模型的优度检验** 尹良与王大顺检验以往 20 余项文献计量学元分析，指出传统将引文年龄视为纯指数分布的假设存在缺陷；基于当代大样本引文统计证明，带有指数截断的对数正态分布不仅能够准确捕获发表后 2–3 年的峰值跳跃，亦能真实刻画中长期的长尾老化过程。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Yin & Wang, 2017, via Wang & Barabási, 2021, pp. 198–199)]]

> [!claim] [[Argument_Liu_2023_NHB|Liu et al. (2023)]]
> **微观机制模型中的引文老化衰减方程** 刘等人指出，科学学中的生成机制模型将带有指数截断的对数正态引文老化概率函数作为微观基础，与优先连接以及个体适应度方程联立，能够从底层推导并复现复杂引文网络的宏观偏态分布与终极影响力演化轨迹。[[Argument_Liu_2023_NHB|(Liu et al., 2023, pp. 6–7)]]

> [!claim] [[Argument_Fortunato_2018_Science|Fortunato et al. (2018)]]
> **跨学科时序重标度折叠与老化规律普适性** 桑托·福图纳托等论证，微观引文动力学模型通过分别测算成果的质量适合度 $\lambda_i$、即时紧迫度 $\mu_i$ 与衰减寿命 $\sigma_i$，能够精准预测成果全生命周期被引轨迹。在消除学科差异与时间标度后，各领域成果的老化时序轨迹无一例外坍缩至标准正态累积分布主曲线，确立了知识老化的普适统计物理规律。[[Argument_Fortunato_2018_Science|(Fortunato et al., 2018, pp. 4–5)]]

---

> [!concept-proposition] 命题二｜数字化检索与同行评议制度显著延缓并拓宽了学术共同体的历史记忆边界
> **技术可及性与学术制度对知识半衰期的反向塑形** 探讨现代搜索引擎与专业审查制度如何反转知识快速被遗忘的自然老化趋势。

> [!claim] [[Argument_Wang_Barabasi_2021_Cambridge_Unit09|Verstak et al. (2014)]]
> **老旧文献被引份额的结构性复苏** 亚历克斯·韦尔斯塔克（Alex Verstak）等追踪 1990 至 2013 年间发表的数千万篇成果，发现引用 10 年以上老文献的比例呈现持续单调上升趋势，并在 2000 年数字化搜索引擎全面普及后进一步加速。至 2013 年，九大研究领域中有四个领域对十年以上老文献的引用占比突破 40%，人文学科更达 51%，颠覆了“数字化将加剧浅层近视”的悲观预期。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Verstak et al., 2014, via Wang & Barabási, 2021, pp. 203–204)]]

---

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **老化函数分布命题** | 截断对数正态函数精确刻画文献发表全生命周期衰减，驱动微观引文动力学生成 | 成果引文时序拟合、前瞻预测与宏观引文建模 | Yin and Wang (2017); [[Argument_Fortunato_2018_Science\|Fortunato et al. (2018)]]; [[Argument_Liu_2023_NHB\|Liu et al. (2023)]] |
> | **制度与技术逆转命题** | 数字化搜索与同行评议制度拓宽历史经典吸收深度 | 科技基础设施评估、学术数据库建设与图书馆学 | Verstak et al. (2014); [[Argument_Wang_Barabasi_2021_Cambridge\|Wang and Barabási (2021)]] |

---

> [!dev-timeline] 概念演变
> - **1950s–1960s — 图书馆剔旧模型** 早期信息学家提出文献半衰期，主要用于纸质馆藏的空间剔旧管理。
> - **1967 — 同行评议全面推行** 《自然》正式推行同行评议，专家审查促使学者在论著中系统性强化对前人文献的引用深度，推动平均参考文献年龄系统性攀升。
> - **2014 — 数字化逆转老化的全网测定** 谷歌学术团队发现老文献被引占比跨越二十年稳步上升。
> - **2017 — 截断对数正态模型确立** 尹良与王大顺确定了最佳拟合老化概率函数。
> - **2018 — 跨学科引文动力学主曲线坍缩与老化参数分离测度** [[Argument_Fortunato_2018_Science|Fortunato et al. (2018)]] 综述科学学实证进展，证实三参数重标度能够将异质文献的生命周期老化轨迹完全折叠在统一的主曲线上（pp. 4–5）。
> - **2021 — WSB 模型集成** 王大顺与巴拉巴西将对数正态老化确立为引文动力学四大基本公理之一。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 209–212)]]
> - **2023 — 机制模型中的引文老化基石地位确立** [[Argument_Liu_2023_NHB|Liu et al. (2023)]] 系统综述计算科学学进展，将对数正态引文老化衰减与优先连接和适应度模型有机结合，确立了引文动力学生成机制模型的核心微观基石。

---

> [!debates] 学术争议
>
> > [!axis] 超链接致盲狭窄化 vs 数字化全文检索深层化
> > 数字化网络对科研人员的文献汲取是拓宽了历史纵深还是加剧了短期跟风。
> >
> > - **埃文斯（Evans, 2008）超链接狭窄假说** 担忧超链接和网络排名算法使研究者过度集中于少数当代流行热点，削弱翻阅纸本时的偶遇发现机会（serendipity）。
> > - **韦尔斯塔克等（Verstak et al., 2014）实证反驳** 大数据全景表明 10 年以上老文献被引份额自 1990 年以来持续攀升，数字化反而打破了物理图书馆的借阅壁垒，大幅唤醒了深沉经典。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 203–204)]]

> [!warning|limits] 适用局限
> 引文老化受学科范式更迭速度强烈调节；在计算机科学等快速演进的高迭代工程领域，半衰期显著短于数学、历史与人文学科，跨学科对比必须消除学科基准差异。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, p. 204)]]

---

> [!empirical-divider]

> [!ref-table]- 其他实证结果（无效应量）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | 变量或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Wang_Barabasi_2021_Cambridge_Unit09\|Verstak et al. (2014)]] | 1990 至 2013 年间发表的数千万篇科技论著全集 | 纵向年代队列追踪与学科横向切片对比 | 引用至少 10 年前老文献的引文条目占比 | 1990 至 2013 年间老文献被引份额单调稳步上升；至 2013 年 9 大门类中有 4 个领域老文献被引占比超 **40%**，人文学科高达 **51%** | 2000 年数字化搜索兴起后显著加速 | 证实数字化搜索拓宽了学术共同体的集体记忆纵深，反驳了数字浅层化假说 |
> | [[Argument_Wang_Barabasi_2021_Cambridge_Unit09\|Wang & Barabási (2021)]] | 1950 至 2010 年间跨越六十年的学术论著参考文献全集 | 跨历史时期平均参考文献年龄演进追踪 | 论著参考文献平均年龄 $\langle T \rangle$（年） | 1950–1970 年维持在 **7.5 年**；1967 年（《自然》推行同行评议）后开启持续单调攀升，至 2010 年逼近 **10 年**（图 19-3） | 历史时间序列趋势清晰稳健 | 揭示同行评议专业审查制度对强化文献回溯深度的结构性制度塑造 |
> | [[Argument_Wang_Barabasi_2021_Cambridge_Unit09\|Stringer et al. (2008)]] | 1991 至 1993 年间发表于各专门期刊的论著全样本 | 发表后跨越 15 年的长期引文稳态饱和检验 | 成果停止获取新增引文的失效期（Expiration Date）判定 | 1991 年成果至 2006 年几乎完全停止吸纳新引文，其引文分布与 1993 年成果完全等同（图 19-5） | 各期刊达到稳态的时间跨度有所不同但均呈现明确失效期 | 证实单篇成果存在客观的注意力失效期，终极被引趋于确定性稳态 |
| [[Argument_Fortunato_2018_Science\|Fortunato et al. (2018)]] | 《物理评论》1964 年发表成果及跨学科期刊引文时序全集 | 机制模型时序拟合与重标度折叠检验 | 适合度 $\lambda_i$、即时性 $\mu_i$、寿命 $\sigma_i$ 与相对引文轨迹 | 呈现暴增衰减、延迟达峰等异质轨迹的论著，经三参数重标度后 $100\%$ 折叠至单一累积分布主曲线上；绝大多数常规成果均遵循可预测的对数正态老化衰减 | 对数正态主曲线拟合良好；极少数睡美人成果突破常规模型 | 验证了引文老化的统计物理普适性，为基于早期引文参数推演数十年终身影响力提供数理基准 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Fortunato_2018_Science|Fortunato et al. (2018)]] — 综述微观引文动力学模型，阐明通过适合度、即时性与衰减寿命三参数重标度可将异质老化轨迹坍缩至统一对数正态主曲线的物理机制（pp. 4–5）。
> - [[Argument_Liu_2023_NHB|Liu et al. (2023)]] — 系统综述生成机制模型将对数正态引文老化作为微观基础，与优先连接及适应度联立预测学术影响力的数理机制（pp. 6–7）。
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit09|Wang & Barabási (2021)]] — 在专著第 19 章系统探讨引文老化的微观特征、测量视角、对数正态模型及数字化与同行评议对老化的逆转（pp. 197–208）。
