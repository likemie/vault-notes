import os
import re

replacements = {
    # Argument_Slethaug_2010_InternationalEducation.md
    '"Educational systems tied to the formation of nation-state citizens and consumers bonded to local systems to the neglect of larger global forces are likely to become obsolete, while those that proactively engage globalization\'s new challenges are more likely to thrive."': '“那些与民族国家公民的培养和局限于本地系统的消费者紧密相连，而忽视更大全球力量的教育系统，很可能会变得过时；而那些主动应对全球化新挑战的教育系统则更有可能蓬勃发展。”\n> ("Educational systems tied to the formation of nation-state citizens and consumers bonded to local systems to the neglect of larger global forces are likely to become obsolete, while those that proactively engage globalization\'s new challenges are more likely to thrive.")',
    '"Perhaps more than most mainstream schools, therefore, [[International Schools]] must orient themselves to the market. They must provide curricula that are in demand at a price that can be afforded by their target clients, and must pay attention to changing demographic and economic forces."': '“因此，也许比大多数主流学校更重要的是，[[International Schools|国际学校]]必须面向市场。它们必须以目标客户能够承受的价格提供抢手的课程，并且必须关注不断变化的人口和经济力量。”\n> ("Perhaps more than most mainstream schools, therefore, [[International Schools]] must orient themselves to the market. They must provide curricula that are in demand at a price that can be afforded by their target clients, and must pay attention to changing demographic and economic forces.")',

    # Argument_Ryan_2010_ChineseLearner.md
    '"Chineseness is in effect defined in terms of deviance from Western norms, and generally as being interestingly different within mainstream, that is Western, psychology."': '“实际上，‘中国性（Chineseness）’是根据其偏离西方规范的程度来定义的，并且在主流（即西方）心理学中通常被认为是一种有趣的不同。”\n> ("Chineseness is in effect defined in terms of deviance from Western norms, and generally as being interestingly different within mainstream, that is Western, psychology.")',
    '"It is particularly infuriating to hear problems with such rhetorical styles attributed to imagined inadequacies in the student\'s education in their home country. ... Such analysis is misleading because it confuses differences in style of expression with a lack of academic rigour."': '“听到将这种修辞风格的问题归咎于学生在母国接受的教育存在假想的缺陷，尤其令人愤怒。……这种分析具有误导性，因为它将表达风格的差异与缺乏学术严谨性混为一谈。”\n> ("It is particularly infuriating to hear problems with such rhetorical styles attributed to imagined inadequacies in the student\'s education in their home country. ... Such analysis is misleading because it confuses differences in style of expression with a lack of academic rigour.")',
    '"T@here is a notable tendency in the applied linguistics literature to report the perceptions and reactions of Western instructors which, rather than being interrogated for ethnocentric bias and stereotyping, are validated by recourse to a Confucian heritage explanation which appears plausible rather than being empirically established."': '“在应用语言学文献中存在一种显著的倾向：报告西方教师的看法和反应，而没有质疑其民族中心主义偏见和刻板印象，反而是通过诉诸一种看似合理而非基于实证确立的儒家传统解释来证实它们。”\n> ("There is a notable tendency in the applied linguistics literature to report the perceptions and reactions of Western instructors which, rather than being interrogated for ethnocentric bias and stereotyping, are validated by recourse to a Confucian heritage explanation which appears plausible rather than being empirically established.")', # Fixed T@here typo in source
    '"Good teaching and learning are \'the common treasures of humanity.\'"': '“良好的教与学是‘人类共同的财富’。”\n> ("Good teaching and learning are \'the common treasures of humanity.\'")',

    # Argument_Gilison_Wilson_2025_UniversityStartups.md
    '"In fact, the odds are stacked against the [[University Spin-Out|university-based startup]] so much so that the successful ones are the true \'Uni-corns.\'"': '“事实上，各种不利因素对[[University Spin-Out|大学初创企业]]非常不利，以至于那些成功的企业才算是真正的‘独角兽’。”\n> ("In fact, the odds are stacked against the [[University Spin-Out|university-based startup]] so much so that the successful ones are the true \'Uni-corns.\'")',
    '"It was like [[Tracking]] a Yeti, where people have heard they exist but never witnessed one firsthand in the wild."': '“这就像在[[Tracking|追踪]]雪人，人们听说过它们的存在，但从未在野外亲眼目睹过。”\n> ("It was like [[Tracking]] a Yeti, where people have heard they exist but never witnessed one firsthand in the wild.")',
    '"The sure way to kill truly disruptive innovation is to have industry directly initiate startup and spin-out creation at universities."': '“扼杀真正颠覆性创新的必然方法，就是让产业界直接在大学发起初创企业和衍生企业的创建。”\n> ("The sure way to kill truly disruptive innovation is to have industry directly initiate startup and spin-out creation at universities.")',

    # Argument_LernerLam_2025_TransdisciplinaryExecutiveEd.md
    '"The evolution of complex, transdisciplinary thinking in response to these challenges—what some have characterized as advanced system thinking or convergence research—is not just confined to university campuses."': '“作为对这些挑战的回应，复杂的跨学科思维的演变——一些人将其描述为高级系统思维或融合研究——并不仅仅局限于大学校园。”\n> ("The evolution of complex, transdisciplinary thinking in response to these challenges—what some have characterized as advanced system thinking or convergence research—is not just confined to university campuses.")',
    '"Particularly for subject matter underlain by highly technical research in science and engineering, core scientific and engineering faculty might not be able to address the policy dynamics inherent in the grander challenge."': '“特别是对于以科学和工程领域高度技术性研究为基础的主题，核心科学和工程教员可能无法解决更宏大挑战中固有的政策动态问题。”\n> ("Particularly for subject matter underlain by highly technical research in science and engineering, core scientific and engineering faculty might not be able to address the policy dynamics inherent in the grander challenge.")',
    '"Columbia calls this its \'[[Fourth Generation University|Fourth Purpose]],\' a responsibility added to the traditional functions of scholarship, teaching and disciplinary service."': '“哥伦比亚大学将此称为其‘[[Fourth Generation University|第四使命]]’，这是在传统的学术、教学和学科服务功能之外增加的一项责任。”\n> ("Columbia calls this its \'[[Fourth Generation University|Fourth Purpose]],\' a responsibility added to the traditional functions of scholarship, teaching and disciplinary service.")',

    # Argument_Narayan_Spohrer_2025_Metrics.md
    '"It involves stakeholders with different outlooks and impact expectations. Moreover, the multidimensional nature of the impacts themselves means they are tangible and intangible, short- and long-term, direct and indirect, positive and negative, making their measurement process very complex."': '“它涉及具有不同观点和影响预期的利益相关者。此外，影响本身的多维性质意味着它们是有形和无形的、短期和长期的、直接和间接的、积极和消极的，这使得它们的衡量过程非常复杂。”\n> ("It involves stakeholders with different outlooks and impact expectations. Moreover, the multidimensional nature of the impacts themselves means they are tangible and intangible, short- and long-term, direct and indirect, positive and negative, making their measurement process very complex.")',
    '"The key to culture is trust based on history of UI relationship as well as the collaborative practice of clearly defining problems of mutual strong interest that can only be solved working together to achieve win-win outcomes. Failures are mutual learning experiences."': '“文化的关键在于建立在产学（UI）关系历史基础上的信任，以及明确界定只有通过合作实现双赢才能解决的共同强烈利益问题的合作实践。失败是共同学习的经验。”\n> ("The key to culture is trust based on history of UI relationship as well as the collaborative practice of clearly defining problems of mutual strong interest that can only be solved working together to achieve win-win outcomes. Failures are mutual learning experiences.")',
    '"AI will not replace service providers (e.g., industry researchers, academic faculty, etc.), but trusted service providers who use AI effectively and ethically will replace those who don\'t."': '“人工智能（AI）不会取代服务提供商（如产业研究人员、大学教员等），但是有效且符合伦理地使用 AI 的值得信赖的服务提供商，将取代那些不这么做的人。”\n> ("AI will not replace service providers (e.g., industry researchers, academic faculty, etc.), but trusted service providers who use AI effectively and ethically will replace those who don\'t.")',
    '"Success breeds success. Metrics associated with increasing flows of talent, publicity, publications and commercial offerings that highlight the new knowledge co-created are the outcomes that matter most in re-inventing a culture of [[University-Industry Collaboration|UI collaboration]] generation after generation."': '“成功孕育成功。与人才流动、宣传、出版物和商业产品的增加相关的指标突出了共同创造的新知识，这些是代代相传地重塑[[University-Industry Collaboration|产学合作]]文化中最关键的成果。”\n> ("Success breeds success. Metrics associated with increasing flows of talent, publicity, publications and commercial offerings that highlight the new knowledge co-created are the outcomes that matter most in re-inventing a culture of [[University-Industry Collaboration|UI collaboration]] generation after generation.")',
    '"Every change in business conditions and focus requires adjusting 6 R investment options and recalibrating metrics, incentives, rewards, and culture to fit the times."': '“商业条件和重点的每一次变化，都需要调整6 R投资选项，并重新校准指标、激励、奖励和文化以适应时代。”\n> ("Every change in business conditions and focus requires adjusting 6 R investment options and recalibrating metrics, incentives, rewards, and culture to fit the times.")',

    # Argument_Parreira do Amaral_2022_geopolitics-knowledge.md
    '"The chapter argues that higher education, in this [[Tracking|setting]], is part of a New [[Geopolitics of Knowledge]] that refers to the integration of higher education in the imaginations and calculations of different actors aiming at asserting and/or improving their positions in the global [[Knowledge-Based Economy]]."': '“本章认为，在这种[[Tracking|背景]]下，高等教育是新[[Geopolitics of Knowledge|知识地缘政治]]的一部分，指的是将高等教育纳入不同行动者的想象和计算中，旨在主张和/或改善他们在全球[[Knowledge-Based Economy|知识经济]]中的地位。”\n> ("The chapter argues that higher education, in this [[Tracking|setting]], is part of a New [[Geopolitics of Knowledge]] that refers to the integration of higher education in the imaginations and calculations of different actors aiming at asserting and/or improving their positions in the global [[Knowledge-Based Economy]].")',

    # Argument_Zapp_2022_Springer.md
    '"Universities have entered the global governance landscape by strategically positioning themselves as global knowledge actors."': '“大学通过战略性地将自身定位为全球知识行动者，已经进入了全球治理的图景。”\n> ("Universities have entered the global governance landscape by strategically positioning themselves as global knowledge actors.")',
    '"With university knowledge becoming an important resource and asset in the global economy, the inter-university race for reputation, revenues, and researchers is oddly transposed to an unlevelled global geopolitical playing [[Champ|field]]."': '“随着大学知识成为全球经济中的重要资源和资产，大学间为声誉、收入和研究人员展开的竞争，被奇特地置换到了一个不平坦的全球地缘政治竞技[[Champ|场]]上。”\n> ("With university knowledge becoming an important resource and asset in the global economy, the inter-university race for reputation, revenues, and researchers is oddly transposed to an unlevelled global geopolitical playing [[Champ|field]].")',
    '"If universities want to preserve their unique status as independent knowledge arbiters in global governance and even reshuffle power structures traditionally skewed towards politics and markets, they have to make sure to not only follow the global agenda but begin to actively shape it."': '“如果大学想要在全球治理中保持其作为独立知识仲裁者的独特地位，甚至重组传统上偏向政治和市场的权力结构，它们必须确保不仅是追随全球议程，而且要开始积极地塑造它。”\n> ("If universities want to preserve their unique status as independent knowledge arbiters in global governance and even reshuffle power structures traditionally skewed towards politics and markets, they have to make sure to not only follow the global agenda but begin to actively shape it.")',

    # Argument_Partaken_2022_Springer.md
    '"Instead of such a static state of knowledge, the inquiry into geopolitics should pay more attention to the phenomena of \'[[Knowledge Transfer|knowledge in motion]]\' such as transfer, dissemination, pedagogy, indoctrination, theft, espionage, surveillance and censorship."': '“与其关注知识的这种静态，对地缘政治的探究应该更多地关注‘[[Knowledge Transfer|运动中的知识]]’现象，如转移、传播、教学法、灌输、窃取、间谍活动、监视和审查。”\n> ("Instead of such a static state of knowledge, the inquiry into geopolitics should pay more attention to the phenomena of \'[[Knowledge Transfer|knowledge in motion]]\' such as transfer, dissemination, pedagogy, indoctrination, theft, espionage, surveillance and censorship.")',
    '"The sovereignty lieth hid in knowledge"': '“主权隐藏在知识之中”\n> ("The sovereignty lieth hid in knowledge")',
}

def translate_quotes(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        
        # We also need to handle the typo case dynamically
        new_content = new_content.replace('T@here is', 'There is')
        
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
