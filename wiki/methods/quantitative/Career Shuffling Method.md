---
title: Career Shuffling Method
aliases:
  - 生涯序列随机置换法
  - 生涯随机打乱法
  - 随机生涯零模型
  - Career Shuffling
  - Randomized Career Null Model
summary: "由 Roberta Sinatra et al. (2016) 提出的科学学生涯纵向引文序列建模与反事实检验方法；在完全保留学者个体各篇成果实际发表时间与生涯生产力曲线的前提下，对全生命周期所有产出成果的被引影响力进行无放回随机置换，以此构建影响力出现时间服从纯随机假设的反事实零模型，用于分离年龄与生产力对重大科学发现时机的影响。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 2
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/model
  - theme/scientometrics
  - theme/science-of-science
related_concepts: []
related_theories: []
related_methods:
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit02]]"
confidence: high
status: active
created: 2026-10-29
updated: 2026-10-29
---

---

> [!def] Career Shuffling Method
> 生涯序列随机置换法是一种用于甄别学者职业生涯中重大突破时机是否具有内在时间依赖性的反事实统计建模技术。该方法在绝对冻结研究者各篇论著真实发表时间与总发文量（生产力曲线）的前提下，对该学者一生发表论著的长期被引影响力指标（如发表后十年被引数 $c_{10}$）进行全局无放回随机置换，构建剥离了时间序列关联的随机零模型，通过比对真实经验曲线与置换反事实曲线的拟合程度判定突破时机的纯随机性。[[Argument_Wang_Barabasi_2021_Cambridge_Unit02|(Wang & Barabási, 2021, pp. 52–55)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 检验学术成果影响力在学者生命周期中的时序生成机制，评估年龄因素对重大科学突破的独立影响。
> - **问题类型** 反事实零模型构建、时间序列独立性检验与机制剥离。
> - **分析单位** 拥有完整发表记录且学术生涯跨越较长时间（如 20 年以上）的学者个体。
> - **输入数据** 学者经过高精度消歧的全量论著列表、各篇论著的确切发表年份以及固定观察窗口的标准化引文数据（$c_{10}$）。
> - **输出形式** 真实与随机置换条件下的巅峰产出学术年龄分布曲线 $P(t^*)$、相对发表位置累积分布 $P_>(N^*/N)$。

> [!citation-card] 西纳特拉等论生涯序列随机打乱法
> 为了探究学术生涯中的创造力是否完全受随机机制主导，我们在保持发文位置绝对不变的前提下随机抽取两枚图钉并交换其高度，反复迭代数千次从而获得每位学者学术生涯的随机打乱版本。打乱后的生涯既没有改变个体的发文总量，也没有改变总引用数或发文时机，唯一改变的只是这些成果发表的先后次序。[[Argument_Wang_Barabasi_2021_Cambridge_Unit02|(Wang & Barabási, 2021, p. 54)]]
>
> *Where does the shuffled career differ from the real one? The net productivity of the individual has not changed. The total impact of these papers didn't change either... Nor did we change the timing of the publications. The only thing that did change is the order in which these papers were published.*

---

> [!method-position] 方法定位
> - **构念效度** 成功将“发文活跃频次（生产力）”与“单篇成果内在质量（突破潜力）”在时间维度上实现正交分离。
> - **研究者判断** 选用十年被引窗口 $c_{10}$ 兼顾了长周期科学评价的稳健性与当代成果的覆盖率；对学者生涯年限设定门槛（如 20 年）以规避早期夭折职业的截断偏差。
> - **有效性标准** 随机置换抽样稳定性、反事实分布与真实分布的柯尔莫哥洛夫－斯米尔诺夫检验（KS 检验）。
> - **不声称回答的问题** 该方法用于检验影响力时序的随机性，不推断具体成果的微观选题因果机制，亦不直接评价学者之间的绝对能力高低。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis|科学计量分析]]、蒙特卡洛置换检验（Permutation Test）。
> - **前置步骤** 学者同名消歧算法（Author Name Disambiguation）、引文窗口标准化。
> - **变体与扩展** 相对位置均匀性检验法（Uniform Distribution Test of $N^*/N$）、跨艺术与电影领域的生涯置换模型。

---

> [!formula-set]- 公式链总览
> ```mermaid
> flowchart LR
>   A["学者全量论著序列 (t_i, c_10,i)"] --> B["冻结时间序列 t_i, 随机打乱 c_10,i"]
>   B --> C["识别置换序列中的最高被引位置 t*_rand"]
>   C --> D["聚合计算反事实概率分布 P_rand(t*)"]
>   D --> E["对比真实分布 P_real(t*) 判定随机性"]
> ```

> [!formula-step] 步骤一　反事实随机置换与时序提取
> $$\pi \in \mathfrak{S}_N, \quad \tilde{c}_{10, i} = c_{10, \pi(i)}, \quad t^*_{\text{rand}} = \arg\max_{t_i} \tilde{c}_{10, i}$$
>
> **这个公式在做什么** 对学者一生发表的 $N$ 篇论著的被引值进行全排列随机置换 $\pi$，将置换后的引文序列重新映射至原始发表时间点 $t_i$ 上，提取在随机假设下该学者产出代表作的学术年龄 $t^*_{\text{rand}}$。[[Argument_Wang_Barabasi_2021_Cambridge_Unit02|(Wang & Barabási, 2021, p. 54)]]
>
> **符号说明**
> - $N$ 学者毕生发表论著的总篇数。
> - $\mathfrak{S}_N$ 长度为 $N$ 的所有对称置换群集合。
> - $t_i$ 第 $i$ 篇论著发表时学者的学术年龄（以首篇发表为第 0 年）。
> - $c_{10, i}$ 第 $i$ 篇成果在发表后十年内累积的被引频次。

> [!formula-step] 步骤二　相对位置的均匀性累积分布检验
> $$P_>\left(\frac{N^*}{N}\right) = 1 - \frac{N^*}{N}$$
>
> **这个公式在做什么** 测算学者最具影响力的成果处于全部论著发表次序中的相对位次 $N^*/N$；若重大成果在发表序列中均匀随机涌现，则其大于特定相对位次的累积概率必然呈现斜率为负一的平直衰减线。[[Argument_Wang_Barabasi_2021_Cambridge_Unit02|(Wang & Barabási, 2021, p. 55)]]
>
> **符号说明**
> - $N^*$ 个人最高被引代表作在学者发表时间先后序列中的序号（$1 \le N^* \le N$）。
> - $P_>(N^*/N)$ 代表作相对位置大于给定比值的累积概率分布函数。

---

> [!method-app] 使用此方法的研究
> - **[[Argument_Wang_Barabasi_2021_Cambridge_Unit02]]** 运用生涯序列随机置换法对 2,856 位长期活跃的物理学家发表序列展开反事实模拟，证实代表作时序分布曲线的波峰完全受生产力曲线驱动，确立了随机影响法则。[[Argument_Wang_Barabasi_2021_Cambridge_Unit02|(Wang & Barabási, 2021, pp. 52–55)]]
