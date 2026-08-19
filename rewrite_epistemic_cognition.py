import re

filepath = "wiki/concepts/educational-psychology/Epistemic Cognition.md"
with open(filepath, "r") as f:
    text = f.read()

# I will replace everything after the `---` (end of frontmatter).
frontmatter_match = re.search(r'^---.*?^---\n', text, re.MULTILINE | re.DOTALL)
if frontmatter_match:
    frontmatter = frontmatter_match.group(0)
else:
    frontmatter = ""

new_content = """# Epistemic Cognition
（认识论认知）

> [!abstract] 定义与内涵
> [[Epistemic Cognition|认识论认知]]是指个体在获取、理解、证成和运用知识时，对“知识本质”（知识是什么）和“认知过程”（如何获得知识）的潜在信念、标准与思维过程。它回答了学习者内心深处的终极问题：“我如何知道我所知道的是真的？”
>
> 相比于早期文献中常用的“认识论信念（Epistemological Beliefs）”，当前的“认识论认知（Epistemic Cognition）”是一个更为宽泛且具包容性的伞形术语。它不再假定个体头脑中存在一套像特质一样稳固、脱离情境的“信念组合”，而是强调认知过程的动态性、情境性和社会互动性。

> [!feature] 核心排他性特征
> 并非所有的高阶认知活动都属于认识论认知。[[Argument_Chinn_2011_EP|(Chinn et al., 2011)]] 明确了其排他性边界：
> - **必须受认识目标（Epistemic Aims）驱动**：其核心动机必须是为了追求真实（truth）、避免虚假（avoiding falsehood）、或获取合理的理解（justified understanding）。
> - **非认识论倾向（Nonepistemic Dispositions）**：如果目标仅仅是指向展示口才、打发时间或单纯的思考乐趣（例如享受辩论的智力挑战，但仅为了赢得比赛），则缺乏追求真理的纯粹偏好，不属于认识论认知。

> [!critique-logic] 理论延伸：批判性思维的两种形态
> 认识论认知构成了**建构性批判（Constructive Critique）**的核心支撑。传统教育常将[[Critical Thinking|批判性思维]]简化为“无差别的怀疑一切”（即缺乏确证标准支撑的表面质疑），这极易使学习者陷入认识论虚无主义（盲目抬杠或愤世嫉俗）。而成熟的认识论认知能够引导学习者进行**合理信任（Calibrated Trust）**，在面对复杂冲突信息时，既不盲从权威，也不盲目拒斥。

---

## 理论流派的演进与核心模型

半个多世纪以来，认识论认知的理论模型经历了从宏大发展阶段到微观情境资源的剧烈演变。[[Argument_Greene_2018_JEP|Greene et al. (2018)]] 将该领域的理论发展总结为四大核心流派：

> [!taxonomy] 认识论认知的四大历史流派
> - **发展论模型（Developmental Models）**：源自 Perry (1970) 和 Kuhn (1991)，认为个体的认识论经历从“绝对主义（非黑即白）”到“多元主义（相对主义）”再到“评价主义（基于证据的客观评价）”的线性发展。
> - **独立信念系统（Independent Beliefs）**：由 Schommer (1990) 提出，打破了单维发展观，认为认识论是由多个独立维度（如知识的确定性、简单性、学习的来源等）组成的系统，这些维度不必同步发展。
> - **认识论资源库（Epistemic Resources）**：以 Elby & Hammer (2001) 为代表，彻底摒弃了宏大的稳定信念假设，主张认知是微观的、细粒度的“资源”，个体在面对不同情境时会瞬间激活不同的资源组合。
> - **整合框架（Integrated Frameworks）**：以 Hofer & Pintrich (1997) 以及近期的 Chinn、Sandoval 等人为代表，试图弥合稳定信念与情境资源之间的鸿沟。

在当代的整合框架中，最具代表性的是以下两大模型：

### Chinn (2011) 扩展五组件框架
> [!feature] 认识论认知的微观构成
> - **认识目标与价值（Epistemic Aims & Epistemic Value）**：探究中追求真理或仅仅是最低限度确证等目标及其价值评估。
> - **知识结构（Structure of Knowledge）**：包括普遍性与特殊性、决定论与随机性，以及具体的认识论形式（如生物学机制、因果模型）。
> - **来源与确证（Sources and Justification）**：知识来源呈现交互特征（涵盖感知、推理、证词），不同情境下界定好证据或好解释的确证标准差异巨大。
> - **认识论美德与恶习（Epistemic Virtues and Vices）**：思想开放、理智勇气等促进认识目标的性格倾向。
> - **可靠与不可靠的过程（Reliable and unreliable processes）**：涵盖产生信念的因果过程（如同行评审、科学实验）及其有效性前提条件的判定。

### Sandoval (2016) 整合多元主义层级框架
> [!framework-table] 聚合层级分类
> | 分析层级 | 关注焦点 | 认识论认知的本体形态 | 研究方法偏好 |
> |---|---|---|---|
> | **个体层级（Individual）** | 学生头脑内部的认知结构 | 个体调配的细粒度“认识论资源” | 改良调查表工具、认知访谈 |
> | **人际交互（Individual-in-interaction）** | 微观的社会互动过程 | 小组内协商共同的认识论目标与标准 | 话语分析、行为观察 |
> | **活动系统（Activity System）** | 宏观文化与制度规范 | 课堂或科学共同体整体的“认识论氛围” | 民族志、制度话语分析 |

---

## 核心实证法则

关于认识论认知如何真正影响学生的[[Academic Achievement|学业成就]]，近期的系统元分析 [[Argument_Greene_2018_JEP|(Greene et al., 2018)]] 揭示了以下四大实证法则：

> [!findings] 预测学业成就的四大法则
> - **对齐（Alignment）法则**：当测量工具的特异性与其预测的成绩任务在颗粒度上严格匹配时，预测效力大幅提升。用通用问卷预测总体 GPA，用学科问卷预测特定学科成绩，是唯一正确的实证路径。
> - **高阶认知强关联**：认识论信念与高阶能力（概念性知识 $r = .190$，论证能力 $r = .154$）的相关性，远高于底层的陈述性/程序性知识。
> - **学段的“反直觉”倒挂**：初中生（$r = .246$）和小学生（$r = .212$）的整体相关性不仅强于大学生（$r = .131$），且置信区间互不重叠。这有力反驳了“低龄儿童缺乏高级认识论认知”的传统偏见。
> - **信度决定论（Reliability Determinism）**：问卷的内部一致性信度极大地预测了效应量大小（元回归 $b = .300, p < .001$）。测量工具设计得越严谨，越能捕捉到真实的认知影响。

---

## 争议与批评

> [!tension] 本体论断层：知识与认知是如何存在的？
> - **认知建构学说（蓝方）**：以 Piaget 发生认识论为基础，视知识为个体为适应经验而建构的内部概念结构，认识论认知是头脑中的相对稳定的信念或特质。[[Argument_Sandoval_2016_RRE|(Sandoval et al., 2016)]]
> - **情境主义立场（红方）**：受 Vygotsky 影响，视知识为分布式的文化产物，认识论认知不再是脱域命题，而是特定共同体解决问题的“社会实践活动（social practices）”。[[Argument_Sandoval_2016_RRE|(Sandoval et al., 2016)]]

> [!tension] 颗粒度危机：普遍性还是高度情境性？
> - **宏大领域特质论（蓝方）**：认为认识论具有宏大跨学科（如科学、历史）间的特异性，但在学科内部保持稳定状态。主张通过标准化问卷测量总体特征。
> - **微观资源库理论（红方）**：摒弃大颗粒度维度，主张认知是微观的“框架与资源”。面对同一学科文本，个体的确证标准也会随当下任务目标发生剧烈切换，传统通用量表根本无法捕捉这种动态。[[Argument_Sandoval_2016_RRE|(Sandoval et al., 2016)]]

> [!critique] 方法论推论危机
> - **脱域困境**：建构派广泛使用的标准化自陈量表将缄默（tacit）的知识强行脱离语境显性化，犯了认识论错误；且部分宣称测量“一般性”认识论的问卷，仅仅是因为题目数量庞杂而在统计学上推高了 Alpha 信度系数，掩盖了构念效度的薄弱。[[Argument_Greene_2018_JEP|(Greene et al., 2018)]]
> - **内部推论黑箱**：情境派崇尚的纯外部话语分析虽保留了真实情境，却陷入了仅靠表面行为流难以准确推断内部隐蔽机制的“推论危机（inference problem）”。这迫使该领域不得不转向混合方法的三角验证。[[Argument_Sandoval_2016_RRE|(Sandoval et al., 2016)]]

---

## 实证数据

> [!ma-table]- [[Meta-analysis|元分析]]总体结果
> <span class="concept-meta-analysis-table-marker" aria-hidden="true"></span>
>
> | 元分析 | [[Dependent Variable\|结果变量]] | k / N | 效应指标与模型 | 汇总效应与 95% [[Confidence Interval\|CI]] | [[Heterogeneity\|异质性]]与预测区间 | 证据确定性 |
> |---|---|---|---|---|---|---|
> | [[Argument_Greene_2018_JEP\|Greene et al. (2018)]] | [[Academic Achievement\|学业成就]] | 151 / 55,418 | r；随机效应 | 0.162 [0.135, 0.189] | I²=88.77%，Q=1335.22 | — |

> [!ma-table]- 调节[[Variable|变量]]与亚组分析
> <span class="concept-meta-moderator-table-marker" aria-hidden="true"></span>
>
> | 元分析 | 调节变量 | 分析方式 | 效应较大的条件或方向 | 条件效应或 β | 交互或回归检验 | 是否预设 | 解释边界 |
> |---|---|---|---|---|---|---|---|
> | [[Argument_Greene_2018_JEP\|Greene et al. (2018)]] | 教育阶段 | 亚组分析 | 初中（r=.246）和混合阶段（r=.233）较大，大学（r=.131）较小 | — | Q_between = 15.111 (p<.05) | 预设 | — |
> | [[Argument_Greene_2018_JEP\|Greene et al. (2018)]] | 成就类型 | 亚组分析 | 概念性知识（r=.190）和论证（r=.154）较高，程序性知识（r=.077，不显著）较低 | — | Q_between = 1.766 (p>.05) | 预设 | — |
> | [[Argument_Greene_2018_JEP\|Greene et al. (2018)]] | [[Epistemology\|认识论]][[Construct\|构念]] | 亚组分析 | 知识发展（r=.274）、一般认识论认知（r=.266）、多种证成（r=.225）较高 | — | Q_between = 57.955 (p<.001) | 预设 | — |

> [!ma-table]- 稳健性与偏倚
> <span class="concept-meta-robustness-table-marker" aria-hidden="true"></span>
>
> | 元分析 | 敏感性分析 | [[Publication Bias\|发表偏倚]]方法 | 校正后效应 | 结论是否改变 | 风险说明 |
> |---|---|---|---|---|---|
> | [[Argument_Greene_2018_JEP\|Greene et al. (2018)]] | — | 漏斗图，Trim-and-fill，Fail-safe N | 0.162 | 稳定 | Fail-safe N=9265，未发现发表偏倚 |

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Chinn_2011_EP|Chinn et al. (2011)]] — 包含五个组件的扩展认识论认知框架推动了研究向细粒度和情境化方向发展。
> - [[Argument_Sandoval_2016_RRE|Sandoval et al. (2016)]] — 系统梳理了该领域的四大理论断层（本体论、情境性、发展轨迹、方法论），并提出了打通个体、互动与系统层级的“整合多元主义”主张。
> - [[Argument_Greene_2018_JEP|Greene et al. (2018)]] — 提供了一项大规模的元分析，评估了认识论认知对学业成就的预测效应，澄清了信度与对齐规则的核心地位。
"""

with open(filepath, "w") as f:
    f.write(frontmatter + new_content)
