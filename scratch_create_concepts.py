import os

base_dir = "/Users/shaoyangwu/Documents/MyNotes/wiki/concepts/educational-psychology/"

concepts = {
    "Received Knowledge": {
        "aliases": ["接收知识", "received knowledge"],
        "summary": "女性认知方式模型中的认识论阶段，个体将知识视为绝对的确切事实，只能从外部权威处被动接收。",
        "theory": "Women's Ways of Knowing",
        "def": "接收知识（Received Knowledge）是 Belenky 等人（1986）在探讨女性认知方式时提出的认识阶段。处于该阶段的个体认为知识是绝对的确切事实，而自己缺乏创造知识的能力。知识只能从全知的外部专家或权威那里被动接收。[[Argument_Hofer_1997_RER|(Hofer & Pintrich, 1997, p. 95)]]"
    },
    "Subjective Knowledge": {
        "aliases": ["主观知识", "subjective knowledge"],
        "summary": "女性认知方式模型中的认识论阶段，个体认识到知识的不确定性，并转向内在的、直觉的真理。",
        "theory": "Women's Ways of Knowing",
        "def": "主观知识（Subjective Knowledge）是 Belenky 等人（1986）模型中的过渡阶段。个体开始认识到绝对真理是不存在的，从而将知识的来源从外部权威转向内在自我，认为知识是个人的、私密的和直觉的（与 Perry 的多元论阶段相对应）。[[Argument_Hofer_1997_RER|(Hofer & Pintrich, 1997, p. 95)]]"
    },
    "Procedural Knowledge": {
        "aliases": ["程序知识", "procedural knowledge"],
        "summary": "女性认知方式模型中的认识论阶段，个体开始关注获取、沟通和运用证据的具体方法。",
        "theory": "Women's Ways of Knowing",
        "def": "程序知识（Procedural Knowledge）是 Belenky 等人（1986）模型中的高级阶段。个体认识到仅仅依靠主观直觉是不够的，开始关注获取和评估知识的程序与方法。它分为“连结型（connected knowing）”（基于共情与体验）和“分离型（separate knowing）”（基于客观和逻辑批判）。[[Argument_Hofer_1997_RER|(Hofer & Pintrich, 1997, p. 95)]]"
    },
    "Constructed Knowledge": {
        "aliases": ["建构知识", "constructed knowledge"],
        "summary": "女性认知方式模型中的最高阶段，个体认为知识是随语境变化的主动建构产物。",
        "theory": "Women's Ways of Knowing",
        "def": "建构知识（Constructed Knowledge）是 Belenky 等人（1986）模型中的最高发展阶段。个体将主观直觉与客观程序相融合，认识到知识并非既定事实，而是由认知者主动建构、随语境变化的产物，学习者本身就是知识的创造者。[[Argument_Hofer_1997_RER|(Hofer & Pintrich, 1997, p. 95)]]"
    },
    "Absolute Knowing": {
        "aliases": ["绝对认知", "absolute knowing"],
        "summary": "认识论反思模型（ERM）的基础阶段，认为知识是绝对确定并由权威掌握的。",
        "theory": "Epistemological Reflection Model",
        "def": "绝对认知（Absolute Knowing）是 Baxter Magolda (1992) 的认识论反思模型中的起点。个体认为知识是绝对的、确定的，且完全掌握在教师或权威手中；学习的任务就是获取这些确切答案。[[Argument_Hofer_1997_RER|(Hofer & Pintrich, 1997, p. 99)]]"
    },
    "Transitional Knowing": {
        "aliases": ["过渡认知", "transitional knowing"],
        "summary": "认识论反思模型（ERM）中的过渡阶段，开始接受部分知识的不确定性。",
        "theory": "Epistemological Reflection Model",
        "def": "过渡认知（Transitional Knowing）是 Baxter Magolda (1992) 模型中的第二阶段。个体开始认识到权威并非全知全能，接受了部分知识存在不确定性。但他们往往认为这只是暂时的，期望未来总会找到确定答案。[[Argument_Hofer_1997_RER|(Hofer & Pintrich, 1997, p. 99)]]"
    },
    "Independent Knowing": {
        "aliases": ["独立认知", "independent knowing"],
        "summary": "认识论反思模型（ERM）的第三阶段，认为知识是不确定的，每个人都有权保留自己的观点。",
        "theory": "Epistemological Reflection Model",
        "def": "独立认知（Independent Knowing）是 Baxter Magolda (1992) 模型中的第三阶段。个体认为大多数知识都是不确定的，从而走向了极端的多元主义：认为每个人都有权保留自己的观点，且所有观点似乎都是同等有效的。[[Argument_Hofer_1997_RER|(Hofer & Pintrich, 1997, p. 99)]]"
    },
    "Contextual Knowing": {
        "aliases": ["语境认知", "contextual knowing"],
        "summary": "认识论反思模型（ERM）的最高阶段，能基于语境和证据对不确定的知识进行概率性评估。",
        "theory": "Epistemological Reflection Model",
        "def": "语境认知（Contextual Knowing）是 Baxter Magolda (1992) 模型中的最高阶段。个体认识到尽管知识具有相对性和不确定性，但并非所有观点都同等有效。他们学会了在特定语境中，运用证据进行概率性的评价与辩护。[[Argument_Hofer_1997_RER|(Hofer & Pintrich, 1997, p. 99)]]"
    },
    "Absolutist": {
        "aliases": ["绝对论者", "absolutist", "absolutists"],
        "summary": "论辩推理模型中的基础认识论立场，视知识为绝对客观的事实。",
        "theory": "Argumentative Reasoning",
        "def": "绝对论者（Absolutist）是 Kuhn (1991) 在日常论辩推理研究中界定的认识论立场。该类个体将知识视为绝对的、客观的事实，相信专家确切掌握着真理，且对社会或科学争议持非黑即白的态度。[[Argument_Hofer_1997_RER|(Hofer & Pintrich, 1997, p. 104)]]"
    },
    "Multiplist": {
        "aliases": ["多元论者", "multiplist", "multiplists"],
        "summary": "论辩推理模型中的中间认识论立场，认为所有观点都同等有效。",
        "theory": "Argumentative Reasoning",
        "def": "多元论者（Multiplist）是 Kuhn (1991) 论辩推理模型中的认识论立场。当绝对论受到现实争议（如专家意见不一）挑战时，个体转向多元论，认为知识完全受限于个人视角，所有意见都仅仅是个人观点，且同等有效，缺乏评估证据的动机。[[Argument_Hofer_1997_RER|(Hofer & Pintrich, 1997, p. 104)]]"
    },
    "Evaluatist": {
        "aliases": ["评价论者", "evaluatist", "evaluatists"],
        "summary": "论辩推理模型中的高级认识论立场，认为观点可以根据证据的优劣进行概率性评估。",
        "theory": "Argumentative Reasoning",
        "def": "评价论者（Evaluatist）是 Kuhn (1991) 模型中的最高认识论立场。个体意识到，尽管没有绝对的确切事实，但并非所有观点都同等合理。他们能够根据证据的优劣和逻辑的一致性，对不同主张进行比较、评价和辩护。[[Argument_Hofer_1997_RER|(Hofer & Pintrich, 1997, p. 104)]]"
    }
}

template = """---
title: {title}
aliases:
{aliases_str}
summary: "{summary}"
type: concept
domain: "educational-psychology"
related_concepts:
  - "[[Source of Knowledge]]"
  - "[[Certainty of Knowledge]]"
  - "[[Justification for Knowing]]"
related_theories:
  - "[[{theory}]]"
related_arguments:
  - "[[Argument_Hofer_1997_RER]]"
status: active
created: 2026-08-15
updated: 2026-08-15
---

# {title}

---

## 定义

> [!def] 核心定义
> {def_text}

> [!concept-lens] 概念透镜
> - **含义** 作为[[{theory}]]中的核心认知阶段，标志着个体在“知识的确定性”与“认知的辩护”上所处的水平。
> - **用途** 帮助教育者识别学生所处的认识论发展位置，并提供与之匹配的干预措施。
> - **边界** 它描述的是个体对知识本质的“信念假设”，而不是一般意义上的智力水平或认知风格。

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Hofer_1997_RER|Hofer & Pintrich (1997)]] — 在梳理认识论发展模型时，将其作为反映知识的确定性、简单性及认知来源与辩护的结构性成分。
"""

for title, data in concepts.items():
    aliases_str = "\n".join([f"  - {alias}" for alias in data["aliases"]])
    content = template.format(
        title=title,
        aliases_str=aliases_str,
        summary=data["summary"],
        theory=data["theory"],
        def_text=data["def"]
    )
    with open(os.path.join(base_dir, f"{title}.md"), "w") as f:
        f.write(content)
    print(f"Created {title}.md")

