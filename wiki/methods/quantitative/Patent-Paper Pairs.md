---
title: Patent-Paper Pairs
aliases:
  - 专利-论文对
  - 专利论文对
  - 专利论文配对法
  - patent-paper pair
  - patent paper pairs
summary: "科学计量学与创新经济学中用于因果识别正式知识产权制度对科学知识流动影响的准实验研究设计。该方法通过将披露同一项底层科学发现的发明专利与其对应的同行评议学术期刊出版物精确配对，在保持科学成果实质内容恒定的前提下，利用专利申请、授权与许可的时间外生冲击，以期刊前向引用变化评估知识产权对科学传播的促进或阻滞效应。"
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
  - method/scientometrics
  - method/causal-inference
related_concepts:
  - "[[Construct]]"
  - "[[Patent Citation]]"
  - "[[Unit of Analysis]]"
  - "[[Technology Transfer Office]]"
  - "[[Construct Validity]]"
  - "[[Internal Validity]]"
  - "[[Document]]"
  - "[[Paradigm]]"
  - "[[Research Tool]]"
  - "[[Heterogeneity]]"
  - "[[Variable]]"
  - "[[Technology Transfer]]"
  - "[[Dependent Variable]]"
  - "[[Independent Variable]]"
  - "[[Material Transfer Agreement]]"
related_theories: []
related_methods:
  - "[[Matched Pairs Design]]"
  - "[[Difference-in-Differences]]"
  - "[[Experimental Research]]"
  - "[[Standard Error]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Bibliometric Analysis]]"
  - "[[Record Linkage]]"
  - "[[Journal Impact Factor]]"
  - "[[Genetic Matching]]"
  - "[[Author Name Disambiguation]]"
  - "[[Matching]]"
related_instruments: []
related_persons:
  - "[[Fiona Murray]]"
  - "[[James C. Scott]]"
  - "[[David C. Mowery]]"
related_facts:
  - "[[United States Patent and Trademark Office]]"
  - "[[Education Policy Outlook]]"
  - "[[Web of Science]]"
  - "[[Scopus]]"
  - "[[Bayh-Dole Act of 1980]]"
related_arguments:
  - "[[Argument_Thompson_et_al_2018_RP]]"
confidence: high
status: draft
created: 2026-11-04
updated: 2026-11-11
---

---

> [!def] Patent-Paper Pairs
> **专利-论文对（Patent-Paper Pairs）** 是科学学、创新经济学与科技政策研究中用于因果识别知识产权制度对科学知识扩散影响的定量[[Matched Pairs Design|配对设计]]。该方法的核心逻辑在于：寻找并建立针对同一项科学发现同时形成的学术期刊出版物与发明专利权之间的映射关联。在底层科学[[Construct|构念]]与技术实质保持不变的前提下，研究者利用专利从申请到正式授权或商业许可的时间滞后（时序外生冲击），追踪关联学术成果在法律状态变动前后的期刊前向被引变化，以此评估排他性产权保护究竟促进了技术商业化还是阻碍了开放科学传播。[[Argument_Thompson_et_al_2018_RP|(Thompson et al., 2018, pp. 1061–1063)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 链接测度知识流动受阻或扩散程度的 [[Patent Citation\|专利引用]] 与学术出版物前向期刊引用，检验制度干预对科学知识公地的因果影响。
> - **问题类型** 因果识别与政策评估（检验学术专利授权、排他许可及材料管制对后续累积性科学研究的因果冲击）。
> - **[[Unit of Analysis|分析单位]]** 配对成果（Patent-Paper Pair）、成果观测年度。
> - **输入数据** 大学或企业[[Technology Transfer Office|技术转移办公室]]（TTO）发明披露记录、专利数据库（[[United States Patent and Trademark Office|USPTO]] / [[Education Policy Outlook|EPO]]）授权与法律状态数据、科学引文数据库（[[Web of Science]] / [[Scopus]]）期刊出版物元数据与前向逐年被引明细。
> - **输出形式** 配对数据集、[[Difference-in-Differences|双重差分]]回归系数 $\gamma$（反映干预后成果被引频次的净变动幅度）。

> [!citation-card] 关键定义
> 考察专利与许可对科学传播的影响聚焦于“专利-论文对”。这些发现在学术期刊上公开发表，并同时成为成功获得专利授权的申请客体。利用这一设计，能够在保持科学发现基本属性不变的前提下，分离出知识产权排他权利对后续引用的因果影响。[[Argument_Thompson_et_al_2018_RP|(Thompson et al., 2018, p. 1061)]]
>
> *Our examination of the effects of patenting and licensing on scientific communication focuses on 'patent-linked publications' (Murray, 2002). These are discoveries that are published in scientific journals and become the subject of successful patent applications.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 发明专利与学术成果是否真正指向同一科学发现是该方法的构念效度核心。若专利涵盖范围显著宽于或偏离[[Experimental Research|实验研究]]，将引入匹配噪声。
> - **研究者判断** 配对算法的选择（专家人工审定、非专利引文反查、或基于发明人与机构的最大似然匹配）以及对后续引用的自引剔除标准。
> - **有效性标准** [[Internal Validity|内部效度]]依赖于平行趋势假定以及控制成果固有质量差异；统计结论效度需校正成果层面的聚类[[Standard Error|标准误]]。
> - **不声称回答的问题** 不能直接度量工业界未发表[[Document|文献]]的技术吸纳行为；未公开发表或未申请专利的孤立技术无法纳入此框架。

> [!method-stack] 方法层级
> - **上位方法** [[Quasi-Experimental Designs|准实验设计]]（[[Quasi-Experimental Designs\|准实验设计]]）、微观计量经济学与[[Bibliometric Analysis|文献计量学]]。
> - **前置步骤** [[Record Linkage|记录链接]]（Record Linkage）、发明人名称消歧、期刊引文时间窗匹配。
> - **变体与扩展** 人工专家配对法（Murray & Stern, 2007）、专利非专利引文链接法（Azoulay et al., 2012）、基于发明人的自动化最大似然配对法（[[Argument_Thompson_et_al_2018_RP|Thompson et al., 2018]]）。

> [!dev-timeline] 方法演变
> - **2002 — 概念奠基** [[Fiona Murray|菲奥娜·默里]]（Fiona Murray）在研究组织工程技术演化时首次提出科学网络与技术网络的“共演”，确立专利与学术成果配对的分析视角。
> - **2007 — 因果检验[[Paradigm|范式]]确立** 菲奥娜·默里与[[James C. Scott|斯科特]]·斯特恩（Scott Stern）通过人工核对 169 对生物技术配对样本，采用双重差分法发现专利授权导致关联成果后续引用下降约 10%，奠定了该方法的计量检验框架。
> - **2018 — 自动化最大似然算法与许可扩展** 尼尔·汤普森（Neil C. Thompson）等学者开发基于发明人全名的自动化最大似然匹配算法，将该方法从单纯的“专利授权”效应拓展至“专利商业许可”与“[[Research Tool|科研工具]]”[[Heterogeneity|异质性]]检验中。[[Argument_Thompson_et_al_2018_RP|(Thompson et al., 2018, pp. 1060–1069)]]

---

> [!formula-step] 步骤一　基于发明人与时序的最大似然配对
> $$P(\text{Match}_{ij} \mid X_{ij}) = \frac{\exp(\beta' X_{ij})}{1 + \exp(\beta' X_{ij})}$$
>
> **这个公式在做什么** 计算特定专利 $i$ 与候选科学出版物 $j$ 属于同一项基础科学发现的后验匹配概率。输入发明人与主要署名学者姓名重合度、发明披露时间与成果刊发时间间隔、机构归属与技术文本重叠特征，输出二元匹配概率值。[[Argument_Thompson_et_al_2018_RP|(Thompson et al., 2018, p. 1063)]]
>
> **符号说明** $X_{ij}$ 为专利发明人与发表成果署名学者的姓名重合特征向量；$\beta$ 为模型权重参数。
>
> **数学直觉** 专利发明人通常也是核心科研成果的主要署名者；通过设定时间窗口与姓名唯一性限制，最大似然算法能够在大规模样本中自动化重现专家人工核验的配对结果，在测试样本中达到 95% 以上的一致率。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 概率阈值 | 设定合理截止概率以判定配对成立，未达阈值的候选出版物予以剔除。 |
> > | 注意 | 同名消歧 | 需防范常见姓氏导致的跨学科错误关联，必须结合机构与研究领域限制。 |

> [!formula-step] 步骤二　配对双重差分因果估计
> $$\Delta \text{Citations}_{t \to t+i} = \beta_0 + \gamma \text{License}_{t} + \beta_1 \text{Age}_{t} + \beta_2 \text{PubYear} + \sum \beta_k X_{kt} + \epsilon_{t}$$
>
> **这个公式在做什么** 测算在配对样本中，专利发生干预（如商业许可或正式授权）对对应出版物在干预后第 $i$ 年（$i \in \{0, 1, 2, 3\}$）被引增量 $\Delta \text{Citations}$ 的净效应。[[Argument_Thompson_et_al_2018_RP|(Thompson et al., 2018, p. 1065)]]
>
> **符号说明** $\text{License}_t$ 为许可状态指示[[Variable|变量]]；$\gamma$ 为关注的核心处理效应参数；$X_{kt}$ 为[[Journal Impact Factor|期刊影响因子]]与前期引用等控制变量。
>
> **数学直觉** 通过一阶纵向差分消除出版物不随时间变异的固有质量，再通过处理组与对照组横向差分消除宏观时间趋势，从而剥离出纯净的处理效应。

---

> [!software-impl] 软件实现
> - **数据来源** USPTO 专利检索数据库、Web of Science 科学引文索引、[[Technology Transfer|大学技术转移]]办公室内部行政披露数据库。
> - **核心包或命令** Python (`RecordLinkage`, `fuzzywuzzy`), R (`Matching`, `fixest`), Stata (`reghdfe`).
> - **实现流程** 发明人姓名清洗与消歧 → 时间窗口筛选 → 建立候选配对矩阵 → [[Genetic Matching|遗传匹配]]获得均衡对照组 → 运行加权双重差分回归。
> - **报告标准** 报告配对命中率、人工抽检验证准确率、匹配前后协变量平衡检验统计量（$t$ 检验与 KS 检验）及聚类稳健标准误。

> [!method-stack] 变量与诊断
> - **数据结构** 专利配对面板数据（Panel Data），包含干预前至少两期的逐年被引记录。
> - **[[Dependent Variable|因变量]]** 成果在各年份获得的同行学术前向引用频次（严格剔除合作研究者自引）。
> - **[[Independent Variable|自变量]]** 专利状态变动哑变量（如专利授权、达成排他许可或非排他许可）。
> - **关键诊断** 政策干预前被引增长率（斜率）的平行趋势检验。

---

> [!method-fit] 适用判断
> - **适合使用** 评估大学技术转移、知识产权扩张、专利资助政策对基础科学成果传播影响的定量因果研究。[[Argument_Thompson_et_al_2018_RP|(Thompson et al., 2018, p. 1061)]]
> - **谨慎使用** 专利申请与成果发表时间间隔超过 5 年的情况（技术方案可能已发生实质性演化）。
> - **不适合使用** 未经同行评议发表的纯商业保密发明，或纯思辨无具体工业应用价值的理论探讨。

---

> [!method-limits] 方法局限
> - **样本选择偏误** 仅能捕捉既公开发表又申请发明专利的“双重披露”成果，这部分成果通常具有更高的科学价值与应用潜力，无法直接推论至一般性期刊成果或一般性专利。
> - **引用指标局限** 学术期刊引用仅反映科学界内部的注意力流向与实验使用，无法度量产业界对未公开发表成果专利的隐性技术扩散。
> - **配对误差累积** 跨数据库[[Author Name Disambiguation|姓名消歧]]存在一定假阳性与假阴性风险，需依赖高质量行政登记数据进行校验。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Patent Citation]] | 概念 | 评估技术端引用的互补指标，配对设计结合了科学端引文与技术端引文。 |
> | [[Research Tool]] | 概念 | 应用此方法发现显著知识流动负向抑制效应的核心对象领域。 |
> | [[Material Transfer Agreement]] | 概念 | 实证识别配对样本中是否属于实体科研工具的关键标记。 |
> | [[Technology Transfer]] | 概念 | 本方法评估的核心上位制度实践。 |
> | [[Difference-in-Differences]] | 方法 | 配对设计中执行因果估计的标准计量模型。 |
> | [[Genetic Matching]] | 方法 | 为配对样本构建平衡对照组的高级非参数匹配算法。 |
> | [[Matching]] | 方法 | 消除处理组与对照组基线特征差异的通用方法家族。 |
> | [[Record Linkage]] | 方法 | 跨专利库与引文库建立配对关系所依赖的数据清洗与链接技术。 |
> | [[David C. Mowery]] | 人物 | 推动专利与科学文献配对自动化及科技政策因果评估的代表学者。 |
> | [[Bayh-Dole Act of 1980]] | 事实 | 激发大学产生大量专利与学术成果双重披露现象的宏观政策背景。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Thompson_et_al_2018_RP|Thompson et al. (2018)]] — 发展基于发明人的最大似然配对方法，自动化构建加州大学专利与学术成果配对样本，并结合遗传匹配与 DID 检验专利许可的异质性影响。
