import sys

filepath = "wiki/concepts/educational-psychology/Epistemic Cognition.md"
with open(filepath, "r") as f:
    text = f.read()

greene1_old = """> [!claim] Greene, J.
> **对齐法则与高阶认知强关联** 只有当测量工具的特异性与成绩任务在颗粒度上严格匹配时（如用学科问卷预测特定学科成绩，而非用通用问卷），预测效力才会大幅提升。此外，认识论信念与高阶能力（如概念性知识与论证）的关联远超底层的陈述性/程序性知识。[[Argument_Greene_2018_JEP|(Greene et al., 2018)]]"""

greene1_new = """> [!claim] Greene, J.
> **对齐法则与高阶认知强关联** 实证预测效力依赖于以下法则：
> - **对齐法则（Alignment）**：只有当测量工具的特异性与成绩任务在颗粒度上严格匹配时（如用学科问卷预测特定学科成绩，而非用通用问卷），预测效力才会大幅提升。
> - **高阶认知强关联**：认识论信念与高阶能力（如概念性知识与论证）的关联远超底层的陈述性或程序性知识。[[Argument_Greene_2018_JEP|(Greene et al., 2018)]]"""

greene2_old = """> [!claim] Greene, J.
> **信度决定论与学段倒挂** 问卷的内部一致性信度直接决定了效应量上限（元回归 $b = .300$）。在严谨测量下，初中和小学生（$r = .246, .212$）的整体相关性显著强于大学生（$r = .131$），打破了传统发展模型关于低龄儿童缺乏高级认识论认知的偏见。[[Argument_Greene_2018_JEP|(Greene et al., 2018)]]"""

greene2_new = """> [!claim] Greene, J.
> **信度决定论与学段倒挂** 测量严谨度会暴露出不同于传统的实证规律：
> - **信度决定论**：问卷的内部一致性信度直接决定了效应量上限（元回归 $b = .300$）。
> - **学段倒挂**：在严谨测量下，初中和小学生（$r = .246, .212$）的整体相关性显著强于大学生（$r = .131$），彻底打破了传统发展模型关于低龄儿童缺乏高级认识论认知的偏见。[[Argument_Greene_2018_JEP|(Greene et al., 2018)]]"""

text = text.replace(greene1_old, greene1_new)
text = text.replace(greene2_old, greene2_new)

with open(filepath, "w") as f:
    f.write(text)

