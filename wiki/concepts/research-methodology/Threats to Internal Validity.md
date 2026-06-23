---
title: Threats to Internal Validity
aliases:
  - 内部效度威胁
  - threats to internal validity
  - internal validity threats
summary: "在量化实验研究中可能混淆自变量与因变量之间真实因果关系的系统性偏差来源，Campbell 和 Stanley 经典框架列出十种主要威胁，Onwuegbuzie 和 Leech 将其扩展至质性研究中的十二种威胁"
type: concept
domain: "research-methodology"
related_count: 20
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
tags:
  - method/research-methods
  - theme/validity
  - theme/causal-inference
related_concepts:
  - "[[Internal Validity]]"
  - "[[Variable]]"
  - "[[Evaluation Research]]"
  - "[[Reliability]]"
  - "[[External Validity]]"
  - "[[Causality]]"
  - "[[Type I and Type II Errors]]"
  - "[[Null Hypothesis]]"
  - "[[Descriptive Validity]]"
  - "[[Hawthorne Effect]]"
  - "[[Effect Size]]"
  - "[[Negative Case Analysis]]"
  - "[[Positivism]]"
related_methods:
  - "[[Intervention Research]]"
  - "[[Random Assignment]]"
  - "[[Quantitative Research]]"
  - "[[Qualitative Research]]"
  - "[[Ethnography]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10]]"
  - "[[Argument_Creswell_2022_SAGE]]"
status: draft
created: 2026-06-23
updated: 2026-06-23
---
# Threats to Internal Validity

---

## 定义

> [!def] 核心定义
> [[Internal Validity|内部效度]]威胁（Threats to internal validity）指在研究过程中可能混淆自[[Variable|变量]]与因变量之间真实关系、使研究者无法确定观测到的效应究竟是来自研究处理还是来自其他混淆因素的系统性偏差来源。[[Internal Validity|内部效度]]寻求证明一项研究的解释实际上能为数据所支撑（p.164），而内部效度威胁正是那些**削弱这一证明力的因素**。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|(Cohen et al., 2011, Ch. 10, pp. 164–168)]]

> [!concept-lens] 概念透镜
> - **含义** 内部效度威胁不是"研究犯了错误"的清单，而是任何研究中都**潜在存在**的系统性偏差来源。研究者需要识别这些威胁并采取措施**减弱**其影响，而非声称完全消除了它们。
> - **用途** 在研究设计阶段，内部效度威胁框架帮助研究者预见可能的混淆因素并预先设计控制策略；在评估已有研究时，该框架提供了批判性[[Evaluation Research|评估研究]]结论可[[Reliability|信度]]的结构化工具。
> - **边界** 内部效度威胁不同于[[External Validity|外部效度]]威胁——前者关注研究**内部**[[Causality|因果推断]]的有效性（"在这个研究中，X 真的导致了 Y 吗？"），后者关注研究发现的**可推广性**（"这个发现能推广到其他情境吗？"）。在 Cook & Campbell 框架中，第一类和[[Type I and Type II Errors|第二类错误]]属于统计结论效度（statistical conclusion validity）而非内部效度，但 Cohen, Manion & Morrison 将其归入内部效度威胁。

---

## 量化研究中的内部效度威胁

Campbell & Stanley (1963)、Bracht & Glass (1968) 和 Lewis-Beck (1993) 建立了经典框架，Creswell & Guetterman (2018) 将其按来源重组为三组共 10 种威胁（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8, Table 8.5]]）。以下整合两个框架，按受试者、实验处理和实验程序三组展开。

### 与受试者相关的威胁

> [!dimension] 受试者威胁（5 种）
> - **历史**（History）
>   实验期间发生的外部事件不当地影响了结果，超出实验处理的影响。应对：让实验组和对照组经历相同的外部事件。
> - **成熟**（Maturation）
>   受试者在实验期间自然成熟或变化，从而影响结果。应对：选择成熟或变化速率相同的受试者（如同龄人）。
> - **回归均值**（Regression to the Mean）
>   选择极端得分的受试者，其得分自然会随时间向均值回归。应对：选择入组特征非极端得分的受试者。
> - **选择**（Selection）
>   受试者因具有某些特征而倾向于产生特定结果。应对：随机选择受试者，使特征在各实验组中概率均等分布。
> - **流失/研究减员**（Mortality/Attrition）
>   受试者因多种原因退出实验，其结果是未知的。应对：招募大样本以应对退出，或比较退出者与继续者的结果特征。
> - **选择-成熟交互**（Selection-maturation interaction）
>   实验组和对照组在成熟速度上不同，这种差异被误判为处理效应——是选择偏差与成熟效应的复合威胁。

> [!example]- 受试者威胁的案例
> **历史**：一学期的数学教学法实验中，学校恰好推行了新的课后辅导政策。即使实验组后测成绩更高，也无法区分是教学法的效果还是课后辅导的效果。两组都经历了新政策时，这一威胁得到控制。
>
> **成熟**：为期一年的阅读[[Intervention Research|干预研究]]中，对照组学生的阅读成绩也在提高，因为他们自然长大了、认知能力在发展。如果不设对照组，这些自然成长会被误判为干预效果。选取同年级学生作为对照组可以控制这一威胁。
>
> **回归均值**：从全年级中选出数学成绩最差的 30 名学生进行补习。即使补习完全无效，他们的成绩也会在第二次测试中自然上升——第一次测试包含了偶然的低分（测量误差），这些偶然因素不会在第二次测试中重复。选择非极端得分的学生入组可以避免这一问题。
>
> **选择**：某实验的实验组由自愿报名的学生组成，对照组由未报名的学生组成。两组在动机水平上可能存在系统性差异，后测差异可能反映的是动机差异而非处理效应。[[Random Assignment|随机分配]]可以消除这种系统性偏差。
>
> **流失**：为期三个月的减肥实验中，体重最重、效果最差的受试者在中期退出。如果只分析坚持到最后的人，实验效果会被高估。预先招募大样本，并在报告时比较退出者与继续者的基线特征，可以评估流失偏差的严重程度。

### 与实验处理相关的威胁

> [!dimension] 实验处理威胁（4 种）
> - **处理扩散/组间交叉污染**（Diffusion of Treatment）
>   对照组和实验组的受试者相互交流，影响两组的结果得分。应对：在实验期间尽可能保持两组分离。
> - **补偿性/怨恨性士气低落**（Compensatory/Resentful Demoralization）
>   只有实验组接受处理时，两组获益不均可能引发不满。应对：向对照组在实验结束后提供处理，或给予不同类型的处理。
> - **补偿性竞争**（Compensatory Rivalry）
>   对照组因未接受处理而感到被低估，从而产生竞争性行为。应对：降低对照组预期或明确说明对照组的价值，创造两组平等感。
> - **工具反应性**（Instrument reactivity, Vulliamy et al., 1990）
>   研究工具本身对参与者产生的效应。例如观察者的在场改变被观察者的行为，问卷中的问题措辞引发受试者的防御性回答。与前述威胁不同，工具反应性关注的是工具本身作为"处理"的一部分对参与者行为的影响。

> [!example]- 处理威胁的案例
> **处理扩散**：同一所学校内，实验班使用新教学法，对照班使用传统教学法。课间休息时实验班的学生把新方法教给了对照班的朋友，导致对照班也部分接触了处理。两组结果因此趋同，处理效应被低估。将实验组和对照组放在不同学校可以解决，但成本更高。
>
> **补偿性怨恨**：学校推行一项新的免费午餐计划，只有实验班学生可以领取。对照班学生知道后感到不公平，在后期测试中消极应答或故意表现差，导致组间差异被人为放大。应对方式是承诺实验结束后给予对照组同等待遇。
>
> **补偿性竞争**：对照组的教师知道自己是"对照组"后，加倍努力教学以证明自己不比实验组差——对照组结果因此被拉高，处理效应被低估。这是 John Henry 效应的一种形式。应对方式是不过度强调"实验 vs 对照"的标签，或给予对照组一个有意义的替代任务，使其感到自己的工作同样重要。

### 与实验程序相关的威胁

> [!dimension] 实验程序威胁（3 种）
> - **测验**（Testing）
>   受试者熟悉结果测量工具，记住前测答案以用于后测。应对：延长前后测时间间隔，或在后测中使用不同于前测的题目。
> - **工具**（Instrumentation）
>   前测和后测之间测量工具发生变化，影响结果得分。应对：前后测使用相同的测量工具。
> - **第一类与[[Type I and Type II Errors|第二类错误]]**（Type I and Type II errors）
>   统计推断中拒绝真[[Null Hypothesis|零假设]]（第一类）或接受假零假设（第二类）的决策错误。两类错误存在内在权衡——降低一类错误的风险必然增加另一类错误的风险。在 Cook & Campbell 框架中属于统计结论效度。

> [!example]- 程序威胁的案例
> **测验**：逻辑推理训练实验中，前后测使用了同一套题目。受试者后测成绩提高可能不是训练的效果，而是做前测时就记住了题目和答案。延长两次测试的时间间隔（如从一周延至两个月），或使用难度相当的平行题本，可以降低这一威胁。
>
> **工具**：写作教学实验中，前测由一位老师评分，后测由另一位评分标准更宽松的老师评分。后测"提高"可能纯粹是评分标准差异导致的，而非写作能力的真实提升。前后测使用相同的评分者和评分标准可以消除这一威胁。

[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|(Cohen et al., 2011, Ch. 10, pp. 164–166)]]

---

## 质性研究中的内部效度威胁

Onwuegbuzie & Leech (2006b: 235–7) 将质性[[Internal Validity|内部效度]]的威胁系统化为十二种类型，这些威胁从不同于[[Quantitative Research|量化研究]]的维度挑战[[Qualitative Research|质性研究]]解释的可信性：

> [!challenges] 十二种质性内部效度威胁
> - **1. 反讽合法化**（Ironic legitimation） 研究能否识别和处理同一情境的多重、甚至同时矛盾的现实和解释？当不同参与者对同一事件有截然不同的叙述时，研究是否只是选择了最方便的版本？
> - **2. 悖论合法化**（Paralogical legitimation） 研究能否捕捉和处理效度主张中的悖论？例如一位教师同时声称"我完全按照课程大纲教学"和"我经常根据学生需要灵活调整"，这种表面矛盾的陈述可能恰恰反映了教育实践的复杂性。
> - **3. 根茎合法化**（Rhizomatic legitimation） 当研究者绘制数据地图（mapping）而非描述数据时，丢失了多少信息？将丰富的生活经验压缩为概念节点和关系线时不可避免有损失，但研究者是否意识到了这种损失并做了弥补？
> - **4. 过度合法化**（Voluptuous legitimation） 对数据的解释是否超出了研究者从数据中支持该解释的能力？例如从三个教师的访谈中推断出全国性结论——数据不足以承载这个主张。
> - **5. [[Descriptive Validity|描述效度]]**（Descriptive validity） 研究者所给描述的准确性——事实层面的[[Reliability|可靠性]]。
> - **6. 观察偏差**（Observational bias） 对研究中词语、观察或行为的不充分抽样——收集的数据太少或太窄，不足以支撑结论。
> - **7. 研究者偏差**（Researcher bias） 研究者的偏见、假设或价值观影响数据的收集和解释。
> - **8. 反应性**（Reactivity） 研究在多大程度上改变了正在研究的情境或参与者——例如[[Hawthorne Effect|霍桑效应]]和新奇效应（novelty effect）。
> - **9. 确认偏差**（Confirmation bias） 研究倾向于确认已有发现或假设——寻找支持已有信念的证据而忽略反证。
> - **10. 虚假确认**（Illusory confirmation） 在实际不存在关系时倾向于发现关系——过度解释数据中的偶然模式。
> - **11. 因果错误**（Causal error） 在不存在[[Causality|因果关系]]或未提供因果证据时推断因果关系。
> - **12. [[Effect Size|效应量]]忽略**（Effect size） 在量化效应量能为质性分析带来精确性和意义时，未能将其纳入考虑。

[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|(Cohen et al., 2011, Ch. 10, pp. 167–168)]]

---

## 两种范式处理威胁的不同逻辑

> [!contrast-table] 量化与[[Qualitative Research|质性研究]]处理[[Internal Validity|内部效度]]威胁的不同逻辑
> | 维度 | [[Quantitative Research\|量化研究]] | 质性研究 |
> |---|---|---|
> | **核心策略** | 通过实验设计和统计控制**排除**混淆因素 | 通过方法论反思和多元验证**纳入并管理**多重解释 |
> | **对时间和变化的态度** | 历史、成熟等时间效应被视为**需要控制的威胁** | [[Ethnography\|民族志研究]]**将变化纳入研究设计**，允许现象随时间演变（p.168） |
> | **观察者效应** | 通过双盲、标准化程序来**消除**研究者影响 | 通过长期田野参与使观察者在场变得**被视为理所当然**来减少影响 |
> | **对异常案例的态度** | 统计上排除异常值（outliers）以提高模型拟合度 | 通过[[Negative Case Analysis\|负面案例分析]]保留并深入理解异常案例，以修正理论 |
> | **效度标准** | 内部效度——[[Causality\|因果推断]]的可信性 | 可信性（credibility）——解释对参与者而言是否可信 |

> [!note] 一个关键区别
> [[Positivism|实证主义]]研究将历史和成熟视为对效度的威胁，而民族志研究简单地**假设这些会发生**——民族志研究允许随时间变化，它将**变化纳入研究设计**。民族志研究还通过让观察者既广泛采样又在情境中停留足够长时间使其在场被视为理所当然来减少观察者效应（p.168）。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|(Cohen et al., 2011, Ch. 10)]]
