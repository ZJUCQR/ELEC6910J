# 4: Markov Decision Processes

<p class="chapter-subtitle">马尔可夫决策过程 · 描述连续决策</p>

!!! info "本章对应课件"

    Lecture 4 · <strong>ELEC6910J_Lec_3_4.pdf，p. 36–81</strong>。
    [查看本讲全部课件](../slides/lecture-04.md) · [下载 PDF](../assets/pdf/ELEC6910J_Lec_3_4.pdf)

## 4.1 From Bandits to MDPs

Bandit 中不建模动作对后续环境状态的影响。MDP（Markov Decision Process）则需要回答：**现在选这个动作，会把未来带到哪里？**

一个 MDP 可写为：

$$
(\mathcal S,\mathcal A,T,R,\gamma).
$$

| 符号 | 含义 |
| --- | --- |
| $\mathcal S$ | State Space，状态空间 |
| $\mathcal A$ | Action Space，动作空间 |
| $T(s,a,s')=P(s'\mid s,a)$ | Transition Dynamics，转移概率 |
| $R(s,a,s')$ | 该次转移的奖励或条件期望奖励 |
| $\gamma$ | Discount Factor，折扣因子 |

每个 $(s,a)$ 对应的后继概率之和必须为 1。环境也可用联合分布 $p(s',r\mid s,a)$ 表示，把随机奖励一起纳入模型。

- Model（模型）：描述动作之后环境如何变化。
- Planning（规划）：利用模型比较可能的未来，决定如何行动。
- Learning（学习）：从经验中估计未知的价值、策略或模型。

### 4.1.1 Markov Property（马尔可夫性）

$$
P(S_{t+1}\mid S_t,A_t,S_{t-1},A_{t-1},\ldots,S_0)
=P(S_{t+1}\mid S_t,A_t).
$$

给定当前状态与动作后，更早的历史不再提供预测下一状态所需的额外信息。**状态必须包含与未来有关的必要信息**；并不是任意一个观察都自动满足马尔可夫性。

### 4.1.2 Full / Partial Observability（可观测性）

- Fully Observable：能够得到决策所需的状态，例如棋盘信息完整可见的围棋。
- Partially Observable：观察仅反映状态的一部分，例如机器人摄像头、扑克中的隐藏手牌。
- 部分可观测问题通常建模为 POMDP。单张图像不一定能提供速度、被遮挡物体等信息。

??? note "课件补充：Markov 与 Chebyshev 不等式"

    对非负随机变量 $X$ 和 $a>0$：

    $$
    P(X\geq a)\leq\frac{\mathbb E[X]}a.
    $$

    对均值为 $\mu$、方差为 $\sigma^2$ 的随机变量：

    $$
    P(|X-\mu|\geq a)\leq\frac{\sigma^2}{a^2}.
    $$

    后者可由前者作用于 $(X-\mu)^2$ 得到。两者是课件 p. 48–49 的概率知识补充；Markov 不等式与 MDP 的马尔可夫性是不同概念。

## 4.2 GridWorld（网格世界） {#gridworld}

沿用第 1 章的噪声移动模型：选择 north 时，向预期方向的概率为 $0.8$，向左右偏移的概率各为 $0.1$，撞墙则停留。

!!! example "原课件例子：从 (1,1) 选择 north"

    按该页采用的坐标记号：

    $$
    \begin{aligned}
    T((1,1),\mathrm{north},(2,1))&=0.8,\\
    T((1,1),\mathrm{north},(1,2))&=0.1,\\
    T((1,1),\mathrm{north},(1,1))&=0.1.
    \end{aligned}
    $$

    三项之和为 1。最后一项来自边界阻挡，并不是环境忽略了该次动作。

{{ slide lec03-04 41 | GridWorld：把一次有噪声的动作写成转移概率 }}

课件随后给出 living reward 为 $-0.1$ 的轨迹例子。每次转移要同时记录状态、动作、下一状态和奖励。注意，不同演示中的 living reward 可能不同，后文价值迭代的演示使用 0。

{{ slide lec03-04 44 | GridWorld 轨迹：实际到达的位置可能偏离选择的方向 }}

## 4.3 Policies（策略）

随机策略：

$$
\pi(a\mid s)=P(A_t=a\mid S_t=s),\qquad
\sum_a\pi(a\mid s)=1.
$$

- Deterministic Policy：每个状态选择一个确定动作，记为 $\pi(s)$。
- Stochastic Policy：给各动作分配概率。
- Stationary Policy：策略不显式依赖时间；学习过程中仍可以不断更新策略参数。
- 有限时域任务中，最佳动作可能与剩余步数有关，此时一般需要 $\pi_t(a\mid s)$。

策略是一套对可能状态的行动规则。它能处理实际偏移后的情况；单一固定动作序列则无法覆盖所有随机分支。

## 4.4 Racing（赛车模型） {#racing}

机器人赛车希望走得远、走得快，但过快会过热。三个状态为 Cool、Warm、Overheated；两个动作为 Slow、Fast。

| 当前状态 | 动作 | 下一状态 | 概率 | 奖励 |
| --- | --- | --- | ---: | ---: |
| Cool | Slow | Cool | 1.0 | +1 |
| Cool | Fast | Cool | 0.5 | +2 |
| Cool | Fast | Warm | 0.5 | +2 |
| Warm | Slow | Cool | 0.5 | +1 |
| Warm | Slow | Warm | 0.5 | +1 |
| Warm | Fast | Overheated | 1.0 | −10 |
| Overheated | 终止 | 无后续决策 | — | 后续回报为 0 |

{{ slide lec03-04 53 | 赛车 MDP：速度收益与过热风险的权衡 }}

!!! tip "读状态图的方法"

    先固定一个状态与动作，再枚举其随机后果。比如 Cool 下的 Fast 有两条概率均为 $0.5$ 的分支，它们共同构成一个动作的期望，不能把两条分支当成两个可自由选择的动作。

课件展示的最优行为是 Cool 时 Fast、Warm 时 Slow。第 6–8 章会在明确折扣设置后计算价值并验证这一策略。

## 4.5 Rewards & Returns（奖励与回报）

Reward Hypothesis（奖励假设）：把目标表述为最大化收到的标量奖励的累计值。奖励描述“希望达到什么”，策略负责学习“怎样达到”。

### 4.5.1 Discounting（折扣）

课件比较 $[1,2,3]$ 与 $[3,2,1]$。当 $\gamma=0.5$：

$$
U([1,2,3])=1+0.5\times2+0.5^2\times3=2.75,
$$

$$
U([3,2,1])=3+0.5\times2+0.5^2\times1=5.25.
$$

未折扣总和相同，但更早获得奖励的序列具有更大折扣回报。折扣也让有界奖励的无限时域回报更容易保持有限。

### 4.5.2 原课件 Quiz：什么时候两条路一样好？ {#discount-quiz}

从 $d$ 出发，向 $e$ 可以立即得到 1；向 $a$ 的路径先得到两个 0，再得到 10。

{{ slide lec03-04 64 | 折扣回报例题：立即的 1 与两步之后的 10 }}

令两条路径回报相等：

$$
0+\gamma\cdot0+\gamma^2\cdot10=1
\quad\Longrightarrow\quad
\gamma=\frac1{\sqrt{10}}\approx0.3162.
$$

- $\gamma$ 更大时，延迟的 10 更有吸引力。
- $\gamma$ 更小时，立即的 1 更有吸引力。
- 指数从 0 开始：第一个收到的奖励不打折。

### 4.5.3 Episodic / Continuing Tasks

Episodic Task（回合制任务）在终止时刻 $T$ 结束：

$$
G_t=\sum_{k=0}^{T-t-1}\gamma^kR_{t+k+1},
\qquad G_T=0.
$$

Continuing Task（持续任务）没有自然终点，通常使用：

$$
G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1},\qquad 0\leq\gamma<1.
$$

若 $|R_t|\leq R_{\max}$，则 $|G_t|\leq R_{\max}/(1-\gamma)$。

!!! warning "无限回报的边界条件"

    有终止状态，并不自动意味着每个策略都会到达它。赛车可以一直慢行而不结束。$\gamma=1$ 时要另外检查终止性及期望回合长度；不能直接套用折扣 MDP 的收敛结论。

## 4.6 Values & Problem Types（价值与任务类型）

$$
V^\pi(s)=\mathbb E_\pi[G_t\mid S_t=s],
\qquad
Q^\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a].
$$

- $V^\pi$：从状态 $s$ 出发，此后遵循 $\pi$ 的期望回报。
- $Q^\pi$：先在 $s$ 做指定动作 $a$，此后遵循 $\pi$ 的期望回报。
- $V^*(s)=\max_\pi V^\pi(s)$，$Q^*(s,a)=\max_\pi Q^\pi(s,a)$。
- Prediction（预测）：给定策略，求它的价值。
- Control（控制）：寻找更好的策略，最终求最优策略。

{{ slide lec03-04 77 | GridWorld 中的价值与策略：数值描述好坏，箭头描述行动 }}

最优价值之间满足：

$$
V^*(s)=\max_aQ^*(s,a),
$$

$$
Q^*(s,a)=\sum_{s'}T(s,a,s')
\left[R(s,a,s')+\gamma V^*(s')\right].
$$

下一章将从回报定义推导这些 Bellman 方程，区分固定策略的期望与最优动作的选择。

## 4.7 本章检查

- 为什么状态应该包含足够的历史信息？
- 转移概率的求和对象是什么？是固定 $(s,a)$ 下的全部后继。
- 回合终止后，为什么价值为 0，却不意味着进入终止态时的奖励为 0？
- 能否从赛车转移表分别写出 Cool / Slow 和 Cool / Fast 的一步期望？
