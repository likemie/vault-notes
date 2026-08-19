import sys

filepath = "wiki/concepts/educational-psychology/Epistemic Cognition.md"
with open(filepath, "r") as f:
    text = f.read()

old_taxonomy = """> [!taxonomy] 认识论认知的四大理论流派
> [[Argument_Greene_2018_JEP|Greene et al. (2018)]] 总结了该领域四种完全不同的本体论架构：
> - **发展论模型（Developmental Models）** 认为个体的认识论经历从“绝对主义（非黑即白）”到“多元主义（相对主义）”再到“评价主义（基于证据的客观评价）”的线性发展。
> - **独立信念系统（Independent Beliefs）** 认为认识论是由多个独立维度（如知识的确定性、简单性等）组成的稳定系统。
> - **认识论资源库（Epistemic Resources）** 彻底摒弃了宏大的稳定信念假设，主张认知是微观的、细粒度的“资源”，个体在面对不同情境时会瞬间激活不同的资源组合。
> - **整合框架（Integrated Frameworks）** 试图弥合稳定信念与情境资源之间的鸿沟，强调微观组件与多层级互动的动态统一。"""

new_taxonomy = """> [!taxonomy] 认识论认知的四大理论流派
> [[Argument_Greene_2018_JEP|Greene et al. (2018)]] 通过全面梳理，将半个多世纪以来的理论演进归纳为四种截然不同的架构：
> - **发展模型（Developmental Models）**：发端于 Perry (1970)。该流派认为认识论认知遵循严格的宏观阶段性演进：从早期的“绝对主义（Absolutism，知识由权威赋予且简单确定）”，经历“多元主义（Multiplism，知识皆为主观意见）”，最终走向成熟的“评价主义（Evaluatism，知识是情境建构的，需基于证据进行客观评估）”。其代表模型还包括 Kuhn (1991) 的论证发展模型，以及 King 和 Kitchener (1994) 的反思性判断模型。
> - **多维模型（Multidimensional Models）**：以 Schommer (1990) 为开创者。该流派彻底打破了单向线性发展的假设，认为认识论是由若干相对独立、不必同步发展的“信念维度”组成的系统。Hofer 和 Pintrich (1997) 进一步将其经典化，划分为“知识的性质”（Nature of knowledge，如简单性、确定性）与“认识的性质”（Nature of knowing，如知识的来源、知识的证成）两大核心构念簇。
> - **哲学驱动模型（Philosophically Driven Models）**：旨在解决早期心理学模型缺乏“分析认识论”哲学根基的根本缺陷。以 Chinn et al. (2011) 提出的 AIR 框架为绝对代表，该流派将认识论认知拆解为微观网络：包含探究目标的“认识论目标（Epistemic aims）”、评估证据的“认识论理想（Epistemic ideals）”以及实现这些目标的“可靠过程（Reliable processes）”。
> - **学科/领域驱动模型（Discipline-Driven Models）**：受情境认知（Situated cognition）理论深度启发，强调认识论并不是跨领域的稳定特质，而是高度依赖特定任务情境的。例如，Elby 和 Hammer (2001) 提出的“认识论资源”模型明确指出，学生在分析历史史料与解决物理方程时，会瞬间动态激活完全不同的认识论预设；而 Muis et al. (2006) 则进一步系统化了这种领域特异性的理论框架。"""

text = text.replace(old_taxonomy, new_taxonomy)

old_timeline = """> [!dev-timeline] 概念演变
> - **1970–1991 — 起源阶段：发展论模型** Perry 和 Kuhn 认为个体的认识论经历从“绝对主义”到“评价主义”的宏大线性发展。
> - **1990 — 扩展阶段：独立信念系统** Schommer 打破了单维发展观，提出知识确定性、简单性等多维独立的信念系统。
> - **2001 — 转向阶段：认识论资源库** Elby & Hammer 提出彻底的微观资源论，认为个体面对不同情境会瞬间激活不同的资源碎片，摒弃了稳定信念假设。
> - **2011至今 — 教育研究应用：整合框架** Chinn 和 Sandoval 等人提出整合框架，弥合内部特质与外部情境的断层；Greene 的元分析确立了该领域的实证基准。[[Argument_Greene_2018_JEP|(Greene et al., 2018)]]"""

new_timeline = """> [!dev-timeline] 概念演变
> - **1970–1994 — 起源阶段：发展模型** Perry (1970) 和 Kuhn (1991) 确立了个体认识论从“绝对主义”到“评价主义”的宏大线性发展阶段。
> - **1990–1997 — 扩展阶段：多维模型** Schommer (1990) 以及 Hofer 和 Pintrich (1997) 打破了单维发展观，提出知识确定性、来源等多维独立的信念系统。
> - **2001–2006 — 转向阶段：学科/领域驱动模型** Elby 和 Hammer (2001) 提出微观的“认识论资源”，Muis et al. (2006) 确立了情境依赖性，摒弃了跨领域稳定特质的假设。
> - **2011至今 — 教育研究应用：哲学驱动与整合框架** Chinn et al. (2011) 和 Sandoval et al. (2016) 等人提出了基于规范哲学与多层系统的整合框架；Greene et al. (2018) 的元分析确立了该领域的实证基准。"""

text = text.replace(old_timeline, new_timeline)

with open(filepath, "w") as f:
    f.write(text)

