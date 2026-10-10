---
title: 深度强化学习
description: ELEC6910J 中文课程笔记与期中复习。从概率与探索，到动态规划、Monte Carlo、TD、SARSA 和 Q-learning。
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
[期中考试复习](#midterm){ .md-button }

</div>

## Mid-Term Exam · 期中复习 {#midterm}

### 考试范围

<div class="exam-scope" markdown="1">

| 考试主题 | 对应笔记 | 复习时需要掌握 |
| --- | --- | --- |
| Bandits and Markov Decision Process | [第 3 章](chapters/03-bandits.md)、[第 4 章](chapters/04-mdp.md) | 探索与利用；状态、动作、转移、奖励；Markov 性；折扣回报 |
| Value Functions and Bellman Equations | [第 5 章](chapters/05-bellman.md) | $V^\pi$ 与 $Q^\pi$；期望方程与最优方程；策略平均与动作最大值 |
| Dynamic Programming | [第 6 章](chapters/06-value-iteration.md)、[第 7 章](chapters/07-policy-evaluation.md)、[第 8 章](chapters/08-policy-iteration.md) | Value Iteration；Policy Evaluation、Improvement、Iteration；终止边界与收敛条件 |
| Monte-Carlo Methods | [第 9 章](chapters/09-mc-prediction.md)、[第 10 章](chapters/10-mc-control.md) | Prediction 与 Control；First-Visit / Every-Visit；完整回报；ES 与 soft policy |
| Temporal Difference Prediction | [第 11 章](chapters/11-td-prediction.md) | TD target、TD error、TD(0)；采样与自举；偏差与方差；多步回报 |
| Temporal Difference Control：On-policy SARSA、Off-policy Q-learning | [第 12 章](chapters/12-td-control.md) | 实际下一动作与贪心目标的差别；Q 表更新；探索覆盖、步长与 GLIE；多步 SARSA |

</div>

!!! info "考试时间"

    **10 月 23 日 15:00**

### 复习顺序

1. **先串起概念**：从 MDP 和回报出发，写出 Bellman 关系；再按“需要模型吗、是否采样、是否自举、何时更新、评估哪种策略”比较 DP、MC、TD、SARSA 与 Q-learning。
2. **再独立手算**：做下面的练习。每一步都写清旧值、目标、误差与新值，终止状态单独处理；完成后再展开答案核对。
3. **最后解释算法**：遮住公式，说明每一项来自模型、真实奖励还是已有估计；检查固定策略、最优策略、行为策略与目标策略有没有混淆。

### 手算练习

| 练习 | 给定条件与任务 |
| --- | --- |
| [GridWorld 策略评估](chapters/07-policy-evaluation.md#gridworld-evaluation) | 4×4 网格，非终止状态每步奖励 $-1$，均匀随机策略，初值全为 0。做一轮同步更新，区分终止与非终止状态。 |
| [首次访问与每次访问 MC](chapters/09-mc-prediction.md#first-every) | 目标状态在 $t=1,2$ 出现，$t=3$ 终止；$r_2=2,r_3=4,\gamma=1$。分别求两次回报、First-Visit 值与 Every-Visit 均值。 |
| [Lake 的 TD 更新](chapters/11-td-prediction.md#lake) | 初值为 0，$\alpha=0.1,\gamma=0.5$，每步奖励 $-0.4$；依次经历 $(1,1)\to(1,2)\to(1,3)\to(1,2)$。顺序更新三个出发状态。 |
| [两步 TD 的终止边界](chapters/11-td-prediction.md#n-step-td) | 两个奖励为 1、2，$\gamma=0.5$。分别计算“两步后未终止且后继价值为 4”与“两步后终止”的目标。 |
| [SARSA 与 Q-learning](chapters/12-td-control.md#on-off-policy) | $Q(s,a)=2,r=0,\gamma=0.9,\alpha=0.1$；下一状态实际动作价值为 1、最大动作价值为 5。分别写目标与新 Q 值。 |
| [小狗 Q 表](chapters/12-td-control.md#dog-grid) | Q 表初值为 0，$\alpha=0.1,\gamma=0.99$。先向右获得 $+1$，再向下获得 $-10$ 并终止，指出每步只修改哪个表项。 |

??? success "自测答案：完成手算后再展开"

    - **GridWorld**：所有非终止状态更新为 $-1$，两个终止状态保持 0。第一轮所有后继旧值为 0。
    - **MC**：$G_1=6,G_2=4$；First-Visit 为 6，Every-Visit 均值为 5。
    - **Lake**：$V(1,1)=-0.04$，$V(1,2)=-0.04$，$V(1,3)=-0.042$。第三步用到第二步刚更新的值。
    - **两步 TD**：未终止时目标为 3；终止时为 2，没有自举项。
    - **SARSA**：目标 0.9，新值 1.89。**Q-learning**：目标 4.5，新值 2.25。
    - **小狗 Q 表**：$Q((0,0),\rightarrow)=0.1$；$Q((0,1),\downarrow)=-1$，其余表项保持原值。

## 课程目录

<div class="chapter-index" markdown="1">

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
| [11 · Temporal Difference Prediction](chapters/11-td-prediction.md) | 怎样在回合结束前学习？ | Lake、Random Walk、多步回报 |
| [12 · Temporal Difference Control](chapters/12-td-control.md) | 实际行动和学习目标可以不同吗？ | Windy GridWorld、小狗 Q 表、SARSA 与 Q-learning |

</div>

## 课程与笔记

!!! info "课程基本信息"

    - **课程**：ELEC6910J · Deep Reinforcement Learning
    - **授课教师**：Ling PAN
    - **学校**：The Hong Kong University of Science and Technology，Department of Electronic and Computer Engineering
    - **笔记范围**：Lecture 1–12，涵盖 DP、MC、TD、SARSA、Q-learning 与 DQN 入门。

## Formula Sheet · 公式速查 { #formulas }

<p class="chapter-subtitle">先确认条件，再选择公式</p>

本页统一使用 $R_{t+1}$ 表示执行 $A_t$ 后获得的奖励；$T$ 表示回合终止时刻。概率和期望均按相关事件有定义、所需矩存在的条件使用。

### 1. Probability（概率）

| 名称 | 公式 |
| --- | --- |
| 条件概率 | $P(A\mid B)=P(A,B)/P(B)$，$P(B)>0$ |
| 乘法公式 | $P(A,B)=P(A\mid B)P(B)$ |
| 边缘化 | $P(X=x)=\sum_yP(X=x,Y=y)$ |
| 全概率 | $P(A)=\sum_iP(A\mid B_i)P(B_i)$，$\{B_i\}$ 构成划分 |
| Bayes | $P(B_j\mid A)=P(A\mid B_j)P(B_j)/P(A)$ |
| 独立 | $P(A,B)=P(A)P(B)$ |
| 条件独立 | $P(X,Y\mid Z)=P(X\mid Z)P(Y\mid Z)$ |
| 期望 | $\mathbb E[X]=\sum_xxP(X=x)$ |
| 方差 | $\operatorname{Var}(X)=\mathbb E[X^2]-(\mathbb E[X])^2$ |
| 标准差 | $\operatorname{Std}(X)=\sqrt{\operatorname{Var}(X)}$ |

[天气联合表与计算](chapters/02-probability.md#weather-table)

### 2. Bandit & Incremental Mean

$$
q_*(a)=\mathbb E[R_t\mid A_t=a],
\qquad
Q_{n+1}=Q_n+\frac1n(R_n-Q_n).
$$

固定步长形式：

$$
Q_{n+1}=Q_n+\alpha(R_n-Q_n)
=(1-\alpha)^nQ_1+\sum_{i=1}^n\alpha(1-\alpha)^{n-i}R_i.
$$

这里的 $n$ 是该动作的样本计数，不一定是全局时间。

### 3. Returns & Values（回报与价值）

$$
G_t=\sum_{k=0}^{T-t-1}\gamma^kR_{t+k+1}
=R_{t+1}+\gamma G_{t+1},\qquad G_T=0.
$$

持续任务在适当折扣条件下，把有限上限改为 $\infty$。

$$
V^\pi(s)=\mathbb E_\pi[G_t\mid S_t=s],
\qquad
Q^\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a].
$$

$$
V^\pi(s)=\sum_a\pi(a\mid s)Q^\pi(s,a),
\qquad V^*(s)=\max_aQ^*(s,a).
$$

### 4. Bellman Equations

#### 4.1 固定策略：对动作加权平均

$$
V^\pi(s)=\sum_a\pi(a\mid s)
\sum_{s',r}p(s',r\mid s,a)[r+\gamma V^\pi(s')].
$$

$$
Q^\pi(s,a)=\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma\sum_{a'}\pi(a'\mid s')Q^\pi(s',a')\right].
$$

#### 4.2 最优策略：对动作取最大值

$$
V^*(s)=\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma V^*(s')].
$$

$$
Q^*(s,a)=\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma\max_{a'}Q^*(s',a')\right].
$$

若使用 $T(s,a,s')$ 与条件期望奖励 $R(s,a,s')$，把对 $(s',r)$ 的和改成对 $s'$ 的和，并在括号内代入 $R$。

### 5. Dynamic Programming

#### 5.1 Value Iteration

$$
V_{k+1}(s)\leftarrow
\max_a\sum_{s'}T(s,a,s')[R(s,a,s')+\gamma V_k(s')].
$$

#### 5.2 Policy Evaluation

$$
V_{k+1}(s)\leftarrow
\sum_a\pi(a\mid s)\sum_{s'}T(s,a,s')
[R(s,a,s')+\gamma V_k(s')].
$$

固定策略的矩阵形式：

$$
(I-\gamma P^\pi)V^\pi=r^\pi.
$$

#### 5.3 Policy Improvement

$$
\pi'(s)\in\arg\max_a
\sum_{s'}T(s,a,s')[R(s,a,s')+\gamma V^\pi(s')].
$$

如果 $Q^\pi(s,\pi'(s))\geq V^\pi(s)$ 对所有状态成立，则在定理适用条件下有 $V^{\pi'}\geq V^\pi$。

#### 5.4 Contraction

$$
\|T^*u-T^*v\|_\infty\leq\gamma\|u-v\|_\infty,\qquad 0\leq\gamma<1.
$$

同样的界适用于 $T^\pi$。$\gamma=1$ 时不能直接套用压缩映射定理。

### 6. Monte Carlo

状态价值的增量样本均值：

$$
N(s)\leftarrow N(s)+1,\qquad
V(s)\leftarrow V(s)+\frac{G-V(s)}{N(s)}.
$$

动作价值：

$$
N(s,a)\leftarrow N(s,a)+1,\qquad
Q(s,a)\leftarrow Q(s,a)+\frac{G-Q(s,a)}{N(s,a)}.
$$

首次访问与每次访问的区别，是**哪些 $G$ 被纳入更新**，不是换了一种平均公式。

### 7. Exploration（探索）

共 $m$ 个动作、一个指定贪心动作时：

$$
\pi(a\mid s)=
\begin{cases}
1-\epsilon+\epsilon/m,&a=a^*,\\
\epsilon/m,&a\ne a^*.
\end{cases}
$$

$\epsilon$-soft 要求 $\pi(a\mid s)\geq\epsilon/m$。固定正 $\epsilon$ 会保留探索，因而最优性的策略类也受到约束。

### 8. Temporal Difference Prediction

$$
Y_t=R_{t+1}+\gamma V(S_{t+1}),\qquad
\delta_t=Y_t-V(S_t),\qquad
V(S_t)\leftarrow V(S_t)+\alpha\delta_t.
$$

未到终止时，多步目标为：

$$
G_{t:t+n}=\sum_{k=0}^{n-1}\gamma^kR_{t+k+1}+\gamma^nV(S_{t+n}),\qquad t+n<T.
$$

若 $t+n\geq T$，奖励只累加到 $R_T$，并去掉自举项。[Lake 手算](chapters/11-td-prediction.md#lake) · [多步回报](chapters/11-td-prediction.md#n-step-td)。

### 9. SARSA & Q-learning

$$
Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha[Y_t-Q(S_t,A_t)].
$$

| 方法 | 非终止转移的目标 $Y_t$ |
| --- | --- |
| SARSA | $R_{t+1}+\gamma Q(S_{t+1},A_{t+1})$，使用实际下一动作 |
| Q-learning | $R_{t+1}+\gamma\max_aQ(S_{t+1},a)$，使用贪心目标 |

$n$-step SARSA 的非终止目标为：

$$
G_{t:t+n}=\sum_{k=0}^{n-1}\gamma^kR_{t+k+1}
+\gamma^nQ(S_{t+n},A_{t+n}).
$$

真正终止时，所有这些方法都去掉终止后的价值项。[两种目标的手算对照](chapters/12-td-control.md#on-off-policy)。

### 10. Step Sizes & Exploration

对每个状态或状态—动作对自身的更新序列，常见步长条件为：

$$
\sum_{k=1}^{\infty}\alpha_k=\infty,\qquad
\sum_{k=1}^{\infty}\alpha_k^2<\infty.
$$

还需充分访问等任务条件。SARSA 的最优性结论通常要求 GLIE：无限探索且策略在极限下趋于贪心；仅有 $\epsilon_t\to0$ 不足以保证前者。[收敛条件](chapters/12-td-control.md#glie)。

## Glossary · 术语对照 { #glossary }

<p class="chapter-subtitle">保留英文术语，对齐中文含义</p>

### 1. Learning & Decision Making

| English | 中文 | 本课程中的含义 |
| --- | --- | --- |
| Agent | 智能体 | 感知环境并采取行动的实体 |
| Environment | 环境 | 对动作作出响应并产生反馈的系统 |
| Rationality | 理性 | 根据已有信息最大化期望效用 |
| Supervised Learning | 监督学习 | 从输入与标签的配对中学习 |
| Unsupervised Learning | 无监督学习 | 从无标签数据中发现结构 |
| Reinforcement Learning | 强化学习 | 从交互与奖励中学习决策 |
| Regression | 回归 | 预测连续数值 |
| Classification | 分类 | 预测离散类别 |
| Feature | 特征 | 用于预测或决策的输入属性 |
| Exploration | 探索 | 通过尝试获得更多信息 |
| Exploitation | 利用 | 根据现有估计选择较好动作 |
| Regret | 遗憾 | 相对于最优选择的机会损失 |

### 2. Probability

| English | 中文 | 说明 |
| --- | --- | --- |
| Sample Space | 样本空间 | 全部可能结果 |
| Event | 事件 | 样本空间的子集 |
| Random Variable | 随机变量 | 样本点到数值或取值的函数 |
| Joint Distribution | 联合分布 | 多个变量共同取值的概率 |
| Marginalization | 边缘化 | 对其他变量求和或积分 |
| Conditional Probability | 条件概率 | 已知某事件发生后的概率 |
| Normalization | 归一化 | 调整总概率质量为 1 |
| Prior / Posterior | 先验／后验 | 观察证据前后的分布 |
| Independence | 独立 | 联合概率可分解为边缘概率之积 |
| Expectation | 期望 | 按概率加权的平均 |
| Variance | 方差 | 与均值的平方偏差的期望 |
| Standard Deviation | 标准差 | 方差的平方根 |

### 3. MDP & Values

| English | 中文 | 说明 |
| --- | --- | --- |
| State | 状态 | 描述决策所需的当前信息 |
| Observation | 观察 | 智能体实际接收到的信息 |
| Action | 动作 | 智能体可作出的选择 |
| Policy | 策略 | 状态到动作或动作分布的映射 |
| Plan | 计划 | 预先给定的动作序列 |
| Transition Dynamics | 转移动力学 | 环境状态如何随动作变化 |
| Markov Property | 马尔可夫性 | 给定当前状态后无需额外历史 |
| Reward | 奖励 | 一次交互的标量反馈 |
| Return | 回报 | 未来奖励的累计，通常带折扣 |
| Discount Factor | 折扣因子 | 控制未来奖励权重的 $\gamma$ |
| Episode | 回合 | 从起点到终止的一段交互 |
| Terminal State | 终止态 | 回合已结束，无后续回报 |
| State Value | 状态价值 | 从状态出发的期望回报 |
| Action Value / Q-value | 动作价值 | 先做指定动作、之后遵循策略的期望回报 |
| Prediction | 预测／评估 | 计算给定策略的价值 |
| Control | 控制 | 改进策略、寻找最优行为 |

### 4. Algorithms

| English | 中文 | 说明 |
| --- | --- | --- |
| Dynamic Programming | 动态规划 | 利用已知模型与 Bellman 关系求解 |
| Backup | 备份／回传更新 | 将后继信息合并为当前价值 |
| Bootstrapping | 自举 | 用已有估计构造新的更新目标 |
| Value Iteration | 价值迭代 | 反复进行 Bellman 最优备份 |
| Policy Evaluation | 策略评估 | 计算固定策略的价值 |
| Policy Improvement | 策略改进 | 根据当前价值构造更好的策略 |
| Policy Iteration | 策略迭代 | 交替执行评估与改进 |
| Policy Extraction | 策略提取 | 从价值函数中选出动作 |
| Contraction | 压缩映射 | 按严格小于 1 的比例缩小距离 |
| Fixed Point | 不动点 | 经过算子作用后不变的点 |
| Monte Carlo | 蒙特卡洛 | 用采样回报平均估计价值 |
| First-Visit | 首次访问 | 每回合只使用某状态或状态—动作对的第一次访问 |
| Every-Visit | 每次访问 | 使用回合中的全部相应访问 |
| Temporal Difference / TD | 时序差分 | 结合采样与自举进行价值更新 |
| TD Target | 时序差分目标 | 一步奖励加折扣后的后继价值估计 |
| TD Error | 时序差分误差 | TD 目标减去当前估计 |
| n-step Return | 多步回报 | 前 n 步真实奖励加末尾自举值；到终点后不再自举 |
| SARSA | 同策略 TD 控制 | 使用实际下一动作的 Q 值构造目标 |
| Q-learning | 异策略 TD 控制 | 使用下一状态最大 Q 值构造目标 |
| Behavior Policy | 行为策略 | 用于与环境交互、收集数据的策略 |
| Target Policy | 目标策略 | 被评估或改进的策略 |
| GLIE | 无限探索且极限贪心 | 同时要求充分访问和最终趋于贪心 |
| Tabular Method | 表格方法 | 为各状态或状态—动作对分别存储估计 |
| Function Approximation | 函数近似 | 用共享参数表示价值等函数 |
| Deep Q-Network / DQN | 深度 Q 网络 | 用神经网络近似动作价值函数 |
| Exploring Starts | 探索性起始 | 各相关状态—动作对都有机会成为起点 |
| Soft Policy | 软策略 | 各可用动作均有正概率 |
| On-policy | 同策略 | 数据生成策略与被评估／改进策略相同 |
| Off-policy | 异策略 | 两种策略可以不同 |
| Usable Ace | 可用 Ace | 在不爆牌的前提下可按 11 计的 Ace |

### 5. 常用符号

| 符号 | 含义 |
| --- | --- |
| $S_t,A_t,R_{t+1}$ | 当前状态、动作、动作之后得到的奖励 |
| $s',a'$ | 后继状态、后继状态中的动作 |
| $\pi(a\mid s)$ | 在 $s$ 下选择 $a$ 的概率 |
| $T(s,a,s')$ | 转移概率；注意与终止时刻 $T$ 区分 |
| $p(s',r\mid s,a)$ | 下一状态与奖励的联合条件分布 |
| $G_t$ | 从时刻 $t$ 开始的回报 |
| $V^\pi,Q^\pi$ | 固定策略下的价值 |
| $V^*,Q^*$ | 最优价值 |
| $\alpha$ | 学习率／步长 |
| $\epsilon$ | 探索概率或软策略参数 |
| $\gamma$ | 折扣因子 |
| $N(s),N(s,a)$ | 纳入统计的访问计数 |
| $\delta_t$ | 当前转移的 TD 误差 |
| $G_{t:t+n}$ | 从时刻 t 开始的 n 步更新目标 |
| $\theta$ | 函数近似器或神经网络的参数 |

<div class="source-note" markdown="1">
课程内容与原图归课件作者及其注明的来源所有。发现问题可在 [GitHub 仓库](https://github.com/ZJUCQR/ELEC6910J/issues)反馈。
</div>
