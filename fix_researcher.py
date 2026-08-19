import sys

filepath = "wiki/concepts/educational-psychology/Academic Achievement.md"
with open(filepath, "r") as f:
    text = f.read()

text = text.replace("采用标准化测试（$r = .214$）和研究者专门开发的测试（$r = .177$）", "采用标准化测试（$r = .214$）和专门开发的测试（$r = .177$）")
text = text.replace("随着理论的深化，研究者开始将笼统的学业成就拆解为程序性", "随着理论的深化，笼统的学业成就开始被拆解为程序性")
text = text.replace("在极大量的实证研究中，研究者出于便利而收集学生主观自报的成绩（self-reported grades）。元分析证实，这类数据充满主观偏差，相比于", "在极大量的实证研究中，出于便利而收集的学生主观自报成绩（self-reported grades）往往充满主观偏差。元分析证实，相比于")
text = text.replace("通过将其操作化为具体的成绩指标（GPA、考分），来倒推和验证不同认知构念对学习深度的预测能力", "将其操作化为具体的成绩指标（GPA、考分）后，可倒推和验证不同认知构念对学习深度的预测能力")

with open(filepath, "w") as f:
    f.write(text)

