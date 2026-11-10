---
title: Prospective Citation Analysis
aliases:
  - 引文前瞻分析
  - 引文前瞻测度法
  - 前瞻引文分析
  - 历时引文分析
  - Diachronous Citation Analysis
  - Citations To Approach
summary: "科学计量学中测度成果全生命周期影响力的长程队列追踪方法；以特定年份发表的文献队列为观测锚点，历时追踪其在后续数十年中逐年获取的新引文时序，测度科学界对特定成果的集体记忆保持与衰减速率；为 WSB 引文动力学模型、引文失效期测定与终身学术影响力前瞻预测的基石方法（Wang & Barabási, 2021）。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 22
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/model
  - theme/scientometrics
  - theme/citation-dynamics
  - theme/science-of-science
related_concepts:
  - "[[Document]]"
  - "[[Ultimate Impact]]"
  - "[[Citation Expiration Date]]"
  - "[[Sleeping Beauty in Science]]"
  - "[[Second Act in Science]]"
  - "[[Unit of Analysis]]"
  - "[[Construct Validity]]"
  - "[[Citation Prediction Envelope]]"
  - "[[Emergence]]"
related_theories:
  - "[[WSB Model]]"
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Confidence Interval]]"
  - "[[Prediction Interval]]"
  - "[[Retrospective Citation Analysis]]"
  - "[[Journal Impact Factor]]"
  - "[[Ordinary Least Squares]]"
related_instruments: []
related_persons:
  - "[[Dashun Wang]]"
  - "[[Albert-László Barabási]]"
  - "[[Chaoming Song]]"
related_facts:
  - "[[Web of Science]]"
  - "[[Scopus]]"
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit09]]"
confidence: high
status: active
created: 2026-11-02
updated: 2026-11-11
---

---

> [!def] Prospective Citation Analysis
> 引文前瞻分析（Prospective Citation Analysis，又称历时引文分析 Diachronous Citation Analysis 或 Citations To 进路）是一种以成果发表队列为基准轴追踪其全生命周期被引演化轨迹的[[Bibliometric Analysis|文献计量学]]量化方法。其核心操作为：固定特定年份 $t_0$ 发表的学术[[Document|文献]]队列，历时追踪其在后续各个年份（$t = t_0 + \tau$）所获得的新增被引频次与累积增长轨迹，从而获得条件概率分布 $P_{\text{prosp}}(\tau)$ 与累积被引曲线 $c(t)$。该方法用以表征科研成果在科学共同体中的“集体记忆（Collective Remembrance）”保持、注意力衰减速率、达峰周期以及长程[[Ultimate Impact|终极学术影响力]]。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 204–205)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 单篇或队列学术成果的被引生命周期、跳跃衰减峰值时段、[[Citation Expiration Date|引文失效期]]、微观适应度 $\lambda$ 以及全生命周期总引用量。
> - **问题类型** 测度学术影响力的动态演变、拟合非线性引文主方程、识别[[Sleeping Beauty in Science|睡美人文献]]与[[Second Act in Science|二次激活]]轨迹，以及前瞻推演未来数十年的引文[[Confidence Interval|置信区间]]包络。
> - **[[Unit of Analysis|分析单位]]** 单篇学术论著、特定年度发表的整批学科出版物队列、期刊创刊成果队列。
> - **输入数据** 具备连续数十年跨期追踪能力的标准化引文数据库全记录（如 [[Web of Science]]、[[Scopus]]）。
> - **输出形式** 年度新增被引轨迹拟合曲线、累积被引增长解析解、无量纲正态累积分布主曲线、动态预测包络锥体。

> [!citation-card] [[Dashun Wang|王大顺]]与[[Albert-László Barabási|巴拉巴西]]论前瞻引文分析的动态价值
> 前瞻法研究特定年份发表的成果在后续历程中随时间推移获得的被引分布。该方法代表了一种集体测度，量化了一篇特定论著随时间推移如何被科学界所记住。因此，前瞻法更适用于理解学术影响力如何随时间发生改变，构成了理解引文失效期与构建微观引文动力学模型的基石。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 204–205)]]
>
> *The prospective (citations to) approach studies the distribution of citations gained over time by papers published in a given year... representing a collective measure, quantifying how a particular paper is remembered over time. Hence, the prospective approach is more useful for understanding how impact changes with time.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 直接追踪知识在同行网络中的吸收与存留时序，是测度文献长程真实学术影响力的黄金标准，不受后续历史文献扩张的统计贴现扭曲。
> - **研究者判断** 训练观测窗口长度设定（通常需 5–10 年以消除早期随机扰动）、追踪时长截断阈值、学科均值重标度方案。
> - **有效性标准** 队列跨期跟踪的完整性、无引文截断丢失、微观主方程拟合优度与前瞻[[Prediction Interval|预测区间]]覆盖率。
> - **不声称回答的问题** 单纯依靠早期一至两年的短窗口前瞻数据无法准确推断成果的终极学术地位；前瞻引文计数受制于领域出版惯例，不可直接开展未归一化的跨学科绝对值比较。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis|文献计量分析]]（Bibliometric Analysis）、时序引文动力学建模（Citation Dynamics Modeling）。
> - **对偶方法** [[Retrospective Citation Analysis|引文回溯分析]]（基于施引截面参考文献统计的对应进路）。
> - **核心支撑理论** 王-宋-巴拉巴西引文动力学模型（[[WSB Model|Wang-Song-Barabási Model]]）。
> - **核心应用衍生物**
>   - **引文失效期测算** 识别成果完全停止获取新引文的时序临界点（Stringer et al., 2008）；
>   - **[[Citation Prediction Envelope|引文预测包络]]** 基于贝叶斯与极大似然估计生成长程未来轨迹置信锥体（Wang et al., 2013）。

> [!dev-timeline] 方法演变
> - **1988 — 中本秀之规范历时分析术语** 中本秀之确立历时（Diachronous）分析的标准框架，指明其以成果出版年为唯一起点。
> - **2004 — 格兰泽尔推导动态模型** 沃尔夫冈·格兰泽尔推导历时引文动力学生成过程，验证其对数正态时间衰减特性。
> - **2008 — 斯特林格确立引文失效期** 斯特林格等通过长程追踪证实常规成果在特定年限后完全停止获引并进入终身稳态。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Stringer et al., 2008; via Wang & Barabási, 2021, pp. 205–206)]]
> - **2013 — 王大顺、[[Chaoming Song|宋超明]]与巴拉巴西创立 WSB 模型** 整合优先连接、对数正态衰老与相对适应度，求得前瞻累积引文主方程封闭解析解。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang et al., 2013; via Wang & Barabási, 2021, pp. 210–213)]]

---

> [!formula-set]- 公式链总览
> ```mermaid
> flowchart LR
>   A["固定队列出版年份 t_0"] --> B["历时追踪逐年获引 Δc_i(t)"]
>   B --> C["对数正态存活概率 P_prosp(τ) 拟合"]
>   C --> D["WSB 动力学累积被引解析闭式解"]
>   D --> E["终极学术影响极限 c_∞ 求解与预测包络"]
> ```

> [!formula-step] 步骤一　前瞻获引存活概率函数
> 单篇学术文献在发表后经历时长 $\tau$ 时获取新引文的注意力保持概率服从对数正态分布：
>
> $$P_{\text{prosp}}(\tau) = \frac{1}{\sqrt{2\pi}\sigma_i \tau} \exp\left(-\frac{(\ln \tau - \mu_i)^2}{2\sigma_i^2}\right)$$
>
> **这个公式在做什么** 输入成果发表后的经历年限 $\tau$，输出该成果在第 $\tau$ 年依然被同行群体查阅并引用的相对存活几率。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang et al., 2013; via Wang & Barabási, 2021, p. 211)]]
>
> **符号说明**
> - $\tau$ 为成果自发表以来经历的实际年数（$\tau = t - t_0$）；
> - $\mu_i$ 为紧迫性参数（调控获引达峰的早晚）；
> - $\sigma_i$ 为寿命参数（调控引文半衰期的长短）。
>
> **数学直觉** 成果在发表初期由于同行关注[[Emergence|涌现]]出现快速攀升，但随着认知热点转移与后续文献堆叠，注意力以对数时间呈现加速衰退。

> [!formula-step] 步骤二　前瞻累积被引封闭解析解与终极影响
> 结合优先连接、文献总规模指数增长与对数正态存活概率，单篇文献在发表 $t$ 年后的全周期累积被引解析闭式解为：
>
> $$c_i(t) = m \left(e^{\lambda_i \Phi\left(\frac{\ln t - \mu_i}{\sigma_i}\right)} - 1\right)$$
>
> 当考察时间趋于无穷大时，高斯累积分布函数 $\Phi(z) \to 1$，成果终身总被引量稳态解为：
>
> $$c_\infty = m(e^{\lambda_i} - 1)$$
>
> **这个公式在做什么** 证明成果的全生命周期总影响 $c_\infty$ 唯一地取决于其内在相对适应度 $\lambda_i$，完全独立于载文期刊的[[Journal Impact Factor|影响因子]]与时间衰老参数。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang et al., 2013; via Wang & Barabási, 2021, pp. 211–217)]]

> [!formula-reading] 前瞻分析的方法特性与注意事项
> | 维度 | 要点 | 说明 |
> |---|---|---|
> | 优势 | 真实影响测度 | 独立追踪每篇成果的真实获引轨迹，排除了文献库整体指数增长的统计贴现扭曲。 |
> | 优势 | 终身影响可测 | 能够通过早期时序参数准确反演成果的终身总被引量与达峰时间。 |
> | 局限 | 数据长程要求 | 必须依赖长时间跨度（10 年以上）的队列追踪，无法在成果刚发表时直接产出经验稳态结果。 |

---

> [!software-impl] 软件实现
> - **核心环境** Python (`pandas`, `numpy`, `scipy.optimize`)。
> - **实现流程** 固定文献出版年份 $t_0$，构建面板数据提取逐年被引计数，使用非线性[[Ordinary Least Squares|最小二乘法]]或极大似然法估计 $\lambda_i, \mu_i, \sigma_i$ 参数。

> [!formula] Python 计算骨架
> ```python
> import numpy as np
> from scipy.special import erf
> from scipy.optimize import curve_fit
> 
> def wsb_cumulative_citations(t, m, lambd, mu, sigma):
>     """WSB 前瞻累积引文闭式模型函数"""
>     Phi = 0.5 * (1 + erf((np.log(t) - mu) / (np.sqrt(2) * sigma)))
>     return m * (np.exp(lambd * Phi) - 1)
> 
> def fit_prospective_trajectory(years_since_pub, actual_cumulative_cites, m=30):
>     """依据前瞻追踪时序拟合成果动力学参数"""
>     popt, _ = curve_fit(
>         lambda t, lambd, mu, sigma: wsb_cumulative_citations(t, m, lambd, mu, sigma),
>         years_since_pub, actual_cumulative_cites,
>         p0=[1.0, 1.0, 1.0], bounds=(0, [10.0, 5.0, 3.0])
>     )
>     lambd_fit, mu_fit, sigma_fit = popt
>     c_inf = m * (np.exp(lambd_fit) - 1)
>     return lambd_fit, mu_fit, sigma_fit, c_inf
> ```

---

> [!method-fit] 适用判断
> - **适合使用** 评估单篇成果长程学术寿命、测定引文失效期、构建前瞻预测包络、检验期刊影响因子脱钩法则。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 205–219)]]
> - **谨慎使用** 早期 2–3 年训练窗口数据较为稀疏，易产生参数估计波动，建议保留至少 5–10 年早期观测窗口。
> - **不适合使用** 评估学者在当前时刻即时的跨领域文献搜寻范围，此类知识结构分析宜采用回溯法。

---

> [!method-limits] 方法局限
> - **偏误来源** 追踪时间窗口不足导致的右侧截断偏误；撤稿与纠错引发的历史时序突变。
> - **适用边界** 需要具备长程连续追踪能力的全量引文数据库。
> - **补救方式** 采用极大似然法与动态包络分析吸收未观测不确定性，或依托对偶贴现关系从大规模回溯数据中交叉验证。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Retrospective Citation Analysis]] | 对偶方法 | 以施引截面测度引用记忆的对应进路，二者通过系统文献增长贴现建立数理映射。 |
> | [[WSB Model]] | 支撑理论 | 以前瞻引文时序与对数正态衰老为物理假设，求解累积被引封闭解析解。 |
> | [[Ultimate Impact]] | 概念 | 前瞻法在演化时间趋于无穷大时求解的客观终极总被引量。 |
> | [[Citation Expiration Date]] | 概念 | 前瞻获引轨迹走向饱和并完全停止获得新引文的时序临界点。 |
> | [[Citation Prediction Envelope]] | 概念 | 依托早期前瞻时序数据向未来投射的动态置信区间锥体。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit09|Wang & Barabási (2021)]] — 在第 19.4 节至第 20 章系统应用前瞻引文分析，推导引文失效期、WSB 动力学模型与期刊脱钩法则（pp. 204–219）。
