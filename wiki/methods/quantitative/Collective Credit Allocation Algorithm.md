---
title: Collective Credit Allocation Algorithm
aliases:
  - 集体贡献分配算法
  - 合作论文声誉分配模型
  - 声誉分配算法
  - Shen-Barabasi Credit Allocation Algorithm
  - collective credit allocation
summary: "由沈华伟与艾伯特－拉斯洛·巴拉巴西（Shen & Barabási, 2014）提出的科学计量学与网络算法；依托目标成果的前向施引文献构建局部共引网络，提取相关成果集合并构建学者参与度矩阵与共引强度向量，通过矩阵乘法 c = As 计算多学者团队中各成员所享有的客观声誉份额；在诺贝尔奖多合署人获奖成果中实现了 81% 的预测准确率，揭示了学术声誉取决于突破成果发表后的持续独立产出与历史学术地位积淀的计量规律。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 13
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
related_theories: []
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Author Name Disambiguation]]"
related_instruments: []
related_persons:
  - "[[Hua-Wei Shen]]"
  - "[[Albert-László Barabási]]"
  - "[[Dashun Wang]]"
  - "[[Douglas Prasher]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit06]]"
confidence: high
status: draft
created: "2026-10-30"
updated: "2026-10-30"
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
> - **[[Construct Validity|构念效度]]** 输出的声誉份额真实反映了学术共同体基于引文网络形成的集体认知，能够有效跨越[[Alphabetical Authorship|字母序署名]]或名义挂名所制造的表面信息障碍；但该指标无法直接检验微观实验室内部的真实劳动投入，测量的是“社会感知的归属”而非“纯物理工时的耗费”。
> - **研究者判断** 施引文献时间窗口的选择、自引文献的清洗规则，以及相关共引成果参与度权重的分配策略（通常按学者人数平均分摊 $1/k$）。
> - **有效性标准** 在 63 项包含多位合署学者的历史诺贝尔奖获奖代表作中，算法对最终获奖科学家的预测准确率达 81%（51 篇准确命中），且在字母序的物理学与贡献序的生物化学领域均表现出高度稳健性。
> - **不声称回答的问题** 算法无法判断某项评奖决策在伦理道德层面是否“公正”，其功能在于揭示由客观引文结构所投射出的共同体平均认知趋势。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis]]、复杂网络共引分析（Co-citation Analysis）。
> - **前置步骤** 学者[[Author Name Disambiguation|姓名消歧]]、文献施引与引文拓扑图谱抽取。
> - **变体与扩展** 引入引文时序衰减因子的动态贡献模型；结合学者先发 h 指数或机构声望的复合贝叶斯推断模型。

> [!dev-timeline] 方法演变
> - **2014 — 沈华伟与巴拉巴西提出算法** 成果发表于 PNAS，奠定了基于共引矩阵的集体声誉分配基本数学架构。[[Argument_Wang_Barabasi_2021_Cambridge_Unit06|(Wang & Barabási, 2021, pp. 154–156)]]
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
> > [!example]- 手算示例
> > 假设目标成果 $p_0$ 由学者甲（红）与学者乙（绿）合著（$M=2$）。施引文献共引网络中筛选出两项紧密相关的论著 $p_1$ 与 $p_2$（即 $P = \{p_0, p_1, p_2\}$）：
> > - $p_0$：甲、乙合著（2 人），$A_{\cdot 0} = [0.5, 0.5]^T$；自共引强度设为 $s_0 = 10$；
> > - $p_1$：甲、乙合著（2 人），$A_{\cdot 1} = [0.5, 0.5]^T$；与 $p_0$ 共引强度 $s_1 = 2$；
> > - $p_2$：甲与外部学者合署（2 人），乙未参与，$A_{\cdot 2} = [0.5, 0.0]^T$；与 $p_0$ 共引强度 $s_2 = 8$。
> >
> > 矩阵乘法计算原始积分：
> > $$(As)_{\text{甲}} = 0.5 \times 10 + 0.5 \times 2 + 0.5 \times 8 = 5 + 1 + 4 = 10$$
> > $$(As)_{\text{乙}} = 0.5 \times 10 + 0.5 \times 2 + 0.0 \times 8 = 5 + 1 + 0 = 6$$
> >
> > 归一化计算声誉份额：
> > $$c_{\text{甲}} = \frac{10}{10 + 6} = \frac{10}{16} = 0.625 \quad (62.5\%)$$
> > $$c_{\text{乙}} = \frac{6}{10 + 6} = \frac{6}{16} = 0.375 \quad (37.5\%)$$
> >
> > 结论：学者甲因独立参与了高共引论著 $p_2$，其在 $p_0$ 中的声誉份额（62.5%）显著压制了学者乙（37.5%）。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 极端案例一：非对称成果库 | 当学者 A 围绕该领域发表了多篇持续被共引的论著，而学者 B 仅参与了 $p_0$ 时，算法将绝大部分声誉赋予学者 A。典型范例为根岸英一（Ei-ichi Negishi）与马场繁（Shigeru Baba）1976 年的诺贝尔奖级成果，马场仅参与该项研究，根岸后续发表多篇高引成果，最终根岸独享诺贝尔奖（pp. 153–154）。 |
> > | 读法 | 极端案例二：对称[[Coauthorship Network\|合著网络]] | 当两位学者深度绑定并联合发表了该课题下几乎全部高共引文献时，声誉份额各占 50%。典型范例为安德烈·海姆（Andre Geim）与康斯坦丁·诺沃肖洛夫（Konstantin Novoselov）共同获得 2010 年石墨烯诺贝尔物理学奖（p. 154）。 |
> > | 注意 | 先发声望赤字（Credit Deficit） | 青年学者若与成名大师在成熟领域合作，即便后续独立发表若干成果，由于大师的历史代表作依然会频繁被同行共引，青年学者往往需要经历漫长的文献积累才能稀释大师的先发生誉垄断（p. 156）。 |

---

> [!method-case] 典型应用案例：诺贝尔奖预测与重大错位争议
> 1. **2013 年希格斯玻色子诺贝尔物理学奖核算**
>    - 历史事实：1964 年共有三组独立团队（六位物理学家）提出玻色子质量机制，分别为恩格勒与布劳特（Englert & Brout）、希格斯（Higgs），以及古拉尼、哈根与基布尔（Guralnik, Hagen & Kibble）。2010 年美国物理学会将樱井奖授予全部六人；但 2013 年诺贝尔委员会仅将物理学奖授予希格斯与恩格勒。
>    - 算法重估：算法计算得出的声誉份额排序依次为：希格斯位居第一，基布尔（Kibble）位居第二，恩格勒位居第三（布劳特已去世）。算法表明，诺贝尔评奖委员会遗漏基布尔的决定偏离了物理学界的集体引文认知（pp. 157–158）。
> 2. **2008 年绿色荧光蛋白（GFP）诺贝尔化学奖核算**
>    - 历史事实：奖项授予钱永健、下村脩与马丁·沙尔菲三人，而首位克隆 GFP 基因的先驱[[Douglas Prasher|道格拉斯·普拉谢尔]]（Douglas Prasher）因离开学界而落选。
>    - 算法重估：算法测算普拉谢尔的贡献份额高达 0.199，虽低于钱永健（0.47）与下村脩（0.25），但显著高于正式获奖者沙尔菲（0.09）。科学界的集体引用事实证明，普拉谢尔的先驱基石地位从未被同行遗忘（pp. 157–158）。
