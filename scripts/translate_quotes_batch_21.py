import os

replacements = {
    # Argument_Pampaka_2016_IJRME.md
    '"What works" 议程在教育中是否有效？通过引入 IJRME 特刊七篇论文，考察当前 [[Randomised Controlled Trials|RCT]] 主导的证据实践在方法论上的进展与局限，探讨是否需要从"什么有效"转向"什么在何处、如何、对谁有效"。': '“什么有效（What works）”议程在教育中是否有效？通过引入 IJRME 特刊七篇论文，考察当前[[Randomised Controlled Trials|RCT]]主导的证据实践在方法论上的进展与局限，探讨是否需要从“什么有效”转向“什么在何处、如何、对谁有效”。',

    # Argument_Sarbiewska_2019_JSR.md
    '"VL 属于[[Radical Constructivism|激进建构主义]]范式，因此[[Constructivist Paradigm|建构主义]]的问题与 Hattie 的教学概念直接相关，这导致教学本质的双重崩溃"': '“VL（可见的学习）属于[[Radical Constructivism|激进建构主义]]范式，因此[[Constructivist Paradigm|建构主义]]的问题与哈蒂（Hattie）的教学概念直接相关，这导致了教学本质的双重崩溃。”\n> ("VL belongs to the paradigm of radical constructivism, and therefore the problems of constructivism are directly related to Hattie’s concept of teaching, which leads to a double collapse of the essence of teaching.")',

    # Argument_Møller_2017_EERJ.md
    '"Education is and always will be a contested [[Champ|field]]."': '“教育现在是、而且永远将是一个充满争议的[[Champ|场域]]。”\n> ("Education is and always will be a contested [[Champ|field]].")',
    '"Success requires that we ask: success in or for what, success for whom, who benefits, and success under what conditions?"': '“成功要求我们追问：在什么方面或为了什么的成功，为谁而成功，谁获益，以及在什么条件下成功？”\n> ("Success requires that we ask: success in or for what, success for whom, who benefits, and success under what conditions?")',
    '"What counts as evidence should not be separated from deeper philosophical questions, because education is essentially a moral enterprise."': '“什么算作证据，不应与更深层的哲学问题相脱离，因为教育本质上是一项道德事业。”\n> ("What counts as evidence should not be separated from deeper philosophical questions, because education is essentially a moral enterprise.")'
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
