import re

file_path = "wiki/arguments/journal-articles/Journal of Educational Psychology/Argument_Greene_2010_JEP.md"
with open(file_path, "r") as f:
    content = f.read()

# Replace Figure 1
fig1_mermaid = """> ```mermaid
> flowchart LR
>     A["完全领域一般性\n(Domain General)"] --- B["包含一般性与特殊性\n的双层中间模型"] --- C["完全领域特殊性\n(Domain Specific)"]
>     
>     style A fill:#f9f9f9,stroke:#333,stroke-width:2px
>     style B fill:#e6f7ff,stroke:#333,stroke-width:2px
>     style C fill:#f9f9f9,stroke:#333,stroke-width:2px
> ```"""
content = re.sub(
    r"> !\[\]\(https://img\.mylikemie\.icu/sources/Greene_2010_JEP/figures/Greene_2010_JEP_Fig1_.*?\.jpg\)",
    fig1_mermaid,
    content,
    flags=re.DOTALL
)

# Replace Figure 2
fig2_mermaid = """> ```mermaid
> flowchart TD
>     subgraph Math [数学领域测量 / Mathematics]
>         direction TB
>         M_SC(("Math SC\n简单与确定知识")) --> M_items1["Observed Items\n(观测题项)"]
>         M_JA(("Math JA\n权威辩护")) --> M_items2["Observed Items\n(观测题项)"]
>         M_PJ(("Math PJ\n个人辩护")) --> M_items3["Observed Items\n(观测题项)"]
>     end
>     
>     subgraph History [历史领域测量 / History]
>         direction TB
>         H_SC(("History SC\n简单与确定知识")) --> H_items1["Observed Items\n(观测题项)"]
>         H_JA(("History JA\n权威辩护")) --> H_items2["Observed Items\n(观测题项)"]
>         H_PJ(("History PJ\n个人辩护")) --> H_items3["Observed Items\n(观测题项)"]
>     end
> 
>     %% 因子间的协方差
>     M_SC <.-> H_SC
>     M_JA <.-> H_JA
>     M_PJ <.-> H_PJ
>     M_SC <.-> M_JA & M_PJ
>     H_SC <.-> H_JA & H_PJ
>     
>     classDef latent fill:#dcfce7,stroke:#22c55e,stroke-width:2px;
>     class M_SC,M_JA,M_PJ,H_SC,H_JA,H_PJ latent;
> ```"""
content = re.sub(
    r"> !\[\]\(https://img\.mylikemie\.icu/sources/Greene_2010_JEP/figures/Greene_2010_JEP_Fig2_.*?\.jpg\)",
    fig2_mermaid,
    content,
    flags=re.DOTALL
)

# Replace Figure 3
fig3_mermaid = """> ```mermaid
> flowchart TD
>     C{"潜在类别 (Latent Class)\n提取出6个定性发展阶段"}
>     
>     subgraph Continuous [连续潜变量因子 / Continuous Factors]
>         direction LR
>         F1(("Math SC"))
>         F2(("Math JA"))
>         F3(("Math PJ"))
>         F4(("Hist SC"))
>         F5(("Hist JA"))
>         F6(("Hist PJ"))
>     end
>     
>     %% 类别预测连续因子的均值分布
>     C -->|决定因子的均值轮廓| Continuous
>     
>     %% 测量模型部分
>     F1 --> I1[Items]
>     F2 --> I2[Items]
>     F3 --> I3[Items]
>     F4 --> I4[Items]
>     F5 --> I5[Items]
>     F6 --> I6[Items]
>     
>     classDef classNode fill:#fee2e2,stroke:#ef4444,stroke-width:2px;
>     classDef factorNode fill:#dcfce7,stroke:#22c55e,stroke-width:2px;
>     class C classNode;
>     class F1,F2,F3,F4,F5,F6 factorNode;
> ```"""
content = re.sub(
    r"> !\[\]\(https://img\.mylikemie\.icu/sources/Greene_2010_JEP/figures/Greene_2010_JEP_Fig3_.*?\.jpg\)",
    fig3_mermaid,
    content,
    flags=re.DOTALL
)

# Replace Figure 4
fig4_mermaid = """> ```mermaid
> flowchart LR
>     subgraph Profiles [类别轮廓模式映射 / Profile Mapping]
>         direction TB
>         C4["类别 4 (现实主义为主)\n数学三维皆强\n历史出现分化"] 
>         C2["类别 2 (怀疑论者)\n依赖个人辩护 PJ\n排斥权威 JA"]
>         C3["类别 3 (理性主义者)\n历史学科中等\n摒弃绝对知识 SC"]
>     end
>     
>     subgraph Dimensions [认知维度得分 / Factor Means]
>         direction TB
>         D1["高 SC / 高 JA"]
>         D2["低 SC / 低 JA / 高 PJ"]
>         D3["低 SC / 中等 JA / 中等 PJ"]
>     end
>     
>     C4 -->|在图表中表现为| D1
>     C2 -->|在图表中表现为| D2
>     C3 -->|在图表中表现为| D3
>     
>     style Profiles fill:#f3f4f6,stroke:#9ca3af,stroke-dasharray: 5 5
> ```"""
content = re.sub(
    r"> !\[\]\(https://img\.mylikemie\.icu/sources/Greene_2010_JEP/figures/Greene_2010_JEP_Fig4_.*?\.jpg\)",
    fig4_mermaid,
    content,
    flags=re.DOTALL
)

with open(file_path, "w") as f:
    f.write(content)

print("Done.")
