import os

replacements = {
    # Argument_Ryan_2010_ChineseLearner.md
    '"There is a notable tendency in the applied linguistics literature to report the perceptions and reactions of Western instructors which, rather than being interrogated for ethnocentric bias and stereotyping, are validated by recourse to a Confucian heritage explanation which appears plausible rather than being empirically established."': '“在应用语言学文献中存在一种显著的倾向：报告西方教师的看法和反应，而没有质疑其民族中心主义偏见和刻板印象，反而是通过诉诸一种看似合理而非基于实证确立的儒家传统解释来证实它们。”\n> ("There is a notable tendency in the applied linguistics literature to report the perceptions and reactions of Western instructors which, rather than being interrogated for ethnocentric bias and stereotyping, are validated by recourse to a Confucian heritage explanation which appears plausible rather than being empirically established.")',

    # Argument_Gilison_Wilson_2025_UniversityStartups.md
    '"Ask for money and they\'ll give you advice. Ask for advice and they\'ll give you money."': '“你问他们要钱，他们会给你建议。你问他们要建议，他们会给你钱。”\n> ("Ask for money and they\'ll give you advice. Ask for advice and they\'ll give you money.")',

    # Argument_Boccanfuso_Hall_2025_Alignment.md
    '"Innovation today often occurs at the \'interface,\' the interstitial space where industry and universities work with each other toward common goals."': '“当今的创新通常发生在‘界面’处，即产业界和大学为了共同目标而相互合作的间隙空间。”\n> ("Innovation today often occurs at the \'interface,\' the interstitial space where industry and universities work with each other toward common goals.")',
    '"Strength and impact are developed not solely through relationships between universities and industry but engagement."': '“实力与影响力的发展，不仅仅依靠大学与产业之间的关系，更在于深度参与。”\n> ("Strength and impact are developed not solely through relationships between universities and industry but engagement.")',
    '"Innovation does not readily occur in isolation."': '“创新很难在孤立的状态下发生。”\n> ("Innovation does not readily occur in isolation.")',
    '"There is substantial literature which suggests that continuous high levels of radical innovation in modern societies require diversity in organization forms, heterogeneity in organizational structures, diversity in ideas."': '“有大量文献表明，现代社会要持续保持高水平的激进创新，就需要组织形式的多样性、组织结构的异质性以及思想的多样性。”\n> ("There is substantial literature which suggests that continuous high levels of radical innovation in modern societies require diversity in organization forms, heterogeneity in organizational structures, diversity in ideas.")',

    # Argument_Rizvi_2022_Springer.md
    '"Asia is rising but Asian wellbeing is not. The quality and quantity of growth are out of synch."': '“亚洲在崛起，但亚洲人的福祉却没有。增长的质量和数量不同步。”\n> ("Asia is rising but Asian wellbeing is not. The quality and quantity of growth are out of synch.")',
    '"language and text can create, shift, or maintain ideologies. In the case of [[GATS and Trade in Education Services|GATS]], the ideology reflects a new imperialism where more powerful countries retain developing countries as markets in which they continue to rule intellectually"': '“语言和文本可以创造、转移或维持意识形态。在[[GATS and Trade in Education Services|《服务贸易总协定》]]（GATS）的案例中，这种意识形态反映了一种新帝国主义，即更强大的国家将发展中国家保留为它们在知识上继续统治的市场。”\n> ("language and text can create, shift, or maintain ideologies. In the case of [[GATS and Trade in Education Services|GATS]], the ideology reflects a new imperialism where more powerful countries retain developing countries as markets in which they continue to rule intellectually")',
    '"the pandemic is a portal"': '“大流行是一扇传送门”\n> ("the pandemic is a portal")',
    '"The Asian Century is an Australian opportunity. As the global centre of gravity shifts to our region, the tyranny of distance is being replaced by the prospects of proximity"': '“亚洲世纪是澳大利亚的机遇。随着全球重心转移到我们这个地区，距离的暴政正在被相邻的前景所取代。”\n> ("The Asian Century is an Australian opportunity. As the global centre of gravity shifts to our region, the tyranny of distance is being replaced by the prospects of proximity")',

    # Argument_Amos_2022_Springer.md
    '"The diagnosis of scholars like Escobar and Haraway is clear enough: Without a significant change, not to say transformation of our mind-set, late modernity may as well be the last stage not only for humanity, but for the planet."': '“像 Escobar 和 Haraway 等学者的诊断已经足够清晰：如果不发生重大改变，或者说如果不转变我们的思维方式，晚期现代性很可能不仅是人类的最后阶段，也是这个星球的最后阶段。”\n> ("The diagnosis of scholars like Escobar and Haraway is clear enough: Without a significant change, not to say transformation of our mind-set, late modernity may as well be the last stage not only for humanity, but for the planet.")',
    '"What is needed then, is an educational theory that draws it all together. One that re-envisions public education with a non-compartmentalized organization of knowledge, that takes connectivity and [[Response-ability]], another term for caring as its organizing principle, one that encourages collaboration, is critical of ideologies that place the human being at the center of the universe, one that encourages non-dualistic thinking and the non-fixity of the self, pays attention to the multiple entanglements both material and non-material."': '“那么，我们需要的是一种能够将这一切结合起来的教育理论。这种理论用一种非碎片化的知识组织方式重新构想公共教育，将联结性和[[Response-ability|回应能力]]（关怀的另一个词）作为其组织原则，鼓励合作，批判将人类置于宇宙中心的意识形态，鼓励非二元思维和自我的非固定性，并关注物质和非物质的多重纠缠。”\n> ("What is needed then, is an educational theory that draws it all together. One that re-envisions public education with a non-compartmentalized organization of knowledge, that takes connectivity and [[Response-ability]], another term for caring as its organizing principle, one that encourages collaboration, is critical of ideologies that place the human being at the center of the universe, one that encourages non-dualistic thinking and the non-fixity of the self, pays attention to the multiple entanglements both material and non-material.")',

    # Argument_Rambla_2022_Springer.md
    '"The European Union has elaborated quite sophisticated imaginaries of education and innovation by means of [[Performance Indicators|policy instruments]] that use expert knowledge to draw certain geographical images of the member states and the regions within these states."': '“欧盟已经通过使用专家知识的[[Performance Indicators|政策工具]]，描绘出成员国及其内部区域的特定地理图像，从而构建了相当复杂的教育和创新想象。”\n> ("The European Union has elaborated quite sophisticated imaginaries of education and innovation by means of [[Performance Indicators|policy instruments]] that use expert knowledge to draw certain geographical images of the member states and the regions within these states.")',
    '"Performance indicators convey \'theories of change\' that highlight how policies activate certain mechanisms in a given context."': '“绩效指标传达了‘变革理论’，凸显了政策如何在特定情境中激活某些机制。”\n> ("Performance indicators convey \'theories of change\' that highlight how policies activate certain mechanisms in a given context.")',
    '"Performance indicators are a policy instrument that directly draws on scientific and technical legitimacy, and pushes policy actors towards competition."': '“绩效指标是一种直接利用科学和技术合法性的政策工具，它推动政策行动者走向竞争。”\n> ("Performance indicators are a policy instrument that directly draws on scientific and technical legitimacy, and pushes policy actors towards competition.")',
    '"Policy instruments \'select\' relevant policy issues in the arena of public debate and simultaneously induce actors to sideline other issues."': '“政策工具在公共辩论的舞台上‘选择’相关的政策议题，同时引导行动者边缘化其他议题。”\n> ("Policy instruments \'select\' relevant policy issues in the arena of public debate and simultaneously induce actors to sideline other issues.")',

    # Argument_Moisio_2022_Springer.md
    '"In this chapter, I seek to geopoliticize the purportedly geoeconomic present. In particular, I argue that the contemporary knowledge-intensive capitalism is a historically contingent geopolitical constellation that brings together a range of issues such as space, cities, states, human capital, education, and technology."': '“在本章中，我试图将据称是地缘经济的现在地缘政治化。具体而言，我主张当代知识密集型资本主义是一个具有历史偶然性的地缘政治星系，它将空间、城市、国家、人力资本、教育和技术等一系列议题汇聚在一起。”\n> ("In this chapter, I seek to geopoliticize the purportedly geoeconomic present. In particular, I argue that the contemporary knowledge-intensive capitalism is a historically contingent geopolitical constellation that brings together a range of issues such as space, cities, states, human capital, education, and technology.")',
    '"Capitalism perpetually strives, therefore, to create a social and physical landscape in its own image and requisite to its own needs at a particular point in time, only just as certainly to undermine, disrupt and even destroy that landscape at a later point in time."': '“因此，资本主义永远在努力按照自己的形象并为满足自己在特定时间点的需求，去创造一种社会和物质景观，然而在随后的时间点，它又同样确凿地会去破坏、扰乱甚至摧毁这种景观。”\n> ("Capitalism perpetually strives, therefore, to create a social and physical landscape in its own image and requisite to its own needs at a particular point in time, only just as certainly to undermine, disrupt and even destroy that landscape at a later point in time.")',
    '"The [[Geopolitics of Knowledge]]-based economization emanates from the very tension within the capitalist circulation process in space: the tension within the geography of accumulation between fixity and motion."': '“基于[[Geopolitics of Knowledge|知识地缘政治]]的经济化，源于资本主义空间循环过程内部的张力：积累地理中固定性与运动之间的张力。”\n> ("The [[Geopolitics of Knowledge]]-based economization emanates from the very tension within the capitalist circulation process in space: the tension within the geography of accumulation between fixity and motion.")',

    # Argument_Zelinka_2022_SCD_subjectivity.md
    '"It is not skills and competencies gained by subjects, but subjectivities, i.e. modes of self-conduct based on desired competencies, that become a source of production."': '“成为生产源泉的，不是主体获得的技能和能力，而是主体性，即基于期望能力的自我行为模式。”\n> ("It is not skills and competencies gained by subjects, but subjectivities, i.e. modes of self-conduct based on desired competencies, that become a source of production.")',
    '"Subjects are only disposable unless they acknowledge and enhance their self-entrepreneurial subjectivity and show passion for growth and a will to accelerate."': '“主体只有承认并增强其自我创业的主体性，表现出对成长的热情和加速的意愿，才不会沦为一次性用品（被随时抛弃）。”\n> ("Subjects are only disposable unless they acknowledge and enhance their self-entrepreneurial subjectivity and show passion for growth and a will to accelerate.")',
    '"The opposition to this kind of novel and innovative endeavor starts with questioning its very basis, i.e. its definition of subjects as knowledge-bearers."': '“对这种新颖和创新尝试的反对，始于质疑其根本基础，即质疑其将主体定义为知识承载者的做法。”\n> ("The opposition to this kind of novel and innovative endeavor starts with questioning its very basis, i.e. its definition of subjects as knowledge-bearers.")',
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
