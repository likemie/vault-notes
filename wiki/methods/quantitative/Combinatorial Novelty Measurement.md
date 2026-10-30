---
title: Combinatorial Novelty Measurement
aliases:
  - 组合新颖性测度法
  - 非典型引文对分析
  - 期刊共引对新颖性分析
  - Atypical Combination Analysis
  - Combinatorial Novelty Metric
summary: "由 Brian Uzzi et al. (2013) 开创的文献计量学量化测度方法；通过比对学术成果参考文献中不同学科期刊共引对的实际出现频次与置换零模型期望频次的 z 分数，同时评估成果在常规性基底与非典型新颖性维度的知识整合特征。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 0
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/indicator
  - theme/scientometrics
  - theme/science-of-science
  - theme/citation-analysis
confidence: high
status: active
created: 2026-10-31
updated: 2026-10-31
---

---

> [!def] Combinatorial Novelty Measurement
> 基于全量文献引文网络，通过统计论著参考文献列表中所有期刊共引对（journal co-citation pairs）的真实共现频次，并与保持文献出引量和期刊入引量不变的置换零模型随机期望进行对比，计算各期刊对的标准化 $z$ 分数；进而提取单项成果共引对 $z$ 分数分布的中位数与第 10 百分位数，分别量化该成果的常规性（conventionality）与非典型新颖性（novelty）。[[Argument_Wang_Barabasi_2021_Cambridge_Unit08|(Wang & Barabási, 2021, pp. 190–193)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 学术论著或发明专利在知识组合层面的结构特征，关联 [[Combinatorial Novelty]] 与常规性知识基底构念。
> - **问题类型** 测度、分类与回归预测（检验知识组合模式对后续引文影响与突破概率的因果或关联效应）。
> - **分析单位** 单篇学术论著、专利发明或学者个人产出组合。
> - **输入数据** 大规模学术数据库（如 Web of Science、Scopus、MAG）中带精确期刊标识与发表年份的参考文献列表。
> - **输出形式** 连续型无量纲分数（中位数常规性 $z$ 分数与第 10 百分位数新颖性 $z$ 分数），以及离散化象限分类（常规/非典型交叉类别）。

> [!citation-card] 关键定义
> 如果一项成果引用的期刊对在以往文献中极少同时出现，这表明该论著引入了前人知识的全新组合。通过与随机重配的零模型进行对比，计算各期刊引证对的共现概率偏离程度，能够在全量文献尺度上精确刻画科学成果的常规基底深度与非典型创新程度。[[Argument_Wang_Barabasi_2021_Cambridge_Unit08|(Wang & Barabási, 2021, pp. 190–191)]]
>
> *If a paper cites a pair of journals that are rarely brought together, it may suggest that the paper introduces a novel combination of prior work... Comparing observed co-citations with randomized null models allows researchers to quantify both the conventional and atypical dimensions of science.*

---

> [!method-position] 方法定位
> - **构念效度** 期刊共引对反映了不同知识分支之间的认知连接；该方法有效克服了单一依赖主观专家评审或粗粒度学科分类标签的局限，但在期刊内部高度细分的方向异质性识别上可能存在分析尺度损耗。
> - **研究者判断** 零模型随机化算法的约束条件（是否约束发表年度、学科分布）、非典型截断阈值（通常选取下四分位数或第 10 百分位数）以及对通用综合性大刊（如 *Nature*、*Science*、*PNAS*）共引权重的平抑处理。
> - **有效性标准** 跨学科时间序列稳健性、置换模拟迭代稳定性、对后续顶尖 1% 高引成果的受试者工作特征（ROC）区分效度。
> - **不声称回答的问题** 该方法测度的是知识构件配对的新颖程度，并不直接度量实证发现的真伪或理论推导的技术质量。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis|文献计量学]]与复杂网络分析方法。
> - **前置步骤** 期刊名称规范化与消歧、全库二部图网络构建、年度随机重连（degree-preserving bipartite randomization）。
> - **变体与扩展** 关键词组合新颖性测度（基于申请书或摘要关键词共现）、专利技术代码分类对（CPC/IPC co-occurrence）组合测度。

> [!dev-timeline] 方法演变
> - **2001 — 技术专利发明组合测度初探** 弗莱明（Lee Fleming）利用美国专利局技术分类号的首次组合频度，初步测定发明专利的重组不确定性。[[Argument_Wang_Barabasi_2021_Cambridge_Unit08|(Wang & Barabási, 2021, p. 191)]]
> - **2013 — 乌齐期刊引文对双重测度体系** [[Brian Uzzi|布赖恩·乌齐]]（Brian Uzzi）等人在《科学》（*Science*）正式确立中位数常规性与第 10 百分位数非典型性的双维标准化测度体系，完成对 1,790 万篇科技论著的大规模测算。[[Argument_Wang_Barabasi_2021_Cambridge_Unit08|(Wang & Barabási, 2021, p. 193)]]
> - **2015 — 团队创造力与引文新颖性解构** 李允娜（Youn-Na Lee）等将该测度扩展至科学家跨界团队协作与个体多学科背景的匹配分析。[[Argument_Wang_Barabasi_2021_Cambridge_Unit08|(Wang & Barabási, 2021, p. 191)]]

---

> [!formula-set]- 公式链总览
> ```mermaid
> flowchart LR
>   A["论著参考文献列表"] --> B["期刊共引对提取 (i, j)"]
>   B --> C["零模型随机化期望计算"]
>   C --> D["期刊对标准化 z 分数计算"]
>   D --> E["单项成果常规性与新颖性指标输出"]
> ```

> [!formula-step] 步骤一　期刊共引对标准化偏离测算
> $$z_{ij} = \frac{C_{ij} - \mu_{ij}}{\sigma_{ij}}$$
>
> **这个公式在做什么** 计算在特定出版年份中，期刊 $i$ 与期刊 $j$ 的真实共同被引频次 $C_{ij}$ 相较于保留网络度分布约束的随机重连零模型均值期望 $\mu_{ij}$ 的相对偏离程度，以标准差 $\sigma_{ij}$ 实施标准化。[[Argument_Wang_Barabasi_2021_Cambridge_Unit08|(Wang & Barabási, 2021, pp. 190–191)]]
>
> **符号说明**
> - $C_{ij}$：在目标年份文献中，同时引用期刊 $i$ 与期刊 $j$ 的实际文献篇数。
> - $\mu_{ij}$：通过蒙特卡洛随机重连网络模拟生成的期刊共引期望均值。
> - $\sigma_{ij}$：随机零模型模拟中期刊共引频次的标准差。
>
> **数学直觉** 若两本期刊的实际共引次数与随机期望一致，则 $z_{ij} \approx 0$；若实际共引显著高于随机期望（$z_{ij} > 0$），反映出两刊处于成熟的主流学术交流圈内；若实际共引极低甚至显著为负（$z_{ij} < 0$），则揭示该期刊对属于违背主流学术惯例的非典型碰撞。
>
> > [!example]- 手算示例
> > 假定在某年度神经科学领域中，期刊 A（*Gene Expression*）与期刊 B（*Journal of Clinical Psychiatry*）的实际共同被引次数为 $C_{AB} = 1$；在 1,000 次随机置换生成的零模型网络中，二者共引的期望均值 $\mu_{AB} = 8.5$，标准差 $\sigma_{AB} = 2.5$。
> > 则该期刊对的标准化得分为：
> > $$z_{AB} = \frac{1 - 8.5}{2.5} = -3.0$$
> > 结果为显著负向偏离，说明该组合具有极强的非典型新颖性。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | $z_{ij} > 0$（正向高分） | 表明期刊对属于高频共现的成熟学术共同体范式，具有极高常规性与同行熟悉度。 |
> > | 读法 | $z_{ij} < 0$（负向低分） | 表明期刊对在统计上属于异质冷门配对，表征突破常规边界的非典型创新构想。 |
> > | 注意 | 规模与稀疏性控制 | 在计算 $\mu$ 与 $\sigma$ 时必须采用严格保持单篇文献出引量和期刊被引总量的度保持随机化（degree-preserving randomization），防止因期刊整体发文体量巨大而造成人为假相关。 |

---

> [!formula-step] 步骤二　单项成果常规性与非典型新颖性双维解构
> $$\text{Conventionality} = \text{Median}\left(\{z_{ij}\}\right), \quad \text{Novelty} = P_{10}\left(\{z_{ij}\}\right)$$
>
> **这个公式在做什么** 对特定论著参考文献列表中的所有期刊对 $\{z_{ij}\}$ 分布进行统计切片，取其中位数作为成果的常规性基底得分，取其第 10 百分位数（低尾分布）作为非典型新颖性测度。[[Argument_Wang_Barabasi_2021_Cambridge_Unit08|(Wang & Barabási, 2021, p. 193)]]
>
> **符号说明**
> - $\{z_{ij}\}$：某项成果参考文献列表中所有两两期刊配对的 $z$ 分数集合。
> - $\text{Median}$：集合的中位数，表征文献整体知识根基的常规主流程度。
> - $P_{10}$：集合的第 10 百分位数，表征文献知识组合中最具颠覆性与反常规的探索边界。
>
> **数学直觉** 绝大多数科学文献都同时引用多个学科的刊物；单一均值容易掩盖引文内部的极端值。取中位数可稳定捕捉主流研究者对该课题的常识共享底色，取左尾第 10 百分位数则能够敏感捕捉成果是否植入了引人注目的异质跨界火花。
>
> > [!example]- 手算示例
> > 某篇论著共引用 5 本期刊，产生 10 组期刊对，其 $z$ 分数升序排列为：
> > $\{-3.5, -2.1, 1.2, 4.5, 5.8, 6.2, 7.0, 8.1, 9.4, 11.2\}$。
> > - 中位数为 $(5.8 + 6.2) / 2 = 6.0$（高度常规）；
> > - 第 10 百分位数为 $-3.5$（高度非典型新颖）。
> > 该成果即属于“深植于常规基底之上的非典型创新”。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 高常规 + 高新颖 | 兼顾扎实可读性与跨界突破性，实证显示其成为前 1% 爆款高引成果的概率是基准水平的两倍以上。 |
> > | 读法 | 低常规 + 高新颖 | 孤立异质跨界，极易因缺乏共同体认知锚点而遭遇同行评审严重打压或陷入长期引文沉没。 |
> > | 注意 | 引文列表长度敏感性 | 参考文献较少的短篇成果可能无法生成足够的期刊对以准确计算第 10 百分位数，通常需设置参考文献数量下限（如不少于 5 或 10 篇引文）。 |

---

> [!method-fit] 适用判断
> - **适合使用** 大规模科学引文大数据的宏观统计分析、跨学科交叉资助项目的立项前沿性评估、学科前沿演进与范式转移追踪。[[Argument_Wang_Barabasi_2021_Cambridge_Unit08|(Wang & Barabási, 2021, pp. 190–193)]]
> - **谨慎使用** 针对人文学科或引文高度依赖专著而非连续出版物的学科，因期刊共引矩阵稀疏性会导致测度偏倚。
> - **不适合使用** 无法用于评估单篇未发表工作手稿的实质逻辑真伪，亦不能替代定性同行评审中的技术细节审查。

---

> [!method-limits] 方法局限
> - **依赖引文规范完备性** 假定学者在参考文献中完全诚实、完整地反映了其思想来源；若存在策略性引用名刊或遗漏竞争对手关键先驱的现象，会扭曲期刊对真实度。
> - **跨学科引文习惯异质性** 不同学科在引文篇幅（如生物学多达几十篇 vs 数学仅有十几篇）与引证半衰期上的客观差异可能对非典型分位数估计带来跨领域噪音。

---

## 使用此方法的研究

- [[Argument_Wang_Barabasi_2021_Cambridge_Unit08]]：王大顺与巴拉巴西在《科学学的科学》第 18 章中，评介了乌齐等人基于该方法对 1,790 万篇科技论著的大数据挖掘，确立了将非典型组合根植于常规基底方能有效倍增顶尖突破概率的核心论断 (pp. 190–193)。
