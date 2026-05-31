import os

replacements = {
    # Argument_Eacott_2015_EPT.md
    '"A social \'scientific\' approach to educational administration, as advocated for in this article, must break free of the ambition of grounding in (rational) reason, the arbitrary division of the social world (e.g. administrators/non-administrators) and instead, take for its object, rather than getting itself caught up in, the struggle for the monopoly of the legitimate representation of the social world."': '“正如本文所倡导的，一种社会‘科学’的教育行政途径必须摆脱以（理性）理智为基础的野心，摆脱对社会世界的任意划分（例如，管理者/非管理者），相反，它应该将争夺社会世界合法再现的垄断权作为其客体，而不是让自己陷入其中。”\n> ("A social \'scientific\' approach to educational administration, as advocated for in this article, must break free of the ambition of grounding in (rational) reason, the arbitrary division of the social world (e.g. administrators/non-administrators) and instead, take for its object, rather than getting itself caught up in, the struggle for the monopoly of the legitimate representation of the social world.")',
    '"administration may derive its most substantive scientific work not from producing countless lists of best practice and essential traits or behaviours, but rather through a constant effort to undertake an informed critique of its own reasoning"': '“行政学可能不是通过炮制无数的最佳实践清单以及基本特征或行为清单，而是通过不断努力对其自身的推理进行有据可依的批判，来得出其最实质性的科学工作”\n> ("administration may derive its most substantive scientific work not from producing countless lists of best practice and essential traits or behaviours, but rather through a constant effort to undertake an informed critique of its own reasoning")',
    '"the educational administration researcher does not stand outside of the social world they analyse, nor do they look down on it from above. Rather, they themselves are agents in the social world"': '“教育行政研究者并不站在他们所分析的社会世界之外，也没有居高临下地俯视它。相反，他们自己也是社会世界中的能动者”\n> ("the educational administration researcher does not stand outside of the social world they analyse, nor do they look down on it from above. Rather, they themselves are agents in the social world")',
    '"nothing can be defined or assumed a priori. That is, the popular practice, especially with graduate students, of operationally defining objects is not appropriate"': '“没有任何东西可以先验地被定义或假设。也就是说，那种操作性定义客体的流行做法（尤其是在研究生中）是不合适的”\n> ("nothing can be defined or assumed a priori. That is, the popular practice, especially with graduate students, of operationally defining objects is not appropriate")',
    '"theory is not something that the researcher applies to the empirical; rather, it is a way of working through and with the empirical"': '“理论不是研究者应用于经验事实的东西；相反，它是一种通过并与经验事实一起工作的方式”\n> ("theory is not something that the researcher applies to the empirical; rather, it is a way of working through and with the empirical")',

    # Argument_Rømer_2018_EPT.md
    '"The mistake I was making was seeing [[Feedback]] as something teachers provide to students... It was only when I discovered that feedback was most powerful when it is from the student to the teacher that I started to understand it better."': '“我犯的错误是把[[Feedback|反馈]]看作是教师提供给学生的东西……直到我发现当反馈是从学生传向教师时它才是最强大的，我才开始更好地理解它。”\n> ("The mistake I was making was seeing [[Feedback]] as something teachers provide to students... It was only when I discovered that feedback was most powerful when it is from the student to the teacher that I started to understand it better.")',
    '"We end up with a world without education and without Beethoven\'s symphonies, and also without things and scientific energy altogether."': '“我们最终将得到一个没有教育也没有贝多芬交响乐的世界，而且也完全没有事物和科学能量。”\n> ("We end up with a world without education and without Beethoven\'s symphonies, and also without things and scientific energy altogether.")',

    # Argument_Nielsen_2021_NordPsych.md
    '"I am a measurement researcher; I am a statistician, I am not a theoretician"': '“我是一个测量研究者；我是一个统计学家，我不是一个理论家”\n> ("I am a measurement researcher; I am a statistician, I am not a theoretician")',
    '"This cut was the average effect from 800-plus meta-analyses... It is a threshold to create a story"': '“这个切分点是来自800多项元分析的平均效应……它是一个用来创造故事的阈值”\n> ("This cut was the average effect from 800-plus meta-analyses... It is a threshold to create a story")',
    '"Within this large body of [[Feedback]] research, there are many conflicting findings and no consistent pattern of results"': '“在这大量的[[Feedback|反馈]]研究中，存在许多相互冲突的发现，并没有一致的结果模式”\n> ("Within this large body of [[Feedback]] research, there are many conflicting findings and no consistent pattern of results")',
    '"The problem occurs when researchers do not explicate how their empirical work is related to and based on theoretical assumptions"': '“当研究者没有阐明他们的实证工作是如何与理论假设相关并基于理论假设时，问题就出现了”\n> ("The problem occurs when researchers do not explicate how their empirical work is related to and based on theoretical assumptions")',

    # Argument_Marginson_2025_ROE.md
    '"If time unfolds as change then space unfolds as interaction"': '“如果时间作为变迁而展开，那么空间则作为互动而展开”\n> ("If time unfolds as change then space unfolds as interaction")',
    '"There are always loose ends"': '“总是有未竟的线索（未收尾之处）”\n> ("There are always loose ends")',
    '"Conceptualizing space as open, multiple and relational, unfinished and always becoming, is a prerequisite for history to be open and thus … for the possibility of politics"': '“将空间概念化为开放的、多重的和相关的、未完成的且始终在生成的，这是历史保持开放的先决条件，进而……也是政治保持可能性的先决条件”\n> ("Conceptualizing space as open, multiple and relational, unfinished and always becoming, is a prerequisite for history to be open and thus … for the possibility of politics")',
    '"Higher education should not be viewed solely as an educational endeavour, but also as a geopolitical project"': '“高等教育不应仅仅被视为一项教育事业，而应同时被视为一项地缘政治项目”\n> ("Higher education should not be viewed solely as an educational endeavour, but also as a geopolitical project")',
    '"So many of our accustomed ways of imagining space have been attempts to tame it"': '“我们许多习惯的想象空间的方式，都曾是试图驯服它的尝试”\n> ("So many of our accustomed ways of imagining space have been attempts to tame it")',
    '"Every space eventually \'escapes in part from those who make use of it\'"': '“每一个空间最终都‘在某种程度上逃脱了那些利用它的人的掌控’”\n> ("Every space eventually \'escapes in part from those who make use of it\'")'
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
