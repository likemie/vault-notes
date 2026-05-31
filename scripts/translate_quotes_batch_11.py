import os

replacements = {
    # Argument_Eacott_2019_IJLE.md
    '"what we are more likely to experience, both as consumers and generators of research is \'[[Parallel Monologues]]\'"': '“作为研究的消费者和生产者，我们更有可能体验到的是‘[[Parallel Monologues|平行独白]]’”\n> ("what we are more likely to experience, both as consumers and generators of research is \'[[Parallel Monologues]]\'")',
    '"It is not about simply producing a counter argument, but engaging with the ideas of another and where necessary refuting them. Not imposing one\'s view of the world on another, but engage on their terms – testing out claims for robustness and internal coherence and not alignment with one\'s own normative position."': '“这不仅仅是提出一个反驳，而是与他人的观点交锋，并在必要时驳斥它们。不是将自己对世界的看法强加于人，而是按照他们的术语（逻辑）参与其中——检验主张的稳健性和内部连贯性，而不是检验其是否与自己的规范性立场相一致。”\n> ("It is not about simply producing a counter argument, but engaging with the ideas of another and where necessary refuting them. Not imposing one\'s view of the world on another, but engage on their terms – testing out claims for robustness and internal coherence and not alignment with one\'s own normative position.")',
    '"what I have offered is a call or invitation to others to engage differently in our work. It is not a call for knowledge centrism and/or one way to be a scholar, but an in-principle agreement that our work as scholars be recognizable for its underlying generative logic of argument and refutation."': '“我所提供的是一种呼吁或邀请，邀请其他人以不同的方式参与我们的工作。这不是在呼吁知识中心主义和/或成为学者的唯一方式，而是一种原则上的同意：即我们作为学者的工作，应当因其潜在的论证与反驳的生成逻辑而被认可。”\n> ("what I have offered is a call or invitation to others to engage differently in our work. It is not a call for knowledge centrism and/or one way to be a scholar, but an in-principle agreement that our work as scholars be recognizable for its underlying generative logic of argument and refutation.")',

    # Argument_Biesta_2010_SPE.md
    '"The important question, therefore, is not whether or not there should be a role for evidence in professional action, but what kind of role it should play."': '“因此，重要的问题不在于证据在专业行动中是否应该发挥作用，而在于它应该发挥什么样的作用。”\n> ("The important question, therefore, is not whether or not there should be a role for evidence in professional action, but what kind of role it should play.")',
    '"A [[Transactional Epistemology]] allows us to make warranted assertions about what has worked in the past but not about what will work in the future."': '“一种[[Transactional Epistemology|交互性认识论]]允许我们对过去什么曾经有效做出有保证的断言，但不能对未来什么将会有效做出断言。”\n> ("A [[Transactional Epistemology]] allows us to make warranted assertions about what has worked in the past but not about what will work in the future.")',
    '"Much talk about \'what works\' operates on the assumption of a mechanistic ontology that is actually the exception, not the norm in the domain of human interaction."': '“许多关于‘什么有效’的谈论都是在机械论本体论的假设下运作的，而这在人类互动领域实际上是个例外，并非寻常状态。”\n> ("Much talk about \'what works\' operates on the assumption of a mechanistic ontology that is actually the exception, not the norm in the domain of human interaction.")',
    '"No one has ever seen a laboratory fact move outside unless the lab is first brought to bear on an \'outside\' situation and that situation is transformed so that it fits laboratory prescriptions."': '“从来没有人见过实验室事实走到外面，除非首先把实验室运用到‘外部’情境中，并将该情境进行转化，使其符合实验室的规定。”\n> ("No one has ever seen a laboratory fact move outside unless the lab is first brought to bear on an \'outside\' situation and that situation is transformed so that it fits laboratory prescriptions.")',
    '"Questions about \'what works\' — that is questions about the effectiveness of educational actions — are always secondary to questions of purpose."': '“关于‘什么有效’的问题——也就是关于教育行动有效性的问题——总是次于关于目的的问题。”\n> ("Questions about \'what works\' — that is questions about the effectiveness of educational actions — are always secondary to questions of purpose.")',
    '"Taken together these deficits not only raise some important questions about the very idea of evidence-based practice but also highlight the role of normativity, power and values."': '“总而言之，这些缺陷不仅对循证实践的理念本身提出了一些重要问题，而且还凸显了规范性、权力和价值观的作用。”\n> ("Taken together these deficits not only raise some important questions about the very idea of evidence-based practice but also highlight the role of normativity, power and values.")',
    '"Educational systems are generally open systems... the connections between intervention and effect are non-linear and, at most, probabilistic."': '“教育系统通常是开放系统……干预与效果之间的联系是非线性的，并且最多只是概率性的。”\n> ("Educational systems are generally open systems... the connections between intervention and effect are non-linear and, at most, probabilistic.")',
    '"Without normative orientations, without decisions about what is educationally desirable, without an articulation of the telos of educational practices, these practices simply do not exist — or at least they do not exist as educational practices."': '“如果没有规范性的导向，没有关于什么是教育上可取之物的决策，没有对教育实践最终目的（telos）的阐明，这些实践根本就不存在——或者至少它们不会作为教育实践而存在。”\n> ("Without normative orientations, without decisions about what is educationally desirable, without an articulation of the telos of educational practices, these practices simply do not exist — or at least they do not exist as educational practices.")',
    '"If evidence were the only base for educational practice, educational practice would be entirely without direction. This is one reason why, in education, values come first."': '“如果证据是教育实践的唯一基础，教育实践将完全失去方向。这就是为什么在教育中，价值观必须放在首位的一个原因。”\n> ("If evidence were the only base for educational practice, educational practice would be entirely without direction. This is one reason why, in education, values come first.")',

    # Argument_Schulte_2009_EncuentrosEducacion.md
    '"The enthusiasm or criticism towards John Dewey was not only about Deweyan ideas. At least below the surface, it was also about Chinese concepts and ideologies that were associated with his philosophy and educational thought."': '“对约翰·杜威（John Dewey）的热情或批评，不仅仅是关于杜威的思想。至少在表面之下，它也关乎那些与他的哲学和教育思想联系在一起的中国本土概念和意识形态。”\n> ("The enthusiasm or criticism towards John Dewey was not only about Deweyan ideas. At least below the surface, it was also about Chinese concepts and ideologies that were associated with his philosophy and educational thought.")',
    '"Dewey did not just represent conceptual imaginaries. Through his role as teacher and mentor of a large number of Chinese students, through his personal and prolonged visit to the country, and, later, through his personal involvement in the Trotsky trial, he was not only the embodiment of more or less [[Abstract]] ideas and theories, but a personality who could arouse admiration, distrust, or even hatred among Chinese intellectuals."': '“杜威并不仅仅代表概念上的想象。通过他作为大量中国学生的老师和导师的角色，通过他亲自且长期对该国的访问，以及后来通过他个人对托洛茨基审判的参与，他不仅是或多或少[[Abstract|抽象]]思想和理论的化身，更是一个能够在中国知识分子中唤起钦佩、不信任甚至仇恨的人格实体。”\n> ("Dewey did not just represent conceptual imaginaries. Through his role as teacher and mentor of a large number of Chinese students, through his personal and prolonged visit to the country, and, later, through his personal involvement in the Trotsky trial, he was not only the embodiment of more or less [[Abstract]] ideas and theories, but a personality who could arouse admiration, distrust, or even hatred among Chinese intellectuals.")',
    '"John Dewey — or rather Duwei — has indeed become both \'red\' and \'expert.\'"': '“约翰·杜威——或者更确切地说是‘杜威（Duwei）’——确实已经变得既‘红’又‘专’了。”\n> ("John Dewey — or rather Duwei — has indeed become both \'red\' and \'expert.\'")'
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
