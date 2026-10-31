---
title: Collective Credit Allocation Algorithm
aliases:
  - 集体贡献分配算法
  - 合作论文声誉分配模型
  - 声誉分配算法
  - Shen-Barabasi Credit Allocation Algorithm
  - collective credit allocation
summary: "由沈华伟与艾伯特-拉斯洛·巴拉巴西（Shen & Barabási, 2014）提出的科学计量学与网络算法；依托目标成果的前向施引文献构建局部共引网络，提取相关成果集合并构建学者参与度矩阵与共引强度向量，通过矩阵乘法 c = As 计算多学者团队中各成员所享有的客观声誉份额；在诺贝尔奖多合署人获奖成果中实现了 81% 的预测准确率，揭示了学术声誉取决于突破成果发表后的持续独立产出与历史学术地位积淀的计量规律。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 19
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/algorithm
  - theme/scientometrics
  - theme/science-of-science
related_concepts:
  - "[[Document]]"
  - "[[Scientific Credit]]"
  - "[[Unit of Analysis]]"
  - "[[Construct Validity]]"
  - "[[Alphabetical Authorship]]"
  - "[[Coauthorship Network]]"
  - "[[Emergence]]"
  - "[[Matthew Effect in Academia]]"
  - "[[Author Contribution Disclosures]]"
  - "[[Construct]]"
related_theories: []
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Author Name Disambiguation]]"
  - "[[Network Analysis]]"
related_instruments: []
related_persons:
  - "[[Hua-Wei Shen]]"
  - "[[Albert-László Barabási]]"
  - "[[Dashun Wang]]"
  - "[[Douglas Prasher]]"
related_facts:
  - "[[National Academy of Sciences]]"
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit06]]"
confidence: high
status: draft
created: "2026-10-30"
updated: 2026-10-31
---

---

> [!def] Collective Credit Allocation Algorithm
> **集体贡献分配算法（Collective Credit Allocation Algorithm）** 是一种通过前向施引[[Document|文献]]网络与后向共引拓扑，客观量化多学者合作科研成果中个体学术声望份额的计算方法。该算法将目标成果全部施引文献所引用的相关成果集合界定为该主题的知识共同体本体，通过学者参与度矩阵 $A$ 与共引强度向量 $s$ 进行线性加权运算 $c = As$，以此模拟科学界在不透视内部实验细节的前提下自发形成的声誉分配过程。[[Argument_Wang_Barabasi_2021_Cambridge_Unit06|(Wang & Barabási, 2021, pp. 153–156)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 多学者合作成果中各合署人获得的公认学术声誉与优先权贡献份额（[[Scientific Credit]]）。
> - **问题类型** 科学计量测度、学术荣誉归属评价与同行评议隐性声誉预测。
> - **[[Unit of Analysis|分析单位]]** 单项多学者学术论著及其合署人集合。
> - **输入数据** 目标成果及其前向施引文献集合、所有施引文献包含的完整参考文献列表，以及相关成果的合署学者全量名录。
> - **输出形式** 归一化的学者声誉份额向量 $c = (c_1, c_2, \dots, c_m)^T$，满足 $\sum_{i=1}^m c_i = 1$。

> [!citation-card] [[Hua-Wei Shen|沈华伟]]与[[Albert-László Barabási|巴拉巴西]]论集体声誉分配的算法逻辑
> 算法的核心逻辑表明，当我们向团队成员分配科学声誉时，我们并不需要确切获知究竟是谁真正完成了实验操作。这强调了一条极为重要的原则：科学声誉的归属不仅关乎实际劳动投入，更取决于共同体的集体感知。每一篇新增发表的后续文献都会传达出关于学者学术贡献的隐性信息。通过追踪论著如何被共同体持续共引，该算法能够以独立于学科特定署名惯例的方式，精确还原科学界分配荣誉的真实面貌。[[Argument_Wang_Barabasi_2021_Cambridge_Unit06|(Wang & Barabási, 2021, pp. 154–156)]]
>
> *The credit allocation algorithm implies that when we allocate credit to team members, we don’t need to know who actually did the work. This underlines an important message: Scientific credit is not just about contribution – it’s also about perception... In the algorithm, each additional paper conveys implicit information about the author’s perceived contribution, capturing, in a discipline-independent fashion, how the scientific community assigns credit to each paper.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 输出的声誉份额真实反映了学术共同体基于引文网络形成的集体认知，能够有效跨越[[Alphabetical Authorship|字母序署名]]或名义挂名所制造的表面信息障碍；但该指标无法直接检验微观实验室内部的真实劳动投入，测量对象是社会感知的归属，有别于纯物理工时的耗费。
> - **研究者判断** 施引文献时间窗口的选择、自引文献的清洗规则，以及相关共引成果参与度权重的分配策略（通常按学者人数平均分摊 $1/k$）。
> - **有效性标准** 在 63 项包含多位合署学者的历史诺贝尔奖获奖代表作中，算法对最终获奖科学家的预测准确率达 81%（51 篇准确命中），且在字母序的物理学与贡献序的生物化学领域均表现出高度稳健性。
> - **不声称回答的问题** 算法无法判断某项评奖决策在伦理道德层面是否公正，其功能在于揭示由客观引文结构所投射出的共同体平均认知趋势。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis]]、复杂网络共引分析（Co-citation Analysis）。
> - **前置步骤** 学者[[Author Name Disambiguation|姓名消歧]]、文献施引与引文拓扑图谱抽取。
> - **变体与扩展** 引入引文时序衰减因子的动态贡献模型；结合学者先发 h 指数或机构声望的复合贝叶斯推断模型。

> [!dev-timeline] 方法演变
> - **2014 — 沈华伟与巴拉巴西提出算法** 成果发表于《[[National Academy of Sciences|美国国家科学院]]院刊》（Proceedings of the National Academy of Sciences, PNAS），奠定了基于共引矩阵的集体声誉分配基本数学架构。[[Argument_Wang_Barabasi_2021_Cambridge_Unit06|(Wang & Barabási, 2021, pp. 154–156)]]
> - **2021 — 纳入科学学教材体系** [[Dashun Wang|王大顺]]与巴拉巴西将该算法作为分析团队科研声誉分配、解释诺贝尔奖遗漏争议的核心量化工具。[[Argument_Wang_Barabasi_2021_Cambridge_Unit06|(Wang & Barabási, 2021, pp. 153–158)]]

---

> [!formula-set]- 公式链总览
> ```mermaid
> flowchart LR
>   A["目标成果 p0<br>合署人集合 A0"] --> B["前向施引集 D<br>提取参考文献"]
>   B --> C["共引成果集 P<br>相关论著全集"]
>   C --> D["学者参与矩阵 A<br>共引强度向量 s"]
>   D --> E["线性加权 c = As<br>归一化声誉份额"]
> ```

---

> [!formula-step] 步骤一　共引成果集合与学者参与度矩阵构建
> 设目标论著为 $p_0$，其合署人集合为 $A_0 = \{a_1, a_2, \dots, a_M\}$。搜集所有引用 $p_0$ 的文献集合 $D = \{d_1, d_2, \dots, d_K\}$。
>
> 追踪 $D$ 中所有文献的参考文献列表，提取所有与 $p_0$ 发生过至少一次同篇共引的成果集合，构成相关学术成果全集：
> $$P = \{p_0, p_1, p_2, \dots, p_N\}$$
>
> 针对 $P$ 中的每一项成果 $p_j$（共 $N+1$ 项），计算目标学者 $a_i$ 在该成果中的参与度份额。构建大小为 $M \times (N+1)$ 的学者参与度矩阵 $A$：
> $$A_{ij} = \begin{cases} \dfrac{1}{k_j}, & \text{若学者 } a_i \text{ 属于成果 } p_j \text{ 的合署人，且该成果共有 } k_j \text{ 位署名者} \\ 0, & \text{若学者 } a_i \text{ 未参与成果 } p_j \end{cases}$$
>
> **这个公式在做什么** 将文献集合 $P$ 视为围绕该课题展开的学术成果总体，矩阵 $A$ 的每一列记录了相关成果 $p_j$ 的名义贡献如何分摊给目标学者。[[Argument_Wang_Barabasi_2021_Cambridge_Unit06|(Wang & Barabási, 2021, pp. 155–156)]]
>
> **符号说明**
> - $M$：目标成果 $p_0$ 的合署人总人数。
> - $N+1$：包含 $p_0$ 自身在内的全量相关共引成果总数。
> - $k_j$：共引成果 $p_j$ 的署名学者总数。

---

> [!formula-step] 步骤二　共引关联强度加权与最终信誉份额计算
> 计算 $P$ 中各成果 $p_j$ 与目标成果 $p_0$ 的共引强度（Co-citation Strength）$s_j$：
> $$s_j = \sum_{k=1}^K I(p_0 \in \text{Ref}(d_k) \land p_j \in \text{Ref}(d_k))$$
> 形成共引强度列向量 $s = (s_0, s_1, \dots, s_N)^T$。通过矩阵乘法计算各合署人的原始声誉积分，并进行归一化：
> $$c = \frac{A s}{\sum_{i=1}^M (As)_i}$$
>
> **这个公式在做什么** 将学者在各项相关成果中的参与度以共引频次为权重进行线性加权，输出目标成果中各学者的感知声誉份额 $c_i$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit06|(Wang & Barabási, 2021, pp. 155–156)]]
>
> **符号说明**
> - $s_j$：成果 $p_j$ 与目标成果 $p_0$ 在施引文献集合 $D$ 中被共同引用的总次数。
> - $c_i$：目标成果合署人 $a_i$ 所获得的最终学术声誉份额，数值处于 $[0, 1]$ 区间。
>
> **数学直觉** 论著 $p_j$ 与 $p_0$ 被同行共同提及的频次越高，表明 $p_j$ 与 $p_0$ 的知识主题关联度越紧密。若某位学者不仅署名了 $p_0$，还在其他与 $p_0$ 紧密共引的高权重成果中持续现身，共同体自然会将该学者视为该项突破的核心智力支柱。
>
> > [!example]- 原著图14-3基准手算示例
> > 以原著图 14-3 为基准 [[Argument_Wang_Barabasi_2021_Cambridge_Unit06|(Wang & Barabási, 2021, p. 156)]]：目标论著 $p_0$ 由红学者与绿学者合著（$M=2$），在 5 篇施引文献 $\{d_1, \dots, d_5\}$ 中提取出相关成果集 $P = \{p_0, p_1, p_2, p_3, p_4\}$：
> > - $p_0$：红、绿学者合署（2 人），参与度向量 $A_{\cdot 0} = [0.50, 0.50]^T$；自共引强度 $s_0 = 5$；
> > - $p_1$：红、绿学者合署（2 人），参与度向量 $A_{\cdot 1} = [0.50, 0.50]^T$；共引强度 $s_1 = 1$（仅被 $d_1$ 共同引用）；
> > - $p_2$：红学者与外部学者合署（2 人），绿学者未参与，参与度向量 $A_{\cdot 2} = [0.50, 0.00]^T$；共引强度 $s_2 = 4$（被 $d_1, d_2, d_3, d_5$ 共同引用）；
> > - $p_3$：红、绿学者与外部学者合署（3 人），参与度向量 $A_{\cdot 3} = [0.33, 0.33]^T$；共引强度 $s_3 = 3$（被 $d_2, d_3, d_4$ 共同引用）；
> > - $p_4$：四位外部学者合署（4 人），红、绿学者均未参与，参与度向量 $A_{\cdot 4} = [0.00, 0.00]^T$；共引强度 $s_4 = 2$（被 $d_3, d_4$ 共同引用）。
> >
> > 矩阵乘法计算原始积分：
> > $$(As)_{\text{红}} = 0.50 \times 5 + 0.50 \times 1 + 0.50 \times 4 + 0.33 \times 3 + 0.00 \times 2 = 2.5 + 0.5 + 2.0 + 1.0 + 0 = 6.0$$
> > $$(As)_{\text{绿}} = 0.50 \times 5 + 0.50 \times 1 + 0.00 \times 4 + 0.33 \times 3 + 0.00 \times 2 = 2.5 + 0.5 + 0.0 + 1.0 + 0 = 4.0$$
> >
> > 归一化计算声誉份额：
> > $$c_{\text{红}} = \frac{6.0}{6.0 + 4.0} = 0.60 \quad (60\%)$$
> > $$c_{\text{绿}} = \frac{4.0}{6.0 + 4.0} = 0.40 \quad (40\%)$$
> >
> > **算例启示** 红学者因独立参与了高共引权重的关联成果 $p_2$（$s_2 = 4$），其在突破论著 $p_0$ 中获得了 60% 的绝对主导声誉份额；这量化确证了在科学共同体眼中，突破之后的持续独立建树对学术优先权认定的决定性作用。
>
> > [!geogebra] 动态参数模拟
> > - **左侧控制滑块** 
> >   - $s_0$（蓝色）：共同核心突破成果 $p_0$ 的自身引用/共引强度（范围 $1$–$20$）；
> >   - $s_1$（红色）：学者甲主导的后续拓展成果 $p_1$ 与 $p_0$ 的共引强度（范围 $0$–$20$）；
> >   - $s_2$（绿色）：学者乙主导的后续拓展成果 $p_2$ 与 $p_0$ 的共引强度（范围 $0$–$20$）。
> > - **动态声誉对比条** 实时计算并可视化甲（红段）与乙（绿段）在突破成果中分配到的感知声誉份额百分比 $c_{\text{甲}}$ 与 $c_{\text{乙}}$。
> > - **右侧局部共引网络拓扑** 直观呈现施引文献共同体如何通过共引连线（连线粗细对应共引强度 $s$）在两名合著者间分配学术声望。
> > - **计量规律验证** 拖动滑块可直观重现：当两名学者后续拓展均衡时（$s_1 = s_2$），声誉呈现 50%-50% 对称均分；一旦某位学者在该方向持续产出高共引论著（如 $s_1 \gg s_2$），即便双方在原初成果中署名无差别，共同体声誉也会极度向该高产学者倾斜，精准解释诺贝尔奖评选中的非对称归属机制。
> >
> > ![[wiki/assets/geogebra/collective_credit_allocation.ggb]]
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 极端案例一：非对称成果库 | 当学者 A 围绕该领域发表了多篇持续被共引的论著，而学者 B 仅参与了 $p_0$ 时，算法将绝大部分声誉赋予学者 A。典型范例为根岸英一（Ei-ichi Negishi）与马场繁（Shigeru Baba）1976 年的诺贝尔奖级成果，马场仅参与该项研究，根岸后续发表多篇高引成果，最终根岸独享诺贝尔奖（pp. 153–154）。 |
> > | 读法 | 极端案例二：对称[[Coauthorship Network\|合著网络]] | 当两位学者深度绑定并联合发表了该课题下几乎全部高共引文献时，声誉份额各占 50%。典型范例为安德烈·海姆（Andre Geim）与康斯坦丁·诺沃肖洛夫（Konstantin Novoselov）共同获得 2010 年石墨烯诺贝尔物理学奖（p. 154）。 |
> > | 注意 | 先发声望赤字（Credit Deficit） | 青年学者若与成名大师在成熟领域合作，即便后续独立发表若干成果，由于大师的历史代表作依然会频繁被同行共引，青年学者往往需要经历漫长的文献积累才能稀释大师的先发生誉垄断（p. 156）。 |

---

> [!software-impl] 软件实现
> - **数据来源** Web of Science、Scopus、OpenAlex 或 Dimensions 等引文数据库；需导出目标成果及其施引文献（Citing papers）与参考文献（Cited references）。
> - **核心包或命令** Python 环境下的 `numpy`（矩阵代数运算）、`networkx`（共引网络拓扑构建）与 `pandas`（数据清洗与学者匹配）。
> - **实现流程** 检索目标论著获取施引集合 $D$；提取 $D$ 的参考文献集合构建共引集 $P$；消歧合署学者并填充参与矩阵 $A$；统计各成果与目标成果的共引频次生成强度向量 $s$；执行矩阵相乘 $c = As$ 并完成归一化。
> - **报告标准** 完整报告引文数据检索时间窗口、自引处理规则、学者姓名消歧准确率以及参与度权重分配基准。

> [!formula] Python 计算骨架
> ```python
> import numpy as np
>
> def collective_credit_allocation(A: np.ndarray, s: np.ndarray) -> np.ndarray:
>     """
>     计算多学者合著成果中的集体声誉分配份额
>     
>     参数:
>         A: 学者参与度矩阵 (M 位学者 x (N+1) 项共引成果)，A[i, j] = 1 / k_j
>         s: 共引强度列向量 ((N+1) 维，各成果与目标成果的共引频次)
>         
>     返回:
>         c: 归一化的学者声誉份额向量 (M 维，元素和为 1.0)
>     """
>     raw_credit = np.dot(A, s)
>     total = np.sum(raw_credit)
>     if total == 0:
>         return np.ones(A.shape[0]) / A.shape[0]
>     return raw_credit / total
> ```

> [!method-stack] 数据口径
> - **数据来源** 不同引文数据库的收录深度与期刊覆盖存在差异；跨库数据混用时须进行文献标识符（DOI/PMID）统一映射。
> - **时间与范围** 需合理界定施引文献的时间观察窗；对于发表时间较短的新成果，因引文网络尚未充分[[Emergence|涌现]]，算法输出可能呈现暂态波动。
> - **清洗与归属** 严格执行学者姓名消歧，剔除目标学者群体的成果自引，控制小团体互引网络对共引权重的非正常扰动。
> - **标准化** 算法输出为团队内部的相对声誉份额（和为 1.0）；进行跨领域或跨成果比较时，须结合目标成果的绝对引用量与学科基准分位数。

---

> [!method-fit] 适用判断
> - **适合使用** 多学者跨学科合作科研成果中的个体学术声望测度、科学奖项（如诺贝尔奖）荣誉归属预测，以及破除字母序署名遮蔽效应的客观计量评估。[[Argument_Wang_Barabasi_2021_Cambridge_Unit06|(Wang & Barabási, 2021, pp. 153–158)]]
> - **谨慎使用** 发表年限过短或累计被引频次过低的早期成果（缺乏足够的共引拓扑支撑）；存在严重学者同名异人歧义或参考文献元数据缺失的历史文献。
> - **不适合使用** 实验室微观内部按照纯工时、试剂消耗或数据录入量进行的操作性劳动考核；无法替代微观实验记录对学术不端行为的事实查证。

---

> [!method-limits] 方法局限
> - **测量偏误** 引文结构深嵌于[[Matthew Effect in Academia|学术马太效应]]与权威声望之中，算法测量的是学术共同体所持有的社会感知声誉（Perceived Credit），并不等同于实验室内部绝对客观的物理工时耗费。
> - **可比边界** 青年学者与资深大师合作时面临先发声誉赤字（Credit Deficit），其应得份额易被资深学者历史庞大的高引论著库所吸附与稀释。
> - **误用风险** 将算法输出的相对引文份额机械等同于科学发现的绝对正义，或将其作为单一指标直接绑定科研人员的人事晋升与薪酬核定。
> - **补救方式** 结合[[Author Contribution Disclosures|贡献者角色分类]]法（CRediT）声明、主要署名者与通讯联络惯例及同行定性评议，实现算法计量与微观质性证据的互补印证。

---

> [!method-case] 典型应用案例：诺贝尔奖预测与重大错位争议
> 1. **2013 年希格斯玻色子诺贝尔物理学奖核算**
>    - 历史事实：1964 年共有三组独立团队（六位物理学家）提出玻色子质量机制，分别为恩格勒与布劳特（Englert & Brout）、希格斯（Higgs），以及古拉尼、哈根与基布尔（Guralnik, Hagen & Kibble）。2010 年美国物理学会将樱井奖授予全部六人；但 2013 年诺贝尔委员会仅将物理学奖授予希格斯与恩格勒。
>    - 算法重估：算法计算得出的声誉份额排序依次为：希格斯位居第一，基布尔（Kibble）位居第二，恩格勒位居第三（布劳特已去世）。算法表明，诺贝尔评奖委员会遗漏基布尔的决定偏离了物理学界的集体引文认知（pp. 157–158）。
> 2. **2008 年绿色荧光蛋白（GFP）诺贝尔化学奖核算**
>    - 历史事实：奖项授予钱永健、下村脩与马丁·沙尔菲三人，而首位克隆 GFP 基因的先驱[[Douglas Prasher|道格拉斯·普拉谢尔]]（Douglas Prasher）因离开学界而落选。
>    - 算法重估：算法测算普拉谢尔的贡献份额高达 0.199，虽低于钱永健（0.47）与下村脩（0.25），但显著高于正式获奖者沙尔菲（0.09）。科学界的集体引用事实证明，普拉谢尔的先驱基石地位从未被同行遗忘（pp. 157–158）。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Scientific Credit]] | 测量对象 | 本算法测度与量化分配的核心[[Construct\|构念]]。 |
> | [[Alphabetical Authorship]] | 测量对象 | 算法无需依赖署名位次，克服字母序署名的归属模糊。 |
> | [[Matthew Effect in Academia]] | 理论 | 解释先发声望如何导致声誉吸附与先发赤字。 |
> | [[Bibliometric Analysis]] | 上位方法 | 算法依托共引[[Network Analysis\|网络分析]]与科学计量学基础方法。 |
> | [[Author Name Disambiguation]] | 前置方法 | 构建学者参与矩阵前必须完成的合著学者唯一标识消歧。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit06|Wang and Barabási (2021)]] — 验证算法在 63 项诺贝尔奖获奖成果中达到 81% 的预测准确率，并剖析普拉谢尔与希格斯玻色子案例。
