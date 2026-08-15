import re

with open("wiki/instruments/questionnaire/Epistemic and Ontological Cognition Questionnaire.md", "r") as f:
    content = f.read()

translations = {
    "In [math/history], the truth means different things to different people.": "In [math/history], the truth means different things to different people.<br>**在[数学/历史]中，真相对不同的人意味着不同的事物。**",
    "To know [math/history] well, you need to memorize what you are taught.": "To know [math/history] well, you need to memorize what you are taught.<br>**要学好[数学/历史]，你需要记住老师教给你的东西。**",
    "In [math/history], what is a fact today will be a fact tomorrow.": "In [math/history], what is a fact today will be a fact tomorrow.<br>**在[数学/历史]中，今天的事实到了明天依然是事实。**",
    "[Mathematicians'/Historians'] knowledge of the facts about math does not change.": "[Mathematicians'/Historians'] knowledge of the facts about [math/history] does not change.<br>**[数学家/历史学家]对于[数学/历史]事实的认识是不会改变的。**",
    "[Math/History] is so complex that humans will never really understand it.": "[Math/History] is so complex that humans will never really understand it.<br>**[数学/历史]太过复杂，人类永远无法真正理解它。**",
    "If a [mathematician/historian] says something is a fact, I believe it.": "If a [mathematician/historian] says something is a fact, I believe it.<br>**如果[数学家/历史学家]说某件事是事实，我就会相信。**",
    "Things written in [math/history] textbooks are true.": "Things written in [math/history] textbooks are true.<br>**写在[数学/历史]教科书上的内容都是真实的。**",
    "I believe everything I learn in [math/history] class.": "I believe everything I learn in [math/history] class.<br>**我相信在[数学/历史]课上学到的所有东西。**",
    "If a [math/history] teacher says something is a fact, I believe it.": "If a [math/history] teacher says something is a fact, I believe it.<br>**如果[数学/历史]老师说某件事是事实，我就会相信。**",
    "In [math/history], everyone's knowledge can be different because there is no one absolutely right answer.": "In [math/history], everyone's knowledge can be different because there is no one absolutely right answer.<br>**在[数学/历史]中，每个人的认识都可能不同，因为不存在唯一绝对正确的答案。**",
    "In [math/history], if you believe something is a fact, no one can prove to you that you are wrong.": "In [math/history], if you believe something is a fact, no one can prove to you that you are wrong.<br>**在[数学/历史]中，如果你相信某件事是事实，没有人能证明你是错的。**",
    "In [math/history], what's a fact depends upon a person's point of view.": "In [math/history], what's a fact depends upon a person's point of view.<br>**在[数学/历史]中，什么是事实取决于个人的观点。**",
    "[Mathematical/Historical] knowledge is all factual and there are no opinions.": "[Mathematical/Historical] knowledge is all factual and there are no opinions.<br>**[数学/历史]知识全都是事实性的，不存在主观观点。**"
}

for eng, trans in translations.items():
    content = content.replace(eng, trans)

with open("wiki/instruments/questionnaire/Epistemic and Ontological Cognition Questionnaire.md", "w") as f:
    f.write(content)

print("Translation applied successfully.")
