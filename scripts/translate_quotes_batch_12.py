import os

replacements = {
    # Argument_Ryabyy_2024_Maneto.md
    '"We do not ask your praise, when you reach home, nor fear your blame, if you will do one thing only, tell your people the facts and let them judge."': '“当你们回到家乡时，我们不奢求你们的赞美，也不惧怕你们的责备，只要你们做一件事，那就是告诉你们的人民事实，让他们自己去评判。”\n> ("We do not ask your praise, when you reach home, nor fear your blame, if you will do one thing only, tell your people the facts and let them judge.")',
    '"Your works, especially \'School and Society\' and \'The School and the Child\' have very much influenced the development of the Russian pedagogy and in the first years of revolution you were one of the most renowned writers."': '“您的著作，尤其是《学校与社会》和《学校与儿童》，极大地影响了俄罗斯教育学的发展，在革命的最初几年，您是最著名的作家之一。”\n> ("Your works, especially \'School and Society\' and \'The School and the Child\' have very much influenced the development of the Russian pedagogy and in the first years of revolution you were one of the most renowned writers.")',
    '"We must begin this great undertaking — the coming together of the more democratic nations of the world."': '“我们必须开始这项伟大的事业——世界上更民主国家的走到一起。”\n> ("We must begin this great undertaking — the coming together of the more democratic nations of the world.")',
    '"This American educators\' mission to Russia, then, is simply one more move in the Communist propaganda game engineered by those who have proved willing tools of the Communists in the past and with various non-Communists drawn in to hide the Communist machinery working underneath."': '“那么，这个美国教育家访问俄罗斯的代表团，仅仅是过去那些被证明是共产主义者顺从工具的人所策划的共产主义宣传游戏中的又一个举动，并拉拢了各种非共产主义者进来，以掩盖在底层运作的共产主义机器。”\n> ("This American educators\' mission to Russia, then, is simply one more move in the Communist propaganda game engineered by those who have proved willing tools of the Communists in the past and with various non-Communists drawn in to hide the Communist machinery working underneath.")',

    # Argument_Wadhwa_2024_RER.md
    '"identifying \'evidence-based\' interventions is still more of a policy aspiration than a reliable research practice."': '“识别‘基于证据的’干预措施仍然更多地是一种政策愿景，而不是一种可靠的研究实践。”\n> ("identifying \'evidence-based\' interventions is still more of a policy aspiration than a reliable research practice.")',
    '"evidence-based has limited practical [[Construct]] validity in the CH context."': '“‘基于证据（evidence-based）’在信息交换中心（CH）的背景下，其实际的[[Construct|构念]]效度是有限的。”\n> ("evidence-based has limited practical [[Construct]] validity in the CH context.")',

    # Argument_Håkansson_2015_Paideia.md
    '"Den tes jag har drivit har varit att vi kan se förskjutningar i riktning mot olika varianter av klassrumsnära strategier i skolutvecklingsarbetet."': '“我所推动的论点是，我们可以看到学校发展工作正朝着各种贴近课堂策略的变体方向发生转变。”\n> ("Den tes jag har drivit har varit att vi kan se förskjutningar i riktning mot olika varianter av klassrumsnära strategier i skolutvecklingsarbetet.")',
    '"Lärarna vittnar även om en ökad medvetenhet om aspekter i undervisningen ... och en stärkt tilltro till att prova nya saker i undervisningen."': '“教师们也证明了他们对教学各个方面的意识有所提高……并且对在教学中尝试新事物的信心也有所增强。”\n> ("Lärarna vittnar även om en ökad medvetenhet om aspekter i undervisningen ... och en stärkt tilltro till att prova nya saker i undervisningen.")',

    # Argument_Allerup_2015_Paideia.md
    '"Man har derfor ikke som ved [[PISA]]-rangordningen adgang til en erkendelse af, at to eller flere indsatser/lande ikke adskiller sig signifikant fra hinanden - selv om de numerisk set er forskellige."': '“因此，人们不能像在[[PISA]]排名中那样去认识到：两项或多项干预措施/国家之间并没有显著差异——即使它们在数值上是不同的。”\n> ("Man har derfor ikke som ved [[PISA]]-rangordningen adgang til en erkendelse af, at to eller flere indsatser/lande ikke adskiller sig signifikant fra hinanden - selv om de numerisk set er forskellige.")'
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
