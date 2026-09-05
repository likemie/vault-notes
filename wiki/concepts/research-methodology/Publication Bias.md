---
title: Publication Bias
aliases:
  - 发表偏差
  - 发表偏倚
summary: "正面或显著结果比零结果或负面结果更可能被发表或传播的系统性倾向，用于解释证据库为何可能高估干预效果。"
type: concept
domain: "research-methodology"
related_count: 22
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
tags:
- publication-bias
- file-drawer-effect
- meta-analysis
- research-methodology
- evidence-based-education
related_concepts:
  - "[[Document]]"
  - "[[Effect Size]]"
  - "[[Critique of Meta-analysis]]"
  - "[[Developer Effect]]"
  - "[[Hypothesis]]"
  - "[[Evaluator Independence]]"
  - "[[Categorical Funding]]"
  - "[[Researcher Degrees of Freedom]]"
  - "[[Visible Learning]]"
  - "[[Preregistration]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Systematic Review]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Quantitative Research]]"
related_persons: []
related_facts:
  - "[[What Works Clearinghouse]]"
  - "[[Creation of REES]]"
  - "[[ESSA 2015 Evidence Standards]]"
related_arguments:
  - "[[Argument_Wolf_2020_JREE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17]]"
  - "[[Argument_Higgins_2016_RE]]"
  - "[[Argument_Kraft_2023_ER]]"
  - "[[Argument_Wecker_2016_ZfE]]"
  - "[[Argument_Zhao_2025_JIntell]]"
confidence: medium
status: draft
created: '2026-05-02'
updated: 2026-07-15
---

## 定义

> [!def] 核心定义
> 发表偏倚（Publication Bias），也称文件抽屉效应（File Drawer Effect），指具有统计显著或正面结果的研究比零结果或负面结果的研究更有可能被发表或传播的系统性倾向。在教育项目评估中，发表偏倚意味着已发表[[Document|文献]]中的平均[[Effect Size|效应量]]可能高估干预的真实有效性。

> [!concept-lens] 概念透镜
> - **含义** 学术发表系统对显著和正面结果的偏好，使得证据库系统性偏离真实效应分布。
> - **用途** 帮助[[Meta-analysis|元分析]]研究者识别和校正证据库的不完整性，为政策制定者提供"证据本身可能已被筛选过"的警觉。
> - **边界** 发表偏倚不等于有意造假——它可以是期刊偏好、研究者自选或资助方经济激励的结果。详见 [[Critique of Meta-analysis]]。

> [!boundary] 概念边界
> - **不等于选择性报告** 发表偏倚指整篇研究不被发表（study-level）；选择性报告指同一研究内某些结果被报告而另一些不被报告（finding-level）。[[Argument_Wolf_2020_JREE|Wolf et al. (2020, p. 441)]] 发现两种机制可能同时在运作。
> - **不等于[[Developer Effect|开发者效应]]** 发表偏倚是开发者效应的一个子机制，估计贡献约 66%，但不是全部解释。

### Rosenthal 的文件抽屉方法

Rosenthal（1991）提出了量化发表偏倚影响的经典方法：计算需要多少篇平均效果为零的未发表研究才能推翻已发表研究的显著结论。在一个例子中，这一比率为 **277:1**，表明仅凭发表偏倚很难完全解释已发表的显著结果。但该方法依赖未发表研究平均效果为零的[[Hypothesis|假设]]，这一假设本身可能不成立。Wolf（1986, pp. 14–17）将发表偏倚列为元分析的六项核心批评之一，指出已发表研究比未发表研究更受青睐。Glass et al.（1981, pp. 226–229）的回应是：元分析恰好适合纳入未发表的学位论文，这些论文往往包含更弱的相关系数，可以对冲已发表研究中更引人注目的结论（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen et al., 2011, Ch17, pp.357–358, 363–365]]）。

---

## 核心要素

> [!feature] 发表偏倚的双重机制
> [[Argument_Wolf_2020_JREE|Wolf et al. (2020, p. 429)]] 识别了教育评估中发表偏倚的双重来源：
> - **学术发表压力** 学术机构研究者面临发表压力，期刊偏好发表"引人注目、干净的故事"（John, Loewenstein, & Prelec, 2012; McBee, Makel, Peters, & Matthews, 2017）
> - **开发者经济激励** 开发者有更强的动机不传播关于其产品功效的零结果或负面结果——即使是开发者雇佣的[[Evaluator Independence|独立评估者]]也可能因不愿破坏与客户关系而压制零结果

> [!warning] 文件抽屉问题的最早案例（1940）
> Pratt and Rhine 在对 145 项超感知觉实验的[[Systematic Review|系统性综述]]中首次估计了未发表论文对总体汇总效果的影响。他们基于汇总证据认为超感知觉存在，但后世对此持怀疑态度——最重要的原因是这些发现未能被重复验证。这说明发表偏差可能导致系统性不完整的研究图景，即使按当时标准进行严格分析也可能无法发现（[[Argument_Higgins_2016_RE|Higgins, 2016, p.35]]）。

> [!info] Vevea-Hedges 权重函数模型
> [[Argument_Wolf_2020_JREE|Wolf et al. (2020, p. 438)]] 使用 Vevea & Hedges (1995) 权重函数模型估计经发表偏倚校正后的平均[[Effect Size|效应量]]：根据效应量的 p 值区间赋予不同权重，模拟不同显著水平下的发表概率差异，通过似然比检验判断校正模型是否比原始模型更好地拟合数据。

> [!info] 在[[Developer Effect|开发者效应]]中的角色
> 发表偏倚可解释约 66% 的开发者效应：开发者研究的原始效应量 +0.292，校正后 +0.276（差异不显著）；独立研究的原始效应量 +0.177，校正后 +0.200（差异显著，$p < .05$，但方向为反向——独立研究的校正效应量反而更大）。原始差异 0.115，校正后差异 0.076（[[Argument_Wolf_2020_JREE|Wolf et al., 2020, p. 442]]）。

> [!info] 对教育干预效应量分布的影响
> [[Argument_Kraft_2023_ER|Kraft (2023)]]指出，教育干预 [[Randomised Controlled Trials|RCT]] 的已发表效应量分布很可能已被发表偏倚推向较大的正效应，因此"36% 的效应量小于 0.05"仍可能低估失败频率。小样本研究若只发现很小估计效应，往往因统计功效不足而更不容易发表；美国教育部[[Categorical Funding|委托研究]]的中位数效应量为 0.03，低于完整样本的 0.10（[[Argument_Kraft_2023_ER|Kraft, 2023, p.186]]）。

## 历史沿革

> [!dev-timeline] 发表偏倚的概念演变
> - **1940 — Pratt and Rhine 的最早检测** 在对 145 项超感知觉实验的[[Systematic Review|系统性综述]]中首次估计未发表论文对汇总效果的影响（[[Argument_Higgins_2016_RE|Higgins, 2016, p.35]]）
> - **1991 — Rosenthal 的文件抽屉方法** 提出量化发表偏倚的经典方法，计算推翻显著结论所需未发表研究数量（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen et al., 2011, Ch17, p.355]]）
> - **1995 — Vevea & Hedges 权重函数模型** 提出用于[[Meta-analysis|元分析]]中发表偏倚统计校正的方法
> - **2020 — Wolf et al. 首次应用于[[Developer Effect|开发者效应]]** 将 Vevea-Hedges 校正应用于开发者 vs 独立研究的[[Effect Size|效应量]]比较
> - **2023 — Kraft 的教育 [[Randomised Controlled Trials|RCT]] 经验分布** 指出发表偏倚使教育干预"失败"的比例高于已发表[[Document|文献]]显示的 36%（[[Argument_Kraft_2023_ER|Kraft, 2023, pp.183, 186]]）

---

## 与相关概念的区别

> [!contrast-table] 与相关概念的区别
> - **vs [[Developer Effect]]** — 发表偏倚是开发者效应的一个子机制，估计贡献约 66%，但不是全部解释
> - **vs [[Researcher Degrees of Freedom]]** — 研究者自由度关注数据分析阶段的选择性决策，发表偏倚关注发表阶段的选择性传播；两者可以同时存在并叠加

---

## 争议与批评

> [!warning] 争议与批评
> - **Vevea-Hedges 校正的[[Hypothesis|假设]]** 权重函数模型依赖于对发表概率与 p 值关系的假设，且仅适用于研究级平均[[Effect Size|效应量]]，忽略研究内效应量变异([[Argument_Wolf_2020_JREE|Wolf et al., 2020, p. 442]])
> - **[[What Works Clearinghouse|WWC]] 数据的特殊性** 由于联邦报告要求，WWC 可能比一般学术期刊包含更多独立研究的零结果，因此发表偏倚在一般[[Document|文献]]中可能比在 WWC 中更严重

> [!warning] Wecker 等人（2016）的中央证据数据库提案
> Wecker, Vogel & Hetmanek（2016）在对 Hattie *[[Visible Learning]]* 的方法论批判中，提出了建立**中央证据数据库**的方案作为系统性缓解发表偏倚的路径([[Argument_Wecker_2016_ZfE|Wecker et al., 2016, p.34-36]])：
>
> - **不分发表状态的全量归档** "收集实证研究的方法和结果——无论期刊出版物如何——并以标准化和[[Meta-analysis|元分析]]可用的格式在中央数据库中提供"
> - **减少选择性发表扭曲** "可以显著减少由选择性发表研究结果引起的扭曲，并且对个别发现的元分析总结变得更加容易"
> - **统一效应量标准** 推荐使用 Hedges' g（标准化均值差的无偏估计量），并制定既定的处理标准
> - **每个元分析发布完整的主要研究表** 使结果可用于更新和其他主要研究的综合——而非像 Hattie 那样的不透明做法
> - **方法论理由** 目前"公共资源在全球范围内不断被用于研究——结果往往不是可靠的"（p.35）；"由于缺乏统计显著影响而在期刊上发表的机会很小"时，相关参数被埋没在文件抽屉中
>
> 这一提案的独特之处在于它将发表偏倚的解决方案定位于**基础设施层面**（集中式开放数据库），而非仅依赖[[Preregistration|预注册]]或期刊政策等程序性改革。Stanat（2012）的 DFG 备忘录也呼吁在教育研究中提供和使用[[Quantitative Research|定量研究]]数据。

---

## 实证检验案例

> [!case]- 实证检验案例：生成式 AI 教育元分析中的发表偏倚诊断（Zhao et al., 2025）
> - **偏倚审计情境** Zhao et al. (2025) 对生成式 AI 赋能高阶思维的 29 项实验与准实验研究（共 59 个效应量）展开多重发表偏倚质控与稳健性诊断。
> - **漏斗图与定量回归双重核验** 首先借助[[Funnel Plot|漏斗图]]目视检验散点空间对称性，确认除 8 个离群点外大多数研究围绕合并均值对称分布；进而采用 Egger 线性回归截距检验进行参数化检验，结果为 $t = 1.871, p = 0.066 > 0.05$。由于未达统计显著水平，排除了严重“文件抽屉效应”对总体合并效应量（$g = 0.609$）的实质性扭曲，证实了实证结论的稳健性。[[Argument_Zhao_2025_JIntell|(Zhao et al., 2025, pp. 9–10)]]

---

## 应用案例

> [!evidence-grid-a] 相关案例索引
> - [[Argument_Zhao_2025_JIntell|Zhao et al. (2025)]] — 结合漏斗图目视诊断与 Egger 线性回归检验（$t = 1.871, p = 0.066$）对生成式 AI 促进高阶思维的元分析证据池开展发表偏倚审计，确证了合并促学效应的发表稳健性。
> - [[Creation of REES]] — [[Preregistration|预注册]]制度被设计用于减少发表偏倚和选择性报告
> - [[ESSA 2015 Evidence Standards]] — 要求采用有证据支持的项目，间接增加了开发者的发表偏倚激励
