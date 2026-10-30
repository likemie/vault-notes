---
title: Relative Citation Normalization
aliases:
  - 相对引文标准化
  - 相对引文比值法
  - 相对引文标准化法
  - 篇均引文相对标准化
  - Relative Citation Indicator
  - Field-Normalized Citation Impact
summary: "科学计量学与科技评价领域用于消除学科差异与出版年级偏差的量化标准化方法；通过将特定论文的原始引文计数 $c$ 除以所属二级学科分类同年度发表论文的基线平均被引数 $\\langle c \\rangle$，输出无量纲相对影响力比值 $c_f = c / \\langle c \\rangle$，使跨学科、跨历史周期的学术成果影响力评估具备统计学可比性。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 11
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/indicator
related_concepts:
  - "[[Citation Distribution]]"
  - "[[Citation Disparity]]"
  - "[[Scientific Productivity]]"
  - "[[Big Science]]"
related_theories:
  - "[[Universality of Citation Distributions]]"
  - "[[Random Impact Rule]]"
related_methods:
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[Dashun Wang]]"
  - "[[Albert-László Barabási]]"
  - "[[Derek de Solla Price]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit07]]"
confidence: high
status: active
created: "2026-10-30"
updated: 2026-10-30
---

---

> [!def] Relative Citation Normalization
> 相对引文标准化（Relative Citation Normalization）是一种用于对异质性学术出版物影响力展开客观比较的文献计量学测度方法。其基本计算规则为：输入待评学术论著在特定时间节点获得的原始被引频次 $c$，以及该论文所属特定学科分类和出版年度的同批次全量学术出版物的平均被引数 $\langle c \rangle$；通过两者的算术比值运算，输出无量纲的相对被引指标 $c_f = c / \langle c \rangle$。若 $c_f > 1$，表明该成果超越了同领域同年出版物的平均关注水准；若 $c_f < 1$，则标识其学术影响低于所属学科同辈中枢。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, pp. 177–179)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 论文或成果组合在学术共同体中的相对学术影响（[[Citation Distribution]]）。
> - **问题类型** 跨学科评估、跨时期绩效比较、学者或机构跨领域综合学术实力评价。
> - **分析单位** 单篇论文、学者论著组合、大学或科研机构成果集合。
> - **输入数据** 论文绝对引文计数、所属细分学科分类标签代码（如 WoS 细分学科类别）、论文发表年份。
> - **输出形式** 连续型正实数标量（相对比值 $c_f$），或结合对数正态累积分布函数映射出的通用分位数位次（Percentile Rank）。

> [!citation-card] Radicchi 等人论相对引文比值的测量功能
> 直接对比来自不同学科的论文绝对引文计数毫无学术意义。通过将单篇论文的被引量除以同领域同年度全部出版物的平均被引量，我们建立起一种稳健的相对引文测度尺度。这一尺度完全消除了各个专业学科在参考文献长度与文献生产规模上的结构性差异，使任何两个不同学科、不同发表时期的学术论著之间能够实现客观且无偏的影响力比对。(Radicchi et al., 2008, pp. 17268–17269)
>
> *Direct comparisons of citation numbers for papers in different disciplines are essentially meaningless. Dividing a paper's citations by the average number of citations for papers in the same field and year yields a metric of relative impact, allowing an unbiased comparison between publications from different disciplines and epochs.*

---

> [!method-position] 方法定位
> - **构念效度** 相对引文比值高度敏感地剥离了学科体量效应与发表年份的时间窗口累积效应，能较好表征单篇论著在其对应学术亚领域中的同侪相对定位；但指标完全承袭引文本身的局限性，无法区分正面引用、批判性负面引用与形式性礼貌引用。
> - **研究者判断** 核心裁量权在于学科分类体系的选取与颗粒度划分。选用粗粒度一级学科（如“工程学”）与选用细粒度二级学科（如“航空航天工程”）计算出的基线均值 $\langle c \rangle$ 差异显著，直接影响最终比值结果。
> - **有效性标准** 经验有效性由统计物理学上的分布坍缩效应确证：在采用精确细分类别后，各学科相对引文比值的概率分布能够高度一致地收敛至单一通用的对数正态曲线。
> - **不声称回答的问题** 该方法不测度成果的社会经济实际效益，亦无法替代对学术论文创新实质与推演严谨性的同行质性审议。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis]]（文献计量分析）、科技指标分析（Scientometric Indicators）。
> - **前置步骤** 学术文献元数据清洗、跨库作者姓名与机构消歧、学科标准代码映射、同领域基准均值矩阵构建。
> - **变体与扩展** 
>   - **学科标准化引文影响力（Category Normalized Citation Impact, CNCI）** 广泛应用于 Clarivate 数据库平台的机构评价变体。
>   - **加权相对引文比值** 针对跨学科交叉论著，按其参考文献引证分布赋予不同学科权重后合成复合基准均值。

> [!dev-timeline] 方法演变
> - **1965 — 早期原始引文批判** 普赖斯发现不同学科文献引用密度相差巨大，警示绝对被引指标用于跨学科横向评聘存在严重制度陷阱。(Price, 1965, pp. 510–515)
> - **2008 — 相对比值与普适曲线建立** Radicchi、Fortunato 与 Castellano 正式提出用 $c_f = c / \langle c \rangle$ 实施归一化，证明该比值能将各学科分布统一至均值参数 $\mu \approx -0.27$、方差参数 $\sigma \approx 1.25$ 的通用对数正态模型。(Radicchi et al., 2008, pp. 17268–17272)
> - **2021 — 科学学跨领域比对推广** 王大顺与巴拉巴西系统总结相对引文标准化方法在比较历史经典论文与当代突破中的实践范例，确立其作为科学学基础度量工具的规范地位。[[Argument_Wang_Barabasi_2021_Cambridge_Unit07|(Wang & Barabási, 2021, pp. 177–180)]]

---

> [!formula] 计算公式与算法细节
> 设某一学术论著 $i$ 发表在年份 $t$，归属于细分学科类别 $s$。论著 $i$ 在观测时间点累积的原始引文频次记为 $c_i$。
> 
> 学科类别 $s$ 在出版年份 $t$ 所发表的所有 $N_{s,t}$ 篇学术论文构成的集合为 $S_{s,t}$。该学科年度组合同批次论文的平均被引数计算公式为：
> $$
> \langle c \rangle_{s,t} = \frac{1}{N_{s,t}} \sum_{j \in S_{s,t}} c_j
> $$
> 
> 则该论文的相对引文比值 $c_{f,i}$ 定义为：
> $$
> c_{f,i} = \frac{c_i}{\langle c \rangle_{s,t}}
> $$
> 
> 借助普适对数正态分布参数，该论文在全学科通用坐标系下的累积百分位位次可由下式积分求得：
> $$
> \text{Percentile}(c_{f,i}) = \int_0^{c_{f,i}} \frac{1}{\sqrt{2\pi}\sigma x} \exp\left(-\frac{(\ln x - \mu)^2}{2\sigma^2}\right) dx
> $$

> [!protocol] 操作步骤
> 1. **抽取候选论著元数据** 检索待评成果，提取其绝对被引次数 $c$、出版年份 $t$ 以及标引的完整学科分类代码。
> 2. **建立同侪基准集合** 在同源文献数据库中，抽取学科代码相同、出版年份严格一致的全量子集 $S_{s,t}$。
> 3. **计算基线均值** 排除无效记录后，求出该学科同年度论著的算术平均被引数 $\langle c \rangle_{s,t}$。
> 4. **求取无量纲比值** 执行算术相除运算得到 $c_f$。
> 5. **映射分位数位次** 对照全学科通用的对数正态分布基准参数，判定成果所处的相对分位层级。

---

> [!boundary]- 边界与局限
> - **长半衰期与短时间窗偏误** 对于发表年份较近的论著（如发表不足 2–3 年），学科基线被引数极低（接近 0 或 1），轻微的引文扰动会导致 $c_f$ 剧烈波动，丧失稳定性。该方法要求论文发表通常应满 3 至 5 年以上。
> - **跨学科分类重叠难题** 交叉前沿成果往往横跨多个不同学科，单一学科代码映射容易高估或低估基准均值，需配合多重赋权或引文级聚类算法修正。
> - **无法过滤引文异质动机** 算法将综述性引证、方法包引用与负面反驳性引用一视同仁赋予同等权重，需警惕单纯“唯指标化”对原创颠覆性研究的错杀。

---

## 使用此方法的研究

- [[Argument_Wang_Barabasi_2021_Cambridge_Unit07]]：运用相对引文标准化方法消除发育生物学（高被引基线）与航空航天工程（低被引基线）之间的跨学科测量鸿沟，证实 1978 年获得 32 次引用的计算几何论文相比 2002 年获得 100 次引用的生物医学论文具有更高的相对学术穿透力（pp. 177–180）。
