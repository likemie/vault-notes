import os

replacements = {
    # Argument_Gorur_2014_Discourse.md
    '"the insouciance and confidence with which the OECD routinely, annually, produces such a range of indicators … belies the decades of hesitation, experimentation, negotiation and effort that went into the development of these [[International Education]] indicators"': '“经合组织（OECD）常规地、每年地发布如此一系列指标时所表现出的那种漫不经心和自信……掩盖了这些[[International Education|国际教育]]指标在开发过程中所经历的数十年的犹豫、实验、协商和努力。”\n> ("the insouciance and confidence with which the OECD routinely, annually, produces such a range of indicators … belies the decades of hesitation, experimentation, negotiation and effort that went into the development of these [[International Education]] indicators")',
    '"the project\'s fundamental scientific ambition was inconsistent with the available means and the interests of the government authorities which would have had to fund the initiative. And so the social science specialists were unable to see their project through to its conclusion. It was a failure."': '“该项目根本性的科学雄心与可用的手段以及原本必须为该倡议提供资金的政府当局的利益是不一致的。因此，社会科学专家们无法将他们的项目进行到底。那是一个失败。”\n> ("the project\'s fundamental scientific ambition was inconsistent with the available means and the interests of the government authorities which would have had to fund the initiative. And so the social science specialists were unable to see their project through to its conclusion. It was a failure.")',
    '"one can get the impression that these indicators have been invented to avoid leaving empty cells in the subgroup of student achievement"': '“人们可能会产生这样一种印象：发明这些指标是为了避免在学生成就的子分组中留下空白单元格。”\n> ("one can get the impression that these indicators have been invented to avoid leaving empty cells in the subgroup of student achievement")',
    '"no cognitive approach leaves the subject of its observation, measurement, analysis, comparison, deciphering, completely unscathed. There is no clear ontological divide between science and techniques, between cognitive reality and its modification."': '“没有任何认知途径能让其观察、测量、分析、比较、破译的对象完全不受影响。科学与技术之间、认知现实与其修改之间，不存在清晰的本体论界限。”\n> ("no cognitive approach leaves the subject of its observation, measurement, analysis, comparison, deciphering, completely unscathed. There is no clear ontological divide between science and techniques, between cognitive reality and its modification.")',

    # Argument_McKnight_2020_Discourse.md
    '"In Visible Learning\'s [[Meta-analysis]], the wisdom of teachers is taken, processed, and served back, at a price. Teachers, in a feminised profession (Apple, 1986/2013), submit to heteronormative, sexist and ableist constructions of education."': '“在‘可见的学习’的[[Meta-analysis|元分析]]中，教师的智慧被夺取、加工，并以一定的代价被重新提供回来。在一个女性化的职业中（Apple, 1986/2013），教师们屈服于教育中异性恋正统的、性别歧视的和能力歧视的构建。”\n> ("In Visible Learning\'s [[Meta-analysis]], the wisdom of teachers is taken, processed, and served back, at a price. Teachers, in a feminised profession (Apple, 1986/2013), submit to heteronormative, sexist and ableist constructions of education.")',
    '"We hire people to deliver it and only one in five passes. That is because almost every teacher wants to get up and talk about their story, their anecdotes and their classrooms. We will not allow that, because as soon as you allow that, you legitimise every teacher in the room talking about their war stories, their views, their kids."': '“我们雇人来传达它（VL培训），只有五分之一的人能通过。那是因为几乎每位老师都想站起来谈论他们的故事、轶事和他们的课堂。我们不允许那样，因为一旦你允许了，你就让房间里的每位老师谈论他们的‘战争故事’、他们的观点、他们的孩子变得合法化了。”\n> ("We hire people to deliver it and only one in five passes. That is because almost every teacher wants to get up and talk about their story, their anecdotes and their classrooms. We will not allow that, because as soon as you allow that, you legitimise every teacher in the room talking about their war stories, their views, their kids.")',
    '"The eye, limited to that single function of sight, hides its inadequacies behind arrogance, and insists that seeing is the only way. ... The eye needs to be belligerent, as it is essentially made of vitreous jelly."': '“眼睛，局限于单一的视觉功能，将自己的不足隐藏在傲慢背后，并坚持认为‘看见’是唯一的方式。……眼睛需要具有好斗性，因为它本质上是由玻璃体冻胶构成的。”\n> ("The eye, limited to that single function of sight, hides its inadequacies behind arrogance, and insists that seeing is the only way. ... The eye needs to be belligerent, as it is essentially made of vitreous jelly.")',
    '"Visible Learning, despite all its complicated effect sizes, equations and figures, is ultimately too simple a mantra."': '“‘可见的学习’，尽管有着所有复杂的效应量、方程式和数字，最终仍是一个过于简单的咒语。”\n> ("Visible Learning, despite all its complicated effect sizes, equations and figures, is ultimately too simple a mantra.")',
    '"We hope our thoughts here may energise dialogue around Visible Learning and teacher professionalism and encourage others to enter the fray."': '“我们希望我们在这里的思考能够激发围绕‘可见的学习’和教师专业精神的对话，并鼓励其他人加入这场争论。”\n> ("We hope our thoughts here may energise dialogue around Visible Learning and teacher professionalism and encourage others to enter the fray.")',

    # Argument_Boccanfuso_Hall_2025_OrgStrategy.md (fixing the one seen in grep)
    '"Relationships"、"partnerships"和"engagement"三个词的精微差异值得注意。': '“Relationships”、“partnerships”和“engagement”三个词的精微差异值得注意。'
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
