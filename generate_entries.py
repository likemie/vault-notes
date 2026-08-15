import os
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")

# 1. CFA Method
cfa_content = f"""---
title: Confirmatory Factor Analysis
aliases:
  - "验证性因子分析"
  - "CFA"
summary: "一种用于检验观测变量（如问卷题项）与潜在结构（如潜变量/因子）之间假设关系的多元统计方法。常用于量表开发、结构效度检验和测量模型确证。"
type: method
method_type: quantitative
method_family: "quantitative"
tags: []
related_concepts:
  - "[[Variable]]"
  - "[[Construct Validity]]"
related_theories: []
related_methods:
  - "[[Factor Mixture Modeling]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Greene_2010_JEP]]"
confidence: medium
status: draft
created: {today}
updated: {today}
---

# Confirmatory Factor Analysis

---

## 定义

> [!def] 方法定义
> 验证性因子分析（Confirmatory Factor Analysis, CFA）是一种用来测试研究者预先设定的潜变量（因子）结构是否与实际收集到的数据相契合的统计方法。与探索性因子分析（EFA）不同，CFA 要求研究者在分析前就明确指定哪些外显指标（观测变量）对应哪些潜在因子。

> [!method-scope] 方法范围
> - **研究对象** 多维度的量表测量数据、外显指标体系。
> - **问题类型** 回答预设的测量模型是否具有良好的结构效度（Construct Validity）。
> - **分析单位** 个体。
> - **输出形式** 因子载荷估计值、模型整体拟合指数（如 $\chi^2$, RMSEA, CFI, SRMR 等）。

---

## 方法定位

> [!method-position] 认识论与方法定位
> - **知识观** 认为心理与教育测量中的诸多概念（如智力、动机、认识论信念）是无法直接观测的潜变量，必须通过一组可观测的指标来推断。
> - **研究者角色** 研究者基于先验理论或前期探索研究提出结构假设，主观决定模型的设定。
> - **有效性标准** 各种绝对拟合指数和相对拟合指数（如 RMSEA < .08, CFI > .90 等）。

> [!method-stack] 方法层级
> - **分析方法** 验证性因子分析（CFA）。
> - **辅助技术** 最大似然估计（ML）、加权最小二乘法（WLSMV，适用于类别变量）。

---

## 研究程序

> [!proc] 通用程序
> 1. 根据理论或前期研究，构建测量模型（指明题项与因子的对应关系，以及因子间的协方差）。
> 2. 收集足够规模的样本数据（通常要求 N > 200）。
> 3. 运行模型并进行参数估计。
> 4. 评价模型拟合度。如果不佳，可参考修正指数（Modification Indices, MI）谨慎修改模型。
> 5. 报告因子载荷、测量误差与整体拟合指数。

### 量化方法模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 横截面数据为主，追踪数据可用于做测量等值性（Measurement Invariance）检验。
> - **变量或指标** 观测变量（题项分数）、潜变量（因子）、测量误差。
> - **模型或统计量** 结构方程模型（SEM）的测量模型部分。
> - **诊断与检验** $\chi^2$ 检验（易受大样本量影响）、RMSEA、SRMR、CFI、TLI 等拟合指标。

> [!formula-step] 公式步骤　CFA 基础测量方程
> $$ y_i = \Lambda \eta_i + \epsilon_i $$
>
> **这个公式在做什么** 描述观测变量的得分是如何由潜在因子的真实水平与测量误差共同决定的。
>
> **符号说明** $y_i$ 是观测变量向量；$\Lambda$ 是因子载荷矩阵（Factor Loadings）；$\eta_i$ 是潜因子向量；$\epsilon_i$ 是特定测量误差向量。
>
> **数学直觉** 把复杂的卷面分数降维剥离出纯净的“潜在特质”得分，同时把杂乱的误差隔离出来。
>
> **结果怎么读** $\Lambda$ 越大且显著，说明该题项越能有效代表其背后的潜变量（通常要求标准载荷 > 0.4 或 0.5）。

> [!software-impl] 软件实现
> - **推荐软件** Mplus、R（lavaan 包）、Amos。
> - **报告标准** 需报告 $\chi^2$ 及其自由度和 $p$ 值，RMSEA 及其 90% 置信区间，CFI，SRMR，以及各个题项的标准化因子载荷。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 验证成熟量表在不同人群中的结构效度，或在进行复杂的结构方程建模前验证测量模型。

---

## 局限性

> [!method-limits] 方法局限
> - **误用风险** 为了追求好的拟合指数，无视理论依据盲目释放误差协方差（ correlated errors）。
> - **适用边界** 样本量过小时估计不稳定；当观测指标不是连续变量而是 Likert 等级评分时，使用传统 ML 估计可能导致标准误偏误。

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Greene_2010_JEP]] — Greene et al. (2010) 使用验证性因子分析（CFA）评估了《认识论与本体论认知问卷》（EOCQ）在数学和历史领域的维度结构及其数据拟合度。
"""
with open("wiki/methods/quantitative/Confirmatory Factor Analysis.md", "w") as f:
    f.write(cfa_content)


# 2. Multinomial Logistic Regression
mlr_content = f"""---
title: Multinomial Logistic Regression
aliases:
  - "多项逻辑回归"
  - "Multinomial Logit Model"
summary: "一种用于预测名义变量（包含两个以上无序类别）的广义线性回归模型。常用于分类预测或探究自变量对个体归属于特定群体几率的影响。"
type: method
method_type: quantitative
method_family: "quantitative"
tags: []
related_concepts: []
related_theories: []
related_methods:
  - "[[Binary Logistic Regression]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Greene_2010_JEP]]"
confidence: medium
status: draft
created: {today}
updated: {today}
---

# Multinomial Logistic Regression

---

## 定义

> [!def] 方法定义
> 多项逻辑回归（Multinomial Logistic Regression）是二元逻辑回归的扩展，用于当因变量分类数大于 2 且各类别之间没有内在大小或顺序（即名义变量）时的回归分析。它通过设定一个“基准类别”（Reference Category），分别计算其他类别相对于基准类别的对数胜率（Log-odds）。

> [!method-scope] 方法范围
> - **研究对象** 截面数据或调查数据。
> - **问题类型** 预测个体归属于某一无序类别的概率，或检验特定自变量对分类归属的显著影响。
> - **分析单位** 个体。
> - **输出形式** 回归系数估计值 $b$、胜率比（Odds Ratio, OR 或 $e^b$）、分类预测概率。

---

## 方法定位

> [!method-position] 认识论与方法定位
> - **知识观** 认为个体的类别归属受到多个可测量因素的影响，且这种影响可以通过概率论进行量化估计。
> - **有效性标准** 伪 $R^2$（Pseudo $R^2$）、似然比检验（Likelihood Ratio Test）、分类准确率。

> [!method-stack] 方法层级
> - **分析方法** 多项逻辑回归。

---

## 研究程序

> [!proc] 通用程序
> 1. 明确一个无序多分类的因变量，并选定一个具有解释意义的分类作为“基准参照组”。
> 2. 将名义型的自变量转化为哑变量（Dummy Variables）。
> 3. 拟合模型，考察自变量的系数显著性。
> 4. 将对数几率系数转化为胜率比（$e^b$）进行实质性解释。

### 量化方法模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 横截面数据。
> - **变量或指标** 因变量必须是名义分类变量（如：分流后的轨道类型、潜在类别群组），自变量可为连续或分类变量。
> - **诊断与检验** 多重共线性诊断、独立无关替换假设检验（IIA, Independence of Irrelevant Alternatives）。

> [!formula-step] 公式步骤　多项逻辑回归模型
> $$ \\ln\\left(\\frac{{P(Y=k)}}{{P(Y=K)}}\\right) = \\beta_{{0k}} + \\beta_{{1k}}X_1 + \\dots + \\beta_{{pk}}X_p $$
>
> **这个公式在做什么** 计算个体属于目标类别 $k$ 与属于基准类别 $K$ 的胜率（几率）比值的自然对数，并将其表示为预测变量的线性组合。
>
> **符号说明** $Y$ 是因变量，$K$ 是设定的基准类别；$X$ 是自变量；$\\beta$ 是偏回归系数。
>
> **数学直觉** 强行预测“某个类别”很难，所以模型退而求其次，预测“选类别 $k$ 而不选基准类别 $K$ 的相对倾向”。
>
> **结果怎么读** $\\beta$ 取指数得到 $e^\\beta$ 即为胜率比（Odds Ratio, OR）。如果自变量 $X$ 增加 1 个单位，$e^\\beta = 1.5$，代表个体被归入类别 $k$ （相对 $K$）的几率增加了 50%。

> [!software-impl] 软件实现
> - **推荐软件** R（`nnet` 包中的 `multinom()` 函数）、SPSS、Stata。
> - **报告标准** 必须说明哪个类别是基准类别。报告系数 $b$、标准误、Wald 检验的显著性 $p$ 值以及胜率比 $e^b$。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 探究学生职业选择、潜类别成员归属等无序多分类结果变量的影响因素。

---

## 局限性

> [!method-limits] 方法局限
> - **适用边界** 需要满足 IIA 假设（各类别间的选择几率不依赖于是否存在其他类别）。如果类别间存在极强的相互替代性，应考虑其他模型（如嵌套 logit 模型）。
> - **偏误来源** 当某一类别的样本量极小时，极大似然估计可能不收敛或产生极大的标准误。

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Greene_2010_JEP]] — Greene et al. (2010) 使用多项逻辑回归（Multinomial Logistic Regression），以学业成绩和受教育年限为自变量预测个体归属特定认识论类别阶段的概率。
"""
with open("wiki/methods/quantitative/Multinomial Logistic Regression.md", "w") as f:
    f.write(mlr_content)


# 3. Academic Achievement Concept
aa_content = f"""---
title: Academic Achievement
aliases:
  - "学业成就"
  - "学业表现"
  - "GPA"
summary: "衡量学生在特定学习阶段、特定学科中知识与技能掌握程度的指标。通常通过课程分数、标准化测试成绩或绩点（GPA）进行测度。"
type: concept
tags: []
related_concepts: []
related_theories: []
related_methods: []
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Greene_2010_JEP]]"
confidence: medium
status: draft
created: {today}
updated: {today}
---

# Academic Achievement

---

## 概念界定

> [!concept-lens] 测量代理变量
> 学业成就往往被视为学生学习过程的结果输出。在不同的实证研究中，它可以被操作化为学生自陈的总体 GPA、特定学科（如数学、历史）的期末分数或统考成绩。

> [!claim] 综合表现
> **衡量标准** 学业成就不只反映智力，还交织着学习动机、认识论信念、家庭背景等多重因素。因此它既可以作为学习干预的结果变量，也可以作为个体认知发展水平的预测变量。

---

## 实证数据

> [!ref-table]- 其他实证结果
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | 变量或指标 | 关键结果 | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Greene_2010_JEP\|Greene et al. (2010)]] | 740名美国中学生至研究生 | 问卷调查（多项逻辑回归） | 历史与数学学科自报成绩（分数越高代表成绩越差） | 较差的数学成绩显著正向预测学生落入“初级认识论阶段”（Class 1）的几率（相对于高级阶段 Class 2，OR = 1.770）。 | $p < .01$ | 表明在结构不良问题和学术表现上，坚持纯粹现实主义（一切有标准答案）的信念会导致更差的学业成就。 |

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Greene_2010_JEP]] — Greene et al. (2010) 将学业成就作为潜类别分析的协变量，证明了特定学科的学业表现差异能有效预测学生的认识论与本体论认知阶段。
"""
with open("wiki/concepts/educational-psychology/Academic Achievement.md", "w") as f:
    f.write(aa_content)


# 4. Educational Level Concept
el_content = f"""---
title: Educational Level
aliases:
  - "受教育水平"
  - "受教育年限"
summary: "衡量个体接受正规学校教育的时长或最高学历层次的人口学变量。是探究认知发展、社会阶层与人力资本积累的核心解释变量。"
type: concept
tags: []
related_concepts: []
related_theories: []
related_methods: []
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Greene_2010_JEP]]"
confidence: medium
status: draft
created: {today}
updated: {today}
---

# Educational Level

---

## 概念界定

> [!concept-lens] 认知发展驱动力
> 随着受教育水平（如从中等教育进入高等教育）的提升，学生所面临的知识环境复杂度和认知挑战剧增，这在理论上构成了个人认识论信念从“绝对主义”向“理性批判主义”演变的催化剂。

> [!claim] 人口学代理
> **变量属性** 在多数量化研究中，受教育水平要么被作为连续变量（受教育年限），要么被作为分类变量（学历层级），用于控制成熟效应或直接探究学校系统对个体发展的累积效应。

---

## 实证数据

> [!ref-table]- 其他实证结果
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | 变量或指标 | 关键结果 | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Greene_2010_JEP\|Greene et al. (2010)]] | 740名美国中学生至研究生 | 问卷调查（多项逻辑回归） | 受教育年限（连续变量） | 受教育水平的增加会显著降低学生被归入初级“现实主义”认知类群（Class 1）的几率（相对于较高阶的 Class 2，OR = 0.496）。 | $p < .01$ | 提供了随教育年限增长、学生认识论信念自然向高阶发展的强有力证据。 |

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Greene_2010_JEP]] — Greene et al. (2010) 验证了受教育水平对个体认识论发展阶段的预测效度，确认教育年限越高，个体越倾向于表现出成熟的认识论信念模式。
"""
with open("wiki/concepts/sociology-of-education/Educational Level.md", "w") as f:
    f.write(el_content)

print("Created 4 new files.")
