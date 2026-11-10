---
title: Natural Experiment
aliases:
  - 自然实验
  - 准自然实验
  - 自然实验法
  - Quasi-Natural Experiment
summary: "利用自然界、历史事件、政策突变或制度行政划分产生的外生冲击构建反事实对照组的因果识别研究设计；通过非人为干预的外生变异分离不可观测混杂变量与选择偏误，兼具高内部效度与观察性现实情境，但受制于局部平均处理效应（LATE）带来的外推效度局限。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 27
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/experimental-design
  - theme/causal-inference
  - theme/econometrics
related_concepts:
  - "[[Study Population and Sample]]"
  - "[[Variable]]"
  - "[[Credibility Revolution]]"
  - "[[Unit of Analysis]]"
  - "[[National Innovation System]]"
  - "[[Early-Career Researchers]]"
  - "[[Epistemology]]"
  - "[[Counterfactual]]"
  - "[[Causality]]"
  - "[[Internal Validity]]"
  - "[[External Validity]]"
  - "[[Dependent Variable]]"
related_theories: []
related_methods:
  - "[[Random Assignment]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Difference-in-Differences]]"
  - "[[Regression Discontinuity Design]]"
  - "[[Instrumental Variables]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Experimental Research]]"
related_instruments: []
related_persons:
  - "[[Pierre Azoulay]]"
  - "[[Dashun Wang]]"
related_facts:
  - "[[Advanced Technological Education]]"
  - "[[National Institutes of Health]]"
  - "[[Bayh-Dole Act of 1980]]"
  - "[[Howard Hughes Medical Institute]]"
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit11]]"
  - "[[Argument_Sahlgren_2015_CPS]]"
confidence: high
status: active
created: 2026-11-02
updated: 2026-11-11
---

---

> [!def] Natural Experiment
> 自然实验（Natural Experiment）指研究者利用不受被研究对象主观控制的外部自然事件、历史意外、法律颁布或行政裁决切分线等外生变异，将[[Study Population and Sample|研究样本]]自然分割为处理组与对照组，从而识别因果效应的实证研究设计。与人为[[Random Assignment|随机分配]]的[[Randomised Controlled Trials|随机对照试验]]不同，自然实验依赖现实世界中偶然产生的类随机分配机制，在不进行人为伦理干预的前提下剥离不可观测混杂[[Variable|变量]]，是微观计量经济学[[Credibility Revolution|可信性革命]]的核心支柱。[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|(Wang & Barabási, 2021, pp. 249–250)]]

> [!method-scope] 方法范围
> - **研究对象** 经历外生政策冲击、突发制度变动、自然灾害或制度截断阈值的个体、机构、地区或科学共同体。
> - **问题类型** 因果效应识别、政策干预净效应评估、制度机制检验。
> - **[[Unit of Analysis|分析单位]]** 科学家个体、科研团队、学术成果、资助申请、学生群体、学校、大学或[[National Innovation System|国家创新系统]]。
> - **输出形式** 平均处理效应（[[Advanced Technological Education|ATE]]）、局部平均处理效应（LATE）、因果弹性系数或断点跳跃估计值。

> [!citation-card] 关键定义
> 寻找一个随机发生的外部事件作为临界划分点，并系统考察其前后发生的变化，这种方法被称为“自然实验”或“准实验”。以[[Early-Career Researchers|青年学者]]遭遇基金申请挫折的研究为例，申请人的评分恰好位于[[National Institutes of Health|美国国家卫生研究院]]（NIH）资助及格线之上还是之下，对于申请人自身的内在能力特质而言是完全外生的。如果这一微小分差预测了学者后续十年的职业生涯走向，就确立了资助待遇与科研成果之间的纯粹因果联系。[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|(Wang & Barabási, 2021, p. 250)]]
>
> *Find a randomly occurring event, use it as a cutoff, and examine what happens before and after. This is known as a “natural experiment” or a “quasi-experiment.”... Whether junior PIs were just above or below the funding threshold for NIH grants is an exogenous variation to any individual characteristics of the PIs themselves... if that predicts your future career outcome, it must mean that there is a link between funding and career outcome, independent of any other observable or unobservable factors.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 坚持[[Counterfactual|反事实]][[Causality|因果推断]]框架（Neyman-Rubin 因果模型）；主张单纯的观察性统计关联不能代表因果联系，真实的因果关系必须依托外生变异进行识别。
> - **研究者角色** 研究者充当外部观察者与数据分析者，不人为操纵干预分配，避免了传统实验在科研资助与政策领域的伦理阻力。
> - **有效性标准** 高度聚焦[[Internal Validity|内部效度]]（外生性假设、类随机分配成立、无溢出效应）；高度关注由局部样本（阈值邻域）向宏观总体外推时的[[External Validity|外部效度]]限制。
> - **不声称回答的问题** 自然实验估算的处理效应通常为特定局部样本的局部平均处理效应（LATE），无法直接外推至远离阈值的宏观全局命题。

> [!method-stack] 方法层级
> - **研究设计** 依托制度突变、行政界线或不可抗力事件构建的自然准实验。
> - **前置步骤** 检验外生冲击的有效性、平行趋势检验或阈值连续性检验、混杂协变量平衡性诊断。
> - **核心估计技术** [[Difference-in-Differences|双重差分]]（DID）、[[Regression Discontinuity Design|断点回归设计]]（RDD）、[[Instrumental Variables|工具变量法]]（IV）。

---

> [!proc] 通用程序
> 1. 识别并论证产生外生冲击的自然事件、制度切分线或法律变动（如 NIH 资助分数线、知名学者猝逝、[[Bayh-Dole Act of 1980|拜杜法案]]生效）。
> 2. 定义处理组与未受干预的对照组，检验两组在冲击发生前的先验特征平衡性与平行演化趋势。
> 3. 收集冲击前后的微观面板数据或断点邻域样本。
> 4. 运用双重差分或断点回归模型估计局部平均处理效应。
> 5. 进行安慰剂检验、敏感性分析与带宽敏感性检验，排除替代性竞争假说。

> [!method-stack] 数据与变量
> - **数据结构** 微观追踪面板数据、行政审批全量底表、断点截面微观数据。
> - **样本与单位** 处于外生冲击影响域或制度截断线邻域的个体、团队或组织。
> - **变量或测量** 外生冲击虚拟变量（Treatment）、受冲击时间或断点运行变量（Running Variable）、[[Dependent Variable|结果变量]]（发表量、被引频次、专利申请数）。

---

> [!method-fit] 适用判断
> - **适合使用** 现实场景中无法进行人为随机干预（受限于科研伦理或财政体制）、但存在明确制度切分线、行政门槛或外生突发事件的因果评估场景（如评估资助门槛效应或基于境内族裔语言群体制度内对照剥离混杂）。[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|(Wang & Barabási, 2021, pp. 249–250)]]; [[Argument_Sahlgren_2015_CPS|(Sahlgren, 2015, pp. 25–29)]]
> - **谨慎使用** 外生性假设存在争议、个体具有主动操纵跨越门槛动机、或冲击存在跨组溢出效应的场景。
> - **不适合使用** 缺乏外生变异的纯横截面观察性调查，以及旨在回答宏观系统演化的全局命题。

---

> [!method-limits] 方法局限
> - **偏误来源** 门槛操纵偏误、处理组与对照组间的交互溢出、不可抗力事件伴生的复合多重外生冲击。
> - **适用边界** 结论通常仅在特定制度背景与局部人群中成立，存在确定性与可推广性之间的内在张力。[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|(Wang & Barabási, 2021, p. 250)]]
> - **误用风险** 将自然实验估计的局部处理效应（LATE）机械外推为普遍适用的全域因果律。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Credibility Revolution]] | 概念 | 自然实验与微观计量因果识别构成了经济学可信性革命的核心方法论基础。 |
> | [[Randomised Controlled Trials]] | 替代方法 | 随机对照试验通过人为随机化分配处理，自然实验则利用现实中的外生事件模拟随机化。 |
> | [[Quasi-Experimental Designs]] | 上位方法 | 自然实验是准[[Experimental Research\|实验设计]]中依赖现实外生变异的关键子集。 |
> | [[Regression Discontinuity Design]] | 补充方法 | 借助行政截断门槛构造的自然实验往往依托断点回归模型进行因果识别。 |
> | [[Difference-in-Differences]] | 补充方法 | 结合突发时间冲击的自然实验常运用双重差分模型估计政策净效应。 |
> | [[Counterfactual]] | 概念 | 自然实验的设计核心在于通过外生变异寻找有效对照组以构建严密反事实。 |
> | [[Pierre Azoulay]] | 人物 | 倡导将自然实验（如明星学者猝逝、[[Howard Hughes Medical Institute\|HHMI]] 入围落选）广泛引入科学经济学与科学学因果推断。 |
> | [[Dashun Wang]] | 人物 | 运用 NIH 基金申请切分线自然实验揭示青年学术挫折的长期反转效应。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit11|Wang & Barabási (2021)]] — 阐释自然实验在科学学因果识别中的方法论逻辑，并结合 NIH 青年基金及格线自然实验展示因果识别实证（pp. 249–250）。
> - [[Argument_Sahlgren_2015_CPS|Sahlgren (2015)]] — 利用芬兰境内瑞典语少数族裔学校构建制度内自然实验，在同等大纲与经费下剥离家庭背景混杂，因果揭示师资选拔门槛对学业产出的决定性影响（pp. 25–29）。
