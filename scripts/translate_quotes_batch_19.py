import os

replacements = {
    # Argument_Bainbridge_2022_ROE.md
    '"I want to establish a thread to run through the debate — that grammar schools are simply good schools and that we need good schools to flourish."': '“我想建立一条贯穿这场辩论的线索——即文法学校（grammar schools）仅仅是优秀的学校，而我们需要优秀的学校来蓬勃发展。”\n> ("I want to establish a thread to run through the debate — that grammar schools are simply good schools and that we need good schools to flourish.")',
    '"What has emerged... is a discourse that is constructive as it actively and persistently distorts the meaning of \'good\' — it is a sidestep into a world of fantasised goodness, while also away from an often-unspoken world of \'badness\'"': '“已经出现的是一种具有建构性的话语，因为它积极且持续地扭曲了‘优秀’的含义——这是一种向幻想中的‘优秀’世界的侧步避让（sidestep），同时也远离了一个经常不被提及的‘糟糕’世界。”\n> ("What has emerged... is a discourse that is constructive as it actively and persistently distorts the meaning of \'good\' — it is a sidestep into a world of fantasised goodness, while also away from an often-unspoken world of \'badness\'")',
    '"The \'good schools\' discourse is an [[Ofsted]]-derived evidenced position, which makes it all the more deceptive; it is a [[Moral Sidestep]] cloaked in the language of evidence."': '“‘优秀学校’的话语是一种源自[[Ofsted|教育标准局（Ofsted）]]的循证立场，这使其更具欺骗性；它是一个披着证据语言外衣的[[Moral Sidestep|道德侧步]]。”\n> ("The \'good schools\' discourse is an [[Ofsted]]-derived evidenced position, which makes it all the more deceptive; it is a [[Moral Sidestep]] cloaked in the language of evidence.")',
    '"It would appear that it is less easy to refute or sidestep certain evidence when it emerges from within Parliament."': '“看起来，当某些证据从议会内部出现时，驳斥或回避它们就不那么容易了。”\n> ("It would appear that it is less easy to refute or sidestep certain evidence when it emerges from within Parliament.")',
    '"Whereas it might be asking too much of our politicians to insist that they be aware of rigorous research methods, it is not too much to hold them to a high standard of ethics and to hold them to account when their demonstrated ethics fall short."': '“虽然坚持要求我们的政治家了解严谨的研究方法可能是要求过高，但要求他们遵守高标准的伦理准则，并在他们表现出的伦理水平不足时追究其责任，并不过分。”\n> ("Whereas it might be asking too much of our politicians to insist that they be aware of rigorous research methods, it is not too much to hold them to a high standard of ethics and to hold them to account when their demonstrated ethics fall short.")',

    # Argument_Peterson_2016_IJRME.md
    '"The key weakness of \'What Works\' is that it generates evidence relevant only to single either-or decisions."': '“‘什么有效（What Works）’的主要弱点在于，它产生的证据仅与单一的非此即彼的决策相关。”\n> ("The key weakness of \'What Works\' is that it generates evidence relevant only to single either-or decisions.")',
    '"In contrast, [[Improvement Science]] and other networked inquiry approaches are designed to fit with the daily context of teaching and learning, allowing for continuous small decisions based on [[Feedback]] and adaptation."': '“相比之下，[[Improvement Science|改进科学]]和其他网络化探究方法旨在适应教与学的日常情境，允许根据[[Feedback|反馈]]和调整做出持续的小型决策。”\n> ("In contrast, [[Improvement Science]] and other networked inquiry approaches are designed to fit with the daily context of teaching and learning, allowing for continuous small decisions based on [[Feedback]] and adaptation.")',
    '"The central advantage of designing trials around mechanisms is that it would allow for greater continuity between randomized evaluations and the \'learning sciences\'."': '“围绕机制设计试验的核心优势在于，它允许随机评估与‘学习科学’之间建立更大的连续性。”\n> ("The central advantage of designing trials around mechanisms is that it would allow for greater continuity between randomized evaluations and the \'learning sciences\'.")',
    '"The shared set of mechanisms would provide a means to learn from, and form a continuity with, the insights generated within improvement and inquiry networks, and within the learning sciences."': '“共享的一组机制将提供一种手段，从改进和探究网络以及学习科学中产生的见解中学习，并与之形成连续性。”\n> ("The shared set of mechanisms would provide a means to learn from, and form a continuity with, the insights generated within improvement and inquiry networks, and within the learning sciences.")',
    '"The learner becomes the focus as opposed to the protocols of the programme to be implemented."': '“学习者成为了焦点，而不是要实施的项目方案。”\n> ("The learner becomes the focus as opposed to the protocols of the programme to be implemented.")',

    # Argument_Håkansson_2015_Paideia.md
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
