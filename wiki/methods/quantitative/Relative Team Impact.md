---
title: Relative Team Impact
aliases:
  - 相对团队影响力
  - 相对团队影响力指标
summary: "由 Stefan Wuchty, Benjamin F. Jones 与 Brian Uzzi (2007) 提出的文献计量学指标，通过计算特定领域和年份内团队合作成果与单人成果的平均被引量比值，量化评估团队科研相对于单人独立科研的引文优势。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 19
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/indicator
  - theme/science-of-science
  - theme/team-science
  - bibliometrics
related_concepts:
  - "[[Response to Intervention]]"
  - "[[Team Science]]"
  - "[[Unit of Analysis]]"
  - "[[SOLO Taxonomy]]"
  - "[[Champ]]"
  - "[[Construct Validity]]"
  - "[[Internal Validity]]"
  - "[[Heterogeneity]]"
  - "[[Document]]"
  - "[[Scientific Productivity]]"
  - "[[Construct]]"
  - "[[Paradigm]]"
related_theories:
  - "[[Burden of Knowledge]]"
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Sample Size Determination]]"
related_instruments: []
related_persons:
  - "[[Stefan Wuchty]]"
  - "[[Benjamin F. Jones]]"
  - "[[Brian Uzzi]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit04]]"
confidence: high
status: active
created: "2026-10-30"
updated: 2026-10-30
---

---

> [!def] Relative Team Impact
> 相对团队影响力（Relative Team Impact, [[Response to Intervention|RTI]]）是测度团队科研成果相对于单人独立成果被引优势的量化比值指标。其计算规则为：在给定的学科领域与发表年份内，将团队署名成果的算术平均被引频次除以单人独立署名成果的算术平均被引频次，输出一个无量纲的相对比值。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 86)]]

> [!method-scope] 方法范围
> - **测量或估计对象** [[Team Science|团队科学]]（Team Science）生产模式相对于单人研究的引文溢价与学术影响力增益。
> - **问题类型** 比较、评价、描述与跨时序趋势测度。
> - **[[Unit of Analysis|分析单位]]** 学科领域年度切片、科研机构、国家或技术专利分类。
> - **输入数据** 出版物或专利的署名学者人数，以及统计窗口内的累计被引频次。
> - **输出形式** 正实数比值（RTI）。

> [!citation-card] 相对团队影响力的基准定义
> 相对团队影响力（RTI）代表团队署名成果所获得的平均被引次数除以同领域单人署名成果获得的平均被引次数。比值为 1 意味着团队与单人成果具有相当的影响力。折线呈现给定年份整个领域的算术平均 RTI。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 86)]]
>
> *The relative team impact (RTI) represents the mean number of citations received by team-authored work divided by the mean number of citations received by [[SOLO Taxonomy|solo]]-authored work in the same [[Champ|field]]. A ratio of 1 implies that team- and solo-authored work have comparable impact. The lines present the arithmetic average of RTI in a given year for the entire field.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** RTI 直接反映[[Bibliometric Analysis|文献计量学]]意义上的均值引文溢价，能够敏感捕捉宏观学术生产体系中知识组合方式对学术反响的结构性影响。
> - **研究者判断** 跨学科引文尺度的归一化基准、统计分析切片的时间窗口，以及是否剔除署名学者自引。
> - **有效性标准** [[Internal Validity|内部效度]]取决于自引剔除前后的估计稳健性；在剔除全部署名自引后，RTI 大于 1 的优势依然保持稳定，排除了多人合著自引膨胀的机械性干扰。
> - **不声称回答的问题** 该指标测度的是宏观聚合层面的平均引文差异，不能直接推断微观单项成果的科学真理性或个别团队内部的协作质量。

> [!method-stack] 方法层级
> - **上位方法** 文献计量学分析（Bibliometric Analysis）。
> - **前置步骤** 署名形态分类（单人独立 vs 多人合作）、学科分类匹配、引文窗口统计与自引清洗。
> - **变体与扩展** 极端引文倍率比值（如在被引达到 1,000 次以上的顶尖层级中团队成果相对单人成果的入选几率比）。

> [!dev-timeline] 方法演变
> - **2007 — 指标创立** 斯特凡·乌赫蒂（[[Stefan Wuchty]]）、[[Benjamin F. Jones|本杰明·F·琼斯]]（Benjamin F. Jones）与[[Brian Uzzi|布赖恩·乌齐]]（Brian Uzzi）在《科学》（*Science*）发表的成果中建立 RTI 指标，测算 1,990 万篇期刊论著与 210 万件专利，证实所有学科门类的团队论著均展现出持续高于单人成果的被引优势。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 85–86)]]

---

> [!formula-step] 步骤一　相对团队影响力测算
> $$\text{RTI}_{f, t} = \frac{\bar{c}_{\text{team}, f, t}}{\bar{c}_{\text{solo}, f, t}} = \frac{\frac{1}{N_{\text{team}, f, t}} \sum_{i \in \text{team}} c_i}{\frac{1}{N_{\text{solo}, f, t}} \sum_{j \in \text{solo}} c_j}$$
>
> **这个公式在做什么** 计算特定学科领域 $f$ 在发表年份 $t$ 中，团队合作成果的算术平均被引频次与单人独立成果的算术平均被引频次之比。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 86)]]
>
> **符号说明**
> - $\bar{c}_{\text{team}, f, t}$：学科 $f$ 在年份 $t$ 发表的所有团队成果（署名人数 $\ge 2$）的篇均被引。
> - $\bar{c}_{\text{solo}, f, t}$：学科 $f$ 在年份 $t$ 发表的所有单人成果（署名人数 $= 1$）的篇均被引。
> - $N_{\text{team}}, N_{\text{solo}}$：对应群组的成果总篇数。
>
> **数学直觉** 以同领域、同年份的单人产出作为基准锚点，通过比值运算消除学科引文习俗与时间积累长度的全局波动，提纯团队生产模式带来的超额引文收益。
>
> > [!example]- 手算示例
> > 假设某学科某年度共有 5 篇成果。团队成果共 3 篇，被引频次分别为 12、18、30 次，均值为 $(12+18+30)/3 = 20$；单人成果共 2 篇，被引频次分别为 6、14 次，均值为 $(6+14)/2 = 10$。代入公式得：$\text{RTI} = 20 / 10 = 2.0$。此结果表明团队成果的平均被引频次是单人独立成果的 2 倍（示例）。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | $\text{RTI} = 1$ | 团队成果与单人成果的平均被引水平完全一致，团队生产未展现额外引文溢价。 |
> > | 读法 | $\text{RTI} > 1$ | 团队成果展现出系统性被引优势；数值越大，团队合作的相对引文溢价越高。 |
> > | 读法 | $\text{RTI} < 1$ | 单人成果平均表现优于团队成果（在 20 世纪下半叶各学科实证中极少出现）。 |
> > | 注意 | 厚尾极值拉动 | 算术均值容易受极少数超级高引成果拉动，需结合剔除极值或分位数检验核实分布特征。 |
> >
> > > [!geogebra] 动态参数模拟与基准参照
> > > - **横轴** 团队规模 $s$（人，取值范围 $1 \le s \le 10$）
> > > - **纵轴** 相对团队影响力 $\text{RTI}$
> > > - **滑块 s** 当前团队规模（绿色，默认 3 人）
> > > - **滑块 β** 学科协同新异性增益系数（蓝色，默认 0.65）
> > > - **滑块 α** 规模弹性指数（紫色，默认 0.70）
> > > - **滑块 c_{solo}** 单人基准篇均被引（橙色，默认 10）
> > > - **红线** 理论相对团队影响力增长轨迹 $\text{RTI}(s) = 1 + \beta (s - 1)^\alpha$
> > > - **基准参照线** 灰虚线（$\text{RTI} = 1.0$ 平价线）、绿虚线（$\text{RTI} \approx 1.4$ 人文社科均值）、蓝虚线（$\text{RTI} \approx 2.1$ 自然科学与工程均值）
> > >
> > > 拖动滑块 $s$ 可直观验证团队协作的引文倍增效应：当 $s=1$ 时落于平价基准线（$\text{RTI} = 1.0$）；随规模增加，红线迅速跨入超额被引区间。调整学科增益系数 $\beta$ 可呈现不同学科的[[Heterogeneity|异质性]]（人文社科 $\beta \approx 0.35$ 增益平缓，自然科学与工程 $\beta \approx 0.85$ 陡峭攀升）。
> > >
> > > ![[wiki/assets/geogebra/relative_team_impact.ggb]]

> [!software-impl] 软件实现
> - **数据来源** Web of Science、Scopus、OpenAlex 或美国专利商标局（USPTO）数据库。
> - **核心包或命令** Python (`pandas`, `numpy`), R (`dplyr`, `data.table`)。
> - **实现流程** 提取[[Document|文献]]题录元数据，依据署名人数字段将样本划分为单人组与团队组，按学科代码与出版年分组汇总被引均值，两列相除生成 RTI。
> - **报告标准** 明确汇报学科分类标准、成果类型（仅 Article 或包含 Review）、引文窗口统计截至年份以及是否剔除自引。

> [!formula] Python 计算骨架
> ```python
> import pandas as pd
> 
> def calculate_rti(df: pd.DataFrame) -> pd.DataFrame:
>     """计算学科-年份切片的相对团队影响力 (RTI)。
>     
>     输入 DataFrame 需包含列: field, year, author_count, citations
>     """
>     df = df.copy()
>     df["is_team"] = df["author_count"] >= 2
>     
>     grouped = (
>         df.groupby(["field", "year", "is_team"])["citations"]
>         .mean()
>         .unstack(fill_value=0)
>     )
>     grouped.columns = ["solo_mean", "team_mean"]
>     grouped["rti"] = grouped["team_mean"] / grouped["solo_mean"].replace(0, float("nan"))
>     return grouped.reset_index()
> ```

> [!method-stack] 数据口径
> - **数据来源** 涉及跨数据库比对时，因收录期刊范围与会议文献标准差异，不同文献源得出的 RTI 绝对值不可直接混用。
> - **时间与范围** 统计引文需固定相同的累积窗口（如发表后 5 年或 10 年窗口），避免较新成果被引不充分。
> - **清洗与归属** 严格执行自引清洗检验；针对集体署名机构无具体个人名单的特殊成果需统一规则。
> - **标准化** 跨学科横向比较时，以各学科各自内部的单人成果为基准比值，天然具备了学科尺度自归一化属性。

---

> [!method-fit] 适用判断
> - **适合使用** 评估不同科研组织形式、学科门类、资助模式对学术成果影响力的宏观作用机制。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 85–86)]]
> - **谨慎使用** 合作模式极少、绝大多数成果为单人撰写的人文学科细分方向，单人与团队[[Sample Size Determination|样本量]]极度失衡可能放大统计波动。
> - **不适合使用** 微观层面上单一团队或单项具体成果的横向绩效考核，不能以宏观 RTI 比值代替微观同行评议。

> [!ref-table]- 参照基准与阈值
> | 情境 | 参照值 | 来源 |
> |---|---|---|
> | 影响力平衡基准线 | $\text{RTI} = 1.0$ | [[Argument_Wang_Barabasi_2021_Cambridge_Unit04\|Wang and Barabási (2021, p. 86)]] |
> | 科学与工程领域学科均值 | $\text{RTI} \approx 1.8\sim 2.1$（1955 至 2000 年呈现持续爬升） | [[Argument_Wang_Barabasi_2021_Cambridge_Unit04\|Wang and Barabási (2021, p. 86)]] |
> | 顶尖突破层级（被引 Top 0.1%）优势倍率 | 团队产出 1,000 次以上引用的概率是单人的 6.3 倍 | [[Argument_Wang_Barabasi_2021_Cambridge_Unit04\|Wang and Barabási (2021, pp. 86–87)]] |

---

> [!method-limits] 方法局限
> - **测量偏误** 引文分布呈现重尾偏态，算术均值容易受极少数超级引文成果拉动。
> - **可比边界** RTI 将所有两人及以上成果统一归入团队类，掩盖了大团队与小团队在颠覆性与渐进式创新上的内部异质性。
> - **误用风险** 容易将宏观文献计量层面的引文溢价误读为团队协作对科学真理性的直接背书，或简单作为学术机构强行推行组团考核的依据。
> - **补救方式** 结合分位数回归、引入极端高引成果（如 Top 1% 或被引破千篇目）的几率比分析，并细分团队规模梯度。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[Team Science]] | 概念 | RTI 测度对象的核心概念载体，量化展示团队科学相对于单人研究的影响力溢价。 |
> | [[Scientific Productivity]] | 概念 | RTI 所测度的科研成果产出效能与学术影响力的[[Construct\|构念]]支撑。 |
> | [[Burden of Knowledge]] | 理论 | 为团队科学崛起与 RTI 持续大于 1 提供认知与分工机制层面的理论解释。 |
> | [[Bibliometric Analysis]] | 上位方法 | RTI 指标依托的文献计量学分析[[Paradigm\|范式]]。 |
> | [[Brian Uzzi]] | 人物 | RTI 指标的共同提出者与倡导者。 |
> | [[Benjamin F. Jones]] | 人物 | RTI 指标的共同提出者与科学学经济学者。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit04|Wang & Barabási (2021)]] — 运用 RTI 评估 50 年间近 2,000 万篇期刊论著与 210 万件专利，证实团队论著平均引文全面超越单人成果，且在科学与工程领域斩获千次以上引用的概率是单人的 6.3 倍。
