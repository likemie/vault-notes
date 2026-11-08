---
title: Follow-on Engagement
aliases:
  - 后继学术卷入度
  - 后继研究互动度
  - follow-on paper engagement
  - follow-on scientific engagement
  - EG
summary: "科学计量学中测度同引某项奠基成果的后继文献群体内部交叉引用与学术互动密度的量化指标；以实际发生的相互引用次数占理论最大可能引用次数的百分比计算，反映新兴研究领域是形成网状思想对话还是退化为孤立的中心辐射星状引文拓扑（McMahan & Evans, 2018; Hao et al., 2026）。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 7
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/indicator
  - theme/scientometrics
  - theme/citation-networks
  - theme/science-of-science
related_concepts:
  - "[[Citation Distribution]]"
  - "[[Knowledge Production]]"
related_theories:
  - "[[Matthew Effect in Academia]]"
related_methods:
  - "[[Knowledge Extent]]"
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[James A. Evans]]"
related_facts: []
related_arguments:
  - "[[Argument_Hao_2026_Nature]]"
confidence: high
status: draft
created: 2026-11-08
updated: 2026-11-08
---

> [!def] Follow-on Engagement
> 后继学术卷入度（Follow-on Engagement, EG）是科学计量学中测度共同引用某项基础研究的后继学术文献群体内部交叉引用密度的量化指标。该指标输入一组共同引用基准成果的文献集合，统计这批后继文献之间实际发生的相互引用次数，并除以按发表时间先后可能产生的最大理论引用次数，输出 0% 至 100% 之间的互动比例。[[Argument_Hao_2026_Nature|(Hao et al., 2026, p. 1241)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 测度科学领域的[[Knowledge Production|知识生产]]协作形态、学术共同体内部的思想互动密集度与[[Citation Distribution|引文分布]]网络拓扑结构。
> - **问题类型** 引文网络拓扑结构测度、学术演化阶段诊断与知识流动连通性评价。
> - **分析单位** 单篇基准文献引文家族（Paper Family）、细分学术领域或特定技术门类的后继研究集合。
> - **输入数据** 具备完整参考文献回溯与时间戳记录的学术引文数据库（如 OpenAlex 或 Web of Science）。
> - **输出形式** 百分比数值（0%–100%）。

> [!citation-card] 关键定义
> 测度共同引用前序研究的后续成果之间发生相互引用的紧密程度，用以区分知识生产是形成繁茂交织的学术网络，还是退化为孤立发散的星状引文拓扑。[[Argument_Hao_2026_Nature|(Hao et al., 2026, p. 1241)]]
>
> *To quantify how frequently citations of the same original paper interact with each other, we design a metric called follow-on engagement, building on previous work. This metric helps quantify the degree of interactions and collaboration among papers that cite the same original work.*

---

> [!method-position] 方法定位
> - **构念效度** 指标有效反映了科学共同体内部围绕某一重大突破是否形成了实质性思想交锋与累积性发展；数值极低提示大量后继成果仅将基准成果作为工具化单向引证，缺乏内部互引与理论整合。
> - **研究者判断** 需明确基准文献发表后的追踪时间窗（如 5 年或 10 年），以及是否剔除自身成果引证与同机构团队成员引用的网络口径。
> - **有效性标准** 需结合后继文献在高维语义空间中的距离分布（如 SPECTER 嵌入向量间距）进行双重验证，避免将单纯的引文抱团误读为知识创新。
> - **不声称回答的问题** 指标属于网络拓扑层面的描述性度量，不能单凭互动度高低推断具体某篇文献学术质量优劣。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis|文献计量学]]与复杂网络分析（Network Analysis）。
> - **前置步骤** 确定源头基准文献、提取全量施引文献集合、构建带有时间戳的有向无环引文子图（Citation Directed Acyclic Graph）。
> - **变体与扩展** 包含考虑发表时间先后的有向网络版本，以及仅计算后继文献间无向连边密度的简化图版本。

> [!dev-timeline] 方法演变
> - **2018 — 概念提出** 彼得·麦克马汉（Peter McMahan）与[[James A. Evans|詹姆斯·埃文斯（James A. Evans）]]提出学术卷入度概念，证实理论概念的模糊性与开放性能够激发广泛的后续研究对话与交叉引用。
> - **2026 — 形式化测度与大样本实证** 郝钱跃（Qianyue Hao）等将该指标标准化为公式并应用于 4,130 万篇自然科学出版物，揭示人工智能工具普及导致后继学术卷入度整体萎缩 22%，引文网络蜕化为围绕少数明星成果孤立发散的星状拓扑。[[Argument_Hao_2026_Nature|(Hao et al., 2026, p. 1241)]]

---

> [!formula-step] 步骤一　后继学术卷入度比率计算
> $$EG = \frac{k}{\binom{n}{2}} = \frac{2k}{n(n - 1)} \times 100\%$$
>
> **这个公式在做什么** 计算引用某基准文献的 $n$ 篇后继成果之间实际发生的交叉引用次数 $k$，与理论上可能存在的最大连接数 $\binom{n}{2}$ 之比。[[Argument_Hao_2026_Nature|(Hao et al., 2026, p. 1241)]]
>
> **符号说明**
> - $n$：引用基准成果的后继文献总数。
> - $k$：这 $n$ 篇后继文献之间实际发生的交叉引用总次数。
> - $\binom{n}{2} = \frac{n(n - 1)}{2}$：在无向网络假设或发表时间先后全序下，这批后继文献之间理论上可能发生的最大互引配对总数。
> - $EG$：后继学术卷入度百分比。
>
> **数学直觉** 公式采用经典的图密度（Graph Density）构造逻辑。当后继学者彼此深入研读、辩驳并互相引证时，$k$ 接近最大可能连接数，$EG$ 趋近 100%；当后继学者仅仅各自独立套用该算法而彼此不发生学术对话时，$k$ 接近 0，$EG$ 跌入极低区间。
>
> > [!example]- 手算示例
> > 假设某基准文献共有 $n = 5$ 篇后继引用文献。
> > 理论上可能发生的最大交叉引用配对数为：
> > $$\binom{5}{2} = \frac{5 \times (5 - 1)}{2} = 10$$
> > 经引文网络检索，这 5 篇文献之间实际仅发生了 $k = 1$ 次相互引用。
> > 则后继学术卷入度为：
> > $$EG = \frac{2 \times 1}{5 \times 4} \times 100\% = 10\%$$
> > 该数值表明后继成果之间高度离散，呈现出明显的中心发散型星状结构。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 趋近 100% | 后继研究高度互通，围绕核心议题形成了成熟、致密的学术交流社群。 |
> > | 读法 | 趋近 0% | 后继研究仅单向引用基准成果，彼此之间处于学术孤立状态，呈现星状拓扑。 |
> > | 注意 | 样本规模门槛 | 当 $n$ 极小（如 $n < 3$）时，分母过小易造成数值剧烈波动，需设置最小引用量阈值。 |

> [!software-impl] 软件实现
> - **数据来源** OpenAlex 开放学术图谱或 Web of Science 导出的引文配对边表。
> - **核心包或命令** Python 环境使用 `networkx` 构建子图并计算网络密度，或使用 `numpy` 进行邻接矩阵稀疏运算。
> - **实现流程** 提取基准成果的全部直接被引文献 ID；在全库引文边表中过滤出起点与终点均属于该集合的内部引文边；根据有效节点数 $n$ 与内部边数 $k$ 计算比值。
> - **报告标准** 需同步报告基准文献的发表年份、被引追踪窗口期（如发表后 3 年或 5 年）以及施引文献总数 $n$。

> [!formula] Python 计算骨架
> ```python
> from typing import List, Tuple
> 
> def calculate_follow_on_engagement(citing_papers: List[str], citation_edges: List[Tuple[str, str]]) -> float:
>     """
>     计算后继学术卷入度 (Follow-on Engagement, EG)
>     
>     :param citing_papers: 引用基准文献的所有后继成果 ID 列表
>     :param citation_edges: 后继成果之间实际发生的内部引用边列表 (source, target)
>     :return: EG 百分比数值 (0.0 - 100.0)
>     """
>     n = len(citing_papers)
>     if n < 2:
>         return 0.0
>     
>     # 仅保留两端都在后继成果集合中的内部引用边，并排除自引
>     paper_set = set(citing_papers)
>     valid_edges = [
>         (u, v) for u, v in citation_edges 
>         if u in paper_set and v in paper_set and u != v
>     ]
>     k = len(valid_edges)
>     
>     # 计算最大可能连接数并输出百分比
>     max_possible = (n * (n - 1)) / 2.0
>     eg = (k / max_possible) * 100.0
>     return eg
> 
> # 示例运行
> if __name__ == "__main__":
>     papers = ["P1", "P2", "P3", "P4", "P5"]
>     edges = [("P2", "P1")]  # 仅 1 条内部互引
>     score = calculate_follow_on_engagement(papers, edges)
>     print(f"Follow-on Engagement: {score:.2f}%")  # 输出 10.00%
> ```

> [!method-stack] 数据口径
> - **数据来源** 引文数据库的收录全面性对指标影响显著，数据库若遗漏文献间引用关系会导致 $k$ 被系统性低估。
> - **时间与范围** 需采用统一的发表后时间窗，避免因早期发表的文献有更长时间累积互引而与近期发表文献产生不可比偏差。
> - **清洗与归属** 必须严格剔除直接自引与团队内部互引，防止少数科研团队通过循环互引人为拉高卷入度。

---

> [!method-fit] 适用判断
> - **适合使用** 评估某项重大技术突破或标志性成果在科学共同体中的知识整合效应，对比不同学科领域引文网络的健康程度。[[Argument_Hao_2026_Nature|(Hao et al., 2026, p. 1241)]]
> - **谨慎使用** 被引量极低（如 $n < 5$）的长尾论著，其网络随机性较大，不宜作为核心统计对象。
> - **不适合使用** 跨越数十年历史跨度的非稳态文献群落粗略汇总比较。

> [!ref-table]- 参照基准与阈值
> | 情境 | 参照值 | 来源 |
> |---|---|---|
> | 自然科学常规非 AI 成果引文网络 | 相对基准（100%） | [[Argument_Hao_2026_Nature\|Hao et al. (2026, p. 1241)]] |
> | 自然科学人工智能增强成果引文网络 | 相对基准下降 22%（$t \ge 8.10, p < .001$） | [[Argument_Hao_2026_Nature\|Hao et al. (2026, p. 1241)]] |

---

> [!method-limits] 方法局限
> - **测量偏误** 后继文献的发表存在时间差，晚发表的成果无法被早发表的成果引用，因此未加时间折扣的静态分母在理论上可能偏高。
> - **可比边界** 不同学科的平均引文行为与参考文献列表长度差异显著，跨学科比较时宜使用标准化后的相对降幅或百分位秩次。
> - **误用风险** 不能简单认为卷入度低的研究就缺乏科学价值；部分高度专精或工具性极强的成熟技术套件，其用户群体天然呈现分散使用特征。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Knowledge Production]] | 测量对象 | 本方法测度知识生产过程中的学术互动与协同演进模式。 |
> | [[Citation Distribution]] | 测量对象 | 本方法从网络拓扑微观视角刻画引文分布的连接密集度。 |
> | [[Matthew Effect in Academia]] | 理论 | 解释引文为何向极少数明星成果高度集聚并压抑后继研究互动。 |
> | [[Knowledge Extent]] | 互补方法 | 知识广度测度语义向量空间直径，本方法测度引文网络拓扑互动率。 |
> | [[Bibliometric Analysis]] | 上位方法 | 本方法所属的宏观科学计量学分析方法家族。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Hao_2026_Nature|Hao et al. (2026)]] — 基于 2,334 万篇引用网络实证测算出人工智能辅助成果的后继学术卷入度下降 22%，揭示出科学探索孤岛化与低水平同质化内耗。
