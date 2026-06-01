import os

replacements = {
    # Argument_Yu_2024_CE.md
    '"The interpretation of the Confucian tradition is a monopolising and dominant discourse that reinforces the cultural hierarchy between different cultural groups."': '“对儒家传统的这种解释是一种垄断性的、占主导地位的话语，它强化了不同文化群体之间的文化等级制度。”\n> ("The interpretation of the Confucian tradition is a monopolising and dominant discourse that reinforces the cultural hierarchy between different cultural groups.")',
    '"The students appear to regard the Confucian tradition as only one culture and worldview in China, which can benefit from the critical reflexivity of other cultures."': '“学生们似乎将儒家传统仅仅视为中国的一种文化和世界观，这种文化和世界观可以从其他文化的批判性反思中获益。”\n> ("The students appear to regard the Confucian tradition as only one culture and worldview in China, which can benefit from the critical reflexivity of other cultures.")',
    '"Cultural exclusion perpetuates ethnic minority inequality."': '“文化排斥使少数民族的不平等永久化。”\n> ("Cultural exclusion perpetuates ethnic minority inequality.")',
    '"The dominant official version of Confucianism, presenting it as the core of a monolithic Han culture to be revered and imitated by all lesser minzu, thus tends to stoke cultural division and alienation."': '“占主导地位的官方版儒家思想，将其作为庞大单一的汉族文化的核心，要求所有其他少数民族尊崇和模仿，因此往往会煽动文化分裂和异化。”\n> ("The dominant official version of Confucianism, presenting it as the core of a monolithic Han culture to be revered and imitated by all lesser minzu, thus tends to stoke cultural division and alienation.")',

    # Argument_Teng_2025_CE.md
    '"The administrative discrimination based on [[Hukou System|hukou]] is increasingly and implicitly being replaced by market discrimination based on family socioeconomic standings."': '“基于[[Hukou System|户口]]的行政歧视正日益且隐蔽地被基于家庭社会经济地位的市场歧视所取代。”\n> ("The administrative discrimination based on [[Hukou System|hukou]] is increasingly and implicitly being replaced by market discrimination based on family socioeconomic standings.")',
    '"The departure of rural children subjects village schools to decreased funding, accelerated teacher turnover, worsening academic performance, and an ultimately increased risk of school closures."': '“农村儿童的流失使村级学校面临资金减少、教师流失加速、学业表现恶化以及最终学校关闭风险增加的困境。”\n> ("The departure of rural children subjects village schools to decreased funding, accelerated teacher turnover, worsening academic performance, and an ultimately increased risk of school closures.")',
    '"School choice, whether driven by marketisation or urbanisation, merely addresses the surface issues when it comes to educational inequality."': '“无论是受市场化还是城市化驱动的择校，在涉及教育不平等时，都仅仅触及了表面问题。”\n> ("School choice, whether driven by marketisation or urbanisation, merely addresses the surface issues when it comes to educational inequality.")',

    # Argument_Vickers_2024_CE.md
    '"The post-2020 overhaul of the curriculum for [[Liberal Studies]] / [[Citizenship and Social Development|CSD]] signals a decisive shift from an emphasis on fostering qualities … essential to the responsible exercise of participatory citizenship, towards imposition of a homogenous and totalising vision of Hong Kong-as-Chinese."': '“2020年后对[[Liberal Studies|通识教育]] / [[Citizenship and Social Development|公民与社会发展科（CSD）]]的全面改革标志着一种决定性的转变：从强调培养……对负责任地行使参与式公民权至关重要的品质，转向强加一种将香港视为中国人的同质化、总体化的愿景。”\n> ("The post-2020 overhaul of the curriculum for [[Liberal Studies]] / [[Citizenship and Social Development|CSD]] signals a decisive shift from an emphasis on fostering qualities … essential to the responsible exercise of participatory citizenship, towards imposition of a homogenous and totalising vision of Hong Kong-as-Chinese.")',
    '"While within Hong Kong, political and ideological discourse pays less direct or explicit homage to the CCP and the person of Xi himself than on the mainland, a growing convergence in narratives of history, culture, values and identity is clear."': '“虽然在香港内部，政治和意识形态话语对中共及习近平本人的致敬不如在内地那样直接或明确，但在历史、文化、价值观和认同叙事上的日益趋同是显而易见的。”\n> ("While within Hong Kong, political and ideological discourse pays less direct or explicit homage to the CCP and the person of Xi himself than on the mainland, a growing convergence in narratives of history, culture, values and identity is clear.")',
    '"Official discourse meanwhile reduces youth alienation to a matter of individual psychological deviance. With critique of the established order now outlawed as treasonous, explanations for public discontent must be sought at the level of private or individual maladaptation."': '“与此同时，官方话语将青年的疏离感简化为个体心理异常的问题。随着对既定秩序的批评如今被定性为叛国并被宣布为非法，对公众不满的解释就必须在私人或个体适应不良的层面上去寻找了。”\n> ("Official discourse meanwhile reduces youth alienation to a matter of individual psychological deviance. With critique of the established order now outlawed as treasonous, explanations for public discontent must be sought at the level of private or individual maladaptation.")',
    '"Hong Kong thus stands as a warning of how \'decolonial\' thinking, in obsessing over the \'pedigree\' of ideas, can overlook the importance of native \'agency\'."': '“因此，香港成为了一个警告，警示了‘去殖民化’思维在沉迷于思想的‘血统’时，是如何可能忽视本土‘能动性’的重要性的。”\n> ("Hong Kong thus stands as a warning of how \'decolonial\' thinking, in obsessing over the \'pedigree\' of ideas, can overlook the importance of native \'agency\'.")',
    '"In fulfilment of a fascistic vision of culture, race and state sovereignty, politics in the new Hong Kong is no longer presented as an arena for civic agency, but as a stage for performing patriotic loyalty."': '“为了实现关于文化、种族和国家主权的法西斯式愿景，新香港的政治不再被呈现为公民能动性的竞技场，而是作为表演爱国忠诚的舞台。”\n> ("In fulfilment of a fascistic vision of culture, race and state sovereignty, politics in the new Hong Kong is no longer presented as an arena for civic agency, but as a stage for performing patriotic loyalty.")'
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
