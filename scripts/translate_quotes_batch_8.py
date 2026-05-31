import os

replacements = {
    # Argument_Creswell_2022_SAGE.md
    '"a set of interrelated [[Construct|constructs]] (variables), definitions, and propositions that presents a systematic view of phenomena by specifying relations among variables, with the purpose of explaining natural phenomena"': '“一组相互关联的[[Construct|构念]]（变量）、定义和命题，它们通过规定变量之间的关系来呈现对现象的系统性看法，其目的是解释自然现象”\n> ("a set of interrelated [[Construct|constructs]] (variables), definitions, and propositions that presents a systematic view of phenomena by specifying relations among variables, with the purpose of explaining natural phenomena")',
    '"What remains to be explored, however, is..."': '“然而，有待进一步探索的是……”\n> ("What remains to be explored, however, is...")',
    '"Despite an increased interest..., it is surprising that so little empirical research has actually been conducted on the topic..."': '“尽管人们对……的兴趣日益浓厚，但令人惊讶的是，关于该主题实际进行的实证研究却如此之少……”\n> ("Despite an increased interest..., it is surprising that so little empirical research has actually been conducted on the topic...")',
    '"A [[Survey Research|survey design]] provides a quantitative description of trends, attitudes, and opinions of a population, or tests for associations among variables of a population, by studying a sample of that population."': '“[[Survey Research|调查设计]]通过研究总体的一个样本，提供对该总体的趋势、态度和观点的量化描述，或检验该总体中变量之间的关联。”\n> ("A [[Survey Research|survey design]] provides a quantitative description of trends, attitudes, and opinions of a population, or tests for associations among variables of a population, by studying a sample of that population.")',
    '"An [[Experimental Research|experimental design]] systematically manipulates one or more variables to evaluate how this manipulation affects an outcome (or outcomes) of interest. Importantly, an experiment isolates the effects of this manipulation by holding all other variables constant."': '“[[Experimental Research|实验设计]]系统地操纵一个或多个变量，以评估这种操纵如何影响感兴趣的结果。重要的是，实验通过保持所有其他变量不变，来孤立这种操纵的效应。”\n> ("An [[Experimental Research|experimental design]] systematically manipulates one or more variables to evaluate how this manipulation affects an outcome (or outcomes) of interest. Importantly, an experiment isolates the effects of this manipulation by holding all other variables constant.")',
    '"Sample size determination is at its core a trade-off: A larger sample will provide more precision, but recruiting more participants is time-consuming and costly."': '“样本量的确定其核心是一种权衡：更大的样本将提供更高的精度，但招募更多的参与者既耗时又费钱。”\n> ("Sample size determination is at its core a trade-off: A larger sample will provide more precision, but recruiting more participants is time-consuming and costly.")',
    '"Sample size determination should be based on your analysis plans and expected outcomes."': '“样本量的确定应基于你的分析计划和预期结果。”\n> ("Sample size determination should be based on your analysis plans and expected outcomes.")',
    '"A [[Power Analysis]] can help you estimate a target sample size. ... This power analysis for sample size determination should be done during study planning and prior to enrolling any participants."': '“[[Power Analysis|功效分析]]可以帮助你估计目标样本量。……这种用于确定样本量的功效分析应当在研究计划阶段、招募任何参与者之前完成。”\n> ("A [[Power Analysis]] can help you estimate a target sample size. ... This power analysis for sample size determination should be done during study planning and prior to enrolling any participants.")',
    '"One of the principal features distinguishing an experiment from a survey study design is the use of [[Random Assignment]]."': '“区分实验与调查研究设计的一个主要特征是[[Random Assignment|随机分配]]的使用。”\n> ("One of the principal features distinguishing an experiment from a survey study design is the use of [[Random Assignment]].")',
    '"A [[Confidence Interval]] is a range of values (an interval) that describes a level of uncertainty around an estimated observed score. A confidence interval shows how good an estimated score might be."': '“[[Confidence Interval|置信区间]]是一个取值范围（一个区间），它描述了围绕估计观察分数的某种不确定性水平。置信区间显示了估计分数可能有多好。”\n> ("A [[Confidence Interval]] is a range of values (an interval) that describes a level of uncertainty around an estimated observed score. A confidence interval shows how good an estimated score might be.")',
    '"An [[Effect Size]] identifies the strength of the conclusions about group differences or the relationships among variables in quantitative studies. It is a descriptive statistic that is not dependent on whether the relationship in the data represents the true population."': '“[[Effect Size|效应量]]在量化研究中标识了关于组间差异或变量之间关系结论的强度。它是一种描述性统计量，不依赖于数据中的关系是否代表了真实的总体。”\n> ("An [[Effect Size]] identifies the strength of the conclusions about group differences or the relationships among variables in quantitative studies. It is a descriptive statistic that is not dependent on whether the relationship in the data represents the true population.")',
    '"A [[Manipulation Check|manipulation check measure]] is defined as a measure of the intended manipulated variable of interest."': '“[[Manipulation Check|操纵检验测量]]被定义为对感兴趣的预期被操纵变量的测量。”\n> ("A [[Manipulation Check|manipulation check measure]] is defined as a measure of the intended manipulated variable of interest.")',
    '"To reduce this form of [[Experimenter Bias]], it is helpful to make the experimenter administering the outcome measure blind to the participant\'s study condition."': '“为了减少这种形式的[[Experimenter Bias|实验者偏差]]，让实施结果测量的实验者对参与者的研究条件保持盲态（双盲）是有帮助的。”\n> ("To reduce this form of [[Experimenter Bias]], it is helpful to make the experimenter administering the outcome measure blind to the participant\'s study condition.")',

    # Argument_Hitchcock_2015_JBE.md
    '"It is important to note that these standards are not used in isolation, and thus generalization details cannot be fully understood without also considering the review protocols and a tool called the [[What Works Clearinghouse|WWC]] [[21st Century Skills and Competencies Discourse|SCD]] review guide."': '“重要的是要注意，这些标准并非孤立使用，因此如果不考虑审查方案以及被称为 [[What Works Clearinghouse|WWC]] SCD（单一个案设计）审查指南的工具，就无法完全理解概括性的细节。”\n> ("It is important to note that these standards are not used in isolation, and thus generalization details cannot be fully understood without also considering the review protocols and a tool called the [[What Works Clearinghouse|WWC]] [[21st Century Skills and Competencies Discourse|SCD]] review guide.")',
    '"The WWC addresses the [[External Validity]] of findings from multiple [[Single-Case Design|SCD]] studies by taking into consideration what Maggin et al. (2013) describe as criteria for assessing generality."': '“WWC 通过考虑 Maggin 等人 (2013) 描述的评估一般性的标准，来解决来自多项[[Single-Case Design|SCD（单一个案设计）]]研究的发现的[[External Validity|外部效度]]问题。”\n> ("The WWC addresses the [[External Validity]] of findings from multiple [[Single-Case Design|SCD]] studies by taking into consideration what Maggin et al. (2013) describe as criteria for assessing generality.")',
    '"These criteria are in fact somewhat arbitrary but they are based on both expert judgment and logic and they are meant to be transparent."': '“这些标准事实上有些武断，但它们基于专家判断和逻辑，并且旨在保持透明。”\n> ("These criteria are in fact somewhat arbitrary but they are based on both expert judgment and logic and they are meant to be transparent.")'
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
