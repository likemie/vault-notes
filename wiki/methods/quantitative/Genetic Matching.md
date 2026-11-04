---
title: Genetic Matching
aliases:
  - 遗传匹配
  - 遗传匹配算法
  - GenMatch
summary: "基于演化遗传算法的多元非参数匹配方法，通过启发式搜索确定广义马氏距离中的协变量权重矩阵，自适应最大化处理组与对照组在所有可观测协变量上的平衡程度。该方法直接以匹配后的平衡检验统计量为优化目标，避免了传统倾向得分匹配与参数回归对函数形式设定的强依赖。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 9
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/causal-inference
  - method/matching
related_concepts:
  - "[[Variable]]"
  - "[[Causality]]"
  - "[[Counterfactual]]"
related_theories:
  - "[[Potential Outcomes Framework]]"
related_methods:
  - "[[Matching]]"
  - "[[Propensity Score Matching]]"
  - "[[Difference-in-Differences]]"
  - "[[Patent-Paper Pairs]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Thompson_et_al_2018_RP]]"
confidence: high
status: draft
created: 2026-11-04
updated: 2026-11-04
---

---

> [!def] Genetic Matching
> **遗传匹配（Genetic Matching，简称 GenMatch）** 是由亚历克西斯·戴蒙德（Alexis Diamond）与贾斯吉特·塞肯（Jasjeet S. Sekhon, 2013）提出的一种多元非参数因果推断匹配方法。该方法将遗传算法（Genetic Algorithm）引入到处理组与对照组的样本配对过程中，通过启发式演化搜索确定广义马氏距离度量中的正定对称权重矩阵 $W$，使得匹配后的样本在所有包含的连续与分类协变量上同时获得最佳的分布平衡（最小化 Kolmogorov-Smirnov 检验与双样本 $t$ 检验的偏离程度）。与传统的[[Propensity Score Matching\|倾向得分匹配（PSM）]]相比，遗传匹配不依赖于研究者预先设定的参数化选择方程或单维得分假设，在处理复杂非线性交互与多维连续变量时具有更优的均方误差表现。[[Argument_Thompson_et_al_2018_RP|(Thompson et al., 2018, pp. 1063–1064)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 估计观察性研究与准实验中的处理组平均处理效应（Average Treatment Effect on the Treated, ATT）。
> - **问题类型** 因果推断与协变量平衡（在无随机分配条件下消除可观测混杂偏差）。
> - **分析单位** 观测样本个体（如学生、学校、专利配对样本、企业）。
> - **输入数据** 处理变量指示符（Treatment Indicator）、多维连续或分类协变量矩阵 $X$、可选的确切匹配限制条件（Exact Match Constraints）与卡尺范围（Caliper）。
> - **输出形式** 配对权重向量、匹配后样本数据集、协变量平衡诊断报告（$t$ 检验与 KS 检验 $p$ 值）。

> [!citation-card] 关键定义
> 我们使用 R 软件中的 Matching 程序包识别这些“最近邻”，该程序包采用“遗传匹配”演化搜索算法将处理观测值与潜在对照进行配对，并迭代改善协变量平衡。在等比例偏差减少所需的假设成立时，遗传匹配在均方误差（MSE）方面优于其他匹配方法；当这些假设不成立时，遗传匹配的优势更为明显。[[Argument_Thompson_et_al_2018_RP|(Thompson et al., 2018, pp. 1063–1064)]]
>
> *We identify these 'nearest neighbors' using the 'Matching' package for R software, which employs the evolutionary search algorithm 'genetic matching' to pair treatment observations with potential controls and iteratively improve covariate balance (Diamond and Sekhon, 2013; Sekhon, 2011)... genetic matching 'dominates the other matching methods in terms of MSE when assumptions required for EPBR hold and, even more so, when they do not.'*

---

> [!method-position] 方法定位
> - **构念效度** 匹配质量取决于纳入遗传搜索算法的协变量是否涵盖了影响处理选择和潜在结果的关键前序特征。
> - **研究者判断** 决定哪些变量执行刚性确切匹配（Exact Matching）、哪些变量允许在卡尺约束内进行最近邻搜索，以及演化算法的种群代数与停止准则。
> - **有效性标准** 匹配后样本在各维协变量均值与累积分布上的平衡性检验，通常要求标准化均值差小于 0.1 且 KS 检验无显著差异。
> - **不声称回答的问题** 无法直接消除未被观测到的时变混杂因素，因果推断依然依赖可忽略性假定。

> [!method-stack] 方法层级
> - **上位方法** [[Matching\|匹配法]]、反事实因果推断框架（[[Potential Outcomes Framework]]）。
> - **前置步骤** 协变量筛选、缺失值插补、马氏距离矩阵初始化。
> - **变体与扩展** 结合卡尺约束的遗传匹配（GenMatch with Calipers）、结合确切匹配的分层遗传匹配、匹配双重差分法（Matching DID）。

---

> [!formula-step] 步骤一　广义马氏距离度量构建
> $$d(X_i, X_j) = \sqrt{(X_i - X_j)' \left( S^{-1/2} \right)' W S^{-1/2} (X_i - X_j)}$$
>
> **这个公式在做什么** 计算处理观测值 $i$ 与对照候选值 $j$ 在协变量空间中的广义加权距离。输入个体协变量向量 $X_i$ 与 $X_j$ 以及样本协方差矩阵的平方根倒数 $S^{-1/2}$，输出单一的标量距离值。[[Argument_Thompson_et_al_2018_RP|(Thompson et al., 2018, p. 1064)]]
>
> **符号说明** $W$ 为由遗传算法搜索确定的非负对角权重矩阵；$S$ 为样本协方差矩阵。
>
> **数学直觉** 标准马氏距离假设所有协变量具有相同的相对权重（$W = I$）；遗传匹配通过自适应搜索非对角或对角权重 $W$，为那些难以平衡的关键协变量赋予更大权重，从而实现整体分布的最优配对。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 距离最小化 | 距离越小表示对照观测值与处理观测值在加权多维特征上越相近。 |
> > | 注意 | 权重矩阵约束 | 权重矩阵 $W$ 必须保持半正定，以确保几何空间中距离测度的单调有效性。 |

> [!formula-step] 步骤二　遗传演化搜索目标函数优化
> $$\max_{W} \min_{k} \left\{ p_{t, k}(W), p_{\text{KS}, k}(W) \right\}$$
>
> **这个公式在做什么** 通过遗传演化算法在解空间中搜寻最优权重矩阵 $W$。目标函数设定为最大化最难平衡协变量的检验 $p$ 值，即使得所有变量中最小的双样本 $t$ 检验 $p$ 值或 Kolmogorov-Smirnov 检验 $p$ 值达到最大。[[Argument_Thompson_et_al_2018_RP|(Thompson et al., 2018, p. 1064)]]
>
> **符号说明** $p_{t, k}$ 为第 $k$ 个协变量的均值差异 $t$ 检验 $p$ 值；$p_{\text{KS}, k}$ 为分布拟合检验 $p$ 值。
>
> **数学直觉** 避免了研究者凭主观经验反复调试倾向得分模型的繁琐试错，将样本平衡直接转变为算法自动化求解的最优化问题。

---

> [!software-impl] 软件实现
> - **核心包或命令** R (`Matching::GenMatch`, `Matching::Match`), Python (`scikit-learn`, `geneticalgorithm`).
> - **实现流程**
>   1. 定义处理变量、协变量矩阵与确切匹配约束：`exact = c("pub_age", "subject", "patent_granted", "mta_issued")`
>   2. 运行演化算法搜索权重矩阵：`genout <- GenMatch(Tr = Treat, X = Covars, exact = exact, caliper = 1)`
>   3. 基于估计权重执行样本配对：`mout <- Match(Tr = Treat, X = Covars, Weight.matrix = genout)`
>   4. 平衡诊断评估：`MatchBalance(Treat ~ Covars, match.out = mout)`
> - **报告标准** 必须报告匹配前后处理组与对照组的变量均值、标准差、标准化差异百分比以及 KS 检验统计量。

> [!method-stack] 变量与诊断
> - **数据结构** 包含处理组与大量潜在未处理候选池的截面或面板数据。
> - **前置假定** 条件独立性假定（Conditional Independence Assumption）与共同支撑集假定（Common Support）。
> - **样本削减** 当施加严格卡尺时，超出卡尺范围的无对照处理个体将被剔除，研究者需评估外部有效性损失。

---

> [!method-fit] 适用判断
> - **适合使用** 协变量维数较高、存在复杂非线性关联，且传统倾向得分匹配无法使关键变量达到满意的平衡标准的观察性研究。[[Argument_Thompson_et_al_2018_RP|(Thompson et al., 2018, pp. 1063–1064)]]
> - **谨慎使用** 样本量极其庞大的大数据集（遗传演化搜索算法在大样本下的计算复杂度较高，耗时显著增加）。
> - **不适合使用** 对照组样本池严重狭窄、无法找到任何相近观测值的极度不平衡情境。

---

> [!method-limits] 方法局限
> - **计算资源开销** 遗传算法依赖大规模种群迭代模拟，搜索时间显著长于一步式倾向得分回归。
> - **未观测混杂风险** 与所有基于可观测变量的匹配方法一致，遗传匹配仅能平衡已纳入模型的特征，无法防御未观测到的选择偏差。
> - **局部解局限** 启发式随机搜索存在陷入局部极值点的概率，建议采用多种随机数种子重复验证结果稳定性。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Matching]] | 方法 | 遗传匹配所属的上位非实验因果推断方法分类。 |
> | [[Propensity Score Matching]] | 方法 | 遗传匹配主要克服与替代的传统参数化匹配算法。 |
> | [[Difference-in-Differences]] | 方法 | 常与遗传匹配联合使用（Matching DID），由遗传匹配构建对照组，由 DID 消除时间不变未观测干扰。 |
> | [[Patent-Paper Pairs]] | 方法 | 在学术技术转移与科学学实证中，遗传匹配用于构建未许可成果对照组的核心应用场景。 |
> | [[Potential Outcomes Framework]] | 理论 | 支撑遗传匹配反事实估计的底层理论框架。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Thompson_et_al_2018_RP|Thompson et al. (2018)]] — 在大学专利许可对科学传播的影响研究中，采用遗传匹配算法对成果发表年限、学科、影响因子与前期引用趋势进行配对，构建了高质量的对照组样本。
