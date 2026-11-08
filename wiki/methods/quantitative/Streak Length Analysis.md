---
title: Streak Length Analysis
aliases:
  - 游程长度分析
  - 连胜长度分析
  - 游程检验
  - Run Length Test
  - Wald-Wolfowitz Runs Test
  - 瓦尔德-沃尔夫维茨游程检验
summary: "时间序列与序列统计中用于检验离散二元产出序列是否偏离独立随机假设的非参数方法族；通过统计游程数、比较观测游程分布与伯努利独立零模型的理论预期，诊断序列中是否存在异常成簇（正自相关）或过度交替（负自相关）；在体育竞技热手论争与科学学学术爆发期研究中均为核心检验工具。"
type: method
method_type: quantitative
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/statistical
  - theme/science-of-science
  - theme/hot-streaks
  - theme/hot-hand
related_concepts: []
related_theories: []
related_methods: []
related_instruments: []
related_persons: []
related_facts: []
related_arguments: []
confidence: high
status: draft
created: 2026-11-08
updated: 2026-11-08
---

---

> [!def] Streak Length Analysis
> 游程长度分析（Streak Length Analysis）又称游程检验（Wald-Wolfowitz Runs Test），是一类非参数序列检验方法，用于判断离散二元产出序列（如"命中/未中"或"高影响/低影响"）中连续相同结果的出现模式是否偏离独立随机假设。输入一段有序的二元序列 $(X_1, X_2, \ldots, X_n)$，统计其中游程数（Runs，即连续相同取值的极大子串数目）$R$，与独立[[Null Hypothesis|零假设]]下的期望游程数 $\mu_R$ 进行比较，输出标准化 $Z$ 统计量用于假设检验。[[Argument_Wang_Barabasi_2021_Cambridge_Unit03|(Wang & Barabási, 2021, pp. 71–72)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 二元离散序列中连续相同结果的分布特征，据以诊断序列自相关性。
> - **问题类型** 非参数假设检验，判断给定序列是否源于独立同分布过程。
> - **分析单位** 按时间或出版顺序排列的单条二元序列（如篮球投篮序列、学者逐篇发表记录中的高影响/低影响标记）。
> - **输入数据** 有限长度的有序二元序列 $(X_1, \ldots, X_n)$，$X_i \in \{0, 1\}$。
> - **输出形式** 整数游程数 $R$、期望值 $\mu_R$、方差 $\sigma_R^2$、标准化 $Z$ 统计量及对应 $p$ 值。

> [!citation-card] 关键定义
> 吉洛维奇等人通过游程检验（Wald-Wolfowitz Runs Test）与序列二项分布比对，分析费城76人队球员的投篮命中序列，发现连续命中与连续投失的游程频次与独立伯努利试验序列一致。这一结果在1985年构成了将热手判定为认知错觉的核心统计依据。[[Argument_Wang_Barabasi_2021_Cambridge_Unit03|(Wang & Barabási, 2021, pp. 71–72)]]
>
> *Gilovich, Vallone, and Tversky analyzed the shooting records of the Philadelphia 76ers, applying the runs test to determine whether hit streaks occurred more often than would be expected by chance.*

---

> [!method-position] 方法定位
> - **构念效度** 游程检验直接捕捉序列中相邻事件的一阶状态转移特征，对长程高阶依赖结构（如周期性或非线性趋势）敏感度较低。
> - **研究者判断** 二元化阈值的选择（如以何种标准区分"高影响"与"低影响"论著）、序列截断范围。
> - **有效性标准** 大样本渐近正态近似的精度，序列长度 $n$ 一般要求 $\geq 20$。
> - **不声称回答的问题** 游程检验仅诊断序列是否偏离独立随机，不能识别偏离的具体模式（如马尔可夫转移矩阵结构），也不能推断偏离的因果机制。

> [!method-stack] 方法层级
> - **上位方法** 非参数序列检验。
> - **前置步骤** 将连续型产出指标二元化（如将被引量按中位数分为高影响/低影响），确保序列的时间排列正确。
> - **变体与扩展** 单样本游程检验（本条目所述标准形式）；多游程长度分布检验（检验各长度游程的频次分布是否符合理论预期）；[[Joint Probability Matrix of Hits|代表作联合发生概率矩阵]]（将成簇检测从一维游程扩展到二维位置共现）。

---

> [!formula-step] 步骤一　游程计数与期望游程数
> $$\mu_R = \frac{2 n_1 n_2}{n} + 1$$
>
> **这个公式在做什么** 在独立零假设下计算长度为 $n$ 的二元序列中游程数的期望值。输入序列中两类事件的频数 $n_1$ 和 $n_2$（$n_1 + n_2 = n$），输出在完全独立随机排列下应观测到的游程数。
>
> **符号说明**
> - $n$：序列总长度。
> - $n_1$、$n_2$：序列中两类事件各自的总频次。
> - $\mu_R$：独立零假设下游程数的数学期望。
>
> **数学直觉** 相邻两个元素取值不同的概率为 $2 n_1 n_2 / [n(n-1)]$（无放回抽样近似），乘以 $n-1$ 个相邻对再加 1（首项自身构成第一个游程），得到期望游程数。当 $n_1 = n_2$ 时期望最大（约 $n/2 + 1$），当其中一类频次远小于另一类时期望接近 1。
>
> > [!example]- 手算示例
> > 假设一位学者发表 10 篇论著（示例），其中 $n_1 = 4$ 篇高影响、$n_2 = 6$ 篇低影响，按时间排列的序列为 H L L H H H L L L H。
> > 1. 统计游程数：H | L L | H H H | L L L | H → $R = 5$。
> > 2. 计算期望游程数：$\mu_R = \frac{2 \times 4 \times 6}{10} + 1 = 5.8$。
> > 3. 观测值 $R = 5$ 略低于期望，提示轻微的同类成簇倾向，但偏离程度需经 $Z$ 检验判断是否显著。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | $R \approx \mu_R$ | 序列中游程数接近期望，不能拒绝独立随机假设。 |
> > | 读法 | $R < \mu_R$（游程偏少） | 同类事件过度成簇，连胜或连败频次超出随机预期，提示正自相关（如热手效应）。 |
> > | 读法 | $R > \mu_R$（游程偏多） | 事件过度交替，相邻观测倾向于不同取值，提示负自相关。 |
> > | 注意 | 大样本正态近似 | $Z$ 检验依赖渐近正态假设，$n_1$ 和 $n_2$ 各自至少约 10 时近似较可靠；序列极短时应采用精确分布。 |

> [!formula-step] 步骤二　标准化检验统计量
> $$Z = \frac{R - \mu_R}{\sigma_R}, \qquad \sigma_R^2 = \frac{2 n_1 n_2 (2 n_1 n_2 - n)}{n^2 (n - 1)}$$
>
> **这个公式在做什么** 将观测游程数 $R$ 标准化为 $Z$ 统计量，输入 $R$、$\mu_R$ 及理论方差 $\sigma_R^2$，输出渐近标准正态分布下的检验统计量，据以计算 $p$ 值。[[Argument_Wang_Barabasi_2021_Cambridge_Unit03|(Wang & Barabási, 2021, pp. 71–72)]]
>
> **符号说明**
> - $R$：序列中观测到的实际游程数。
> - $\sigma_R^2$：独立零假设下游程数的理论方差。
> - $Z$：标准化统计量；当 $|Z| > 1.96$ 时，在 5% 显著性水平下拒绝独立随机假设。
>
> **数学直觉** 方差公式来自超几何分布框架下游程数的精确方差推导；在零假设下，游程数的分布随 $n$ 增大而趋于正态，$Z$ 统计量即为偏离独立基线的标准化距离。
>
> > [!example]- 手算示例
> > 沿用步骤一的示例（$n = 10$，$n_1 = 4$，$n_2 = 6$，$R = 5$，$\mu_R = 5.8$）：
> > 1. 计算方差：$\sigma_R^2 = \frac{2 \times 4 \times 6 \times (2 \times 4 \times 6 - 10)}{10^2 \times 9} = \frac{48 \times 38}{900} \approx 2.027$。
> > 2. 标准差：$\sigma_R \approx 1.424$。
> > 3. $Z = \frac{5 - 5.8}{1.424} \approx -0.56$。$|Z| < 1.96$，在 5% 水平下未能拒绝独立随机假设。
>
> > [!geogebra] 游程检验与连胜长度模拟
> > - **上半区** 二元序列可视化（红色 = 命中，灰色 = 未中）
> > - **下半区** 命中连胜长度分布柱状图（$L = 1, 2, 3, 4, 5+$）
> > - **滑块 序列长度 n** 控制序列长度（15–30）
> > - **滑块 成功概率 p** 控制每次独立命中概率（0.3–0.7）
> > - **滑块 热手增益 Δp** $\in [0, 0.30]$：Δp = 0 时为独立伯努利序列；Δp > 0 时前次命中后下次命中概率提升至 $p + \Delta p$，模拟正向自相关
> > - **滑块 样本** 切换 5 组预设随机序列
> > - **右侧面板** 显示观测游程数 $R$、期望游程数 $\mu_R$、$Z$ 统计量、最长连续命中 $L$
> >
> > 从 Δp = 0 开始拖动至 0.3，观察游程数减少（同类成簇加剧）、最长连胜 $L$ 增大、$Z$ 统计量绝对值增加直至拒绝零假设的过程。
> >
> > ![[wiki/assets/geogebra/streak_length_analysis.ggb]]

> [!software-impl] 软件实现
> - **数据来源** 按时间排序的二元序列；在科学学中通常来自 Web of Science、Scopus 或 MAG 的个人全生涯发表时序。
> - **核心包或命令** Python `statsmodels.sandbox.stats.runs.runstest_1samp`；R `tseries::runs.test`；SAS `PROC NPAR1WAY`。
> - **实现流程** 按时间排列个体产出 → 以选定阈值二元化 → 计算 $n_1$、$n_2$、$R$ → 代入公式计算 $\mu_R$、$\sigma_R^2$、$Z$ → 与正态分位数比较判定。
> - **报告标准** 报告 $n$、$n_1$、$n_2$、$R$、$\mu_R$、$Z$ 及对应 $p$ 值，注明二元化标准与双侧/单侧检验选择。

> [!formula] Python 计算骨架
> ```python
> import numpy as np
> from scipy import stats
> 
> def runs_test(sequence):
>     """
>     对二元序列执行 Wald-Wolfowitz 游程检验。
>     sequence: array-like of 0s and 1s
>     returns: (R, mu, sigma, Z, p_value)
>     """
>     seq = np.asarray(sequence)
>     n = len(seq)
>     n1 = int(np.sum(seq))
>     n2 = n - n1
>     
>     # 统计游程数
>     runs = 1 + np.sum(seq[1:] != seq[:-1])
>     
>     # 期望与方差
>     mu = 2 * n1 * n2 / n + 1
>     var = (2 * n1 * n2 * (2 * n1 * n2 - n)) / (n**2 * (n - 1))
>     sigma = np.sqrt(var)
>     
>     # Z 统计量与 p 值（双侧）
>     z = (runs - mu) / sigma
>     p = 2 * (1 - stats.norm.cdf(abs(z)))
>     
>     return runs, mu, sigma, z, p
> ```

> [!method-stack] 变量与诊断
> - **数据结构** 单条有序二元时间序列（如按发表年份排列的"高影响/低影响"论著标记）。
> - **变量** 因变量为每个观测位点的二元取值（0/1）；自变量为时间或序列位次。
> - **识别假设** 零假设为序列中各元素独立同分布（i.i.d.），即不存在时间自相关。
> - **诊断与检验** $Z$ 统计量的渐近正态性在 $n_1, n_2 \geq 10$ 时较可靠；序列较短时需查精确分布表或使用蒙特卡洛置换检验。

---

> [!method-fit] 适用判断
> - **适合使用** 拥有清晰时间排序的二元观测序列，用于一阶自相关的快速非参数诊断（如投篮热手检验、学者生涯产出序列的随机性检验）。[[Argument_Wang_Barabasi_2021_Cambridge_Unit03|(Wang & Barabási, 2021, pp. 71–72)]]
> - **谨慎使用** 序列长度极短（$n < 20$）或两类频次严重不均衡时，正态近似不可靠，需改用精确分布或置换检验。
> - **不适合使用** 连续型时间序列（应使用自相关函数 ACF 或 Ljung-Box 检验）；需要识别具体自相关结构（如马尔可夫阶数、周期性或趋势成分）的场景。

---

> [!method-limits] 方法局限
> - **测量偏误** 二元化阈值的选择（如以中位数、均值还是百分位截断）直接影响 $n_1/n_2$ 比例，从而影响检验的统计功效。
> - **可比边界** 游程检验仅捕捉一阶相邻依赖；高阶自相关结构（如"每隔两篇出现一次高峰"）不被该方法检出。
> - **误用风险** 将"未拒绝零假设"等同于"序列确实随机"；吉洛维奇等人 1985 年的游程检验结论在 2018 年被米勒与桑胡尔霍证明受到有限样本条件概率偏差的系统性影响。[[Argument_Wang_Barabasi_2021_Cambridge_Unit03|(Wang & Barabási, 2021, pp. 71–72)]]
> - **补救方式** 搭配[[Joint Probability Matrix of Hits|代表作联合概率矩阵]]进行二维位置共现检测；使用[[Career Shuffling Method|生涯洗牌法]]生成反事实基准；使用变点检测算法识别爆发期的精确起止点。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Hot Streak]] | 测量对象 | 游程检验用于诊断学术生涯中是否存在代表作异常成簇的爆发期。 |
> | [[Hot Hand Fallacy]] | 理论 | 游程检验是 1985 年吉洛维奇等人判定热手为认知错觉的核心统计工具。 |
> | [[Hot-Streak Model]] | 理论 | 爆发期模型以游程检验结果为经验前提，参数化爆发期的持续时间与幅度。 |
> | [[Random Impact Rule]] | 理论 | 游程检验的零假设对应随机影响规律所假设的独立同分布基线。 |
> | [[Joint Probability Matrix of Hits]] | 扩展方法 | 将一维游程成簇检测扩展为二维代表作位置的联合概率比值矩阵。 |
> | [[Career Shuffling Method]] | 互补方法 | 通过置换重组生成反事实基准序列，补充游程检验的零模型构建。 |

---

> [!evidence-grid-a|notitle] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit03|Wang & Barabási (2021)]] — 回顾吉洛维奇等人如何运用游程检验将篮球热手判定为认知错觉，以及米勒与桑胡尔霍如何揭示该检验在有限样本中的条件概率偏差。
