import sys

filepath = "wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2018_JEP.md"
with open(filepath, "r") as f:
    text = f.read()

# 1. ES and CI in Table 5
text = text.replace("| [[Effect Size\\|效应量]] (ES) | 95% [[Confidence Interval\\|CI]] |", "| [[Effect Size\\|效应量]]（Effect Size, ES） | 95% [[Confidence Interval\\|置信区间]]（Confidence Interval, CI） |")

# 2. CMA software
text = text.replace("使用 CMA 软件", "使用综合元分析软件（Comprehensive Meta-Analysis, CMA）")

# 3. GPA in Table 13
text = text.replace("| 官方 GPA |", "| 官方平均绩点（Grade Point Average, GPA） |")

# 4. Text in Step 5
old_step_5_text = "领域对口的印第安纳数学信念量表（$r = .421$）和 Conley et al. (2004) 量表（$r = .242$）表现出极强的预测力；而曾经非常流行的 Hofer (2000) DEBQ （$r = .059$）和 Jehng et al. (1993) 问卷（$r = .051$）"
new_step_5_text = "领域对口的印第安纳数学信念量表（Indiana Mathematics Belief Scale, $r = .421$）和 Conley et al. (2004) 问卷（Conley et al. Questionnaire, $r = .242$）表现出极强的预测力；而曾经非常流行的 Hofer (2000) 特定学科认识论信念问卷（Discipline-Focused Epistemological Beliefs Questionnaire, DEBQ，$r = .059$）和 Jehng et al. (1993) 问卷（Jehng et al. Questionnaire, $r = .051$）"
text = text.replace(old_step_5_text, new_step_5_text)

# 5. Table 16 full replacement
old_table = """> [!ma-table]- 表 16：认识论问卷调节变量分析（完整复刻 20 种）
> | 认识论问卷 | k | 效应量 (ES) | 95% CI |
> |---|---|---|---|
> | Indiana Mathematics Belief Scale | 5 | .421 | [.196, .604] |
> | GEBEP | 1 | .284 | [.062, .478] |
> | Conley et al. (2004) Questionnaire | 17 | .242 | [.155, .325] |
> | Epistemic Understanding Inventory (EUI) | 5 | .242 | [.104, .371] |
> | Bråten et al. JFK-Q | 7 | .179 | [.100, .255] |
> | CAEB | 3 | .170 | [.022, .312] |
> | Elder (1999) Questionnaire | 4 | .166 | [.006, .317] |
> | Schommer (1990) EQ | 53 | .156 | [.115, .195] |
> | Schraw et al. (2002) EBI | 17 | .154 | [.044, .259] |
> | Wood & Kardash EBS | 3 | .148 | [.067, .226] |
> | Muis & Royce Psycho-Epistemological Profile | 2 | .131 | [-.026, .282] |
> | Topic-specific Epistemic Beliefs | 6 | .125 | [.051, .198] |
> | Scientific Epistemological Views Scale | 1 | .099 | [-.065, .258] |
> | CEASBQ | 1 | .087 | [-.017, .190] |
> | Hofer (2000) DEBQ | 14 | .059 | [-.016, .133] |
> | Jehng et al. (1993) Questionnaire | 5 | .051 | [-.005, .107] |
> | Hofer's Nature of Mathematics Epistemological Belief Scale | 1 | .040 | [-.054, .133] |
> | Mathematics Epistemological Beliefs Scale | 5 | .035 | [-.158, .226] |
> | EBAPS | 1 | .028 | [-.193, .246] |
> | Epistemic Thinking Assessment | 2 | .006 | [-.124, .136] |"""

new_table = """> [!ma-table]- 表 16：认识论问卷调节变量分析（完整复刻 20 种）
> | 认识论问卷 | k | 效应量 (ES) | 95% CI |
> |---|---|---|---|
> | 印第安纳数学信念量表（Indiana Mathematics Belief Scale） | 5 | .421 | [.196, .604] |
> | 希腊物理认识论信念评估工具（Greek Epistemological Beliefs Evaluation Instrument for Physics, GEBEP） | 1 | .284 | [.062, .478] |
> | Conley et al. (2004) 问卷（Conley et al. Questionnaire） | 17 | .242 | [.155, .325] |
> | 认识论理解量表（Epistemic Understanding Inventory, EUI） | 5 | .242 | [.104, .371] |
> | Bråten et al. 认知证成问卷（Justification for Knowing Questionnaire, JFK-Q） | 7 | .179 | [.100, .255] |
> | 认识论信念内涵方面问卷（Connotative Aspects of Epistemological Beliefs Questionnaire, CAEB） | 3 | .170 | [.022, .312] |
> | Elder (1999) 问卷（Elder Questionnaire） | 4 | .166 | [.006, .317] |
> | Schommer (1990) 认识论问卷（Epistemological Questionnaire, EQ） | 53 | .156 | [.115, .195] |
> | Schraw et al. (2002) 认识论信念量表（Epistemic Belief Inventory, EBI） | 17 | .154 | [.044, .259] |
> | Wood & Kardash 认识论信念量表（Epistemological Belief Scale, EBS） | 3 | .148 | [.067, .226] |
> | Muis & Royce 心理认识论轮廓量表（Psycho-Epistemological Profile） | 2 | .131 | [-.026, .282] |
> | 特定主题认识论信念问卷（Topic-Specific Epistemic Beliefs） | 6 | .125 | [.051, .198] |
> | 科学认识论观点量表（Scientific Epistemological Views Scale） | 1 | .099 | [-.065, .258] |
> | 特定情境认识论目标与来源信念问卷（Context-Specific Epistemic Aims and Source Beliefs Questionnaire, CEASBQ） | 1 | .087 | [-.017, .190] |
> | Hofer (2000) 特定学科认识论信念问卷（Discipline-Focused Epistemological Beliefs Questionnaire, DEBQ） | 14 | .059 | [-.016, .133] |
> | Jehng et al. (1993) 问卷（Jehng et al. Questionnaire） | 5 | .051 | [-.005, .107] |
> | Hofer 数学本质认识论信念量表（Nature of Mathematics Epistemological Belief Scale） | 1 | .040 | [-.054, .133] |
> | 数学认识论信念量表（Mathematics Epistemological Beliefs Scale） | 5 | .035 | [-.158, .226] |
> | 物理科学认识论信念评估工具（Epistemological Beliefs Assessment for Physical Science, EBAPS） | 1 | .028 | [-.193, .246] |
> | 认识论思维评估工具（Epistemic Thinking Assessment） | 2 | .006 | [-.124, .136] |"""

text = text.replace(old_table, new_table)

with open(filepath, "w") as f:
    f.write(text)
