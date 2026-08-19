import sys

with open("wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2018_JEP.md", "r") as f:
    lines = f.readlines()

new_content = """> [!ma-table]- 表 8：学术领域调节变量分析
> | 学术领域 | k | 效应量 (ES) | 95% CI |
> |---|---|---|---|
> | 科学 | 49 | .199 | [.153, .243] |
> | 数学 | 19 | .157 | [.026, .282] |
> | 跨领域/通用 | 61 | .143 | [.107, .178] |
> | 心理学 | 8 | .123 | [.062, .182] |
>
> [!ma-table]- 表 9：问卷特异性调节变量分析
> | 问卷特异性 | k | 效应量 (ES) | 95% CI |
> |---|---|---|---|
> | 领域特定 | 67 | .184 | [.137, .230] |
> | 领域通用 | 81 | .140 | [.108, .172] |
> | 主题特定 | 9 | .098 | [.046, .149] |
>
> [!ma-table]- 表 10：特异性（颗粒度）对齐调节变量分析
> | 特异性对齐情况 | k | 效应量 (ES) | 95% CI |
> |---|---|---|---|
> | 颗粒度对齐 | 110 | .176 | [.144, .208] |
> | 颗粒度错配 | 55 | .130 | [.089, .171] |
>
> [!ma-table]- 表 11：学术领域（情境）对齐调节变量分析
> | 学术领域对齐情况 | k | 效应量 (ES) | 95% CI |
> |---|---|---|---|
> | 领域对齐 | 119 | .179 | [.145, .211] |
> | 领域错配 | 44 | .111 | [.075, .147] |
"""

# Replace lines 290 to 305
lines[289:306] = [new_content]

with open("wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2018_JEP.md", "w") as f:
    f.writelines(lines)
