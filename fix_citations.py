import glob

files = [
    "wiki/methods/quantitative/Confirmatory Factor Analysis.md",
    "wiki/methods/quantitative/Multinomial Logistic Regression.md",
    "wiki/concepts/educational-psychology/Academic Achievement.md",
    "wiki/concepts/sociology-of-education/Educational Level.md"
]

for file_path in files:
    with open(file_path, "r") as f:
        content = f.read()
    
    # Fix the citation format in evidence grids
    content = content.replace(
        "[[Argument_Greene_2010_JEP]] — Greene et al. (2010)", 
        "[[Argument_Greene_2010_JEP|Greene et al. (2010)]] — "
    )
    
    with open(file_path, "w") as f:
        f.write(content)

print("Fixed citations.")
