import sys

with open("wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2018_JEP.md", "r") as f:
    lines = f.readlines()

new_content = """> [!ma-table]- 表 6：理论模型[[Moderator Analysis|调节变量分析]]（完整复刻）
> | 核心理论模型 | k | 效应量 (ES) | 95% CI | Q 值 |
> |---|---|---|---|---|
> | 哲学驱动模型 (Chinn) | 1 | .087 | [-.017, .190] | .000 |
> | 建构主义 (Constructivism) | 12 | .240 | [.071, .396] | 324.381 |
> | 整合模型 (Greene/Bråten) | 8 | .189 | [.112, .264] | 11.500 |
> | 学科模型 (Hammer) | 4 | .166 | [.006, .317] | 6.778 |
> | 多维模型 (Hofer & Pintrich) | 46 | .158 | [.119, .197] | 374.182 |
> | 发展模型 (Kuhn) | 7 | .142 | [-.003, .280] | 13.416 |
> | 哲学驱动模型 (Muis et al. Royce) | 2 | .131 | [-.026, .282] | .238 |
> | 多维模型 (Schommer/Schommer-Aikins) | 72 | .144 | [.107, .181] | 491.088 |

> [!ma-table]- 表 7：认识论构念调节变量分析（完整复刻及内涵解释）
> | 认识论构念 (Epistemic cognition construct) | 构念内涵解释 | k | 效应量 (ES) | 95% CI |
> |---|---|---|---|---|
> | **知识的发展 (Development of knowledge)** | 认识到知识是不断演化和发展的（第一梯队） | 18 | .274 | [.180, .363] |
> | **一般认识论认知 (General epistemic cognition)** | 将多维度的不同信念加总求和的整体得分 | 14 | .266 | [.097, .420] |
> | **Kuhn 的发展层次 (Kuhn's levels)** | 测试学生所处阶段（绝对主义/多元主义/评价主义） | 5 | .241 | [.105, .369] |
> | **知识的证成 (Justification of knowledge)** | 关注如何评估知识主张以及何种证据能使其成立 | 26 | .228 | [.160, .294] |
> | **多源证成 (Multiple justification)** | 认为需要整合多个来源的证据来交叉验证知识 | 7 | .225 | [.139, .308] |
> | **学习速度 (Quick learning)** | 认为学习要么很快发生，要么永远学不会（归为智力内隐） | 52 | .199 | [.146, .252] |
> | **建构主义 (Constructivism)** | 认为学习是主动建构意义的过程（已被证实存在概念混杂） | 22 | .191 | [.098, .281] |
> | **知识的来源 (Source of knowledge)** | 关注知识是来自外部权威赋权还是由个人内部建构 | 29 | .174 | [.089, .256] |
> | **个人证成 (Personal justification)** | 倾向于基于个人经验、观点或直觉来证成知识 | 13 | .169 | [.084, .252] |
> | **简单知识 (Simple knowledge)** | 认为知识是孤立的、碎片化的事实，而非复杂的关联网络 | 52 | .162 | [.113, .209] |
> | **简单与确定知识 (Simple and certain)** | 混合维度：知识不仅碎片化，而且一成不变 | 15 | .146 | [.089, .203] |
> | **先天能力 (Innate ability)** | 认为学习能力是天生的、不可改变的（归为智力内隐） | 52 | .137 | [.066, .207] |
> | **确定知识 (Certain knowledge)** | 认为知识是绝对不变的，排斥其暂定性（tentative） | 78 | .136 | [.087, .184] |
> | **基于权威的证成 (Justification by authority)** | 认为知识只需要权威（如书本、专家）背书即可成立 | 10 | .110 | [.041, .177] |
> | **全知权威 (Omniscient authority)** | 认为权威掌握着所有的真理，不会犯错 | 26 | .083 | [.024, .141] |
> | **认识论目标 (Epistemic aims)** | 认知活动追求的终点（如获得满分 vs 追求深层理解） | 1 | .087 | [-.018, .189] |
> | **真理的可及性 (Attainability of truth)** | 是否认为最终可以获得绝对且客观的真理 | 10 | .050 | [-.001, .100] |
> | **知识的结构 (Structure of knowledge)** | 关注知识的组织形态（第三梯队，效应均不显著） | 8 | -.035 | [-.219, .152] |
> | **微观可变性 (Texture & Variability)** | 特定实验任务中的细粒度知识建构属性（罕见维度） | 2 | .148 | [-.065, .328] |
"""

lines[211:235] = [new_content]

with open("wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2018_JEP.md", "w") as f:
    f.writelines(lines)
