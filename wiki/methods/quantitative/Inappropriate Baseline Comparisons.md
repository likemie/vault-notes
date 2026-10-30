---
title: Inappropriate Baseline Comparisons
aliases:
  - 不当基线比较
  - 基准比较偏误
  - 不当基准比较
  - baseline comparison bias
  - baseline fallacy
  - 基线比较谬误
summary: "在实验、元分析与证据综合中因缺乏明确、对称或对等反事实对照基准，导致效应量符号与量级被人为操纵或歪曲的系统性统计方法偏误；在当代循证教育二阶综合中常表现为因单向基准依赖而逆转干预性质，属于科学可重复性危机中的三大核心统计错误之一。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 35
method_related_level: 3
method_related_stars: "💎"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - effect-size
  - meta-analysis
  - methodology-critique
  - causal-inference
  - statistical-bias
related_concepts:
  - "[[Reproducibility Crisis]]"
  - "[[Counterfactual]]"
  - "[[Unit of Analysis]]"
  - "[[Document]]"
  - "[[Type I and Type II Errors]]"
  - "[[Epistemology]]"
  - "[[Causality]]"
  - "[[Internal Validity]]"
  - "[[Sampling Error]]"
  - "[[Variable]]"
  - "[[Class Size]]"
  - "[[Socioeconomic Status]]"
  - "[[Gender Differences in Academic Achievement]]"
  - "[[Academic Achievement]]"
  - "[[Visible Learning]]"
  - "[[Central Question]]"
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Primary and Secondary Documents]]"
  - "[[Construct]]"
  - "[[Category Mistake]]"
  - "[[Commensuration]]"
  - "[[Zone of Desired Effects]]"
related_theories: []
related_methods:
  - "[[Experimental Research]]"
  - "[[Meta-analysis]]"
  - "[[Effect Size]]"
  - "[[Research Synthesis]]"
  - "[[Pre-test and Post-test]]"
  - "[[Baseline Standardized Mean Difference]]"
  - "[[Funnel Plot]]"
  - "[[Meta-meta-analysis]]"
  - "[[Cross-sectional Study]]"
related_instruments: []
related_persons:
  - "[[John Hattie]]"
  - "[[Pierre-Jérôme Bergeron]]"
related_facts: []
related_arguments:
  - "[[Argument_Bergeron_2017_MJE]]"
confidence: high
status: completed
created: 2026-10-18
updated: 2026-10-30
---

（不当基线比较）

---

> [!def] Inappropriate Baseline Comparisons
> **不当基线比较（Inappropriate Baseline Comparisons，亦称基准比较偏误）** 是指在[[Experimental Research|实验研究]]、[[Meta-analysis|元分析]]（Meta-analysis）与二阶综合中，由于未清晰界定、主观操纵或混淆对照基线总体，从而导致[[Effect Size|效应量]]（Effect Size, ES）正负方向、数值量级与实质因果定性产生系统性扭曲的统计方法偏误。阿利森等（Allison et al., 2016, p. 27）在《自然》（*Nature*）杂志上将其与“元分析计算失误”并列为当代科学[[Reproducibility Crisis|可重复性危机]]（Reproducibility Crisis）中的三大统计死穴之一；伯杰龙与里瓦尔（Bergeron & Rivard）进一步证实，在宏观教育[[Research Synthesis|证据综合]]中，脱离对等[[Counterfactual|反事实]]参照系的单向基线设定，会诱发政策推荐结论的根本性颠倒。[[Argument_Bergeron_2017_MJE|(Bergeron & Rivard, 2017, pp. 240–242)]]

> [!method-scope] 方法范围
> - **研究对象** 涉及组间均值差（Cohen's $d$、Hedges' $g$）、前[[Pre-test and Post-test|后测]]变化量、风险比及跨研究汇总效应量的实证研究设计。
> - **问题类型** 评估干预因果效力、建立跨干预效能排行榜、检验组间差距（如性别、阶层）的宏观综合评估。
> - **[[Unit of Analysis|分析单位]]** 原始实验对比组、元分析效应量数据点、二阶综合指标。
> - **输出形式** 基线参照系审计报告、符号对偶反转敏感性分析、加权调整后净效应估计量。

> [!citation-card] 科学研究中不当基线比较的系统性危害
> 在科学[[Document|文献]]中，最常见也最具破坏力的[[Type I and Type II Errors|统计错误]]之一便是对基线比较的不当处理。效应量尽管缺乏物理度量单位，但本质上是一个提供相对比较的无量纲测度。如果不明确比较的目标基线人群与反事实状态，研究者便能轻易通过选择单向基准，将其实质上微弱甚至有害的操作包装为正面干预成果，造成巨大的政策误导。[[Argument_Bergeron_2017_MJE|(Allison et al., 2016, p. 27; Bergeron & Rivard, 2017, pp. 240–241)]]
>
> *“The fundamental problem here is that every effect size, despite the absence of a unit, is a relative measure that provides a comparison to a set, group, or baseline population, even if it may be implicit. Inappropriate baseline comparisons constitute a tragedy of errors in science.”*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 建立在关系性认识论与现代[[Causality|因果推断]]框架之上。强调任何[[Effect Size|效应量]]都不存在孤立的客观绝对零点，所有测量数值的意义必须锚定在清晰界定的基线对比条件（*ceteris paribus* 参照系）之中。
> - **在因果推断中的角色** 充当[[Internal Validity|内部效度]]与结论有效性的质控滤网。审查基线设定是否合理，能够排查因对照组定义不清或参照系倒置引发的伪因果结论。
> - **有效性标准** 对偶一致性与[[Counterfactual|反事实]]对称性。一项合格的因果比较必须经得起参照系反转检验，其符号与分类逻辑应当在数学和政策伦理上保持内在自洽。
> - **不声称回答的问题** 无法单凭基线审查消除原始数据本身的[[Sampling Error|抽样误差]]或实验执行失误，必须结合全流程统计咨询与设计审查。

> [!method-stack] 方法层级
> - **研究设计** 涉及两组对比实验、准实验对照设计、多基线跨期分析与二阶证据汇总。
> - **分析技术** 相对测度对偶敏感性检验、倒数/反号对称性重算、亚群流行率加权分析。
> - **偏误诊断工具** 基线不平衡指数、协[[Variable|变量]]标准化均值差（[[Baseline Standardized Mean Difference|Baseline SMD]]）、[[Funnel Plot|漏斗图]]基线偏倚诊断。

---

## 机制与表现形态

### 1. 效应量符号的对偶可逆性原理

标准化均值差在数学定义上完全可逆，其正负符号直接取决于研究者主观指定的减数与被减数顺序。

> [!formula-step] 公式步骤　双样本标准化均值差的对偶可逆性
> $$d_{A \to B} = \frac{\mu_A - \mu_B}{\sigma_{\text{pooled}}} = - \left( \frac{\mu_B - \mu_A}{\sigma_{\text{pooled}}} \right) = - d_{B \to A}$$
>
> **这个公式在做什么** 计算条件 A 相对于基线条件 B 的[[Effect Size|效应量]]，揭示反向设定基线时的严格反号关系。
>
> **符号说明**
> - $\mu_A, \mu_B$ 分别为处理条件 A 与对照条件 B 的总体均值。
> - $\sigma_{\text{pooled}}$ 为合并标准差。
> - $d_{A \to B}$ 为 A 对比 B 的效应量；$d_{B \to A}$ 为 B 对比 A 的对偶效应量。
>
> **数学直觉** 组间均值差是纯粹的相对矢量，不存在单向绝对标量。若分析者仅凭单向正负号赋予价值判断（如将正值划为“有益”，负值划为“有害”），改变参照基准便会使价值评定瞬间颠倒。[[Argument_Bergeron_2017_MJE|(Bergeron & Rivard, 2017, p. 240)]]

---

### 2. 基线颠倒导致的价值定性突变

在教育循证宏观综合中，研究者常常在无意识中单向选定某一方作为基线，从而导致完全相悖的政策与社会学推论。

> [!contrast-table] 基线比较设定对效应量方向与政策判定的颠倒机制
> | 议题领域 | 单向基准设定 | 效应量 | 气压计分类判定 | 对偶反转基线设定 | 对偶效应量 | 反转后性质判定 | 方法学漏洞与实质后果 |
> |:---|:---|:---|:---|:---|:---|:---|:---|
> | **[[Class Size\|班级规模]]** | 小班 vs 大班（以大班为基线） | $d = +0.20$ | 低于 $d=0.40$ 阈值，被贬为“平庸无价值” | 大班 vs 小班（以小班为基线） | $d = -0.20$ | 严格落入 $d < 0$ 的“逆向有害效应区” | 维持或扩大班额直接构成损害学业的危险实践；单向基线掩盖了大班危害。 |
> | **[[Socioeconomic Status\|社会经济地位]]** | 优渥 vs 贫困（以贫困为基线） | $d = +0.59$ | 归入前列高效益区，但拒绝作为调节[[Variable\|变量]] | 贫困 vs 优渥（以优渥为基线） | $d = -0.59$ | 全书最具杀伤力的极端逆向破坏因素 | 贫困构成最深层的负向结构劣势，单向正值包装粉饰了阶级剥夺的严酷性。 |
> | **[[Gender Differences in Academic Achievement\|学业性别差距]]** | 男生 vs 女生（以女生为基线） | $d = +0.12$ | 宣称[[Academic Achievement\|学业表现]]轻微有利于男生 | 女生 vs 男生（以男生为基线） | $d = -0.12$ | 男生全面处于学业劣势 | 与跨国实证（女生在阅读与综合总评稳定领先）矛盾，暴露基准混淆失范。 |

---

### 3. 因素总体与文献总体的范畴混淆及鱼子酱物价指数隐喻

伯杰龙与里瓦尔（[[Argument_Bergeron_2017_MJE|Bergeron & Rivard, 2017, pp. 241–242]]）指出，不当基线比较不仅体现在双样本公式中，更深层地体现在宏观汇总时混淆了两类完全不同的总体：
1. **现实中影响学业成果的客观因素总体（Population of Influences）**；
2. **学者恰好就这些因素发表了一阶[[Meta-analysis|元分析]]的[[Document|文献]]总体（Population of Studies）**。

> [!concept-lens] 鱼子酱物价指数隐喻（The Caviar Price Index Metaphor）
> 假定经济学家进入一家大型杂货店，将店内所有上架商品的价格变动不加权地求算术平均，得出“海鲜类商品对普通家庭账单影响最大”的结论，理由是顶级鱼子酱的价格极其昂贵。
> 这一分析犯下了荒谬的基线加权错误：普通消费者在实际生活中极少购买鱼子酱，真实生活成本指数必须基于日常必需品（如土豆、面包）的购买频率实施加权。
> 在《[[Visible Learning|可见的学习]]》中，[[John Hattie|哈蒂]]将涵盖白血病、癌症、镰状细胞贫血及消化道疾病的罕见“疾病”效应量（$d = -0.20$），与千百万学生每天经历的课堂教学法赋予完全相同的未加权权重进行总平均，彻底脱离了学校教育生态的真实基线结构。[[Argument_Bergeron_2017_MJE|(Bergeron & Rivard, 2017, pp. 241–242)]]

---

> [!proc] 基线有效性审查的五步诊断清单
> 针对任何声称具备因果效力的量化[[Meta-analysis|元分析]]或实证综合，研究者应依序执行以下审查程序：
> 1. **确认[[Central Question|核心研究问题]]与因果意图** 明确该研究所考察的核心干预措施是什么，所声称的因果效应是否具备现实物理可行性。
> 2. **审查对照组性质与[[Counterfactual|反事实]]等价性** 审查对照组是个体自身的基线[[Pre-test and Post-test|前测]]、接受常规教学的独立对照组，还是不同维度的横向关联群体；严禁将未受操纵的自然群体差异直接充当干预基线。
> 3. **核查[[Variable|变量]]测量的生态层级** 审查[[Independent Variable|自变量]]与[[Dependent Variable|因变量]]是在微观个体、班级组织、学校还是国家行政层级测度，防止跨层级基线漂移。
> 4. **实施符号对偶反转敏感性测试** 将减数与被减数的方向完全对调，检验所得负[[Effect Size|效应量]]在理论框架与分类标准下是否导出荒谬结论。若改变基准即摧毁全书逻辑自洽性，表明该基准属于人为武断设定。
> 5. **审查加权模型与生态流行率** 核实跨领域均值汇总时是否对各类现象在现实人群中的真实暴露率与发生频率实施了恰当加权，排除“鱼子酱指数”式数据拼凑。

---

> [!method-fit] 适用判断
> - **适合使用基线审查的场景** 针对大规模证据清理库、跨国二阶[[Meta-meta-analysis|元综合]]报告以及教育公共政策优先级清单展开方法学审计与质检。[[Argument_Bergeron_2017_MJE|(Bergeron & Rivard, 2017, pp. 240–242)]]
> - **谨慎解释的场景** 当主要研究受限于伦理条件无法设立纯粹无干预对照组、只能使用替代疗法或次优方案作为基准时，必须在报告中明确声明基线为相对活性对照而非绝对零点。
> - **严禁使用的做法** 严禁脱离基线说明直接抛出孤立的[[Effect Size|效应量]]排行榜；严禁将横截面关联作为干预前后因果增益与基线进行对比。

> [!method-limits] 方法局限与偏误防范
> - **防范基线漂移** 统一规范同一[[Meta-analysis|元分析]]池中所有[[Primary and Secondary Documents|原始文献]]的比较基准，严禁将“干预组 vs 对照组”研究与“高分组 vs 低分组”[[Cross-sectional Study|横截面研究]]混入同一分析模型。
> - **放弃通用绝对阈值依赖** 废除缺乏物理基准的硬性数值截断线（如 $d=0.40$），转而依据具体学科情境、基准控制质量与公共实施成本进行多维综合权衡。
> - **引入独立统计咨询协作** 在教育实证设计之初即联合专业统计学者共同制定基线规程，从源头杜绝基线比较失范。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Effect Size]] | 上位方法 | 效应量属于相对无量纲指标，其数学与实践解释严格依赖于基线参照系的界定。 |
> | [[Baseline Standardized Mean Difference]] | 前置工具 | 基线标准化均值差用于检验实验组与对照组在干预前的等价性，防范基线选择偏误。 |
> | [[Counterfactual]] | [[Construct\|理论构念]] | 反事实推理构成了[[Causality\|因果推断]]的核心基石，不当基线本质上是对反事实状态的虚构或错配。 |
> | [[Category Mistake]] | 哲学概念 | 将具有异质基线前提的效应量视为具有普遍绝对零点的实体刻度，属于典型的范畴错置。 |
> | [[Commensuration]] | 概念透镜 | 不当基线比较是强行通约异质[[Variable\|变量]]时的典型副产物，抹平了基线背后的结构性差异。 |
> | [[Class Size]] | 实证案例 | 班级规模因基准反转（$+0.20 \leftrightarrow -0.20$）直接从低效区跌入逆向有害区，成为基线偏误典型反例。 |
> | [[Socioeconomic Status]] | 实证案例 | 贫困背景因基准反转（$+0.59 \leftrightarrow -0.59$）逆转为全书最大破坏因素，揭露单向基准对阶级压迫的掩饰。 |
> | [[Gender Differences in Academic Achievement]] | 实证案例 | 单向二阶基准（$d=+0.12$ 男生占优）与跨国实证现实相脱节，证实宏观粗放基准汇总的失真。 |
> | [[Zone of Desired Effects]] | 批判靶标 | 哈蒂设立的 $d=0.40$ 期望分水岭高度依赖于单向正向基线假设，基线颠倒直接瓦解了该分界线的有效性。 |
> | [[Pierre-Jérôme Bergeron]] | 代表学者 | 统计学者，系统发表数理对偶审计论文，揭露基线不当比较在教育[[Meta-meta-analysis\|元综合]]中的灾难性后果。 |
> | [[Argument_Bergeron_2017_MJE\|Bergeron and Rivard (2017)]] | 实证与方法学来源 | 系统论证基线颠倒、鱼子酱指数隐喻及因素/文献总体混淆的方法学批判奠基之作。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Bergeron_2017_MJE|Bergeron and Rivard (2017)]] — 从数理统计学视角剖析《[[Visible Learning|可见的学习]]》中的不当基准比较，以[[Class Size|班级规模]]、社会阶层和性别为例证实基线颠倒彻底推翻政策结论，提出鱼子酱未加权物价指数隐喻（pp. 240–242）。
> - Allison et al. (2016) — 在《自然》（*Nature*）系统归纳科学研究中的三大致命[[Type I and Type II Errors|统计错误]]，将不当基线比较确立为诱发[[Reproducibility Crisis|可重复性危机]]的核心偏误类型（pp. 27–29）。
