import sys

filepath = "wiki/concepts/educational-psychology/Epistemic Cognition.md"
with open(filepath, "r") as f:
    text = f.read()

text = text.replace("King 和 Kitchener (1994)", "King & Kitchener (1994)")
text = text.replace("Hofer 和 Pintrich (1997)", "Hofer & Pintrich (1997)")
text = text.replace("Elby 和 Hammer (2001)", "Elby & Hammer (2001)")
text = text.replace("Chinn 等人明确了其排他性边界", "Chinn et al. (2011) 明确了其排他性边界")
text = text.replace("根据 Chinn 等人的整合框架", "根据 Chinn et al. (2011) 的整合框架")
text = text.replace("Chinn 等人提出整合框架", "Chinn et al. (2011) 等人提出整合框架")

with open(filepath, "w") as f:
    f.write(text)

