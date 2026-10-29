---
title: Pearson Product-Moment Correlation
aliases:
  - Pearson相关
  - 皮尔逊相关
  - Pearson's correlation
  - Pearson's r
  - 积差相关
  - 皮尔逊积差相关
  - Product-Moment Correlation Coefficient
summary: "测量两个连续变量间双变量线性关联强度与方向的推断统计量，通过协方差与两变量标准差之积的比值标准化至 [-1, +1] 区间"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 38
method_related_level: 3
method_related_stars: "💎"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/statistical
  - quantitative-research
  - correlation
  - statistics/bivariate
  - theme/effect-size
related_concepts:
  - "[[Variable]]"
  - "[[Academic Achievement]]"
  - "[[Unit of Analysis]]"
  - "[[Study Population and Sample]]"
  - "[[Epistemology]]"
  - "[[Positivism]]"
  - "[[Postpositivism]]"
  - "[[Reliability]]"
  - "[[Causality]]"
  - "[[Scale of Measurement]]"
  - "[[Achievement and Aptitude Tests]]"
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Research Question]]"
  - "[[Zone of Desired Effects]]"
  - "[[Visible Learning]]"
  - "[[Category Mistake]]"
  - "[[Creativity]]"
  - "[[Creativity Training]]"
  - "[[Heterogeneity]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Confidence Interval]]"
  - "[[Correlational Research]]"
  - "[[Survey Research]]"
  - "[[Non-intervention Research]]"
  - "[[Questionnaire]]"
  - "[[Effect Size]]"
  - "[[Multiple Regression]]"
  - "[[Meta-regression]]"
  - "[[Meta-meta-analysis]]"
  - "[[Sample Size Determination]]"
  - "[[Effect Size Conversion]]"
related_instruments: []
related_persons:
  - "[[Karl Pearson]]"
  - "[[Francis Galton]]"
  - "[[Pierre-Jérôme Bergeron]]"
related_facts: []
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Bergeron_2017_MJE]]"
  - "[[Argument_Runco_2026_CRJ]]"
confidence: high
status: active
created: 2026-05-31
updated: 2026-10-29
---

---

> [!def] Pearson Product-Moment Correlation
> 皮尔逊积差相关（Pearson Product-Moment Correlation，简称 Pearson 相关），由[[Karl Pearson|卡尔·皮尔逊]]（[[Karl Pearson]]）基于[[Francis Galton|弗朗西斯·高尔顿]]的工作系统化推导提出，是一种测量两个连续[[Variable|变量]]之间双变量（bivariate）线性关联系数和关联方向的基础推断统计方法，使用统计量 $r$ 呈现。该统计量严格界定在 $[-1, +1]$ 区间内：正值指示两变量同步增减的正向共变，负值指示反向变动，零值指示不存在线性相关趋势（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）。

> [!method-scope] 方法范围
> - **研究对象** 两个等距或等比尺度的连续测量变量（如认知测验得分、[[Academic Achievement|学业成绩]]、标准化量表连续总分等）。
> - **问题类型** 探索或检验两变量是否存在统计学上的线性共变模式，评估关联的紧密程度与变化方向。
> - **[[Unit of Analysis|分析单位]]** 包含成对测量数据的个体、班级、学校、年份或[[Meta-analysis|元分析]]中的实证[[Study Population and Sample|研究样本]]。
> - **输出形式** 积差相关系数 $r$、决定系数 $R^2$、双尾或单尾显著性检验 $p$ 值以及对应[[Confidence Interval|置信区间]]。

> [!citation-card] 关键定义
> Pearson 相关属于双变量推断统计，报告时统计符号 $r$ 须以斜体呈现，核心功能在于量化两个连续变量间关联的强度与方向。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, Ch8, Table 8.3)]]
>
> *Pearson correlation (r) relates two continuous variables to examine the strength and direction of the association.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** [[Positivism|实证主义]]与[[Postpositivism|后实证主义]]视角下对客观可观察量度之间共变规律的经验概括；将关联视为[[Variable|变量]]间协同波动的统计现象。
> - **研究者角色** 客观分析者，负责检验数据分布形态、甄别离群异常值并依据统计效度规程客观呈现关联系数。
> - **有效性标准** 满足双变量正态分布假设、测量[[Reliability|信度]]与效度保障、无极端异常点干扰以及足够的统计功效（Statistical Power）。
> - **不声称回答的问题** 明确不能直接推断变量间的因果决定机制（[[Causality|因果推断]]），亦不能测量非线性（如 U 型或倒 U 型）动态关联模式。

> [!method-stack] 方法层级
> - **研究设计** [[Correlational Research|相关性研究]]（Correlational Research）、[[Survey Research|调查研究]]（Survey Research）、横断面实证设计与[[Non-intervention Research|非干预研究]]。
> - **数据收集** 心理[[Scale of Measurement|测量量表]]、标准化[[Achievement and Aptitude Tests|成就测验]]、学籍管理系统连续成绩及[[Questionnaire|问卷]]连续评分。
> - **分析方法** 双变量协方差矩阵分解、点二列相关扩展、显著性 $t$ 检验及 Fisher's $z$ 变换。
> - **辅助技术** 散点图可视化检验、Cook 距离与马氏距离异常值诊断、残差正态性检验。

---

> [!proc] 双[[Variable|变量]]相关分析通用程序
> 1. 明确[[Independent Variable|自变量]]与[[Dependent Variable|因变量]]的理论概念界定，确认二者均具备等距或等比测量属性。
> 2. 绘制双变量双向散点图，直观审视变量间形态是否符合线性关系假定，排查离群极端值与强影响点。
> 3. 检验变量边缘分布与联合分布的正态性特征，确认满足双变量正态性假设前提。
> 4. 计算两变量协方差与各自标准差乘积的比值，求得样本相关系数 $r$ 及其对应的双尾 $p$ 值与[[Confidence Interval|置信区间]]。
> 5. 结合[[Effect Size|效应量]]标准与决定系数 $R^2 = r^2$ 解释方差贡献度，并在研究报告中按规范格式呈现相关矩阵。

> [!ref-table] Creswell 量化统计模型选择标准矩阵
> | [[Research Question\|研究问题]]性质 | 自变量数 | 因变量数 | 协变量数 | 变量类型 | 分数分布 | 统计方法与符号 | 模型功能说明 |
> |---|---|---|---|---|---|---|---|
> | 变量关联 | 1 | 1 | 0 | 连续／连续 | 正态 | [[Pearson Product-Moment Correlation\|Pearson 相关]]（$r$） | 两变量关联的强度与方向 |
> | 变量关联 | $\ge 2$ | 1 | 0 | 连续／连续 | 正态 | [[Multiple Regression\|多元回归]]（$R^2, F, b, t$） | 评估多预测变量对单一结果变量的相对预测力 |
> | 组间比较 | $\ge 1$ | 1 | 0 | 类别／连续 | 正态 | 方差分析（ANOVA, $F$） | 检验两组或多组均值差异 |
> | 组间比较 | $\ge 1$ | 1 | 1 | 类别／连续 | 正态 | 协方差分析（ANCOVA, $F$） | 控制协变量后比较各组均值差异 |
> | 组间关联 | 1 | 1 | 0 | 类别／类别 | 非正态 | 卡方检验（$\chi^2$） | 检验两个分类变量的列联关联 |
>
> *来源：[[Argument_Creswell_2022_SAGE|Creswell & Creswell (2022, Ch8, Table 8.3)]]*

---

> [!formula-step] 公式步骤　皮尔逊积差相关系数定义方程
> $$r = \frac{\sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^n (X_i - \bar{X})^2 \sum_{i=1}^n (Y_i - \bar{Y})^2}} = \frac{s_{XY}}{s_X s_Y}$$
>
> **这个公式在做什么** 将两连续[[Variable|变量]]的样本协方差除以两变量样本标准差之乘积，消除度量单位影响并输出无量纲关联系数 $r$。
>
> **符号说明**
> - $X_i, Y_i$：第 $i$ 个样本观测单位在两变量上的测定取值。
> - $\bar{X}, \bar{Y}$：两变量在总体样本中的算术平均值。
> - $s_{XY}$：两变量的样本协方差（Covariance）。
> - $s_X, s_Y$：两变量各自的样本标准差（Standard Deviation）。
>
> **数学直觉** 公式分子计算各观测点在两维度上离均差乘积的总和。若大部分样本点落在第一和第三象限（即同向高于均值或同向低于均值），离均差乘积为正，分子呈正值；反之落在第二和第四象限则为负值。分母为两变量总离差平方和的几何平均值，起到严格规范化作用，保证结果落入 $[-1, +1]$。
>
> **结果怎么读**
> - $r = +1.0$：两变量呈现完全正向线性共变。
> - $r = 0.0$：两变量间不存在可检测的线性相关结构。
> - $r = -1.0$：两变量呈现完全负向线性共变。
>
> **注意事项** 该公式要求变量间呈线性形态；极端离群点会剧烈扭曲分子协方差乘积，导致 $r$ 虚高或骤降。

> [!formula-step] 公式步骤　决定系数与方差解释度
> $$R^2 = r^2$$
>
> **这个公式在做什么** 计算两变量线性回归模型中[[Independent Variable|自变量]]对[[Dependent Variable|因变量]]总方差的解释比例（Coefficient of Determination）。
>
> **数学直觉** 在一元线性最小二乘模型中，回归平方和占总离差平方和的比例严格等价于皮尔逊相关系数的平方。
>
> **结果怎么读** $R^2$ 衡量预测确定性。例如 $r=0.196$ 时，$R^2 = (0.196)^2 \approx 0.0385$，表示一个变量仅能解释另一个变量 3.85% 的离散波动，剩余 96.15% 属于无法由该线性关系说明的噪声（[[Argument_Bergeron_2017_MJE|Bergeron & Rivard, 2017, p. 242]]）。

> [!formula-step] 公式步骤　相关系数向 Cohen's d 换算与渐近发散公式
> $$d = \frac{2r}{\sqrt{1 - r^2}}, \quad \lim_{r \to 1^-} d = +\infty$$
>
> **这个公式在做什么** 接收双变量相关系数 $r$，尝试映射为标准化组间均值差指标 Cohen's $d$（[[Argument_Bergeron_2017_MJE|Bergeron & Rivard, 2017, p. 242]]）。
>
> **数学直觉与渐近边界** 当 $r$ 趋近于 1.0 时，分母 $\sqrt{1-r^2}$ 迅速收敛逼近 0，导致换算后的 $d$ 产生趋于无穷大的发散性爆炸。更为关键的是，该非线性函数对弱相关产生大幅度的数值放大效应。
>
> **理论先决条件** 依据 Borenstein et al. (2009) 的数理证明，该换算公式仅在一种严苛前提下具有数学合法性：相关系数必须是某个连续变量与一个经过人工二分（且二分比例严格为 50/50）的潜在连续变量之间的**双列相关（Biserial Correlation）**；若直接将两个自然连续变量之间的常规 Pearson 积差相关代入该公式，属于违背数学假定的形式滥用（[[Argument_Bergeron_2017_MJE|Bergeron & Rivard, 2017, p. 242]]）。
>
> **换算对照表**
> | 皮尔逊相关系数 $r$ | 决定系数 $R^2$（方差解释度） | 对应标准化均值差 Cohen's $d$ | 统计学定性与特征 |
> |---|---|---|---|
> | 0.100 | 1.00% | 0.201 | 微弱相关，对应小型均值差异 |
> | **0.196** | **3.85%** | **0.400** | 弱相关被机械放大至哈蒂[[Zone of Desired Effects\|期望效应区]]临界线 |
> | 0.300 | 9.00% | 0.629 | 中低度相关，换算为中等偏上[[Effect Size\|效应量]] |
> | 0.500 | 25.00% | 1.155 | 中等相关，换算突破 $d > 1.0$ 巨大效应 |
> | 0.800 | 64.00% | 2.667 | 强相关，换算产生超常效应量估计 |
> | 0.900 | 81.00% | 4.129 | 极强相关，效应量呈现指数型膨胀 |
> | **1.000** | 100.00% | **$+\infty$（无穷大）** | 极值数学崩溃：对照组零方差自相关输出无穷大值 |

---

> [!contrast-table] 关联与均值度量方法多维辨析
> | 维度 | [[Pearson Product-Moment Correlation\|Pearson 积差相关]] | Spearman 等级相关 | [[Multiple Regression\|多元线性回归]] | [[Effect Size\|Cohen's d]] |
> |---|---|---|---|---|
> | **[[Variable\|变量]]尺度** | 两个连续变量（等距／等比） | 顺序变量或非正态连续变量 | 多个连续[[Independent Variable\|预测变量]]与一个连续[[Dependent Variable\|结果变量]] | 分类自变量（两组）与连续因变量 |
> | **关系形态** | 严格线性关联 | 单调递增或单调递减关联 | 线性组合与加权超平面拟合 | 组间分布平移差值 |
> | **参数假定** | 双变量正态分布假设 | 非参数秩次检验，无正态假定 | 残差正态性、同方差与独立性 | 各组正态分布与方差齐性 |
> | **核心统计量** | 相关系数 $r \in [-1, +1]$ | 秩相关系数 $\rho \in [-1, +1]$ | 偏回归系数 $b$ 与模型拟合优度 $R^2$ | 标准化均值差 $d \in (-\infty, +\infty)$ |
> | **核心功能** | 评估两变量双向共变强度 | 评估基于排名的单调协同方向 | 评估控制协变量后的独立预测贡献 | 评估实验干预带来的因果或组间效应量 |

---

> [!critique-method] 跨设计换算发散与方差解释度微弱风险
> 皮埃尔-热罗姆·伯杰龙（[[Pierre-Jérôme Bergeron]]）与利桑·里瓦尔（Lysanne Rivard）针对《[[Visible Learning|可见的学习]]》展开的数理审查表明，将 Pearson 相关系数无约束地转换为 Cohen's $d$ 带来了严重的数理失真与算法崩溃现象（[[Argument_Bergeron_2017_MJE|Bergeron & Rivard, 2017, pp. 242–245]]）：
> - **弱相关机械放大至[[Zone of Desired Effects|期望效应区]]** 公式在弱相关区间呈现陡峭斜率，仅需 $r = 0.196$ 的微弱关联即可换算出 $d = 0.40$ 的期望效应门槛。然而其对应的一[[Meta-regression|元回归]]决定系数仅为 $R^2 = 3.85\%$，表明存在高达 96.15% 的无法解释随机噪声。以此为基准指导教育政策决策，存在将微弱噪声定性为重大干预成效的风险。
> - **零变异对照组极限发散** 在受控随机模拟实验中，保持成绩完全未变的对照组由于各学生增量均为 0，前后成绩自相关达到 $r = 1.0$。若套用相关换算公式，该对照组将产出 $d = +\infty$ 的理论极大值，由此产生未施加任何教学干预的对照组在排行榜上超越全部实验教学法的数学反常。
> - **双列相关前置条件的系统性违背**Borenstein et al. (2009) 明确指出该换算仅适用于二分[[Variable|变量]]与连续变量的双列相关模型；若在实际文献合成中无视二分切割条件与连续正态假定，直接对常规 Pearson $r$ 进行代入，属于数理推导层面的操作越界。

> [!critique-method] 相关关系伪装因果干预的[[Category Mistake|范畴错误]]
> 将横截面[[Correlational Research|相关性研究]]数据借助公式换算包装为实验干预[[Effect Size|效应量]]，构成了严重的范畴错误（[[Category Mistake|范畴错误]]）与因果混淆（[[Argument_Bergeron_2017_MJE|Bergeron & Rivard, 2017, p. 242]]）：
> - **[[Creativity|创造力]]实证错位** 在[[Meta-meta-analysis|二阶元分析]]中，金（Kim, 2005）的[[Meta-analysis|元分析]]被包装为[[Creativity|创造力]]对[[Academic Achievement|学业成就]]的强大因果干预；然而原始研究所汇集的证据实质上仅是智商测验（IQ）与创造力量表得分之间的横向静态相关，从未测量[[Creativity Training|创造力培养]]或教学训练带来的实验增量。
> - **自我报告成绩榜首失范** 在教育排行榜中常年位列榜首的学生自我报告成绩（Self-reported grades），其原始数据仅为学生自我预估成绩与真实期末成绩之间的双变量自相关；该数据反映的是学生对自己能力的评估准确性，缺乏实施自我预估组与未实施预估组之间的因果对照，将其换算为干预效应量并列入排行榜首位，构成了将预测一致性偷换为教学效能的逻辑谬误。

---

> [!software-impl] 软件实现
> - **推荐环境** R 语言与 Python 统计计算库。
> - **R 语言规程**
>   ```R
>   # 双变量皮尔逊相关检验
>   cor_result <- cor.test(data$var1, data$var2, method = "pearson", conf.level = 0.95)
>   r_val <- cor_result$estimate
>   p_val <- cor_result$p.value
>   ci_val <- cor_result$conf.int
>   
>   # 决定系数计算
>   r_squared <- r_val^2
>   
>   # Borenstein 换算函数（需确保符合双列相关前提）
>   r_to_d <- function(r) {
>     if (abs(r) >= 1) stop("r 必须严格落于 (-1, 1) 开区间")
>     2 * r / sqrt(1 - r^2)
>   }
>   ```
> - **Python 规程**
>   ```python
>   from scipy import stats
>   import numpy as np
>
>   # 计算 Pearson 相关系数与双尾检验 p 值
>   r, p_value = stats.pearsonr(x, y)
>   r_sq = r ** 2
>
>   # 换算为 Cohen's d 并做数值截断检验
>   def convert_r_to_d(r_val):
>       if abs(r_val) >= 1.0:
>           raise ValueError("相关系数必须在 (-1, 1) 范围内以避免除零发散")
>       return (2 * r_val) / np.sqrt(1 - r_val**2)
>   ```
> - **规范报告标准** 报告时斜体呈现 $r$，同时汇报自由度 $df = N - 2$、精确 $p$ 值、95% [[Confidence Interval|置信区间]]以及决定系数 $R^2$；明确强调数据的双[[Variable|变量]]正态性检验结果与非[[Causality|因果性]]属性。

---

> [!method-fit] 适用判断
> - **适合使用** 适用于检验两个连续[[Variable|变量]]之间是否存在线性关联结构；适用于在[[Survey Research|调查研究]]与横截面设计中评估变量共变方向与紧密度；适用于构建多元统计分析前的初始相关系数矩阵（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）。
> - **谨慎使用** 当数据存在轻度偏态、含有潜在亚组[[Heterogeneity|异质性]]分布或处于跨研究[[Meta-analysis|元分析]]聚合场景时，必须执行变量分布转换（如 Fisher's $z$ 变换）并审慎检验[[Sample Size Determination|样本量]]加权机制（[[Argument_Runco_2026_CRJ|Runco et al., 2026, p. 5]]）。
> - **不适合使用** 不适合用于度量具有明显曲线（非线性）形态的变量关系；不适合用于顺序尺度或分类离散变量；严禁将双变量相关系数直接当作因果干预[[Effect Size|效应量]]，严禁在脱离双列相关假定前提下直接套用公式换算为 Cohen's $d$（[[Argument_Bergeron_2017_MJE|Bergeron & Rivard, 2017, pp. 242–245]]）。

> [!method-limits] 方法局限
> - **线性度量限制** 仅能捕捉严格的线性共变；两变量若存在强烈的非线性结构（如倒 U 型关系），其计算得出的 $r$ 可能趋近于 0，掩盖真实的关联模式。
> - **离群异常值敏感性** 协方差分子对极端数据点高度敏感；少数偏离主群体的极端离群值能够显著人为拔高或压低相关系数。
> - **第三变量与伪相关风险** 相关关系反映统计协同变化，无法排除混淆变量（第三变量 $Z$）带来的间接关联效应，存在将虚假共变误读为实质关联的风险（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）。
> - **跨设计换算爆炸风险** 将常规 Pearson $r$ 代入均值差换算公式时，在强相关下会出现极限发散，在弱相关下存在方差解释力过低却被放大为期望效应的风险（[[Argument_Bergeron_2017_MJE|Bergeron & Rivard, 2017, p. 242]]）。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Correlational Research\|相关性研究]] | 上位方法 | 提供双[[Variable\|变量]]相关分析所属的非干预实证研究设计框架。 |
> | [[Multiple Regression\|多元回归]] | 扩展方法 | 将双变量分析扩展至多[[Independent Variable\|预测变量]]系统并评估相对贡献。 |
> | [[Effect Size Conversion\|效应量转换]] | 转化方法 | 规定相关系数与其他[[Effect Size\|效应量]]指标之间跨尺度转换的数学条件。 |
> | [[Effect Size\|效应量]] | 统计概念 | 将 Pearson $r$ 纳入无量纲标准化效应量家族进行统一考察。 |
> | [[Category Mistake\|范畴错误]] | 批判概念 | 指涉将非实验静态相关硬性包装为因果干预效应量的逻辑谬误。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Creswell_2022_SAGE|Creswell and Creswell (2022)]] — 规范了量化设计中依据[[Variable|变量]]数目与分布形态选择 Pearson 相关的决策矩阵。
> - [[Argument_Bergeron_2017_MJE|Bergeron and Rivard (2017)]] — 揭示了将皮尔逊相关换算为均值差时的极值发散风险与方差解释度虚增问题。
> - [[Argument_Runco_2026_CRJ|Runco et al. (2026)]] — 在[[Creativity|创造力]][[Meta-analysis|元分析]]中将各实证研究的一阶效应指标统一转换为皮尔逊 $r$ 并执行 Fisher's $z$ 变换。
