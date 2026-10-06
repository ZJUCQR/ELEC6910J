# Sources · 资料来源与说明

<p class="chapter-subtitle">内容出处、整理范围与原页核对</p>

## 1. 课程来源

本站根据提供的五份 ELEC6910J Deep Reinforcement Learning 课件整理，共 329 页，授课教师为 HKUST ECE 的 **Ling PAN**。

| 文件 | 页数 | 对应内容 |
| --- | ---: | --- |
| [ELEC6910J_Lec_1_2_updated.pdf](../assets/pdf/ELEC6910J_Lec_1_2_updated.pdf) | 85 | Introduction、Probability Basics |
| [ELEC6910J_Lec_3_4.pdf](../assets/pdf/ELEC6910J_Lec_3_4.pdf) | 81 | Bandits、MDPs |
| [ELEC6910J_Lec_5_6.pdf](../assets/pdf/ELEC6910J_Lec_5_6.pdf) | 65 | Value Functions、Bellman、Value Iteration |
| [ELEC6910J_Lec_7_8.pdf](../assets/pdf/ELEC6910J_Lec_7_8.pdf) | 57 | Policy Evaluation、Improvement、Iteration、Convergence |
| [ELEC6910J_Lec_9_10.pdf](../assets/pdf/ELEC6910J_Lec_9_10.pdf) | 41 | MC Prediction、MC Control |

原课件注明部分内容改编自 UC Berkeley CS188 / CS285、Stanford CS109 / CS229、CMU 10-403 等。各页原有署名和致谢保留在截图及 PDF 中。

课件推荐 Sutton 与 Barto 的 Reinforcement Learning。可结合作者提供的[教材页面](http://incompleteideas.net/book/the-book-2nd.html)阅读，但本站的章节范围以这五份文件为准。

课程课件、截图及其引用素材的权利属于原作者。本站新增说明为学习整理，不代表授课教师的官方讲义；也不为原课件重新授予许可。

## 2. 原课件与笔记补充

正文中的“原课件例子”可通过图下注明的 PDF 页码核对；“笔记补充”包括进一步展开的数值计算、Python 示例和赛车交互演示。

以下是整理时发现、并在相关章节说明的差异：

| 位置 | 原页情况 | 笔记处理 |
| --- | --- | --- |
| Lec 1–2，[p. 39](../slides/lecture-01.md#p039) | 把 DeepSeek-R1 标在 2024 年应用条目中 | 保留截图，但不把这一标签改写成核实后的发布时间；DeepSeek-R1 正式发布于 2025 年 1 月 |
| Lec 1–2，[p. 80](../slides/lecture-02.md#p080) | 方差性质一行将两个二阶量以等号连接 | 使用 $\operatorname{Var}(X)=\mathbb E[X^2]-(\mathbb E[X])^2$ |
| Lec 3–4，[p. 34](../slides/lecture-03.md#p034) | Contextual Bandit 举例包含动作决定下一机器 | 若动作影响未来上下文，应按序列决策／MDP 理解 |
| Lec 3–4，[p. 65–67](../slides/lecture-04.md#p065) | 回报下标及有限回合末项指数写法不统一 | 统一为 $G_t=\sum_{k=0}^{T-t-1}\gamma^kR_{t+k+1}$ |
| Lec 7–8，[p. 28–29](../slides/lecture-07.md#p028) | 文字只提右下终止态，图与数值包含两角 | 按图中的两个终止态解释 4×4 例题 |
| Lec 7–8，[p. 30](../slides/lecture-08.md#p030) | 第二部分封面仍为 Lecture 7 | 依据文件分组和主题，将此部分编为第 8 章 |
| Lec 9–10，[p. 14](../slides/lecture-09.md#p014) | 每次访问回报展开项与前文不一致 | 用 $(r_2+(1+\gamma)r_3)/2$，并说明 $\gamma=1$ 的特殊情形 |
| Lec 9–10，[p. 21](../slides/lecture-09.md#p021) | “Converge quadratically” 易与数值迭代二次收敛混淆 | 说明独立有限方差样本均值的 MSE 与标准误差速率 |
| Lec 9–10，[p. 30](../slides/lecture-10.md#p030) | $\epsilon$-soft 一处使用严格大于 | 采用标准下界 $\pi(a\mid s)\geq\epsilon/|\mathcal A(s)|$ |

对 Bellman 方程唯一解、压缩映射与算法收敛，正文补充有限状态、折扣、终止性、访问覆盖等相应条件，避免把有限步演示推广为无条件结论。

## 3. 公开副本与页码

- 本地提供的原 PDF 保持不变。
- 公开版本仅遮盖了教学事务页中的会议访问凭据，学术内容与页序保持完整。
- 所有引用采用 PDF 物理页序，从 1 开始。
- 课件中的作业、考试和课程事务日期是原始记录，不作为当前日程提醒。
- 课件中的视频或动画以所提供 PDF 能呈现的静态页保留；不同演示阶段若已导出为不同页，均保存在逐页档案。

## 4. 修订反馈

若发现公式、解释或页码有误，可在 [GitHub Issues](https://github.com/ZJUCQR/ELEC6910J/issues)注明章节与原页。正文与构建配置均保存在同一仓库，便于继续补充后续课件。
