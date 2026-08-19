import sys

filepath = "wiki/concepts/educational-psychology/Epistemic Cognition.md"
with open(filepath, "r") as f:
    text = f.read()

# Fix taxonomy quotes
text = text.replace("从早期的“绝对主义（Absolutism，知识由权威赋予且简单确定）”，经历“多元主义（Multiplism，知识皆为主观意见）”，最终走向成熟的“评价主义（Evaluatism，知识是情境建构的，需基于证据进行客观评估）”", "从早期的绝对主义（Absolutism，知识由权威赋予且简单确定），经历多元主义（Multiplism，知识皆为主观意见），最终走向成熟的评价主义（Evaluatism，知识是情境建构的，需基于证据进行客观评估）")
text = text.replace("“信念维度”", "信念维度")
text = text.replace("“知识的性质”（Nature of knowledge，如简单性、确定性）与“认识的性质”（Nature of knowing，如知识的来源、知识的证成）", "知识的性质（Nature of knowledge，如简单性、确定性）与认识的性质（Nature of knowing，如知识的来源、知识的证成）")
text = text.replace("“分析认识论”", "分析认识论")
text = text.replace("“认识论目标（Epistemic aims）”", "认识论目标（Epistemic aims）")
text = text.replace("“认识论理想（Epistemic ideals）”", "认识论理想（Epistemic ideals）")
text = text.replace("“可靠过程（Reliable processes）”", "可靠过程（Reliable processes）")
text = text.replace("“认识论资源”", "认识论资源")

# Check dev-timeline for quotes
text = text.replace("“绝对主义”到“评价主义”", "绝对主义到评价主义")
text = text.replace("微观的“认识论资源”", "微观的认识论资源")

with open(filepath, "w") as f:
    f.write(text)

