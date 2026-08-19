import sys

filepath = "wiki/concepts/educational-psychology/Epistemic Cognition.md"
with open(filepath, "r") as f:
    text = f.read()

chinn_old = """> [!claim] Chinn, C.
> **扩展五组件框架** 认识论认知是由五个高度情境化的组件构成的微观网络：1. 探究中追求真理等目标的“认识目标与价值”；2. 包括决定论与机制在内的“知识结构”；3. 交互且具特异性的“来源与确证”标准；4. 思想开放等“认识论美德”；5. 涵盖同行评审与因果推断的“可靠过程”。[[Argument_Chinn_2011_EP|(Chinn et al., 2011)]]"""

chinn_new = """> [!claim] Chinn, C.
> **扩展五组件框架** 认识论认知是由五个高度情境化的组件构成的微观网络：
> - **认识目标与价值**：探究中追求真理或最低限度确证等目标及其价值评估。
> - **知识结构**：包括普遍性与特殊性、决定论与随机性及具体形式。
> - **来源与确证**：交互涵盖感知、推理、证词及不同情境下的确证标准。
> - **认识论美德与恶习**：思想开放、理智勇气等促进认识目标的性格倾向。
> - **可靠与不可靠的过程**：涵盖产生信念的因果推断与同行评审机制。[[Argument_Chinn_2011_EP|(Chinn et al., 2011)]]"""

sandoval_old = """> [!claim] Sandoval, W.
> **整合多元主义层级框架** 认识论认知的本体形态不能局限于个体头脑，必须通过多层聚合来分析：在“个体层级”是调配细粒度认识论资源，在“人际交互层级”是微观社会协商认识目标与标准，在“活动系统层级”是科学共同体整体的认识论氛围。[[Argument_Sandoval_2016_RRE|(Sandoval et al., 2016)]]"""

sandoval_new = """> [!claim] Sandoval, W.
> **整合多元主义层级框架** 认识论认知的本体形态不能局限于个体头脑，必须通过多层聚合来分析：
> - **个体层级**：调配细粒度认识论资源与心智模型。
> - **人际交互层级**：微观社会群体内协商共同的认识目标与标准。
> - **活动系统层级**：科学共同体或整体课堂文化所形塑的认识论氛围。[[Argument_Sandoval_2016_RRE|(Sandoval et al., 2016)]]"""

text = text.replace(chinn_old, chinn_new)
text = text.replace(sandoval_old, sandoval_new)

with open(filepath, "w") as f:
    f.write(text)

