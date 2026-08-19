import sys

filepath = "wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2018_JEP.md"
with open(filepath, "r") as f:
    text = f.read()

old_table = """> [!ma-table]- 表 16：认识论问卷调节变量分析（完整复刻 20 种）
> | 认识论问卷 | k | 效应量 (ES) | 95% CI |
> |---|---|---|---|
> | Indiana mathematics belief scale | 5 | .421 | [.196, .604] |
> | GEBEP | 1 | .284 | [.062, .478] |
> | Conley et al. Q | 17 | .242 | [.155, .325] |
> | Epistemic understanding inventory | 5 | .242 | [.104, .371] |
> | Bråten JFK-Q | 7 | .179 | [.100, .255] |
> | CAEB | 3 | .170 | [.022, .312] |
> | Elder Q | 4 | .166 | [.006, .317] |
> | Schommer EQ | 53 | .156 | [.115, .195] |
> | Schraw et al. EBI | 17 | .154 | [.044, .259] |
> | Wood & Kardash EBS | 3 | .148 | [.067, .226] |
> | Muis/Royce psycho-epistemological profile | 2 | .131 | [-.026, .282] |
> | Topic-specific epistemic beliefs | 6 | .125 | [.051, .198] |
> | Scientific epistemological views scale | 1 | .099 | [-.065, .258] |
> | CEASBQ | 1 | .087 | [-.017, .190] |
> | Hofer DEBQ | 14 | .059 | [-.016, .133] |
> | Jehng et al. Questionnaire | 5 | .051 | [-.005, .107] |
> | Hofer's nature of mathematics epistemological belief scale | 1 | .040 | [-.054, .133] |
> | Mathematics epistemological beliefs scale | 5 | .035 | [-.158, .226] |
> | EBAPS | 1 | .028 | [-.193, .246] |
> | Epistemic thinking assessment | 2 | .006 | [-.124, .136] |"""

new_table = """> [!ma-table]- 表 16：认识论问卷调节变量分析（完整复刻 20 种）
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

text = text.replace(old_table, new_table)
with open(filepath, "w") as f:
    f.write(text)

