import os

replacements = {
    # Argument_Kraft_2023_ER.md (remaining one from previous batch if missed)
    '"Efforts to improve education often fail to improve student outcomes, particularly student achievement."': '“改善教育的努力往往未能改善学生的结果，特别是学生的学业成就。”\n> ("Efforts to improve education often fail to improve student outcomes, particularly student achievement.")',

    # Argument_Simpson_2017_JEP.md
    '"Areas which rank highly in Marzano (1998), [[John Hattie|Hattie]] (2009) and Higgins et al. (2013) are those in which researchers can design more sensitive experiments."': '“在 Marzano (1998)、[[John Hattie|Hattie]] (2009) 和 Higgins et al. (2013) 中排名较高的领域，是那些研究者能够设计出更敏感的实验的领域。”\n> ("Areas which rank highly in Marzano (1998), [[John Hattie|Hattie]] (2009) and Higgins et al. (2013) are those in which researchers can design more sensitive experiments.")',
    '"Standardised [[Effect Size]] is not a measure of educational impact because larger numbers produced from this process are not indicative of larger educational impact. Instead, areas which rank highly ... are those in which researchers can design more sensitive experiments."': '“标准化[[Effect Size|效应量]]不是教育影响力的衡量标准，因为从这个过程中产生的更大的数字并不意味着更大的教育影响力。相反，排名靠前的领域……是研究者能设计出更敏感实验的领域。”\n> ("Standardised [[Effect Size]] is not a measure of educational impact because larger numbers produced from this process are not indicative of larger educational impact. Instead, areas which rank highly ... are those in which researchers can design more sensitive experiments.")',
    '"The numerical summaries used to develop the toolkit (or the alternative \'barometer of influences\': [[John Hattie|Hattie]] 2009) are not a measure of educational impact."': '“用于开发工具包（或替代性的‘影响气压计’：[[John Hattie|Hattie]] 2009）的数字摘要，并不是教育影响力的衡量标准。”\n> ("The numerical summaries used to develop the toolkit (or the alternative \'barometer of influences\': [[John Hattie|Hattie]] 2009) are not a measure of educational impact.")',
    '"These violations do not cause random fluctuations in reported effect size: they are not just noise which gets factored out when large numbers of studies are combined. Instead, there is systematic and unadjusted bias in the violation of these assumptions."': '“这些违背并不会在报告的效应量中引起随机波动：它们不仅仅是在合并大量研究时会被剔除的噪音。相反，在违背这些假设的过程中存在系统性的且未经调整的偏见。”\n> ("These violations do not cause random fluctuations in reported effect size: they are not just noise which gets factored out when large numbers of studies are combined. Instead, there is systematic and unadjusted bias in the violation of these assumptions.")',
    '"While calculating an effect size may be simple enough for a first course in statistics, there are considerable subtleties in understanding it sufficiently well to ensure that the processes of combining effect sizes in meta-analyses allows valid conclusions to be drawn."': '“虽然计算效应量对于统计学的入门课程来说可能足够简单，但在充分理解它以确保在元分析中组合效应量的过程能够得出有效结论方面，存在相当大的微妙之处。”\n> ("While calculating an effect size may be simple enough for a first course in statistics, there are considerable subtleties in understanding it sufficiently well to ensure that the processes of combining effect sizes in meta-analyses allows valid conclusions to be drawn.")',
    '"Standardised effect size is a research tool for individual studies, not a policy tool for directing whole educational areas."': '“标准化效应量是用于单项研究的研究工具，而不是用于指导整个教育领域的政策工具。”\n> ("Standardised effect size is a research tool for individual studies, not a policy tool for directing whole educational areas.")',
    '"It might be argued that \'effect size\' is badly named. It is not simply a measure of the size of an effect at all and it might have been better named \'effect clarity\': a large d indicates that, for that particular intervention, between the two groups used and on the measure selected, the difference is very clear. But that does not mean the difference is large or important or educationally significant."': '“有人可能会说‘效应量（effect size）’这个名字起得很糟糕。它根本不仅仅是对效应大小的衡量，它或许更应该被命名为‘效应清晰度（effect clarity）’：一个很大的 d 值表明，对于该特定干预，在所使用的两组之间以及所选定的测量指标上，差异非常清晰。但这并不意味着这种差异很大、很重要或具有教育意义。”\n> ("It might be argued that \'effect size\' is badly named. It is not simply a measure of the size of an effect at all and it might have been better named \'effect clarity\': a large d indicates that, for that particular intervention, between the two groups used and on the measure selected, the difference is very clear. But that does not mean the difference is large or important or educationally significant.")',
    '"These meta-meta-analyses which order areas on the basis of effect size are thus poor selection mechanisms for driving educational policy and should not be used for directing large portions of a country\'s education budget."': '“因此，这些基于效应量对领域进行排序的元-元分析，是驱动教育政策的糟糕选择机制，不应被用于指导一个国家教育预算的大部分流向。”\n> ("These meta-meta-analyses which order areas on the basis of effect size are thus poor selection mechanisms for driving educational policy and should not be used for directing large portions of a country\'s education budget.")',

    # Argument_Knudsen_2017_NordSTEP.md
    '"I am a measurement person, I am a statistician, and the work with the concept and implementation was kind of a hobby I did on the side."': '“我是一个搞测量的人，我是一个统计学家，而这个概念以及实施方面的工作只是我业余的一种爱好。”\n> ("I am a measurement person, I am a statistician, and the work with the concept and implementation was kind of a hobby I did on the side.")',
    '"It is scripted. To the word. You would never know it, and that\'s part of the success."': '“这是有脚本的。精确到每个字。你永远不会知道，而这也是成功的一部分。”\n> ("It is scripted. To the word. You would never know it, and that\'s part of the success.")',

    # Argument_Qvortrup_2019_NordSTEP.md
    '"The aim of Visible Learning is to support teachers\' professional judgement. One of the contributions of educational research is, as accurate as possible, to identify, which interventions and conditions with the greatest probability will lead to learning and personal development. The aim is not to provide teachers with what works best recipes. The aim is to provide teachers with \'[[Hypothesis|hypotheses]] for intelligent problem solving\' (Hattie, 2009, p. 247)."': '“可见的学习（Visible Learning）的目的是支持教师的专业判断。教育研究的贡献之一是尽可能准确地识别哪些干预措施和条件最有可能带来学习和个人发展。其目的并不是为教师提供‘什么最有效’的食谱。其目的是为教师提供‘智能解决问题的[[Hypothesis|假设]]’ (Hattie, 2009, p. 247)。”\n> ("The aim of Visible Learning is to support teachers\' professional judgement. One of the contributions of educational research is, as accurate as possible, to identify, which interventions and conditions with the greatest probability will lead to learning and personal development. The aim is not to provide teachers with what works best recipes. The aim is to provide teachers with \'[[Hypothesis|hypotheses]] for intelligent problem solving\' (Hattie, 2009, p. 247).")',

    # Argument_Eacott_2011_JEAH.md
    '"The preparation of principals in the New South Wales public school system is evidence of the diminished strength of the [[Champ|field]] of schooling to refract interference from other fields, particularly the economic and political fields."': '“新南威尔士州公立学校系统对校长的培训，证明了学校教育[[Champ|场域]]折射来自其他场域（特别是经济和政治场域）干预的力量正在减弱。”\n> ("The preparation of principals in the New South Wales public school system is evidence of the diminished strength of the [[Champ|field]] of schooling to refract interference from other fields, particularly the economic and political fields.")',
    '"The central thesis of this article is that if school leaders are to reclaim their radical past and engage in public intellectualism, an alternate leadership [[Habitus]], one built on educational problem posing and contestation as opposed to organisational problem solving, is required."': '“本文的核心论点是，如果学校领导者要重拾其激进的过去并参与公共知识分子活动，就需要一种替代性的领导[[Habitus|惯习]]，这种惯习是建立在提出教育问题和争论（而非解决组织问题）的基础之上的。”\n> ("The central thesis of this article is that if school leaders are to reclaim their radical past and engage in public intellectualism, an alternate leadership [[Habitus]], one built on educational problem posing and contestation as opposed to organisational problem solving, is required.")',
    '"To be a player in the game of [[School Leadership]], one must learn or be habituated to the rules of the game. A game couched in economic language with frequent intervention, or interference, from those beyond education."': '“要成为[[School Leadership|学校领导力]]游戏中的玩家，一个人必须学习或习惯于游戏规则。这是一场用经济语言表达的游戏，伴随着来自教育领域之外的人的频繁干预或干扰。”\n> ("To be a player in the game of [[School Leadership]], one must learn or be habituated to the rules of the game. A game couched in economic language with frequent intervention, or interference, from those beyond education.")',
    '"Any attempt to objectify and/or de-contextualise leadership practice destroys that which it attempts to explain. Leadership is a social practice, it is not static, it is defined moment-by-moment in the interactions between organisational/group members."': '“任何试图将领导实践客观化和/或去情境化的尝试，都会摧毁它试图解释的东西。领导力是一种社会实践，它不是静止的，它是在组织/群体成员之间的互动中每时每刻被定义出来的。”\n> ("Any attempt to objectify and/or de-contextualise leadership practice destroys that which it attempts to explain. Leadership is a social practice, it is not static, it is defined moment-by-moment in the interactions between organisational/group members.")',
    '"If orthodoxy is to be challenged alternate ways of being are needed. Not just alternate means of problem solving, but alternate ways of thinking and problem posing."': '“如果正统观念要受到挑战，就需要替代性的存在方式。不仅仅是解决问题的替代手段，还必须是替代性的思维方式和提出问题的方式。”\n> ("If orthodoxy is to be challenged alternate ways of being are needed. Not just alternate means of problem solving, but alternate ways of thinking and problem posing.")',

    # Argument_Keddie_2020_JEAH.md
    '"the notion of markets [is] not … terrific in other domains of adult experience but they are toxic for children — because the sense of a child existing in a market and hierarchy with winners/losers is absolutely antithetical to our understanding of what everyone wants for our young"': '“市场的概念……在成人经验的其他领域也算不上太好，但它们对儿童来说是有毒的——因为让一个儿童存在于一个有赢家/输家的市场和等级制度中的感觉，绝对与我们对大家希望年轻人得到什么的理解背道而驰。”\n> ("the notion of markets [is] not … terrific in other domains of adult experience but they are toxic for children — because the sense of a child existing in a market and hierarchy with winners/losers is absolutely antithetical to our understanding of what everyone wants for our young")',
    '"you couldn\'t design something more effective for social division"': '“你不可能设计出比这更有效的社会分化工具了”\n> ("you couldn\'t design something more effective for social division")',
    '"nobody knows, except the principal" where funds are allocated, "because it is not transparent"': '除了校长，“没有人知道”资金被分配到哪里去了，“因为它是不透明的”\n> ("nobody knows, except the principal" where funds are allocated, "because it is not transparent")',
    '"it is a class system; very much a class system"': '“这是一个阶级系统；非常严重的阶级系统”\n> ("it is a class system; very much a class system")',
    '"as long as these [market] imperatives are dominant in such governance, there will continue to be \'goal displacement\' … and a compromising of ethical practice within our public education systems"': '“只要这些[市场]要求在这种治理中占主导地位，我们公共教育系统内就将继续存在‘目标置换’……以及对伦理实践的妥协”\n> ("as long as these [market] imperatives are dominant in such governance, there will continue to be \'goal displacement\' … and a compromising of ethical practice within our public education systems")',

    # Argument_SpronkenSmith_2024_AEHE.md
    '"I can\'t think of a single thing that I didn\'t already get preparation for in terms of just job skills that were very transferable."': '“我连一件我尚未获得工作技能准备的事情都想不出来，那些技能是非常可迁移的。”\n> ("I can\'t think of a single thing that I didn\'t already get preparation for in terms of just job skills that were very transferable.")',
    '"It\'s a thinking game… how we see the world and how we prepare ourselves to see the world from others\' views. No matter if you are in academia, in consultancy or in private, the qualification does serve a purpose, it\'s just how you transfer the skills being learned to different aspects in life."': '“这是一场思维游戏……关乎我们如何看待世界，以及我们如何准备从他人的视角看待世界。无论你是在学术界、咨询界还是在私营部门，这个资质确实是有用的，问题只在于你如何将学到的技能迁移到生活的不同方面。”\n> ("It\'s a thinking game… how we see the world and how we prepare ourselves to see the world from others\' views. No matter if you are in academia, in consultancy or in private, the qualification does serve a purpose, it\'s just how you transfer the skills being learned to different aspects in life.")',
    '"I was strongly encouraged by my mentors to pursue an academic pathway from undergraduate onward. This was implied to be the only career pathway and/or career pathway for those with the best skills… No one ever discussed any other possibilities."': '“从本科阶段起，我的导师就强烈鼓励我追求学术道路。这被暗示为唯一的职业道路和/或那些拥有最好技能的人的职业道路……从来没有人讨论过其他任何可能性。”\n> ("I was strongly encouraged by my mentors to pursue an academic pathway from undergraduate onward. This was implied to be the only career pathway and/or career pathway for those with the best skills… No one ever discussed any other possibilities.")',
    '"There\'s a default assumption that everybody in the department is going to go into academia."': '“系里有一个默认的假设，即系里的每个人都将进入学术界。”\n> ("There\'s a default assumption that everybody in the department is going to go into academia.")'
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
