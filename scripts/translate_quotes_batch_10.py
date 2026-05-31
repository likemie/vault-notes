import os

replacements = {
    # Argument_Cheung_2021_ROE.md
    '"For a very long time, educational policies have been based on ideological standpoints or individual views rather than evidence or best practices."': '“在很长一段时间里，教育政策都是基于意识形态立场或个人观点，而不是证据或最佳实践。”\n> ("For a very long time, educational policies have been based on ideological standpoints or individual views rather than evidence or best practices.")',
    '"When evaluating whether a treatment or a vaccine is effective, what they rely on are not small studies with questionable methodologies but large, well-conducted randomized controlled trials."': '“在评估一种治疗方法或疫苗是否有效时，他们依赖的不是方法论存疑的小型研究，而是大规模、执行良好的随机对照试验。”\n> ("When evaluating whether a treatment or a vaccine is effective, what they rely on are not small studies with questionable methodologies but large, well-conducted randomized controlled trials.")',

    # Argument_Dachet_2021_ROE.md
    '"for [[Evidence-Based Reform]] to prevail, three conditions must exist"': '“要让[[Evidence-Based Reform|循证改革]]盛行，必须具备三个条件”\n> ("for [[Evidence-Based Reform]] to prevail, three conditions must exist")',
    '"we are at the very beginning of the path"': '“我们正处于这条道路的最开端”\n> ("we are at the very beginning of the path")',

    # Argument_Ross_Morrison_2021_ROE.md
    '"Evidence does not exist in a void unaffected by prevailing educational policies and exigencies."': '“证据并不存在于一个不受现行教育政策和紧迫需求影响的真空中。”\n> ("Evidence does not exist in a void unaffected by prevailing educational policies and exigencies.")',
    '"Technology is not an operationally definable intervention but rather a mode for delivering instruction."': '“技术不是一种在操作上可定义的干预，而是一种传递教学的模式。”\n> ("Technology is not an operationally definable intervention but rather a mode for delivering instruction.")',

    # Argument_Pellegrini_2021_ROE.md
    '"Evidence cannot be used as a kind of recipe book"': '“证据不能被当作一种菜谱来使用”\n> ("Evidence cannot be used as a kind of recipe book")',
    '"Europe prefers the term \'evidence-informed education\'"': '“欧洲更倾向于使用‘证据启发的教育（evidence-informed education）’一词”\n> ("Europe prefers the term \'evidence-informed education\'")',

    # Argument_Wong_2022_HERD.md
    '"the formation of UK graduate attributes appears quite diverse, which is likely to reflect the individual cultures and ethos of the respective university, rather than to emulate any national frameworks"': '“英国毕业生特质的形成显得非常多样化，这很可能反映了各自大学独特的文化和精神气质，而不是在模仿任何国家框架。”\n> ("the formation of UK graduate attributes appears quite diverse, which is likely to reflect the individual cultures and ethos of the respective university, rather than to emulate any national frameworks")',
    '"Graduate attributes could be interpreted as a proxy for the \'ideal graduate\'"': '“毕业生特质可以被解释为‘理想毕业生’的代理指标。”\n> ("Graduate attributes could be interpreted as a proxy for the \'ideal graduate\'")',

    # Argument_Nelson_2017_ER.md
    '"Evidence-based practice is not \'cook book\' teaching or policing, nor should it be about prescribing what goes on from a position of unchallenged authority. It is about integrating professional expertise with the best external evidence from research to improve the quality of practice."': '“循证实践不是‘按图索骥（照菜谱做菜）’式的教学或监管，也不应该关于从一个不容挑战的权威位置来规定发生的事情。它是关于将专业技能与来自研究的最佳外部证据相结合，以提高实践质量。”\n> ("Evidence-based practice is not \'cook book\' teaching or policing, nor should it be about prescribing what goes on from a position of unchallenged authority. It is about integrating professional expertise with the best external evidence from research to improve the quality of practice.")',
    '"Evidence needs to be planted in \'fertile ground\' if it is to take root and grow."': '“如果证据要生根发芽，就需要被种植在‘肥沃的土壤’中。”\n> ("Evidence needs to be planted in \'fertile ground\' if it is to take root and grow.")',
    '"The process of being evidence-informed requires both rigorous evidence and a rigorous process of professional judgement."': '“成为证据启发（evidence-informed）的过程，既需要严谨的证据，也需要严谨的专业判断过程。”\n> ("The process of being evidence-informed requires both rigorous evidence and a rigorous process of professional judgement.")',
    '"We must not fall into the trap of seeking to understand only those components that can easily be quantified."': '“我们绝不能落入仅仅寻求理解那些容易被量化的组成部分的陷阱中。”\n> ("We must not fall into the trap of seeking to understand only those components that can easily be quantified.")',

    # Argument_Keddie_2020_IJLE.md
    '"the discourses and practices of devolution, economic efficiency, competition and individualism constitute [[School Autonomy]] in ways that have decimated structural support for public schools, exacerbated stratification and residualization within the sector, undermined a collective approach to education as a public good and disadvantaged rural/remote, low SES and small schools"': '“权力下放、经济效率、竞争和个人主义的话语和实践构成了[[School Autonomy|学校自主权]]，其方式摧毁了对公立学校的结构性支持，加剧了该部门内部的分层和边缘化，破坏了将教育作为公共产品的集体途径，并使农村/偏远地区、低社会经济地位（SES）和小型学校处于劣势。”\n> ("the discourses and practices of devolution, economic efficiency, competition and individualism constitute [[School Autonomy]] in ways that have decimated structural support for public schools, exacerbated stratification and residualization within the sector, undermined a collective approach to education as a public good and disadvantaged rural/remote, low SES and small schools")',
    '"To further public education as both ideal and practice (for the common good), we need a much more nuanced understanding of what is in the public interest, how the public is constituted and how we might define public education"': '“为了进一步将公共教育作为理想和实践（为了共同利益）来推进，我们需要对什么是公共利益、公众是如何构成的以及我们可能如何定义公共教育，有一种更加细致入微的理解。”\n> ("To further public education as both ideal and practice (for the common good), we need a much more nuanced understanding of what is in the public interest, how the public is constituted and how we might define public education")'
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
