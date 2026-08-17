import re

with open("wiki/arguments/reports-policy-documents/Argument_Bergeron_2015_TeachingTOK.md", "r", encoding="utf-8") as f:
    content = f.read()

target = """> [!chain-link] 目标排序与对学生的益处
> 在对总体目的的量化排序中（见表16），前三名分别为：建立对知识构建方式的认识；在学科间和知情行之间建立连接；识别并反思个人[[Hypothesis|假设]]。而排在最后的是“为进一步学习做准备”。在探讨“益处”的量化排序中（见表17），“批判性评估知识”同样居首。在更深层的开放式回应中（表5），除了批判性评估知识外，教师频繁补充了“国际情怀（international mindedness）”。值得注意的是，“不论断他人（not judging他人（not judging others）”和“挑战自我中心思维”构成了国际情怀形成过程中的重要基石。"""

replacement = """> [!chain-link] 目标排序与对学生的益处
> - **链节一：重认知建构而非实用工具**
>   在对总体目的的量化排序中（见表16），“建立对知识构建方式的认识”位居榜首，排在最后的是纯粹实用的“为进一步学习做准备”。
> - **链节二：批判性思维向跨学科溢出**
>   在探讨“益处”的量化排序中（见表17），“批判性评估知识”居首。表5显示这种批判性思维跨学科溢出到了扩展论文（EE）和其他 DP 科目中。
> - **链节三：形塑参与式国际公民特质**
>   焦点小组补充了“国际情怀（international mindedness）”。值得注意的是，“不论断他人（not judging others）”和“挑战自我中心思维”构成了国际情怀形成过程中的重要基石。

> [!voice] 焦点小组的“改变人生”时刻
> 一旦学生开始建立认知方式和知识领域的联系，“这种状态就无法逆转（that bell can't be unrung）”。在一些学校它甚至变成了动词——“你被知识论了（you have been TOKed）”。（p. 25）"""

content = content.replace(target, replacement)

target2 = """> [!chain-link] 挑战、精力耗费与成功要素
> 在所有的挑战中，评估学习环节耗费精力最大（M=7.47，满分10分），显著高于备课（7.25）和实际上课实施（6.17）。与有明确客观答案的科目不同，评价学生[[Epistemology|认识论]]思维的隐性过程过于主观。另一方面，量化调查显示 86.5% 的参与者明确表示享受教学，且在影响课程成功的最重要因素排名中，“任课群体的兴趣”高居榜首。"""

replacement2 = """---

> [!chain-link] 挑战、精力耗费与成功要素
> - **链节一：主观性引发评价困境**
>   在所有的挑战中，评估学习环节耗费精力最大（M=7.47，满分10分），显著高于备课（7.25）和实际上课实施（6.17）。评价学生[[Epistemology|认识论]]思维的隐性过程具有高度主观性。
> - **链节二：群体热情对冲系统阻力**
>   尽管评价困难重重，量化调查显示 86.5% 的参与者明确表示享受教学，且在影响课程成功的最重要因素排名中，“任课群体的兴趣”高居榜首（M=2.89）。"""

content = content.replace(target2, replacement2)

with open("wiki/arguments/reports-policy-documents/Argument_Bergeron_2015_TeachingTOK.md", "w", encoding="utf-8") as f:
    f.write(content)
