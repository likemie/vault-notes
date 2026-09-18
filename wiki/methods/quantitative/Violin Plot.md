---
title: Violin Plot
aliases:
  - 小提琴图
  - 核密度小提琴图
summary: "一种结合箱线图与核密度估计的定量数据可视化方法，由 Hintze & Nelson（1998）提出。通过对称的平滑密度轮廓展示连续变量的概率分布形态、多峰特征与四分位统计量，常用于不同组别或模型提取结果在连续尺度上的分布对齐性检验。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 19
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/data-visualization
  - method/quantitative
  - method/descriptive-statistics
related_concepts:
  - "[[Variable]]"
  - "[[Unit of Analysis]]"
  - "[[Document]]"
  - "[[Epistemology]]"
  - "[[Heterogeneity]]"
  - "[[Dependent Variable]]"
  - "[[Independent Variable]]"
  - "[[Visible Learning]]"
related_theories: []
related_methods:
  - "[[Effect Size]]"
  - "[[Meta-analysis]]"
  - "[[Sample Size Determination]]"
  - "[[Analysis of Variance]]"
  - "[[Inter-Rater Reliability]]"
  - "[[Questionnaire]]"
  - "[[Coding in Qualitative Research]]"
  - "[[UpSet Plot]]"
  - "[[Intraclass Correlation Coefficient]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Jansen_2026_EPR]]"
confidence: high
status: active
created: 2026-09-18
updated: 2026-09-18
---

# Violin Plot

---

## 定义

> [!def] 方法定义
> **小提琴图（Violin Plot）**是一种用于呈现连续数值型[[Variable|变量]]概率分布与汇总统计量的定量数据可视化方法，由杰里·欣策与雷·纳尔逊（Hintze & Nelson, 1998）正式提出。该方法在传统箱线图（Box Plot）的基础上，沿中心对称轴融合了连续变量的平滑双侧**核密度估计（Kernel Density Estimation, KDE）**，能够在紧凑的空间中同时展示数据的集中趋势（中位数）、离散程度（四分位距与极值）以及潜在的多峰（Multimodal）、偏态（Skewness）与厚尾形态。[[Argument_Jansen_2026_EPR|(Jansen et al., 2026, pp. 15–16)]]

> [!method-scope] 方法范围
> - **研究对象** 连续型数值变量、模型预测输出、[[Effect Size|效应量]]分布、评分数据或多组实验测量值。
> - **问题类型** 适合回答多组别分布形状对比、分布对齐性检验、非正态性与多峰识别、以及极值与离散程度辨析。
> - **[[Unit of Analysis|分析单位]]** 观测值、被试得分、[[Meta-analysis|元分析]]效应量、[[Document|文献]]提取指标或模型参数。
> - **输出形式** 水平或垂直排列的多组对称密度外轮廓，内部内嵌微型箱线图、中位数标记点或散点抖动（Jitter）。

> [!citation-card] 小提琴图的视觉统合逻辑
> 小提琴图将箱线图的汇总统计优势与核密度估计对复杂分布形态的敏感性结合在一起。它能够在一幅图形中清晰揭示被传统五数概括法所掩盖的双峰、多峰与聚类特征，使跨组分布对比更为严密与直观。(Hintze & Nelson, 1998; Jansen et al., 2026)
>
> *"The violin plot combines the box plot with a rotated kernel density plot to create a visualization that shows the density shape of the data. It is particularly useful when comparing multimodal distributions across multiple categories where a standard box plot would hide clustering features."*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 将经验测量数据视为底层连续概率生成过程的样本实现；强调仅凭均值、方差或四分位数等点估计不足以完整刻画数据特征，必须保留连续分布的几何轮廓以避免汇总统计量造成的认知降维偏误。
> - **研究者角色** 研究者需在核密度平滑带宽（Bandwidth）的选择上做出方法学审慎权衡：过大带宽导致过度平滑掩盖真实特征，过小带宽导致假性噪点扰动；同时负责确定是否裁剪超出理论边界的密度尾翼（如非负[[Variable|变量]]的截断）。
> - **有效性标准** 核函数的数学适切性、带宽选取的理论合规度（如 Silverman 经验法则）、[[Sample Size Determination|样本量]]对密度估计的支撑度（通常要求每组 $N \ge 30$）。
> - **不声称回答的问题** 小提琴图本身属于描述性与探索性分析方法，不能替代针对组间差异的推断统计检验（如[[Analysis of Variance|方差分析]]、独立样本 $t$ 检验或 Kolmogorov-Smirnov 检验）。

> [!method-stack] 方法层级
> - **研究设计** 跨组准实验对比、多[[Inter-Rater Reliability|评分者信度]]研究、大语言模型基准评测、[[Meta-analysis|元分析]][[Heterogeneity|异质性]]探索。
> - **数据收集** 连续型实验测量、学术[[Document|文献]]参数提取、[[Questionnaire|问卷]]连续题项总分、模型统计参数。
> - **分析方法** 非参数核密度估计（KDE）、箱线图五数概括（极小值、$Q_1$、中位数、$Q_3$、极大值）。
> - **辅助技术**
>   - R 语言生态：`ggplot2::geom_violin()`、`vioplot`
>   - Python 生态：`seaborn.violinplot()`、`matplotlib.pyplot.violinplot()`
>   - Stata 生态：`vioplot` 命令

---

## 研究程序

> [!proc] 通用程序
> 1. **数据准备与分组标定** 整理包含连续[[Dependent Variable|因变量]]（如综合[[Effect Size|效应量]] $d$）与离散分类[[Independent Variable|自变量]]（如[[Coding in Qualitative Research|编码]]主体：金标准、专家、LLMs）的长表数据集。
> 2. **参数设定与核密度估计** 针对每个组别独立拟合核密度曲线，推荐采用高斯核函数（Gaussian Kernel），并检验默认平滑带宽的拟合效果。
> 3. **边界控制与截断处理** 依据[[Variable|变量]]的理论取值域（如研究篇数 $k$ 与[[Sample Size Determination|样本量]] $N$ 必须为非负整数）设置核密度估计的极值边界截断，避免虚假的负值延伸。
> 4. **嵌套汇总统计标记** 在对称小提琴外廓内部内嵌深色粗线条展示四分位距（IQR），以白色圆点标示中位数，或保留须线标示非异常值范围。
> 5. **并列对齐与分布研判** 将各组小提琴图并列在同一基准线上，比较各组分布的对称性、宽度、峰度及中位数对齐程度。

### 量化可视化模块

> [!method-stack] 图形构件与核密度原理
> - **外侧对称密度轮廓（Density Contour）** 轮廓的宽度代表数据在该数值处的概率密度大小；小提琴“肚子”最宽处即数据频次最集中的众数区域；轮廓变窄表示频数稀疏。
> - **内部微型箱线图（Embedded Box Plot）**
>   - **中位数标记（Median Marker）** 通常为高亮白色实心圆点或黑色横线，反映组别集中趋势；
>   - **四分位黑条（Interquartile Range Bar）** 位于对称轴中心的深色粗矩形，覆盖第 25 百分位数（$Q_1$）至第 75 百分位数（$Q_3$），长度即 IQR；
>   - **外延细须线（Whiskers）** 延伸至 $1.5 \times \text{IQR}$ 范围内的极值，反映除极端异常值外的数据覆盖区间。
> - **半小提琴与云雨图拓展（Raincloud Plot Extension）** 在复杂情境下可采用单侧小提琴（半小提琴图），配合另一侧的原始散点抖动图（Jittered Points），同时达成宏观密度与微观原始个案的同步呈现。

> [!software-impl] 软件实现
> - **R 语言生态（`ggplot2` 经典代码）**
>   ```r
>   library(ggplot2)
>   ggplot(df, aes(x = rater, y = effect_size, fill = rater)) +
>     geom_violin(trim = FALSE, alpha = 0.5) +
>     geom_boxplot(width = 0.15, fill = "white", color = "black", outlier.shape = NA) +
>     theme_minimal()
>   ```
> - **Python 生态（`seaborn` 经典代码）**
>   ```python
>   import seaborn as sns
>   import matplotlib.pyplot as plt
>   sns.violinplot(x='Model', y='Accuracy', data=df, inner='box', palette='muted')
>   plt.show()
>   ```

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**
>   - 多组别连续[[Variable|变量]]的宏观概率分布对齐性检验（如检验大语言模型与人类专家在提取[[Effect Size|效应量]] $d$、研究数 $k$ 与[[Sample Size Determination|样本量]] $N$ 时是否存在系统性偏倚或尺度偏移）。[[Argument_Jansen_2026_EPR|(Jansen et al., 2026, pp. 15–16)]]
>   - 识别存在双峰或多峰现象的复杂分布（传统箱线图会将双峰误判为普通的宽分布）。
>   - 样本量中等偏大（每组 $N \ge 30$，最好 $N \ge 100$）的统计结果呈现。
> - **谨慎使用**
>   - 样本量过小（$N < 20$）时，核密度估计严重依赖少数极端点，容易产生虚假的光滑起伏，此时应退化为普通箱线图叠加全样本散点。
> - **不适合使用**
>   - 离散程度极低或仅包含有限离散整数的有序分类变量。

---

## 局限性

> [!method-limits] 方法局限
> - **小样本伪密度与伪多峰** 当[[Sample Size Determination|样本量]]匮乏时，核密度平滑算法可能平滑出实际上并不存在的连续形态或局部假峰，造成过度解读。
> - **边界泄漏（Boundary Leakage）** 默认高斯核估计会将处于边界截断的数据向两侧溢出平滑，可能导致非负[[Variable|变量]]（如样本量、年龄、考试成绩）在图中延伸至不可能的负值区域，必须手动设置理论截断（`trim = TRUE` 或指定下界）。
> - **不展示原始数据点数量** 纯小提琴图无法直观反映不同组别之间的样本量悬殊（如 A 组 500 人与 B 组 30 人可能呈现外形完全一致的小提琴），建议结合组样本量标签或散点抖动展示。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[UpSet Plot]] | 补充方法 | 结合使用：小提琴图评测连续[[Variable\|变量]]分布重叠度，UpSet Plot 解构离散多分类交集分歧。 |
> | [[Effect Size]] | 分析对象 | 小提琴图常用于展示元分析中不同干预亚组间效应量 $d$ 的异质性分布形态。 |
> | [[Intraclass Correlation Coefficient]] | 补充方法 | 检验多组评分者间一致性的量化系数，小提琴图为其提供直观的概率分布重合佐证。 |
> | [[Meta-analysis]] | 应用场景 | 用于展示初审与终审研究效应量的总体分布密度与偏态特征。 |
> | [[Argument_Jansen_2026_EPR\|Jansen et al. (2026)]] | 关键论证 | 论文图 2 运用小提琴图直观证实大模型与人类专家在三大统计变量上具备高度一致的概率分布特征。 |

---

## 使用此方法的研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Jansen_2026_EPR|Jansen et al. (2026)]] — 在《[[Visible Learning|可见的学习]]》156 项一阶[[Meta-analysis|元分析]]的大模型提取评测中绘制图 2，运用小提琴图系统比较人类专家、既有数据库与三大前沿大语言模型在综合[[Effect Size|效应量]] $d$、研究数 $k$ 与学生[[Sample Size Determination|样本量]] $N$ 上的概率密度轮廓，实证证实模型与金标准的统计分布完全对齐。
