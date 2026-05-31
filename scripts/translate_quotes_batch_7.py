import os

replacements = {
    # Argument_Hattie_2015_SOTLP.md
    '"When teachers see teaching and learning through the eyes of their students, and when students become their own teachers then outcomes and engagement are maximized."': '“当教师透过学生的眼睛来看待教与学，并且当学生成为他们自己的老师时，成果和参与度就会最大化。”\n> ("When teachers see teaching and learning through the eyes of their students, and when students become their own teachers then outcomes and engagement are maximized.")',
    '"As nearly every intervention can show some evidence of success, we need to ask not \'What works?\' but \'What works best\' and seek comparisons between different ways of influencing student learning."': '“由于几乎所有的干预措施都能显示出一些成功的证据，我们需要问的不是‘什么有效？’而是‘什么最有效’，并寻求对影响学生学习的不同方式进行比较。”\n> ("As nearly every intervention can show some evidence of success, we need to ask not \'What works?\' but \'What works best\' and seek comparisons between different ways of influencing student learning.")',
    '"It is less what teachers do in their teaching, but more how they think about their role. It is their mind frames, or ways of thinking about teaching and learning, that are most critical."': '“这较少关乎教师在教学中做了什么，而更多关乎他们如何思考自己的角色。他们对教与学的心智框架或思维方式，才是最关键的。”\n> ("It is less what teachers do in their teaching, but more how they think about their role. It is their mind frames, or ways of thinking about teaching and learning, that are most critical.")',
    '"The fundamental premise of [[Visible Learning]] is that when educators focus on defining, evaluating, and understanding their impact this leads to maximizing student learning and achievement."': '“[[Visible Learning|可见的学习]]的基本前提是，当教育工作者专注于定义、评估和理解他们的影响时，这会导致学生学习和成就的最大化。”\n> ("The fundamental premise of [[Visible Learning]] is that when educators focus on defining, evaluating, and understanding their impact this leads to maximizing student learning and achievement.")',

    # Argument_Larsen_2019_EducSci.md
    '"An international consensus seems to have developed in educational research—and among educational planners and policymakers—during the last 10–15 years proclaiming that learning is, and must be, a visible phenomenon. This paper questions this predominant view."': '“在过去10-15年间，教育研究界——以及教育规划者和决策者之间——似乎形成了一项国际共识，宣称学习是，也必须是一种可见的现象。本文对这种主导观点提出了质疑。”\n> ("An international consensus seems to have developed in educational research—and among educational planners and policymakers—during the last 10–15 years proclaiming that learning is, and must be, a visible phenomenon. This paper questions this predominant view.")',
    '"The thesis is that powerful scientific and political adherents of learning cannot see what they cannot see—neither when they see what they (think they) see, nor when they do not see what they do not (want to) see."': '“其论点是，对学习拥有强大科学和政治话语权的拥护者们看不到他们看不见的东西——无论是在他们看到他们（以为自己）看到的东西时，还是在他们没有看到他们不（想）看到的东西时。”\n> ("The thesis is that powerful scientific and political adherents of learning cannot see what they cannot see—neither when they see what they (think they) see, nor when they do not see what they do not (want to) see.")',
    '"The purpose of education is much more demanding and challenging than enhancing [[Visible Learning]] processes and results."': '“教育的目的比增强[[Visible Learning|可见的学习]]过程和结果要求更高，也更具挑战性。”\n> ("The purpose of education is much more demanding and challenging than enhancing [[Visible Learning]] processes and results.")',
    '"What goes on in the brain can never be directly depicted in the visible learning paradigm. Thinking is more than learning and learning is more than visible learning."': '“大脑中正在发生的事情永远无法在可见的学习范式中被直接描绘出来。思考不仅仅是学习，而学习也不仅仅是可见的学习。”\n> ("What goes on in the brain can never be directly depicted in the visible learning paradigm. Thinking is more than learning and learning is more than visible learning.")',

    # Argument_Håkansson_2015_TT.md
    '"One superior teaching dimension consists of structure and interaction."': '“一个卓越的教学维度是由结构和互动构成的。”\n> ("One superior teaching dimension consists of structure and interaction.")',
    '"The quality of interplay and communication between teacher and pupil is considered to be crucial."': '“师生之间互动与交流的质量被认为是至关重要的。”\n> ("The quality of interplay and communication between teacher and pupil is considered to be crucial.")',
    '"A too far-reaching individualisation ... has no research support, but, on the other hand, neither does a one-sided pulpit teaching."': '“一种走得太远的个性化……没有研究支持，但另一方面，单向的讲坛式教学也没有。”\n> ("A too far-reaching individualisation ... has no research support, but, on the other hand, neither does a one-sided pulpit teaching.")',

    # Argument_Zhao_2017_JEC.md
    '"I have not yet found an educational product that comes with a warning label carrying information such as \'this program works in raising your students\' test scores in reading, but may make them hate reading forever.\'"': '“我还没有发现哪个教育产品带有一个包含类似信息的警告标签：‘该项目在提高你学生的阅读考试分数方面有效，但可能会让他们永远讨厌阅读。’”\n> ("I have not yet found an educational product that comes with a warning label carrying information such as \'this program works in raising your students\' test scores in reading, but may make them hate reading forever.\'")',
    '"The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor."': '“任何量化社会指标越是被用于社会决策，它就越容易受到腐败压力的影响，也就越容易扭曲和腐蚀它旨在监控的社会过程。”\n> ("The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor.")',
    '"Teaching constrains children\'s exploration and discovery. Children who were taught a function of a toy performed fewer kinds of actions of the toy and discovered fewer of its other functions."': '“教学限制了儿童的探索和发现。被教授了玩具某项功能的儿童，对玩具执行的动作种类更少，发现的玩具其他功能也更少。”\n> ("Teaching constrains children\'s exploration and discovery. Children who were taught a function of a toy performed fewer kinds of actions of the toy and discovered fewer of its other functions.")',

    # Argument_Brady_2023_EPR.md
    '"The percentage of articles employing experimental methods has continued to decrease (20%), whereas qualitative methods have increased (22%)."': '“采用实验方法的文章比例继续下降（20%），而质性方法则有所上升（22%）。”\n> ("The percentage of articles employing experimental methods has continued to decrease (20%), whereas qualitative methods have increased (22%).")',
    '"In all approaches combined, in 2020, RFP were included in about two out of three nonintervention articles."': '“在结合所有路径的情况下，2020 年，大约三分之二的非干预文章中包含了实践建议（RFP）。”\n> ("In all approaches combined, in 2020, RFP were included in about two out of three nonintervention articles.")',
    '"The underlying assumption of this study is that any RFP that is not based on sound methodology that can identify causal relations is suspect."': '“本研究的潜在假设是，任何未建立在能识别因果关系的严谨方法论基础上的实践建议（RFP），都是值得怀疑的。”\n> ("The underlying assumption of this study is that any RFP that is not based on sound methodology that can identify causal relations is suspect.")',

    # Argument_Bolton_2017_ArchPsych.md
    '"This review suggests that Piagetian development theory may be closely aligned with changes in the anatomical and physiological development of the brain—in particular, the [[Prefrontal Cortex]] and its associated connections."': '“本综述表明，皮亚杰的发展理论可能与大脑解剖和生理发展的变化——特别是[[Prefrontal Cortex|前额叶皮层]]及其相关连接的变化——紧密一致。”\n> ("This review suggests that Piagetian development theory may be closely aligned with changes in the anatomical and physiological development of the brain—in particular, the [[Prefrontal Cortex]] and its associated connections.")',
    '"It is the claim of this article that the changes are a function of the development of executive functioning as the brain develops."': '“本文的主张是，这些变化是随着大脑发育，执行功能发展的一个函数。”\n> ("It is the claim of this article that the changes are a function of the development of executive functioning as the brain develops.")',

    # Argument_Yan_2025_JCS.md
    '"To make sense of this curriculum change, we address two questions: Why and how did [[Liberal Studies|LS]] emerge as a compulsory school subject; and why was it replaced by CSD in 2021?"': '“为了理解这种课程变革，我们解决两个问题：[[Liberal Studies|通识教育（LS）]]为何以及如何成为一门必修课；以及为什么它在 2021 年被 CSD（公民与社会发展科）所取代？”\n> ("To make sense of this curriculum change, we address two questions: Why and how did [[Liberal Studies|LS]] emerge as a compulsory school subject; and why was it replaced by CSD in 2021?")',
    '"The emergence of LS was linked to the post-handover restructuring of the education system, the quest for educational reform and facilitated by a process of referencing global trends and overseas models. Its demise was the result of direct state intervention following the introduction of the National Security Law in 2020."': '“LS（通识教育）的出现与回归后教育体系的重组、对教育改革的追求相关，并受到参考全球趋势和海外模式过程的推动。它的消亡是 2020 年引入国家安全法后，国家直接干预的结果。”\n> ("The emergence of LS was linked to the post-handover restructuring of the education system, the quest for educational reform and facilitated by a process of referencing global trends and overseas models. Its demise was the result of direct state intervention following the introduction of the National Security Law in 2020.")',
    '"All intended curriculum changes are at their core political."': '“所有预期的课程变革，其核心都是政治性的。”\n> ("All intended curriculum changes are at their core political.")',
    '"Local problems are sometimes created in line with packaged global solutions, rather than the other way round."': '“有时，本地问题是根据打包好的全球解决方案而被创造出来的，而不是相反。”\n> ("Local problems are sometimes created in line with packaged global solutions, rather than the other way round.")',
    '"The strain of holding together a society shot through with profound divisions of class, residency, culture and ethnicity falls largely upon schooling and propaganda, backed up by repressive violence."': '“将一个充斥着阶级、居住地、文化和种族深刻分歧的社会维系在一起的重任，很大程度上落在了学校教育和宣传上，并辅以压制性的暴力。”\n> ("The strain of holding together a society shot through with profound divisions of class, residency, culture and ethnicity falls largely upon schooling and propaganda, backed up by repressive violence.")',
    '"If there were an intention to \'kill\' LS, it would be more straightforward to abolish the subject."': '“如果有意要‘扼杀’通识科（LS），直接废除该科目会更直截了当。”\n> ("If there were an intention to \'kill\' LS, it would be more straightforward to abolish the subject.")',

    # Argument_Hitchcock_2015_JBE.md
    '"Generalization details are not evaluated but rather described in detail so that consumers can make their own determinations about generalization."': '“概括（Generalization）细节不被评估，而是被详细描述，以便消费者能够对概括性做出自己的决定。”\n> ("Generalization details are not evaluated but rather described in detail so that consumers can make their own determinations about generalization.")'
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
