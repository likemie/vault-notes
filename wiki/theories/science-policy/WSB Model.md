---
title: WSB Model
aliases:
  - WSB模型
  - WSB引文模型
  - WSB引文动力学模型
  - Wang-Song-Barabási Model
  - Wang-Song-Barabasi Model
  - Minimal Citation Model
summary: "由 Dashun Wang、Chaoming Song 与 Albert-László Barabási (2013) 提出的单篇学术文献引文动力学最小模型；系统整合科学文献指数增长、优先连接、内生适应度与对数正态衰老机制，推导出单篇成果累积被引轨迹的封闭解析解与跨学科普适标度律，证明长程终极影响仅由相对适应度决定。"
type: theory
theory_field: "science-policy"
theory_related_count: 12
theory_related_level: 1
theory_related_stars: "⭐"
theory_related_color: "#dbeafe"
tags:
  - theme/science-policy
  - theme/network-science
  - theme/scientometrics
  - theme/citation-dynamics
related_concepts:
  - "[[Citation Distribution]]"
  - "[[Citation Disparity]]"
  - "[[Sleeping Beauty in Science]]"
related_theories:
  - "[[Price Cumulative Advantage Model]]"
  - "[[Bianconi-Barabási Model]]"
  - "[[Universality of Citation Distributions]]"
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Journal Impact Factor]]"
related_instruments: []
related_persons:
  - "[[Dashun Wang]]"
  - "[[Albert-László Barabási]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit09]]"
  - "[[Argument_Wang_Barabasi_2021_Cambridge]]"
confidence: high
status: draft
created: "2026-10-31"
updated: 2026-10-31
---

---

> [!theory-position] 理论定位
> - **解释对象** 单篇学术文献在发表后全生命周期内的引文演化轨迹、篇际引文轨迹的剧烈异质性，以及跨学科普适引文标度律的微观生成机制。
> - **理论问题** 经典的[[Price Cumulative Advantage Model|普赖斯累积优势模型]]与[[Bianconi-Barabási Model|边康尼-巴拉巴西模型]]虽然解释了宏观引文分布的重尾特征与后发成果的反超可能，却将单篇文献的获引能力视为无限持续的过程，忽略了文献生命周期中的注意力衰减与知识老化现象；同时，真实单篇文献的年度获引曲线呈现高度多样的波动形态，既有快速爆发后沉寂的跳跃衰减型，也有平稳获引型与迟滞达峰型，传统动力学模型无法用统一方程精确刻画这一微观层面的异质轨迹。
> - **理论类型** 复杂网络竞争生长理论与非平稳引文动力学生成模型。
> - **知识位置** 处于统计物理学、复杂网络科学、[[Bibliometric Analysis|科学计量学]]与科学学的交叉前沿，是连接微观注意力衰减与宏观引文分布演化的核心桥梁。

> [!claim] 核心判断
> 单篇学术文献的引文动态演化由科学系统指数增长、优先连接、内生适应度与对数正态衰老四大机制协同支配。新成果引用既有文献 $i$ 的微观概率方程表述为：
> 
> $$\Pi_i(t) \propto \eta_i c_i(t) P_i(t)$$
> 
> 文献随时间的注意力衰减由对数正态存活概率函数精确刻画：
> 
> $$P_i(t) = \frac{1}{\sqrt{2\pi}\sigma_i t} \exp\left(-\frac{(\ln t - \mu_i)^2}{2\sigma_i^2}\right)$$
> 
> 结合系统总文献规模的指数扩张方程，该模型解析推导出单篇文献在发表后 $t$ 年的累积被引频次闭式解：
> 
> $$c_i(t) = m \left(e^{\lambda_i \Phi\left(\frac{\ln t - \mu_i}{\sigma_i}\right)} - 1\right)$$
> 
> 式中 $\Phi(x)$ 为标准正态累积分布函数，$m$ 为系统平均参考文献数。该解确立了引文动力学的普适性：通过对时间与被引量进行无量纲重标度，所有学科与时期的异质引文曲线均坍缩至同一条标准正态累积分布曲线上；当 $t \to \infty$ 时，文献终极累积被引仅取决于相对适应度 $\lambda_i$，完全独立于紧迫性 $\mu_i$ 与寿命 $\sigma_i$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 210–217)]]

> [!geogebra] WSB 单篇文献引文动力学与终极影响模拟
> - **横轴** 文献发表后时间 $t$（年）
> - **纵轴** 单篇成果累积被引频次 $c_i(t)$（次）
> - **滑块 lambda** 调节文献相对适应度（$\lambda \in [0.5, 4.5]$），决定文献长程吸引力与终极被引天花板 $c_\infty = m(e^\lambda - 1)$
> - **滑块 mu** 调节紧迫性参数（$\mu \in [0.5, 3.0]$），控制文献进入同行视野的早晚与获引达峰时点 $t_{\text{peak}} = \exp(\mu - \sigma^2)$
> - **滑块 sigma** 调节寿命/衰老参数（$\sigma \in [0.4, 1.8]$），控制注意力衰退速率与峰值后半衰期跨度
> - **参照虚线** 终极引文影响渐近上限 $c_\infty = m(e^\lambda - 1)$，揭示终极影响对时间参数的独立特征
> 
> ![[wiki/assets/geogebra/wsb_citation_model.ggb]]

---

> [!theory-origin] 提出者如何形成理论
> - **提出者与原始文本** [[Dashun Wang|王大顺]]（Dashun Wang）、宋朝鸣（Chaoming Song）与[[Albert-László Barabási|艾伯特-拉斯洛·巴拉巴西]]（Albert-László Barabási）于 2013 年在 Science 发表研究 *Quantifying Long-Term Scientific Impact*，正式确立单篇成果引文动力学最小模型（WSB 模型）。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 210–213)]]
> - **原初问题** 科学界普遍使用短期被引指标（如两年期[[Journal Impact Factor|期刊影响因子]]）评估成果价值，但个体成果的引文轨迹极其复杂分散；研究者面临的核心难题在于，能否超越宏观稳态引文分布统计，构建能够准确刻画并预测任意单篇文献全周期引文轨迹的微观生成模型。
> - **理论资源与材料** 理论吸收了普赖斯的优先连接理论、边康尼-巴拉巴西的网络适应度模型，以及信息计量学关于文献老化的经验观测。实证分析基于《物理评论》（Physical Review）自 1893 年创刊以来的百年全量引文网络大数据，以及涵盖自然科学各领域的跨学科期刊数据库。
> - **形成路径** 研究团队识别出驱动成果获引的四个基本机制：系统文献指数扩张、基于存量的优先连接、反映内生学术质量的适应度，以及由对数正态衰老概率支配的注意力衰减。将四大机制整合进连续时间主方程并求出解析解，推导出三参数引文轨迹公式。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 210–213)]]

---

> [!entry-map] 关键概念与理论构件
> 
> | 构件 | 类型 | 在理论中的功能 |
> |:-----|:-----|:--------------|
> | **相对适应度（$\lambda_i$）** | 变量参数 | 刻画文献内生学术价值与吸引同行引用的相对竞争力，在时间无穷大时唯一决定终极引文量。 |
> | **紧迫性（$\mu_i$）** | 变量参数 | 决定文献被学术共同体关注与吸收的时间尺度，直接调控引文增长率达到峰值的早晚。 |
> | **寿命参数（$\sigma_i$）** | 变量参数 | 刻画学术共同体对文献注意力衰减的持续跨度，数值越大代表成果被引的衰老过程越平缓长久。 |
> | **对数正态存活概率（$P_i(t)$）** | 机制函数 | 表征学术同行对特定成果的引用记忆与使用衰减过程，解释文献获引概率随时间推移的必然归零。 |
> | **普适缩放函数（$\Phi(\tilde{t})$）** | 宏观规律 | 将异质引文轨迹映射为标准正态累积分布，证明看似分散随机的个体引文行为受统一动力学法则支配。 |

---

> [!formula-step] 模型动力学推导与解析结构
> 
> 设系统文献总规模随时间呈指数增长 $N(t) = N_0 e^{\beta t}$，平均每篇新论著包含 $m$ 条参考文献。在时刻 $t$，系统新增文献引用既有文献 $i$ 的微观概率 $\Pi_i(t)$ 满足：
> 
> $$\Pi_i(t) = \frac{\eta_i c_i(t) P_i(t)}{\sum_j \eta_j c_j(t) P_j(t)}$$
> 
> 式中 $\eta_i$ 为文献固有适应度，$c_i(t)$ 为累积被引量，$P_i(t)$ 为发表后经过时间 $t$ 的对数正态老化概率：
> 
> $$P_i(t) = \frac{1}{\sqrt{2\pi}\sigma_i t} \exp\left(-\frac{(\ln t - \mu_i)^2}{2\sigma_i^2}\right)$$
> 
> 文献 $i$ 的被引增长率主方程写为：
> 
> $$\frac{dc_i(t)}{dN} = m \frac{\Pi_i(t)}{\sum_j \Pi_j(t)}$$
> 
> 通过变量代换求解该非线性微分方程组，最终得到单篇文献的累积引文轨迹解析解：
> 
> $$c_i(t) = m \left(e^{\lambda_i \Phi\left(\frac{\ln t - \mu_i}{\sigma_i}\right)} - 1\right)$$
> 
> 其中 $\Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^x e^{-y^2/2} dy$ 为标准正态累积分布函数，$\lambda_i = \eta_i / A$ 为无量纲相对适应度。定义重标度时间 $\tilde{t}_i = \frac{\ln t - \mu_i}{\sigma_i}$ 与重标度引文 $\tilde{c}_i = \frac{\ln(1 + c_i(t)/m)}{\lambda_i}$，方程严格坍缩为：
> 
> $$\tilde{c}_i = \Phi(\tilde{t}_i)$$
> 
> 该结论在数学上确立了引文动力学的全域普适性。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 211–213, 262–263)]]

---

> [!warrant] 终极影响（Ultimate Impact）与期刊声誉的独立分离
> 当考察时间跨度趋于无穷大（$t \to \infty$）时，标准正态累积分布函数趋近于极限值 $\Phi(\infty) = 1$。文献在其整个学术生命周期内所能获得的全部被引总数（终极影响 $c_\infty$）表达为：
> 
> $$c_i^\infty = m (e^{\lambda_i} - 1)$$
> 
> 该数学推导揭示了一项根本性法则：决定文献长程学术影响力的唯一起决定性作用的内在参数是相对适应度 $\lambda_i$；紧迫性参数 $\mu_i$ 与寿命参数 $\sigma_i$ 仅调节获引的短期速率与波形，不改变长程总累积被引规模。对发表在不同影响因子期刊（Cell、PNAS、PRB）上但具备相近适应度（$\lambda \approx 1$）的文献进行长达二十年的追踪证实，顶尖名刊论著仅在发表后前两到四年享有暂时的获引领先，至第二十年时各类期刊成果的累积被引分布高度重合，最终均吻合于由适应度预测的理论值 $c_\infty \approx 51.5$。这证明成果长程价值取决于内容本身的适应度，期刊品牌效应随时间流逝完全消退。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 214–217)]]

---

> [!limits] 理论边界与适用条件
> - **参数静态性假定** 模型假定成果的内在适应度 $\lambda_i$ 在发表之初便已固定且全生命周期保持恒定，未囊括后续跨学科新范式重塑所诱发的适应度大幅提升过程。
> - **非典型轨迹的偏离限制** 模型以单峰跳跃衰减为主体架构，无法直接拟合具有双峰特征的复杂成果（如经历二次复苏的超导理论论著）以及超长休眠后复苏的[[Sleeping Beauty in Science|睡美人现象]]，处理此类文献需将老化函数扩展为多峰混合存活概率。
> - **前瞻预测的时间窗门槛** 模型利用早期被引数据拟合参数并预测长程影响时，前两年预测误差较大；训练窗口需延长至发表后五年以上方能形成高度收紧的预测置信包络。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 213–219)]]

---

## 围绕理论形成的命题

> [!claim] 命题一：引文轨迹的多样性根源于适应度、紧迫性与寿命的三维正交组合
> 个体文献展现出的引文演化曲线虽然在形态上高度分异，本质上均是三维参数空间 $(\lambda_i, \mu_i, \sigma_i)$ 的特定映射。紧迫性控制获引达峰时序，寿命决定获引衰减半衰期，相对适应度决定整体振幅，三者正交独立运作，生成了从昙花一现到恒久发光的全部经验轨迹。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 211–214)]]

> [!claim] 命题二：微观引文动力学在宏观尺度上展现出严格的跨学科普适标度律
> 尽管不同学科在发表习惯、文献半衰期与团队合作规模上存在显著差异，一旦将单篇文献的自然时间与被引计数按其内生参数进行重标度，不同学科、不同时期的数万篇文献均在统计上严格重合于标准正态累积分布曲线，证实学术同行集体引用机制遵循统一的复杂网络演化规律。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 212–214)]]

> [!claim] 命题三：短期引文窗口与期刊层级指标无法代表文献的长程终极学术价值
> 由于短期被引严重受制于紧迫性参数 $\mu_i$ 与载文期刊的短期曝光优势，以发表后两年被引为基础的评价指标与成果长程价值存在系统性错位；长程学术影响严格由相对适应度 $\lambda_i$ 决定，不同层级期刊刊载的高适应度文献在二十年后展现出完全均等的累积被引分布。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 216–217)]]
