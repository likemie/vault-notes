---
title: Factor Mixture Modeling
aliases:
  - "因子混合模型"
  - "FMM"
summary: "一种结合了验证性因子分析（Confirmatory Factor Analysis, CFA）与潜在剖面分析（Latent Profile Analysis, LPA）的量化方法。它能够通过考察个体在多维度连续潜在因子上的模式（轮廓）表现，识别出总体数据中隐含的异质性潜在类别（群组）。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 13
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags: []
related_concepts:
  - "[[Heterogeneity]]"
  - "[[Variable]]"
  - "[[Hypothesis]]"
  - "[[Epistemology]]"
  - "[[Sample Size Determination]]"
  - "[[Research Question]]"
  - "[[Questionnaire]]"
  - "[[Reliability]]"
  - "[[Null Hypothesis]]"
  - "[[Alternative Hypothesis]]"
related_theories: []
related_methods:
  - "[[Confirmatory Factor Analysis]]"
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

# Factor Mixture Modeling

---

## 定义

> [!def] 方法定义
> 因子混合模型（Factor Mixture Modeling, FMM）结合了因子分析降维测量的优势与潜在类别/剖面分析探究[[Heterogeneity|异质性]]的功能。它利用个体在多个连续的潜在因子（潜[[Variable|变量]]）上的表现特征，将其划分至具备不同特征轮廓（profile）的未知类群中。[[Argument_Greene_2010_JEP|(Greene et al., 2010, p. 239)]]

> [!method-scope] 方法范围
> - **研究对象** 具备多维测量结构并[[Hypothesis|假设]]存在群体异质性分类的数据。
> - **问题类型** 探索或验证异质样本中的亚群结构（如划分认知发展阶段类型）。
> - **分析单位** 个体。
> - **输出形式** 潜在类别分配、类别的因子均值轮廓图。

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 认为人类的心理或行为属性既具有多维度的连续特征，也在总体上包含本质不同的类别群体。
> - **研究者角色** 需要在各类拟合指数中选择合理的模型分类数目，并基于理论为不同类群特征赋予命名和实质解释。
> - **有效性标准** 赤池信息准则（Akaike Information Criterion, AIC）、贝叶斯信息准则（Bayesian Information Criterion, BIC）、[[Sample Size Determination|样本量]]调整后的贝叶斯信息准则（Sample-Size Adjusted BIC, SABIC）、洛-鲁-鲁比似然比检验（Lo-Mendell-Rubin likelihood ratio test, LMR）、自举似然比检验（Bootstrapped Likelihood Ratio Test, bLRT）以及模型分类熵（Entropy）。

> [!method-stack] 方法层级
> - **分析方法** 因子混合模型（FMM）。
> - **辅助技术** [[Confirmatory Factor Analysis|验证性因子分析]]（CFA）、潜在剖面分析（LPA）。

---

## 研究程序

> [!proc] 通用程序
> 1. 明确[[Research Question|研究问题]]、对象以及假定的[[Heterogeneity|异质性]]亚群结构。
> 2. 首先运行标准[[Confirmatory Factor Analysis|验证性因子分析]]（CFA），确认测量模型的合理性。
> 3. 拟合具有递增类别数目（如从2类到6类）的混合模型，并设定不同严格程度的方差/协方差等值限制（如 strict vs strong invariance）。
> 4. 使用多项拟合信息准则（如 AIC、BIC、bLRT 等）对比以确定最佳的类别数量模型。
> 5. 提取最优模型下各潜在类别的因子均值（轮廓特征），并结合理论对其进行实质性解释。

> [!method-stack] 数据、[[Variable|变量]]与模型
> - **数据结构** 常见为横截面量表数据（跨断面测量）或追踪数据（纵向混合模型）。
> - **样本与单位** [[Sample Size Determination|样本量]]要求较高（受模型复杂度和待估参数限制，通常需几百至上千样本量，否则极易不收敛）。分析单位为个体。
> - **变量或指标** 观测变量（如[[Questionnaire|问卷]]题项得分）、连续潜变量（因子分数）、类别潜变量（未知的异质性群组）。
> - **模型或统计量** 因子混合模型（FMM），输出包含类别概率、各类别下的潜因子均值及方差-协方差矩阵。
> - **诊断与检验** 信息准则（AIC、BIC、SABIC 越小越好）、似然比检验（LMR检验、bLRT检验考察 $K$ 类是否优于 $K-1$ 类）、模型收敛性检查、分类熵（Entropy，一般要求 > 0.8 以确保分类精度）。

> [!formula-step] 公式步骤　FMM 基础测量方程
> $$ y_{ik} = \nu_{k} + \lambda_{k} \eta_{ik} + \epsilon_{ik} $$
>
> **这个公式在做什么** 将针对潜因子的连续维度测量（CFA）与针对人群分类的潜在类别分析（LPA）融合，构建异质类别 $K$ 下观测变量与潜因子的回归方程。
>
> **符号说明** $y_{ik}$：个体 $i$ 在属于类别 $k$ 时的观测变量得分；$\nu_{k}$：类别 $k$ 的截距；$\lambda_{k}$：类别 $k$ 的因子载荷；$\eta_{ik}$：个体 $i$ 的连续潜在因子（如具体的心理测验得分）；$\epsilon_{ik}$：特定类别下的测量残差。
>
> **数学直觉** 传统的 CFA 只有一条全局方程，假定所有人同属一个同质群体；而传统的 LPA 只能基于含有测量误差的原始观测分（$y$）进行聚类。FMM 把两者的优势拼在了一起：它既用潜变量 $\eta$ 吸收了测量误差，又允许 CFA 的各个参数在 $K$ 个未知的异质性类别中**自由变化**。算法通过最大似然估计，从数据中“盲抽”出在各个潜因子上表现出特定模式（如“高-低-中”）的典型特征亚群。
>
> **结果怎么读** 跑完模型后，主要看提取出的 $K$ 个类别的**联合轮廓图（Profile）**。如果设定 $K=6$ 的模型在信息准则（BIC、SABIC 越小越好）上拟合最优，说明样本整体在数学上可以稳定划分为六类截然不同的人群。
>
> **注意事项** 模型对起点的初值极为敏感，常面临局部极值和不收敛问题（尤其是强制进行强等值检验时）。因此算法提取出的类别数目必须结合领域理论进行实质性解释，否则容易导致过度拟合。

> [!formula-step] 公式步骤　贝叶斯信息准则（BIC）
> $$ BIC = -2 \log(L) + p \ln(n) $$
>
> **这个公式在做什么** 平衡模型的拟合优度与模型复杂度，用于在不同类别数（$K$）的候选模型中挑选最优的潜类别模型。
>
> **符号说明** $L$ 是模型的最大似然函数值；$p$ 是模型中需要自由估计的参数数量；$n$ 是样本量。
>
> **数学直觉** 对数似然值（$\log L$）越大，说明模型对数据的拟合越好，但一味增加潜在分类数 $K$ 会导致参数量 $p$ 激增，引发过拟合风险。因此公式的后半部分 $p \ln(n)$ 作为“惩罚项”：类别分得越碎、参数越多，惩罚就越重。
>
> **结果怎么读** 数值**越小越好**。通常需要平行对比 $K=2, 3, 4, ...$ 等一系列模型，找出 BIC 达到最小或者呈现明显下降拐点（Elbow）对应的模型类别数。
>
> **注意事项** SABIC（Sample-Size Adjusted BIC）是对小样本特化的变体，它用 $(n+2)/24$ 替代公式中的 $n$ 以减轻惩罚。FMM 普遍高度依赖 BIC / SABIC 作为“定类”的首要客观指标。

> [!formula-step] 公式步骤　分类熵（Entropy）
> $$ Entropy = 1 - \frac{\sum_{i=1}^{n} \sum_{k=1}^{K} -p_{ik} \ln(p_{ik})}{n \ln(K)} $$
>
> **这个公式在做什么** 量化 FMM 模型把个体划分到各自类别时的不确定性与分类清晰度。
>
> **符号说明** $p_{ik}$ 是模型估计出的个体 $i$ 属于类别 $k$ 的后验概率；$n$ 为总样本量；$K$ 为类别总数。
>
> **数学直觉** 借用了信息论中“熵”的概念。如果模型分类极度清晰（某人以 99% 的概率属于 A 类，且 0% 属于其他类），那么 $p_{ik} \ln(p_{ik})$ 就会趋近于 0，此时 Entropy 接近 1。反之，如果一个人属于 A 类的概率是 50%，B 类也是 50%（完全模棱两可），分类的不确定性（惩罚项）达到最大，Entropy 趋近于 0。
>
> **结果怎么读** 范围在 0 到 1 之间，**越接近 1 越好**。业界普遍以 **0.80** 作为优良线，代表类别划分清晰，样本个体的归属具有高可[[Reliability|信度]]。
>
> **注意事项** Entropy 高只代表“在当前划分下，人与类别的从属关系很明确”，并不代表当前的分类数量 $K$ 就是最符合真理的最佳结构。因此，不能单纯为了追求高 Entropy 而随意削减或增加类别，它必须配合 BIC 与 bLRT 等拟合指标综合判断。

> [!formula-step] 公式步骤　似然比检验（LRT, LMR / bLRT）
> $$ LR = -2 \log \left( \frac{L_{K-1}}{L_K} \right) = -2 (\log L_{K-1} - \log L_K) $$
>
> **这个公式在做什么** 通过[[Hypothesis|假设]]检验的方式，直接比较 $K-1$ 个类别的模型（[[Null Hypothesis|零假设]]）与 $K$ 个类别的模型（[[Alternative Hypothesis|备择假设]]），判断增加一个类别是否能带来统计学上显著的拟合提升。
>
> **符号说明** $L_K$ 是 $K$ 类模型的最大似然函数值；$L_{K-1}$ 是少一类的模型的似然函数值。
>
> **数学直觉** 如果把人群分为 $K$ 类比分为 $K-1$ 类好得多，那么 $K$ 类模型的似然值（$L_K$）就会远大于 $L_{K-1}$，从而产生一个很大的 $LR$ 统计量。传统[[Chi-Squared Test|卡方检验]]在这里不适用，因此 **LMR**（Lo-Mendell-Rubin检验）提供了一种解析近似的理论分布来算 $p$ 值；而 **bLRT**（Bootstrapped LRT）则是通过计算机反复重抽样（Bootstrap）来暴力模拟出统计量的真实经验分布，精度更高。
>
> **结果怎么读** 核心看检验给出的显著性 $p$ 值。如果 $p < .05$，拒绝零假设，说明增加类别带来了显著提升（即 $K$ 类比 $K-1$ 类好，保留 $K$ 类）；如果 $p > .05$，说明强行增加一类纯属画蛇添足，此时应当“退回”到更简洁的 $K-1$ 类别模型。
>
> **注意事项** bLRT 被统计学界公认在决定 FMM 分类数量时比 LMR 更为准确稳健，但它的重抽样计算过程非常耗时。实操中，研究者通常会寻找 BIC 下降趋势变缓的“拐点”，以及 bLRT 从显著（$p<.05$）变为不显著（$p>.05$）的临界点，两者结合敲定最终类别数。

> [!software-impl] 软件实现
> - **数据处理** 多采用全息极大似然估计（Full Information Maximum Likelihood, FIML）处理缺失值，确保各维度变量数据类型和尺度的正确设定。
> - **推荐软件** Mplus（最为成熟的主流选择）、R。
> - **核心包或命令** Mplus 中通过 `TYPE=MIXTURE` 语句开启；R 中常配合 `MplusAutomation` 批量调用 Mplus 代码，或使用 `tidyLPA`、`flexmix` 包探索类似模型。
> - **实现流程** 1. 首先运行单组 CFA 确认整体测量结构；2. 设定循环（如 $K=2$ 到 $6$）拟合含有不同群组数的混合模型；3. 对参数进行不同程度的等值约束（如载荷相等）；4. 汇总信息准则与检验结果判定最佳类别数；5. 导出类别的边际概率与联合轮廓图。
> - **报告标准** 必须报告多模型对比适配度表（含类别数、对数似然值、AIC、BIC、SABIC、Entropy、LMR/bLRT 的 $p$ 值），并绘制最终模型各个类群在各维度上的轮廓折线图与样本规模占比。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 具有深层分类学假说、需要在多维度上综合识别异质发展阶段群体的研究场景。[[Argument_Greene_2010_JEP|(Greene et al., 2010, p. 239)]]

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源** 对起点的初值较为敏感，极大可能面临局部极值和不收敛问题，通常需要充足的[[Sample Size Determination|样本量]]；另外潜在类群的实质解释依赖研究者的理论预设，有主观色彩。

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Greene_2010_JEP]] — 该研究通过因子混合模型，将大样本学生在[[Epistemology|认识论]]维度上的测量得分有效聚类为了理论预设的四个阶段组。
