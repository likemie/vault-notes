---
title: AlphaFold
aliases:
  - 阿尔法折叠
  - AlphaFold 1
  - AlphaFold 2
  - DeepMind AlphaFold
summary: "由 DeepMind 研发的基于深度学习与多层神经网络的蛋白质三维空间结构预测系统；在 2018 年第 13 届国际蛋白质结构预测关键评估（CASP13）竞赛中实现跨越式突破，其单届预测精度提升幅度超过以往两届赛事总和，一举超越全球所有资深结构生物学团队，确立了人工智能攻克极端高维复杂科学难题的里程碑范例。"
type: fact
subtype: program
region: global
fact_region: "global"
fact_kind: "program"
fact_related_count: 8
fact_related_level: 0
fact_related_stars: "☆"
fact_related_color: "#ede9fe"
period: "2018–至今"
initiator_organization: "DeepMind Technologies"
official_website: "https://alphafold.ebi.ac.uk"
tags:
  - fact/program
  - theme/artificial-intelligence
  - theme/deep-learning
  - theme/scientific-discovery
  - theme/structural-biology
  - region/global
related_concepts:
  - "[[Paradigm]]"
  - "[[Scientific Paradigm]]"
  - "[[Man-Computer Symbiosis]]"
  - "[[Algorithmic Bias]]"
  - "[[Trend Study]]"
related_theories: []
related_methods:
  - "[[Network Analysis]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[Critical Assessment of Structure Prediction]]"
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit10]]"
confidence: high
status: draft
created: 2026-11-02
updated: 2026-11-08
---

---

> [!claim] 项目定位
> **AlphaFold（阿尔法折叠）** 是英国 DeepMind 团队研发的人工智能深度学习系统，致力于攻坚分子结构生物学半个世纪未决的蛋白质折叠世纪难题。系统利用深层残差神经网络直接从一维氨基酸线性序列高精度预测空间三维构象，标志着数据驱动的机器智能在自然科学底层基础问题求解中全面超越人类领域专家。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 231–232)]]

> [!program-context] 项目背景
> - **立项时间 / 周期** 2016 年 AlphaGo 战胜李世石后启动立项，2018 年在 CASP13 首次亮相并夺冠，2020 年发布 AlphaFold 2 达到原子级精度，常态化服务全球生命科学研究。
> - **研发主体与资源配置** 谷歌旗下 DeepMind 计算研究团队，集聚计算机科学家、物理学家与生物信息学家，依托大规模图形处理器（GPU）与张量处理器（TPU）超算集群进行端到端表征训练。
> - **技术服务对象** 全球结构生物学、药物设计、神经退行性疾病（阿尔茨海默病、帕金森病）机理研究与合成生物学领域学者。
> - **核心科学问题导向** 攻克结构生物学领域的宏大挑战：由长链氨基酸构成的大分子蛋白质如何在物理环境中自发折叠为特定致密立体构象。传统晶体学实验解析单一结构耗时数月至数年且成本高昂，严重制约了生命科学探索进程。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, p. 231)]]

---

> [!claim] 核心干预／机制假说
> 运用深层神经网络对全球蛋白质数据库（PDB）进行特征抽取与高维参数调谐，通过学习氨基酸残基对之间的空间距离与几何角度概率分布，替代传统手工力场计算与穷举构象搜索，实现前所未有的折叠构象预测精度。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 232–234)]]

> [!policy-design] 方案设计
> - **多层深度网络表征** 构建包含海量隐藏层的深层非线性网络，将原始一维序列映射为高维几何拓扑空间，系统自主完成特征工程调谐。
> - **盲测竞技与客观评估** 参与[[Critical Assessment of Structure Prediction|国际蛋白质结构预测关键评估]]（Critical Assessment of Structure Prediction, CASP），在完全不知晓目标蛋白质真实空间构象的前提下提交盲测预测。
> - **开放获取与科学公共基础设施** 联合欧洲生物信息学研究所（EMBL-EBI）建立公开数据库，向全球学术界免费开放数以亿计的预测蛋白质空间结构。

> [!citation-card] AlphaFold 跨界突破传统学科边界
> 在 2018 年 CASP13 盲测中，没有任何生物学建制背景的 DeepMind 团队凭借 AlphaFold 系统取得了前所未有的技术飞跃，其单届竞赛取得的预测精度增幅相当于以往两届常规赛事的总和，平均准确度显著超越全球其他 97 支由资深科学家领衔的国际顶尖参赛团队。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 231–232)]]
>
> *In December 2018, at the 13th Critical Assessment of Structure Prediction (CASP) competition... DeepMind with its AlphaFold system outperformed all traditional structural biologists. In a blind test of 90 target proteins, AlphaFold's accuracy significantly outpaced the other 97 competing teams.*

---

> [!dev-timeline] 项目推进历程
> - **2016–2018 — 初代模型攻坚与 CASP13 夺冠** DeepMind 设立蛋白质折叠研发团队，2018 年 12 月初代 AlphaFold 在 CASP13 夺得榜首，预测精度实现历史性飞跃。
> - **2020 — AlphaFold 2 原子级突破与 CASP14 绝尘** 引入空间演化几何约束与注意力机制，预测精度在 CASP14 达到可匹敌 X 射线晶体学实验的 90 分以上的 GDT 评分，公认基本攻克折叠难题。
> - **2021–至今 — 全球结构数据库开源与生态扩散** 联合 EMBL-EBI 上线 AlphaFold 数据库，覆盖人类全蛋白质组及数亿种已知生命蛋白结构，深刻重塑生物医药研发范式。
> - **2026 — 科学学实证检验与计算生物学重构** [[Argument_Hao_2026_Nature|Hao et al. (2026)]] 将其作为自然科学 AI 渗透的典型代表，实证揭示 AlphaFold 预测结构绕过传统实验成本，驱动分子生物学 AI 成果激增 4.70 倍。[[Argument_Hao_2026_Nature|(Hao et al., 2026, p. 1237)]]

---

> [!actor-grid] 实施协同矩阵
> - **DeepMind 核心攻关团队** 负责深层架构设计、损失函数制定与大规模分布式训练。
> - **CASP 独立评审组委会** 负责汇集未公开晶体结构的盲测目标蛋白，组织全球同行展开双盲评分评测。
> - **全球生物医学学术共同体** 将预测结构应用于病理机制探索、酶工程改造与抗癌新药研发。

---

> [!indicators] 评估指标体系
> - **全局距离测试评分（GDT_TS）** 衡量预测空间骨架与真实实验测定构象重合度的客观指标（0–100）。
> - **盲测竞赛排名** 在 CASP 同台盲测中相对全球其他近百支传统结构生物学实验室的综合名次。
> - **单届精度提升倍率** 与以往赛事历史递增速度的比值。

> [!finding-cards] 核心实证结论
> - **预测精度打破历史慢速积累** 单届竞赛实现的算法预测精度增幅，相当于 CASP 过去两届（四年）常规进展的总和。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, p. 231)]]
> - **非建制团队展现颠覆性优势** 完全缺乏分子生物学传统建制背景的计算团队跨界击败全部顶尖领域学者，验证了通用深层网络在特定高维科学空间内的求解效率。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 231–232)]]
> - **窄域智能的边界与互补性** 汪大胜（Dashun Wang）与阿尔伯特-拉斯洛·巴拉巴西（Albert-László Barabási）指出，AlphaFold 展现了专用解题工具的极致性能，但其成功高度依赖海量高质量训练数据与明确的优化目标，无法自行提出新的前沿科学命题或替代人类直觉。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 238–239)]]

> [!stat-cards]- 关键实证数据
> 在针对 90 种已知但未公开构象的盲测蛋白质中全面领先；击败全场 97 支由资深科学家领衔的国际顶尖参赛团队；预测精度单届提升增量达到过去两届赛事总和。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 231–232)]]

---

> [!debates] 核心争议
>
> > [!axis] 科学理解深度 vs 黑箱拟合精度
> > 算法预测空间构象是否等同于真正理解折叠物理定律的认识论分歧。
> >
> > - **计算经验主义立场** 算法能够以原子级精度直接输出正确构象并支持新药研发，已达成自然科学的实用目标。
> > - **物理因果机制立场** 批评指出 AlphaFold 预测出静态折叠终态，并未揭示蛋白质折叠在真实细胞微秒级尺度下的动力学生理热力学路径，机器智能未能完全替代对第一性原理物理定律的因果解释。

---

> [!evidence-grid-a|notitle] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit10|Wang & Barabási (2021)]] — 详述 AlphaFold 在 CASP13 击败 97 支人类专家团队的历史突破，并以此澄清现代深度学习系统的专用解题属性与人类科学家的领导力边界。
> - [[Argument_Hao_2026_Nature|Hao et al. (2026)]] — 实证揭示 AlphaFold 为代表的结构预测模型驱动分子生物学 AI 成果激增 4.70 倍，重构了计算生物学工程范式。
