---
title: Learning Analytics
aliases:
  - 学习分析
  - 学习分析学
  - Educational Data Mining
  - 学习分析与教育数据挖掘
summary: "通过收集、测量、分析和报告学习者及其环境的数字痕迹以理解和优化学习的技术与治理实践；既赋能个性化自适应与纵向学习增益测查，也在先发制人治理、算法主体性规训与构念简化上面临深刻伦理挑战。"
type: concept
domain: "educational-technology"
related_count: 17
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - theme/learning-analytics
  - theme/educational-data-mining
  - theme/digitalization
  - theme/edtech
  - theme/subjectification
  - theme/higher-order-thinking
  - level/higher-education
  - level/k12
related_concepts:
  - "[[Homework]]"
  - "[[Academic Achievement]]"
  - "[[Learning Gain]]"
  - "[[Feedback]]"
  - "[[Performativity of Measurement]]"
  - "[[Digital Optimum]]"
  - "[[Disciplina and Doctrina]]"
  - "[[Epistemology]]"
  - "[[Data Behaviorism]]"
  - "[[Construct]]"
  - "[[Paradigm]]"
  - "[[Formative Assessment]]"
  - "[[Reliability]]"
  - "[[Computerized Adaptive Testing]]"
  - "[[Higher-Order Thinking Skills]]"
  - "[[Knowledge-Based Economy]]"
  - "[[Critical Thinking]]"
  - "[[Preemptive Governance]]"
  - "[[Online Self-Assessment]]"
  - "[[Digital Self]]"
  - "[[Promising Student]]"
  - "[[Gamification]]"
  - "[[Bildung]]"
  - "[[Document]]"
  - "[[Variable]]"
  - "[[Growth]]"
  - "[[Educational Technology Industry]]"
  - "[[Transhumanism]]"
related_theories:
  - "[[Item Response Theory]]"
related_methods:
  - "[[Multiple-Choice Questions]]"
related_instruments:
  - "[[Consensual Assessment Technique]]"
  - "[[Collegiate Learning Assessment]]"
related_persons: []
related_facts:
  - "[[OECD]]"
  - "[[Higher Education Funding Council for England]]"
  - "[[KoKoHs Program]]"
  - "[[TECO Project]]"
related_arguments:
  - "[[Argument_Thompson_2022_Promising_Student]]"
  - "[[Argument_Bouckaert_2023_OECD]]"
  - "[[Argument_Amos_2022_Springer]]"
  - "[[Argument_Jornitz_2022_Bildung_algorithmic]]"
confidence: high
status: completed
created: 2026-05-08
updated: 2026-08-27
---

# Learning Analytics

---

## 定义

> [!def] 核心定义
> 学习分析（Learning Analytics, LA）是指通过对学习者在数字化学习环境中生成的行为轨迹（点击流、停留时长、[[Homework|作业]]提交、交互日志）及[[Academic Achievement|学业表现]]数据进行系统性收集、测量、挖掘与建模，以理解、预测和优化学习过程及其发生环境的技术与教育治理实践。在现代高等教育中，学习分析已从单纯的在线学习行为追踪，进一步扩展为支撑跨学期[[Learning Gain|学习增益]]（Learning Gain）测查与高阶认知素养评估的系统性数据工程。[[Argument_Thompson_2022_Promising_Student|(Thompson et al., 2022, p. 224)]]; [[Argument_Bouckaert_2023_OECD|(Bouckaert, 2023, pp. 17–19)]]

> [!concept-lens] 概念透镜
> - **含义** 包含微观层面的“学习者认知与行为建模（Learner Modeling）”、中观层面的“课程自适应与实时反馈（Adaptive [[Feedback]]）”、以及宏观层面的“机构学业预警与[[Learning Gain|学习增益]]分析”。
> - **用途** 帮助教育者突破传统期末单次考试的黑箱，获得动态、持续的过程性评价证据；在教育治理中为学业预警、自适应推荐及国家级教育干预效果评估提供数据基座。
> - **生产性反思** 学习分析不仅“反映”学习，更通过[[Performativity of Measurement|测量的生产性]]塑造新的等级秩序与主体性认同；算法设定的“[[Digital Optimum|数字最优]]”直接[[Disciplina and Doctrina|规训]]着学生的自我认知与学习策略。[[Argument_Thompson_2022_Promising_Student|(Thompson et al., 2022, p. 225)]]
> - **边界** 区别于纯粹的后台数据统计，学习分析的核心在于服务教学干预与意义理解；若脱离教育学[[Epistemology|认识论]]指导，单纯的算法关联极易退化为[[Data Behaviorism|数据行为主义]]与[[Construct|构念]]代表性不足。

> [!boundary]- 概念边界
> - 不等于 **教育数据挖掘（Educational Data Mining, EDM）** —— EDM 更偏向计算机科学与统计学导向，侧重于算法自动化发现新模式；学习分析更偏向教育学与人类中心导向，侧重于赋能教师与学生解释数据、开展形成性干预。[[Argument_Thompson_2022_Promising_Student|(Thompson et al., 2022, p. 224)]]
> - 不等于 **学术分析（Academic Analytics）** —— 学术分析聚焦高校机构层面的运营效率、招生配额、财务与科研产出指标；学习分析严格聚焦教学法、学习过程与学生认知发展本身。

---

## 概念辨析

> [!contrast-table] 学习分析与相关技术治理[[Paradigm|范式]]辨析
> | 维度 | 学习分析 (Learning Analytics) | 传统标准化测验 (Standardized Testing) | 形成性课堂评价 ([[Formative Assessment]]) |
> |---|---|---|---|
> | **数据源泉** | 动态数字足迹（点击流、交互日志、CBT 反应时） | 静态纸笔或机考终结性答卷（正误得分） | 教师即时口头提问、课堂观察与[[Homework\|作业]]批改 |
> | **分析时间轴** | 持续、实时或纵向跨阶段追踪 | 离散的单次时间截面 | 教学过程中的嵌入式即时发生 |
> | **核心功能** | 预测风险、自适应推送、[[Learning Gain\|学习增益]]测算 | 选拔分流、文凭准入、横向常模排序 | 诊断思维卡点、提供指向下一步的精准反馈 |
> | **潜在危机** | [[Data Behaviorism\|数据行为主义]]、构念代表性不足、主体规训 | 负向反拨诱发应试刷题、忽视能力生成 | 主观偏差、跨班级跨校[[Reliability\|信度]]难以标准化 |

---

## 核心要素

> [!feature] 学习分析的技术与治理核心构件
> - **全息数据追踪与数字海洋（Digital Ocean）** 从传统教育评价的“数字荒漠”跃升为对学习过程细粒度数字痕迹（交互频率、测验耗时、视频回放、讨论区语义）的全面捕获。[[Argument_Thompson_2022_Promising_Student|(Behrens & DiCerbo, 2014; Thompson et al., 2022, p. 224)]]
> - **学习者建模与预测分类（Learner Modeling）** 基于多源认知与行为数据构建预测模型（如 ASAP 分类器），早期识别学业失败风险或高潜能力特质。[[Argument_Thompson_2022_Promising_Student|(Pea, 2014; Thompson et al., 2022, p. 224)]]
> - **纵向[[Learning Gain|学习增益]]测算（Longitudinal Gain Analytics）** 借助[[Computerized Adaptive Testing|计算机自适应测验]]（[[Consensual Assessment Technique|CAT]]）与[[Item Response Theory|项目反应理论]]（IRT），对学生在大学就读期间的[[Higher-Order Thinking Skills|高阶思维]]与跨学科能力增量实施跨年级追踪评估。[[Argument_Bouckaert_2023_OECD|(Bouckaert, 2023, pp. 17–19)]]
> - **仪表盘可视化与即时反馈闭环（Dashboards & [[Feedback]] Loop）** 将复杂算法输出转化为红绿警戒色、进度条与推荐雷达图，驱动个性化自适应学习或辅导员先发制人干预。[[Argument_Amos_2022_Springer|(Amos, 2022, pp. 56–57)]]; [[Argument_Jornitz_2022_Bildung_algorithmic|(Jornitz & Klinge, 2022, pp. 242–245)]]

---

## 围绕概念形成的命题

---

### 命题一　学习分析通过将不可见学习过程数据化表征，重构了教学决策并产生生产性现实

> [!concept-lens] 数据化与[[Performativity of Measurement|测量的生产性]]
> 学习分析不仅是中立的测量工具，它通过量化与指标赋值，创造出关于“好学生/风险学生”的新型等级秩序并深刻重塑师生互动。

> [!claim] Amos; Thompson et al.
> **数据表征重塑教师角色并创造新型价值秩序** 学习分析将教师的直觉观察转化为数据仪表盘指标，使教师从“经验观察者”转变为“数据响应者”；同时，量化过程伴随着价值化（Valorization），通过界定何种行为指标具有高权重，反向塑造了学生的学习策略与机构资源分配。[[Argument_Amos_2022_Springer|(Amos, 2022, p. 57)]]; [[Argument_Thompson_2022_Promising_Student|(Thompson et al., 2022, p. 225)]]

---

### 命题二　学习分析在高等教育质量治理中正从微观点击流转向多维度的纵向“学习增益”评估

> [!concept-lens] 认知能力增益与宏观质量测查
> 面对[[Knowledge-Based Economy|知识经济]]对高阶素养的要求，国家高教治理正利用测试分析技术开展大规模增值性评价，以衡量院校教学对学生高阶能力的实质贡献。

> [!claim] Bouckaert / [[OECD]]
> **[[Learning Gain|学习增益]]分析成为连接国家政策与院校评价的关键工具** 英国 [[Higher Education Funding Council for England|HEFCE]] 学习增益项目（涵盖 70 余所高校）、德国 [[KoKoHs Program|KoKoHs]] 计划 与意大利 [[TECO Project|TECO]] 项目 表明，现代学习分析正将纵向追踪、机考技术与真实量规相结合，用以精准测定[[Critical Thinking|批判性思维]]与通用能力的增益幅度；这不仅推动了高教增值评价的科学化，也倒逼参与高校系统反思其整体教学与考核设计。[[Argument_Bouckaert_2023_OECD|(Bouckaert, 2023, pp. 17–19, 21–22)]]

---

### 命题三　基于算法预判的先发制人治理将学生主体性重构为对标“数字最优”的自我调节机器

> [!concept-lens] 主体性生产与先发制人[[Disciplina and Doctrina|规训]]
> 算法在学生发生实际学业危机前便提前介入，将求助的自主权转化为被动接受算法调制的依附性。

> [!claim] Thompson et al.
> **[[Preemptive Governance|先发制人治理]]重塑有前景学生的主体性** 在 在线自我评估（[[Online Self-Assessment|OSA]]） 等场景中，学习分析在入学前即构建出“[[Digital Self|数字自我]]”并对标“[[Digital Optimum|数字最优]]”；当学生的日常行为偏离最优轨迹时，系统触发先发制人式干预（[[Preemptive Governance|Preemptive Governance]]），迫使个体将自身不断修剪为符合算法预设的“[[Promising Student|有前景的学生]]”，剥夺了学生在真实探索与犯错中生成主体性的空间。[[Argument_Thompson_2022_Promising_Student|(Thompson et al., 2022, pp. 224–226)]]

---

### 命题四　仪表盘与游戏化界面的视觉符号规训可能以行为主义顺从遮蔽深层的知识论理解

> [!concept-lens] 界面认知与算法修养危机
> 仪表盘的颜色警戒与[[Gamification|游戏化]]代币制造了强烈的情绪刺激，容易使学生陷入刷取指标的数字游戏中，背离深度[[Bildung|教化]]（Bildung）。

> [!claim] Jornitz & Klinge
> **视觉符号条件反射侵蚀质性知识反思** 学习分析仪表盘的色彩符号（红黄绿）与[[Gamification|游戏化]]代币（金币、徽章）具有强大的情绪压迫力；学生与教师逐渐被条件化为追求“100% 处于绿色安全区”或累积虚拟代币，算法绕过了复杂的批判性反思与概念理解，使教育退化为遵循指令的[[Data Behaviorism|数据行为主义]]。[[Argument_Jornitz_2022_Bildung_algorithmic|(Jornitz & Klinge, 2022, pp. 242–245)]]

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心理论判定 | 适用分析情境 | 代表学者与[[Document\|文献]] |
> |---|---|---|---|
> | **数据化生产性** | 行为数据表征重构教学角色，创造具有等级划分效力的价值秩序 | 在线学习平台、教师专业发展、EdTech 产业 | [[Argument_Amos_2022_Springer\|Amos (2022)]]; [[Argument_Thompson_2022_Promising_Student\|Thompson et al. (2022, p. 225)]] |
> | **学习增益测查** | 结合机考与量规实现跨阶段追踪，成为高教增值评价核心工具 | 高教质量保障、纵向评估项目（HEFCE/TECO） | [[Argument_Bouckaert_2023_OECD\|Bouckaert (2023, p. 17)]] |
> | **先发制人规训** | 通过数字自我与最优对标实施早期干预，重塑标准化主体性 | 入学在线自测（OSA）、学业预警系统 | [[Argument_Thompson_2022_Promising_Student\|Thompson et al. (2022, p. 226)]] |
> | **视觉符号异化** | 仪表盘警示色与游戏代币诱发条件反射，以行为顺从替代深度教化 | 自适应平台界面（Antolin/bettermarks）、教育游戏化 | [[Argument_Jornitz_2022_Bildung_algorithmic\|Jornitz & Klinge (2022)]] |

---

## 概念演变

> [!dev-timeline] 学习分析发展演进历程
> - **2000 年代中 — 教育数据挖掘（EDM）萌芽** 随着学习管理系统（LMS, 如 Moodle/Blackboard）普及，研究者开始运用关联规则、分类与聚类算法挖掘学生日志数据。
> - **2011 年 — 学习分析（LA）概念正式确立** 首届国际学习分析与知识大会（LAK 2011）召开，正式将 LA 定义为聚焦人类学习理解与优化的交叉学科，与偏重算法的 EDM 形成互补。
> - **2010 年代中 — [[Preemptive Governance|先发制人治理]]与在线自测（[[Online Self-Assessment|OSA]]）应用** 欧美高校将 LA 技术前移至招生与衔接阶段，通过在线自测构建[[Digital Self|数字自我]]并开展先发制人式生源管理。[[Argument_Thompson_2022_Promising_Student|(Thompson et al., 2022, p. 224)]]
> - **2010 年代末 — 国家级[[Learning Gain|学习增益]]（Learning Gain）大规模试验** 英国 [[Higher Education Funding Council for England|HEFCE]]（2014–2018）、德国 [[KoKoHs Program|KoKoHs]] 与意大利 [[TECO Project|TECO]] 运用机考分析与 [[Collegiate Learning Assessment|CLA+]] 等工具开展院校增值测查。[[Argument_Bouckaert_2023_OECD|(Bouckaert, 2023, pp. 17–19)]]
> - **2020 年代至今 — 生成式 AI 时代的多模态分析与高阶素养对齐** 面对大语言模型冲击，学习分析正转向多模态过程性证据整合，探索如何通过真实表现量规克服[[Multiple-Choice Questions|选择题]]分析的[[Construct|构念]]代表性不足。

---

## 争议与批评

> [!debates] 学术争议焦点
>
> > [!axis] 学习分析面临的四大理论与伦理批评
> > - **实证改善学习效果的证据依然薄弱（Lack of Empirical Efficacy）** 尽管 EdTech 产业极力标榜自适应算法的优越性，但独立严谨的大规模实证研究仍未能证实学习分析能显著降低辍学率或提升深层学业理解。[[Argument_Amos_2022_Springer|(Amos, 2022, p. 57)]]
> > - **[[Construct|构念]]代表性不足与意义剥离（Construct Underrepresentation）** 将复杂的思维过程窄化为停留时间、点击频率等易量化代理[[Variable|变量]]，严重遗漏了沉思、困惑、灵感酝酿等难以数字化的深层认知维度。[[Argument_Bouckaert_2023_OECD|(Bouckaert, 2023, pp. 24–25)]]
> > - **先发制人预判的伦理暴力（Ethical Violence of Preemption）** 在学生展示自身潜能之前，算法已依据历史模型为其贴上“高风险”或“缺乏前景”的标签，形成自证预言并加剧教育不平等。[[Argument_Thompson_2022_Promising_Student|(Thompson et al., 2022, pp. 224–225)]]
> > - **对全人[[Bildung|教化]]（[[Bildung]]）开放性的封锁** 教育的本质是指向一个未知且不可预测的自由主体[[Growth|成长]]，而算法决定论则试图将未来锁死在历史数据的概率相关性中。[[Argument_Jornitz_2022_Bildung_algorithmic|(Jornitz & Klinge, 2022, p. 242)]]

---

## 实证数据

> [!ref-table]- 学习分析与增益测查关键实证研究
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 / 项目 | 样本规模与实施情境 | 研究设计与数据源 | 核心考察[[Variable\|变量]] | 原始统计与实证发现 | 解释边界与政策启示 |
> |---|---|---|---|---|---|
> | [[Argument_Bouckaert_2023_OECD\|Bouckaert (2023, pp. 17–19)]] / HEFCE 计划 | 英国 70 余所高校，13 项试验子项目 | 纵向跨阶段追踪与自适应测验 | 本科生通用能力增益与院校增值 | 证实结合 [[Collegiate Learning Assessment\|CLA+]] 等工具可实现跨年级[[Learning Gain\|学习增益]]测查，但对高校内部教学考核方式产[[Growth\|生长]]远反思重塑 | 验证了学习分析从点击流向高阶认知增益分析跃迁的政策可行性 |
> | [[Argument_Bouckaert_2023_OECD\|Bouckaert (2023, p. 18)]] / 意大利 TECO 测评 | 意大利 23 所大学逾 6,000 名本科生 | 机考化纵向能力测评分析 | 跨学科核心通用能力分布 | 成功建立全国性大学生高阶素养基准数据库，为大学质量保障提供跨校可比增益依据 | 展示了全国性机考分析平台在支持高校自我诊断中的效能 |
> | Klinge et al. (2020)（引自 [[Argument_Jornitz_2022_Bildung_algorithmic\|Jornitz & Klinge, 2022, pp. 243–244]]） | 数字健康与学习仪表盘实验参与者 | 质性追踪与用户情绪测量 | 仪表盘色彩符号的情感冲击力 | 即使专家已口头澄清结果无大碍，被仪表盘“红色”标示的参与者仍经历数周焦虑与行为自抑 | 证实仪表盘视觉符号具有压倒理性评估的强烈情感与行为[[Disciplina and Doctrina\|规训]]效应 |

---

## 相关研究

> [!evidence-grid] 相关[[Document|文献]]索引
> - [[Argument_Bouckaert_2023_OECD|Bouckaert (2023)]] — [[OECD]] 国际报告，系统评述 [[Higher Education Funding Council for England|HEFCE]]、[[KoKoHs Program|KoKoHs]]、[[TECO Project|TECO]] 等大规模[[Learning Gain|学习增益]]分析项目，指出机考分析技术在测查高阶素养时的[[Construct|构念]]有效性挑战与政策杠杆。
> - [[Argument_Thompson_2022_Promising_Student|Thompson et al. (2022)]] — 批判性考察在线自我评估（[[Online Self-Assessment|OSA]]）中的学习分析技术，揭示[[Preemptive Governance|先发制人治理]]、[[Digital Self|数字自我]]与“有前景学生”的主体性[[Disciplina and Doctrina|规训]]机制。
> - [[Argument_Amos_2022_Springer|Amos (2022)]] — 剖析[[Educational Technology Industry|教育技术产业]]如何将学习分析包装为教师专业发展工具，指出其实证效益不足与[[Transhumanism|超人类主义]]效率导向。
> - [[Argument_Jornitz_2022_Bildung_algorithmic|Jornitz & Klinge (2022)]] — 探讨算法时代的[[Bildung|教化]]（Bildung）危机，分析仪表盘色彩象征与[[Gamification|游戏化]]代币对学生认知的[[Data Behaviorism|数据行为主义]]驯化。
