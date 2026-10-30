---
title: Citation Distribution
aliases:
  - 引文分布
  - 科学引文分布
  - 论文引文分布
  - 引用分布
summary: "刻画学术出版物群体中随机抽取的一篇论文获得特定引用频次 $c$ 之概率的统计学分布 $P(c)$；由德里克·J·德索拉·普赖斯（Derek J. de Solla Price, 1965）首创测算并确认为具有高方差的肥尾分布（Fat-tailed Distribution），与自然界常见的正态高斯分布呈结构性对立，核心表现为绝大多数论文被引极少而极少数论著吸附海量引用的极化特征。"
type: concept
domain: "science-policy"
related_count: 14
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - theme/science-of-science
  - theme/scientometrics
  - theme/citation-distribution
related_concepts:
  - "[[Citation Disparity]]"
  - "[[Scientific Productivity]]"
  - "[[Big Science]]"
related_theories:
  - "[[Universality of Citation Distributions]]"
  - "[[Price's Law]]"
  - "[[Preferential Attachment in Academia]]"
  - "[[Random Impact Rule]]"
related_methods:
  - "[[Relative Citation Normalization]]"
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[Derek de Solla Price]]"
  - "[[Eugene Garfield]]"
  - "[[Dashun Wang]]"
  - "[[Albert-László Barabási]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit07]]"
confidence: high
status: active
created: "2026-10-30"
updated: 2026-10-30
---

---

> [!def] Citation Distribution
> 引文分布（Citation Distribution）是指用于描述某特定文献集合（如特定学科、期刊或全量数据库）中，随机抽取的一篇学术论文恰好获得 $c$ 次引用的概率函数 $P(c)$。该分布由科学计量学奠基人[[Derek de Solla Price|德里克·J·德索拉·普赖斯]]（Derek J. de Solla Price, 1965）首次基于早期手工引文记录计算并确立。实证表明，学术引文分布不服从经典统计学中的高斯正态对称分布（钟形曲线），而是表现为具有极大方差的重尾或肥尾分布（Fat-tailed Distribution），在宏观上呈现为幂律函数（$P(c) \sim c^{-\gamma}$，其中引文指数 $\gamma \approx 3$）或对数正态函数形态。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, pp. 174–177)]]

> [!concept-lens|notitle] 概念透镜
> - **含义** 标识科学建制中学术承认与注意力资源在宏观出版物全集中的概率分配形态。
> - **用途** 为科学计量学家、政策制定者与学术评估机构提供分析学术成果影响力异质性、识别长尾极端事件以及检验引文增长动力学机制的基础数理模型。
> - **边界** 适用于具有稳定引文积累窗口的同行评议出版物集合；不适用于单个学者终身成果的离散计数，亦不直接等同于瞬时传播维度的网络点击与社交媒体热度（Altmetrics）。

> [!citation-card] 普赖斯关于科学论文引文分布的开创性实证
> 统计数据表明绝大多数已发表论著在后续年份中仅获得微乎其微的引用，而极少数论著却能吸纳极其可观的引文总量。将各被引频次的论文数量绘制在双对数坐标图上，引文频次的概率分布紧密贴合一条斜率约为负三的幂律直线，揭示了引文生成机制本质上是一种不断自我强化的累积优势动态过程。(Price, 1965, pp. 510–515)
>
> *Most papers receive few or no citations, while a tiny fraction of papers amass enormous numbers of citations. Plotting the data reveals that the citation distribution is well approximated by a power law with an exponent close to three, reflecting an underlying cumulative advantage process.*

> [!boundary]- 概念边界
> - 不等于 [[Citation Disparity]]。引文分布是指描述全部概率密度的数理函数全貌（$P(c)$），而引文差距侧重于指称该分布所体现出的头部垄断、零被引堆积与结构性不平等的社会学后果。
> - 不等于单一正态分布。引文分布具有显著的正偏态与超高二阶矩，严禁在未经对数转换或非参数处理的情况下套用标准差、t 检验或普通最小二乘法进行线性回归。
> - 不等同于文献内在科学质量评价。引文分布测量的是学术社群在文本层面的显性引证注意力拓扑，受社交网络连接、学科规模与优先权宣称等多重社会学机制调节。

---

> [!contrast-table|notitle] 概念辨析
> | 维度 | 本概念（[[Citation Distribution]]） | 高斯正态分布（Normal Distribution） | [[Citation Disparity]] |
> |------|--------|----------------|----------------|
> | 数理形态 | 肥尾分布（幂律或对数正态函数） | 对称钟形曲线（围绕均值迅速指数衰减） | 不平等基尼系数与头部份额指标 |
> | 极端值概率 | 极高，存在被引超万次的超级离群奇迹 | 极低，3 倍标准差之外概率几乎为零 | 关注前 1% 成果占总被引的份额比例 |
> | 均值代表性 | 均值无统计代表性，受极端极大值严重拉抬 | 算术均值与中位数重合，具备核心代表性 | 强调均值与中位数的极端偏离事实 |
> | 理论机制 | 优先连接网络动态与自催化累积优势 | 独立同分布微观随机扰动的线性加总 | 科学声望马太效应与注意力稀缺分配 |

---

> [!feature] 核心要素
> - **重尾极化结构（Fat-Tail Property）** 百万量级仅获数次引用的普通论文与少数被引上万次的超级代表作长期共存，方差极大，排斥均值化简化。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, pp. 176–177)]]
> - **双对数坐标线性特征（Log-Log Scale Linearity）** 在双对数坐标系下，幂律引文分布呈现为斜率为 $-\gamma$ 的笔直下降线，直观标识各量级之间尺度不变的无标度拓扑。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, p. 176)]]
> - **帕累托二八法则效应（Pareto 80/20 Rule）** 引文分布高度符合广义帕累托法则，全学科约 80% 的引用总量往往由前 15% 至 20% 的优势成果所吸纳。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, p. 177)]]
> - **对数正态主体拟合（Lognormal Core Fit）** 现代大样本实证表明，针对全部学科论文的主流区间，对数正态公式较纯幂律具有更优秀的参数拟合效度。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, pp. 178–179)]]

> [!logic-map]- 要素关系
> ```mermaid
> flowchart TD
>     A["论文发表总量指数增长"] --> B["学术共同体有限注意力竞争"]
>     B --> C["非对称选择与优先连接机制"]
>     C --> D["引文分布 P(c) 形成"]
>     D --> E["底部：约50%零被引沉没层"]
>     D --> F["中部：均值附近的对数正态主体"]
>     D --> G["顶端：前1%高被引幂律厚尾"]
>     G --> H["[[Citation Disparity|引文差距结构性加剧]]"]
> ```
