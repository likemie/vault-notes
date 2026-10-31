---
title: Relative Citation Normalization
aliases:
  - 相对引文标准化
  - 相对引文比值法
  - 相对引文标准化法
  - 篇均引文相对标准化
  - Relative Citation Indicator
  - Field-Normalized Citation Impact
summary: "科学计量学与科技评价领域用于消除学科差异与出版年级偏差的量化标准化方法；通过将特定论著的原始引文计数 c 除以所属二级学科分类同年度发表成果的基线平均被引数 ⟨c⟩，输出无量纲相对影响力比值 cf = c / ⟨c⟩，使跨学科、跨历史周期的学术成果影响力评估具备统计学可比性。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 15
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/indicator
  - theme/scientometrics
  - theme/science-policy
related_concepts:
  - "[[Heterogeneity]]"
  - "[[Citation Distribution]]"
  - "[[Unit of Analysis]]"
  - "[[Document]]"
  - "[[Champ]]"
  - "[[Construct Validity]]"
related_theories:
  - "[[Universality of Citation Distributions]]"
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Confidence Interval]]"
  - "[[Disruption Index]]"
  - "[[Documentary Analysis]]"
related_instruments: []
related_persons:
  - "[[Derek de Solla Price]]"
  - "[[Dashun Wang]]"
  - "[[Albert-László Barabási]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit07]]"
confidence: high
status: active
created: "2026-10-30"
updated: 2026-10-31
---

---

> [!def] Relative Citation Normalization
> 相对引文标准化（Relative Citation Normalization）是一种用于对[[Heterogeneity|异质性]]学术成果影响力展开客观比较的[[Bibliometric Analysis|文献计量学]]测度方法。其基本计算规则为：输入待评学术论著在特定时间节点获得的原始被引频次 $c$，以及该成果所属特定学科分类和出版年度的同批次全量学术出版物的平均被引数 $\langle c \rangle$；通过两者的算术比值运算，输出无量纲的相对被引指标 $c_f = c / \langle c \rangle$。若 $c_f > 1$，表明该成果超越了同领域同年出版物的平均关注水准；若 $c_f < 1$，则标识其学术影响低于所属学科基线中枢。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, pp. 177–179)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 成果或成果组合在学术共同体中的相对学术影响（[[Citation Distribution]]）。
> - **问题类型** 跨学科评估、跨时期绩效比较、学者或机构跨领域综合学术实力评价。
> - **[[Unit of Analysis|分析单位]]** 单篇论著、学者论著组合、大学或科研机构成果集合。
> - **输入数据** 成果绝对引文计数 $c$、所属二级学科分类代码、成果出版年份 $t$。
> - **输出形式** 连续型正实数标量（相对比值 $c_f$），或结合通用对数正态累积分布函数映射出的百分位位次。

> [!citation-card] 相对引文比值的测量功能
> 直接对比来自不同学科的成果绝对引文计数缺乏学术意义。通过将单篇论著的被引量除以同领域同年度全部出版物的平均被引量，能够建立起稳健的相对引文测度尺度。这一尺度消除了各个专业学科在参考[[Document|文献]]长度与文献生产规模上的结构性差异，使两个不同学科、不同发表时期的学术论著之间能够实现客观且无偏的影响力比对。(Radicchi et al., 2008, pp. 17268–17269)
>
> *Direct comparisons of citation numbers for papers in different disciplines are essentially meaningless. Dividing a paper's citations by the average number of citations for papers in the same [[Champ|field]] and year yields a metric of relative impact, allowing an unbiased comparison between publications from different disciplines and epochs.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 相对引文比值剥离了学科体量效应与发表年份的时间窗口累积效应，表征单篇论著在其对应学术亚领域中的同侪相对定位；但指标承袭引文本身的局限性，无法区分正面引用、批判性负面引用与形式性引证。
> - **研究者判断** 核心裁量权在于学科分类体系的选取与划分细度。选用粗粒度一级学科（如“工程学”）与选用细粒度二级学科（如“航空航天工程”）计算出的基线均值 $\langle c \rangle$ 差异显著，直接影响最终比值结果。
> - **有效性标准** 经验有效性由统计物理学上的分布坍缩效应确证：在采用精确细分类别后，各学科相对引文比值的概率分布高度一致地契合单一通用的对数正态曲线。
> - **不声称回答的问题** 该方法不测度成果的社会经济实际效益，亦无法替代对学术成果创新实质与推演严谨性的同行质性审议。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis]]（文献计量分析）、科技指标分析（Scientometric Indicators）。
> - **前置步骤** 学术文献元数据清洗、跨库学者姓名与机构消歧、学科标准代码映射、同领域基准均值矩阵构建。
> - **变体与扩展** 
>   - **学科标准化引文影响力（Category Normalized Citation Impact, CNCI）** 广泛应用于 Clarivate 数据库平台的机构评价变体。
>   - **加权相对引文比值** 针对跨学科交叉论著，按其参考文献引证分布赋予不同学科权重后合成复合基准均值。

> [!dev-timeline] 方法演变
> - **1965 — 早期原始引文批判** [[Derek de Solla Price|普赖斯]]发现不同学科文献引用密度相差巨大，警示绝对被引指标用于跨学科横向评聘存在严重制度陷阱。(Price, 1965, pp. 510–515)
> - **2008 — 相对比值与普适曲线建立** Radicchi、Fortunato 与 Castellano 正式提出用 $c_f = c / \langle c \rangle$ 实施归一化，证明该比值能将各学科分布统一至均值参数 $\mu \approx -0.27$、方差参数 $\sigma \approx 1.25$ 的通用对数正态模型。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Radicchi et al., 2008, pp. 177–179)]]
> - **2021 — 科学学跨领域比对推广** [[Dashun Wang|王大顺]]与[[Albert-László Barabási|巴拉巴西]]系统总结相对引文标准化方法在比较历史经典论著与当代突破中的实践范例，确立其作为科学学基础度量工具的规范地位。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, pp. 177–180)]]

---

> [!formula-set]- 公式链总览
> ```mermaid
> flowchart LR
>   A["提取单篇原始引文 c 与同类集合"] --> B["计算学科同年度篇均基线 ⟨c⟩"]
>   B --> C["无量纲标准化运算 cf = c / ⟨c⟩"]
>   C --> D["映射通用对数正态主曲线 P(cf)"]
>   D --> E["确定超越全域同侪百分位与学术评价"]
> ```

> [!formula-step] 步骤一　相对被引比值测算
> $$
> c_{f,i} = \frac{c_i}{\langle c \rangle_{s,t}}, \quad \text{其中} \quad \langle c \rangle_{s,t} = \frac{1}{N_{s,t}} \sum_{j \in S_{s,t}} c_j
> $$
>
> **这个公式在做什么** 将待评成果 $i$ 在特定年份 $t$ 所获得的原始被引次数 $c_i$，除以该细分学科分类 $s$ 同年出版所有成果的篇均被引数 $\langle c \rangle_{s,t}$，输出无量纲相对被引比值 $c_{f,i}$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, pp. 177–179)]]
>
> **符号说明**
> - $c_i$：待评成果 $i$ 的绝对被引频次。
> - $S_{s,t}$：所属二级学科 $s$ 在出版年 $t$ 的全量学术出版物集合。
> - $N_{s,t}$：集合 $S_{s,t}$ 包含的出版物总量。
> - $\langle c \rangle_{s,t}$：学科同年度出版物的篇均被引基线。
>
> **数学直觉** 通过同侪基线除法消除学科环境容量与出版时间窗口的尺度差异，将各学科离散异质的引文刻度缩放至以 1.0 为均值锚点的统一相对标尺上。
>
> > [!example]- 手算示例
> > 假设 1978 年某计算几何成果获得 32 次引用，该学科当年篇均被引为 3.2 次，计算其相对比值：
> > $$c_f = \frac{32}{3.2} = 10.0$$
> > 另假设 2002 年某发育生物学成果获得 100 次引用，该学科当年篇均被引为 25.0 次，计算其相对比值：
> > $$c_f = \frac{100}{25.0} = 4.0$$
> > 结果显示，前者的相对学术穿透力（10 倍基准）显著高于后者（4 倍基准）。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 相对基准 | $c_f = 1$ 代表与学科同辈持平；$c_f > 1$ 标识超出平均水平；$c_f \ge 5$ 在绝大多数学科对应前 1% 成果。 |
> > | 读法 | 跨界可比 | 不同学科之间 $c_f$ 数值可直接进行横向排序与比较。 |
> > | 注意 | 分类敏感性 | 二级学科划分过宽或错配会导致分母 $\langle c \rangle$ 失真，进而扭曲相对评估结论。 |
> > | 注意 | 时滞约束 | 发表不足 3 年的新近成果因基线过低容易造成比值极端虚高，需设立合理时间窗。 |

> [!formula-step] 步骤二　通用对数正态主曲线坍缩与分位点映射
> $$
> P(c_f) = \frac{1}{\sqrt{2\pi}\sigma c_f} \exp\left(-\frac{(\ln c_f - \mu)^2}{2\sigma^2}\right)
> $$
>
> **这个公式在做什么** 将经由学科均值缩放后的无量纲相对引文指数 $c_f$ 代入全学科普适对数正态密度函数，输出特定相对学术影响力位置的概率密度值 $P(c_f)$，消除不同学科引文分布形态的异质性。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, pp. 177–179)]]
>
> **符号说明**
> - $c_f$：成果的无量纲相对被引比值（$c_f = c / \langle c \rangle$）；
> - $\mu$：通用对数正态分布的位置参数，全学科经验拟合值为 $\mu \approx -0.27$；
> - $\sigma$：通用对数正态分布的尺度参数，全学科经验拟合值为 $\sigma \approx 1.25$。
>
> **数学直觉** 引文累积微观过程受到随机乘性机制支配，导致各学科原始引文均呈偏斜形态；除以同领域篇均引文 $\langle c \rangle$ 消除了各学科独特的体量尺度因子，使原本离散割裂的各领域曲线完全坍缩重叠至同一条通用主曲线上。
>
> > [!example]- 手算示例
> > 以学科平均基准水准 $c_f = 1.0$ 为例：
> > $\ln(c_f) = \ln(1) = 0$。代入普适拟合参数 $\mu = -0.27, \sigma = 1.25$ 计算：
> > $$P(1.0) = \frac{1}{\sqrt{2\pi} \times 1.25 \times 1.0} \exp\left(-\frac{(0 - (-0.27))^2}{2 \times (1.25)^2}\right) \approx 0.3192 \times \exp(-0.0233) \approx 0.312$$
> > 结果表明在归一化主曲线上，位于学科基线平均值附近的出版物聚集密度最高。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 概率同构性 | 无论来自高被引的发育生物学还是低被引的航天工程，成果均服从相同分布。 |
> > | 读法 | 分位数对应 | 积分概率计算表明：$c_f \ge 1.0$ 超越约 60% 同类文献；$c_f \ge 5.0$ 稳定处于前 1% 极顶突破区间。 |
> > | 注意 | 极端肥尾平滑 | 被引破千的超级经典在极右端存在轻微幂律拖尾，纯对数正态在极右侧可能存在微幅低估。 |
>
> > [!geogebra] 动态参数模拟
> > - **横轴** 相对被引指数 $c_f = c / \langle c \rangle$
> > - **纵轴** 普适对数正态概率密度 $P(c_f)$
> > - **滑块 c** 成果绝对被引频次（蓝色滑块）
> > - **滑块 c0** 学科同年度篇均基准 $\langle c \rangle$（绿色滑块）
> > - **滑块 μ** 对数正态参数（紫色滑块，默认 -0.27）
> > - **滑块 σ** 对数正态参数（橙色滑块，默认 1.25）
> >
> > 拖动滑块调节不同学科篇均基准与成果原始被引，观察不同学科散乱分布如何坍缩至通用对数正态主曲线，以及绿色虚线（$c_f = 1.0$）标识的学科均值基准线。
> > ![[wiki/assets/geogebra/relative_citation_normalization.ggb]]

> [!software-impl] 软件实现
> - **数据来源** Web of Science 核心合集、Scopus、OpenAlex 或 Dimensions API。
> - **核心包或命令** Python（`pandas`, `scipy.stats`）、R（`bibliometrix`）。
> - **实现流程** 提取论著被引量与学科年份标签 $\rightarrow$ 分组聚合求取同年度篇均引文均值 $\rightarrow$ 比值运算生成 $c_f$ $\rightarrow$ 映射通用百分位。
> - **报告标准** 完整报告所选数据库名称、学科分类体系代码版本、引文统计截止时间节点以及样本纳入标准。

> [!formula] Python 计算骨架
> ```python
> import numpy as np
> from scipy.stats import lognorm
> 
> def relative_citation_impact(c: float, c_mean: float, mu: float = -0.27, sigma: float = 1.25):
>     """
>     计算相对引文标准化指数 cf 及在全学科通用对数正态主曲线中的位置
>     :param c: 成果绝对被引频次
>     :param c_mean: 所属细分学科同出版年的篇均被引基准
>     :param mu: 通用对数正态分布均值参数 (Radicchi et al., 2008)
>     :param sigma: 通用对数正态分布尺度参数
>     :return: 包含 cf, 概率密度 pdf 与超越同侪百分位的字典
>     """
>     if c_mean <= 0:
>         raise ValueError("学科基线篇均被引必须大于 0")
>     
>     # 1. 相对引文标准化比值
>     cf = c / c_mean
>     
>     # 2. 映射至普适对数正态主曲线
>     scale = np.exp(mu)
>     pdf_val = lognorm.pdf(cf, s=sigma, scale=scale)
>     percentile = lognorm.cdf(cf, s=sigma, scale=scale) * 100
>     
>     return {
>         "relative_citation": cf,
>         "probability_density": pdf_val,
>         "percentile": percentile,
>         "is_above_average": cf >= 1.0,
>         "is_top_1_percent": cf >= 5.0
>     }
> ```

> [!method-stack] 数据口径
> - **数据来源** 跨引文数据库（如 WoS 与 Scopus）基线均值不一致，不可混合计算。
> - **时间与范围** 建议选取发表满 3 至 5 年以上的成果群体以保证被引积累稳定。
> - **清洗与归属** 剔除勘误、撤稿与会议摘要；对跨学科交叉成果实施多学科分类基线加权。
> - **标准化** 以同细分学科、同出版年的全部同行评审研究长文为基线分子集合。

---

> [!method-fit] 适用判断
> - **适合使用** 跨学科科研绩效评估、跨历史时期学术代表作横向比对、跨学院科研资助遴选。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, pp. 177–180)]]
> - **谨慎使用** 涉及极新发表成果（不足 2 年）或样本稀疏的前沿微观冷门方向，需结合[[Confidence Interval|置信区间]]审慎评估。
> - **不适合使用** 无法用于推断单篇成果的方法严谨性、数据真实性，亦不能作为职称晋升的唯一定量裁决依据。

> [!ref-table]- 参照基准与阈值
> | 评价情境 | 参照值与相对被引阈值 | 来源 |
> |---|---|---|
> | 学科同侪平均基准水准 | 相对被引比值 1.0 倍基准 | [[Argument_Wang_Barabasi_2021_Cambridge_Unit07\|(Radicchi et al., 2008, p. 178)]] |
> | 全学科通用对数正态参数 | 拟合参数均值 -0.27 与方差 1.25 | [[Argument_Wang_Barabasi_2021_Cambridge_Unit07\|(Radicchi et al., 2008, p. 179)]] |
> | 顶尖前 1% 极高影响力成果 | 相对被引比值达 5.0 倍以上 | [[Argument_Wang_Barabasi_2021_Cambridge_Unit07\|(Wang & Barabási, 2021, p. 180)]] |
> | 1978 年计算几何成果 (32 引) | 相对被引比值 10.0 倍学科基准 | [[Argument_Wang_Barabasi_2021_Cambridge_Unit07\|(Wang & Barabási, 2021, p. 179)]] |
> | 2002 年发育生物学成果 (100 引) | 相对被引比值 4.0 倍学科基准 | [[Argument_Wang_Barabasi_2021_Cambridge_Unit07\|(Wang & Barabási, 2021, p. 179)]] |

---

> [!method-limits] 方法局限
> - **测量偏误** 分类体系依赖偏误；数据库对跨学科交叉论著归属的模糊性会导致基线分母失准。
> - **可比边界** 仅适用于具备规范引文网络的长线科技期刊成果；人文艺术与专著主导领域覆盖度有限。
> - **误用风险** 将 $c_f$ 比值绝对高低等同于科学内在价值，忽视方法性工具论著的高引虚高与综述溢价。
> - **补救方式** 结合代表作同行专家质性评议，配合复合指标（如[[Disruption Index|颠覆性指数]]）进行综合裁定。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Citation Distribution]] | 测量对象 | 相对引文标准化旨在客观测度成果在重尾引文网络中的相对位置。 |
> | [[Universality of Citation Distributions]] | 理论 | 相对引文标准化消解学科异质性并坍缩至对数正态分布的理论基石。 |
> | [[Bibliometric Analysis]] | 上位方法 | 相对引文标准化隶属于科技计量学[[Documentary Analysis\|文献分析]]指标工具箱。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit07|Wang & Barabási (2021)]] — 运用相对引文标准化方法消除发育生物学与航空航天工程之间的跨学科测量鸿沟，证实 1978 年获得 32 次引用的计算几何论著相比 2002 年获得 100 次引用的生物医学成果具有更高的相对学术穿透力（pp. 177–180）。
