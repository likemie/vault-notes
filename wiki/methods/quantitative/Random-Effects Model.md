---
title: Random-Effects Model
aliases:
  - 随机效应模型
  - 随机效应
  - Random-Effects Models
  - Random Effects Model
  - Random Effect Model
  - Random Effects
summary: "假定真实效应量服从正态分布并同时分解抽样方差与研究间异质性方差（τ²）的统计合成模型，实现权重再平衡与面向超总体的广义推断"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 59
method_related_level: 5
method_related_stars: "💎⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - statistics/meta-analysis
  - statistical-model
  - random-effects-model
  - methodology
related_concepts:
  - "[[Heterogeneity]]"
  - "[[Paradigm]]"
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Publication Bias]]"
  - "[[Internal and External Generalizability]]"
  - "[[Document]]"
  - "[[Visible Learning]]"
  - "[[Extracurricular Activities]]"
  - "[[Sampling Error]]"
  - "[[Category Mistake]]"
  - "[[Commensuration]]"
  - "[[Worked Examples]]"
  - "[[Direct Instruction]]"
  - "[[Charter Schools]]"
  - "[[Learning Styles]]"
  - "[[Class Size]]"
  - "[[Construct]]"
  - "[[Critical Thinking]]"
  - "[[Generative Artificial Intelligence]]"
  - "[[Graphic Organizer]]"
  - "[[Higher-Order Thinking Skills]]"
  - "[[Variable]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Fixed-Effect Model]]"
  - "[[Effect Size]]"
  - "[[Between-Study Variance]]"
  - "[[Inverse-Variance Weighting]]"
  - "[[Prediction Interval]]"
  - "[[Meta-regression]]"
  - "[[Confidence Interval]]"
  - "[[Forest Plot]]"
  - "[[Sample Size Determination]]"
  - "[[Meta-meta-analysis]]"
  - "[[Random Sampling]]"
  - "[[Funnel Plot]]"
  - "[[Trim and Fill Method]]"
  - "[[Role-playing]]"
  - "[[Begg and Mazumdar Rank Correlation]]"
  - "[[Small Study Effects]]"
  - "[[Cochran's Q Test]]"
  - "[[I-squared Statistic]]"
  - "[[Three-Level Meta-Analysis]]"
  - "[[Robust Variance Estimation]]"
  - "[[Standard Error]]"
  - "[[Intervention Research]]"
related_instruments: []
related_persons:
  - "[[Gene Glass]]"
  - "[[John Hattie]]"
  - "[[Christof Wecker]]"
  - "[[Ivan Snook]]"
related_facts: []
related_arguments:
  - "[[Argument_Higgins_2016_ROE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17]]"
  - "[[Argument_Wecker_2016_ZfE]]"
  - "[[Argument_Snook_2009_NZJES]]"
  - "[[Argument_Hattie_2010_NZJES]]"
  - "[[Argument_Abrami_2015_RER]]"
  - "[[Argument_Chen_Cheung_2025_ERR]]"
  - "[[Argument_Lei_Ding_Chiu_2026_ERR]]"
  - "[[Argument_Zhao_2025_JIntell]]"
confidence: high
status: completed
created: 2026-06-08
updated: 2026-10-30
---

---

> [!def] Random-Effects Model
> 随机效应模型（Random-Effects Model）是[[Meta-analysis|元分析]]中应对初级研究间实质性[[Heterogeneity|异质性]]的标准统计建模[[Paradigm|范式]]。与[[Fixed-Effect Model|固定效应模型]]假定单一恒定真值不同，随机效应模型假定各纳入研究的真实[[Effect Size|效应量]]本身并不相同，而是服从一个具有均值 $\mu$ 与方差 $\tau^2$ 的广义真实效应正态分布。模型将观测变异显式分解为两个独立层次：**“研究内抽样方差”（Within-study variance, $v_i$）** 与 **“[[Between-Study Variance|研究间真实方差]]”（Between-study variance, $\tau^2$）**。通过将 $\tau^2$ 纳入[[Inverse-Variance Weighting|逆方差加权]]分母（$w_i^* = \frac{1}{v_i + \tau^2}$），模型实现了权重再平衡，并将统计推论拓展至包含未来研究的广义“超总体”（Super-population）。[[Argument_Higgins_2016_ROE|(Higgins, 2016, p. 39)]]; [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|(Cohen et al., 2011, Ch. 17)]]

> [!method-scope] 方法范围
> - **研究对象** 在教学情境、样本群体、干预时长及测量工具上存在合理变异的多中心或多研究实证效应量集合。
> - **核心目标** ① 估计广义超总体的真实效应均值 $\mu$；② 准确估计研究间真实方差 $\tau^2$ 与异质性比率 $I^2$；③ 构建 95% [[Prediction Interval|预测区间]]（PI）以评估干预在未来单项新情境中的潜在效应范围；④ 借助[[Meta-regression|元回归]]解释异质性来源。
> - **[[Unit of Analysis|分析单位]]** 纳入元分析的独立实验样本或初级研究提取的效应量点估计值。
> - **输出形式** 随机效应合并平均效应量（$\hat{\mu}_{\text{RE}}$）、95% [[Confidence Interval|置信区间]]（95% CI）、研究间方差（$\hat{\tau}^2$）、95% 预测区间（95% PI）及[[Forest Plot|森林图]]菱形。

> [!citation-card] 随机效应模型的超总体推论
> 随机效应模型假定真实效应量本身存在分布，观察到的研究间差异反映了真实的异质性；其统计推断面向更广泛的可能研究超总体，而不仅限于当前样本。[[Argument_Higgins_2016_ROE|(Higgins, 2016, p. 39)]]
>
> *The random-effects model allows true effect sizes to vary across studies... generalizing to a hypothetical super-population of studies rather than just the observed sample.*

> [!citation-card] 二级随机效应建模的[[Sample Size Determination|样本量]]瓶颈
> 在[[Meta-meta-analysis|二级元分析]]中，每个影响因素平均仅收录约 5.8 项一阶元分析；在如此微小的样本量下，研究间方差 $\tau^2$ 根本无法可靠估计，导致随机效应模型在宏观二阶综合中陷入实际瘫痪。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 32–33)]]
>
> *Bei durchschnittlich nur knapp sechs Metaanalysen pro Einflussfaktor lässt sich die Varianz zwischen den Metaanalysen nicht verlässlich schätzen, sodass Random-Effects-Modelle auf der zweiten Stufe scheitern.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 承认人类社会与教育干预生态的复杂性与情境依赖性，将知识视作具有概率分布特征的广义因果空间，坚决摒弃“单一绝对真值”的机械教条。
> - **研究者角色** 要求研究者不仅报告平均[[Effect Size|效应量]]，更必须全面呈现变异分布（[[Gene Glass]] 准则）；在解释政策效果时必须结合 95% [[Prediction Interval|预测区间]]评估干预失败或负效应风险。
> - **有效性标准** 依赖于足够的研究数量（建议 $k \ge 10$）以确保限制性最大似然法（REML）或 DerSimonian-Laird（DL）矩估计稳定收敛；严格防范因提升小研究权重而加剧[[Publication Bias|发表偏倚]]。
> - **不声称回答的问题** 合并均值 $\hat{\mu}$ 无法代替针对特定课堂或地方学校的具体教学决策；即便总体均值显著正向，预测区间跨越 0 仍表明干预在特定条件下可能无效甚至有害。

> [!contrast-table] 随机效应模型 vs [[Fixed-Effect Model|固定效应模型]]核心参数与决策对比
> | 比较维度 | 随机效应模型（Random-Effects Model） | 固定效应模型（[[Fixed-Effect Model]]） |
> |:---|:---|:---|
> | **核心哲学假设** | 存在一个“真实效应量分布”（Distribution of True Effects） | 存在唯一的“单一真实效应”（One True Effect） |
> | **方差来源分解** | 抽样方差 $v_i$ + [[Between-Study Variance\|研究间方差]] $\tau^2$ | 仅抽样方差（Within-study variance, $v_i$） |
> | **权重分配机制** | 权重趋于均衡（$w_i^* = \frac{1}{v_i + \tau^2}$），大样本绝对优势被 $\tau^2$ 稀释 | 极度偏向超大样本研究（$w_i = 1/v_i \propto N_i$） |
> | **[[Confidence Interval\|置信区间]]宽度** | 较宽（充分纳入了跨情境[[Heterogeneity\|异质性]]带来的推断不确定性） | 较窄（仅反映研究内抽样方差，容易产生假性精确） |
> | **95% 预测区间** | 可计算 95% [[Prediction Interval\|预测区间]]，量化未来单项试验的真实风险 | 无法计算预测区间（模型预设研究间方差为 0） |
> | **小研究偏倚敏感性** | **高度敏感** 相对抬高了小样本研究的权重，易受小样本发表偏倚扭曲 | 相对不敏感：小样本劣质研究权重被方差严重压缩 |
> | **统计推断外推** | 面向未知的广义超总体（Super-population），具[[Internal and External Generalizability\|外部推广性]] | 严格局限于纳入的特定研究集合，不得向外盲目外推 |

---

> [!formula-set]- 随机效应两层变异分解与参数估计流程
> ```mermaid
> flowchart LR
>   A["步骤 1：两层变异模型分解<br/>区分研究内抽样误差与研究间异质性"] --> B["步骤 2：估计研究间真实方差 Tau²<br/>DerSimonian-Laird 矩估计或 REML 最大似然法"]
>   B --> C["步骤 3：权重再平衡计算<br/>将真实异质性方差纳入加权分母衰减极端权重"]
>   C --> D["步骤 4：计算合并均值与方差<br/>获得广义超总体真实效应平均值与综合方差"]
>   D --> E["步骤 5：构建双重推断区间<br/>95% 置信区间反映平均效应精度，预测区间反映未来分散度"]
> ```

---

### 公式步骤一　双层方差分解统计模型

> [!formula-step] 公式步骤　双层随机效应模型结构
> $$y_i = \theta_i + \epsilon_i = \mu + u_i + \epsilon_i$$
> $$u_i \sim N(0, \tau^2), \quad \epsilon_i \sim N(0, v_i)$$
>
> **这个公式在做什么** 表达第 $i$ 项研究观测到的[[Effect Size|效应量]] $y_i$ 包含三重成分：超总体的真实效应均值 $\mu$、该特定研究真实效应偏离均值的离散量 $u_i$（[[Heterogeneity|研究间异质性]]，方差为 $\tau^2$），以及该研究受试者的[[Random Sampling|随机抽样]]误差 $\epsilon_i$（研究内方差，方差为 $v_i$）。[[Argument_Higgins_2016_ROE|(Higgins, 2016, p. 39)]]
>
> **总方差分解**
> $$\operatorname{Var}(y_i) = v_i + \tau^2$$

---

### 公式步骤二　研究间方差估计与调整权重合成

> [!formula-step] 公式步骤　DerSimonian-Laird 矩估计与随机效应加权
> 经典 DerSimonian and Laird (1986) 矩估计算法通过 Cochran's $Q$ 统计量与自由度之差估计 $\tau^2$：
> $$\hat{\tau}^2 = \max\left(0, \frac{Q - (k-1)}{\sum w_i - \frac{\sum w_i^2}{\sum w_i}}\right), \quad \text{其中 } w_i = \frac{1}{v_i}$$
>
> 代入修正后的逆方差权重：
> $$w_i^* = \frac{1}{v_i + \hat{\tau}^2}$$
> $$\hat{\mu}_{\text{RE}} = \frac{\sum_{i=1}^k w_i^* y_i}{\sum_{i=1}^k w_i^*}, \quad \text{Var}(\hat{\mu}_{\text{RE}}) = \frac{1}{\sum_{i=1}^k w_i^*}, \quad \text{SE}(\hat{\mu}_{\text{RE}}) = \sqrt{\frac{1}{\sum_{i=1}^k w_i^*}}$$
>
> **数学直觉** 引入 $\hat{\tau}^2$ 后，分母加项使各研究权重之间的极差缩小。超大样本研究的权重不再无限膨胀，中小样本研究的贡献被适度提升。

---

### 公式步骤三　95% 预测区间（Prediction Interval, PI）推导

> [!formula-step] 公式步骤　95% [[Prediction Interval|预测区间]]计算公式
> $$\text{PI}_{95\%} = \hat{\mu}_{\text{RE}} \pm t_{k-2, 0.975} \sqrt{\text{Var}(\hat{\mu}_{\text{RE}}) + \hat{\tau}^2}$$
>
> **这个公式在做什么** 接收合并均值 $\hat{\mu}_{\text{RE}}$、估计误差 $\text{Var}(\hat{\mu}_{\text{RE}})$ 以及[[Between-Study Variance|研究间真实方差]] $\hat{\tau}^2$，结合自由度为 $k-2$ 的 $t$ 分布临界值，估计在**未来某一个单项具体新情境研究**中可能观察到的真实效应量范围。[[Argument_Higgins_2016_ROE|(Higgins, 2016, p. 40)]]
>
> **结果研判准则**
> - **[[Confidence Interval|置信区间]]（CI）** 反映的是“超总体均值估计有多精确”；
> - **预测区间（PI）** 反映的是“单项新课堂面临的真实效应波动有多宽”；
> - 即使 95% CI 全部显著大于 0，若 95% PI 的下限跌入负值区间（跨越 0），决策者必须清醒认识到：该干预在某些特定学校或情境下极有可能无效甚至产生负面损害。

> [!math-principle] 随机效应模型的数理机制与小研究放大警示
> - **权重再平衡机制（Weight Leveling Effect）** 当跨研究异质性极大（$\tau^2 \gg v_i$）时，$w_i^* = \frac{1}{v_i + \tau^2} \to \frac{1}{\tau^2}$。此时所有研究不论[[Sample Size Determination|样本量]]大小，其权重几乎完全相等，[[Fixed-Effect Model|固定效应模型]]下的大样本垄断被打破。
> - **小研究[[Publication Bias|发表偏倚]]放大警示** 若[[Document|文献]]库中存在显著的[[Publication Bias|发表偏倚]]（小样本研究往往因显著的正向极端效应才得以发表），权重再平衡会大幅提升这些劣质小研究在总分中的比重，导致随机效应合并均值 $\hat{\mu}_{\text{RE}}$ 反而显著高于固定效应估计值 $\hat{\theta}_{\text{FE}}$。例如[[John Hattie|约翰·哈蒂]]（John Hattie）在《[[Visible Learning|可见的学习]]》讨论[[Extracurricular Activities|课外活动]]时，曾明确提醒读者慎重对待 $d = 0.47$ 的结论，因其基于随机效应模型计算，极易赋予小样本研究过多权重而虚增效应量（Hattie, 2009; 引自 [[Argument_Snook_2009_NZJES|Snook et al., 2009, p. 95]]）。因此报告随机效应模型必须强制配合[[Funnel Plot|漏斗图]]、Egger 检验与[[Trim and Fill Method|剪补法]]。
> - **小样本 $k$ 估计瘫痪** 当纳入的研究数量过少（$k < 5$）时，$\tau^2$ 的[[Sampling Error|抽样分布]]极度偏斜，点估计极易落入 0 或产生极大方差，导致置信区间产生严重误导。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 32–33)]]

---

## 认识论危机与双重不可行性困境（Wecker et al., 2016）

在教育科学与[[Meta-meta-analysis|二阶元分析]]的宏观实践中，[[Christof Wecker|克里斯托夫·韦克尔]]（Christof Wecker）等人深入剖析了随机效应模型在面对现实数据时遭遇的“双重不可行性困境”：

> [!contrast-table] 一级与二级统计建模的双重不可行性困境（Double Infeasibility Dilemma）
> | 分析层级 | 经验与理论现实 | 统计建模困境 | 导致后果与推论崩溃 |
> |:---|:---|:---|:---|
> | **一级主要研究层** | 教学主题、教师个人风格与学校社会文化情境高度异质，真实[[Effect Size\|效应量]]变异极大。 | [[Fixed-Effect Model\|固定效应模型]]关于单一恒定真实效应的公理假定完全破产。 | 必须采用随机效应模型；若强用固定模型，标准误严重低估，假阳性膨胀。[[Argument_Wecker_2016_ZfE\|(Wecker et al., 2016, pp. 31–32)]] |
> | **二级[[Meta-analysis\|元分析]]层** | 继承了一级异质性，数学上必须在二级层面采用随机效应模型估计 $\tau^2$。 | 每个影响因素平均仅收录约 5.8 项元分析（$800/138$），样本量过小导致参数估计无法收敛。 | 样本量过小使 $\tau^2$ 估计崩溃，宏观二级统计推断失去立足之基。[[Argument_Wecker_2016_ZfE\|(Wecker et al., 2016, pp. 32–33)]] |

> [!critique-logic] 单一均值抹平教学情境与德甲联赛[[Category Mistake|范畴错误]]
> - **情境[[Heterogeneity|异质性]]抹平危机** 以 Fisher (1992, p. 175) 游戏元分析为例，社会[[Role-playing|角色扮演]]游戏效应高达 $d = 1.48$，纯想象主题游戏仅为 $d = 0.28$。随机效应模型虽然在数学上容纳了方差，但其最终输出的单一均值 $0.74$ 仍将具体实践机制抹平，使一线教师无法判断哪种具体形式有效。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 30–31)]]
> - **跨本体范畴的强行比较** 德甲联赛隐喻表明，教育因素跨越了制度框架条件、个体心理特征、综合教学方案与微观设计变体四大基线不可[[Commensuration|通约]]的本体范畴。随机效应模型可以平衡统计权重，但无法消除将微观 1.5 小时实验（如[[Worked Examples|样例学习]]）与宏观全年改革（[[Direct Instruction|直接教学]]）放在同一排行榜上的范畴错误。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 33–34)]]

> [!critique-logic] 随机效应模型效应虚增警示与元分析质量审查的随意性
> 约翰·[[Ivan Snook|斯努克]]（Ivan Snook）等学者从方法论一致性视角，指出了宏观二阶综合在运用随机效应模型时暴露出的标准双标问题：
> - **模型的选择性警示** [[John Hattie|哈蒂]]在《[[Visible Learning|可见的学习]]》前言中公开声明不对原始研究开展质量批评；然而在具体章节中，他在[[Extracurricular Activities|课外活动]]（报告 $d = 0.47$）中明确警示随机效应模型容易人为抬高小研究权重并虚增效应量，在[[Charter Schools|特许学校]]研究中指出剔除低质量研究后效应量从 $0.2$ 归零（p. 66），在[[Learning Styles|学习风格]]（$d = 0.41$）中以研究动机可疑为由断然拒绝采信结论（pp. 195–197）。
> - **方法论一致性的瓦解** 斯努克等（[[Argument_Snook_2009_NZJES|Snook et al., 2009, p. 95]]）指出，哈蒂对随机效应模型放大效应量的敏感性本身表明，单纯依赖效应量数值而不审查底层研究质量在[[Epistemology|认识论]]上无法自洽；但在大多数其他领域（如[[Class Size|班级规模]]、家庭背景、教师效能），他又放弃了对随机效应模型敏感度与研究质量的审查。哈蒂（[[Argument_Hattie_2010_NZJES|Hattie, 2010, p. 88]]）辩护称，凡已知质量或模型属性对结果产生实质影响之处均已作标注，但批评者认为这种非系统性的局部警示破坏了二阶综合的客观性准绳。

---

> [!proc] 随机效应模型五步标准操作规程
> 1. **[[Effect Size|效应量]]提取与[[Construct|构念]]核查** 提取各独立样本标准化效应量（优先选用 Hedges' $g$）并计算其抽样方差 $v_i$；严格审查对照组属性（活跃对照 vs 常规对照），确保干预定义具备可比性。
> 2. **前置[[Heterogeneity|异质性]]量化检验** 计算 Cochran's $Q$ 统计量与 $I^2$ 指数；只要存在潜在真实变异或 $I^2 > 25\%$，默认采用随机效应模型。
> 3. **稳健参数估计与模型拟合** 优先采用限制性最大似然法（REML）替代传统 DL 矩估计法，计算[[Between-Study Variance|研究间方差]] $\hat{\tau}^2$；由 $w_i^* = 1/(v_i + \hat{\tau}^2)$ 计算合并平均效应量与 95% [[Confidence Interval|置信区间]]。
> 4. **计算 95% [[Prediction Interval|预测区间]]（PI）** 结合 $t$ 分布与总方差估计，显式计算并汇报 95% 预测区间，评估真实效应跨越 0 甚至呈现负效应的风险边界。
> 5. **[[Publication Bias|发表偏倚]]诊断与敏感性检验** 绘制[[Funnel Plot|漏斗图]]，配合 Egger 线性回归与 Begg [[Begg and Mazumdar Rank Correlation|秩相关检验]][[Small Study Effects|小研究效应]]；运用[[Trim and Fill Method|剪补法]]（Trim and Fill）检验在填补潜在未发表研究后合并效应量与置信区间的稳定性。

---

> [!software-impl] R 语言随机效应模型完整工作流
> ```R
> library(metafor)
> 
> # 1. 效应量与抽样方差计算 (标准化均值差 Hedges' g)
> dat <- escalc(measure = "SMD", 
>               m1i = m_exp, sd1i = sd_exp, n1i = n_exp,
>               m2i = m_ctl, sd2i = sd_ctl, n2i = n_ctl, 
>               data = raw_data)
> 
> # 2. 拟合随机效应模型 (推荐 REML 限制性最大似然估计)
> fit_re <- rma(yi, vi, data = dat, method = "REML")
> summary(fit_re)
> 
> # 3. 计算 95% 预测区间 (Prediction Interval)
> predict(fit_re)
> 
> # 4. 证据可视化：绘制森林图与漏斗图
> forest(fit_re, slab = paste(author, year), xlab = "Hedges' g")
> funnel(fit_re, xlab = "Hedges' g")
> 
> # 5. 发表偏倚诊断：Egger 回归与剪补法
> regtest(fit_re, model = "rma")
> trimfill(fit_re)
> ```

---

> [!entry-map] 相关理论与方法
> | 条目 | 类型 | 关系说明 |
> |:---|:---|:---|
> | [[Fixed-Effect Model]] | 基础[[Paradigm\|范式]] | 固定效应模型假定单一恒定真实效应，是随机效应模型的前置对比基准。 |
> | [[Between-Study Variance]] | 核心参数 | 研究间方差（$\tau^2$）量化跨研究真实异质性，是调整逆方差权重的关键加项。 |
> | [[Prediction Interval]] | 推断指标 | 随机效应模型独有的外推指标，量化未来单项新情境可能面临的效应范围。 |
> | [[Cochran's Q Test]] | 诊断检验 | 检验真实[[Effect Size\|效应量]]是否完全同质，为启动随机效应模型提供统计依据。 |
> | [[I-squared Statistic]] | 诊断指标 | 量化总变异中由真实[[Heterogeneity\|异质性]]解释的比例，反映随机效应建模的必要性程度。 |
> | [[Three-Level Meta-Analysis]] | 高阶扩展 | 当研究内报告多个相关效应量时，将随机效应扩展为三水平层级模型。 |
> | [[Meta-regression]] | 分析方法 | 在随机效应框架下纳入协变量以系统解释 $\tau^2$ 的实质来源。 |
> | [[Robust Variance Estimation]] | 补救方法 | 在文献重叠与复杂相关依赖下提供渐近无偏的稳健[[Standard Error\|标准误]]推断。 |
> | [[Argument_Higgins_2016_ROE\|Higgins (2016)]] | 论证 | 系统阐述随机效应模型在面向广义超总体推论中的方法论优越性与历史演进。 |
> | [[Argument_Wecker_2016_ZfE\|Wecker et al. (2016)]] | 论证 | 揭示二级随机效应模型因[[Meta-analysis\|元分析]]数量过少（平均约 5.8 项）导致的双重不可行性困境。 |
> | [[Argument_Snook_2009_NZJES\|Snook et al. (2009)]] | 方法批评 | 揭示二阶综合中对随机效应模型虚增效应量警示的选择性援引，批判研究质量审查的随意性。 |
> | [[Argument_Hattie_2010_NZJES\|Hattie (2010)]] | 方法辩护 | 回应 Snook et al. 批评，辩护元分析模型属性与质量控制的局部标注策略。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Higgins_2016_ROE|Higgins (2016)]] — 系统阐述随机效应模型的超总体推论哲学，指出其通过纳入[[Between-Study Variance|研究间方差]]真实反映了证据[[Heterogeneity|异质性]]。
> - [[Argument_Wecker_2016_ZfE|Wecker et al. (2016)]] — 论证一级研究因教育复杂性必须采用随机效应模型，但揭示二级综合因一阶[[Document|文献]][[Sample Size Determination|样本量]]过小导致随机效应建模陷入双重不可行性困境。
> - [[Argument_Abrami_2015_RER|Abrami et al. (2015)]] — 在 341 项[[Critical Thinking|批判性思维]]教学研究中采用随机效应模型与混合效应[[Meta-regression|元回归]]，稳健合成干预效应（$g+ = 0.57$）。
> - [[Argument_Chen_Cheung_2025_ERR|Chen and Cheung (2025)]] — 运用随机效应模型综合 57 项[[Generative Artificial Intelligence|生成式人工智能]]教育[[Intervention Research|干预研究]]，结合[[Trim and Fill Method|剪补法]]严格诊断小研究[[Publication Bias|发表偏倚]]。
> - [[Argument_Lei_Ding_Chiu_2026_ERR|Lei et al. (2026)]] — 运用随机效应模型综合 66 项[[Graphic Organizer|图形组织器]]研究，以 Wald 检验与元回归系统解释异质性变异来源。
> - [[Argument_Zhao_2025_JIntell|Zhao et al. (2025)]] — 运用随机效应模型综合 29 项生成式 AI 对[[Higher-Order Thinking Skills|高阶思维]]影响的实证研究，检验多维情境调节[[Variable|变量]]。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen, Manion & Morrison (2011, Ch. 17)]] — 系统介绍随机效应模型加权机制、$\tau^2$ 估计方法与[[Prediction Interval|预测区间]]解读规程。
> - [[Argument_Snook_2009_NZJES|Snook et al. (2009, p. 95)]] — 援引 Hattie 在课外活动中对随机效应模型导致[[Effect Size|效应量]]虚增的论述，批判宏观二阶综合在模型选择与研究质量审查上的随意性与双重标准。
> - [[Argument_Hattie_2010_NZJES|Hattie (2010, p. 88)]] — 回应 Snook et al. 批评，辩护[[Meta-analysis|元分析]]处理异质性与质量控制的方法论权能，澄清对模型属性与调节变量的报告策略。
