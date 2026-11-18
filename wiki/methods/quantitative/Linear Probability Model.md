---
title: Linear Probability Model
aliases:
  - 线性概率模型
  - LPM
summary: "将二元分类因变量直接套用普通最小二乘法进行回归估计的计量经济学模型，其回归系数直接解释为自变量每变动一单位导致结果发生概率的边际变化，具有直观可比和便于容纳多维高维固定效应的优势。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 0
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/model
related_concepts: []
related_theories: []
related_methods: []
related_instruments: []
related_persons: []
related_facts: []
related_arguments: []
confidence: high
status: draft
created: 2026-11-19
updated: 2026-11-19
---

---

> [!def] Linear Probability Model
> 线性概率模型（Linear Probability Model, LPM）是将二值因变量（$Y \in \{0, 1\}$）直接作为被解释变量、通过普通最小二乘法（Ordinary Least Squares, OLS）估计参数的线性回归方法；自变量系数向量直接反映协变量变动引起的事件发生概率的边际变化。[[Argument_Phyo_2025_SocSci|(Phyo & Ilie, 2025, p. 9)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 估算自变量（如社会经济地位、人口学特征、干预政策）对二元教育结局（如 [[Higher Education Access|高等教育获得]]、升学决策、学业留存或辍学）发生概率的边际影响。
> - **问题类型** 因果识别、条件概率估计、跨群体差距比较与政策效应评估。
> - **分析单位** 个体、家庭、学生队列或微观调查受访者。
> - **输入数据** 包含二元结果变量及分类或连续自变量的大样本截面数据、重复截面调查或面板数据。
> - **输出形式** OLS 点估计系数、异方差稳健标准误、边际效应概率变化值及置信区间。

> [!citation-card] 线性概率模型在跨国教育公平队列分析中的应用
> 选用线性概率模型而非二元 Logit 或 Probit 模型的考量，在于其系数具有直观清晰的可解释性，能够直接展示各阶层与边际群体的绝对百分点差距。[[Argument_Phyo_2025_SocSci|(Phyo & Ilie, 2025, p. 9)]]
>
> *We employ linear probability models with within-country region fixed effects to examine the relationship between wealth and higher education access across different cohorts in each country. We chose linear probability models over other commonly used regression techniques such as probit or logit because it is much easier to interpret the coefficients.*

---

> [!method-position] 方法定位
> - **构念效度** 输出系数严格对应概率的线性边际增量，直观呈现不同财富五等分、性别及城乡群体之间的绝对参与率差距。
> - **研究者判断** 权重设置、参考基准类别选择（如以最贫困群体为基准）、固定效应维度的设定以及是否纳入交互项。
> - **有效性标准** 统计推断依赖异方差稳健标准误（Huber-White Sandwich Standard Errors）或整群稳健标准误；在大样本及非极值概率区间具备高度可靠的逼近效度。
> - **不声称回答的问题** 线性设定无法保证拟合值严格落在 $[0, 1]$ 理论概率区间内，不能用于外推极低或极高概率边缘个体的极端预测。

> [!method-stack] 方法层级
> - **上位方法** [[Multiple Regression|多元线性回归]]与普通最小二乘估计。
> - **前置步骤** 抽样权重校准、二元因变量编码、参照组设定及多重共线性排查。
> - **变体与扩展** 纳入区域固定效应的 LPM 模型、异质性交互项 LPM 模型、整群调整稳健误差修正。

---

> [!formula-step] 步骤一　基准线性概率设定与 OLS 估计
> $$Y_{i} = \alpha + \mathbf{X}_{i} \boldsymbol{\beta} + \varepsilon_{i}, \quad E[Y_i \mid \mathbf{X}_i] = P(Y_i = 1 \mid \mathbf{X}_i) = \alpha + \mathbf{X}_i \boldsymbol{\beta}$$
>
> **这个公式在做什么** 因变量 $Y_i$ 为指示变量（1 代表获得该事件，0 代表未获得）；条件期望即为事件发生概率。回归系数 $\beta_k$ 直接表示自变量 $X_k$ 变动一个单位时，事件发生概率上升或下降的绝对数值。[[Argument_Phyo_2025_SocSci|(Phyo & Ilie, 2025, p. 9)]]
>
> **符号说明**
> - $Y_i$：个体 $i$ 的二元结果取值。
> - $\mathbf{X}_i$：包含截距项的解释变量行向量。
> - $\boldsymbol{\beta}$：待估计边际概率系数向量。
> - $\varepsilon_i$：扰动项，其条件方差为 $P_i(1 - P_i)$，天然具有异方差性。
>
> **数学直觉** 将离散二值问题转化为条件期望的连续线性近似，避免了非线性 Logit/Probit 模型中因胜算比（Odds Ratio）跨组非可比或边际效应受样本分布基准影响的解释困难。
>
> > [!example]- 计算示例
> > 假设以最贫困五等分群体为参照组，较富裕组虚拟变量的回归系数为 $\beta = 0.155$（$p < 0.001$）。这表明在控制其他变量前提下，较富裕群体的入学会概率较基准贫困群体高出 15.5 个百分点。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 系数正负与量级 | 正系数代表发生概率增加，负系数代表发生概率受抑；数值即为绝对概率增减幅度。 |
> > | 注意 | 异方差假定 | 二元扰动项方差随自变量取值变动，常规 OLS 标准误存在偏误，必须使用稳健标准误纠正。 |

> [!formula-step] 步骤二　区域固定效应与交互项扩展
> $$Y_{ir} = \alpha + \boldsymbol{\beta}_1 \cdot \text{wealth}_{ir} + \boldsymbol{\beta}_2 \cdot \mathbf{X}_i + \boldsymbol{\beta}_3 \cdot (\text{wealth}_{ir} \times \text{gender}_{ir}) + \boldsymbol{\beta}_4 \cdot (\text{wealth}_{ir} \times \text{rural}_{ir}) + u_r + \varepsilon_{ir}$$
>
> **这个公式在做什么** 在基准模型中引入区域固定效应 $u_r$，吸纳地区间不随时间变异的资源禀赋差异；同时加入财富与性别、城乡属性的交互项，检验不同社会阶层内部的边缘化异质性。[[Argument_Phyo_2025_SocSci|(Phyo & Ilie, 2025, p. 9)]]
>
> **符号说明**
> - $Y_{ir}$：位于区域 $r$ 的个体 $i$ 的二元教育获得指示值。
> - $\text{wealth}_{ir}$：家庭财富五等分虚拟变量向量。
> - $u_r$：次国家层级区域固定效应，控制地理与地方资源异质性。
> - $\boldsymbol{\beta}_3, \boldsymbol{\beta}_4$：阶层与人口学属性的交叉交互系数。
>
> **数学直觉** 线性模型中的交互项系数可直接反映斜率的代数差异，无需像非线性模型那样通过二阶导数交叉项展开复杂的非线性边际效应校准。

> [!software-impl] 软件实现
> - **数据来源** 微观调查截面数据（如 DHS、MICS）。
> - **核心包或命令** Python 可使用 `statsmodels.formula.api.ols` 配备 `cov_type='HC1'`；R 可使用 `fixest::feols`；Stata 可使用 `reg y x, vce(robust)` 或 `reghdfe`。
> - **实现流程** 清洗并生成虚拟变量、构建公式字符串、拟合包含稳健协方差阵的模型、提取边际效应并进行敏感性检验。
> - **报告标准** 报告 OLS 系数、稳健标准误、观测样本量、调整后 $R^2$ 以及与 Logit 模型的稳健性对比结论。

> [!formula] Python 计算骨架
> ```python
> import statsmodels.formula.api as smf
> import pandas as pd
>
> # df 包含 y (0/1), wealth (Categorical), gender (0/1), rural (0/1), region (Categorical)
> formula = "y ~ C(wealth, Treatment(reference='Poorest')) + gender + rural + C(region)"
> model = smf.ols(formula, data=df).fit(cov_type='HC1')
> print(model.summary())
> ```

> [!method-stack] 变量与诊断
> - **数据结构** 大样本跨国分层整群微观抽样调查数据。
> - **变量** 因变量为高等教育获得二元变量；解释变量为财富五等分、性别、城乡区位及区域固定效应。
> - **识别假设** 误差项条件均值为零；在大样本下未观测因素被组内去均值或固定效应吸收。
> - **诊断与检验** 计算预测概率分布以排查越界比例；对比非线性二元选择模型（Logit/Probit）确保主结论与统计显著性方向稳健。

---

> [!method-fit] 适用判断
> - **适合使用** 核心研究目标关注解释变量的绝对边际效应；需要控制多维高维分类固定效应；模型包含大量复杂的交互项设定。[[Argument_Phyo_2025_SocSci|(Phyo & Ilie, 2025, p. 9)]]
> - **谨慎使用** 样本规模极小或平均事件发生率极低（如小于 1% 或大于 99%），此时预测值落于 $[0, 1]$ 之外的比例偏高。
> - **不适合使用** 研究首要目的在于对未来极端个体进行精确外推预测，且对预测概率落在有效区间有严格数学约束的工程场景。

---

> [!method-limits] 方法局限
> - **测量偏误** 扰动项方差依赖于均值分布，普通 OLS 标准误必然失真，未加稳健标准误修正时会导致假设检验严重偏差。
> - **越界预测问题** 线性假定在解释变量取极端值时可能得出负概率或大于 1 的无意义预测概率。
> - **误用风险** 忽略非线性关系在边界处的渐近与饱和特征。
> - **补救方式** 统一报告 Huber-White 异方差稳健标准误；采用二元 Logit/Probit 模型作为基准稳健性检验。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Higher Education Access]] | 测量对象 | 线性概率模型用于估计和解释社会阶层与人口学特征对高等教育获得概率的边际效应。 |
> | [[Maximally Maintained Inequality]] | 理论 | 用于检验教育扩张进程中优势群体与劣势群体相对获得概率差距演进的实证工具。 |
> | [[Binary Logistic Regression]] | 替代方法 | 将概率约束在区间内的非线性替代模型，二者常用作稳健性对照。 |
> | [[Multiple Regression]] | 上位方法 | 线性概率模型是将二值变量作为因变量的多元线性回归特例。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Phyo_2025_SocSci|Phyo and Ilie (2025)]] — 采用含地区固定效应的线性概率模型估计东南亚八国不同出生队列中财富、性别与城乡对高等教育获得率的边际效应及交互作用。
