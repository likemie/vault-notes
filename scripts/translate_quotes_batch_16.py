import os

replacements = {
    # Argument_Bergeron_2017_MJE.md
    '"When taking the necessary in-depth look at [[Visible Learning]] with the eye of an expert, we find not a mighty castle but a fragile house of cards that quickly falls apart."': '“当以专家的眼光对[[Visible Learning|可见的学习]]进行必要的深入审视时，我们发现的不是一座坚固的城堡，而是一个迅速崩塌的脆弱纸牌屋。”\n> ("When taking the necessary in-depth look at [[Visible Learning]] with the eye of an expert, we find not a mighty castle but a fragile house of cards that quickly falls apart.")',
    '"To believe [[John Hattie|Hattie]] is to have a blind spot in one\'s critical thinking when assessing scientific rigor. To promote his work is to unfortunately fall into the promotion of pseudoscience. Finally, to persist in defending Hattie after becoming aware of the serious critique of his methodology constitutes willful blindness."': '“相信[[John Hattie|哈蒂]]（Hattie）意味着在评估科学严谨性时存在批判性思维的盲点。推崇他的工作不幸地陷入了对伪科学的宣传。最后，在意识到对其方法论的严肃批评后仍坚持为哈蒂辩护，则构成了蓄意的盲目。”\n> ("To believe [[John Hattie|Hattie]] is to have a blind spot in one\'s critical thinking when assessing scientific rigor. To promote his work is to unfortunately fall into the promotion of pseudoscience. Finally, to persist in defending Hattie after becoming aware of the serious critique of his methodology constitutes willful blindness.")',
    '"Hattie\'s comparisons are arbitrary and he is completely unaware of it."': '“哈蒂的比较是武断的，而他对此完全没有意识到。”\n> ("Hattie\'s comparisons are arbitrary and he is completely unaware of it.")',
    '"Basically, Hattie computes averages that do not make any sense."': '“基本上，哈蒂计算的平均值没有任何意义。”\n> ("Basically, Hattie computes averages that do not make any sense.")',
    '"It is clear that John Hattie and his team have neither the knowledge nor the competencies required to conduct valid statistical analyses. No one should replicate this methodology because we must never accept pseudoscience."': '“显而易见，约翰·哈蒂及其团队既不具备也不拥有进行有效统计分析所需的知识或能力。不应有人复制这种方法论，因为我们绝不能接受伪科学。”\n> ("It is clear that John Hattie and his team have neither the knowledge nor the competencies required to conduct valid statistical analyses. No one should replicate this methodology because we must never accept pseudoscience.")',

    # Argument_Blass_2020_JESP.md
    '"Would you want a surgeon looking at books from 1990 to learn about the use of robotics in surgery? No! Would you want an oncologist to look up the latest cancer treatments from the 1980\'s? No! So why are you allowing teaching outcomes from this time to influence what you are doing today in the classroom?"': '“你会希望一位外科医生查阅 1990 年的书籍来学习如何在手术中使用机器人吗？不！你会希望一位肿瘤科医生查找 1980 年代的最新癌症疗法吗？不！那么，你为什么要允许那个时代的教学结果影响你今天在课堂上的所作所为呢？”\n> ("Would you want a surgeon looking at books from 1990 to learn about the use of robotics in surgery? No! Would you want an oncologist to look up the latest cancer treatments from the 1980\'s? No! So why are you allowing teaching outcomes from this time to influence what you are doing today in the classroom?")',
    '"Australia has lost its way in education and [[John Hattie|Hattie]] is the fallback that is used to justify this position. But I doubt this was Hattie\'s intent."': '“澳大利亚在教育上迷失了方向，而[[John Hattie|哈蒂]]（Hattie）成为了被用来证明这一立场正当性的退路。但我怀疑这是否是哈蒂的本意。”\n> ("Australia has lost its way in education and [[John Hattie|Hattie]] is the fallback that is used to justify this position. But I doubt this was Hattie\'s intent.")',
    '"Being the subject matter expert is no longer the role of the teacher; teaching passion for a subject and learning is."': '“成为学科专家不再是教师的角色；教导对某一学科的热情以及如何学习才是。”\n> ("Being the subject matter expert is no longer the role of the teacher; teaching passion for a subject and learning is.")',

    # Argument_Schulze-Cleven_2017_HighEduc.md
    '"Policymakers\' discursive tropes—from the needs of dynamic \'knowledge economies\' to the benefits of \'excellence\'—tend to distract from the distributional conflicts and power dynamics in the sector."': '“政策制定者的话语修辞——从动态‘知识经济’的需求到‘卓越’的好处——往往会转移人们对该部门内分配冲突和权力动态的注意力。”\n> ("Policymakers\' discursive tropes—from the needs of dynamic \'knowledge economies\' to the benefits of \'excellence\'—tend to distract from the distributional conflicts and power dynamics in the sector.")',
    '"Money is not the only \'currency\' in scientific and educational fields, since competition among academics also revolves around \'symbolic goods\' (Bourdieu, 1984), like prestige, recognition, or distinction."': '“金钱并不是科学和教育领域的唯一‘货币’，因为学术界之间的竞争也围绕着‘符号商品’（Bourdieu, 1984）展开，如声望、认可或区分（distinction）。”\n> ("Money is not the only \'currency\' in scientific and educational fields, since competition among academics also revolves around \'symbolic goods\' (Bourdieu, 1984), like prestige, recognition, or distinction.")',
    '"The ongoing re-structuring of academic relations of dependence and loyalty (as portrayed in Bourdieu, 1984) appears to not only produce free-market dynamics but also to give rise to neo-feudal systems of power relations."': '“正在进行的对学术依赖与忠诚关系的重组（如 Bourdieu 1984 年所描述的那样），似乎不仅产生了自由市场动态，而且还导致了新封建主义（neo-feudal）权力关系的产生。”\n> ("The ongoing re-structuring of academic relations of dependence and loyalty (as portrayed in Bourdieu, 1984) appears to not only produce free-market dynamics but also to give rise to neo-feudal systems of power relations.")',
    '"The new political economy of higher education is not the result of anonymous, unstoppable market forces but rather of political decisions and social practices, whose rules are not set in stone."': '“高等教育的新政治经济学不是匿名的、不可阻挡的市场力量的结果，而是政治决策和社会实践的结果，其规则并非一成不变。”\n> ("The new political economy of higher education is not the result of anonymous, unstoppable market forces but rather of political decisions and social practices, whose rules are not set in stone.")',
    '"Distributional conflicts in higher education extend to the way knowledge is produced and recognized in the higher education sector and in society more broadly. In turn, it is the very nature of socially accepted and legitimate knowledge that is at [[Robert E. Stake|Stake]] in academic capitalism. The old question of the relationship between knowledge, power, and money therefore remains central to the new political economy of higher education."': '“高等教育中的分配冲突延伸到了高等教育部门乃至更广泛社会中知识的生产和认可方式。反过来，在学术资本主义中，社会接受且合法的知识的本质本身也处于风险（at stake）之中。因此，关于知识、权力和金钱之间关系的老问题仍然是高等教育新政治经济学的核心。”\n> ("Distributional conflicts in higher education extend to the way knowledge is produced and recognized in the higher education sector and in society more broadly. In turn, it is the very nature of socially accepted and legitimate knowledge that is at [[Robert E. Stake|Stake]] in academic capitalism. The old question of the relationship between knowledge, power, and money therefore remains central to the new political economy of higher education.")',
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
