import re

with open("wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2010_JEP.md", "r") as f:
    content = f.read()

# Fix Step 2 Warrant
step2_old = """> [!warrant]- 推理桥梁
> 领域特定模型拟合更优反驳了领域一般性假设，证实学生在面对劣构的学科领域与良构的学科领域时，其心智中调用的本体论和认识论信念属于相互独立的结构。"""

step2_new = """> [!warrant] 推理桥梁
> 如果认识论认知是“领域一般性”的（即放之四海而皆准），那么学生对所有学科的信念评分应该高度一致，从而在因子分析中合并为一个统一的潜变量。但数据表明，强行将历史和数学合并会导致模型拟合度断崖式下降。这在逻辑上直接推翻了领域一般性假设，证实学生在面对劣构领域（历史）与良构领域（数学）时，调用的是两套相互独立的信念评估体系。"""
content = content.replace(step2_old, step2_new)

# Fix Step 3 Warrant
step3_old = """> [!warrant]- 推理桥梁
> 聚类结果不仅映射出了特定的发展阶段组合，还呈现了历史认知更为发达的发展特征。将分散的信念维度整合成潜在的综合特征档案，能够更有效地描绘复杂的认知全貌。"""

step3_new = """> [!warrant] 推理桥梁
> 从零散的量表得分到经典的定性阶段，这一跨越是如何完成的？如果个体的信念仅仅是三个随机波动的独立维度，那么人群中就不应该出现高度集中的特定组合模式。然而，FMM 聚类成功在样本中找出了 6 个典型的特征群组（Profile），且这些群组的得分轮廓（如“三维皆强”或“一弱两强”）竟然与表 2 中由理论推导出的发展阶段完美重合。这在逻辑上完成了从“量化维度特征”到“定性发展阶段”的实证闭环。"""
content = content.replace(step3_old, step3_new)

# Fix Step 4 Warrant (Add missing warrant)
step4_old = """> [!chain-link] 证据到判断
> 多项逻辑回归结果表明，相较于处于现实主义阶段为主的初级群组，受教育年限的增加会显著提高进入高级认知阶段类群的几率。同时，数学或历史成绩较差的学生更容易被归入现实主义水平的初级类别中。"""

step4_new = """> [!chain-link] 证据到判断
> 多项逻辑回归结果表明，相较于处于现实主义阶段为主的初级群组，受教育年限的增加会显著提高进入高级认知阶段类群的几率。同时，数学或历史成绩较差的学生更容易被归入现实主义水平的初级类别中。
> 
> > [!warrant] 推理桥梁
> > 认识论阶段不仅是一个心理学模型，它必须具备现实的外部效度。回归分析补齐了论证的最后一环：随着受教育年限的增长，学生接触到的冲突观点增多，客观上推动了他们从幼稚的“现实主义”向高级的“理性主义”演化；反之，那些死抱着“知识只有唯一标准答案”的初级认知阶段学生，在应对复杂的学术任务时必然受挫（表现为 GPA 较差）。这就证明了该阶段模型对真实学业发展具有强大的解释力和预测力。"""
content = content.replace(step4_old, step4_new)

with open("wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2010_JEP.md", "w") as f:
    f.write(content)

print("Argument steps updated successfully.")
