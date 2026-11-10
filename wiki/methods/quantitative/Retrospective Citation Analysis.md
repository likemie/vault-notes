---
title: Retrospective Citation Analysis
aliases:
  - 引文回溯分析
  - 引文回溯测度法
  - 回溯引文分析
  - 共时引文分析
  - Synchronous Citation Analysis
  - Citation From Approach
summary: "科学计量学中测度引文时间维度的截面分析方法；以特定出版年份的施引论著为观测锚点，统计其参考文献的发表年龄分布，测度科研人员开展探索时的引用记忆纵深；该方法计算便捷、仅需单期截面数据，但受系统文献指数增长的调制，使历史文献的宏观被引呈现人为贴现效应（Wang & Barabási, 2021）。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 17
method_related_level: 1
method_related_stars: "⭐"
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
  - "[[Knowledge Hotspots]]"
  - "[[Unit of Analysis]]"
  - "[[Construct Validity]]"
  - "[[Citation Distribution]]"
  - "[[Citation Aging]]"
  - "[[Construct]]"
related_theories: []
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Prospective Citation Analysis]]"
  - "[[Relative Citation Normalization]]"
related_instruments: []
related_persons:
  - "[[Dashun Wang]]"
  - "[[Albert-László Barabási]]"
  - "[[Derek de Solla Price]]"
related_facts:
  - "[[Web of Science]]"
  - "[[Scopus]]"
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit09]]"
  - "[[Argument_Wang_Barabasi_2021_Cambridge]]"
confidence: high
status: active
created: 2026-11-02
updated: 2026-11-11
---

---

> [!def] Retrospective Citation Analysis
> 引文回溯分析（Retrospective Citation Analysis，又称共时引文分析 Synchronous Citation Analysis 或 Citation From 进路）是一种以施引[[Document|文献]]为基准轴测度引文时间年龄分布的[[Bibliometric Analysis|文献计量学]]量化方法。其核心操作为：固定特定出版年份 $t$ 的施引学术文献样本，统计其所引述参考文献的发表年代，计算引文年龄跨度 $\tau = t - t_{\text{cited}}$ 的经验概率分布 $P_{\text{retro}}(\tau)$。该方法用以表征科研人员在写作特定成果时向过去审视的“引用记忆（Citing Memory）”深度与文献搜寻结构。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 204–205)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 科学共同体在特定历史截面的知识检索跨度、引用记忆半衰期（Citing Half-Life）与[[Knowledge Hotspots|知识热点]]架构。
> - **问题类型** 描述学术引文的年龄分布结构、分析数字化检索工具与同行评议对历史文献引证偏好的重塑、测算学科引用记忆的时序演变。
> - **[[Unit of Analysis|分析单位]]** 单篇学术文献的参考文献清单、特定期刊同年度全量发表文献集群、学科领域年度出版全集。
> - **输入数据** 包含标准出版年份与参考文献题录列表的引文数据库记录（如 [[Web of Science]] 或 [[Scopus]]）。
> - **输出形式** 参考文献年龄概率分布密度直方图、平均参考文献年龄 $\langle \tau \rangle$、离散系数 $\sigma_\tau$ 及知识热点象限分布。

> [!citation-card] [[Dashun Wang|王大顺]]与[[Albert-László Barabási|巴拉巴西]]论回溯引文分析的测度视角
> 回溯法考察特定年份出版文献所引用的参考文献，分析这些引文向过去追溯的年龄分布。这种方法量化了研究者在引用早期工作时向后回看的距离，刻画了该论著的引用记忆。研究显示，由于施引文献固定且无需长周期追踪，2000 年之前的文献计量学研究大多依赖回溯法展开。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 204–205)]]
>
> *The retrospective (citation from) approach considers papers cited by a publication during a particular year and analyzes the age distribution of these citations, looking back in time... characterizing the citing 'memory' of a paper.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 能够精确反映科研人员撰写成果时的即时知识吸纳视野，但受制于历史文献存量指数扩容的稀释效应，无法单独作为文献内在影响寿命的无偏指标。
> - **研究者判断** 施引年份选择、参考文献类型筛选（剔除书籍、会议摘要或非正式出版物）、自引剔除标准。
> - **有效性标准** 参考文献年代字段完备率、跨学科归一化基准以及对系统性历史扰动（如世界大战出版骤降）的控制。
> - **不声称回答的问题** 不能直接推断单篇新成果在未来的长程被引增长轨迹；不能将回溯分布中高龄文献的低占比直接解释为经典知识价值的物理消亡。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis|文献计量分析]]（Bibliometric Analysis）。
> - **对偶方法** [[Prospective Citation Analysis|引文前瞻分析]]（基于成果队列历时追踪的对应进路）。
> - **衍生应用**
>   - **知识热点二维模型** 结合平均参考文献年龄与变异系数测定突破性创新架构（Mukherjee et al., 2017）；
>   - **学术记忆历史分析** 测算 1960 年代以来由于复印机普及、同行评议与搜索引擎带来的经典引用回升（[[Argument_Wang_Barabasi_2021_Cambridge|Wang & Barabási, 2021, pp. 200–204]]）。

> [!dev-timeline] 方法演变
> - **1965 — [[Derek de Solla Price|普赖斯]]半衰期测度** [[Derek de Solla Price|德里克·德索拉·普赖斯]]运用截面期刊参考文献统计，提出科学文献引用的半衰期定律。
> - **1988 — 中本秀之确立共时分析概念** 中本秀之界定共时（Synchronous）[[Citation Distribution|引文分布]]规范，明确其与历时追踪的视角边界。
> - **2005 — 雷德纳大规模物理引文实证** 西德尼·雷德纳利用《物理评论》百年全量数据，绘制出精确的回溯引文年龄幂律衰减曲线。
> - **2017 — 尹良与王大顺推导积分对偶映射** 尹良与[[Dashun Wang|王大顺]]推导出回溯分布与前瞻分布在文献指数增长环境下的精确积分解析式。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Yin & Wang, 2017; via Wang & Barabási, 2021, pp. 204–205)]]

---

> [!formula-set]- 公式链总览
> ```mermaid
> flowchart LR
>   A["固定施引年份 t 的参考文献清单"] --> B["测算年龄差 τ = t - t_cited"]
>   B --> C["经验回溯概率分布 P_retro(τ)"]
>   C --> D["引入系统年增长率 β 进行指数去贴现"]
>   D --> E["反演前瞻获引存活分布 P_prosp(τ)"]
> ```

> [!formula-step] 步骤一　回溯引文年龄分布的稳态贴现公式
> 在全系统文献规模服从指数扩张 $N(t) \propto e^{\beta t}$ 的条件下，回溯引文年龄分布 $P_{\text{retro}}(\tau)$ 表现为前瞻获引存活概率 $P_{\text{prosp}}(\tau)$ 与历史文献基数贴现因子的乘积积分归一化：
>
> $$P_{\text{retro}}(\tau) = \frac{P_{\text{prosp}}(\tau) e^{-\beta \tau}}{\int_0^\infty P_{\text{prosp}}(\tau') e^{-\beta \tau'} d\tau'}$$
>
> **这个公式在做什么** 输入单篇成果在发表经历 $\tau$ 年时的客观前瞻获引存活率 $P_{\text{prosp}}(\tau)$ 与系统文献年均扩张指数 $\beta$，输出施引文献参考文献中年龄为 $\tau$ 的理论分布概率。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, p. 204)]]
>
> **符号说明**
> - $\tau$ 为被引成果距当期的年龄跨度（$\tau = t - t_{\text{cited}} \ge 0$）；
> - $\beta$ 为科学系统出版成果总量的年化指数增长率（自然科学通常在 0.04 至 0.05 之间，对应约 15 年翻倍周期）；
> - $e^{-\beta \tau}$ 为历史产出贴现因子。
>
> **数学直觉** 施引学者即便在主观上对新老知识一视同仁，由于历史早期发表的文献基数呈几何级数少于近代文献，随机知识采样必然导致历史成果在统计上出现指数缩水。

> [!formula-reading] 回溯分析的方法优势与使用要点
> | 维度 | 要点 | 说明 |
> |---|---|---|
> | 优势 | 计算即时性 | 只需收集当期成果的参考文献列表，无需长达数十年的追踪时间窗口即可出具结果。 |
> | 优势 | 搜寻行为映射 | 直接反映科学界当下在知识前沿与经典基石之间的认知平衡状态。 |
> | 注意 | 人为陡峭偏差 | 原始引文年龄曲线表现出的急剧衰减，相当比例源自文献库整体的快速膨胀，不可轻率视同知识失效。 |

---

> [!software-impl] 软件实现
> - **核心逻辑** 遍历提取施引成果元数据中的参考文献出版年份，计算差值并聚合为分布频率向量。
> - **报告标准** 明确实体匹配率、剔除未标注年份参考文献的比例，并报告平均年龄与方差。

> [!formula] Python 计算骨架
> ```python
> import numpy as np
> import pandas as pd
> 
> def compute_retrospective_age_distribution(citations_df: pd.DataFrame, citing_year: int):
>     """
>     计算特定施引年份下的回溯引文年龄概率分布
>     citations_df 包含字段: citing_year, cited_year
>     """
>     subset = citations_df[citations_df['citing_year'] == citing_year].copy()
>     subset['age'] = subset['citing_year'] - subset['cited_year']
>     valid_ages = subset[subset['age'] >= 0]['age']
>     
>     max_age = int(valid_ages.max())
>     age_counts = valid_ages.value_counts().sort_index()
>     p_retro = np.zeros(max_age + 1)
>     for age, cnt in age_counts.items():
>         p_retro[int(age)] = cnt
>     p_retro /= p_retro.sum()
>     
>     mean_age = valid_ages.mean()
>     return p_retro, mean_age
> ```

---

> [!method-fit] 适用判断
> - **适合使用** 分析科研人员文献查阅跨度、考察电子期刊与搜索引擎对学术记忆的改变、度量交叉创新中的新旧知识结合。[[Argument_Wang_Barabasi_2021_Cambridge_Unit09|(Wang & Barabási, 2021, pp. 200–204)]]
> - **谨慎使用** 跨越重大战争或历史数据库收录断代时，需对系统文献增长率进行分段估计。
> - **不适合使用** 评估单篇刚发表成果未来的长期获引峰值与终身影响力，此类任务必须采用前瞻法。

---

> [!method-limits] 方法局限
> - **偏误来源** 历史文献早期数字化遗漏引发的高龄截断偏误；学者引文复制导致的伪流行偏误。
> - **适用边界** 仅适用于规范标记参考文献发表年代的现代文献引文库。
> - **补救方式** 结合对偶贴现公式反演客观前瞻存活曲线，或配合[[Relative Citation Normalization|相对引文标准化]]剔除领域增长率偏倚。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Prospective Citation Analysis]] | 对偶方法 | 以发表队列追踪长程影响力的对应进路，二者通过增长贴现积分建立数学对偶映射。 |
> | [[Bibliometric Analysis]] | 上位方法 | 构成文献计量学测度知识搜寻与引用记忆的基础分支。 |
> | [[Knowledge Hotspots]] | 概念 | 回溯引文年龄均值与离散系数在二维拓扑中识别高突破知识架构的核心应用。 |
> | [[Citation Aging]] | 概念 | 测度与刻画文献引用随时间推移注意力消退的客观[[Construct\|构念]]。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit09|Wang & Barabási (2021)]] — 在第 19 章前 3 节（pp. 200–204）与专栏 19.1（pp. 204–205）详尽阐述回溯分析的测度逻辑及其在揭示知识热点中的关键应用。
