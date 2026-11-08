---
title: Cognitive Extent
aliases:
  - 认知广度
  - 认知疆界
  - 认知领地
  - cognitive extent of science
  - CE
summary: "科学计量学与知识图谱分析中基于词汇与短语离散空间测度某一学科认知领地与概念多样性的量化方法；通过从学术出版物标题与摘要中提取独立概念短语，并依托希普斯定律（Heaps' Law）或固定规模样本控制样本量偏误，评估学科知识边界的探索范围（Milojević, 2015; Hao et al., 2026）。"
type: method
method_type: quantitative
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/indicator
  - theme/scientometrics
  - theme/science-of-science
  - theme/computational-linguistics
related_concepts:
  - "[[Knowledge Production]]"
  - "[[Scientific Productivity]]"
  - "[[Heterogeneity]]"
related_theories: []
related_methods:
  - "[[Knowledge Extent]]"
  - "[[Knowledge Entropy]]"
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[James A. Evans]]"
related_facts: []
related_arguments:
  - "[[Argument_Hao_2026_Nature]]"
confidence: high
status: draft
created: 2026-11-08
updated: 2026-11-08
---

> [!def] Cognitive Extent
> 认知广度（Cognitive Extent, CE）是科学计量学中测度特定学科或研究领域知识疆界与概念空间覆盖范围的量化方法。该方法输入一组文献出版物的标题与摘要文本，通过自然语言处理抽取指代科学构念的核心词汇与名词短语集合，统计独立概念短语的数量随发文规模扩展的幂律关系，或在固定样本量（如 $N = 1,000$ 篇）下计算去重概念总量，输出表征认知领地宽度的数值。[[Argument_Hao_2026_Nature|(Hao et al., 2026, p. 1241)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 测度学科的[[Knowledge Production|知识生产]]探索范围、概念库丰富度与前沿知识概念的累积扩散形态。
> - **问题类型** 学科演化广度测度、跨学科认知覆盖面比较与前沿概念增量监测。
> - **分析单位** 细分学科、科研门类或特定技术范式在设定时间窗内的文献集合。
> - **输入数据** 包含规范标题、摘要与关键词记录的学术文献文本语料库。
> - **输出形式** 去重独立短语计数（整数）或幂律增长指数 $\beta$（实数）。

> [!citation-card] 关键定义
> 学科认知领地宽度的基础度量方式，以给定规模抽样文献批次中包含的独立概念短语总数作为科学构念代理，为控制跨学科样本量规模偏差提供了基准框架。[[Argument_Hao_2026_Nature|(Hao et al., 2026, p. 1241)]]
>
> *Cognitive extent, which is a measure of the breadth of a scientific field’s cognitive territory, and is quantified by the number of unique phrases—as a proxy for scientific concepts—found within a sampled batch of papers of a given size.*

---

> [!method-position] 方法定位
> - **构念效度** 以抽取的自然语言学术短语作为科学概念（Scientific Concepts）的经验代理，能够直观反映学者共同体在词汇表层探索新术语与新议题的活跃程度。
> - **研究者判断** 短语抽取的词频过滤门槛（如最小出现频次）、词干还原（Stemming）与同义词合并规则，以及对比时抽样批次规模 $N$ 的设定。
> - **有效性标准** 需控制总体发文规模膨胀对词汇数量的机械抬升效应，通过固定样本规模重抽样或拟合增长指数确保跨群体可比。
> - **不声称回答的问题** 词汇层面的丰富度受限于自然语言的多义性与同义替换，无法完全捕捉深层概念之间复杂的非线性几何关联。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis|文献计量学]]与计算语言学文本挖掘（Text Mining）。
> - **前置步骤** 停用词过滤、词形还原、名词短语（Noun Phrases）实体识别与低频噪声切除。
> - **变体与扩展** 结合词嵌入语义相似度的连续向量空间扩展版本，即[[Knowledge Extent|知识广度]]（Knowledge Extent）。

> [!dev-timeline] 方法演变
> - **2015 — 原初指标提出** 斯塔莎·米洛耶维奇（Staša Milojević）在《信息计量学杂志》（Journal of Informetrics）发表经典研究，形式化提出认知广度概念，证实多数学科的认知领地扩张遵循亚线性幂律，揭示了科学知识生产的认知承载约束。
> - **2026 — 抽样控制与几何对比** 郝钱跃（Qianyue Hao）等将米洛耶维奇的认知广度抽样控制思想（1,000 篇批次重复 1,000 次）引入连续嵌入向量测度，与几何广度及知识熵并列，奠定了现代科学学评估学科视野宽度的经验基准。[[Argument_Hao_2026_Nature|(Hao et al., 2026, p. 1241)]]

---

> [!formula-step] 步骤一　独立概念短语统计与希普斯定律拟合
> $$V(N) = \alpha N^\beta$$
>
> **这个公式在做什么** 描述文献抽样数量 $N$ 与识别出的去重独立概念短语总量 $V(N)$ 之间的非线性幂律演进关系。
>
> **符号说明**
> - $N$：纳入统计的文献抽样累计篇数。
> - $V(N)$：在这 $N$ 篇文献语料中出现的去重独立科学概念短语总数（Vocabulary Size）。
> - $\alpha$：初始词汇丰富度缩放参数。
> - $\beta$：希普斯幂律增长指数（通常 $0 < \beta < 1$），表征新概念涌现的边际速率。
>
> **数学直觉** 随着文献数量递增，常见核心概念被反复提及，新概念短语的涌现速度呈现边际递减规律（$\beta < 1$）。若某领域 $\beta$ 显著偏低，表明该领域虽发文数量增加，但词汇概念高度固化停滞；而在固定样本规模 $N$ 下直接比较 $V(N)$，则可消除发文体量带来的统计伪影。
>
> > [!example]- 手算示例
> > 对某领域抽取固定规模 $N = 1,000$ 篇文献批次。
> > 自然语言处理流水线共识别出 15,000 个概念短语候选，经去重与词形归一化后，保留独立概念短语 $V(1000) = 4,200$ 个。
> > 对对照领域抽取相同规模 $N = 1,000$ 篇文献，去重独立概念短语仅为 $V(1000) = 2,800$ 个。
> > 结果表明基准领域具有高出 50% 的概念认知广度，词汇探索空间更为开阔。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | $V(N)$ 较高 | 该文献群落涉及更广泛的专业术语与概念构件，认知探索领地更为宽广。 |
> > | 读法 | $\beta$ 趋近 1 | 新概念短语随发文持续快速涌现，处于剧烈拓界与概念创生的初期阶段。 |
> > | 注意 | 样本规模平衡 | 绝不能在样本量差异悬殊的总体之间直接比对绝对词汇数，必须使用等量抽样批次。 |

> [!software-impl] 软件实现
> - **数据来源** OpenAlex、PubMed 或 Web of Science 导出的纯文本元数据（标题与摘要）。
> - **核心包或命令** Python 环境采用 `spacy` 或 `nltk` 提取候选名词短语（Noun Phrases），配合 `scikit-learn` 的 `CountVectorizer` 统计词表。
> - **实现流程** 对文本进行分词与词性标注；抽取符合“形容词+名词”或名词串的实体短语；统计唯一样本词汇量并拟合幂律曲线。
> - **报告标准** 明确报告分词工具、停用词表来源、词形还原规则与批次抽样重复次数。

> [!formula] Python 计算骨架
> ```python
> import re
> from typing import List, Set
> 
> def extract_unique_phrases(documents: List[str], min_length: int = 3) -> Set[str]:
>     """
>     从固定规模文献文本批次中抽取去重概念词汇 (Cognitive Extent 代理)
>     
>     :param documents: 批次文献标题与摘要文本列表
>     :param min_length: 概念词汇最小字符长度
>     :return: 去重独立概念短语集合
>     """
>     unique_phrases = set()
>     # 简易正则过滤标点与数值，提取基础词汇单元
>     for text in documents:
>         clean_text = re.sub(r'[^a-zA-Z\s]', ' ', text.lower())
>         words = [w for w in clean_text.split() if len(w) >= min_length]
>         # 生成单字词与双词短语 (bigrams)
>         for w in words:
>             unique_phrases.add(w)
>         for i in range(len(words) - 1):
>             bigram = f"{words[i]} {words[i+1]}"
>             unique_phrases.add(bigram)
>     return unique_phrases
> 
> # 示例运行
> if __name__ == "__main__":
>     sample_docs = [
>         "Deep learning accelerates scientific discovery and structural inference.",
>         "Machine learning models identify protein structures with high accuracy."
>     ]
>     phrases = extract_unique_phrases(sample_docs)
>     print(f"Cognitive Extent (Unique Concepts): {len(phrases)}")
> ```

> [!method-stack] 数据口径
> - **数据来源** 摘要写作风格因学科而异，医学领域摘要较长且专业词汇密集，理论物理摘要精炼，跨学科比较需谨慎校准基准。
> - **时间与范围** 应限定同一时间窗口内的出版物，避免语言自然演化引入新词干扰。
> - **清洗与归属** 必须滤除通用研究修饰词（如 "method", "results", "analysis"），仅保留实质专业概念。

---

> [!method-fit] 适用判断
> - **适合使用** 追踪新兴学科在概念形成期的术语分化、测度跨学科合作带来的概念融合程度。
> - **谨慎使用** 包含大量非规范缩写或拼写变体的高噪音文本集。
> - **不适合使用** 在未固定样本规模的情况下直接进行宏观历时对比。

---

> [!method-limits] 方法局限
> - **符号离散局限** 词汇计数将近义词（如 "AI" 与 "artificial intelligence"）视作独立概念，容易高估表面词汇繁荣而无法反映真实语义重叠。
> - **语境脱离** 仅统计短语出现，无法识别词汇在不同语境下的多义性变化。
> - **补救方式** 结合密集语义嵌入模型，将离散符号测度升级为连续几何空间的[[Knowledge Extent|知识广度]]（Knowledge Extent）测度。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Knowledge Production]] | 测量对象 | 本方法测度知识生产过程中的概念创生与词汇领地拓展。 |
> | [[Knowledge Extent]] | 升级方法 | 克服本方法的离散符号局限，在连续语义向量空间中测度几何外延直径。 |
> | [[Knowledge Entropy]] | 互补方法 | 认知广度测度词表总体规模，知识熵测度主题分布的均匀度与集中度。 |
> | [[Bibliometric Analysis]] | 上位方法 | 本方法所属的文献计量与计算语言学分析方法家族。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Hao_2026_Nature|Hao et al. (2026)]] — 在方法论述中将认知广度作为基准对照，指出基于固定规模批次抽样的必要性，并据此设计了向量空间知识广度指标。
