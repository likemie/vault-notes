---
title: Meta-analysis
aliases:
  - 元分析
summary: "通过汇总多项原始研究的效应量来综合证据的统计方法，常用于比较干预强度、估计平均效果和检验结果一致性"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 53
method_related_level: 6
method_related_stars: "⭐⭐⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - meta-analysis
  - effect-size
  - evidence-based-education
  - statistical-synthesis
  - methodology
related_concepts:
  - "[[Effect Size]]"
  - "[[Sampling Error]]"
  - "[[Evidence-Based Education]]"
  - "[[Sample Size Determination]]"
  - "[[Variable]]"
  - "[[Humility in Learning]]"
  - "[[Epistemology]]"
  - "[[Reliability]]"
  - "[[Critique of Meta-analysis]]"
  - "[[Ontology]]"
  - "[[Forest Plot]]"
  - "[[Visible Learning]]"
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Fitness for Purpose]]"
  - "[[Interaction Effect]]"
  - "[[Heterogeneity]]"
  - "[[Intercoder Agreement]]"
  - "[[Statistical Significance]]"
  - "[[Research Question]]"
  - "[[Hypothesis]]"
  - "[[Research Utilization]]"
  - "[[Class Size]]"
  - "[[Publication Bias]]"
related_theories:
  - "[[Critical Realism]]"
related_methods:
  - "[[Coding in Qualitative Research]]"
  - "[[Moderator Analysis]]"
  - "[[Meta-meta-analysis]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Secondary Analysis]]"
  - "[[Random Sampling]]"
  - "[[Analysis of Variance]]"
  - "[[Fixed-Effect and Random-Effects Models]]"
  - "[[Systematic Review]]"
  - "[[Quantitative Research]]"
  - "[[Experimental Research]]"
  - "[[Observation Method]]"
related_persons:
  - "[[Gene Glass]]"
  - "[[Karl Pearson]]"
related_facts:
  - "[[EEF Teaching and Learning Toolkit]]"
  - "[[Education Endowment Foundation]]"
related_arguments:
  - "[[Argument_Higgins_2016_RE]]"
  - "[[Argument_Wiliam_2019_ERE]]"
  - "[[Argument_Wrigley_2019_ERE]]"
  - "[[Argument_Qvortrup_2015_Paideia]]"
  - "[[Argument_Qvortrup_2019_NordSTEP]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17]]"
  - "[[Argument_Berk_2011_ER]]"
  - "[[Argument_Simpson_2017_JEP]]"
  - "[[Argument_Snook_2010_NZJES]]"
  - "[[Argument_Hattie_2015_Paideia]]"
  - "[[Argument_Hattie_2015_SOTLP]]"
  - "[[Argument_Wrigley_2018_BERJ]]"
confidence: medium
status: draft
created: '2026-05-01'
updated: 2026-07-14
---

# Meta-analysis

---

## 定义

> [!def] 核心定义
> 元分析（Meta-analysis）是"对分析的分析"（the analysis of other analyses），即聚合和合并可比较研究的结果以发现主要效应。该术语由 [[Gene Glass]] 于 1976 年在美国教育研究协会主席演说中首次提出（Glass, 1976），Glass et al.（1981）将其发展为系统方法（pp.341–343）。
>
> 定量元分析的核心操作是：对多项独立研究的[[Effect Size|效应量]]进行统计综合，同时分析效应量与纳入研究特征之间的关系。统计处理用于减弱污染因素的影响，如[[Sampling Error|抽样误差]]、测量误差和范围限制。研究发现被[[Coding in Qualitative Research|编码]]为实质性类别以便概括（Glass et al., 1981），使传统叙事综述会错过的发现一致性得以揭示。质性元分析同样被倡导（pp.341–343）。
>
> 元分析有两个核心目标：判断某一干预或方法总体上是否有效，以及通过[[Moderator Analysis|调节变量分析]]解释研究间效果的变异（[[Argument_Higgins_2016_RE|Higgins, 2016, p.32]]）。
>
> [[Argument_Wiliam_2019_ERE|Wiliam (2019, p.11)]] 在定义上增加了关键的层级区分：元分析综合原始研究的效应量；而[[Meta-meta-analysis|元-元分析]]是通过效应量的加权合并综合多个元分析的结果，是另一回事。Wiliam 断言后者在教育政策制定中绝对没有任何角色。
>
> 在[[Evidence-Based Education|证据本位教育]]中，元分析被用作综合[[Randomised Controlled Trials|随机对照试验]]（RCT）证据的核心工具，其结论（平均效应量）被视为"什么有效"的主要证据来源（[[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, p. 118]]）。

### 三层分析

Glass（1976）和 Glass et al.（1981）区分了三个层次的分析（p.344）：

> [!info] 三层分析框架
> 1. **初级分析（Primary analysis）** 对原始数据的最初分析
> 2. **次级分析（[[Secondary Analysis|Secondary analysis]]）** 使用不同统计量对数据的再分析，以回答新问题
> 3. **元分析（Meta-analysis）** 对多项独立研究的结果进行统计分析以整合发现

早期元分析使用组合概率和结果落入定义类别的频率（如在给定水平上是否显著），但[[Sample Size Determination|样本量]]差异混淆了严谨性：大样本可使微小效应显著，小样本的重要数据可能因未达显著性而被遗漏（Light & Smith, 1971; Glass et al., 1981; McGaw, 1997: 371）（pp.343–344）。

---

## 方法定位

### 为什么需要元分析：叙事综述的局限

元分析的兴起部分源于对传统叙事综述的不满。McGaw（1997: 371）认为定量元分析用透明和明确的程序替代了叙事综述中常见的主观判断（Wood, 1995: 389），在研究间差异很大时尤其必要。Jackson（1980）、Cook et al.（1992: 13）和 Wood（1995: 390）系统指出了叙事综述的九项缺陷（pp.342–343）：

> [!critique] 叙事综述的九项缺陷
> 1. **缺乏全面性** 具有选择性，只涉及部分研究
> 2. **错误和粗略呈现** 对研究发现进行歪曲和粗糙的表述
> 3. **过度依赖显著性检验** 忽视样本量对显著性水平的主要影响，也忽视效应量
> 4. **忽视[[Random Sampling|随机抽样]]误差** 未能认识到随机[[Sampling Error|抽样误差]]可以导致研究间发现的变化
> 5. **忽视冲突发现** 忽略不同和相互矛盾的研究发现
> 6. **未批判性审查先前综述** 未能审查先前综述的证据、方法和结论
> 7. **忽视样本特征的中介作用** 忽视研究发现受样本特征中介的程度
> 8. **忽视中介[[Variable|变量]]** 忽视中介变量在研究中的重要性
> 9. **不可复制** 因综合研究发现的程序未明示而不可复制

### 元分析的优势

Fitz-Gibbon（1985: 46）从实用角度列举了元分析的三项优势（p.341）：

> [!strength] Fitz-Gibbon (1985: 46) 的三项优势
> - **让被遗忘的小规模报告重获价值** 那些[[Humility in Learning|谦逊]]的小规模报告不必继续蒙尘，可以通过元分析贡献证据
> - **汇总多研究结果而不必协调研究本身** 个别学生和教师的小规模研究因此变得有用，元分析从多项独立研究中提取和合并结果，不需要研究者之间事先协商统一方案
> - **开辟历史比较的新维度** 将不同年代的效应量串联起来，考察干预效果如何随历史条件变化，为教育史研究提供量化视角

### 认识论前提与有效性问题

> [!method-position] [[Epistemology|认识论]]前提与有效性问题
> **研究者角色** 元分析者作为二次分析师，从原始研究中提取和重新组织证据，而非直接收集数据。
>
> **有效性标准** 元分析的效度取决于源研究的质量、纳入标准的合理性、[[Coding in Qualitative Research|编码]]的[[Reliability|可靠性]]以及统计模型的适用性。详见 [[Critique of Meta-analysis]]。
>
> **不能回答的问题** 元分析不能替代对因果机制的实质理解。[[Critical Realism|批判实在论]]从三层[[Ontology|本体论]]（实在/实际/经验）角度指出元分析停留在"经验"层面（观察到的[[Effect Size|效应量]]），未能深入"实在"层面（产生效应的因果机制及其激活条件）（[[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, pp. 116–117]]）。

---

## 历史发展

> [!dev-timeline] 元分析的历史发展脉络
> - **1904 — Pearson 的思想先驱** [[Karl Pearson|Karl Pearson]] 在《英国医学杂志》上发表了最早的跨研究合并分析——合并英国军队在印度和南非的伤寒疫苗接种数据。他同时追求两个目标：合并多项小研究的发现以获得更可靠结论，以及探索研究间效果变异的原因（如志愿者自我选择偏差）。他将每项研究结果以独立行呈现并给出平均相关系数的呈现方式，预示了后来[[Forest Plot|森林图]]的标准形式（[[Argument_Higgins_2016_RE|Higgins, 2016, p.33]]）。
>
> - **1930s–1950s — Fisher 的统计基础** Ronald Fisher 在[[Analysis of Variance|方差分析]]等技术上的发展为跨研究比较奠定了统计基础，鼓励研究者清晰严格地报告发现（[[Argument_Higgins_2016_RE|Higgins, 2016, p.34]]）。
>
> - **1976 — 命名与确立** [[Gene Glass|Gene Glass]] 在美国教育研究协会主席演说中首次提出"元分析"一词。他与 Mary Lee Smith 合作的心理治疗效果元分析（Smith & Glass, 1977）发现平均[[Effect Size|效应量]]为 0.6 个标准差，直接挑战了 Eysenck 的心理治疗无效共识。Glass 将效应量确立为跨研究比较的通用尺度（[[Argument_Higgins_2016_RE|Higgins, 2016, pp.36–37]]）。
>
> - **1970s–1980s — 医学领域的扩展** Peter Elwood 和 Archie Cochrane 等人通过阿司匹林预防心脏病发作的随机试验展示了元分析在医学证据综合中的力量。Richard Peto 推广了[[Fixed-Effect and Random-Effects Models|固定效应模型]]（按精度加权），Larry Hedges（1983）倡导随机效应模型，DerSimonian & Laird（1986）提供了简化公式（[[Argument_Higgins_2016_RE|Higgins, 2016, pp.38–39]]）。
>
> - **1980s — "苹果和橙子"争论** Eysenck 称元分析为"超级愚蠢"，批评其将不可比的研究混为一谈。Slavin（1984）同样提出苹果和橙子问题。Glass 的回应是："当然它混合苹果和橙子；在研究水果时没有别的合理做法"——任何推论都直接取决于元分析所包含的内容（[[Argument_Higgins_2016_RE|Higgins, 2016, p.37]]）。
>
> - **1990s–2000s — [[Systematic Review|系统综述]]的制度化** 1993 年 Cochrane 协作网成立，将系统综述和元分析制度化为医学证据综合的标准方法。2009 年 PRISMA 声明发布，为系统综述的透明报告提供了标准化框架（[[Argument_Higgins_2016_RE|Higgins, 2016, p.38]]）。
>
> - **1990s–2010s — 教育领域的扩展** 元分析在教育研究中的应用从 1990 年代起迅速扩展。Hattie（1992）综合了 134 项元分析，2008 年扩展至 800 多项。[[EEF Teaching and Learning Toolkit]]（2011）将元分析结果转化为面向实践者的政策工具。然而[[Sample Size Determination|样本量]]与效应量之间的系统性相关（r = –0.28）表明该领域仍面临方法论挑战（[[Argument_Higgins_2016_RE|Higgins, 2016, p.48]]）。

---

## 研究程序

### 基本流程

> [!proc] 元分析的四步基本流程
> 1. **选择源研究** 基于技术标准（如是否为 [[Randomised Controlled Trials|RCT]]）筛选相关研究
> 2. **提取[[Effect Size|效应量]]** 从每项源研究中提取或计算标准化[[Effect Size|效应量]]
> 3. **加权与平均** 对效应量进行加权（通常按[[Sample Size Determination|样本量]]），计算平均效应量
> 4. **报告** 以平均效应量（有时转换为更直观的单位，如 [[Education Endowment Foundation|EEF]] Toolkit 的"额外学习月数"）呈现结果
>
> [[Meta-meta-analysis|元-元分析]]是在元分析基础上进一步聚合——综合多个元分析的效应量产生更高层次的排名或估计。Wecker, Vogel & Hetmanek（2016）从[[Fixed-Effect and Random-Effects Models|固定效应模型]]推导了该方法必须满足的 6 项方法论要求，并论证 Hattie 的 *[[Visible Learning]]* 在六个分析步骤中均存在方法论不足。完整技术细节见 [[Meta-meta-analysis]]。

---

### 详细操作模型

> [!info] 四套详细操作模型（pp.343–357）
> 以下四套模型从不同角度补充了基本流程，分别代表了 Glass、Cook、Fitz-Gibbon 和 Gorard 的方法论取向：

#### Glass et al. (1981) 与 Hunter et al. (1982) 的八步法

> [!proc] Glass & Hunter 八步程序（pp.344–346）
> 1. **确定关注的[[Variable|变量]]** 识别[[Independent Variable|自变量]]和[[Dependent Variable|因变量]]
> 2. **识别所有涉及这些变[[Quantitative Research|量的研究]]**
> 3. **[[Coding in Qualitative Research|编码]]研究特征** 对每项研究[[Coding in Qualitative Research|编码]]可能预测结果和效应量的特征（如参与者年龄、性别、种族、干预持续时间）
> 4. **计算效应量** 计算每对变量（因变量和自变量）的效应量（见 Glass, 1977），按样本量加权
> 5. **计算均值和标准差** 计算跨研究效应量的均值和标准差，即跨研究方差
> 6. **确定误差影响** 确定[[Sampling Error|抽样误差]]、测量误差和范围限制的影响
> 7. **判断准确性** 若方差的大部分归因于步骤 6 的问题，平均效应量可被视为变量间关系的准确估计
> 8. **审查相关特征** 若方差的大部分不可归因于步骤 6，则审查与效应量相关的特征

#### Cook et al. (1992: 7–12) 的四阶段整合性综述

> [!proc] Cook 四阶段整合性综述（pp.346–348）
> 1. **问题形成（Problem formulation）** 高质量元分析必须在综述的设计、执行和分析上保持严谨
> 2. **数据收集（Data collection）** 纳入研究的抽样必须展示[[Fitness for Purpose|目的适配性]]
> 3. **数据检索与分析（Data retrieval and analysis）** 处理非[[Experimental Research|实验研究]]（整合性综述即属此类）中的效度威胁，效度必须展示目的适配性、编码[[Reliability|信度]]，并关注原始研究的方法论严谨性
> 4. **分析与解释（Analysis and interpretation）** 多项研究的累积发现应被视为复杂数据点，需要通过细致的统计分析来解释

#### Fitz-Gibbon (1984: 141–142) 的四步法

> [!proc] Fitz-Gibbon 四步程序（pp.348–349）
> 1. **寻找研究** 寻找可计算效应量的研究（已发表和未发表）
> 2. **编码研究特征** 日期、发表状态、设计特征、设计质量、研究者身份
> 3. **测量效应量** 将实验组定位为控制组分布中的 z 分数，使结果可在共同尺度上测量，控制"块状数据"（lumpy data，即大数据集中的非独立数据）
> 4. **关联效应量与情境变量** 区分控制良好和控制不佳的研究，识别两者之间的差异

#### Gorard (2001b: 72–73) 的四步模型

> [!proc] Gorard 四步程序（pp.355–356）
> 1. 收集所有适合纳入的研究
> 2. 按规模和质素对每项研究加权
> 3. 列出使用的结果测量
> 4. 根据收集的数据性质选择聚合方法（如计数出现效应的研究和不出现效应的研究，或计算跨研究的平均效应量）

---

### 质量控制：Wolf (1986) 的十条改进建议

面对元分析面临的多维度批判，Wolf（1986: 55–56）提出了十条程序层面的改进建议，聚焦于"如果要做元分析，怎样才能做得更严谨"（pp.359–362）：

> [!proc] Wolf 的十条程序改进建议
> 1. **明确纳入排除标准** 使研究的纳入和排除标准清晰
> 2. **搜索未发表研究** 主动寻找未发表的研究
> 3. **扩大编码范围** 制定涵盖最广泛已识别研究的编码类别
> 4. **检查[[Interaction Effect|交互效应]]** 寻找[[Interaction Effect|交互效应]]，分别检查多个自变量和因变量
> 5. **检验[[Heterogeneity|异质性]]和异常值** 检验结果的[[Heterogeneity|异质性]]和异常值的影响，绘制结果分布图
> 6. **检查[[Intercoder Agreement|编码者间信度]]** 检查[[Intercoder Agreement|编码者间信度]]
> 7. **使用效应量指标** 使用效应量指标而非[[Statistical Significance|统计显著性]]
> 8. **计算未调整和加权结果** 同时计算未调整（原始）和加权的检验与效应量，以检查样本量对结果的影响
> 9. **结合定性与定量方法** 将定性和定量综述方法结合
> 10. **报告局限性** 报告所进行元分析的局限性

> [!info] Thomas & Pring (2004) 的补充要求
> 从研究设计层面，元分析还应明确说明：[[Research Question|研究问题]]、概念框架、综述协议、搜索和检索策略，以及多项研究发现被整合的具体方式（Thomas & Pring, 2004: 54–55）（pp.362）。

---

### 效应量计算

效应量是元分析中优先于[[Statistical Significance|统计显著性]]的统计量，也是元分析的核心分析单位（pp.349–353）。

> [!formula-step] Glass et al. (1981: 29, 102) 的效应量公式
> $$\Delta = \frac{M_{\text{实验组}} - M_{\text{对照组}}}{SD_{\text{控制组}}}$$
>
> 其中 $M_{\text{实验组}}$ 为实验组均值，$M_{\text{对照组}}$ 为控制组均值，$SD_{\text{控制组}}$ 为控制组标准差。Wood（1995: 393）建议效应量也可通过将显著性水平除以样本量来计算。

Hedges（1981）和 Hunter et al.（1982）提出了考虑样本量差异的不同权重的替代公式。Lipsey（1992: 93–100）列出了处理效应量、效应量均值和同质性的系列统计检验。最常用的两种效应量指标是标准化均值差和相关系数（Glass et al., 1981: 373），非参数统计量（如中位数）也可使用。

> [!warning] 适用范围限制
> Glass 等人[[Hypothesis|假设]]元分析仅适用于实验型研究而非所有类型的研究，这可能限制其适用性（pp.350–351）。

---

## 适用场景

> [!success] 作为效果总体估计的工具
> - 当有大量使用可比较设计和结果测[[Quantitative Research|量的研究]]时，元分析可以提供效果的总体估计
> - 在医学领域（其起源领域），元分析在已有充分理论理解治疗机制的前提下可以补充回答"效果平均多大"
> - 元分析对教育研究尤其重要，因为许多小型研究具有中等或较低的效果，可能无法达到[[Statistical Significance|统计显著性]]。Cooper & Rosenthal（1980）的实证检验表明，元分析比传统叙事综述更不容易低估证据。Gorard（2014）同样指出，合并小型研究可以提供答案，而不必过度依赖与[[Sample Size Determination|样本量]]直接相关的统计显著性（[[Argument_Higgins_2016_RE|Higgins, 2016, p.32]]）
> - 教育领域中使用元分析的倡导者认为它适合为实践者和政策制定者提供关于"什么有效"的总结性指导（[[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, pp. 110–111]]）

> [!success] 作为追问变异和调节[[Variable|变量]]的工具
> - Hattie（2015）从支持者立场强调，元分析最有价值的用法不是把平均效应当成最后答案，而是迫使教育者追问调节[[Variable|变量]]和竞争解释：哪些年龄、学段、文化、先前成绩和结果测量类型会改变效果，平均值背后的变异说明了什么（Hattie, 2015, pp.10–11, 14–15）
> - [[Argument_Qvortrup_2015_Paideia|Qvortrup (2015, pp.25–27)]]从支持者立场认为，教育元分析不需要等待所有[[Research Utilization|研究使用]]完全相同的学习结果定义才可比较；[[Effect Size|效应量]]提供的是干预组与控制组或干预前后之间的相对效果，因此可以跨研究比较"相对学习结果"。但这种比较的代价是学习结果变得抽象，研究者难以说明测量的是表层知识、深层理解、社会能力还是概念性学习（[[Argument_Qvortrup_2015_Paideia|Qvortrup, 2015, p.27]]）
> - [[Argument_Qvortrup_2019_NordSTEP|Qvortrup (2019, p.5)]]从支持者立场提出"观察透镜"论证：元分析是系统观察的一种形式，所有观察都从特定位置和特定透镜进行，元分析透镜产生的图像与定性[[Observation Method|观察研究]]的图像不同但互补——前提是两者均遵循高效度标准
> - [[Argument_Wiliam_2019_ERE|Wiliam (2019, p.11)]]的谨慎立场：如果且仅当满足 11 项条件，元分析才可能值得严肃对待

### 典型案例：班级规模与学习成就（Glass & Smith, 1978）

> [!case] Glass & Smith · [[Class Size|班级规模]]与学习成就
> Glass & Smith（1978）和 Glass et al.（1981: 35–44）收集了 **77 项**关于[[Class Size|班级规模]]与学生学习的实证研究，共 **725 项**大小班级成就比较，数据来自近 **900,000 名**各年龄段和能力的学生，覆盖各学科领域。使用回归分析，725 项比较被整合为一条显示班级规模与成就关系的单一曲线，揭示了明确的**负相关**。
>
> 研究者随后在不同情境下推导类似曲线：年级水平、学科类型、学生能力等。结果发现，**几乎没有任何特殊情境改变了这一基本关系**。只有一个因素显著影响了曲线形态：**原始研究是否进行了充分的实验控制**。控制充分的研究（well-controlled studies）产生了更陡峭的曲线，控制不充分的研究（poorly controlled studies）曲线较平坦。Glass et al. 据此按控制质量分层呈现效应量，而不是报告单一的平均值。
>
> 值得注意的是，不充分的控制倾向于**低估**班级规模效应，而不是像通常[[Hypothesis|假设]]的那样混杂变量会夸大效应。这一发现颠覆了控制不佳的研究必然高估效应的直觉。
>
> > [!example]- 图17.1：班级规模与学习成就——控制良好与控制不佳研究的回归线
> > ![](https://img.mylikemie.icu/books/Cohen_Manion_Morrison_2011_Routledge/figures/Figure_17-1_Class_Size_and_Learning.jpg)
> >
> > *Regression lines for the regression of achievement (expressed in percentile ranks) onto class size for studies that were well-controlled and poorly controlled.*
> >
> > Source: Adapted from Glass & Smith, 1978
>
> [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|(Cohen et al., 2011, Ch17, pp.357–360)]]

---

## 局限性

> [!warning] 批判总览
> 元分析面临来自方法论前提、操作程序、统计推断和政策用途等多层面的系统批判，涵盖研究可比性（苹果和橙子问题）、输入质量（垃圾进垃圾出）、[[Publication Bias|发表偏倚]]、非独立数据与过度简化、伪精确性、统计推断[[Hypothesis|假设]]违背、抽样与伦理问题、领域迁移不匹配、平均效应误导以及[[Meta-meta-analysis|元-元分析]]的偏倚传播。[[Argument_Wiliam_2019_ERE|Wiliam (2019)]]提出了 11 点评估清单作为元分析可[[Reliability|信度]]的检验框架。详细的批判维度、学者论证与回应见 [[Critique of Meta-analysis]]。

> [!warning] 操作层面的关键提醒
> - **可比性** 根本不同的研究被聚合时，平均[[Effect Size|效应量]]的解释力有限。[[Gene Glass]]——元分析的创始人——本人警告："元分析的结果永远不应该是平均值；它应该是一张图"（Robinson, 2004, p. 29, cited in [[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, p. 119]]）。
> - **输入质量** Eysenck（1978）的"垃圾进，垃圾出"奠定了所有方法论批评的基础命题：聚合的质量取决于输入的质量。
> - **统计推断** [[Argument_Berk_2011_ER|Berk (2011)]]和 [[Argument_Simpson_2017_JEP|Simpson（2017）]]论证元分析的统计推断假设在教育研究中几乎从未被满足。
> - **领域差异** [[Argument_Snook_2010_NZJES|Snook et al.（2010）]]指出元分析在医学中成功运作的条件（概念清晰、设计标准化、机制可分离）在教育领域经常不成立。
> - **平均效应** Kluger & DeNisi（1996）的反馈元分析显示，平均 d ≈ 0.4 掩盖了约 38% 的效应量为负的事实（[[Argument_Wiliam_2019_ERE|Wiliam, 2019, pp.10–11]]）。
> - **二级聚合** [[Meta-meta-analysis|元-元分析]]在聚合层级间传播和放大偏倚。详见 [[Critique of Meta-analysis]]。

---

## 替代方案

面对上述局限，Pawson（2006）提出了**实在论综合（Realist Synthesis）**作为替代路径。不同于元分析追求单一平均效应量，实在论综合基于因果理论追问干预"为什么有效、对谁有效、在什么条件下有效"，基于理论相关性而非纯技术标准选择源研究，输出形式为揭示效应变异性的分散图景（[[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, pp. 119, 123]]）。

---

## 相关理论与方法

> [!info] 相关理论
> - [[Critical Realism]] — 为元分析的经验主义[[Hypothesis|假设]]提供了系统的哲学批判：因果机制而非[[Effect Size|效应量]]平均值才是科学知识的真正对象

> [!info] 相关方法
> - [[Systematic Review]] — 元分析的前置步骤，通过系统搜索和筛选识别符合条件的研究
> - [[Moderator Analysis]] — 元分析中解释研究间效果变异的核心分析技术
> - [[Meta-meta-analysis]] — 在元分析基础上进一步聚合，综合多个元分析的效应量
> - [[Fixed-Effect and Random-Effects Models]] — 元分析中两种基本的统计建模策略
> - [[Randomised Controlled Trials]] — 元分析最常见的源研究设计类型

---

## 使用此方法的研究

> [!evidence-grid-a] 研究案例索引
> - [[Argument_Hattie_2015_Paideia]] — Hattie 回应《[[Visible Learning|可见的学习]]》批评时把元分析解释为寻找调节[[Variable|变量]]和竞争解释的证据地图，而不是直接替教师做决策的排名表
> - [[Argument_Hattie_2015_SOTLP]] — Hattie 将 1200 项元分析（65,000 多项研究）综合应用于高等教育，提出六项关键发现和八项思维框架
> - [[Argument_Wrigley_2019_ERE]] — 通过 [[Education Endowment Foundation|EEF]] Toolkit 体育参与案例的深度追踪揭示[[Meta-meta-analysis|元-元分析]]的程序缺陷
> - [[Argument_Wrigley_2018_BERJ]] — 对元分析和元-元分析（Hattie / EEF Toolkit）的系统方法论批判
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen, Manion & Morrison (2011, Ch17)]] — 系统介绍元分析的四种操作模型（Glass 八步、Cook 四阶段、Fitz-Gibbon 四步、Gorard 四步）、[[Effect Size|效应量]]计算、[[Class Size|班级规模]]案例及多维度批判

---
