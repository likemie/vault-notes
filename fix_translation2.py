import re

with open("wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2018_JEP.md", "r") as f:
    text = f.read()

text = text.replace("天生能力", "先天能力")
text = text.replace("依靠权威证成", "基于权威的证成")
text = text.replace("多种证成", "多源证成")

with open("wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2018_JEP.md", "w") as f:
    f.write(text)
