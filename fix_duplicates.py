import sys

filepath = "wiki/concepts/educational-psychology/Epistemic Cognition.md"
with open(filepath, "r") as f:
    text = f.read()

# Fix Sandoval 2016 duplicate in tension
text = text.replace("社会实践活动（social practices）”。[[Argument_Sandoval_2016_RRE|(Sandoval et al., 2016)]]", "社会实践活动（social practices）”。")

# Fix Greene 2018 duplicate in ma-table
text = text.replace("> | [[Argument_Greene_2018_JEP\\|Greene et al. (2018)]] | 成就类型 |", "> | 同上 | 成就类型 |")
text = text.replace("> | [[Argument_Greene_2018_JEP\\|Greene et al. (2018)]] | [[Epistemology\\|认识论]][[Construct\\|构念]] |", "> | 同上 | [[Epistemology\\|认识论]][[Construct\\|构念]] |")

with open(filepath, "w") as f:
    f.write(text)
