---
title: Multitrait-Multimethod Matrix
aliases:
  - 多特质-多方法矩阵
  - 多特质多方法矩阵
  - 多特质多方法
  - MTMM
  - Multitrait-Multimethod
  - MTMM Matrix
summary: "Campbell & Fiske (1959) 提出的经典测量效度检验矩阵，通过交叉评估多种特质与多种独立方法的相关结构，系统检验构念效度中的收敛效度与判别效度，并拓展至循证教育清算中心跨机构评级一致性的元评估。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 7
method_related_level: 0
method_related_stars: ""
method_related_color: "#dcfce7"
tags:
  - mtmm
  - construct-validity
  - convergent-validity
  - discriminant-validity
  - measurement
  - quantitative-methods
  - psychometrics
related_concepts:
  - "[[Construct Validity]]"
related_theories:
  - "[[Campbellian Validity Framework]]"
related_methods:
  - "[[Confirmatory Factor Analysis]]"
  - "[[Pearson Product-Moment Correlation]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10]]"
  - "[[Argument_Wadhwa_2024_RER]]"
  - "[[Argument_Hitchcock_2015_JBE]]"
confidence: high
status: active
created: 2026-08-21
updated: 2026-08-21
---

# Multitrait-Multimethod Matrix

---

## 定义

> [!def] 方法定义
> **多特质-多方法矩阵（Multitrait-Multimethod Matrix, MTMM）** 是由 Donald T. Campbell 与 Donald W. Fiske 于 1959 年创立的心理测量与构念效度检验方法，指通过同时测量至少两种不同的目标特质（Traits）并分别采用至少两种相互独立的方法（Methods），构建出一套包含全部成对相关系数的对称矩阵，以系统分离特质方差、方法方差与随机误差方差，从而全面确证测量工具的收敛效度（Convergent Validity）与判别效度（Discriminant Validity）([[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|Cohen et al., 2011, Ch. 10, pp. 176–178]]; [[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, p. 4]])。

> [!method-scope] 方法范围
> - **研究对象** 心理测量量表、行为观察系统、多源评价工具（如教师评定 vs 学生自评 vs 档案记录），以及宏观证据清算机构（Clearinghouses）对干预项目的等级评定数据。
> - **问题类型** 测量学工具的构念效度验证、方法效应（Method Effects）诊断、跨评价者一致性检验及政策评价体系的元评估（Meta-Evaluation）。
> - **分析单位** 受试者个体得分、题目维度指标、或被多个独立机构共同评估的具名干预项目。
> - **输出形式** 相关系数矩阵、效度对角线判定比值、结构方程模型（CFA）特质与方法因子载荷、以及收敛/对立冲突率统计。

> [!citation-card]- 关键定义
> 构念效度不能依赖单一方法证明。多特质-多方法矩阵要求：不同方法测量同一特质时相关必须显著且高（收敛效度）；相似方法测量不同特质、或不同方法测量不同特质时相关必须显著低于效度对角线（判别效度）。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|(Cohen et al., 2011, Ch. 10, pp. 176–178)]]
>
> *Convergent validation is confirmed by the degree of agreement between two attempts to measure the same trait through maximally different methods. Discriminant validation is confirmed when correlations between different traits measured by the same or different methods are significantly lower than validity correlations. (Campbell & Fiske, 1959)*

---

## 方法定位

> [!method-position] 认识论与方法定位
> - **知识观** 秉持后实证主义（Postpositivism）与证伪主义；主张任何单一测量方法都不可避免地带有该方法特有的系统性偏差（方法方差），客观构念的真实性只能通过不同独立方法的交叉收敛来逼近。
> - **研究者角色** 要求研究者在测量设计阶段主动引入不同性质的独立测量途径（如自陈量表 + 行为客观测验 + 专家盲评），并预先设立排他性的竞争特质。
> - **有效性标准** 效度对角线显著大于零（收敛效度达标）；效度对角线系数高于异特质-同方法三角区与异特质-异方法三角区（判别效度达标且排除方法效应）。
> - **不声称回答的问题** MTMM 检验的是测量与构念之间的对应关系，不能直接推断变量之间的因果效应大小。

> [!method-stack] 方法层级
> - **研究设计** 多特质多方法交叉测量设计、多评价者重叠审查设计。
> - **数据收集** 问卷调查、标准化测验、课堂观察、档案审查、清算中心数据库元数据爬取。
> - **分析方法** Pearson 积差相关矩阵分析、验证性因子分析（CFA-MTMM 模型）、相关系数差异显著性检验。
> - **辅助技术** 矩阵热力图可视化、结构方程建模（SEM）、跨平台配对卡方检验。

---

## 研究程序

> [!proc] MTMM 分析标准六步法
> 1. **选取目标特质与对照特质** 确定至少两个具有清晰理论界限的特质（例如 $T_1$ 学习动机，$T_2$ 焦虑水平）。
> 2. **选取相互独立的方法** 确定至少两种测量介质或独立评价主体（例如 $M_1$ 学生自陈量表，$M_2$ 教师观察量规）。
> 3. **采集全交叉测量数据** 对同一批样本或对象同时实施全部特质-方法组合测量（$T_1M_1, T_2M_1, T_1M_2, T_2M_2$）。
> 4. **构建 MTMM 相关矩阵** 计算全部成对相关系数，并在对角线填入各工具的单特质-同方法信度系数（Reliability Diagonal）。
> 5. **执行四大经典效度判别准则** 对比效度对角线（Monotrait-Heteromethod）与各异特质三角块的相关大小。
> 6. **构建 CFA 结构方程验证** 建立特质因子（Trait Factors）与方法因子（Method Factors）正交模型，检验参数显著性。

---

### 量化方法模块

> [!framework-table] 经典 MTMM 矩阵结构与模块划分（2 Traits × 2 Methods 示范）
> | 测量组合 | $M_1: T_1$ | $M_1: T_2$ | $M_2: T_1$ | $M_2: T_2$ | 矩阵区块性质与解读 |
> |:---|:---:|:---:|:---:|:---:|:---|
> | **方法 1: 特质 1 ($M_1T_1$)** | **($r_{11}$)** | | | | **单特质-同方法对角线 (Monotrait-Monomethod)**<br>括号内为信度系数（Reliability），代表测量稳定上限。 |
> | **方法 1: 特质 2 ($M_1T_2$)** | $r_{21}$ | **($r_{22}$)** | | | **异特质-同方法三角区 (Heterotrait-Monomethod)**<br>反映相同方法引发的共享方法方差（Method Variance）。 |
> | **方法 2: 特质 1 ($M_2T_1$)** | **$\mathbf{r_{31}^*}$** | $r_{32}$ | **($r_{33}$)** | | **单特质-异方法对角线 (Monotrait-Heteromethod)**<br>即**效度对角线（Validity Diagonal）**，检验**收敛效度**。 |
> | **方法 2: 特质 2 ($M_2T_2$)** | $r_{41}$ | **$\mathbf{r_{42}^*}$** | $r_{43}$ | **($r_{44}$)** | **异特质-异方法三角区 (Heterotrait-Heteromethod)**<br>不同方法测量不同特质，反映最纯净的特质间客观相关。 |

> [!formula-step] 公式步骤　Campbell & Fiske 四大效度判别准则
>
> 1. **准则一：收敛效度检验（Convergent Validity）**
>    $$\mathbf{r_{validity}^*} = r(T_iM_j, T_iM_k) > 0 \quad (\text{显著不为 } 0 \text{ 且足够大})$$
>    - **含义** 同一特质通过不同方法测量时的相关系数（效度对角线）必须达到统计显著且具备实质量级。
>
> 2. **准则二：判别效度准则 A（高于异特质-异方法）**
>    $$\mathbf{r(T_iM_j, T_iM_k)} > r(T_iM_j, T_mM_k) \quad (\text{其中 } i \neq m)$$
>    - **含义** 效度对角线上的相关必须高于同一行和列中由不同方法测量的不同特质相关。
>
> 3. **准则三：判别效度准则 B（高于异特质-同方法）**
>    $$\mathbf{r(T_iM_j, T_iM_k)} > r(T_iM_j, T_mM_j) \quad (\text{其中 } i \neq m)$$
>    - **含义** 效度对角线上的相关必须高于相同方法测量不同特质时的相关，确保特质方差压倒共享方法效应。
>
> 4. **准则四：特质相关模式一致性**
>    - **含义** 在所有单方法块和跨方法块中，不同特质之间的相关模式应保持相似的相对排序。

> [!logic-map]- MTMM 方差分解与效度判定逻辑
> ```mermaid
> flowchart TD
>     A["总测量方差<br>(Total Variance)"] --> B["特质方差<br>(Trait Variance)"]
>     A --> C["方法方差<br>(Method Variance)"]
>     A --> D["随机测量误差<br>(Error Variance)"]
>     B --> E["效度对角线相关高<br>(收敛效度达标)"]
>     C --> F{"方法效应诊断"}
>     F -->|特质方差 > 方法方差| G["判别效度达标<br>(真实特质主导)"]
>     F -->|方法方差 > 特质方差| H["方法效应污染<br>(人工假象风险)"]
> ```

> [!software-impl] 现代 CFA-MTMM 模型软件实现（R 语言 `lavaan`）
> ```r
> # 加载 lavaan 包构建 Correlated Traits-Correlated Methods (CTCM) 模型
> library(lavaan)
>
> mtmm_model <- '
>   # 特质因子 (Traits)
>   Trait1 =~ T1M1 + T1M2 + T1M3
>   Trait2 =~ T2M1 + T2M2 + T2M3
>   
>   # 方法因子 (Methods - 彼此正交或相关)
>   Method1 =~ T1M1 + T2M1
>   Method2 =~ T1M2 + T2M2
>   Method3 =~ T1M3 + T2M3
>   
>   # 特质与方法之间设定为正交 (Covariance = 0)
>   Trait1 ~~ 0*Method1 + 0*Method2 + 0*Method3
>   Trait2 ~~ 0*Method1 + 0*Method2 + 0*Method3
> '
>
> fit <- cfa(mtmm_model, data = my_data, std.lv = TRUE)
> summary(fit, fit.measures = TRUE, standardized = TRUE)
> ```

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 心理与教育量表效度验证、多主体评价系统（学生/教师/家长）、教育评估工具跨平台一致性检验、以及循证清算中心跨机构评级收敛性元评估([[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|Cohen et al., 2011, p. 176]]; [[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, p. 4]])。
> - **谨慎使用** 当测量方法之间并非真正独立（例如两种方法均为纸笔自陈问卷）时，方法方差会严重膨胀并伪装成特质相关。
> - **不适合使用** 仅包含单一特质或单一方法的简单测验；探索性研究初期缺乏清晰理论构念界定时。

---

## 局限性

> [!method-limits] 方法局限
> - **对角线启发式判别的主观性** 传统 Campbell-Fiske 相关比较缺乏严格的概率推断检验，容易在临界值处产生裁量分歧（已被现代 CFA 结构方程建模部分弥补）。
> - **方法独立性假设难以满足** 在社会科学现场中，很难找到在测量介质、刺激形态与施测情境上完全相互正交的“纯粹独立方法”。
> - **CFA 模型不收敛与非正定解（Heywood Cases）** 在复杂 MTMM 结构方程中，由于特征值过小或方法因子共线性，经常出现负误差方差或模型无法迭代收敛。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[Campbellian Validity Framework]] | 理论 | 坎贝尔效度体系为 MTMM 提供了构念效度与排除替代解释的元理论基础。 |
> | [[Construct Validity]] | 目标构念 | MTMM 专门用于实证确证与量化构念效度中的收敛与判别维度。 |
> | [[Confirmatory Factor Analysis]] | 替代与升级方法 | CFA-MTMM 提供了检验特质与方法因子载荷的标准参数化统计工具。 |
> | [[Pearson Product-Moment Correlation]] | 基础技术 | MTMM 矩阵的底层基础单元为变量间的成对积差相关系数。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wadhwa_2024_RER|Wadhwa, Zheng, & Cook (2024)]] — 创新性将 MTMM 矩阵扩展至宏观教育证据清算体系，把 10 个独立清算中心视为不同“评价方法（Methods）”，实证检验 1,359 个项目在跨机构评级上的收敛效度与判别效度。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|Cohen, Manion, & Morrison (2011)]] — 系统阐释 MTMM 矩阵在心理与教育测量构念效度检验中的经典设计、区块划分与判别准则。
> - [[Argument_Hitchcock_2015_JBE|Hitchcock et al. (2015)]] — 结合 Campbellian 效度传统，讨论跨设计与跨方法效度评估的一致性基准。
