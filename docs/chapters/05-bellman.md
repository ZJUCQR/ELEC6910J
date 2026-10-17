# 5: Value Functions & Bellman Equations

<p class="chapter-subtitle">价值函数与贝尔曼方程 · 把未来拆成一步</p>

**主要内容**：State Value、Action Value、两种价值的关系、Backup Diagram、Bellman 期望与最优方程，以及策略提取。

## 5.1 Value Functions（价值函数）

价值函数衡量在给定策略下，一个状态或状态—动作对有多好。这里的“好”由**未来累计奖励的期望**定义。

**State Value · 状态价值**：站在状态 $s$，从现在开始一直按策略 $\pi$ 行动，平均能获得多少折扣回报？

$$
V^\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]
=\mathbb E_\pi\!\left[\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}\mid S_t=s\right].
$$

**Action Value · 动作价值**：站在状态 $s$，先执行指定动作 $a$，此后一直按策略 $\pi$ 行动，平均能获得多少折扣回报？

$$
Q^\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]
=\mathbb E_\pi\!\left[\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}\mid S_t=s,A_t=a\right].
$$

| 比较 | $V^\pi(s)$ | $Q^\pi(s,a)$ |
| --- | --- | --- |
| 已经指定什么 | 当前状态 $s$ | 当前状态 $s$ 与当前动作 $a$ |
| 当前动作怎样产生 | 按 $\pi(a\mid s)$ 选择 | 固定为给定的 $a$ |
| 下一步起怎样行动 | 按 $\pi$ | 按 $\pi$ |
| 表格中保存什么 | 每个状态一个值 | 每个可行动作对应一个值 |

两者都包含本步奖励与后续回报。$Q^\pi(s,a)$ 中固定当前动作，并不会固定环境的转移结果；环境仍可能把同一个动作带到不同的下一状态。即使策略 $\pi$ 在 $s$ 不选择 $a$，也可以评价“先执行一次 $a$，再遵循 $\pi$”的价值。

上标 $\pi$ 表示回报取决于后续如何行动：同一状态在不同策略下可能有不同的价值。一次实际轨迹得到的是 $G_t$，$V^\pi$ 与 $Q^\pi$ 则对所有可能的相关轨迹取期望。

终止态没有后续奖励，因此 $V^\pi(s_{\mathrm{terminal}})=0$。进入终止态的奖励已计入前一次转移；回合制任务的回报求和在终止时结束。

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

从回报递归式出发，先固定当前状态，再展开当前动作与环境结果：

$$
\begin{aligned}
V^\pi(s)
&=\mathbb E_\pi[R_{t+1}+\gamma G_{t+1}\mid S_t=s]\\
&=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma V^\pi(s')\right].
\end{aligned}
$$

其中 $p(s',r\mid s,a)=P(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a)$，描述下一状态与奖励的联合分布。

按以下顺序读公式：

1. **策略选动作**：用 $\pi(a\mid s)$ 对动作加权。
2. **环境作出响应**：用 $p(s',r\mid s,a)$ 对下一状态和奖励加权。
3. **计算这条分支的价值**：即时奖励 $r$ 加上 $\gamma V^\pi(s')$。

因此，一条完整分支 $(a,s',r)$ 的概率是 $\pi(a\mid s)p(s',r\mid s,a)$，分支值是 $r+\gamma V^\pi(s')$。将“概率 × 分支值”相加，就是全期望公式的展开。式中的 $s'$ 和 $r$ 随环境变化，$\pi$ 决定对哪些动作赋予多大权重。

如果策略是确定性的，只有 $a=\pi(s)$ 的概率为 1，外层动作求和消失：

$$
V^\pi(s)=\sum_{s',r}p(s',r\mid s,\pi(s))
\left[r+\gamma V^\pi(s')\right].
$$

当题目提供转移表 $T(s,a,s')$ 和该转移的奖励或条件期望奖励 $R(s,a,s')$ 时，同一方程可以写成：

$$
V^\pi(s)=\sum_a\pi(a\mid s)\sum_{s'}T(s,a,s')
\left[R(s,a,s')+\gamma V^\pi(s')\right].
$$

{{ slide lec05-06 21 | 两层随机性：策略选择动作，环境决定后果 }}

### 5.3.2 Action Value

这次同时固定 $S_t=s$ 与 $A_t=a$，下一时刻的动作 $A_{t+1}$ 才由策略产生：

$$
\begin{aligned}
Q^\pi(s,a)
&=\mathbb E_\pi[R_{t+1}+\gamma G_{t+1}\mid S_t=s,A_t=a]\\
&=\mathbb E_\pi[R_{t+1}+\gamma Q^\pi(S_{t+1},A_{t+1})\mid S_t=s,A_t=a].
\end{aligned}
$$

先枚举环境产生的 $(s',r)$，再枚举到达 $s'$ 后可能选择的动作 $a'$：

$$
Q^\pi(s,a)=
\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma\sum_{a'}\pi(a'\mid s')Q^\pi(s',a')\right].
$$

当前动作 $a$ 已固定，所以最外层不再对当前动作求平均。下一状态的动作 $a'$ 仍由策略选择，因此内层需要对 $a'$ 求和。

手算时可以从内向外做：

1. 对每个 $s'$，先算 $\sum_{a'}\pi(a'\mid s')Q^\pi(s',a')$，得到到达该状态后按策略行动的价值。
2. 乘 $\gamma$，再加这次转移的奖励 $r$。
3. 用 $p(s',r\mid s,a)$ 对环境的所有结果加权相加。

如果后续策略是确定性的，内层平均化为 $Q^\pi(s',\pi(s'))$。这里计算的始终是“当前做 $a$，以后跟随 $\pi$”；把内层换成 $\max_{a'}$，就改变了后续行为的含义。

### 5.3.3 Relating $V^\pi$ and $Q^\pi$

**由 $Q^\pi$ 得到 $V^\pi$：按当前策略对动作价值加权。**

$$
V^\pi(s)=\sum_a\pi(a\mid s)Q^\pi(s,a),
$$

例如，同一策略下 $Q^\pi(s,a_1)=2$、$Q^\pi(s,a_2)=6$，并且 $\pi(a_1\mid s)=0.75$、$\pi(a_2\mid s)=0.25$，则：

$$
V^\pi(s)=0.75\times2+0.25\times6=3.
$$

这里的 3 是跟随该策略的平均价值。确定性策略满足 $V^\pi(s)=Q^\pi(s,\pi(s))$；只有当策略把概率全部分配给当前最大的 $Q^\pi$ 动作时，这个平均才等于 $\max_a Q^\pi(s,a)$。

**由 $V^\pi$ 得到 $Q^\pi$：固定动作，做一步环境前瞻。**

$$
Q^\pi(s,a)=\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma V^\pi(s')\right].
$$

计算时需要该动作的奖励与转移模型。把这个式子代入 $V^\pi=\sum_a\pi Q^\pi$，得到 State Value 的 Bellman 方程；反过来，把 $V^\pi(s')=\sum_{a'}\pi(a'\mid s')Q^\pi(s',a')$ 代入上式，得到 Action Value 的 Bellman 方程。

| 转换方向 | 合并哪些分支 | 需要的信息 |
| --- | --- | --- |
| $Q^\pi\to V^\pi$ | 当前状态的各个动作 | $Q^\pi$ 与策略 $\pi$ |
| $V^\pi\to Q^\pi$ | 固定动作后的环境结果 | $V^\pi$ 与转移、奖励模型 |

**赛车例子：当前动作与后续策略分开看。** 令策略 $\pi$ 在 Cool、Warm 都选 Slow，且 $\gamma=0.5$。以后每步都获得 $+1$，所以：

$$
V^\pi(C)=V^\pi(W)=1+0.5+0.5^2+\cdots=2.
$$

使用[赛车转移表](04-mdp.md#racing)，先做一次指定动作，再恢复 Slow：

$$
\begin{aligned}
Q^\pi(C,\mathrm{Slow})&=1+0.5\times2=2,\\
Q^\pi(C,\mathrm{Fast})&=0.5(2+0.5\times2)+0.5(2+0.5\times2)=3,\\
Q^\pi(W,\mathrm{Slow})&=0.5(1+0.5\times2)+0.5(1+0.5\times2)=2,\\
Q^\pi(W,\mathrm{Fast})&=-10+0.5\times0=-10.
\end{aligned}
$$

虽然 $Q^\pi(C,\mathrm{Fast})=3$ 更大，原策略仍在 Cool 选择 Slow，因此 $V^\pi(C)=1\times2+0\times3=2$。数值 3 评价的是“这一步 Fast、以后 Slow”；把后续策略也改为最优策略后，价值还会变化。

### 5.3.4 Backup Diagram（备份图）

Backup 表示把后继的价值信息向当前节点回传。读图时**从上往下展开可能性，从下往上合并价值**；叶子上的价值概括剩余未来，无需把整条无限轨迹画出来。

| 图中元素 | 含义 | 对应计算 |
| --- | --- | --- |
| 空心圆 $s$、$s'$ | 状态节点 | 值为 $V$；展开该状态可选择的动作 |
| 实心圆 $(s,a)$、$(s',a')$ | 状态—动作节点 | 值为 $Q$；展开执行该动作后的环境结果 |
| 状态 → 动作 | 策略选择 | 期望方程按 $\pi$ 加权；最优方程取最大值 |
| 动作 → 下一状态 | 环境转移，并产生奖励 $r$ | 按 $p$ 加权，对分支计算 $r+\gamma V(s')$ |

**State Value backup：$s\to(s,a)\to s'$。**

{{ slide lec05-06 22 | Bellman backup：枚举所有一步后果并按概率加权 }}

根节点是状态 $s$。先把每个动作下的环境分支合并为 $Q^\pi(s,a)$，再按 $\pi(a\mid s)$ 合并各个动作，回传到根节点 $V^\pi(s)$。

**Action Value backup：$(s,a)\to s'\to(s',a')$。**

{{ slide lec05-06 25 | Action Value backup：先展开环境结果，再展开下一状态的动作 }}

根节点已包含当前动作 $a$。先在每个后继状态 $s'$ 下按策略合并 $Q^\pi(s',a')$，得到 $V^\pi(s')$；将后续价值乘 $\gamma$ 并加上本步奖励，再按环境概率合并，回传到根节点 $Q^\pi(s,a)$。

图的两层边只展开了一次环境转移：选择动作本身不会额外增加一个折扣因子，因此公式只有一个 $\gamma$。图中叶子即使没有继续展开，也可能是非终止状态，仍要使用其后续价值。

DP 的 **full backup** 枚举全部一步分支并使用后继价值；TD 使用实际采到的一步转移与后继价值；MC 使用完整回合的实际回报。使用当前价值估计构造更新目标称为 **bootstrapping（自举）**，DP 与 TD 都采用这一做法。

## 5.4 Bellman Optimality Equations（贝尔曼最优方程）

定义：

$$
V^*(s)=\max_\pi V^\pi(s),\qquad
Q^*(s,a)=\max_\pi Q^\pi(s,a).
$$

$V^*(s)$ 允许从当前时刻起最优行动；$Q^*(s,a)$ 的第一步仍固定为 $a$，从下一步起最优行动。两者满足：

$$
V^*(s)=\max_a Q^*(s,a),\qquad
Q^*(s,a)=\sum_{s',r}p(s',r\mid s,a)[r+\gamma V^*(s')].
$$

**最优状态价值：先求每个动作的期望，再挑最大的动作。** 将第二式代入第一式，得到：

$$
V^*(s)=
\max_a\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma V^*(s')\right].
$$

**最优动作价值：当前动作固定，到达下一状态后再选最佳动作。** 将 $V^*(s')=\max_{a'}Q^*(s',a')$ 代入，得到：

$$
Q^*(s,a)=
\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma\max_{a'}Q^*(s',a')\right].
$$

在 $V^*$ 方程中，当前动作在观察下一状态前选择，所以 $\max_a$ 放在环境求和外面。在 $Q^*$ 方程中，到达 $s'$ 后才选择下一动作，所以 $\max_{a'}$ 放在每个后继状态对应的分支内；不同 $s'$ 可以选择不同的最佳动作。

如果题目使用 $T$、$R$ 记号，同样可以写成：

$$
\begin{aligned}
V^*(s)&=\max_a\sum_{s'}T(s,a,s')[R(s,a,s')+\gamma V^*(s')],\\
Q^*(s,a)&=\sum_{s'}T(s,a,s')\left[R(s,a,s')+\gamma\max_{a'}Q^*(s',a')\right].
\end{aligned}
$$

{{ slide lec05-06 30 | 从固定策略到最优策略：对动作的平均变为取最大值 }}

### 5.4.1 Expectation 与 Optimality 的区别

| 问题 | 对动作如何处理 | 对环境如何处理 |
| --- | --- | --- |
| 固定策略的价值 | 按 $\pi$ 加权平均 | 按转移概率加权平均 |
| 最优价值 | 选择价值最大的动作 | 仍按转移概率加权平均 |

从 Backup Diagram 看，改变的是**状态节点到动作节点**的合并方式；动作节点到后继状态节点仍按环境概率求期望。当前动作、奖励和后继状态的位置不变。

因此，$\max_a\mathbb E[\cdot\mid s,a]$ 一般不能换成 $\mathbb E[\max_a\cdot]$。赛车处于 Cool 时可以选 Fast，但 Cool 与 Warm 两条环境分支仍需按概率相加。

### 5.4.2 方程与解

- 固定策略的 Bellman 方程是一组线性方程。
- 最优方程包含 $\max$，一般是非线性方程组。
- 在有限状态、奖励有界且 $0\leq\gamma<1$ 的折扣设置下，分别存在唯一的 $V^\pi$ 与 $V^*$。
- $\gamma=1$ 的回合制情形需要额外的终止性条件；不要省略适用范围。

把 Bellman 方程的右侧看作作用于价值函数的算子，固定策略的算子记为 $T^\pi$，最优算子记为 $T^*$。这里的 $T^\pi,T^*$ 是完整的备份操作，与转移概率 $T(s,a,s')$ 区分：

$$
V^\pi=T^\pi V^\pi,\qquad V^*=T^*V^*.
$$

这是价值函数应满足的不动点方程。实际计算时从估计 $V_k$ 出发，用 $V_{k+1}=T^\pi V_k$ 做固定策略评估，或用 $V_{k+1}=T^*V_k$ 做 Value Iteration。一次更新的结果通常还没有达到方程的解。

### 5.4.3 赛车：把最优方程写成两个状态的联立关系

沿用 $\gamma=0.5$，Overheated 为终止态且价值为 0。每个状态分别比较 Slow 与 Fast：

$$
\begin{aligned}
V^*(C)&=\max\left\{
\underbrace{1+0.5V^*(C)}_{\mathrm{Slow}},\;
\underbrace{2+0.25V^*(C)+0.25V^*(W)}_{\mathrm{Fast}}
\right\},\\
V^*(W)&=\max\left\{
\underbrace{1+0.25V^*(C)+0.25V^*(W)}_{\mathrm{Slow}},\;
\underbrace{-10}_{\mathrm{Fast}}
\right\}.
\end{aligned}
$$

尝试策略 Cool / Fast、Warm / Slow，对应的两个等式为：

$$
\begin{aligned}
v_C&=2+0.25v_C+0.25v_W,\\
v_W&=1+0.25v_C+0.25v_W.
\end{aligned}
$$

两式相减得 $v_C-v_W=1$，代回可得 $v_C=3.5$、$v_W=2.5$。再检查这组值是否使所选动作达到最大：

| 状态 | Slow 的一步期望 | Fast 的一步期望 | 最大值对应动作 |
| --- | --- | --- | --- |
| Cool | $1+0.5\times3.5=2.75$ | $2+0.25\times3.5+0.25\times2.5=3.5$ | Fast |
| Warm | $1+0.25\times3.5+0.25\times2.5=2.5$ | $-10$ | Slow |

所选动作确实在各自状态取到最大值，因此这组值满足 Bellman 最优方程：$V^*(C)=3.5$、$V^*(W)=2.5$。表中的四个动作值就是相应的 $Q^*$。

前面“以后都 Slow”时 $Q^\pi(C,\mathrm{Fast})=3$；这里 $Q^*(C,\mathrm{Fast})=3.5$，增加的价值来自后续采用更好的策略。

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
