import os

replacements = {
    # Argument_Wolf_2020_JREE.md
    '"We find evidence of a \'[[Developer Effect]],\' where program evaluations carried out or commissioned by developers produced average effect sizes that were substantially larger than those identified in evaluations conducted by independent parties."': '“我们发现了‘[[Developer Effect|开发商效应]]’的证据，即由开发商执行或委托的项目评估所产生的平均效应量，显著大于由独立第三方进行的评估。”\n> ("We find evidence of a \'[[Developer Effect]],\' where program evaluations carried out or commissioned by developers produced average effect sizes that were substantially larger than those identified in evaluations conducted by independent parties.")',
    '"When looking within the same program, developer-commissioned studies produced average effect sizes that were 1.7 times greater than those in independent studies."': '“在针对同一个项目时，由开发商委托的研究产生的平均效应量是独立研究的 1.7 倍。”\n> ("When looking within the same program, developer-commissioned studies produced average effect sizes that were 1.7 times greater than those in independent studies.")',
    '"Open access to study data holds the greatest promise for mitigating bias when authors publish complete datasets, including missing values and all participants who were included in the study at the onset, to the extent possible."': '“当作者尽可能发布完整的数据集——包括缺失值和研究开始时的所有参与者——时，开放研究数据在减轻偏见方面具有最大的潜力。”\n> ("Open access to study data holds the greatest promise for mitigating bias when authors publish complete datasets, including missing values and all participants who were included in the study at the onset, to the extent possible.")',

    # Argument_Wrigley_2018_BERJ.md
    '"When \'evidence\' is reduced to a mean [[Effect Size]], the individual person or event is shut out, complexity is lost and values are erased."': '“当‘证据’被简化为一个平均[[Effect Size|效应量]]时，个体或事件被拒之门外，复杂性消失了，价值观也被抹去了。”\n> ("When \'evidence\' is reduced to a mean [[Effect Size]], the individual person or event is shut out, complexity is lost and values are erased.")',
    '"There is, in truth, no evidence of benefit from Fresh Start compared with the control group: the headlined \'three months additional progress\' is simply a phantom of poor randomisation."': '“事实上，没有证据表明 Fresh Start 项目相比对照组有任何益处：头条新闻中所谓的‘三个月的额外进展’仅仅是糟糕随机化的幻影。”\n> ("There is, in truth, no evidence of benefit from Fresh Start compared with the control group: the headlined \'three months additional progress\' is simply a phantom of poor randomisation.")',
    '"An aggregate mean of effect sizes calculated ... the conclusion drawn that \'[[Feedback]]\' is the most effective way to improve attainment. Since feedback is inevitably present in some way in any pedagogical interaction, it would be more illuminating to examine reasons for the differences."': '“通过计算得出的效应量聚合平均值……得出的结论是‘[[Feedback|反馈]]’是提高成绩最有效的方法。由于反馈在任何教学互动中都会以某种方式不可避免地存在，因此研究差异产生的原因会更具启发性。”\n> ("An aggregate mean of effect sizes calculated ... the conclusion drawn that \'[[Feedback]]\' is the most effective way to improve attainment. Since feedback is inevitably present in some way in any pedagogical interaction, it would be more illuminating to examine reasons for the differences.")',
    '"Placing classroom assistants near the bottom of the Toolkit\'s league table...could result in schools and academy chains terminating their employment, especially in times of budget cuts."': '“将课堂助教置于工具包排行榜底部附近……可能会导致学校和学院联盟终止对他们的聘用，尤其是在预算削减时期。”\n> ("Placing classroom assistants near the bottom of the Toolkit\'s league table...could result in schools and academy chains terminating their employment, especially in times of budget cuts.")',
    '"The sloganistic \'what works\' reflects a neoliberal demand to extract maximum efficiency from education, while marginalising the qualitative and political dimensions of human formation."': '“口号式的‘什么有效’反映了新自由主义从教育中榨取最大效率的需求，同时将人的塑造（human formation）的质性维度和政治维度边缘化了。”\n> ("The sloganistic \'what works\' reflects a neoliberal demand to extract maximum efficiency from education, while marginalising the qualitative and political dimensions of human formation.")',
    '"Social programmes ... offer resources (material, social, cognitive) to subjects, and whether they work depends on the reasoning of these individuals."': '“社会项目……为受试者提供资源（物质的、社会的、认知的），而它们是否有效取决于这些个体的推理（reasoning）。”\n> ("Social programmes ... offer resources (material, social, cognitive) to subjects, and whether they work depends on the reasoning of these individuals.")',
    '"At every stage of the meta-analytic review, simplifications are made. ... In this purgative process the very features that explain how interventions work are eliminated from the reckoning."': '“在元分析综述的每个阶段，都在进行简化。……在这一‘清洗’过程中，解释干预措施如何发挥作用的那些关键特征被排除在考量之外。”\n> ("At every stage of the meta-analytic review, simplifications are made. ... In this purgative process the very features that explain how interventions work are eliminated from the reckoning.")',
    '"The attempt to make learning visible eclipses older understandings of education as [[Bildung]] and pedagogy (both words carrying the sense of human formation)."': '“让学习可见的尝试，使人们对教育作为[[Bildung|陶冶（Bildung）]]和教育学的旧有理解（这两个词都带有人的塑造的含义）变得暗淡无光。”\n> ("The attempt to make learning visible eclipses older understandings of education as [[Bildung]] and pedagogy (both words carrying the sense of human formation).")'
}

def translate_quotes(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for eng, chn in replacements.items():
            new_content = new_content.replace(eng, chn)
            
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    count = 0
    for root, dirs, files in os.walk('wiki/arguments/'):
        for file in files:
            if file.endswith('.md'):
                if translate_quotes(os.path.join(root, file)):
                    count += 1
                    print(f"Translated quotes in {file}")
    print(f"Total files updated: {count}")

if __name__ == '__main__':
    main()
