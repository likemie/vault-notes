import sys

filepath = "wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2018_JEP.md"
with open(filepath, "r") as f:
    text = f.read()

old_step_5 = """### 步骤五：方法学影响与信度决定论

> [!claim] 测量的可靠性是决定关联强度的底层方法学因素
> 剥开理论外衣，工具本身的设计方法（同侪评审状态、测量信度以及所选用的问卷类型）极大地决定了最终效应量的上限。

> [!chain-link] 证据到判断
> - **同行评审的质量门槛效应** 经过同行评审的[[Document|文献]]由于数据清洗和审稿标准更严，其报告的效应量（$r = .175$）明显高于未经同行评审（$r = .132$）或会议论文（$r = .097$）。
> - **问卷方差极大** 从 Table 16 可以看出，使用印第安纳数学信念量表（$r = .421$）和 Conley 等人的量表（$r = .242$）能抓取极强的相关性，而早期多维模型代表作 Hofer DEBQ （$r = .059$）的整体效应竟然不显著异于 0。
> - **致命的信度回归** 元回归分析显示，测量工具的[[Internal Consistency|内部一致性]]信度极大地预测了效应量大小（$b = .300, p < .001$）。

> [!ma-table]- 表 15：同行评审状态调节变量分析
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

new_step_5 = """### 步骤五：方法学影响与信度决定论

> [!claim] 测量的可靠性是决定关联强度的底层方法学因素
> 剥开理论外衣，工具本身的设计方法（同侪评审状态、测量信度以及所选用的特定问卷）极大地决定了最终效应量的上限。元回归分析揭示了一个惊人的事实：信度才是王道。

> [!chain-link] 证据到判断
> - **同行评审的质量门槛** 经过同行评审的期刊文献（$r = .175$）由于数据清洗和质量把控更严，其报告的效应量显著高于学术会议论文（$r = .097$），两者的 95% CI 互不重叠。
> - **问卷效力的巨大方差** 当样本量 $k > 5$ 时，各问卷捕获的效应量存在天壤之别。领域对口的印第安纳数学信念量表（$r = .421$）和 Conley 科学量表（$r = .242$）表现出极强的预测力；而曾经非常流行的 Hofer DEBQ （$r = .059$）和 Jehng 问卷（$r = .051$）的整体效应竟然在统计学上不显著异于 0。
> - **决定性的“信度回归”** 元回归（Meta-regression）分析揭示，问卷的[[Internal Consistency|内部一致性信度]]直接决定了效应量大小（$b = .300, p < .001$）。在这个回归模型中，如果一份问卷的信度是 0，那么它与成绩的相关性也会归 0；而如果一份问卷的信度达到完美的 1.0，它与成绩的预期相关性将高达 $r = .300$！

> [!ma-table]- 表 15：同行评审状态调节变量分析
> | 同行评审状态 | k | 效应量 (ES) | 95% CI |
> |---|---|---|---|
> | 同行评审期刊 | 114 | .175 | [.145, .204] |
> | 非同行评审 | 27 | .132 | [.049, .213] |
> | 会议论文 | 10 | .097 | [.056, .138] |

> [!ma-table]- 表 16：认识论问卷调节变量分析（完整复刻 20 种）
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

text = text.replace(old_step_5, new_step_5)

with open(filepath, "w") as f:
    f.write(text)
