import re

with open("wiki/arguments/reports-policy-documents/Argument_Bergeron_2015_TeachingTOK.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Background
bg_target = """### 背景：知识论（TOK）的独特定位

> [!abstract] 区别于传统哲学的架构
> [[Theory of Knowledge|知识论]]探讨知识的生成与理解（generation and understanding of knowledge），审视知识构建背后的心理与社会文化机制。虽然它涉及柏拉图、笛卡尔等哲学家的讨论，但**知识论并非一门传统的哲学课**。它拥有独特的教学目标，专门围绕特定的八大**[[Areas of Knowledge|知识领域]]**（AOKs：伦理学、历史、人文科学、本土知识系统、数学、自然科学、宗教知识系统、艺术）和八种**[[Ways of Knowing|认知方式]]**（WOKs：情感、信仰、想象、本能、直觉、语言、记忆、理性、感官知觉）展开探究。该课程旨在引导学生探讨“什么是认知”、“我们如何认知”以及“追求真理与说服的过程”。"""

bg_replacement = """### 背景：知识论（TOK）的独特架构与定位

> [!def] 知识论（Theory of Knowledge）
> 国际文凭大学预科项目（IBDP）的核心课程之一。旨在引导学生探讨“什么是认知”、“我们如何认知”以及“追求真理与说服的过程”，通过审视知识构建背后的心理与社会文化机制，培养反思性的知识构建意识。

> [!contrast-table] 知识论与传统哲学的区别
> | 维度 | 知识论（TOK） | 传统哲学课程 |
> |---|---|---|
> | **探讨重心** | 认知的过程（认知方式）与知识的分类（知识领域） | 哲学史流派、形而上学或经典文本 |
> | **探究目的** | 建立跨学科联系，挑战自我中心，培养国际情怀 | 深入理解哲学家的思想与推导逻辑 |

> [!feature] 知识论的核心组件
> - **八大[[Areas of Knowledge|知识领域]]（AOKs）** 伦理学、历史、人文科学、本土知识系统、数学、自然科学、宗教知识系统、艺术。作为分类不同知识属性的框架。
> - **八大[[Ways of Knowing|认知方式]]（WOKs）** 情感、信仰、想象、本能、直觉、语言、记忆、理性、感官知觉。作为探究人类如何获取和加工知识的工具。"""

content = content.replace(bg_target, bg_replacement)

# Save
with open("wiki/arguments/reports-policy-documents/Argument_Bergeron_2015_TeachingTOK.md", "w", encoding="utf-8") as f:
    f.write(content)
