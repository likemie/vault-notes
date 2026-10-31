---
title: Mark and Recapture Method in Scientometrics
aliases:
  - 标记重捕法
  - 标记重捕模型
  - 文献规模生态学抽样测算法
  - 文献标记重捕法
  - Mark-Recapture Method
summary: "一种借鉴种群生态学调查原理测算互联网与数据库不可见学术文献总体规模的量化评估方法。该方法通过在独立学术搜索引擎（如 Google Scholar 与 Microsoft Academic Search）中抽样并比对文献重合捕获率（Overlap Ratio），利用林肯-彼得森（Lincoln-Petersen）估计量或查普曼（Chapman）修正公式，在无法对全量文献进行逐篇清点的条件下无偏估计网络学术文献与出版物总体规模。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 5
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/statistical
  - method/model
  - scientometrics
related_concepts:
  - "[[Big Science]]"
  - "[[Science Immediacy]]"
  - "[[Mountain of Science]]"
related_theories: []
related_methods:
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit07]]"
confidence: high
status: active
created: 2026-10-31
updated: 2026-10-31
---

---

> [!def] Mark and Recapture Method in Scientometrics
> 标记重捕法是一种在全域样本不可穷尽时推算文献总体规模的非参数抽样估计方法；该方法输入两个相互独立文献检索系统或数据库各自抽样捕获的文献集合（样本规模分别为 $M$ 与 $C$），通过比对二者交集确定重合捕获的文献量 $R$，依据捕获概率守恒计算重合捕获率并输出总体文献规模的点估计量 $\hat{N} = \frac{M \cdot C}{R}$ 及其置信区间。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, p. 163)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 互联网公开可访问或特定学术数据库未完全编目的全球科技文献总体规模（Total Volume of Scholarly Documents）。
> - **问题类型** 总体容量无偏参数估计（Population Size Estimation）与数据库覆盖率测度。
> - **分析单位** 科技论著、学术专著、会议报告或预印本独立条目实体。
> - **输入数据** 两个或多个独立学术搜索引擎（如 Google Scholar、Microsoft Academic Search）通过均匀随机关键词检索抽取的文献条目标识符集合。
> - **输出形式** 连续型正实数总体估计量 $\hat{N}$、查普曼小样本偏误修正值及其方差与渐近置信区间。

> [!citation-card|notitle] 关键定义
> 2014 年，研究人员利用标记重捕法估算互联网公开学术文献总体规模。该方法原由生态学家开创，用于在无法清点每一个个体的情况下估算野生动物种群规模。测算显示，彼时网络上公开可检索的英文学术文献至少有 1.14 亿篇。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, p. 163)]]
>
> *In 2014, researchers estimated the total number of scholarly documents on the Internet using a 'mark and recapture' method (originally developed by ecologists to estimate the population size of wild animals when they cannot count every individual). They found that back then, there were at least 114 million English-language scholarly documents accessible on the Web.*

---

> [!method-position] 方法定位
> - **构念效度** 测算出的 $\hat{N}$ 代表两引擎检索抓取范围在全网重叠交集的理论极限，高度反映公开网络可索引文献体量，但未计入深度隐藏于付费防火墙之后且完全无开放元数据的沉没文献。
> - **研究者判断** 抽样检索词字典库构建、停用词过滤规则、两库相同文献跨数据库匹配消歧阈值（标题编辑距离与 DOI 比对）。
> - **有效性标准** 两检索系统抓取行为的独立性检验、样本抽取的等概率无偏性以及重合样本识别的准确率。
> - **不声称回答的问题** 总体估计量仅反映文献物理规模存量，不度量文献的学术质量、引用影响力或知识原创度。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis|文献计量分析]]、非参数统计抽样理论。
> - **前置步骤** 随机检索词字典库构建、搜索 API 自动化采集、元数据清洗与重复条目消歧匹配。
> - **变体与扩展** 查普曼（Chapman）小样本偏误修正模型、贝叶斯多样本重捕模型（Schnabel Estimator）。

> [!dev-timeline] 方法演变
> - **1896 — 海洋生态学提出** C. G. Johannes Petersen 在调查比目鱼种群迁徙与数量时，首创给鱼群贴附标牌并再次捕捞的标记重捕思想。
> - **1930 — 经典林肯指数确立** Frederick C. Lincoln 建立林肯-彼得森估计量（Lincoln-Petersen Index），通过标记释放野鸭测算北美候鸟种群总容量。
> - **1951 — 小样本无偏修正** Douglas G. Chapman 提出分母加一的小样本调整公式，消除重合样本偏少时的正偏误并推导理论方差。
> - **2014 — 科学学文献规模测算** Madian Khabsa 与 C. Lee Giles 将生态标记重捕法跨界迁移至互联网学术文献规模评估，利用 Google Scholar 与 Microsoft Academic Search 的重合度估计全网英文学术文献突破 1.14 亿篇。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, p. 163)]]

---

> [!formula-set]- 公式链总览
> ```mermaid
> flowchart LR
>   A["系统一独立抽样抓取 M 篇并标记"] --> B["系统二独立抽样抓取 C 篇文献"]
>   B --> C["跨库比对识别重合捕获量 R"]
>   C --> D["林肯-彼得森基准估计量 N = M · C / R"]
>   D --> E["查普曼小样本偏误修正与方差评定"]
> ```

> [!formula-step] 步骤一　林肯-彼得森基准总体规模估计
> $$\hat{N} = \frac{M \cdot C}{R}$$
>
> **这个公式在做什么** 输入第一学术搜索引擎抽取的样本量 $M$、第二学术搜索引擎抽取的样本量 $C$，以及两样本中同时出现的重叠文献量 $R$，输出全域学术文献总量的无偏点估计值 $\hat{N}$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, p. 163)]]
>
> **符号说明**
> - $\hat{N}$：全网或数据库全域学术文献总量的估计值；
> - $M$：第一检索系统（如 Google Scholar）样本中被抓取并视作“被标记”的文献数；
> - $C$：第二检索系统（如 Microsoft Academic Search）独立抽样捕获的文献总量；
> - $R$：在第二样本中被“重捕”（即同时存在于第一样本）的文献数量。
>
> **数学直觉** 假定第二检索系统对文献的抓取是随机且独立的，其样本中重合文献所占的比例 $\frac{R}{C}$，应当近似等于第一检索系统样本在全域总体中所占的比例 $\frac{M}{N}$；依据 $\frac{R}{C} \approx \frac{M}{N}$ 进行代数变换，即可解得总体规模 $\hat{N} \approx \frac{M \cdot C}{R}$。
>
> > [!example]- 手算示例
> > 假定研究人员从第一学术搜索引擎抽样检索并标记了 $M = 10,000$ 篇文献；随后在第二独立搜索引擎中随机抓取了 $C = 8,000$ 篇文献。经过跨库标题与 DOI 查重，发现第二样本中有 $R = 800$ 篇与第一样本重合（重合捕获率为 10%）。代入公式计算：
> > $$\hat{N} = \frac{10,000 \times 8,000}{800} = 100,000 \text{ 篇}$$
> > 结果表明在设定检索口径下，全域文献总体估算为 10 万篇。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 重叠量 $R$ 的反比效应 | 重合文献数 $R$ 越小，说明第一样本在全域中所占比例越微小，推算出的总体规模 $\hat{N}$ 呈双曲线上升。 |
> > | 注意 | 抽样独立性假定 | 两个检索系统的数据抓取必须相互独立，若两系统倾向于共同抓取高被引名刊，重叠量 $R$ 将被人工抬高，导致总体 $\hat{N}$ 被严重低估。 |
>
> > [!geogebra] 动态参数模拟
> > - **横轴** 双库重合文献量 $R$（单位：百万篇）
> > - **纵轴** 估计全域文献总体 $\hat{N}$（单位：百万篇）
> > - **滑块 M** 第一引擎抓取样本量 $M$（蓝色滑块）
> > - **滑块 C** 第二引擎抓取样本量 $C$（绿色滑块）
> > - **滑块 R** 双库重合捕获量 $R$（红色滑块）
> >
> > 拖动滑块调节两库抽样体量与重叠数，观察估计曲线的双曲线走势与总体估计量 $\hat{N}$ 的渐近稳定性。
> > ![[wiki/assets/geogebra/mark_and_recapture_scientometrics.ggb]]

> [!formula-step] 步骤二　查普曼小样本偏误修正与方差估计
> $$\hat{N}_{\text{Chapman}} = \frac{(M + 1)(C + 1)}{R + 1} - 1$$
> $$\widehat{\mathrm{Var}}(\hat{N}_{\text{Chapman}}) = \frac{(M + 1)(C + 1)(M - R)(C - R)}{(R + 1)^2 (R + 2)}$$
>
> **这个公式在做什么** 当重合文献量 $R$ 较小时，传统林肯-彼得森估计量存在向上偏误且分母为零时失效；查普曼（Chapman）修正公式通过在各参数上加 1 进行平滑，给出小样本条件下的无偏估计量并测定其抽样方差。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, p. 163)]]
>
> **符号说明**
> - $\hat{N}_{\text{Chapman}}$：修正后的总体规模无偏估计值；
> - $\widehat{\mathrm{Var}}(\hat{N}_{\text{Chapman}})$：估计量的理论抽样方差，用于构建 95% 置信区间 $\hat{N} \pm 1.96 \sqrt{\widehat{\mathrm{Var}}}$。
>
> **数学直觉** 在有限样本抽样中，随机波动可能导致 $R$ 偏小，直接相除会导致极大极值；查普曼公式利用超几何分布期望的数学性质，通过在分子分母同步加入拉普拉斯平滑项，严格证明了其数学期望在样本满足 $M + C \ge N$ 时完全无偏。
>
> > [!example]- 手算示例
> > 沿用前例数据 $M = 10,000$，$C = 8,000$，$R = 800$：
> > $$\hat{N}_{\text{Chapman}} = \frac{10,001 \times 8,001}{801} - 1 \approx 99,899 \text{ 篇}$$
> > 样本量较大时修正值与基准值高度吻合，微小下调修正了有限抽样误差。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 稳健性测度 | 方差大小取决于重合文献数 $R$；$R$ 超过 100 时方差迅速趋小，估计置信区间显著收窄。 |
> > | 注意 | 封闭总体假定 | 假定在抽样调查的时间窗口内，全网文献总体保持相对稳定，未发生大规模突发性批量注销或数据迁移。 |

---

> [!software-impl] 软件实现
> - **数据来源** Google Scholar、Microsoft Academic Search 或 OpenAlex 等学术检索系统开放接口。
> - **核心包或命令** Python 标准库 `math`、科学计算包 `numpy`、`scipy.stats`。
> - **实现流程** 提取两系统抽样数据列表，基于 DOI 与规范化标题计算交集，代入查普曼公式计算点估计值与 95% 置信区间。
> - **报告标准** 明确报告抽样检索词列表、两系统抽取样本数、重叠篇数、消歧算法准确度以及最终估计区间。

> [!formula] Python 计算骨架
> ```python
> import math
> 
> def mark_and_recapture_estimate(m: int, c: int, r: int):
>     """
>     计算文献规模标记重捕法估计量 (Lincoln-Petersen & Chapman)
>     :param m: 引擎一抽样量 (Marked)
>     :param c: 引擎二抽样量 (Captured)
>     :param r: 双引擎重合量 (Recaptured)
>     :return: 包含基准估计、修正估计、标准误与置信区间的字典
>     """
>     if r <= 0:
>         raise ValueError("重合文献数必须大于 0")
>     
>     # 1. 林肯-彼得森基准估计
>     n_lp = (m * c) / r
>     
>     # 2. 查普曼小样本修正
>     n_chapman = ((m + 1) * (c + 1)) / (r + 1) - 1
>     
>     # 3. 方差与标准误
>     var_n = ((m + 1) * (c + 1) * (m - r) * (c - r)) / (((r + 1) ** 2) * (r + 2))
>     se_n = math.sqrt(max(0, var_n))
>     
>     # 4. 95% 置信区间
>     ci_lower = max(m + c - r, n_chapman - 1.96 * se_n)
>     ci_upper = n_chapman + 1.96 * se_n
>     
>     return {
>         "lincoln_petersen": n_lp,
>         "chapman": n_chapman,
>         "std_error": se_n,
>         "ci_95": (ci_lower, ci_upper)
>     }
> ```

> [!method-stack] 数据口径
> - **数据来源** 跨搜索引擎抽样需注意不同平台索引边界差异（如 Google Scholar 抓取包含预印本与学位论著，而部分传统引文索引仅限同行评审期刊）。
> - **时间与范围** 保持两引擎抓取在同一时间窗口内同步完成，避免时间差带来的文献指数增量干扰。
> - **清洗与归属** 采用规范化标题（小写、去除标点空格）与 DOI 联合消歧，排除因署名学者拼写变体导致的假阴性漏配。
> - **标准化** 明确排除重复抓取项、撤稿条目与非学术垃圾内容网页。

---

> [!method-fit] 适用判断
> - **适合使用** 评估互联网开源学术文献规模、测定隐蔽学术灰色文献存量，以及核验不同文献数据库的收录完整性。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, p. 163)]]
> - **谨慎使用** 两数据库抓取偏好高度趋同（如均优先抓取同一商业出版集团期刊）时，必须实施异质性加权校正。
> - **不适合使用** 总体处于极度剧烈变动状态，或样本捕获概率与文献特征深度绑定的强选择性场景。

> [!ref-table]- 参照基准与阈值
> | 调查情境 | 参照值与测算结果 | 来源 |
> |---|---|---|
> | 2014 年全网可检索英文学术文献总量 | 至少 1.14 亿篇文献存量 | [[Argument_Wang_Barabasi_2021_Cambridge_Unit07\|(Khabsa & Giles, 2014, p. 163)]] |
> | 2018 年微软学术搜索全量索引规模 | 超过 1.71 亿篇文献记录 | [[Argument_Wang_Barabasi_2021_Cambridge_Unit07\|(Sinha et al., 2015, p. 163)]] |
> | Google Scholar 相对全网学术覆盖度 | 估算收录占比超过 80% | [[Argument_Wang_Barabasi_2021_Cambridge_Unit07\|(Khabsa & Giles, 2014, p. 163)]] |

---

> [!method-limits] 方法局限
> - **测量偏误** 若高被引文献在两系统中均极易被检索到，而冷门文献双双被忽略，抽样异质性会导致重合率虚高，从而低估文献真实总体。
> - **可比边界** 英文学术文献与非英文学术文献的抓取率存在显著鸿沟，基于英文词典抽样的估计值无法直接推广至全球多语言体系。
> - **误用风险** 将特定搜索引擎可索引的网络公开学术资源，误读为人类历史上曾经出版过的全部纸质与闭源文献总和。
> - **补救方式** 采用分层抽样设计（按学科、年代、语言分层估算）与多重捕获贝叶斯网络模型降低抽样偏差。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Big Science]] | 测量对象 | 标记重捕法用于定量测算大科学时代全网学术出版物的庞大存量。 |
> | [[Science Immediacy]] | 测量对象 | 文献总量的持续倍增直接构成了科学即时性命题的经验基础。 |
> | [[Mountain of Science]] | 测量对象 | 对应科学之山底层全量文献规模的宏观外推基准。 |
> | [[Bibliometric Analysis]] | 上位方法 | 标记重捕法所属的文献计量统计分析方法体系。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit07|Wang & Barabási (2021)]] — 评介 Khabsa and Giles (2014) 运用标记重捕法对全网学术文献规模开展的开创性定量评估，确立了全网英文学术文献突破 1.14 亿篇的基准事实。
