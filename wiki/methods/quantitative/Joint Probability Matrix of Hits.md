---
title: Joint Probability Matrix of Hits
aliases:
  - 代表作联合发生概率矩阵
  - 代表作联合概率矩阵
  - 代表作共现概率矩阵
  - Hit Co-location Matrix
  - Joint Probability Distribution of Hits
summary: "科学学与创造力计量中量化个体职业生涯中高影响代表作时序成簇自相关特征的二维离散检验矩阵；通过比对观测序列中最佳代表作与次佳代表作的联合发生概率与生涯洗牌零模型基准的比值，诊断创造力爆发在全生涯序列中是否偏离独立无偏随机假设；实测显示矩阵沿主对角线显著隆起，紧邻发表概率达随机预期的1.57倍，构成了确立学术爆发期模型的核心实证计量工具。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 23
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/statistical
  - theme/science-of-science
  - theme/hot-streaks
  - theme/scientometrics
related_concepts:
  - "[[Null Hypothesis]]"
  - "[[Hot Streak]]"
  - "[[Creativity]]"
  - "[[Unit of Analysis]]"
  - "[[Construct Validity]]"
  - "[[Emergence]]"
  - "[[Metascience]]"
  - "[[Paradigm]]"
  - "[[Document]]"
  - "[[Variable]]"
  - "[[Construct]]"
related_theories:
  - "[[Random Impact Rule]]"
  - "[[Hot-Streak Model]]"
related_methods:
  - "[[Statistical Significance]]"
  - "[[Bibliometric Analysis]]"
  - "[[Career Shuffling Method]]"
related_instruments: []
related_persons:
  - "[[Roberta Sinatra]]"
  - "[[Lu Liu]]"
  - "[[Dashun Wang]]"
  - "[[Albert-László Barabási]]"
related_facts:
  - "[[Victorian HITS and Literacy Toolkit]]"
  - "[[Microsoft Academic Graph]]"
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit03]]"
confidence: high
status: active
created: 2026-10-30
updated: 2026-10-31
---

---

> [!def] Joint Probability Matrix of Hits
> 代表作联合发生概率矩阵（Joint Probability Matrix of [[Victorian HITS and Literacy Toolkit|Hits]]，$\phi(N^\ast, N^{\ast\ast})$）是科学学中用于检验学者、艺术家及电影导演全生命周期产出序列中顶级代表作是否具有时序自相关成簇特征的量化检验矩阵。通过统计个体最高被引论著（第 $N^\ast$ 篇）与次高被引论著（第 $N^{\ast\ast}$ 篇）在全产生涯序列中同时出现的经验联合概率分布 $P(N^\ast, N^{\ast\ast})$，并除以基于生涯洗牌法置换生成的独立随机[[Null Hypothesis|零假设]]期望 $P_{\text{rand}}(N^\ast, N^{\ast\ast})$，输出归一化比值矩阵 $\phi(N^\ast, N^{\ast\ast})$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit03|(Wang & Barabási, 2021, pp. 72–74)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 测度个体学术生涯中的成果时序自相关性与[[Hot Streak|学术爆发期]]成簇强度。
> - **问题类型** [[Creativity|创造力]]动力学中的随机过程检验、时序自相关诊断与局部成簇识别。
> - **[[Unit of Analysis|分析单位]]** 具有长周期发表记录（通常产出成果数 $N \ge 20$）的学者、艺术家或电影导演个体全序列。
> - **输入数据** 个体全生命周期发表成果的时间时序排列、各成果的十年被引频次（$c_{10}$）或拍卖成交额/IMDb 评分。
> - **输出形式** 二维实数归一化概率比值矩阵 $\phi \in \mathbb{R}^{N \times N}$ 及热力图。

> [!citation-card] 关键定义
> 为了检验代表作是否在时间上成簇出现，研究团队计算了个体最佳成果 $N^\ast$ 与次佳成果 $N^{\ast\ast}$ 在归一化职业时序中的联合概率分布 $P(N^\ast, N^{\ast\ast})$。通过将其与发文次序随机重组的零模型预期 $P_{\text{rand}}(N^\ast, N^{\ast\ast})$ 比对，构建了比值矩阵 $\phi(N^\ast, N^{\ast\ast})$。如果成果出现完全服从[[Random Impact Rule|随机影响法则]]，矩阵各处取值应近似为 1；然而经验数据在沿对角线区域展现出强烈的红色峰值（$\phi > 1$），证实最佳成果紧邻诞生的几率显著超越随机预期。[[Argument_Wang_Barabasi_2021_Cambridge_Unit03|(Wang & Barabási, 2021, pp. 72–74)]]
>
> *To test whether hits cluster in time, we measured the joint probability distribution P(N*, N**) of the timing of the top two hits... and compared it to the expectation from a random null model where the timing of hits is uncorrelated.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 直接从时序拓扑距离切入，有效捕捉了成果影响力在时间轴上的局域聚集，但未包含成果的具体内容语义关联。
> - **研究者判断** 选取考量极值成果的数量（如前 2 大代表作还是前 3 大代表作），以及归一化时序分箱（Binning）区间的划定。
> - **有效性标准** 对角线离差检验的[[Statistical Significance|统计显著性]]、跨学科跨领域的稳健复现性。
> - **不声称回答的问题** 矩阵本身是描述性与诊断性检验工具，度量时序聚集的强弱，不能单独解释爆发期[[Emergence|涌现]]的微观认知因果机制。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis]]（文献计量分析）、时间序列点过程统计。
> - **前置步骤** 学者成果同名消歧、全生命周期发表记录排序、长窗口引文标准化。
> - **依赖基准** [[Career Shuffling Method]]（生成分母独立零模型的置换洗牌法）。
> - **变体与扩展** 扩展至第三高峰代表作的三维张量 $\phi(N^\ast, N^{\ast\ast}, N^{\ast\ast\ast})$，或基于相对生涯进度 $n^\ast = N^\ast / N$ 的连续概率密度比值曲面。

> [!dev-timeline] 方法演变
> - **2016 — 随机影响法则与独立基准确立** [[Roberta Sinatra]] et al. 提出随机影响规律，确立单篇成果在全生涯服从均匀抽样，为联合矩阵提供了基线零假设。
> - **2018 — 《自然》刊载成果正式提出代表作联合概率矩阵** [[Lu Liu|刘路]]、[[Dashun Wang|王大顺]]与[[Albert-László Barabási|艾伯特-拉斯洛·巴拉巴西]]发明归一化联合概率矩阵 $\phi(N^\ast, N^{\ast\ast})$，首次在大样本实证中量化证实对角线峰值达到 1.57 倍，为学术爆发期提供首要实证支柱。[[Argument_Wang_Barabasi_2021_Cambridge_Unit03|(Wang & Barabási, 2021, pp. 72–74)]]
> - **2021 — 科学学专著系统推广** 王大顺与巴拉巴西在《[[Metascience|科学的科学]]》专著中将该矩阵列为检验科研、艺术与影视跨界创造力动力学的标准诊断[[Paradigm|范式]]。

---

> [!formula-set]- 公式链总览
> ```mermaid
> flowchart LR
>   A["个体全生涯成果时序序列"] --> B["识别最高被引 N* 与次高被引 N**"]
>   B --> C["统计经验联合概率 P(N*, N**)"]
>   A --> D["生涯洗牌法打乱引文次序"]
>   D --> E["生成零模型独立基准 Prand"]
>   C & E --> F["比值归一化矩阵 phi(N*, N**) = P / Prand"]
>   F --> G["绘制热力图并检验对角线离差峰值"]
> ```

> [!formula-step] 步骤一　归一化联合概率矩阵计算
> $$\phi(N^\ast, N^{\ast\ast}) = \frac{P(N^\ast, N^{\ast\ast})}{P_{\text{rand}}(N^\ast, N^{\ast\ast})}$$
>
> **这个公式在做什么** 输入跨个体全量发表成果中头两大代表作的出现位置，通过除以无记忆独立随机置换基准，输出排除个体发文总量差异后的代表作时序共现倍率。[[Argument_Wang_Barabasi_2021_Cambridge_Unit03|(Wang & Barabási, 2021, pp. 72–74)]]
>
> **符号说明**
> - $N^\ast$：个体学者全生命周期中被引最高的第一代表作在发表序列中的绝对次序（或相对进度 $n^\ast = N^\ast / N$）。
> - $N^{\ast\ast}$：个体学者第二高被引代表作在序列中的次序（满足 $N^{\ast\ast} \neq N^\ast$）。
> - $P(N^\ast, N^{\ast\ast})$：在全样本个体中观测到头两大代表作分别落于位置 $N^\ast$ 与 $N^{\ast\ast}$ 的联合经验概率。
> - $P_{\text{rand}}(N^\ast, N^{\ast\ast})$：由随机影响法则推导的理论独立分布；在离散序列中 $P_{\text{rand}} = \frac{1}{N(N-1)}$。
> - $\phi(N^\ast, N^{\ast\ast})$：归一化共现强度，刻画真实发生频率相较于随机预期的倍数。
>
> **数学直觉**
> 公式通过将经验联合分布除以独立零模型，消除了不同个体发文总量与总体发文速率波动的边际分布干扰。当 $\phi = 1$ 时代表无自相关；任何显著偏离 1 的区域均揭示时序动力学的非平稳性。
>
> > [!example]- 手算示例
> > 假设考察一组发表量均为 10 篇的学者队列（示例）：
> > 1. 在完全独立的随机零模型下，第 1 代表作落在位置 3 且第 2 代表作落在位置 4 的概率为 $P_{\text{rand}}(3, 4) = \frac{1}{10 \times 9} = \frac{1}{90} \approx 0.0111$。
> > 2. 实测 1,000 位学者中，有 17 位学者的头两大代表作恰好落在第 3 篇与第 4 篇，经验联合概率为 $P(3, 4) = \frac{17}{1000} = 0.0170$。
> > 3. 代入公式计算比值：$\phi(3, 4) = \frac{0.0170}{0.0111} \approx 1.53$。该位置观测到的共现频率为随机预期的 1.53 倍，呈现出显著的对角线聚集效应。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | $\phi \approx 1$（白色区域） | 代表作出现时序完全独立，符合随机影响法则与无偏抽样假设。 |
> > | 读法 | $\phi > 1$（红色隆起） | 代表作共现频率显著超越随机预期；实测在主对角线邻近处（$|N^\ast - N^{\ast\ast}| = 1$）达到 1.57，证实成果成簇。 |
> > | 读法 | $\phi < 1$（蓝色低谷） | 代表作在特定时序间距下出现概率受抑制，体现出长间隔下的时序排斥或休眠。 |
> > | 注意 | 对角线绝对零值 | 由于第一代表作与第二代表作必然是两篇不同论著，对角线正中心点 $N^\ast = N^{\ast\ast}$ 在数学上恒等于 0，峰值呈现在紧邻对角线的斜上方与斜下方。 |

> [!software-impl] 软件实现
> - **数据来源** Web of Science、Scopus 或 [[Microsoft Academic Graph|MAG]] 的长周期学者发表与引文序列。
> - **核心包或命令** Python `numpy`、`scipy`、`matplotlib` 或 `seaborn`。
> - **实现流程** 提取个体作品被引排名 → 定位前两大成果发表位次 → 统计经验频数构建网格 → 通过洗牌模拟生成基准分母 → 矩阵逐元素相除输出热力图。
> - **报告标准** 报告样本学者总数、单人最低成果门槛、归一化分箱精度（Bin size）及对角线统计显著性区间。

> [!formula] Python 计算骨架
> ```python
> import numpy as np
> 
> def compute_hit_colocation_matrix(career_data, n_bins=10):
>     """
>     计算代表作联合发生概率矩阵 phi(n*, n**)
>     career_data: list of arrays, 每个 array 为单个学者按发表时序排列的被引次数
>     n_bins: 归一化生涯进度的分箱数量 (0 到 1 之间)
>     """
>     obs_matrix = np.zeros((n_bins, n_bins))
> 
>     for citations in career_data:
>         n_total = len(citations)
>         if n_total < 2:
>             continue
>         # 提取头号与次号代表作索引 (0-based)
>         sorted_indices = np.argsort(citations)[::-1]
>         idx1, idx2 = sorted_indices[0], sorted_indices[1]
>         
>         # 归一化至 [0, 1) 区间
>         rel_pos1 = min(int((idx1 / n_total) * n_bins), n_bins - 1)
>         rel_pos2 = min(int((idx2 / n_total) * n_bins), n_bins - 1)
>         obs_matrix[rel_pos1, rel_pos2] += 1
> 
>     # 经验联合概率 P(N*, N**)
>     p_obs = obs_matrix / np.sum(obs_matrix)
> 
>     # 随机零模型基准 P_rand: 均匀随机选择两不同位置
>     p_rand = np.ones((n_bins, n_bins)) / (n_bins * n_bins - n_bins)
>     np.fill_diagonal(p_rand, 0)
>     p_rand = p_rand / np.sum(p_rand)
> 
>     # 归一化比值矩阵 phi
>     with np.errstate(divide='ignore', invalid='ignore'):
>         phi = np.where(p_rand > 0, p_obs / p_rand, 0)
>         
>     return phi
> ```

> [!method-stack] 数据口径
> - **数据来源** 跨学科引文数据库、拍卖行成交记录或影视商业数据库，不可将单篇短期即时引文与十年长周期标准化引文混用。
> - **时间与范围** 学者生涯长度通常要求 $\ge 20$ 篇论著，确保相对时序具有足够的分辨率。
> - **清洗与归属** 严格执行学者同名消歧，排除自引异常波动的[[Document|文献]]论著。
> - **标准化** 成果被引须采用按学科与发文年份标准化的十年被引分位数，避免学科篇幅差异污染排名。

---

> [!method-fit] 适用判断
> - **适合使用** 具有清晰离散发表时序记录、成果质量具备长周期评价指标的创造性职业（科学家、艺术家、作曲家、作家）。[[Argument_Wang_Barabasi_2021_Cambridge_Unit03|(Wang & Barabási, 2021, pp. 72–74)]]
> - **谨慎使用** 成果数量极少（如发文低于 10 篇）的初入行学者，此时离散分母极小会导致比值剧烈抖动。
> - **不适合使用** 连续流式产出或无离散标志作的非创造性常规生产过程。

---

> [!method-limits] 方法局限
> - **测量偏误** 依赖事后全生命周期引文回溯，无法对处于生涯早期的未定型学者实施即时预警。
> - **可比边界** 针对两篇代表作的联合分布未直接建模三次及以上连续爆发的复杂高阶关联。
> - **误用风险** 将统计学上的对角线时序成簇直接等同于因果机制，忽略了学者策略转型或外部资助激增等潜在混杂[[Variable|变量]]。
> - **补救方式** 结合马尔可夫两状态模型与变点检测算法进一步提取爆发期的确切起止时间点。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Hot Streak]] | 测量对象 | 本矩阵用于检验与诊断的核心创造力成簇[[Construct\|构念]]。 |
> | [[Hot-Streak Model]] | 理论 | 以本矩阵的经验成簇发现为首要实证前提构建的数学模型。 |
> | [[Random Impact Rule]] | 理论 | 本矩阵零模型分母所依托的独立无偏随机零假设。 |
> | [[Career Shuffling Method]] | 依赖方法 | 用于打乱个体发文引文时序并生成分母随机零模型的计算算法。 |
> | [[Lu Liu]] | 人物 | 领衔设计该矩阵算法并开展跨领域大样本实证的核心科学学家。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit03|Wang & Barabási (2021)]] — 运用归一化联合概率矩阵图示科学家、艺术家与导演的最佳代表作成簇现象，测定紧邻发表概率达随机预期的 1.57 倍。
