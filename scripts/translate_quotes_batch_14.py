import os

replacements = {
    # Argument_Hansen_2015_Paideia.md
    '"Det vigtigste er, at den enkelte lærer forstår, at hans eller hendes rolle er at evaluere sin virkning."': '“最重要的是，每一位教师都要理解，他或她的角色是评估自己的影响。”\n> ("Det vigtigste er, at den enkelte lærer forstår, at hans eller hendes rolle er at evaluere sin virkning.")',
    '"Som grundlag for hele denne indsats er John Hatties arbejde med synlig læring et uomgængeligt udgangspunkt."': '“作为整个这项努力的基础，约翰·哈蒂关于可见的学习的工作是一个不可回避的起点。”\n> ("Som grundlag for hele denne indsats er John Hatties arbejde med synlig læring et uomgængeligt udgangspunkt.")',

    # Argument_Laursen_2015_Paideia.md
    '"Svaret bliver et \'ja\', og hvis man vil være forsigtig, kan man eventuelt tilføje et \'i det store og hele\'."': '“答案将是‘是’的，如果你想谨慎一点，也许可以加上‘总体而言’。”\n> ("Svaret bliver et \'ja\', og hvis man vil være forsigtig, kan man eventuelt tilføje et \'i det store og hele\'.")',
    '"Konteksten, forstået som elevernes sociale baggrund, betyder i høj grad noget. Men konteksten, forstået som den nationale kultur, ser ikke ud til at spille nogen større rolle..."': '“作为学生社会背景被理解的情境非常重要。但是，作为国家文化被理解的情境，似乎并没有发挥什么重要作用……”\n> ("Konteksten, forstået som elevernes sociale baggrund, betyder i høj grad noget. Men konteksten, forstået som den nationale kultur, ser ikke ud til at spille nogen større rolle...")',

    # Argument_Nordahl_2015_Paideia.md
    '"Det er hva læreren gjør og ikke gjør, som er mest avgjørende for elevenes læringsutbytte."': '“教师做什么以及不做什么，对学生的学习成果起着决定性的作用。”\n> ("Det er hva læreren gjør og ikke gjør, som er mest avgjørende for elevenes læringsutbytte.")',
    '"Praksis som bygger evidensbasert pedagogisk forskning, kan ikke garantere gode resultater, men den kan øke sannsynligheten."': '“建立在循证教育研究基础上的实践并不能保证好结果，但它可以增加其可能性。”\n> ("Praksis som bygger evidensbasert pedagogisk forskning, kan ikke garantere gode resultater, men den kan øke sannsynligheten.")',
    '"Det vi mangler, er ikke verdier, men kunnskap om hvordan verdiene kan realiseres i handling."': '“我们缺少的不是价值观，而是关于如何在行动中实现价值观的知识。”\n> ("Det vi mangler, er ikke verdier, men kunnskap om hvordan verdiene kan realiseres i handling.")',

    # Argument_Xu_2024_CE.md
    '"This study revealed a \'one country, two narratives\' view of China in the two regions\' Chinese history textbooks."': '“本研究揭示了两地中国历史教科书中关于中国的‘一国两叙事’视角。”\n> ("This study revealed a \'one country, two narratives\' view of China in the two regions\' Chinese history textbooks.")',
    '"Mainland China\'s textbooks constructed China as a nation by stressing its constitutive territory and ethnic inclusiveness, whereas Hong Kong\'s highlighted its constitutive ethnicity and changing territory, more frequently and directly narrated interethnic conflicts, and more explicitly promoted Han superiority."': '“中国大陆的教科书通过强调其构成性领土和种族包容性来将中国构建为一个国家，而香港的教科书则突出了其构成性种族和不断变化的领土，更频繁、更直接地叙述族际冲突，并更明确地宣扬汉族优越论。”\n> ("Mainland China\'s textbooks constructed China as a nation by stressing its constitutive territory and ethnic inclusiveness, whereas Hong Kong\'s highlighted its constitutive ethnicity and changing territory, more frequently and directly narrated interethnic conflicts, and more explicitly promoted Han superiority.")',
    '"The study proposes constructing the nation in history education as a contextualised and socio-political exercise of reinterpreting the past to reflect current contexts and needs."': '“该研究提出，应将历史教育中的国家构建视为一种情境化的、社会政治性的实践，即重新解释过去以反映当前的背景和需求。”\n> ("The study proposes constructing the nation in history education as a contextualised and socio-political exercise of reinterpreting the past to reflect current contexts and needs.")',
    '"The \'one country, two narratives\' view of China as a nation in the textbooks reveals a contextualised, socio-political exercise of nation construction, reflecting different interactions between government and textbook editors/writers in different contexts for different purposes."': '“教科书中将中国作为一个国家的‘一国两叙事’观点，揭示了一种情境化的、社会政治性的国家建构实践，反映了政府与教科书编辑/作者在不同情境下出于不同目的的不同互动。”\n> ("The \'one country, two narratives\' view of China as a nation in the textbooks reveals a contextualised, socio-political exercise of nation construction, reflecting different interactions between government and textbook editors/writers in different contexts for different purposes.")'
}

def translate_quotes(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        
        # Clean up existing partially translated ones with weird parenthesis
        new_content = new_content.replace('（回答是"是"，若谨慎一点，可加上"总体上"。）', '')
        new_content = new_content.replace('（作为学生社会背景的语境非常重要；但作为国家文化的语境似乎并不 发挥同样大的作用。）', '')
        
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
