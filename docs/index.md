---
title: 深度强化学习
description: ELEC6910J 中文课程笔记。从概率与探索，到 Bellman 方程、动态规划和 Monte Carlo。
hide:
  - toc
---

<div class="course-cover" markdown="1">
<div class="cover-label"><span class="cover-dot"></span> COURSE NOTES <span class="cover-divider">/</span> ELEC6910J</div>

# 深度强化学习

<p class="cover-english">Deep Reinforcement Learning</p>
<p class="cover-intro">从一次选择，到长期回报。<br>沿着概率、价值与策略，理解智能体如何从交互中学习。</p>

<div class="cover-equation" aria-label="价值等于奖励与折扣后的未来价值的期望">
<span>STATE</span><b>→</b><span>ACTION</span><b>→</b><span>REWARD</span><b>↗</b>
<div class="arithmatex">\(G_t = R_{t+1} + \gamma G_{t+1}\)</div>
</div>

[从第 1 章开始 →](chapters/01-introduction.md){ .md-button .md-button--primary }
[查找课件例题](examples.md){ .md-button }

<div class="cover-stats"><div><strong>10</strong><span>讲课程笔记</span></div><div><strong>329</strong><span>页课件档案</span></div><div><strong>05</strong><span>份原课件</span></div><div><strong>中 / EN</strong><span>术语对照</span></div></div>
</div>

## 学习路线

课程内容由“如何描述不确定性”，逐步走向“如何比较行动”和“如何从经验中改进策略”。按授课顺序阅读，也可以从熟悉的主题直接进入。

<div class="learning-route" markdown="1">

<div class="route-stage"><span>01 — 04</span><strong>描述问题</strong><small>概率 · 探索 · MDP</small></div>
<div class="route-stage"><span>05 — 08</span><strong>有模型时求解</strong><small>价值 · Bellman · 动态规划</small></div>
<div class="route-stage"><span>09 — 10</span><strong>从经验中学习</strong><small>Monte Carlo · 预测与控制</small></div>

</div>

### Part I · Foundations

| 章节 | 核心问题 | 课件中的例子 |
| --- | --- | --- |
| [01 · Introduction](chapters/01-introduction.md) | 智能体为什么需要策略？ | 出租车 PEAS、图像识别、随机网格 |
| [02 · Probability Basics](chapters/02-probability.md) | 怎样用分布描述不确定性？ | 天气与温度、骰子、条件概率 |
| [03 · Multi-Armed Bandits](chapters/03-bandits.md) | 何时探索，何时利用？ | 广告投放、LG1 / LG7 餐厅选择 |
| [04 · Markov Decision Processes](chapters/04-mdp.md) | 当前行动怎样影响未来？ | GridWorld、赛车、折扣路径选择 |

### Part II · Planning with a Model

| 章节 | 核心问题 | 课件中的例子 |
| --- | --- | --- |
| [05 · Value Functions & Bellman Equations](chapters/05-bellman.md) | 怎样把长期回报分解为一步？ | 状态价值、动作价值与备份图 |
| [06 · Value Iteration](chapters/06-value-iteration.md) | 最优价值如何逐轮计算？ | 五状态方程、赛车、价值传播 |
| [07 · Policy Evaluation](chapters/07-policy-evaluation.md) | 一套固定策略有多好？ | 折扣赛车、4×4 GridWorld |
| [08 · Policy Iteration & Convergence](chapters/08-policy-iteration.md) | 怎样保证策略越改越好？ | 赛车策略迭代、压缩映射 |

### Part III · Learning from Experience

| 章节 | 核心问题 | 课件中的例子 |
| --- | --- | --- |
| [09 · Monte-Carlo Prediction](chapters/09-mc-prediction.md) | 没有模型，怎样估计价值？ | 首次访问与每次访问 |
| [10 · Monte-Carlo Control](chapters/10-mc-control.md) | 怎样在探索中改进策略？ | Exploring Starts、Blackjack |

## 课程与笔记

!!! info "课程基本信息"

    - **课程**：ELEC6910J · Deep Reinforcement Learning
    - **授课教师**：Ling PAN
    - **学校**：The Hong Kong University of Science and Technology，Department of Electronic and Computer Engineering
    - **笔记范围**：本次提供的 Lecture 1–10，共五份 PDF。后续 TD、Policy Gradient、Actor-Critic 等内容尚不在这些材料中。

!!! note "笔记编写方式"

    正文采用英文术语与中文解释，按“概念—公式—例子—易错点”整理。课件原图、例题和分步演示保存在[完整课件](slides/index.md)中；正文选取重点截图并标注 PDF 页码。可点击图片放大，或跳转原页核对。

    标为“笔记补充”的计算、代码和交互演示用于帮助理解。涉及原页不一致之处，说明见[资料来源与勘误](reference/sources.md)。

## 复习入口

- [例题索引](examples.md)：按问题找到截图、计算步骤和对应章节。
- [公式速查](reference/formulas.md)：概率、回报、Bellman、DP 与 MC 的核心公式。
- [术语对照](reference/glossary.md)：中英术语和符号。
- [完整课件与下载](slides/index.md)：329 页原页档案和五份 PDF。
- [赛车迭代演示](chapters/06-value-iteration.md#racing-lab)：调整折扣，观察同一模型的价值如何变化。

<div class="source-note" markdown="1">
笔记组织与语言参考 [ZhengliangDuanfang · 计算机网络](https://zhengliangduanfang.github.io/T-ComputerNetworks/)；视觉重新设计。课程内容与原图归课件作者及其注明的来源所有。发现问题可在 [GitHub 仓库](https://github.com/ZJUCQR/ELEC6910J/issues)反馈。
</div>
