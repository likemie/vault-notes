---
title: Record Linkage
aliases:
  - 记录链接
  - 数据链接
  - 实体对齐
  - Data Linkage
  - Entity Resolution
  - 记录匹配
  - Record Matching
summary: "在缺乏统一个人或实体物理标识符的情境下，跨异构数据集识别、匹配并合并指向同一客观实体的记录的量化数据工程与分析方法；包含确定性规则匹配与基于特征相似度的概率匹配模型，为微观个体行为追踪、多源政策评估与科学学知识网络构建提供数据整合基础。"
type: method
method_type: quantitative
method_family: "quantitative"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/data-cleaning
  - theme/scientometrics
  - theme/computational-social-science
related_concepts:
  - "[[Construct]]"
  - "[[Unit of Analysis]]"
  - "[[Construct Validity]]"
  - "[[Variable]]"
  - "[[Data Infrastructure]]"
related_theories: []
related_methods:
  - "[[Author Name Disambiguation]]"
  - "[[Bibliometric Analysis]]"
  - "[[Matching]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[Microsoft Academic Graph]]"
  - "[[SciSciNet]]"
related_arguments:
  - "[[Argument_Lin_2023_SciData]]"
confidence: high
status: active
---

---

> [!def] Record Linkage
> 记录链接（Record Linkage），亦称数据链接（Data Linkage）或实体对齐（Entity Resolution），是一种用于在缺乏跨库全局唯一标识符的情境下，识别、关联并合并分布在两个或多个独立数据集中代表同一真实世界实体的记录的量化数据科学与统计计算方法。该方法输入带有噪声的异构属性文本（如篇名、人名、资助编号、机构地址等），经过文本标准化、分块索引、相似度计算与阈值分类，输出高置信度的实体匹配对。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]

> [!method-scope] 方法范围
> - **研究对象** 跨异构数据库的实体属性记录，包括学术文献、基金资助编号、专利发明人、医疗受试者、学生学籍档案与税收行政记录。
> - **问题类型** 数据清洗、实体识别、跨库合并与长程追踪。
> - **[[Unit of Analysis|分析单位]]** 数据表中的单条记录行、跨数据源的成对实体关系。
> - **输出形式** 经匹配去重后的多源关联关系表、实体唯一映射词表及匹配置信度得分。

> [!citation-card] 非结构化文献与资助记录的对齐规程
> 针对基金资助与科学出版物之间缺乏统一标识符的瓶颈，记录链接管道通过从非结构化描述中抽取论著题名，计算候选字符编辑距离比率，并施加资助批准年份与发表年份的时间窗窗口限制，辅以作者姓氏验证，实现高精度跨源知识对齐。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
>
> *We developed a record linkage pipeline combining text parsing, fuzzy string matching, and strict temporal and authorship constraints to match unstructured reference strings from grant reports to standardized publication records.*

---

> [!method-position] 认识论与方法定位
> - **知识观** 承认单一实证数据库的局限性与信息片断性，将科学知识与社会现象视为分布在不同制度记录中的立体网络，通过记录链接重建整体经验证据。
> - **研究者角色** 在匹配算法的规则构建、相似度阈值划定、阻断分块策略与人工核验抽样中承担关键的设计与校准职能。
> - **有效性标准** 查准率（Precision）、查全率（Recall）、F1 分数以及基于已知黄金标准子集的混淆矩阵检验。
> - **不声称回答的问题** 记录链接本身仅解决跨库实体的匹配与身份对齐，无法直接推出变量之间的因果机制或解释相关效应的生成过程。

> [!method-stack] 方法层级
> - **确定性匹配（Deterministic Linkage）** 依托社保号、身份证号、标准 DOI 等强唯一键或若干完全一致属性的组合进行直接规则匹配。
> - **概率性匹配（Probabilistic Linkage）** 基于 Fellegi-Sunter 概率模型，为不同属性的吻合或差异赋予对数几率权重，计算综合匹配概率。
> - **启发式与机器学习匹配** 引入编辑距离（Levenshtein / Jaro-Winkler）、TF-IDF 向量余弦相似度、深度语义嵌入（BERT）与时间窗物理约束的复合匹配流水线。

---

> [!proc] 通用程序
> 1. **数据清洗与预处理** 清理特殊字符、规范大小写、统一机构与缩写表达、提取非结构化文本中的核心实体字段。
> 2. **分块索引设计（Blocking）** 针对海量数据笛卡尔积组合爆炸问题，依据粗粒度稳定特征（如首字母、邮编、年份区间）建立搜索窗口，削减候选对规模。
> 3. **属性相似度打分** 逐字段比对候选记录，计算连续型文本相似度分数或分类离散指示值。
> 4. **阈值判定与约束过滤** 设定分类决策边界，并结合业务逻辑施加硬性排他约束（如发表年份不能早于资助立项过多）。
> 5. **质量核验与基准校准** 采用人工双盲抽样复查，或与权威商业基准进行跨库重合度交叉验证。

> [!method-stack] 数据与变量
> - **数据结构** 包含跨源多表的非配对关系数据库或非结构化半结构化元数据文本。
> - **样本与单位** 数万至数亿量级的待匹配记录对。
> - **变量或测量** 字符串编辑相似度、时间差偏移量、作者重合度与匹配分类判定指示变量。

---

> [!method-fit] 适用判断
> - **适合使用** 适合多源行政数据合并、跨世纪学术图谱构建、产学研资助流向追踪以及缺少统一代码的大规模纵向追踪研究。[[Argument_Lin_2023_SciData|(Lin et al., 2023)]]
> - **谨慎使用** 在属性字段重度缺失（如仅有单一模糊常见姓氏）、拼写极度不规则或时间跨度极大导致实体演化漂移的场景下须谨慎，严防大范围假阳性级联。
> - **不适合使用** 不适合用于样本量极小且可完全人工逐笔核验的高风险敏感决策。

---

> [!method-limits] 方法局限
> - **偏误来源** 常见姓名同名异人、拼写变体与转录OCR误读极易导致特征打分失真。
> - **假阳性与假阴性权衡** 提高相似度阈值会减少错误匹配（降低假阳性），但会遗漏大量真实关联（增加假阴性）；反之则会引入大量虚假关联。
> - **算力复杂度瓶颈** 在亿级无唯一标识记录库中，全量对齐的比对开销呈二次方爆炸（$O(N \times M)$），必须依赖高效的分块索引与剪枝策略。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[Author Name Disambiguation]] | 前置/伴生方法 | 著者姓名消歧是记录链接在学者个体实体对齐上的专门分支。 |
> | [[Bibliometric Analysis]] | 上位方法家族 | 科学计量学依赖记录链接打通论文、基金、专利与引文网络。 |
> | [[Matching]] | 关联统计方法 | 因果推断中的匹配方法关注处理组与对照组变量分布平衡，记录链接关注物理实体标识一致。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Lin_2023_SciData|Lin et al. (2023)]] — 开发融合文本抽取、模糊字符串距离与发表年份约束的记录链接管道，成功对齐 131 万条 NSF 项目非结构化引文与微软学术图谱主论著，并以 Dimensions 商业数据库完成双盲交叉核验。
