import re

with open("wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2018_JEP.md", "r") as f:
    text = f.read()

text = text.replace("测量仪器名称", "测量工具名称")
text = text.replace("仪器的信度", "量表的信度")
text = text.replace("仪器信度", "量表信度")
text = text.replace("测量仪器", "测量工具")
text = text.replace("仪器", "测量工具")
text = text.replace("信度幻影", "统计幻象")
text = text.replace("同行评审的光环效应", "同行评审的质量门槛效应")
text = text.replace("衰减了真实相关性", "导致真实相关性被低估")

with open("wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2018_JEP.md", "w") as f:
    f.write(text)
