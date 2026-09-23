---
title: Chi-Squared Test
aliases:
  - 卡方检验
  - 卡方检定
  - chi-square test
  - χ2 test
  - chi-squared test of independence
  - 卡方独立性检验
  - 卡方拟合优度检验
summary: "检验类别变量间关联性或单变量观测分布与理论分布吻合度的推断统计方法族，基于χ2统计量与期望频数比较，广泛应用于列联表分析与分类数据假设检验"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 38
method_related_level: 4
method_related_stars: "⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/statistical
  - quantitative-research
  - categorical-data
related_concepts:
  - "[[Variable]]"
  - "[[Hypothesis]]"
  - "[[Null Hypothesis]]"
  - "[[Unit of Analysis]]"
  - "[[Research Question]]"
  - "[[Dependent Variable]]"
  - "[[Homework]]"
  - "[[Scale of Measurement]]"
  - "[[Metacognition]]"
  - "[[Epistemic Stances]]"
  - "[[Evaluativist]]"
  - "[[Generative Artificial Intelligence]]"
  - "[[Epistemology]]"
  - "[[Causality]]"
  - "[[Alternative Hypothesis]]"
  - "[[Independent Variable]]"
  - "[[Absolutist]]"
  - "[[Reliability]]"
  - "[[Epistemic Agency]]"
  - "[[Epistemological Theories]]"
  - "[[Epistemic Friction]]"
related_theories: []
related_methods:
  - "[[Effect Size]]"
  - "[[Quantitative Research]]"
  - "[[Survey Research]]"
  - "[[Cross-sectional Study]]"
  - "[[Questionnaire]]"
  - "[[Coding in Qualitative Research]]"
  - "[[Sample Size Determination]]"
  - "[[Analysis of Variance]]"
  - "[[Likert Scale]]"
  - "[[Triangulation]]"
  - "[[t-test]]"
  - "[[Repeated Measures Design]]"
  - "[[Generalized Estimating Equations]]"
  - "[[Pearson Product-Moment Correlation]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Wu_2025_ER]]"
confidence: high
status: active
created: 2026-05-31
updated: 2026-09-22
---

# Chi-Squared Test

---

## 定义

> [!def] 方法定义
> 卡方检验（Chi-Squared Test, $\chi^2$ test）是一族基于卡方分布（$\chi^2$ distribution）对类别[[Variable\|变量]]（categorical variables）的频数数据进行推断统计的非参数[[Hypothesis\|假设]]检验方法。其核心机制在于比较实际观测频数（Observed Frequencies, $O$）与在原[[Hypothesis\|假设]]（[[Null Hypothesis\|零假设]] $H_0$）成立条件下的理论期望频数（Expected Frequencies, $E$），通过构建两者偏差平方加权和的 $\chi^2$ 统计量，评估观测分布与理论分布的偏离程度或检验两个类别变量之间是否存在统计学关联。[[Argument_Creswell_2022_SAGE\|(Creswell & Creswell, 2022, Ch8)]]; [[Argument_Wu_2025_ER\|(Wu et al., 2025, pp. 362–365)]]

> [!method-scope] 方法范围
> - **研究对象** 类别数据（定类变量与无序分类数据）、二分类或多分类列联表（contingency tables）以及理论分布比例拟合。
> - **问题类型** 适合回答两类核心问题：① 拟合优度问题（实际分布是否符合预设的理论比例）；② 独立性/关联性问题（两个分类变量之间是否相互独立或存在统计关联）。
> - **[[Unit of Analysis\|分析单位]]** 个体在分类题项上的频数计数、群体分类标签、实验样本表型分类等。
> - **输出形式** $\chi^2$ 检验统计量、自由度（$df$）、$p$ 值、标准化残差（Standardized Residuals）以及关联[[Effect Size\|效应量]]（Cramér's $V$、$\phi$ 系数或列联系数 Contingency Coefficient）。

> [!citation-card] 关键定义
> 当[[Research Question\|研究问题]]涉及组间关联（association between groups）且两个变量均为类别变量（如性别与投票倾向）时，卡方检验是唯一的标准推断统计选择。[[Argument_Creswell_2022_SAGE\|(Creswell & Creswell, 2022, Ch8, Table 8.3)]]
>
> *When the research question involves association between groups and both independent and [[Dependent Variable\|dependent variables]] are categorical, Chi-Square test is the appropriate inferential statistical technique.*

> [!citation-card] 人机交互中的方法学审问与边界辨析
> 在解决统计推论[[Homework\|作业]]时，大语言模型（如 ChatGPT）常因语境模糊或[[Scale of Measurement\|测量尺度]]混淆而给出不匹配的检验建议（如对极小样本或顺序量表误推卡方独立性或齐性检验）。学习者必须凭借扎实的[[Metacognition\|元认知]]监控与高阶[[Epistemic Stances\|认识立场]]，严格依据测量尺度、独立性与期望频数假设对模型输出实施批判性审问。[[Argument_Wu_2025_ER\|(Wu et al., 2025, pp. 362–365)]]
>
> *Students with [[Evaluativist]] epistemic stances actively interrogate [[Generative Artificial Intelligence\|Generative AI]] suggestions through multi-turn stress-testing, rejecting mismatched chi-squared tests when sample sizes are minimal or measurement scales violate nominal assumptions.*

---

## 方法定位

> [!method-position] [[Epistemology\|认识论]]与方法定位
> - **知识观** 卡方检验植根于频数统计与概率论视域，将分类现象视为离散状态的概率分布，通过比较经验观察频数与理论期望频数的偏离程度来判定分类[[Variable\|变量]]间的关联状态。
> - **研究者角色** [[Quantitative Research\|量化研究]]者需在研究设计阶段严密界定分类变量的[[Scale of Measurement\|测量尺度]]（名义尺度 vs 顺序尺度），严格核验各单元格期望频数[[Hypothesis\|假设]]（通常要求 $E \ge 5$），并在模型输出显著后结合[[Effect Size\|效应量]]与残差进行实质解释，避免简单将统计显著等同于因果效应。
> - **有效性标准** 统计结论效度（依赖期望频数满足准则与样本代表性）、测量效度（分类变量互斥与穷尽界定）以及正确的变体选择（独立性 vs 齐性 vs 拟合优度 vs Fisher 精确检验）。
> - **不声称回答的问题** 卡方检验无法提供连续变量的均值差异估计；不能直接反映顺序变量的等级单调递增/递减趋势；显著的卡方关联绝不等于[[Causality\|因果关系]]，且无法提供两个分类变量之间的方向性机制解释。

> [!method-stack] 方法层级
> - **研究设计** [[Survey Research\|调查研究]]、[[Cross-sectional Study\|横截面研究]]、观察性研究、准实验及生物遗传表型检验。
> - **数据收集** [[Questionnaire\|问卷调查]]单选/多选题项、分类[[Coding in Qualitative Research\|编码]]文本、档案频数记录、实验分类计数。
> - **分析方法** 卡方拟合优度检验（Goodness-of-Fit）、卡方独立性检验（Independence）、卡方齐性检验（Homogeneity）。
> - **辅助技术与小样本修正**
>   - 连续性修正（Yates's Correction for Continuity）
>   - 费希尔精确检验（Fisher's Exact Test，用于小样本期望频数 $<5$ 情境）
>   - 关联效应量计算（Cramér's $V$, $\phi$ 系数）
>   - 标准化残差分析（Standardized Pearson Residuals）

---

## 研究程序

> [!proc] 通用检验程序
> 1. **明确[[Hypothesis\|研究假设]]与[[Variable\|变量]]尺度** 确定自[[Variable\|变量]]与[[Dependent Variable\|因变量]]是否均为名义分类尺度，提出原假设 $H_0$（两变量相互独立/观测分布符合理论比例）与[[Alternative Hypothesis\|备择假设]] $H_1$。
> 2. **构建列联表与计算期望频数** 汇总各单元格实际观测频数 $O_{ij}$，依据行列边缘合计计算理论期望频数 $E_{ij}$。
> 3. **假设前提诊断** 检查样本独立性与期望频数分布：任意单元格期望频数不得小于 1，且期望频数小于 5 的单元格比例不得超过 20%（若违反则合并类别或改用 Fisher 精确检验）。
> 4. **计算 $\chi^2$ 统计量与判定显著性** 计算卡方值与自由度 $df = (r-1)(c-1)$，对照卡方分布表或计算 $p$ 值，与预设显著性水平 $\alpha = .05$ 比较。
> 5. **计算[[Effect Size\|效应量]]与残差剖析** 报告 Cramér's $V$ 或 $\phi$ 系数以衡量关联强度，并通过标准化残差定位导致显著偏离的具体单元格。

> [!method-stack] 数据、变量与模型
> - **数据结构** $r \times c$ 二维列联表或 $1 \times k$ 单维频数向量。
> - **样本与单位** 相互独立的抽样个体（不可重复测量同一批被试作为不同列联行），[[Sample Size Determination\|样本量]]通常要求 $N \ge 20$。
> - **变量要求** 类别变量（Categorical/Nominal）；若数据为等级/顺序量表且样本极小，强行使用卡方检验会丢失顺序信息且极易违背期望频数前提。
> - **诊断与检验** 期望频数矩阵完整性、单元格稀疏性诊断、连续性修正判定。

> [!formula-step] 公式步骤一　皮尔逊卡方检验统计量（Pearson's Chi-Squared Statistic）
> $$\chi^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$
>
> **这个公式在做什么** 计算所有单元格中观测频数与期望频数相对偏差平方的加权总和，衡量实际数据与理论模型之间的整体偏离程度。
>
> **符号说明**
> - $O_{ij}$：第 $i$ 行、第 $j$ 列单元格的实际观测频数（Observed Frequency）。
> - $E_{ij}$：第 $i$ 行、第 $j$ 列单元格在独立假设下的理论期望频数（Expected Frequency）。
> - $r, c$：列联表的行数（rows）与列数（columns）。
>
> **数学直觉** 若两个变量完全独立或观测分布完全契合理论，则对所有单元格 $O_{ij} \approx E_{ij}$，分子接近 0，$\chi^2$ 接近 0；当实际观测值与理论期望值偏差越大，分子平方后迅速放大，$\chi^2$ 统计量越大，拒绝原假设的证据越充分。除以分母 $E_{ij}$ 是为了对基数不同的单元格实施方差标准化加权。
>
> **结果怎么读** $\chi^2$ 越大且对应的 $p < .05$，表明拒绝两变量相互独立的原假设，两类别变量之间存在显著统计关联。
>
> **注意事项** 自由度计算为 $df = (r - 1)(c - 1)$；对于单维拟合优度检验，自由度为 $df = k - 1$（$k$ 为分类数）。

> [!formula-step] 公式步骤二　列联表理论期望频数计算（Expected Frequency）
> $$E_{ij} = \frac{R_i \times C_j}{N}$$
>
> **这个公式在做什么** 基于概率乘法定理，在两变量相互独立的理论假设下，计算第 $i$ 行第 $j$ 列单元格应有的理论频数。
>
> **符号说明**
> - $R_i = \sum_{j=1}^c O_{ij}$：第 $i$ 行各单元格观测频数的边际行和（Row Marginal Total）。
> - $C_j = \sum_{i=1}^r O_{ij}$：第 $j$ 列各单元格观测频数的边际列和（Column Marginal Total）。
> - $N$：全样本总频数（Total Sample Size）。
>
> **数学直觉** 独立事件联合概率等于边缘概率之乘积 $P(A \cap B) = P(A)P(B) = (R_i/N) \times (C_j/N)$，乘以总样本数 $N$ 即得理论期望频数 $E_{ij} = N \times (R_i/N)(C_j/N) = \frac{R_i C_j}{N}$。

> [!formula-step] 公式步骤三　列联表关联效应量 Cramér's V
> $$V = \sqrt{\frac{\chi^2}{N \times \min(r-1, c-1)}}$$
>
> **这个公式在做什么** 将受样本量 $N$ 影响膨胀的 $\chi^2$ 值标准化为 $[0, 1]$ 之间的相对关联强度指标，用于跨研究比较。
>
> **符号说明**
> - $\chi^2$：计算所得的皮尔逊卡方值。
> - $N$：样本总频数。
> - $\min(r-1, c-1)$：行自由度与列自由度中的较小值。
>
> **数学直觉** $\chi^2$ 统计量与样本量 $N$ 成正比（样本量翻倍，$\chi^2$ 亦翻倍），导致大样本下微弱关联也能达到显著。通过除以 $N$ 和最小自由度维度消除规模效应，从而量化纯粹的关联紧密度。
>
> **结果怎么读** $V \in [0, 1]$；$V \approx 0.1$ 表示弱关联，$V \approx 0.3$ 表示中等关联，$V \ge 0.5$ 表示强关联。对于 $2 \times 2$ 表格，Cramér's $V$ 退化为 $\phi$ 系数（$\phi = \sqrt{\chi^2 / N}$）。

> [!software-impl] 软件实现
> - **R 语言**
>   - 拟合优度检验：`chisq.test(x = c(315, 108, 101, 32), p = c(9/16, 3/16, 3/16, 1/16))`
>   - 独立性检验：`chisq.test(table(data$var1, data$var2), correct = FALSE)`
>   - 效应量计算：`rcompanion::cramerV(table_data)` 或 `vcd::assocstats(table_data)`
>   - 小样本精确检验：`fisher.test(table_data)`
> - **Python**
>   - `scipy.stats.chi2_contingency(contingency_matrix)` 返回卡方值、$p$ 值、$df$ 与期望频数矩阵。
>   - `scipy.stats.chisquare(f_obs, f_exp)` 用于一维拟合优度检验。
> - **SPSS**
>   - 菜单路径：`Analyze -> Descriptive Statistics -> Crosstabs`，勾选 `Chi-square`、`Phi and Cramer's V` 及单元格中的 `Expected` 与 `Standardized Residuals`。

---

## 方法变体与相近方法辨析

> [!tension-table] 分类与推断统计方法选择全景对比
> | 方法名称 | 适用数据类型 | 样本设计与[[Unit of Analysis\|分析单位]] | 核心检验目的 | 关键[[Hypothesis\|假设]]与约束条件 | 替代/升级方案 |
> |---|---|---|---|---|---|
> | **卡方拟合优度检验（Goodness-of-Fit）** | 单个名义类别[[Variable\|变量]] | 单一样本频数分布 | 检验样本分类比例是否符合特定理论预期（如遗传定律） | 各单元格期望频数 $E \ge 5$ | 单元格稀疏时合并类别或二项分布检验 |
> | **卡方独立性检验（Independence）** | 两个名义类别变量 | 单一样本的两个离散属性交叉 | 检验两分类变量之间是否独立或存在关联 | 观测独立；$E \ge 5$ 占 80% 以上 | 关联显著时计算 Cramér's $V$ 补充效应量 |
> | **卡方齐性检验（Homogeneity）** | 一个分组变量 + 一个分类[[Dependent Variable\|因变量]] | 两个或多个独立抽样总体 | 检验不同总体在同一分类特征上的分布是否一致 | 各组为独立抽样总体；期望频数满足准则 | Fisher's 精确检验（小样本） |
> | **麦克尼马尔检验（McNemar Test）** | 二分类类别变量 | 配对样本/自身前后重复测量 | 检验配对二分类数据的边缘频数是否发生对称性改变 | 仅限 $2 \times 2$ 配对二分类（如前后测“及格/不及格”） | 顺序尺度时不可用 |
> | **费希尔精确检验（Fisher's Exact Test）** | 类别变量（主要用于 $2 \times 2$） | 独立样本（尤其适合极小样本） | 基于超几何分布计算列联表出现的精确超几何概率 | 无期望频数需 $\ge 5$ 的限制 | 大样本时计算开销较大，回退至标准卡方 |
> | **[[Analysis of Variance\|单因素方差分析]]（One-Way ANOVA）** | [[Independent Variable\|自变量]]分类 + 因变量**连续**数值 | 两个或多个独立组别 | 比较多组连续变量的均值差异 | 因变量正态性、方差同质性（Levene 检验） | 方差不齐改用 Welch's ANOVA；非正态改用 Kruskal-Wallis |
> | 斯皮尔曼等级相关（Spearman Rank Correlation） | 顺序/等级尺度（如[[Likert Scale\|李克特量表]]） | 成对排序数据或小样本顺序量表 | 评估两顺序变量之间的单调递增/递减关联趋势 | 适用于小样本与非正态顺序数据 | 克服卡方检验丢弃等级次序信息的严重缺陷 |

---

## 人机交互中的认识论审问与典型误用辨析

在引入[[Generative Artificial Intelligence|生成式人工智能]]（如 ChatGPT）辅助统计决策的情境下，大模型的高速概率生成机制极易产生“看似言之成理、实则方法错配”的误用风险。学习者的[[Epistemic Stances|认识立场]]与[[Metacognition|元认知监控]]深度决定了其能否识别这些陷阱（[[Argument_Wu_2025_ER|Wu et al., 2025, pp. 362–365]]）：

> [!case] Case 1: Student A —— 孟德尔杂交实验拟合优度检验与绝对论盲从（[[Argument_Wu_2025_ER\|Wu et al., 2025]]）
> - **任务背景** 生物统计学[[Homework\|作业]]：检验孟德尔杂交实验中的豌豆表现型数据（黄色圆粒、绿色圆粒、黄色皱粒、绿色皱粒，总计 556 粒）是否符合经典的理论遗传比例（$9:3:3:1$）。
> - **人机交互记录复刻**
>   - **学生提问** *"What statistical test should I use to check if the phenotypic ratio of peas fits the 9:3:3:1 ratio from Mendel's experiment?"*
>   - **ChatGPT 回复** *"You should use the Chi-Square Goodness-of-Fit Test. Here is the formula $\chi^2 = \sum \frac{(O-E)^2}{E}$ and the R code: `chisq.test(x = c(315, 108, 101, 32), p = c(9/16, 3/16, 3/16, 1/16))`..."*
>   - **学生后续行动** 学生仅在课程讲义（Lecture slides）中简单搜索并确认提到了卡方拟合优度检验后，未作任何进一步公式理解或参数推演，立即结束对话并将 R 代码与输出结果直接粘贴至作业中。
> - **[[Epistemology\|认识论]]机制诊断** 表现出典型的一阶绝对论（[[Absolutist]]）特征。将统计知识视为非黑即白的固定操作，过度依赖外部权威（大模型与讲义），缺乏对期望频数计算逻辑或自由度设定的深层理解，认知加工停留在代码复制与程序执行层面。

> [!figure]- 图1：Student A 与 ChatGPT 的交互对话记录（绝对论立场）
> ![](https://img.mylikemie.icu/sources/Wu_2025_ER/figures/Wu_2025_ER_Fig1_Student_A_Interaction_Dialog.jpg)

> [!case] Case 3: Student C —— [[Likert Scale\|李克特量表]]极小样本一致性检验与评价论7轮多源核验（[[Argument_Wu_2025_ER\|Wu et al., 2025]]）
> - **任务背景** 调查统计作业：评估 8 名学生（$N=8$）在 4 点[[Likert Scale\|李克特量表]]（非常不同意、不同意、同意、非常同意）上回答 2 个关联题项得分的一致性程度。
> - **7 轮多源审问交互记录复刻**
>   - **Round 1（初始提问与初筛）** 学生询问该问题能否使用卡方检验；ChatGPT 初步建议采用卡方独立性检验（Chi-Squared Test of Independence），给出交叉表构造提示。
>   - **Round 2（压力测试与自相矛盾暴露）** 学生为验证[[Reliability\|可靠性]]，变换提示词再次输入相同情境进行确认；ChatGPT 发生自相矛盾，改口建议采用卡方齐性检验（Chi-Squared Test of Homogeneity）。学生凭借扎实的先验知识，敏锐指出 8 名学生属于同一批被试、而非来自两个独立总体，当场推翻了齐性检验的前提。
>   - **Round 3（开放式探询）** 学生追问 *"If homogeneity test is invalid, what else can I use?"*，ChatGPT 建议采用针对配对频数的麦克尼马尔检验（McNemar's test）。
>   - **Round 4（[[Scale of Measurement\|测量尺度]]辨析）** 学生反向质询模型为何在第一轮推荐独立性检验、其根本缺陷何在；ChatGPT 承认独立性检验用于名义[[Variable\|变量]]，无法反映顺序量表的等级差异。
>   - **Round 5（推翻模型[[Hypothesis\|假设]]）** 学生进一步核验麦克尼马尔检验的适用前提，指出自身数据为 4 点顺序量表而非二分类配对（$2 \times 2$）数据，且[[Sample Size Determination\|样本量]]仅 $N=8$，期望频数过低导致卡方近似完全崩溃，再次否决麦克尼马尔检验。
>   - **Round 6（同伴研讨与外部印证）** 学生暂停人机交互，将 ChatGPT 暴露出的自相矛盾与小样本约束带入课后研讨小组，与同伴交流非参数相关分析的适用性。
>   - **Round 7（最终决策收束）** 综合极小样本（$N=8$）、4 点顺序量表与数据非正态分布特征，全面排除所有卡方检验变体，最终独立决策采用非参数的斯皮尔曼等级相关（Spearman Rank Correlation）。
> - **认识论机制诊断** 充分展现了高阶评价论（[[Evaluativist]]）风范。以方法学假设前提为准绳，实施对抗性提示与多源[[Triangulation\|三角互证]]，将大语言模型从“解答生成器”降级为“论辩压力测试靶标”，牢固坚守了人类研究者的[[Epistemic Agency\|认识能动性]]与最终裁决权。

> [!figure]- 图3：Student C 与 ChatGPT 的交互对话记录（评价论立场）
> ![](https://img.mylikemie.icu/sources/Wu_2025_ER/figures/Wu_2025_ER_Fig3_Student_C_Interaction_Dialog.jpg)

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**
>   - [[Survey Research\|调查研究]]中分析两个名义类别[[Variable\|变量]]之间的列联交叉表关联（如学科专业与职业选择、政策知晓度与参与意愿）。[[Argument_Creswell_2022_SAGE\|(Creswell & Creswell, 2022, Ch8)]]
>   - 生物、医学或教育测验中检验样本表型分布是否符合预设的理论比例模型（卡方拟合优度检验）。
>   - [[Sample Size Determination\|样本量]]充足且各单元格期望频数普遍 $\ge 5$ 的大中型分类频数数据集。
> - **谨慎使用**
>   - $2 \times 2$ 四格表或单元格期望频数较小时，必须采用 Yates 连续性修正或改用 Fisher's 精确检验。
>   - 顺序/等级量表数据（如李克特 5 点量表）：使用卡方检验会丢失顺序信息，应优先考虑等级相关或非参数秩和检验。[[Argument_Wu_2025_ER\|(Wu et al., 2025, pp. 363–364)]]
> - **不适合使用**
>   - 连续数值[[Dependent Variable\|因变量]]的组间均值比较（应使用 [[t-test]] 或 [[Analysis of Variance\|方差分析]]）。
>   - 极小样本（如 $N < 20$）且包含稀疏单元格的数据集。
>   - 配对或[[Repeated Measures Design\|重复测量设计]]（应使用 McNemar 检验或[[Generalized Estimating Equations\|广义估计方程]]）。

---

## 局限性

> [!method-limits] 方法局限
> - **[[Sample Size Determination\|样本量]]极端敏感性** $\chi^2$ 值随总样本量 $N$ 的增加而线性放大；在大样本（如 $N > 5000$）下极微弱且无实质意义的微小差异也能产生极小 $p$ 值，必须强制补充报告 Cramér's $V$ [[Effect Size\|效应量]]。
> - **小样本期望频数崩溃** 当单元格理论期望频数 $< 5$ 时，卡方连续分布近似的抽样分布会产生严重偏离，大幅增加第一类或第二类错误风险。
> - **非[[Causality\|因果性]]与方向性缺失** 卡方检验显著仅证明[[Variable\|变量]]间非独立，无法判定因果影响方向，亦不能揭示多变量间的复杂调节或中介机制。
> - **高维列联表解释困境** 在 $r \times c$ 复杂大表中，卡方显著无法直接定位差异来源，必须依赖标准化残差剖析或对数线性模型（Log-linear Models）进行分解。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Analysis of Variance]] | 替代方法 | 比较分组[[Variable\|变量]]对**连续数值[[Dependent Variable\|因变量]]**的均值影响；与卡方检验处理类别因变量形成互补。 |
> | [[t-test]] | 替代方法 | 检验两组在连续变量上的均值差异。 |
> | [[Pearson Product-Moment Correlation]] | 替代方法 | 衡量两个**连续变量**之间的线性相关程度。 |
> | [[Effect Size]] | 补充方法 | 提供 Cramér's $V$ 与 $\phi$ 系数，克服卡方统计量随样本量膨胀的缺陷。 |
> | [[Sample Size Determination]] | 前置方法 | 确保抽样规模满足期望频数 $\ge 5$ 的基本数学假设。 |
> | [[Scale of Measurement]] | 前置理论 | 区分名义、顺序、等距与等比尺度，防范将顺序/连续数据不当降级为卡方分类。 |
> | [[Epistemic Stances]] | [[Epistemological Theories\|认识论理论]] | 解释学习者在人机协同解决卡方检验任务时的思维差异（绝对论 vs 多元论 vs 评价论）。 |
> | [[Metacognition]] | 调控机制 | 在大模型误推卡方检验时激活[[Epistemic Friction\|认知摩擦]]与多源核验的核心监控中枢。 |

---

## 使用此方法的研究

> [!evidence-grid-a] [[Correlational Research\|相关研究]]索引
> - [[Argument_Creswell_2022_SAGE\|Creswell & Creswell (2022)]] — 阐明卡方检验在量化调查与实验设计中作为两类别[[Variable\|变量]]关联检验的标准统计程序。（Ch8）
> - [[Argument_Wu_2025_ER\|Wu et al. (2025)]] — 记录研究生在解决孟德尔表型拟合优度检验与[[Likert Scale\|李克特量表]]一致性任务中，与 ChatGPT 对话时对卡方检验适用前提的[[Epistemology\|认识论]]审问与批判决策。（pp. 362–365）
