---
title: Meta-meta-analysis
aliases:
  - 元-元分析
  - 元元分析
  - mega-analysis
  - meta-synthesis
  - 元综合
  - super-analysis
  - super-synthesis
  - Second-Order Meta-Analysis
  - 二阶元分析
  - 二级元分析
  - SOMA
summary: "在更高层级汇总多个已发表元分析结果的统计综合方法，运用多水平层级效应与稳健方差估计处理大型证据库并探索全领域异质性来源"
type: method
method_type: quantitative
tags:
  - method/quantitative
  - statistics/meta-analysis
  - theme/meta-meta-analysis
  - field/research-methodology
confidence: high
status: draft
created: 2026-05-03
updated: 2026-08-24
---

# Meta-meta-analysis

---

## 定义

> [!def] 方法定义
> [[Meta-meta-analysis|元-元分析]]（Meta-meta-analysis，在现代统计学中亦称二阶元分析 Second-Order Meta-Analysis, SOMA，早期文献称 Mega-analysis 或 Meta-synthesis）指在更高统计层级上对多个已发表[[Meta-analysis|元分析]]（Meta-analysis）结果进行系统检索、方法学质控与定量合成的方法体系。与一阶元分析综合原始主要研究不同，二阶元分析以一阶元分析提取的汇总[[Effect Size|效应量]]（及其背后的抽样误差结构）为分析单位，旨在估计宏观领域效应量基准、比较不同理论构念与干预维度的相对有效性，并识别全领域效应异质性的深层来源。[[Argument_Terhart_2011_JCS|(Terhart, 2011, p. 436)]]; [[Argument_Runco_2026_CRJ|(Runco et al., 2026, p. 2)]]

> [!method-scope] 方法范围
> - **研究对象** 已发表或灰色文献中关于特定主题的系统评价与一阶元分析汇总效应量矩阵。
> - **问题类型** 评估跨领域宏观效应量强度、检验不同理论构念或干预模式的相对差异、探索出版偏倚与方法学质量的调节效应。
> - **分析单位** 纳入的一阶元分析或其报告的独立一阶效应量集群（Clusters）。
> - **输出形式** 经小研究效应偏倚校正后的二阶总体效应量点估计值（$r$ 或 $g$）、95% [[Confidence Interval|置信区间]]（CI）、95% 预测区间（PI）及多水平二阶元回归调节系数。

> [!citation-card]- 关键定义
> 二阶元分析在大样本水平上整合多重一阶元分析，采用系统评价质量评估工具与多水平稳健方差估计，能够克服单一研究局限，提供高度稳健且具备可推广性的效应量基准。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, pp. 2–5)]]
>
> *Second-order meta-analyses synthesize the findings of previous meta-analyses to provide a higher-order summary of evidence... controlling for dependencies through cluster-robust variance estimation.*

---

## 术语演变与方法定位

> [!ref-table]- 术语演变对照表
> | 术语 | 提出者 / 使用者 | 含义侧重与历史定位 |
> |---|---|---|
> | **Meta-meta-analysis** | Kazrin et al. (1979) | 强调对元分析进行再分析与统计聚合。 |
> | **Mega-analysis** | Smith (1982) | 强调在样本与文献规模上的超级扩展。 |
> | **Super-analysis** | Dillon (1982) | 强调统计抽象层级上的超越。 |
> | **Super-synthesis** | Sipe & Curlette (1996) | 强调跨元分析的系统综合过程。 |
> | **Meta-synthesis** | Sipe & Curlette (1997); Higgins (2016) | 质性与量化综合的通用统称。 |
> | **Second-Order Meta-Analysis (SOMA)** | Schmidt & Oh (2013); Runco et al. (2026) | 强调估计一阶抽样误差并采用多水平稳健方差模型进行精确校正的现代统计学标准术语。 |

> [!concept-lens] Higgins (2016) 的两种用法区分
> [[Argument_Higgins_2016_RE|Higgins (2016, p. 41)]] 区分了二阶综合的两种截然不同的研究目的：
> 1. **方法学过程研究** 将元分析作为分析单位来研究元分析过程本身的统计特征、发表偏倚与报告质量（如 Ioannidis & Trikalinos, 2007; Lipsey & Wilson, 1993）；
> 2. **实质性主题综合** 试图将不同元分析合并为关于更广泛教育或心理主题的单一信息结论（如 Hattie, 1992; Marzano, 1998; Runco et al., 2026）。后者必须解决深刻的构念可比性与异质性挑战。

> [!contrast-table] 一阶元分析 vs 传统元综合 vs 现代多水平二阶元分析
> | 比较维度 | 一阶元分析（Meta-analysis） | 传统元综合（如早版 Hattie） | 现代多水平二阶元分析（Runco et al., 2026） |
> |---|---|---|---|
> | **分析单位** | 原始实证研究（Primary Studies） | 已发表一阶元分析的汇总 $d$ | 一阶元分析汇总效应量及其多水平依赖集群 |
> | **质量准入** | 原始研究设计筛选 | 粗放纳入、声称不关心质量 | 严格基于 AMSTAR 12 项准则设定质量门槛（$\ge 0.75$） |
> | **统计模型** | 单级固定效应 / 随机效应模型 | 伪固定效应模型、简单未加权平均 | 相关与层级效应工作模型（CHE）+ 稳健方差估计（RVE） |
> | **偏倚控制** | 漏斗图、经典艾格回归 | 无偏倚检验与校正 | 多水平改进艾格回归（Multilevel Egger's Test）截距校正 |
> | **核心目的** | 检验具体干预或相关关系的平均效应 | 建立宏观排名联盟表（League Table） | 估计宏观效应基准、分解全领域异质性、检验理论调节模型 |

---

## 历史演变与范式演进

> [!phase] 二阶元分析的四个发展阶段
>
> - **早期探索与教育生产力模型检验（1980s）**
>
>   Glass 提出元分析 10 年后，Fraser, Walberg & Hattie（1987）首次综合了 226 项元分析以检验 Walberg 的教育生产力模型，涵盖数千项原始研究，识别学生资质、教学与环境三类影响变量，开创了跨元分析大规模统计汇总的先河。[[Argument_Higgins_2016_RE|(Higgins, 2016, pp. 41–42)]]
>
> - **大一统通用连续体与气压计排名（1990s–2000s）**
>
>   Hattie（1992）综合 Fraser et al. 中的 134 项元分析（涵盖 22,155 个效应量、7,827 项研究和 500–1500 万学生），建立标准差单位的通用连续体（Universal Continuum），平均效应量为 $d = 0.40$（SD 0.13），强化（1.13）、反馈（0.65）最高，个别化教学（0.14）最低。Hattie（2008）在《可见的学习》中扩展至 800 多项元分析（涵盖 52,649 项研究、8300 万学生与 146,626 个效应量），提出 $d = 0.40$ 的影响气压计关节点并生成 138 项干预排名。[[Argument_Terhart_2011_JCS|(Terhart, 2011, pp. 427–428)]]
>
> - **理论驱动的构念精细化分类（1998）**
>
>   Marzano（1998）综合 100 多项元分析（涵盖 4000 多个实验-控制组比较），系统批评了将不同干预成分打包为粗放品牌名（Brand-name）聚合的做法。例如 Athappilly et al. (1983) 现代数学元分析中，操作教具为 $d = 0.51$、直接教学为 $d = 0.35$、探究方法为 $d = 0.04$；将其粗暴平均为单一品牌名会掩盖核心有效成分。Marzano 按认知、元认知、自我系统等四层学习机制细化分类，推动元综合走向机制解释。[[Argument_Higgins_2016_RE|(Higgins, 2016, pp. 42–43)]]
>
> - **现代多水平稳健统计推断模型（2013–至今）**
>
>   Sipe & Curlette（1997）严格筛选 103 项元分析并验证重叠率低于 10%；Schmidt & Oh（2013）提出二阶抽样误差估计理论；Runco et al.（2026）在创造力研究中确立了由 PRISMA 检索、AMSTAR 方法学评估、效应量正态化转换、CHE 多水平工作模型与 RVE 三明治估计量组成的现代二阶元分析规范范式。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, pp. 2–6)]]

---

## 经典二阶综合操作案例：Hattie 的六大领域与影响气压计

> [!ref-table]- Hattie (2009) 六大影响因素领域与气压计分区
> | 领域分组 | 涵盖维度与特征 | 一阶元分析数量 | 平均效应量（Cohen's $d$） |
> |---|---|---|---|
> | **教师（Teacher）** | 教师期望、师生关系、清晰度、微格教学 | 约 36 项元分析 | **$d = 0.49$** |
> | **课程（Curricula）** | 阅读干预、数学方案、整合课程、户外项目 | 约 147 项元分析 | **$d = 0.45$** |
> | **教学方法（Teaching）** | 反馈、直接教学、合作学习、元认知策略 | 约 332 项元分析 | **$d = 0.42$** |
> | **学生（Student）** | 先前成就、动机倾向、自我概念、认知能力 | 约 141 项元分析 | **$d = 0.40$** |
> | **家庭（Home）** | 社会经济地位、家庭环境、父母参与 | 约 33 项元分析 | **$d = 0.31$** |
> | **学校（School）** | 班级规模、校舍设施、分轨制、学校领导 | 约 127 项元分析 | **$d = 0.23$** |

> [!tip] 影响气压计的四个判定区间
> 1. **负面效应区（$d < 0$）** 对学业产生阻碍或倒退（如留级 $d = -0.16$、暑期滑坡）；
> 2. **发展效应区（$0.0 \le d \le 0.15$）** 学生不接受干预仅随生理成熟与自然生长产生的基线进步；
> 3. **教师效应区（$0.15 < d \le 0.40$）** 普通教师常规教学能够达到的平均年度进步幅度；
> 4. **期望效应区（$d > 0.40$）** 超越常规教学效果的卓越干预门槛（即 Hattie 设定的“关节点” Hinge Point）。

---

## 现代二阶元分析研究程序

> [!proc] 现代二阶元分析六步标准操作规程
> 1. **多数据库系统检索与灰色文献扩展** 检索主流学术数据库与博硕士论文库，遵循 PRISMA 声明进行四阶段筛选，严格排除缺乏定量合并矩阵的质性综述与无关系效应量的坐标元分析。
> 2. **AMSTAR 12 项方法学质量评估** 采用改编的 AMSTAR 准则进行双人独立编码（一致率 $\ge 95\%$），设定得分阈值（如 $\ge 0.75$）作为高质量指示变量。
> 3. **[[Effect Size Conversion|效应量标准化转换]]与正态化** 将不同一阶指标统一转换为皮尔逊相关系数 $r$ 或标准化均值差 $g$，运用 Fisher's $z$ 变换实现方差稳定化。
> 4. **多水平 CHE 与 RVE 稳健方差建模** 设定集群内相关系数（$\rho = 0.8$），运用经验残差构造三明治估计量，计算稳健标准误与小样本 $F$ 检验。
> 5. **多水平改进艾格回归偏倚检验与校正** 检验小研究效应并根据回归模型截距输出偏倚校正后的二阶效应量点估计值与置信区间。
> 6. **二阶元回归与亚组调节变量检验** 纳入理论构念类型、自变量/结果变量角色、研究设计等调节变量，全面分解效应异质性来源。

---

## 核心统计模型与数学公式

> [!formula-set] 二阶元分析统计推断与加权建模流程
> ```mermaid
> flowchart LR
>   A["一阶元分析效应量 z_ij<br/>(嵌套于一阶元分析 j)"] --> B["三水平方差分解<br/>σ²_3(研究间) + σ²_2(研究内) + V_ij(抽样)"]
>   B --> C["相关与层级效应工作模型 (CHE)<br/>设定协方差矩阵 V (ρ=0.8)"]
>   C --> D["稳健方差估计 (RVE)<br/>构造经验三明治估计量 V_R"]
>   D --> E["多水平艾格回归偏倚校正<br/>估计截距 β_0 与 95% CI/PI"]
>   E --> F["二阶元回归模型<br/>全变量调节检验 (Wald F 检验)"]
> ```

---

### 1. 固定效应二级汇总的数学等价性与方法论条件

> [!formula-step] 公式步骤　固定效应二级汇总等价性定理
> $$d_{\text{second}} = \frac{\sum_{j=1}^{m} w_j d_j}{\sum_{j=1}^{m} w_j} = \frac{\sum_{j=1}^{m} \left(\sum_{i=1}^{k_j} w_{ji}\right) d_j}{\sum_{j=1}^{m} \left(\sum_{i=1}^{k_j} w_{ji}\right)} = \frac{\sum_{\text{all } i} w_i d_i}{\sum_{\text{all } i} w_i}$$
>
> **这个公式在做什么** 证明当且仅当所有一阶元分析纳入的主要研究**互不重叠**且严格按精度反比（$w_j = 1/v_{d_j}$）加权时，二级固定效应元分析才在数学上等价于对所有原始研究直接进行的一级元分析。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 24–28)]]
>
> **推导过程与数学原理**
> 1. 第一级元分析 $j$ 对主要研究 $i$ 进行加权估计：$d_j = \frac{\sum w_{ji} d_{ji}}{\sum w_{ji}}$，其方差为 $v_{d_j} = \frac{1}{\sum w_{ji}}$。
> 2. 第二级元分析对一阶元分析 $j$ 进行加权估计：$w_j = 1/v_{d_j} = \sum_{i=1}^{k_j} w_{ji}$。
> 3. 代入二级汇总公式展开即得公式右端：$d_{\text{second}} = \frac{\sum_{\text{all } i} w_i d_i}{\sum_{\text{all } i} w_i}$。
>
> **注意事项** 若一级元分析间存在重复研究，该研究的数据被重复计数，人为压缩了标准误并严重扭曲点估计；因此现代二阶元分析必须采用处理聚类依赖性的多水平模型。

---

### 2. Wecker et al. (2016) 二阶元分析 6 项方法论要求

> [!ref-table]- 二阶元分析必须满足的 6 项方法论要求及其违背后果
> | 要求编号 | 方法论准则与规范要求 | 违背类型 | 对效应量 $d$ 与标准误 $SE_d$ 的影响后果 |
> |---|---|---|---|
> | **要求 1** | 统一效应量测度（推荐 Hedges' $g$），正确计算合并标准差，严格区分 SE 与 SD，执行 Fisher's $z$ 转换。 | 测度混合 / SE 与 SD 混淆 | 效应量可放大或缩小十倍（如 Eisenstaedt 1990 中 SE=2.74 被当 SD，导致 $d$ 从 $-0.80$ 膨胀至 $-8.29$），极端值严重扭曲总体平均。 |
> | **要求 2** | 一级元分析必须按精度反比加权（$w_{ji} = 1/v_{ji}$），严禁使用简单算术平均。 | 一级未加权平均 | 估计非最优；$p$ 值与置信区间失真，系统性低估标准误。 |
> | **要求 3** | 纳入的一阶元分析必须基于**互不重叠的主要研究集**，确保抽样独立性。 | 主要研究重复计数 | 重复数据被赋予不成比例的过大权重，置信区间虚假变窄，显著性检验假阳性膨胀。 |
> | **要求 4** | 每个一级元分析必须完整报告联合效应量 $d_j$ 及其方差/标准误/置信区间。 | 方差与精度信息缺失 | 无法确定真实权重与精度边界。 |
> | **要求 5** | 二级汇总必须使用精度反比（$w_j = 1/v_{d_j}$）加权，严禁使用简单算术平均。 | 二级未加权平均 | 估计出现两级复合偏差，排名发生严重对调（如正确加权后 $d = 0.59 \to 0.23$，排名从 #26 骤跌至 #98）。 |
> | **要求 6** | 正确计算联合标准误（$SE_d = \sqrt{1/\sum w_j}$）与 95% 置信区间，执行严格统计显著性检验。 | 标准误人为武断设定 | 人为设置 0.05 下限导致置信区间不可靠，显著性不可解释。 |

---

### 3. 相关与层级效应工作模型（Correlated and Hierarchical Effects Model, CHE）

> [!formula-step] 公式步骤　CHE 三水平随机效应模型
> $$z_{ij} = \beta_0 + \sum_{p=1}^P \beta_p X_{p,ij} + \zeta_{(3)j} + \zeta_{(2)ij} + \epsilon_{ij}$$
> $$\operatorname{Var}(\zeta_{(3)j}) = \tau_3^2, \quad \operatorname{Var}(\zeta_{(2)ij}) = \tau_2^2, \quad \operatorname{Var}(\epsilon_{ij}) = V_{ij}$$
>
> **这个公式在做什么** 将一阶效应量 $z_{ij}$ 的总方差分解为三层：一阶元分析间变异 $\tau_3^2$（Level 3）、同一元分析内不同效应量间变异 $\tau_2^2$（Level 2）以及主要研究已知的抽样方差 $V_{ij}$（Level 1）。
>
> **推导过程与数学原理**
> 1. 考虑来自同一一阶元分析 $j$ 的多个效应量存在相关性，设定集群内相关系数为 $\rho$（通常在敏感性检验中设定 $\rho = 0.8$）。
> 2. 构建块对角已知抽样协方差工作矩阵 $V_j$，其中对角线元素为 $V_{ijj} = 1/(n_{ij}-3)$，非对角线协方差为 $\operatorname{Cov}(z_{aj}, z_{bj}) = \rho \sqrt{V_{aj} V_{bj}}$。
> 3. 采用限制极大似然法（REML）联合估计研究间异质性方差分量 $\tau_3^2$ 与 $\tau_2^2$。
>
> **结果怎么读** 异质性方差比率 $I_{(3)}^2 = \frac{\tau_3^2}{\tau_3^2 + \tau_2^2 + \bar{V}}$ 与 $I_{(2)}^2 = \frac{\tau_2^2}{\tau_3^2 + \tau_2^2 + \bar{V}}$ 分别反映二阶元分析间与元分析内的真实效应离散比例。

---

### 4. 稳健方差估计与三明治估计量（Robust Variance Estimation, RVE）

> [!formula-step] 公式步骤　聚类稳健三明治方差估计量
> $$V_R = \left( \sum_{j=1}^m X_j' W_j X_j \right)^{-1} \left( \sum_{j=1}^m X_j' W_j e_j e_j' W_j X_j \right) \left( \sum_{j=1}^m X_j' W_j X_j \right)^{-1}$$
>
> **这个公式在做什么** 在 CHE 工作模型设定的相关系数 $\rho$ 不完全准确甚至协方差结构误设的条件下，基于经验残差向量 $e_j$ 给出渐近无偏、稳健的标准误与假设检验结果。
>
> **推导过程与数学原理**
> 1. 设广义最小二乘（GLS）权重矩阵为 $W_j = (\tau_3^2 I + \tau_2^2 J + V_j)^{-1}$。
> 2. 残差向量定义为 $e_j = z_j - X_j \hat{\beta}$。
> 3. 利用经验外积矩阵 $\sum X_j' W_j e_j e_j' W_j X_j$ 替代未知的真实协方差矩阵，形成经典的“面包-肉-面包”三明治估计量结构。
> 4. 配合 Tipton & Pustejovsky（2015）的小样本自由度调整，采用 Hotelling $T^2$ 近似进行稳健 $F$ 检验，有效控制假阳性错误率。
>
> **结果怎么读** 即使一阶效应量之间存在未知的复杂交叉重叠，RVE 也能保证置信区间和 $p$ 值的严格可信度。

---

### 5. 多水平偏倚校正艾格回归模型（Multilevel Egger's Test）

> [!formula-step] 公式步骤　多水平艾格回归偏倚检验
> $$z_{ij} = \beta_0 + \beta_{\text{SE}} \sqrt{V_{ij}} + \zeta_{(3)j} + \zeta_{(2)ij} + \epsilon_{ij}$$
>
> **这个公式在做什么** 检验全领域是否存在小研究效应与发表偏倚（Publication Bias），并通过回归截距 $\beta_0$ 估计剔除小样本膨胀效应后的无偏二阶效应量。
>
> **数学原理与读法**
> - 若斜率系数 $\beta_{\text{SE}}$ 显著（$p < 0.05$），表明效应量大小与抽样标准误显著正相关，证实存在显著的小研究偏倚；
> - 截距项 $\beta_0$ 即代表当抽样误差趋近于 0（理论无限大样本）时的二阶真实效应量估计值，通过 $\tanh(\beta_0)$ 还原为相关系数汇报。

---

## 认识论辩护与推论层级约束

> [!concept-lens] Qvortrup (2015) 的辩护与动态知识学习模型
> [[Argument_Qvortrup_2015_Paideia|Qvortrup (2015, pp. 27–33)]] 从支持者角度为二阶综合的合理性辩护：元-元分析通过效应量将不同的具体测量转换为“共同表达式”，使跨研究比较相对学习结果成为可能。但他同时指出，共同表达式的代价是结果高度抽象化，难以判断总体效应究竟来自表层记忆、深层理解还是概念性学习；因此主张引入[[Dynamic Knowledge and Learning Model|动态知识与学习模型]]，按知识类型对学习结果进行多维细化分解。

> [!boundary] Higgins (2016) 的比较推论层级与苹果橙子类比
> [[Argument_Higgins_2016_RE|Higgins (2016, pp. 40–41)]] 指出，**比较性元分析**（在单一元分析内比较多种干预）回答的是“X 是否比 Y 更有效”；而**比较性元综合**（跨元分析比较）面临更高层级的“苹果与橙子”难题。以 Graham et al. (2012) 写作教学元分析为例，虽然可以识别策略教学、自我调节、文本结构、创造力与转录等共同有益特征，但这类似于讨论水果的共同繁殖特征（种子），无法推断橙子特有的内部组织结构。

---

## 软件实现与代码规程

> [!software-impl] R 语言多水平二阶元分析实现代码
> ```R
> library(metafor)
> library(clubSandwich)
> 
> # 1. 效应量转换与计算抽样方差（Fisher's z）
> dat <- escalc(measure = "ZCOR", ri = r_val, ni = n_sample, data = raw_data)
> 
> # 2. 构建 CHE 协方差工作矩阵（设定集群内相关系数 rho = 0.8）
> V_mat <- impute_covariance_matrix(vi = dat$vi, cluster = dat$meta_id, r = 0.8)
> 
> # 3. 拟合三水平 CHE 随机效应模型
> model_che <- rma.mv(yi, V_mat, random = ~ 1 | meta_id / effect_id, 
>                     data = dat, sparse = TRUE)
> 
> # 4. 应用 RVE 稳健方差估计（CR2 小样本校正）
> robust_res <- coef_test(model_che, vcov = "CR2", cluster = dat$meta_id)
> 
> # 5. 多水平二阶元回归调节检验
> model_reg <- rma.mv(yi ~ predictor_type + study_design + amstar_high, 
>                     V_mat, random = ~ 1 | meta_id / effect_id, data = dat)
> robust_reg <- Wald_test(model_reg, constraints = constrain_predictors(model_reg), 
>                         vcov = "CR2", cluster = dat$meta_id)
> ```

---

## 使用此方法的核心代表研究

> [!evidence-grid] 使用此方法的核心代表研究
> - **[[Visible Learning]]** Hattie (2009) 综合 800 多项元分析的开创性巨型综合项目。[[Argument_Terhart_2011_JCS|(Terhart, 2011)]]
> - **[[EEF Teaching and Learning Toolkit]]** 英国教育捐赠基金会以效应量与额外学习月数排名 30+ 类教育干预的循证政策工具。[[Argument_Wrigley_2019_ERE|(Wrigley & McCusker, 2019)]]
> - **创造力全领域二阶元分析** Runco et al. (2026) 综合 52 项一阶元分析（2,609 项原始研究、124 万被试），运用 CHE 与 RVE 确立创造力预测效度与教育干预效应。[[Argument_Runco_2026_CRJ|(Runco et al., 2026)]]
> - **固定效应等价性与方法论批判** Wecker et al. (2016) 从固定效应数学模型推导 6 项要求并系统审查《可见的学习》。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016)]]

---

## 方法学局限与学术争议总览

> [!warning] 方法学局限与争议提示
> 二阶元分析虽然在统计技术上实现了多水平稳健化，但在认识论和证据应用层面仍面临多重系统性挑战：
> 1. **试验灵敏度混淆** 效应量大小可能反映研究者操纵试验灵敏度的难易程度而非干预本身有效性（Simpson, 2017, 2019）；
> 2. **偏倚逐级复合** 一阶元分析中的未加权、SE/SD 混淆与公式不可比性无法在二阶统计中被自动消除（Allerup, 2015; Bergeron & Rivard, 2017; Wecker et al., 2016）；
> 3. **透明度与数据重构危机** 粗放元综合常存在数据提取不透明与证实偏差（Johnson & Janzen, 2023; O'Connor, 2020）；
> 4. **因果机制距离与政策角色争议** 宏观抽象聚合远离了实在层面的因果机制，知识的局部性与临时性使其难以直接指导政策决策（Snook et al., 2009; Terhart, 2011; Wiliam, 2019; Wrigley & McCusker, 2019）。
>
> 完整详尽的批判脉络、数学反例、透明度重构与案例剖析详见专门理论条目：
> 🔗 **[[Critique of Meta-meta-analysis|元-元分析批判（Critique of Meta-meta-analysis）]]**。

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关联方向 | 说明 |
> |:-----|:-----|:---------|:-----|
> | [[Critique of Meta-meta-analysis]] | 概念 | 方法学反思 | 系统阐释元-元分析在认识论、测量错位与政策误用层面的理论批判。 |
> | [[Effect Size Conversion]] | 方法 | 计算前置 | 二阶元分析依赖效应量转换统一不同一阶研究的量规尺度。 |
> | [[Robust Variance Estimation]] | 方法 | 核心统计 | RVE 三明治估计量是解决二阶聚类依赖性与小样本膨胀的支柱技术。 |
> | [[AMSTAR]] | 工具 | 质量控制 | 用于二阶元分析中对一阶元分析规范度进行量化评级的方法学工具。 |
> | [[Argument_Runco_2026_CRJ|Runco et al. (2026)]] | 论证 | 典范应用 | 创造力领域二阶元分析代表作，确立了现代六步建模与偏倚校正规程。 |
> | [[Argument_Wecker_2016_ZfE|Wecker et al. (2016)]] | 论证 | 数学证明 | 推导二级固定效应等价性的 6 项数学要求，揭示粗糙元综合的计算失真。 |
