import os

replacements = {
    # Argument_Lekhal_2015_Paideia.md
    '"Resultatene viser dermed at kjønn i seg selv ikke ser ut til å virke direkte inn på skolefaglige prestasjoner, men at kjønn påvirker prestasjonene indirekte i et samspill med andre variabler."': '“因此，结果表明，性别本身似乎并不直接影响学业成绩，而是性别在与其他变量的相互作用中，间接影响学业成绩。”\n> ("Resultatene viser dermed at kjønn i seg selv ikke ser ut til å virke direkte inn på skolefaglige prestasjoner, men at kjønn påvirker prestasjonene indirekte i et samspill med andre variabler.")',

    # Argument_Fredens_2015_Paideia.md
    '"Der er kort sagt brug for en præcisering af, hvordan vi bedst lærer noget. Så hvad er læring? Det har [[John Hattie]] og Gregory Yates et videnskabeligt bud på."': '“简言之，我们需要澄清如何最好地学习。那么什么是学习？[[John Hattie|约翰·哈蒂]]（John Hattie）和 Gregory Yates 对此有一个科学的答案。”\n> ("Der er kort sagt brug for en præcisering af, hvordan vi bedst lærer noget. Så hvad er læring? Det har [[John Hattie]] og Gregory Yates et videnskabeligt bud på.")',
    '"Gør skolen til en feedbackkultur."': '“使学校成为一种反馈文化。”\n> ("Gør skolen til en feedbackkultur.")',
    '"Det, der tilegnes let, glemmes let."': '“轻易获得的，轻易就会忘记。”\n> ("Det, der tilegnes let, glemmes let.")',
    '"En uddannelseskultur skal ikke fikses, men kultiveres; det fordrer et partnerskab mellem lærer og forskning."': '“一种教育文化不应是被修理的，而应是被培养的；这需要教师与研究之间的伙伴关系。”\n> ("En uddannelseskultur skal ikke fikses, men kultiveres; det fordrer et partnerskab mellem lærer og forskning.")',

    # Argument_Hattie_2015_Paideia.md
    '"Kend din virkning"': '“了解你的影响（Know thy impact）”\n> ("Kend din virkning")',
    '"Det er således en disposition til at ønske at kende sin virkning, der ligger i kernen af VL-modellen."': '“因此，渴望了解自己影响的这种倾向（disposition），正是可见的学习（VL）模型的核心所在。”\n> ("Det er således en disposition til at ønske at kende sin virkning, der ligger i kernen af VL-modellen.")',

    # Argument_Qvortrup_2015_Paideia.md
    '"All studies differ and the only interesting questions to ask about them concern how they vary across the factors we conceive as important."': '“所有研究各不相同，而关于它们唯一有趣的问题是，它们如何在被我们认为重要的那些因素上产生差异。”\n> ("All studies differ and the only interesting questions to ask about them concern how they vary across the factors we conceive as important.")',
    '"A limitation of many of the results in this book is that they are more related to the surface and deep knowing and less to conceptual understanding."': '“本书许多结果的一个局限性在于，它们更多地与表层和深层知识相关，而较少与概念理解相关。”\n> ("A limitation of many of the results in this book is that they are more related to the surface and deep knowing and less to conceptual understanding.")'
}

def translate_quotes(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        
        # dynamic cleanup for previously translated but slightly malformed ones if needed
        new_content = new_content.replace('（简言之，我们需要澄清如何最好地学习。那么什么是学习？John Hattie 和 Gregory Yates 对此有科学答案）', '')
        new_content = new_content.replace('（使学校成为反馈文化）', '')
        new_content = new_content.replace('（轻易获得的东西，轻易被遗忘）', '')
        new_content = new_content.replace('（教育文化不应被修理，而应被培养；这需要教师与研究之间的伙伴关系）', '')
        
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
