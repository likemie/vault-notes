import re

with open("wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2018_JEP.md", "r") as f:
    text = f.read()

text = text.replace('related_persons:\n  - "[[Thomas Kuhn]]"\nrelated_facts:', 'related_persons: []\nrelated_facts:')

with open("wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2018_JEP.md", "w") as f:
    f.write(text)
