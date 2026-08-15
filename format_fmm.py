import re

with open("wiki/methods/quantitative/Factor Mixture Modeling.md", "r") as f:
    content = f.read()

# 1. Remove the previously added `> [!info] 数学与统计原理` block
info_block = """> [!info] 数学与统计原理
> FMM 的核心在于它同时包含了**连续潜变量**（Continuous Latent Variables，即因子）和**类别潜变量**（Categorical Latent Variables，即潜在类别）：
> 1. **验证性因子分析（CFA）层面**：建立外显观测指标 $y$ 与连续潜因子 $\eta$ 之间的线性回归方程：$y_{i} = \\nu + \\lambda \\eta_{i} + \\epsilon_{i}$，用来吸收测量误差、提取有效的维度构建。
> 2. **潜在剖面分析（LPA）层面**：传统的 LPA 是直接对杂乱的外显题目进行聚类。而 FMM 则更进一步，假设人群中存在 $K$ 个未知的异质性类别（群组 $k=1, 2, ..., K$）。
> 3. **模型融合**：FMM 允许 CFA 的参数（如截距 $\\nu$、因子载荷 $\\lambda$、因子均值 $\\alpha$、协方差等）在不同的 $K$ 类别中自由变化（即 $y_{ik} = \\nu_{k} + \\lambda_{k} \\eta_{ik} + \\epsilon_{ik}$）。这使得研究者不仅能确保问卷结构的信效度，还能通过计算联合概率分布提取出“在潜因子得分上表现出特定模式（如某维高、某维低）”的典型特征人群。"""
content = content.replace(info_block + "\n\n", "")

# 2. Insert the formal `> [!formula-step]` block under `## 研究程序` right after `> [!method-stack]`
formula_block = """> [!formula-step] 公式步骤　FMM 基础测量方程
> $$ y_{ik} = \\nu_{k} + \\lambda_{k} \\eta_{ik} + \\epsilon_{ik} $$
>
> **这个公式在做什么** 将针对潜因子的连续维度测量（CFA）与针对人群分类的潜在类别分析（LPA）融合，构建异质类别 $K$ 下观测变量与潜因子的回归方程。
>
> **符号说明** $y_{ik}$：个体 $i$ 在属于类别 $k$ 时的观测变量得分；$\\nu_{k}$：类别 $k$ 的截距；$\\lambda_{k}$：类别 $k$ 的因子载荷；$\\eta_{ik}$：个体 $i$ 的连续潜在因子（如具体的心理测验得分）；$\\epsilon_{ik}$：特定类别下的测量残差。
>
> **数学直觉** 传统的 CFA 只有一条全局方程，假定所有人同属一个同质群体；而传统的 LPA 只能基于含有测量误差的原始观测分（$y$）进行聚类。FMM 把两者的优势拼在了一起：它既用潜变量 $\\eta$ 吸收了测量误差，又允许 CFA 的各个参数在 $K$ 个未知的异质性类别中**自由变化**。算法通过最大似然估计，从数据中“盲抽”出在各个潜因子上表现出特定模式（如“高-低-中”）的典型特征亚群。
>
> **结果怎么读** 跑完模型后，主要看提取出的 $K$ 个类别的**联合轮廓图（Profile）**。如果设定 $K=6$ 的模型在信息准则（BIC、SABIC 越小越好）上拟合最优，说明样本整体在数学上可以稳定划分为六类截然不同的人群。
>
> **注意事项** 模型对起点的初值极为敏感，常面临局部极值和不收敛问题（尤其是强制进行强等值检验时）。因此算法提取出的类别数目必须结合领域理论进行实质性解释，否则容易导致过度拟合。"""

# Find insertion point
method_stack_pattern = r"(> \[!method-stack\] 数据、变量与模型.*?> - \*\*诊断与检验\*\* LMR 检验、模型收敛性及参数异常判定（如 Heywood case）。\n)"
content = re.sub(method_stack_pattern, r"\1\n" + formula_block + r"\n", content, flags=re.DOTALL)

with open("wiki/methods/quantitative/Factor Mixture Modeling.md", "w") as f:
    f.write(content)

print("Formatted successfully.")
