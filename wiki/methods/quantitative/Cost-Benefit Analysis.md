---
summary: "一种系统评估公共政策、工程项目与投资方案经济合理性的量化分析方法；通过将全部直接与间接收益与成本统一折算为货币现值并计算净现值或收益成本比，在新公共管理中被广泛用于微观决策，但因其静态已知假设与对激进创新外溢的系统性低估而在使命政策理论中受到深刻批判。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 9
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - method/policy-evaluation
  - welfare-economics
  - cost-benefit-analysis
  - public-policy
  - new-public-management
related_concepts:
  - "[[New Public Management]]"
  - "[[Counterfactual]]"
  - "[[Paradigm]]"
  - "[[Hypothesis]]"
  - "[[Grand Challenges]]"
  - "[[Market Failure]]"
  - "[[Lead-and-Learn Paradigm]]"
related_theories: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Kattel_Mazzucato_2018_ICC]]"
related_methods:
  - "[[Analytic Framework]]"
confidence: high
status: active
created: 2026-10-03
updated: 2026-10-03
title: Cost-Benefit Analysis
aliases:
  - 成本收益分析
  - 成本效益分析
  - CBA
  - 成本–收益分析
  - 成本效益分析法
---

# Cost-Benefit Analysis

---

## 方法定义与公式模型

> [!def] 核心定义
> **成本收益分析（Cost-Benefit Analysis, CBA / 成本效益分析）**是一种基于新古典福利经济学与微观经济学理论的规范性政策与项目量化评估方法；它通过将特定公共政策、基础设施投资或技术方案在整个生命周期内所引发的全部直接与间接、有形与无形的社会收益（Benefits）与社会成本（Costs）系统识别并折算为统一的货币度量单位，进而利用折现率计算其**净现值（Net Present Value, NPV）**或**收益成本比（Benefit-Cost Ratio, BCR）**，用以判断该干预是否符合卡尔多–希克斯改进（Kaldor-Hicks Improvement）与经济效率最大化准则（Boardman et al., 2018）。在[[New Public Management|新公共管理]]（NPM）浪潮中，CBA 成为各国政府控制财政开支与审批微观项目的标准金科玉律。[[Argument_Kattel_Mazzucato_2018_ICC|(Kattel & Mazzucato, 2018, p. 798)]]

> [!math] 核心数学模型与决策准则
> **1. 净现值模型（Net Present Value, NPV）**
> $$NPV = \sum_{t=0}^{T} \frac{B_t - C_t}{(1 + r)^t}$$
> 其中，$B_t$ 为第 $t$ 期产生的全部社会收益货币化总额，$C_t$ 为第 $t$ 期的社会成本总额，$r$ 为社会贴现率（Social Discount Rate），$T$ 为评估期年限。当 $NPV > 0$ 时，项目在经济上可行。
>
> **2. 收益成本比（Benefit-Cost Ratio, BCR）**
> $$BCR = \frac{\sum_{t=0}^{T} \frac{B_t}{(1 + r)^t}}{\sum_{t=0}^{T} \frac{C_t}{(1 + r)^t}}$$
> 当 $BCR > 1$ 时，单位成本带来的社会收益大于投入，项目具有经济合理性。

---

## 经典操作流程

> [!process] 成本收益分析的标准实施链条
> ```mermaid
> flowchart LR
>     Scope["1. 界定干预范围<br>与基准对照组（Counterfactual）"] --> ID["2. 全面识别物理影响<br>（直接与间接产出/外部性）"]
>     ID --> Monetize["3. 货币化定价与估值<br>（市场价格/影子价格/WTP）"]
>     Monetize --> Discount["4. 选定社会贴现率<br>折算 NPV 与 BCR"]
>     Discount --> Sens["5. 敏感性分析与风险检验<br>（参数鲁棒性评估）"]
> ```
> 1. **[[Counterfactual|反事实]]界定** 确定政策干预存在与不存在时的两种情境基准。
> 2. **影响识别** 列出项目在环境、健康、经济与时间上的全部正负效应。
> 3. **影子价格度量** 利用支付意愿（Willingness to Pay, WTP）或避免成本法将非市场价值（如生命统计价值、洁净空气）转化为货币数值。
> 4. **贴现折现** 运用社会贴现率消除跨期资金的时间价值差异。
> 5. **敏感性检验** 测试贴现率波动与极端情境下的决策稳健性。

---

## 科技政策中的方法批判与局限

> [!tension-table] [[New Public Management|新公共管理]]微观 CBA 评估 vs. 使命导向动态演化评估深度对比
>
> | 评估维度 | 传统微观成本收益分析（CBA / NPM [[Paradigm\|范式]]） | 使命导向动态演化评估（Lead-and-Learn 范式） |
> |:---|:---|:---|
> | **基本[[Hypothesis\|假设]]** | 假设未来技术与市场结果的概率分布已知且可测。 | 承认创新充满根本不确定性（Fundamental Uncertainty）。 |
> | **视野盲区** | **青蛙视角（Frog View）** 局限于单个孤立项目的短期合规。 | **全景演化视角** 关注跨部门投资组合与全系统结构跃迁。 |
> | **对外溢效应处理** | 将非预期外溢视为分析误差或次要副产品，难以量化。 | 将跨领域技术与制度外溢视为使命政策的核心演化资产。 |
> | **贴现惩罚机制** | 高贴现率使得 20–30 年后的气候与健康长期收益几乎归零。 | 强调代际正义与不可逆生态红线，摆脱机械金融贴现。 |
> | **容错与试错** | 零容忍失败；项目受挫被判定为 CBA 预测失误与行政失职。 | 将探索性失败视为组织积累动态能力的必要学习成本。 |

> [!citation-card] 成本收益分析在应对[[Grand Challenges|重大挑战]]中的青蛙视角异化
> 传统新公共管理改革强行将所有公共决策塞入狭隘的成本收益[[Analytic Framework|分析框架]]，形成了只盯住微观可见指标的“青蛙视角”（Frog View）。面对颠覆性创新与 21 世纪重大社会挑战，CBA 假设事前的成本与产出能够被精确量化预测，这在本质上抹杀了前沿探索的根本不确定性，导致公共机构不敢承担高风险探索，系统性扼杀具有巨大长期社会外溢的突破性使命。[[Argument_Kattel_Mazzucato_2018_ICC|(Kattel & Mazzucato, 2018, pp. 797–798)]]
>
> *Innovation policy needs to shift from the existing support-and-measure approach (find [[Market Failure]]; fix it with a support instrument; and measure the impact with CBA) to a [[Lead-and-Learn Paradigm|lead-and-learn approach]]... CBA assumes static efficiency and predictable outcomes, inherently penalizing bold, open-ended, high-uncertainty missions.*

---

