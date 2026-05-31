import os

replacements = {
    # Argument_Downey_2016_SoE.md
    '"When it comes to inequality, \'schooling is more part of the solution than part of the problem.\'"': '“在不平等问题上，‘学校教育在更大程度上是解决方案的一部分，而不是问题的一部分。’”\n> ("When it comes to inequality, \'schooling is more part of the solution than part of the problem.\'")',
    '"The proper way to assess schools\' effect on achievement gaps is not to focus solely on school year patterns but to compare the school year (treatment) and summer (control) patterns. Schools are compensatory whenever achievement trajectories are more equal when school is in versus out of session."': '“评估学校对成就差距影响的正确方法，不是仅仅关注学年模式，而是要比较学年（处理组）和夏季（对照组）的模式。只要在开学期间成就轨迹比放假期间更平等，学校就发挥了补偿作用。”\n> ("The proper way to assess schools\' effect on achievement gaps is not to focus solely on school year patterns but to compare the school year (treatment) and summer (control) patterns. Schools are compensatory whenever achievement trajectories are more equal when school is in versus out of session.")',
    '"The question is not whether it is possible via school reform to reduce achievement gaps; the question is whether school reform is the best strategy for reducing them."': '“问题不在于是否有可能通过学校改革来缩小成就差距；问题在于，学校改革是否是缩小差距的最佳策略。”\n> ("The question is not whether it is possible via school reform to reduce achievement gaps; the question is whether school reform is the best strategy for reducing them.")',
    '"A cynical—and entirely plausible—interpretation of the greater emphasis on reforming schools relative to reforming other institutions is that it serves a purpose: It distracts people from the real sources of inequality, thereby serving the interests of those who benefit from current social arrangements."': '“对于相较于改革其他机构更强调改革学校这一现象，一种愤世嫉俗——却完全合理——的解释是它服务于一种目的：它转移了人们对不平等的真正根源的注意力，从而服务于那些从当前社会安排中获益的人的利益。”\n> ("A cynical—and entirely plausible—interpretation of the greater emphasis on reforming schools relative to reforming other institutions is that it serves a purpose: It distracts people from the real sources of inequality, thereby serving the interests of those who benefit from current social arrangements.")',

    # Argument_Ball_2008_SR.md
    '"the sociology of education has created the \'conditions of possibility\' and an \'optics of power\'"': '“教育社会学创造了‘可能性的条件’和一种‘权力的光学’”\n> ("the sociology of education has created the \'conditions of possibility\' and an \'optics of power\'")',
    '"Education was no longer the solution but the problem."': '“教育不再是解决方案，而成了问题所在。”\n> ("Education was no longer the solution but the problem.")',
    '"effectiveness operates as a technology of normalisation."': '“有效性作为一种正常化的技术在运作。”\n> ("effectiveness operates as a technology of normalisation.")',

    # Argument_Golovchin_2019_ESC.md
    '"The variation of the [[Variable|variables]] used by Hattie exceeds 50%, which is higher than the statistical threshold of sample homogeneity (33%). ... Determining the strength of any effects in such a model, due to its instability, will likely not lead to the formation of objective conclusions."': '“Hattie 使用的[[Variable|变量]]变异系数超过了50%，高于样本同质性的统计阈值（33%）。……由于该模型的不稳定性，确定这种模型中任何效应的强度，很可能无法得出客观的结论。”\n> ("The variation of the [[Variable|variables]] used by Hattie exceeds 50%, which is higher than the statistical threshold of sample homogeneity (33%). ... Determining the strength of any effects in such a model, due to its instability, will likely not lead to the formation of objective conclusions.")',
    '"The implementation of Hattie\'s ideas within the framework of Russian educational policy is inapplicable, since it can cause negative consequences and extend the range of new problems (in particular, the increase in the bureaucratic functionality of the teaching profession in the pursuit of \'[[School Leadership]]\')."': '“在俄罗斯教育政策的框架内实施 Hattie 的观点是不适用的，因为这可能会造成负面后果并引发一系列新问题（特别是在追求‘[[School Leadership|学校领导力]]’的过程中，教师职业的官僚化职能增加）。”\n> ("The implementation of Hattie\'s ideas within the framework of Russian educational policy is inapplicable, since it can cause negative consequences and extend the range of new problems (in particular, the increase in the bureaucratic functionality of the teaching profession in the pursuit of \'[[School Leadership]]\').")',
    '"In education, however, there is little that \'works\' and little that \'does not work\'. The correct question is: \'Under what conditions will this work in school?\'"': '“然而，在教育中，几乎没有什么‘有效’，也几乎没有什么‘无效’。正确的问题是：‘在什么条件下，这在学校里会有效？’”\n> ("In education, however, there is little that \'works\' and little that \'does not work\'. The correct question is: \'Under what conditions will this work in school?\'")',
    '"The book is perceived as a panacea for the educational community, but as a result of taking this drug, the school will experience a short-term placebo effect."': '“这本书被教育界视为灵丹妙药，但服用这剂药的结果是，学校将经历一次短期的安慰剂效应。”\n> ("The book is perceived as a panacea for the educational community, but as a result of taking this drug, the school will experience a short-term placebo effect.")',

    # Argument_Simpson_2019_ERE.md
    '"In each of these examples, the educational intervention (and control activity and population and sample size, etc.) is exactly the same... yet the effect size varies from 0 to 0.4, to 0.6, to 4, to infinity."': '“在这些例子中，每一个的教育干预（以及控制活动、人群和样本量等）都完全相同……然而效应量却从0变到0.4，变到0.6，变到4，直至无穷大。”\n> ("In each of these examples, the educational intervention (and control activity and population and sample size, etc.) is exactly the same... yet the effect size varies from 0 to 0.4, to 0.6, to 4, to infinity.")',
    '"The enemy of clarity being noise — anything which acts to increase the noise of an experiment... will decrease effect size."': '“清晰的敌人是噪音——任何增加实验噪音的因素……都会降低效应量。”\n> ("The enemy of clarity being noise — anything which acts to increase the noise of an experiment... will decrease effect size.")',
    '"Mistaking effect size for a measure of educational importance or influence is, then, a category error."': '“那么，将效应量误认为是教育重要性或影响力的衡量标准，就是一个范畴错误。”\n> ("Mistaking effect size for a measure of educational importance or influence is, then, a category error.")',
    '"The appearance of [[Direct Instruction]] interventions like [[Feedback]] and meta-cognition at the top of meta-meta-analytic tables should be taken only as evidence that researchers have found it easier to conduct less noisy experiments in these areas compared to behaviour interventions or summer schools."': '“像[[Feedback|反馈]]和元认知这样的[[Direct Instruction|直接教学]]干预出现在元-元分析榜单顶部，只能被视为一种证据：表明与行为干预或暑期学校相比，研究者发现这些领域更容易开展低噪音的实验。”\n> ("The appearance of [[Direct Instruction]] interventions like [[Feedback]] and meta-cognition at the top of meta-meta-analytic tables should be taken only as evidence that researchers have found it easier to conduct less noisy experiments in these areas compared to behaviour interventions or summer schools.")',
    '"Forms of intervention are promoted as more effective when, in fact, the evidence merely indicates they are areas in which it may be easier to conduct clearer studies. This misidentification is leading policy, driving the use of scarce resources and causing major changes in teaching methods. There\'s the harm."': '“某些干预形式被推广为更有效，而事实上，证据仅仅表明在这些领域开展更清晰的研究可能更容易。这种错误识别正在引导政策，驱动稀缺资源的使用，并导致教学方法的重大改变。这就是危害所在。”\n> ("Forms of intervention are promoted as more effective when, in fact, the evidence merely indicates they are areas in which it may be easier to conduct clearer studies. This misidentification is leading policy, driving the use of scarce resources and causing major changes in teaching methods. There\'s the harm.")'
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
