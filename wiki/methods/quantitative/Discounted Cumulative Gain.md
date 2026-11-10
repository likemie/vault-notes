---
title: Discounted Cumulative Gain
aliases:
  - 折损累积增益
  - 累积增益折损
  - DCG
  - Discounted Cumulated Gain
summary: "信息科学与科学计量学中用于度量排序结果质量或聚合学者全生涯产出绩效的非线性加权算法，通过对排序靠后的成果施加对数折损惩罚，有效克服了算术平均受极值稀释与简单求和诱发成果通胀的方法学瓶颈。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 11
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - scientometrics
  - information-retrieval
  - evaluation
related_concepts:
  - "[[Unit of Analysis]]"
  - "[[Construct Validity]]"
  - "[[Hot Streak]]"
  - "[[Document]]"
  - "[[Emergence]]"
related_theories:
  - "[[Constant-Probability-of-Success Model]]"
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Disruption Index]]"
related_persons: []
related_facts:
  - "[[Microsoft Academic Graph]]"
  - "[[OpenAlex]]"
related_arguments:
  - "[[Argument_Chen_2025_HSSC]]"
confidence: high
status: completed
created: 2026-11-04
updated: 2026-11-11
---

---

> [!def] Discounted Cumulative Gain
> **折损累积增益（Discounted Cumulative Gain, DCG）** 是指在信息检索与[[Bibliometric Analysis|科学计量学]]中评估排序列整体质量与聚合多项产出价值的量化算法。该方法依据成果在列表中的相关度（或影响力和颠覆度得分）进行降序排列，并对位置靠后的低秩项施加对数衰减折扣（$\frac{1}{\log_2(i+1)}$）。在学者生涯动力学研究中，DCG 能够同时兼顾成果价值与数量规模，解决算术平均受低值稀释以及简单加总过度奖赏平庸发文的系统性偏差。[[Argument_Chen_2025_HSSC|(Chen et al., 2025, pp. 5–6)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 搜索引擎检索排序列表的累积效用、学者在特定年份或职业生涯阶段多项学术成果的综合影响力与颠覆度水平。
> - **问题类型** 非线性多属性聚合、排序结果质量评价、科研全生命周期产出指数构建。
> - **[[Unit of Analysis|分析单位]]** 查询结果文档序列、学者年度成果集合、音乐艺术家专辑曲目列表。
> - **输出形式** 大于或等于零的连续实数聚合得分（$DCG \ge 0$），亦可除以理想最优排序得分转化为归一化指标（Normalized DCG, NDCG $\in [0, 1]$）。

> [!citation-card] 学者论折损累积增益在非均权聚合中的优势
> 在评估学者年度整体产出状态时，DCG 超越了基于求和与均值的传统聚合方式，它通过考虑单项成果的秩次位次分配递减权重，有效平抑低影响力成果的干扰，比算术平均和简单加总更能真实映射学者的核心贡献。[[Argument_Chen_2025_HSSC|(Chen et al., 2025, p. 6)]]
>
> *DCG exceeds sum- and mean-based aggregation methods by considering the ranking of the disruptiveness or citation impact of publications published by a specific author instead of treating every publication equally... DCG is able to consider both value and number.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 传统科研评价指标常假设各项成果具有同质权重或仅取单篇极值；DCG 将“重大代表作具有主导价值、常规后续产出具备递减边际收益”的认知规律形式化为对数折扣权重，兼顾顶尖突破高度与持续产出厚度。
> - **研究者判断** 需明确相关度得分的映射规则（如原始被引频次是否需取对数压缩偏态、[[Disruption Index|颠覆性指数]]是否仅提取正向颠覆值）、截断位置 $k$ 的设定以及是否采用理想基准（IDCG）进行归一化。
> - **有效性标准** 排序单调性（高质量成果置于前列时得分更高）、尺度不变性及对随机低值波动的抗噪稳健性。
> - **不声称回答的问题** DCG 本身仅提供聚合算式，无法解决原始指标自身的输入偏差（如被引时滞或引文通胀）。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis|文献计量分析]]、多属性评价方法（MCDA）、信息检索评价体系。
> - **前置步骤** 成果元数据清洗、被引频次统计、[[Disruption Index|颠覆性指数]]解算与多篇成果降序排列。
> - **变体与扩展** 归一化折损累积增益（NDCG）、对数被引 DCG 变体（$DCG_{\text{citation}}$）、正向颠覆度 DCG 变体（$DCG_{\text{disruption}}$）。

> [!dev-timeline] 方法演变
> - **2002 — 信息科学基础算法确立** Kalervo Järvelin 与 Jaana Kekäläinen 在 ACM TOIS 提出累积增益（CG）与折损累积增益（DCG），奠定现代检索系统非二元相关度评估标准。
> - **2023 — 创意产业多作品价值聚合拓展** Oliveira 等将 DCG 算法拓展至音乐产业，成功测度艺术家单曲曲目集合与全生命周期的爆发期动态。
> - **2025 — 科学学生涯颠覆度动态聚合与建模** [[Argument_Chen_2025_HSSC|Chen et al. (2025)]] 将 DCG 引入大样本经济学家面板分析，分别构建年度被引与颠覆度 DCG 指数，实证揭示学者[[Hot Streak|学术爆发期]]内的颠覆度显著超越常规时期，且解释力达 $R^2 = 0.822$。

---

> [!formula-set]- 公式链总览
> ```mermaid
> flowchart LR
>   A["提取单年度全部产出成果<br>计算被引 C_i 与颠覆度 D_i"] --> B["按数值从大到小降序排列<br>赋予位次序号 i = 1, 2, ..., n"]
>   B --> C["施加对数衰减加权因子<br>权重系数 w_i = 1 / log2(i + 1)"]
>   C --> D["累加折损后得分<br>输出年度 DCG 指数"]
> ```

> [!formula-step] 步骤一　标准折损累积增益基础算式
> $$\text{DCG}_p = \sum_{i=1}^p \frac{rel_i}{\log_2(i + 1)}$$
>
> **这个公式在做什么** 接收一组经降序排序后的成果相关度得分序列 $rel_i$（$rel_1 \ge rel_2 \ge \dots \ge rel_p$），对各成果除以与其位次相关的对数递增分母，输出加权累积值。[[Argument_Chen_2025_HSSC|(Chen et al., 2025, p. 6)]]
>
> **符号说明**
> - $rel_i$：排序后位于第 $i$ 位的成果效用分值（如单篇相关度或影响指标）。
> - $i$：成果在降序列表中的位次编号（首位 $i = 1$ 时分母为 $\log_2 2 = 1$）。
> - $p$：纳入统计的成果总篇数。
>
> **数学直觉** 排名第 1 的核心成果获得 100% 满额权重（分母为 1）；第 2 位成果权重降至约 63.1%（$1/\log_2 3 \approx 0.631$）；第 3 位权重降至 50%（$1/\log_2 4 = 0.500$）。随着位次后移，低效用成果对总分的拉动被平滑抑制，有效防范发文凑数带来的虚假虚高。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 数值单调递增 | 随高影响力成果增加，DCG 稳步增大；代表作越突出，总得分越高。 |
> > | 注意 | 排序依赖 | 计算前必须执行严格的由大到小降序排列，未排序直接代入会导致折损逻辑失效。 |

> [!formula-step] 步骤二　学者年度被引与颠覆度对数 DCG 变体
> $$\text{DCG}_{\text{citation}} = \sum_{i=1}^p \frac{\log_2(C_i + 1)}{\log_2(i + 1)}, \quad \text{DCG}_{\text{disruption}} = \sum_{i=1}^{p'} \frac{D_i}{\log_2(i + 1)}$$
>
> **这个公式在做什么** 针对科学计量中被引频次与颠覆度分布特征定制的聚合算式。对右偏严重的长尾被引量取以 2 为底的对数压缩极值；针对颠覆性指数（$D \in [-1, 1]$），仅提取大于 0 的正向颠覆成果集合（共 $p'$ 篇）进行聚合，隔离巩固型负值对颠覆测度的代数抵消。[[Argument_Chen_2025_HSSC|(Chen et al., 2025, p. 6)]]
>
> **符号说明**
> - $C_i$：排序后第 $i$ 篇成果获得的施引频次。
> - $D_i$：排序后第 $i$ 篇成果的颠覆性指数得分。
> - $p'$：该年度内具有正颠覆度（$D > 0$）的成果总篇数。
>
> **数学直觉** 颠覆度若包含负值（巩固型工作），简单加总会导致“一篇极高颠覆加多篇常规工作”的总分反遭扣减；通过滤除负值并结合对数位次折损，精准测度学者在该年度实现的纯前沿开拓势能。

---

> [!software-impl] 软件实现
> - **数据来源** 学者年度论著引文列表、[[Disruption Index|颠覆性指数]]计算结果数据表。
> - **核心代码示例**
>
> ```python
> import numpy as np
> 
> def calculate_dcg_citation(citations):
>     """计算年度学术被引 DCG 得分"""
>     if not citations:
>         return 0.0
>     # 1. 降序排列
>     sorted_cits = np.sort(np.array(citations))[::-1]
>     # 2. 对数效用与位次折损
>     ranks = np.arange(1, len(sorted_cits) + 1)
>     gains = np.log2(sorted_cits + 1)
>     discounts = np.log2(ranks + 1)
>     return float(np.sum(gains / discounts))
> 
> def calculate_dcg_disruption(disruptions):
>     """计算年度正向颠覆度 DCG 得分"""
>     # 仅保留正向颠覆度成果
>     pos_d = [d for d in disruptions if d > 0]
>     if not pos_d:
>         return 0.0
>     sorted_d = np.sort(np.array(pos_d))[::-1]
>     ranks = np.arange(1, len(sorted_d) + 1)
>     discounts = np.log2(ranks + 1)
>     return float(np.sum(sorted_d / discounts))
> ```

> [!method-stack] 数据口径
> - **数据来源** 完备引文知识图谱（如 [[Microsoft Academic Graph]]、[[OpenAlex]]）。
> - **时间与范围** 按日历年或入行学术年资汇总单体学者名下全部经消歧清洗的成果。
> - **清洗与归属** 剔除无被引且无参考[[Document|文献]]的边缘条目；对单篇成果设置最低引文窗口（如 5 年窗口 $D_5$）。
> - **聚合参数** 颠覆度聚合限定 $D > 0$ 成果；被引聚合取 $\log_2(C+1)$ 以控制极端高引项的拉动效应。

---

> [!contrast-table] DCG 与传统聚合方法（算术平均、简单求和）多维对比
> | 比较维度 | 折损累积增益（DCG） | 算术平均（Mean） | 简单求和（Sum） |
> |:---|:---|:---|:---|
> | **处理单项成果权重** | 按成果重要性降序分配对数衰减权重 | 所有成果均分权重（$1/N$） | 所有成果权重相等（$1.0$） |
> | **对低值及零值的敏感性** | 稳健抗噪，低值成果位于尾部且受深度折扣 | 极度敏感，多篇低值成果大幅拉低整体均值 | 不受低值抑制，但机械累加轻微数值 |
> | **对发文膨胀与灌水的反应** | 有效抑制，后继平庸产出边际贡献迅速衰减 | 产生惩罚效应，拉低已有均值 | 产生过度奖励，形成发文多即总分高的偏差 |
> | **生涯爆发期测度表现** | 突出代表作高度兼顾持续产出，$R^2 = 0.822$ | 掩盖代表作突破，方差波动失真 | 掩盖质量差异，回归解释力偏低（$R^2 = 0.281$） |

---

> [!method-fit] 适用判断
> - **适合使用** 学者多篇成果长周期生涯动态追踪、学术爆发期（[[Hot Streak]]）识别、创意产出非均权综合评估、信息检索排序质量校验。[[Argument_Chen_2025_HSSC|(Chen et al., 2025, pp. 5–6)]]
> - **谨慎使用** 成果数量极少（如单年仅 1 篇）的样本，此时 DCG 无法体现多篇折损优势；评价需跨学科绝对值直接对比时，需辅以百分位归一化（NDCG）。
> - **不适合使用** 不适合用于需严格保持加法线性分解的财务成本核算；不适合在未做排序的情况下直接按发表时序套用公式。

---

> [!method-limits] 方法局限
> - **偏误来源** 对排序首位（$i=1$）成果赋予极高权重，若顶尖成果存在数据提取错误或偶然共引异化，总得分受其单项波动牵动较深。
> - **适用边界** 依赖于可连续排序的定量基准；在成果影响力差距极小或呈均匀分布时，折损加权优势不明显。
> - **误用风险** 盲目将包含大量负值的巩固型指标（如 $D < 0$）直接代入，导致代数相消歪曲事实；未做对数压缩直接代入超高引爆文，造成分母折损失效。
> - **补救方式** 正负指标分离计算；长尾指标前置对数变换；结合理想排序基准（IDCG）计算归一化得分 NDCG。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[Disruption Index]] | 配套方法 | 为 DCG 颠覆度聚合提供单篇底层的知识拓扑测度输入。 |
> | [[Bibliometric Analysis]] | 上位方法 | 文献计量学为 DCG 在科学学领域的跨学科迁移提供底层数据支撑。 |
> | [[Hot Streak]] | 解释对象 | DCG 为准确捕捉学者爆发期内突破性成果[[Emergence\|涌现]]提供核心聚合算法。 |
> | [[Constant-Probability-of-Success Model]] | 理论 | DCG 揭示更长爆发期对应更高巅峰颠覆度，经验印证了试错累积假说。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Chen_2025_HSSC|Chen et al. (2025)]] — 首次将 DCG 算法系统引入两万余名经济学家的长周期生涯分析，克服算术平均与简单加总的局限，证实学者学术爆发期兼具高颠覆度特征。（pp. 5–6）
