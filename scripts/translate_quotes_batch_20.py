import os

replacements = {
    # Argument_Eacott_2017_SLM.md
    '"I argue that the uncritical acceptance and proliferation of this cult is a tragedy for Australian [[School Leadership]]."': '“我认为，这种对个人崇拜的盲目接受和扩散是澳大利亚[[School Leadership|学校领导力]]领域的一场悲剧。”\n> ("I argue that the uncritical acceptance and proliferation of this cult is a tragedy for Australian [[School Leadership]].")',
    '"Rather than models of pedagogy, even those that came with instruments to measure the quality of practice ... Hattie provided school administrators with evidence on which they could base decisions – evidence informed decisions."': '“相比于教学模型——即使是那些配有衡量实践质量工具的模型——哈蒂（Hattie）为学校管理者提供的是他们可以据以做出决策的证据，即循证决策。”\n> ("Rather than models of pedagogy, even those that came with instruments to measure the quality of practice ... Hattie provided school administrators with evidence on which they could base decisions – evidence informed decisions.")',
    '"The partitioning of teaching into smallest measurable units, a piecemeal articulation of how to improve student learning, is not too removed from the work of Taylor over 100 years ago."': '“将教学划分为最小的可测量单位，这种零碎地阐述如何改善学生学习的方式，与100多年前泰勒（Taylor）的工作并没有太大的区别。”\n> ("The partitioning of teaching into smallest measurable units, a piecemeal articulation of how to improve student learning, is not too removed from the work of Taylor over 100 years ago.")',
    '"To subjectify oneself to a single figure is to elevate that individual to guru status. What the Australian school leadership community arguably needs is more rigorous and robust work and more significantly, dialogue and debate (to which Hattie is a part) not the blind adherence to a single guru."': '“将自己主体化于某个单一人物之下，就是将该人物提升到了‘教父（guru）’的地位。澳大利亚学校领导力共同体可以说更需要的是更严谨、更稳健的工作，以及更重要的对话与辩论（哈蒂也是其中的一部分），而不是盲目追随某一个教父。”\n> ("To subjectify oneself to a single figure is to elevate that individual to guru status. What the Australian school leadership community arguably needs is more rigorous and robust work and more significantly, dialogue and debate (to which Hattie is a part) not the blind adherence to a single guru.")',

    # Argument_Hattie_2017_SLM.md
    '"Every paradigm or set of conjectures should be tested to destruction and its authors, adherents, and users of the ideas should face public accountability. Thesis-antithesis-synthesis is well built into the water of academia."': '“每一个范式或每一组推测都应该被测试到直至毁灭，其思想的作者、追随者和使用者都应该面临公共问责。正题-反题-合题（Thesis-antithesis-synthesis）已经深深植根于学术界的传统之中。”\n> ("Every paradigm or set of conjectures should be tested to destruction and its authors, adherents, and users of the ideas should face public accountability. Thesis-antithesis-synthesis is well built into the water of academia.")',

    # Argument_Johnson_2023_CE.md
    '"We view this opaque exposition of methodology as outside the spirit of scientific inquiry"': '“我们认为，这种不透明的方法论阐述不符合科学探究的精神”\n> ("We view this opaque exposition of methodology as outside the spirit of scientific inquiry")',
    '"Visible Learning is a product that exists in the marketized world of educational gurus and magic bullet fads. This is far from the tradition of careful experimentation and peer review."': '“‘可见的学习’是一个存在于由教育教父和‘灵丹妙药’式热潮组成的市场化世界中的产品。这与严谨实验和同行评审的传统相去甚远。”\n> ("Visible Learning is a product that exists in the marketized world of educational gurus and magic bullet fads. This is far from the tradition of careful experimentation and peer review.")',
    '"It promises simple, cheap, classroom level fixes to manufactured alarm surrounding achievement scores."': '“它承诺针对围绕学业成绩分数制造出的恐慌，提供简单、廉价、课堂层面的修复方案。”\n> ("It promises simple, cheap, classroom level fixes to manufactured alarm surrounding achievement scores.")',

    # Argument_Bainbridge_2022_ROE.md (cleaning up the straggler)
    '"What has emerged...is a discourse that is constructive as it actively and persistently distorts the meaning of \'good\'—it is a sidestep into a world of fantasised goodness, while also away from an often-unspoken world of \'badness\'"': '“已经出现的是一种具有建构性的话语，因为它积极且持续地扭曲了‘优秀’的含义——这是一种向幻想中的‘优秀’世界的侧步避让（sidestep），同时也远离了一个经常不被提及的‘糟糕’世界。”\n> ("What has emerged...is a discourse that is constructive as it actively and persistently distorts the meaning of \'good\'—it is a sidestep into a world of fantasised goodness, while also away from an often-unspoken world of \'badness\'")'
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
