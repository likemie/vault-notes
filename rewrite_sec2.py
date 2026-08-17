import re

with open("wiki/arguments/reports-policy-documents/Argument_Bergeron_2015_TeachingTOK.md", "r", encoding="utf-8") as f:
    content = f.read()

target = """### 2. 知识论对任课群体的影响（Impact on Teachers）

> [!claim] 步骤二主张
> 教学工作是一种高影响的在职专业发展（Professional Development, PD）。它深刻改变了教学哲学，增进了教学信心，并且不同[[Areas of Knowledge|知识领域]]的信心存在显著落差，整体信心随着教龄增长而稳步提升。

> [!chain-link] 证据到判断
> 教学信心量表（[[Confidence Teaching TOK Scale|Confidence Teaching TOK]], [[Classical Test Theory|CTT]]）显示群体极具信心，但信心在八大知识领域（Areas of Knowledge, AOK）的应对上展现出显著梯次：应对伦理学（M=3.60）、人文科学（3.59）和历史（3.59）时信心最高；应对本土知识系统（2.73）、数学（2.83）以及应用[[Knowledge Framework|知识框架]]（2.96）时信心最低。教龄对总体信心有显著的正面影响。

> [!ref-table]- 表 7：不同知识论教龄群体的教学信心得分与事后比较
> 
> | 教龄 | N | 平均分（Mean） | 标准差（SD） | Tukey 事后比较显著性 |
> |------|-----|--------------|-------------|---------------------|
> | 1-3 年 | 289 | 3.17 | 0.47 | 基准组 |
> | 4-9 年 | 274 | 3.35 | 0.42 | 显著高于 1-3 年组 (p<.001) |
> | 10+ 年 | 105 | 3.40 | 0.40 | 显著高于 1-3 年组 (p<.001) |

> [!chain-link] 质性主题支持
> 在教学哲学的转变上，广泛使用了基于讨论、以学生为中心和[[Reflexivity|反思性]]等词汇来描述自身的改变。

> [!example]- 图1：教学哲学编码词频图
> ![](https://img.mylikemie.icu/sources/Bergeron_2015_TeachingTOK/figures/Bergeron_2015_TeachingTOK_Fig1_Word_frequency_display.jpg)

> [!ref-table]- 表 9：与知识论对教师影响相关的主题与编码
> 
> | 主题（Theme） | 编码（Codes） | 引用示例（Illustrative quotes） |
> |---|---|---|
> | **改进教学（Improves teaching）** | 增进教师理解；改进教学法 | “知识论也发展了教学法。我清楚在课堂方法上我[[Growth\|成长]]了多少...当我开始沉浸于 IB 哲学时，我发现它们是思维的常规，是一种结构化的探究方式。” |
> | **教学方法（Methods）** | 以学生为中心的哲学；明确教授技能；文本支持；基于讨论 | “这是一次反思学生所学内容的机会...这是一个建立跨课程联系的机会，让他们反思知识本身和构成知识的基础底蕴。” |
> | **合作（Collaboration）** | 在材料和活动的开发中合作；客座讲师；分享专业知识；团队教学 | “我认为大家坐在一起真正尝试共同开发想法并从不同视角看待它，实际上是非常有趣的。” |"""

replacement = """### 2. 知识论对任课群体的影响（Impact on Teachers）

> [!claim] 步骤二主张
> 教学工作本身构成了一种高影响的在职专业发展（Professional Development, PD）。它深刻改变了教师的教学哲学，促使其拥抱课程改革。然而，对庞杂知识体系的掌握随着不同[[Areas of Knowledge|知识领域]]（AOKs）呈现显著落差。

> [!evidence-grid] 支持论断的证据
> - **量表单一维度的高效度** 探索性因子分析（EFA）确认教学信心量表可作为单一维度评估（Cronbach's $\alpha = 0.798$），验证了群体信心随着教龄的稳步攀升（见表3、4、7）。
> - **知识领域的显著信心梯次** 应对伦理学（M=3.60）信心最高；应对本土知识系统（2.73）和数学（2.83）信心最低。
> - **积极拥抱课程变革** 对知识论近期变革表现出显著的积极接纳态度，绝大多数认为认知方式（WOKs）和知识领域（AOKs）的修改提升了课程质量（表10）。
> - **教学理念从传递转向探究** 质性访谈揭示了“以学生为中心”、“反思性”、“基于讨论”的教学模式转变（图1与表9）。

> [!stat-cards]- 量表信效度与改革支持度
> - **$\alpha$ = 0.798** 包含 11 个题项的教学信心量表（CTT）展现了良好的内部一致性（表3，表4）。
> - **M=3.32** 对“近期 WOKs 的改变提升了 TOK 课程”的认同度，M=3.28 对 AOKs 改变的认同度（4 分制，N=695），显示高度的改革支持（表10）。

> [!ref-table]- 表 10：对知识论近期变革的描述性统计
> 
> | 题项 | 总量（Total） | 均值（Mean） | 标准差（SD） |
> |---|---|---|---|
> | 近期 WOKs 的改变提升了 TOK 课程 | 695 | 3.32 | 0.86 |
> | 近期 AOKs 的改变提升了 TOK 课程 | 692 | 3.28 | 0.86 |
> | 近期知识框架的改变提升了 TOK 课程 | 691 | 3.27 | 0.88 |

> [!ref-table]- 表 7：不同知识论教龄群体的教学信心得分与事后比较
> 
> | 教龄 | N | 平均分（Mean） | 标准差（SD） | Tukey 事后比较显著性 |
> |------|-----|--------------|-------------|---------------------|
> | 1-3 年 | 289 | 3.17 | 0.47 | 基准组 |
> | 4-9 年 | 274 | 3.35 | 0.42 | 显著高于 1-3 年组 (p<.001) |
> | 10+ 年 | 105 | 3.40 | 0.40 | 显著高于 1-3 年组 (p<.001) |

---

> [!example]- 图1：教学哲学编码词频图
> ![](https://img.mylikemie.icu/sources/Bergeron_2015_TeachingTOK/figures/Bergeron_2015_TeachingTOK_Fig1_Word_frequency_display.jpg)

> [!ref-table]- 表 9：与知识论对教师影响相关的主题与编码
> 
> | 主题（Theme） | 编码（Codes） | 引用示例（Illustrative quotes） |
> |---|---|---|
> | **改进教学（Improves teaching）** | 增进教师理解；改进教学法 | “知识论也发展了教学法。我清楚在课堂方法上我[[Growth\|成长]]了多少...当我开始沉浸于 IB 哲学时，我发现它们是思维的常规，是一种结构化的探究方式。” |
> | **教学方法（Methods）** | 以学生为中心的哲学；明确教授技能；文本支持；基于讨论 | “这是一次反思学生所学内容的机会...这是一个建立跨课程联系的机会，让他们反思知识本身和构成知识的基础底蕴。” |
> | **合作（Collaboration）** | 在材料和活动的开发中合作；客座讲师；分享专业知识；团队教学 | “我认为大家坐在一起真正尝试共同开发想法并从不同视角看待它，实际上是非常有趣的。” |"""

content = content.replace(target, replacement)
with open("wiki/arguments/reports-policy-documents/Argument_Bergeron_2015_TeachingTOK.md", "w", encoding="utf-8") as f:
    f.write(content)
