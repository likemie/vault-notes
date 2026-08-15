import re

with open("wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2010_JEP.md", "r") as f:
    content = f.read()

# Define the new content
new_text = """> [!chain-link] 证据到判断
> 传统的阶段模型（见表1）本质上可以解构为对客观现实、知识来源和评价机制的不同量化态度。

> [!contrast-table] 表1：Kuhn et al. (2000) 认识论思维模型（Kuhn et al.'s Model of Epistemological Thinking）
> | 阶段（Level） | 客观现实（Reality） | 知识（Knowledge） | 批判性思维（Critical thinking） | 知识主张（Assertions） |
> | --- | --- | --- | --- | --- |
> | 现实主义者（Realist） | 可直接认知 | 确定，来自外部来源 | 不必要 | 对外部现实的复制 |
> | 绝对主义者（Absolutist） | 可直接认知 | 确定，来自外部来源 | 用于确定谁是“正确的” | 可对可错的事实 |
> | 多元主义者（Multiplist） | 无法直接认知 | 不确定，来自人类心智 | 不相关 | 不可质疑的观点 |
> | 评价主义者（Evaluativist） | 无法直接认知 | 不确定，来自人类心智 | 用于做出好决定并促进理解 | 可供评估的判断 |
> 
> *核心看点：此表呈现了传统的认识论发展阶段。作者指出，这四个定性的阶段本质上可以被拆解为个体对客观现实、知识来源及评价机制的不同信念维度的强弱组合。*
> *来源：Greene et al. (2010), p. 235*

> [!warrant] 推理桥梁
> 作者将上述传统模型与三维量化信念（SC、JA、PJ）进行了逻辑重构，演化出了全新的整合模型。
> - **合并初级阶段**：Kuhn 模型中的“现实主义者”（视知识为现实的无脑复制、无需批判性思维）多见于幼儿，而“绝对主义者”（引入批判性思维以辨别事实对错）多见于小学生。由于这两者在量化问卷中都会表现出极其相似的极端轮廓（即盲信知识简单确定、盲信权威与个人感觉），加之本研究的样本排除了低龄儿童，因此作者将这两者合并为了新模型中的“现实主义”。
> - **拆分中期阶段**：随着对知识绝对性的质疑，原本的“多元主义”被拆分为了两条分化路径：要么在不确定中依然盲从权威（教条主义），要么彻底只信自己的主观体验（怀疑主义）。
> - **重定义高级阶段**：最终能够整合多方证据的“评价主义”，则被重新定义为“理性主义”。
> 
> ```mermaid
> flowchart LR
>     subgraph Kuhn [Kuhn et al. 经典阶段]
>         direction TB
>         A0[现实主义 Realist]
>         A[绝对主义 Absolutist]
>         B[多元主义 Multiplist]
>         C[评价主义 Evaluativist]
>     end
> 
>     subgraph Greene [Greene EOC 整合模型]
>         direction TB
>         D[现实主义 Realism]
>         E1[教条主义 Dogmatism]
>         E2[怀疑主义 Skepticism]
>         F[理性主义 Rationalism]
>     end
> 
>     A0 -- "合并为三维皆强" --> D
>     A -- "合并为三维皆强" --> D
>     B -- "重权威、轻个人" --> E1
>     B -- "轻权威、重个人" --> E2
>     C -- "理性评估与整合" --> F
> ```

> [!contrast-table] 表2：认识论与本体论认知模型（Model of Epistemic and Ontological Cognition）
> | 受教育水平 | 劣构领域阶段 | SC 信念 | JA 信念 | PJ 信念 | 良构领域阶段 | SC 信念 | JA 信念 | PJ 信念 |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | 小学早期 | 现实主义 | 强 | 强 | 强 | 现实主义 | 强 | 强 | 强 |
> | 小学晚期至大学早期 | 教条/怀疑主义 | 弱<br>弱 | 强<br>弱 | 弱<br>强 | 现实主义 | 强 | 强 | 强 |
> | 大学中期至晚期 | 理性主义 | 弱 | 中等 | 中等 | 教条/怀疑主义 | 弱<br>弱 | 强<br>弱 | 弱<br>强 |
> | 本科后教育（研究生） | 理性主义 | 弱 | 中等 | 中等 | 理性主义 | 弱 | 中等 | 中等 |
> 
> *核心看点：本表是作者提出的核心整合模型。它展示了四个定性的发展阶段（现实、教条/怀疑、理性）是如何由三个独立信念维度的不同强弱配置（Profile）构成的，并预测了个体在劣构领域（如历史）中的认知发展会快于良构领域（如数学）。*
> *注：SC=简单与确定知识（Simple and Certain Knowledge）; JA=权威辩护（Justification by Authority）; PJ=个人辩护（Personal Justification）。来源：Greene et al. (2010), p. 238*"""

# We know it's between "> [!chain-link] 证据到判断" and the end of Table 2 "*注：SC=...来源：Greene et al. (2010), p. 238*"
pattern = re.compile(r"> \[!chain-link\] 证据到判断.*?来源：Greene et al\. \(2010\), p\. 238\*", re.DOTALL)
new_content = pattern.sub(new_text, content)

with open("wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2010_JEP.md", "w") as f:
    f.write(new_content)

print("Replacement successful")
