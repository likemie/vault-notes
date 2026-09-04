---
title: Multinomial Logistic Regression
aliases:
  - "多项逻辑回归"
  - "Multinomial Logit Model"
summary: "一种用于预测名义变量（包含两个以上无序类别）的广义线性回归模型。常用于分类预测或探究自变量对个体归属于特定群体几率的影响。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 12
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags: []
related_concepts:
  - "[[Dependent Variable]]"
  - "[[Variable]]"
  - "[[Independent Variable]]"
  - "[[Epistemology]]"
  - "[[Hypothesis]]"
  - "[[Standard Error]]"
  - "[[Sample Size Determination]]"
  - "[[Academic Achievement]]"
  - "[[Educational Level]]"
related_theories: []
related_methods:
  - "[[Binary Logistic Regression]]"
  - "[[Chi-Squared Test]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Greene_2010_JEP]]"
confidence: medium
status: draft
created: 2026-08-15
updated: 2026-08-15
---

# Multinomial Logistic Regression

---

## 定义

> [!def] 方法定义
> 多项逻辑回归（Multinomial Logistic Regression）是[[Binary Logistic Regression|二元逻辑回归]]的扩展，用于当[[Dependent Variable|因变量]]分类数大于 2 且各类别之间没有内在大小或顺序（即名义[[Variable|变量]]）时的回归分析。它通过设定一个“基准类别”（Reference Category），分别计算其他类别相对于基准类别的对数胜率（Log-odds）。

> [!method-scope] 方法范围
> - **研究对象** 截面数据或调查数据。
> - **问题类型** 预测个体归属于某一无序类别的概率，或检验特定[[Independent Variable|自变量]]对分类归属的显著影响。
> - **分析单位** 个体。
> - **输出形式** 回归系数估计值 $b$、胜率比（Odds Ratio, OR 或 $e^b$）、分类预测概率。

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 认为个体的类别归属受到多个可测量因素的影响，且这种影响可以通过概率论进行量化估计。
> - **有效性标准** 伪 $R^2$（Pseudo $R^2$）、似然比检验（Likelihood Ratio Test）、分类准确率。

> [!method-stack] 方法层级
> - **分析方法** 多项逻辑回归。

---

## 研究程序

> [!proc] 通用程序
> 1. 明确一个无序多分类的[[Dependent Variable|因变量]]，并选定一个具有解释意义的分类作为“基准参照组”。
> 2. 将名义型的[[Independent Variable|自变量]]转化为哑[[Variable|变量]]（Dummy Variables）。
> 3. 拟合模型，考察自变量的系数显著性。
> 4. 将对数几率系数转化为胜率比（$e^b$）进行实质性解释。

### 量化方法模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 横截面数据。
> - **变量或指标** 因变量必须是名义分类变量（如：分流后的轨道类型、潜在类别群组），自变量可为连续或分类变量。
> - **诊断与检验** 多重共线性诊断、独立无关替换[[Hypothesis|假设]]检验（IIA, Independence of Irrelevant Alternatives）。

> [!formula-step] 公式步骤　多项逻辑回归模型
> $$ \ln\left(\frac{P(Y=k)}{P(Y=K)}\right) = \beta_{0k} + \beta_{1k}X_1 + \dots + \beta_{pk}X_p $$
>
> **这个公式在做什么** 计算个体属于目标类别 $k$ 与属于基准类别 $K$ 的胜率（几率）比值的自然对数，并将其表示为预测变量的线性组合。
>
> **符号说明** $Y$ 是因变量，$K$ 是设定的基准类别；$X$ 是自变量；$\beta$ 是偏回归系数。
>
> **数学直觉** 强行预测“某个类别”很难，所以模型退而求其次，预测“选类别 $k$ 而不选基准类别 $K$ 的相对倾向”。
>
> **结果怎么读** 这是原始的回归系数 $\beta$。通常我们不会直接解释 $\beta$，而是将其取指数转化为胜率比（Odds Ratio）来解释。

> [!formula-step] 公式步骤　胜率比（Odds Ratio, OR）
> $$ OR = e^\beta $$
>
> **这个公式在做什么** 将反人类直觉的“对数几率”（Log-odds）转换成现实世界中容易理解的“倍数”关系。
>
> **数学直觉** 逻辑回归的原始输出 $\beta$ 告诉你“自变量增加1个单位，对数几率变了多少”。通过取自然指数 $e^\beta$，它变成了我们熟悉的话语：如果自变量 $X$ 增加一个单位，个体落入目标类别 $k$ （相较于基准类别 $K$）的几率就会变成原来的 $e^\beta$ 倍。
>
> **结果怎么读** 如果 $OR > 1$，说明自变量增加了进入目标类别 $k$ 的几率（正向预测）；如果 $0 < OR < 1$，说明降低了该几率（负向预测）；如果 $OR = 1$，说明该变量没影响。

> [!formula-step] 公式步骤　麦克法登伪 $R^2$（McFadden's Pseudo $R^2$）
> $$ R_{McFadden}^2 = 1 - \frac{\ln(L_{model})}{\ln(L_{null})} $$
>
> **这个公式在做什么** 评估模型整体上对数据的拟合和解释程度（类似于线性回归中的 $R^2$，但含义并非“解释了百分之多少的方差”）。
>
> **符号说明** $L_{model}$ 是当前包含所有自变量的完整模型的似然值；$L_{null}$ 是只包含截距（没有任何预测变量）的空模型的似然值。
>
> **数学直觉** 如果你的自变量群非常有用，模型似然值（$L_{model}$）就会远大于空模型的似然值（$L_{null}$），从而让对数比值变小，使得 $R^2$ 远离 0。它衡量的是你的模型比“瞎猜”（空模型）进步了多少。
>
> **结果怎么读** 范围在 0 到 1 之间，**越大越好**。注意：在逻辑回归中，伪 $R^2$ 通常普遍偏低，一般达到 0.2 到 0.4 之间就已经被业界公认是一个拟合极其出色的模型了。

> [!formula-step] 公式步骤　整体拟合似然比检验（Likelihood Ratio Test）
> $$ G^2 = -2 \ln(L_{null}) - (-2 \ln(L_{model})) = -2 \ln\left(\frac{L_{null}}{L_{model}}\right) $$
>
> **这个公式在做什么** 从统计推断的角度，检验你辛辛苦苦找来的这堆自变量是否真的一起发挥了作用，还是说它们全都是在“浑水摸鱼”。
>
> **数学直觉** 算出空模型的“不拟合度”（$-2\ln L$ 代表 Deviance 偏差）减去当前模型的“不拟合度”。如果差值（$G^2$ 卡方统计量）足够大，就说明这组自变量切实地、显著地填补了模型解释力的空白。
>
> **结果怎么读** 看[[Chi-Squared Test|卡方检验]]给出的 $p$ 值。如果 $p < .05$，说明模型整体是有意义的，成功拒绝了“所有自变量系数全为0”的零假设。

> [!software-impl] 软件实现
> - **推荐软件** R（`nnet` 包中的 `multinom()` 函数）、SPSS、Stata。
> - **报告标准** 必须说明哪个类别是基准类别。报告系数 $b$、[[Standard Error|标准误]]、Wald 检验的显著性 $p$ 值以及胜率比 $e^b$。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 探究学生职业选择、潜类别成员归属等无序多分类[[Dependent Variable|结果变量]]的影响因素。

---

## 局限性

> [!method-limits] 方法局限
> - **适用边界** 需要满足 IIA [[Hypothesis|假设]]（各类别间的选择几率不依赖于是否存在其他类别）。如果类别间存在极强的相互替代性，应考虑其他模型（如嵌套 logit 模型）。
> - **偏误来源** 当某一类别的[[Sample Size Determination|样本量]]极小时，极大似然估计可能不收敛或产生极大的[[Standard Error|标准误]]。

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Greene_2010_JEP|Greene et al. (2010)]] —  使用多项逻辑回归（Multinomial Logistic Regression），以[[Academic Achievement|学业成绩]]和[[Educational Level|受教育年限]]为[[Independent Variable|自变量]]预测个体归属特定[[Epistemology|认识论]]类别阶段的概率。
