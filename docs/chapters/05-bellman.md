# 5: Value Functions & Bellman Equations

<p class="chapter-subtitle">价值函数与贝尔曼方程 · 把未来拆成一步</p>

**主要内容**：状态价值与动作价值、Bellman 期望方程、最优方程与策略提取。

## 5.1 Value Functions（价值函数）

价值函数衡量在给定策略下，一个状态或状态—动作对有多好。这里的“好”由**未来累计奖励的期望**定义。

$$
V^\pi(s)=\mathbb E_\pi[G_t\mid S_t=s],
$$

$$
Q^\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a].
$$

- $V^\pi$ 的第一个动作也由 $\pi$ 选择。
- $Q^\pi$ 的第一个动作固定为 $a$，之后才按 $\pi$ 行动。
- 上标 $\pi$ 不能随意省略：同一状态在不同策略下可能有完全不同的价值。
- 终止态没有后续奖励，因此 $V^\pi(s_{\mathrm{terminal}})=0$。进入终止态的奖励已计入前一次转移。

### 5.1.1 GridWorld 中的三种表示

{{ slide lec05-06 17 | 同一个 GridWorld 的状态价值、动作价值与最优策略 }}

- 每个格子的一个数：$V^*(s)$。
- 每个格子按动作分区的数：$Q^*(s,a)$。
- 箭头：$\pi^*(s)$。

这个例子使用 noise $=0.2$、discount $=0.9$、living reward $=0$。这些条件共同决定图中的数值，不能与之前 living reward 为 $-0.1$ 的轨迹混用。

## 5.2 Recursive Return（回报的递归关系）

$$
\begin{aligned}
G_t
&=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots\\
&=R_{t+1}+\gamma G_{t+1}.
\end{aligned}
$$

这一步把整段未来分成两部分：**眼前奖励**，以及**下一时刻起的折扣回报**。

固定 $S_t=s$ 并取期望：

$$
V^\pi(s)
=\mathbb E_\pi[R_{t+1}+\gamma V^\pi(S_{t+1})\mid S_t=s].
$$

这里使用了条件期望与马尔可夫性：给定下一状态后，遵循固定策略的剩余期望回报可由 $V^\pi(S_{t+1})$ 表示。

## 5.3 Bellman Expectation Equations（贝尔曼期望方程）

### 5.3.1 State Value

$$
V^\pi(s)=
\sum_a\pi(a\mid s)
\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma V^\pi(s')\right].
$$

按以下顺序读公式：

1. **策略选动作**：用 $\pi(a\mid s)$ 对动作加权。
2. **环境作出响应**：用 $p(s',r\mid s,a)$ 对下一状态和奖励加权。
3. **计算这条分支的价值**：即时奖励 $r$ 加上 $\gamma V^\pi(s')$。

{{ slide lec05-06 21 | 两层随机性：策略选择动作，环境决定后果 }}

### 5.3.2 Action Value

$$
Q^\pi(s,a)=
\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma\sum_{a'}\pi(a'\mid s')Q^\pi(s',a')\right].
$$

当前动作 $a$ 已固定，所以最外层不再对当前动作求平均。下一状态的动作 $a'$ 仍由策略选择，因此内层需要对 $a'$ 求和。

### 5.3.3 Relating $V^\pi$ and $Q^\pi$

$$
V^\pi(s)=\sum_a\pi(a\mid s)Q^\pi(s,a),
$$

$$
Q^\pi(s,a)=\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma V^\pi(s')\right].
$$

两种价值函数不是两个独立的问题：从 $Q^\pi$ 对当前动作平均，可以得到 $V^\pi$；由 $V^\pi$ 做一步模型前瞻，可以得到 $Q^\pi$。

### 5.3.4 Backup Diagram（备份图）

{{ slide lec05-06 22 | Bellman backup：枚举所有一步后果并按概率加权 }}

图中从状态向下展开动作，再展开环境的随机后果。DP 的 full backup 会考虑所有可能的一步转移；后面的 MC 则使用采样得到的一条完整轨迹。

!!! example "笔记补充：沿用赛车模型读 Bellman 方程"

    固定策略为两个非终止态都选 Slow，则：

    $$
    \begin{aligned}
    V^\pi(C)&=1+\gamma V^\pi(C),\\
    V^\pi(W)&=\tfrac12[1+\gamma V^\pi(C)]
    +\tfrac12[1+\gamma V^\pi(W)].
    \end{aligned}
    $$

    Cool 的 Slow 是确定转移；Warm 的 Slow 有两种随机后果。固定动作并不意味着环境也变得确定。

## 5.4 Bellman Optimality Equations（贝尔曼最优方程）

定义：

$$
V^*(s)=\max_\pi V^\pi(s),\qquad
Q^*(s,a)=\max_\pi Q^\pi(s,a).
$$

最优状态价值满足：

$$
V^*(s)=
\max_a\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma V^*(s')\right].
$$

最优动作价值满足：

$$
Q^*(s,a)=
\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma\max_{a'}Q^*(s',a')\right].
$$

{{ slide lec05-06 30 | 从固定策略到最优策略：对动作的平均变为取最大值 }}

### 5.4.1 Expectation 与 Optimality 的区别

| 问题 | 对动作如何处理 | 对环境如何处理 |
| --- | --- | --- |
| 固定策略的价值 | 按 $\pi$ 加权平均 | 按转移概率加权平均 |
| 最优价值 | 选择价值最大的动作 | 仍按转移概率加权平均 |

!!! warning "只能选择动作，不能选择运气"

    $\max_a\mathbb E[\cdot\mid s,a]$ 一般不能换成 $\mathbb E[\max_a\cdot]$。
    赛车处于 Cool 时可以选 Fast，但不能指定这一次 Fast 必须仍然留在 Cool。

### 5.4.2 方程与解

- 固定策略的 Bellman 方程是一组线性方程。
- 最优方程包含 $\max$，一般是非线性方程组。
- 在有限状态、奖励有界且 $0\leq\gamma<1$ 的折扣设置下，分别存在唯一的 $V^\pi$ 与 $V^*$。
- $\gamma=1$ 的回合制情形需要额外的终止性条件；不要省略适用范围。

## 5.5 Policy Extraction（由价值提取策略）

若已经知道 $Q^*$：

$$
\pi^*(s)\in\arg\max_a Q^*(s,a).
$$

若只知道 $V^*$：

$$
\pi^*(s)\in\arg\max_a
\sum_{s'}T(s,a,s')
\left[R(s,a,s')+\gamma V^*(s')\right].
$$

两者的区别很关键：**仅有状态价值时，还需要模型来比较动作；动作价值已经把每个动作的后果合并进了数值。**

并列最优时，任选一个最大化动作，或在最大化动作之间分配概率，都可以形成最优策略。不能把每个并列动作的概率都赋为 1。

## 5.6 本章检查

- 是否能从 $G_t=R_{t+1}+\gamma G_{t+1}$ 推导 $V^\pi$ 的期望方程？
- $Q^\pi$ 为什么对下一动作求平均，却不对当前动作求平均？
- 最优方程中的最大化究竟作用于哪里？
- Bellman 方程与实际求解价值的迭代算法是什么关系？

??? success "参考答案"

    1. **从回报递归到期望方程**：先对给定 $S_t=s$ 的回报取条件期望，再按策略选择的动作、环境产生的后继状态与奖励展开。Markov 性使后续期望可写成 $V^\pi(s')$：

        $$
        \begin{aligned}
        V^\pi(s)
        &=\mathbb E_\pi[R_{t+1}+\gamma G_{t+1}\mid S_t=s]\\
        &=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)
        [r+\gamma V^\pi(s')].
        \end{aligned}
        $$

    2. **当前动作已固定**：$Q^\pi(s,a)$ 的条件中已经指定 $A_t=a$，因此不再对当前动作求平均。到达 $s'$ 后才恢复按策略 $\pi$ 行动，所以后续价值为 $\sum_{a'}\pi(a'\mid s')Q^\pi(s',a')$。
    3. **最大化的对象是可选择的动作**：在 $V^*$ 方程中，先算每个当前动作的期望，再在动作间取最大值：

        $$
        V^*(s)=\max_a\sum_{s',r}p(s',r\mid s,a)
        [r+\gamma V^*(s')].
        $$

        在 $Q^*$ 方程中，当前动作固定，最大化放在后继状态的动作上：

        $$
        Q^*(s,a)=\sum_{s',r}p(s',r\mid s,a)
        [r+\gamma\max_{a'}Q^*(s',a')].
        $$

        状态转移和奖励由环境产生，不能把对它们的期望替换为挑选最有利结果。
    4. **方程与算法**：Bellman 方程规定真实价值必须满足的不动点关系；迭代算法从初值出发，把右侧的后继价值换成当前估计，反复更新。固定策略的期望备份用于 Policy Evaluation，带最大化的备份用于 Value Iteration；满足相应收敛条件后，估计才趋于方程的解。
