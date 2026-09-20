---
title: Interaction Effect
aliases:
  - 交互效应
  - 交互作用
  - 调节效应
  - interaction effect
  - interaction effects
  - moderation effect
summary: "一个自变量对因变量的因果效应依赖于另一个自变量或调节变量水平的非可加性现象，是因子设计与条件性因果推断的核心，揭示了教学干预在不同学习者特征与情境中的异质性机制"
type: concept
domain: "research-methodology"
concept_field: "research-methodology"
related_count: 14
related_level: 1
related_stars: "⭐"
related_color: "#e5e7eb"
tags:
  - subject/research-methodology
  - experiment
  - causal-inference
  - quantitative-methods
related_concepts:
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Variable]]"
  - "[[Causality]]"
  - "[[Heterogeneity]]"
  - "[[Learning Gain]]"
  - "[[Executive Function]]"
  - "[[Self-Efficacy]]"
  - "[[Scaffolding]]"
  - "[[Productive Failure]]"
related_methods:
  - "[[Factorial Design]]"
  - "[[Analysis of Variance]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Meta-analysis]]"
  - "[[Sample Size Determination]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
  - "[[Argument_DeJong_2023_ERR]]"
status: active
created: 2026-07-12
updated: 2026-09-21
---

# Interaction Effect

## 定义

> [!def] 核心定义
> 交互效应（Interaction Effect）指在多因子实验或观测研究中，一个[[Independent Variable|自变量]]（或干预措施）对[[Dependent Variable|因变量]]（或结果指标）的效应**依赖于**另一个自[[Variable|变量]]或调节变量的水平——即两个或多个变量对结果的联合影响并非单项独立效应的线性简单相加，而是表现出条件依赖性与相互调节的非可加性关系（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 323–324]]）。在统计建模中，交互效应通过乘积项（Product Term）捕获；在[[Causality|因果推断]]中，交互效应表征了因果[[Heterogeneity|异质性]]（Causal [[Heterogeneity]]）。

交互效应与**主效应（Main Effect）**相对：主效应指某个自变量跨越其他所有条件后的独立平均效应；而交互效应揭示了一个自变量的因果作用强度或方向随情境与对象特征而发生转移。在现代学习科学与[[Evidence-Based Education|循证教育]]研究中，探究的核心议题已从单一孤立地提问“某种教学法是否普遍有效”（寻求单一主效应），转向探究“该教学法在何种条件、经由何种序列、针对具备何种认知特征的学生最为有效”（检验高阶交互效应）（[[Argument_DeJong_2023_ERR|De Jong et al., 2023, pp. 7–9]]）。

> [!concept-lens] 交互效应在因果推断与教学设计中的定位
> - **含义** 交互效应构建了“X 对 Y 的影响取决于 Z（$X \to Y \mid Z$）”的条件因果结构，反映系统内部多重因素协同作用的非线性本质。
> - **用途** 识别干预的适用边界与受益人群，解释实验结果的分歧与异质性，指导自适应支架系统与分层教学序列的设计。
> - **边界** 交互效应不等于主效应的缺失（二者在方差分解中完全正交）；交互项显著时直接解释主效应极易产生严重误导；交互效应亦区别于中介效应（中介阐明因果传导链条 $X \to M \to Y$，交互阐明因果边界条件 $X \times Z \to Y$）。

---

## 核心机制与统计表征

> [!feature] 交互效应的核心特征与表现形式
> - **条件依赖性与非可加性** 单一干预的有效性并非绝对常数。在线性模型中，$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 (X_1 X_2) + \epsilon$，交互项系数 $\beta_3 \neq 0$ 即证实了联合效应偏离加和基准。
> - **几何图示特征** 
>   - *平行线*（无交互作用）：不同调节水平下的回归线保持平行，表明处理效应在各群体间保持恒定。
>   - *相交线/交叉交互（Crossover Interaction）*：两条趋势线在观察范围内交叉，表明干预在一个群体中产生积极增益，但在另一群体中产生消极阻碍（质性反转）。
>   - *发散/收敛线（Ordinal Interaction）*：斜率方向一致但陡峭程度不同，表明干预在某一群体中效果被显著放大或稀释（量级差异）。
> - **统计检力瓶颈** 检验交互项（乘积项）所需的统计功效（Statistical Power）显著高于主效应检验；在小样本或测量误差较大的教育现场实验中，交互效应往往难以达到统计显著，需依托大样本[[Randomised Controlled Trials|随机对照试验]]（[[Randomised Controlled Trials|RCT]]）或[[Meta-analysis|元分析]]（[[Meta-analysis|Meta-analysis]]）中的亚组调节分析（Moderation Analysis）。

---

## 概念辨析

> [!contrast-table] 交互效应、主效应与中介效应辨析
> | 维度 | 主效应（Main Effect） | 交互效应（Interaction Effect / 调节） | 中介效应（Mediation Effect） |
> |---|---|---|---|
> | **核心问题** | [[Independent Variable\|自变量]] X 是否独立影响结果 Y？ | X 对 Y 的影响在何种条件 Z 下更强或更弱？ | X 是通过何种中间机制 M 导致了 Y？ |
> | **模型结构** | $X \to Y$ | $X \times Z \to Y$（Z 调节 X 与 Y 的关系） | $X \to M \to Y$（M 充当因果中介桥梁） |
> | **因果角色** | 平均因果效应（Averaged Effect） | 条件因果效应与边界条件（Boundary Conditions） | 内部传导机制与中间[[Variable\|变量]]（Causal Mechanism） |
> | **教育解释示例** | [[Inquiry-Based Learning\|指导式探究]]平均提升科学学习成绩 | 探究教学对高[[Executive Function\|执行功能]]学生的促进显著高于低执行功能学生 | 探究教学通过增强[[Metacognition\|元认知监控]]从而提高[[Problem Solving\|问题解决能力]] |

---

## 教育科学中的交互机制与实证证据

在现代科学教育与认知负荷研究中，单一孤立地评判“[[Inquiry-Based Learning|探究式学习]]”与“[[Direct Instruction|直接讲授]]”的优劣已被证实不具有实质意义，关键在于解构教学指导与学生个体认知特征、教学时序之间的深层交互效应（[[Argument_DeJong_2023_ERR|De Jong et al., 2023]]）：

### 1. 学生认知特征 × 教学指导结构的交互

> [!effect-table] 学习者个体特征与教学干预交互实证表
> | 交互维度 | 调节[[Variable\|变量]]（学生特征） | 比较条件（干预变量） | [[Dependent Variable\|结果变量]] | 交互实证发现 | 理论解释 | 证据来源 |
> |---|---|---|---|---|---|---|
> | **[[Executive Function\|执行功能]] × 探究结构** | 抑制控制（Inhibitory Control） | 开放式探究模拟 vs 结构化支架模拟 | 概念获得与迁移测验 | 高抑制控制学生在探究迁移题上表现更优；低抑制控制学生在无支架时受干扰信息严重拖累，在结构化支架下劣势消除 | 高执行功能个体能自主抑制无关参数干扰；低抑制控制学生必须依托外源支架补偿认知控制不足 | Kwon & Lawson (2000); Homer & Plass (2014) |
> | **[[Self-Efficacy\|自我效能感]] × 引导机制** | 初始科学自我效能感 | 纯自主发现 vs 教师/系统支架引导 | 探究数据搜集行为与成就 | 初始阶段高效能感学生搜集更多数据；但随着数字化支架介入，效能感对探究行为的调节作用减弱，支架抹平了低效能感学生的行为差距 | 自适应支架提供了即时[[Scaffolding\|脚手架]]支持，降低任务门槛，重构了低效能感学生的行动信念 | Ketelhut (2007); Liu & Wang (2022) |
> | **先验知识 × 指导程度（专业逆转）** | 领域先验知识水平 | 显性直接指导 vs 开放探索 | 学习效率与认知负荷 | 低先验知识学生在直接指导下显著获益，在开放探索中负荷超载；高先验知识学生在重复显性指导下产生厌烦与负荷冗余 | 教学设计的专业逆转效应（Expertise Reversal Effect）；先验图式充当了内部支架，与外在显性指导产生冗余交互 | Sweller et al. (2003); De Jong et al. (2023) |

### 2. 教学时序 × 认知目标类型的交互

教学干预与时序编排的交互作用是近年来学习科学最重要的突破之一。以[[Productive Failure|生产性失败]]（Productive Failure）与反转序列为代表的研究确立了教学时序与认知目标深度的交叉交互（[[Argument_DeJong_2023_ERR|De Jong et al., 2023, pp. 8–9]]）：
- **记忆提取 vs 深层迁移的交互** 若教学目标仅为机械事实性识记（如化学元素符号）或单一步骤运算，直接讲授展现出高效率的主效应；若教学目标为深层概念理解（Conceptual Understanding）与灵活迁移（Transfer），“先探究后讲授”（Inquiry before Direct Instruction）与目标类型产生显著正向交互。
- **即时测试 vs 延迟保持的交互（必要难度）** 在即时课[[Pre-test and Post-test|后测]]验中，直接讲授由于减少了学习过程中的尝试错误，往往表现出更高的即时正确率；但在数周后的延迟测验（Delayed Assessment）中，经历先期探究磨砺与错误辨析的学生表现出更具韧性的长期保持，直接讲授的优势随时间衰减，显现出时序与时间跨度的显著交互作用（Vitale, McBride, & Linn, 2016; De Jong et al., 2023, p. 9）。

---

## 经典应用案例

> [!case] 性别 × 年龄对数学学习动机的交互效应
> 以性别和年龄为两个[[Independent Variable|自变量]]研究数学学习动机时（Cohen et al., 2011, Ch16, Figure 16.3），男女之间的动机差异并非恒定不变，而是随年龄增长发生显著分化——在低年龄段男女动机基线差异极小，进入青春期后差异急剧扩大。如果研究者仅报告性别的主效应，会得出“男生与女生在数学动机上存在系统性差异”的笼统论断；但引入交互效应后则揭示出该结论仅在特定发展年龄段成立，避免了简单化概括（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 324]]）。

> [!case] 数字化仿真微世界中交互探索与即时解释的交互
> 在物理电路探究模拟中，单纯让学生操作虚拟仪表（单纯交互）或单纯阅读原理解释（单纯讲授）的效果均有限。Adams et al. 与 Wieman et al. 的实验揭示出操作性交互与即时认知反馈的强交互作用：当直接解释被精准嵌入在学生操纵仿真参数产生疑问的瞬间时，学生的定性概念掌握产生了显著飞跃（De Jong et al., 2023, pp. 8–9）。这表明交互并非外在界面的机械点击，而是学生内部认知结构与外部支架动态响应的深度耦合。

---

## 相关条目网络

> [!entry-map]
> 
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Factorial Design]] | 方法 | 因子设计是系统析离并检验主效应与交互效应的标准实验[[Paradigm\|范式]]。 |
> | [[Analysis of Variance]] | 方法 | 方差分析中的双因素或多因素模型提供了检验交互项[[Statistical Significance\|统计显著性]]的基本工具。 |
> | [[Randomised Controlled Trials]] | 方法 | 大样本[[Multi-Arm Trial\|多臂随机对照试验]]是检验教育干预[[Heterogeneity\|异质性]]与条件因果效应的金标准。 |
> | [[Causality]] | 概念 | 交互效应刻画了因果关系的条件依赖性与情境敏感性。 |
> | [[Executive Function]] | 概念 | 执行功能（尤其是抑制控制）是调节[[Inquiry-Based Learning\|探究学习]]成效的关键学习者特征。 |
> | [[Self-Efficacy]] | 概念 | 学生初始效能感与支架设计存在动态交互，优质探究环境能抹平效能鸿沟。 |
> | [[Productive Failure]] | 概念 | 生产性失败通过“先探索后讲授”的时序交互最大化概念理解与深度迁移。 |
> | [[Argument_DeJong_2023_ERR\|De Jong et al. (2023)]] | 论证 | 权威综述提出破除两派二元对立，强调基于学习者特征与时序交互整合教学。 |
