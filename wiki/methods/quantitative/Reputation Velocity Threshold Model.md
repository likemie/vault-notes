---
title: Reputation Velocity Threshold Model
aliases:
  - 声望加速度临界阈值模型
  - 声望促进偏好连接模型
  - cx 阈值模型
  - Reputation-Boost Preferential Attachment Model
  - Crossover Effect of Reputation
  - 声望临界阈值模型
summary: "由 Alexander M. Petersen et al. (2014) 提出的文献计量微观动力学建模方法；将新论著引文演化形式化为结合学者初始声望加速度 c0 的分段偏好连接方程（Π(c) ∝ c + c0, c < cx），揭示学术声誉在早期赋予显著引流优势，但当累积被引越过临界阈值 cx（资深学者 cx ≈ 40，青年学者 cx ≈ 10）后声望红利耗尽，引文动力学完全回归成果内在学术质量主导的纯偏好连接。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 8
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/model
  - theme/science-policy
  - theme/scientometrics
  - theme/citations
related_concepts:
  - "[[Document]]"
  - "[[Matthew Effect in Academia]]"
  - "[[Unit of Analysis]]"
  - "[[Construct Validity]]"
  - "[[Heterogeneity]]"
related_theories: []
related_methods:
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[National Academy of Sciences]]"
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit01]]"
confidence: high
status: completed
created: 2026-10-29
updated: 2026-10-30
---

---

> [!def] Reputation Velocity Threshold Model
> **声望加速度临界阈值模型（Reputation Velocity Threshold Model）** 由物理学家与[[Bibliometric Analysis|科学计量学]]者亚历山大·M·彼得森（Alexander M. Petersen）等人于 2014 年提出，是刻画新发表学术成果引文获取动态的微观量化方法。该模型将成果的边际引文增长率 $\Pi(c)$ 形式化为带有外生初速度的广义偏好连接方程：在[[Document|文献]]面世早期，学者既有学术声誉提供初始加速度 $c_0$（$\Pi(c) \propto c + c_0$）；当累积引用突破临界交叠阈值 $c_x$ 之后，声誉促进项归零，引文动态完全由成果内在质量主导的经典偏好连接（$\Pi(c) \propto c$）接管。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 32–34)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 单篇学术成果的微观引文增长加速度、学者历史声望对新成果的早期溢价效应，以及声誉红利出清的临界被引阈值 $c_x$。
> - **问题类型** 非线性偏好连接拟合、引文演化阶段识别、[[Matthew Effect in Academia|学术马太效应]]的时间边界测算。
> - **[[Unit of Analysis|分析单位]]** 跨学科单篇学术[[Document|文献]]及其署名学者的完整生涯发表记录。
> - **输入数据** 文献各年度的新增被引时间序列，以及署名学者在文献发表时刻的累积总引用量与 $h$ 指数。
> - **输出形式** 初始声誉加速度参数估计值 $\hat{c}_0$、临界交叠阈值 $\hat{c}_x$ 及分段引文增长概率密度函数。

> [!citation-card] 彼得森论声誉加速度与质量临界阈值
> 经典偏好连接模型假定文献获取后续引用的概率严格正比于现有被引量，忽视了新文献初入网络时度数为零的冷启动状态。知名学者在发表新作时，凭借长期建立的同行知名度赋予文稿显著的初始被引加速度 $c_0$。然而实证拟合证实，这一声誉红利仅在早期窗口有效，存在明确的交叠阈值 $c_x$。一旦累积引用越过 $c_x$，声誉溢价出清，长期引用演化完全贴合由学术质量决定的纯偏好连接基准。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 32–34)]]
>
> *Early citations are dominated by reputation-boosted preferential attachment, Π(c) ∝ c + c0, but beyond a critical threshold cx, citations transition to pure preferential attachment governed solely by the paper’s intrinsic scientific quality.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 突破了传统观点将学术马太效应视作终身无界累积的泛化假设，在数理结构上界定了声誉加速窗口与质量检验阶段的分界线。
> - **研究者判断** $c_x$ 阈值的具体数值受学科平均引文规模调节（例如物理学资深学者约为 40，而在年均引用较少的小众量化分支中绝对值会相应收缩）。
> - **有效性标准** 早期引文非线性拟合优度、双对数图上的斜率拐点显著性检验，以及跨资历群体的参数显著性比较。
> - **不声称回答的问题** 不用于测量极少数历经数十年才被学界发掘的睡美人文献，亦不直接评价同行评阅意见书的文本内容。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis]]。
> - **理论对话** 拓展了复杂网络中的经典 偏好连接理论，将其零度数冷启动困境形式化为声誉偏置参数；数理上细化了 [[Matthew Effect in Academia|学术马太效应]] 的衰减阶段。
> - **后续应用** 为学术期刊推荐算法、科技基金结项评审与代表作评价提供时间窗截断依据。

> [!dev-timeline] 方法演变
> - **2014 — 模型首创提出** 彼得森团队在《[[National Academy of Sciences|美国国家科学院]]院刊》（PNAS）发表长周期追踪成果，基于物理学高被引学者与青年学者数据确立分段方程与 $c_x$ 阈值。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, p. 32)]]
> - **2021 — 科学学理论体系整合** 王大顺与巴拉巴西在教材中将该模型作为解决学术引文冷启动机制与声望边界的标准分析工具。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 32–34)]]

---

> [!formula-set]- 公式链总览
> ```mermaid
> flowchart LR
>   A["学者历史学术声望"] --> B["初始加速度参数 c0"]
>   B --> C["早期声誉加速期 Π(c) ∝ c + c0"]
>   C --> D["累积被引越过临界阈值 cx"]
>   D --> E["质量接管期 纯偏好连接 Π(c) ∝ c"]
> ```

> [!formula-step] 步骤一　声誉加速度与临界阈值分段方程
> $$\Pi(c) \propto \begin{cases} c + c_0 & (c < c_x) \\ c & (c \ge c_x) \end{cases}$$
>
> **这个公式在做什么** 刻画单篇学术成果在累积获得 $c$ 次被引后，在下一时间步获取新引用的边际增长概率 $\Pi(c)$。公式将引文演化拆分为声誉加速主导期（$c < c_x$）与质量主导接管期（$c \ge c_x$）。[[Argument_Wang_Barabasi_2021_Cambridge_Unit01|(Wang & Barabási, 2021, pp. 32–34)]]
>
> **符号说明**
> - $c$：论著当前已累积获得的有效被引频次；
> - $\Pi(c)$：该论著在单位时间内获得下一次新增引用的条件概率；
> - $c_0$：学者在论著发表时所具备的外生初始学术声望加速度；
> - $c_x$：声誉红利出清的临界交叠阈值（顶尖资深学者 $c_x \approx 40$，青年学者 $c_x \approx 10$）。
>
> **数学直觉** 经典优先连接模型中被引概率正比于现有引用 $c$（内生累积），新成果在 $c=0$ 时面临起跑线困境。引入非零外生参数 $c_0$ 后，新作在 $c=0$ 时的初始获引概率由学者学术声望主导。当引用越过 $c_x$ 阈值后，内生积累量 $c$ 占据支配地位，曲线平滑过渡为纯偏好连接。
>
> > [!example]- 手算与阶段转换示例
> > 设定一名资深物理学家（$c_0 \approx 40$）与一名青年助理教授（$c_0 \approx 10$）分别发表一篇新论著：
> > - **发表初期的起跑线差距（$c = 0$）**
> >   - 资深学者新作边际获引概率：$\Pi_{senior}(0) \propto 0 + 40 = 40$；
> >   - 青年学者新作边际获引概率：$\Pi_{junior}(0) \propto 0 + 10 = 10$；
> >   - 初始起跑线获引概率比为 $\frac{40}{10} = 4$ 倍，知名学者作品具有极高的先发能见度。
> > - **早期发展期（$c = 5$）** 资深学者边际概率 $\Pi(5) \propto 5 + 40 = 45$；青年学者边际概率 $\Pi(5) \propto 5 + 10 = 15$。
> > - **突破临界阈值（$c \ge 40$）** 双方作品均累积获得 50 次引用（越过各自的 $c_x$ 阈值），资深学者作品边际概率回归为 $\Pi(50) \propto 50$，青年学者作品边际概率亦为 $\Pi(50) \propto 50$。两者长期边际获引速率完全等同，声望溢价出清，后续长期扩散纯粹由成果内在科学价值主导。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 初始初速度 $c_0$ | 衡量学者既有声誉为新成果提供的无形起跑线加速红利。 |
> > | 读法 | 临界阈值 $c_x$ | 标志声望外生效应消耗完毕、学术共同体转入实质质量检验的界线。 |
> > | 注意 | 质量检验独立性 | 初始声誉仅能将作品推过 $c_x$ 门槛，无法单独维持数百次以上的高被引长期增长。 |
>
> > [!geogebra] 动态参数模拟
> > - **横轴** 成果累积被引量 $c$（次）
> > - **纵轴** 边际引文增长率 $\Pi(c)$
> > - **滑块 c0** 学者先验学术声誉初速度（红色，调节声望加成强度）
> > - **红线** 声望红利窗口 $\Pi(c) \propto c + c_0$（$c < c_x$）
> > - **蓝线** 学术质量接管期 $\Pi(c) = c$（$c \ge c_x$）
> > - **紫虚线** 临界交叠阈值 $c_x$（声誉红利出清截断点）
> > - **灰虚线** 纯偏好连接质量基线 $\Pi(c) = c$
> >
> > 调节滑块可观察到：先验学术声誉赋予新成果显著的早期引文初速度，降低成果被同行忽略的风险；然而一旦累积引文跨越临界阈值 $c_x$，声誉促进项归零，成果引文轨迹完全贴合经典质量偏好连接基准线。
> >
> > ```geogebra
> > file: wiki/assets/geogebra/reputation_threshold_model.ggb
> > height: 480
> > toolbar: false
> > ```

---

> [!warning] 适用局限与理论边界
> - **引文规范生态依赖** 模型假定引用行为主要由真实的学术同行参考驱动；在存在不当互引或排他性引用小圈子时，声誉溢价可能在越过 $c_x$ 后继续非正常维系。
> - **团队合署[[Heterogeneity|异质性]]** 模型将声誉主要映射至单篇成果的单一代表学者，对多位不同资历学者深度协作时的声望归属划分需结合署名权重细化。
> - **学科引用基线差异** 不同领域的基础引文速度不同，在实务应用中需根据学科引用中位数对 $c_x$ 和 $c_0$ 作基准归一化。

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit01|Wang & Barabási (2021)]] — 结合引文动力学与物理学者实证数据，系统论证 Petersen 等人的声誉加速度与 $c_x$ 临界阈值模型。
