import sys

filepath = "wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2018_JEP.md"
with open(filepath, "r") as f:
    text = f.read()

text = text.replace(">\n> [!ma-table]", "\n> [!ma-table]")

old_12_13 = """> [!ma-table]- 表 12-13：成就类型与成就测量工具调节分析
> | 调节变量分类 | 类别 (Levels) | k | 效应量 (ES) | 95% CI |
> |---|---|---|---|---|---|
> | **表12：成就类型** | 论证 (Argumentation) | 12 | .154 | [.081, .226] |
> | | 概念性知识 (Conceptual knowledge) | 11 | .190 | [.073, .301] |
> | | 一般知识 (General knowledge) | 126 | .160 | [.132, .188] |
> | | 陈述性知识 (Declarative knowledge) | 7 | .127 | [.053, .200] |
> | | 程序性知识 ([[Procedural Knowledge]]) | 2 | .077 | [-.102, .251] |
> | **表13：成就测量方式**| 标准化测试 (Standardized test) | 14 | .214 | [.110, .312] |
> | | 研究者开发 (Researcher developed) | 61 | .177 | [.127, .227] |
> | | 官方 GPA (GPA official) | 17 | .139 | [.035, .240] |
> | | 参与者自报 (Participant reported) | 13 | .083 | [.018, .147] |"""

new_12_13 = """> [!ma-table]- 表 12：成就类型调节变量分析
> | 成就类型 | k | 效应量 (ES) | 95% CI |
> |---|---|---|---|
> | 论证 | 12 | .154 | [.081, .226] |
> | 概念性知识 | 11 | .190 | [.073, .301] |
> | 一般知识 | 126 | .160 | [.132, .188] |
> | 陈述性知识 | 7 | .127 | [.053, .200] |
> | 程序性知识 | 2 | .077 | [-.102, .251] |

> [!ma-table]- 表 13：成就测量方式调节变量分析
> | 成就测量方式 | k | 效应量 (ES) | 95% CI |
> |---|---|---|---|
> | 标准化测试 | 14 | .214 | [.110, .312] |
> | 研究者开发 | 61 | .177 | [.127, .227] |
> | 官方 GPA | 17 | .139 | [.035, .240] |
> | 参与者自报 | 13 | .083 | [.018, .147] |"""

text = text.replace(old_12_13, new_12_13)

old_15_16 = """> [!ma-table]- 表 15-16：方法论调节变量分析（同行评审与问卷类型）
> | 调节变量分类 | 类别 (Levels) | k | 效应量 (ES) | 95% CI |
> |---|---|---|---|---|---|
> | **表15：同行评审状态**| 同行评审期刊 (Peer reviewed) | 114 | .175 | [.145, .204] |
> | | 非同行评审 (Not peer reviewed) | 27 | .132 | [.049, .213] |
> | | 会议论文 (Conference proceeding) | 10 | .097 | [.056, .138] |
> | **表16：认识论问卷** | Indiana mathematics belief scale | 5 | .421 | [.196, .604] |
> | *(部分关键问卷)* | Conley et al. Q | 17 | .242 | [.155, .325] |
> | | Bråten JFK-Q | 7 | .179 | [.100, .255] |
> | | Schommer EQ | 53 | .156 | [.115, .195] |"""

new_15_16 = """> [!ma-table]- 表 15：同行评审状态调节变量分析
> | 同行评审状态 | k | 效应量 (ES) | 95% CI |
> |---|---|---|---|
> | 同行评审期刊 | 114 | .175 | [.145, .204] |
> | 非同行评审 | 27 | .132 | [.049, .213] |
> | 会议论文 | 10 | .097 | [.056, .138] |

> [!ma-table]- 表 16：认识论问卷调节变量分析（部分关键问卷）
> | 认识论问卷 | k | 效应量 (ES) | 95% CI |
> |---|---|---|---|
> | Indiana mathematics belief scale | 5 | .421 | [.196, .604] |
> | Conley et al. Q | 17 | .242 | [.155, .325] |
> | Bråten JFK-Q | 7 | .179 | [.100, .255] |
> | Schommer EQ | 53 | .156 | [.115, .195] |"""

text = text.replace(old_15_16, new_15_16)

with open(filepath, "w") as f:
    f.write(text)
