# 8: Policy Iteration & Convergence

<p class="chapter-subtitle">策略迭代与收敛 · 评估之后，再改进</p>

!!! info "本章对应课件"

    <strong>ELEC6910J_Lec_7_8.pdf，p. 30–57</strong>，主题为 Policy Improvement、Policy Iteration 与 Convergence。原文件此处分节封面仍标为 Lecture 7，本站按主题顺序归入第 8 章。
    [查看全部原页](../slides/lecture-08.md) · [下载 PDF](../assets/pdf/ELEC6910J_Lec_7_8.pdf)

## 8.1 Policy Improvement（策略改进）

已经知道策略 $\pi$ 的价值 $V^\pi$。现在考虑：在状态 $s$ 先换一个动作 $a$，之后继续遵循旧策略，是否会更好？

$$
Q^\pi(s,a)=\sum_{s',r}p(s',r\mid s,a)
[r+\gamma V^\pi(s')].
$$

与原策略的价值比较：

- $Q^\pi(s,a)>V^\pi(s)$：先做动作 $a$ 更好。
- $Q^\pi(s,a)=V^\pi(s)$：期望回报相同。
- $Q^\pi(s,a)<V^\pi(s)$：这次替换更差。

{{ slide lec07-08 33 | 先试一次新动作，之后仍沿用旧策略，比较两种行为的价值 }}

### 8.1.1 Policy Improvement Theorem（策略改进定理）

在有限折扣 MDP 等适用条件下，若对所有状态都有：

$$
Q^\pi(s,\pi'(s))\geq V^\pi(s),
$$

则：

$$
V^{\pi'}(s)\geq V^\pi(s),\qquad\forall s.
$$

这说明：如果每个状态的一步替换都不差，把这些替换形成一个长期执行的新策略，也不会更差。

最直接的构造是对旧策略的 $Q^\pi$ 贪心：

$$
\pi'(s)\in\arg\max_a Q^\pi(s,a).
$$

这里虽然只向前看一步，但已经通过 $V^\pi(s')$ 纳入了后续长期回报，并非只比较即时奖励。

??? note "笔记补充：为什么一步改进能推广到长期？"

    从 $V^\pi\leq T^{\pi'}V^\pi$ 开始，反复应用保持序关系的 Bellman 期望算子：

    $$
    V^\pi\leq T^{\pi'}V^\pi\leq(T^{\pi'})^2V^\pi\leq\cdots.
    $$

    在折扣条件下，右侧收敛到 $V^{\pi'}$，于是得到策略改进结论。

## 8.2 Policy Iteration（策略迭代）

交替执行两个阶段：

1. **Evaluation**：固定当前策略 $\pi_i$，求 $V^{\pi_i}$。
2. **Improvement**：用这个价值做一步前瞻，得到贪心策略 $\pi_{i+1}$。

$$
\pi_{i+1}(s)\in\arg\max_a
\sum_{s',r}p(s',r\mid s,a)
[r+\gamma V^{\pi_i}(s')].
$$

当策略不再改变时停止。有限 MDP 中，精确评估与一致的并列处理规则可使策略迭代在有限次改进后到达最优策略。

~~~text
initialize a policy π
repeat:
    V = evaluate(π)
    stable = true
    for each non-terminal state s:
        old_action = π(s)
        π(s) = greedy action using R + γ V
        if π(s) differs from old_action:
            stable = false
until stable
~~~

!!! tip "并列动作的处理"

    若旧动作仍属于最大化动作，可保留旧动作，避免在同样好的动作之间来回切换。这不会妨碍达到最优价值。

## 8.3 赛车的策略迭代 {#racing-policy-iteration}

原课件设 $\gamma=0.5$，初始策略在 Cool 与 Warm 都选择 Slow。

### 8.3.1 评估初始策略

$$
V^{\pi_0}(C)=1+0.5V^{\pi_0}(C)\quad\Rightarrow\quad V^{\pi_0}(C)=2,
$$

$$
V^{\pi_0}(W)
=0.5[1+0.5\times2]+0.5[1+0.5V^{\pi_0}(W)]
\quad\Rightarrow\quad V^{\pi_0}(W)=2.
$$

### 8.3.2 改进策略

| 状态 | Slow 的一步前瞻 | Fast 的一步前瞻 | 新动作 |
| --- | ---: | ---: | --- |
| Cool | $1+0.5\times2=2$ | $0.5(2+1)+0.5(2+1)=3$ | Fast |
| Warm | $0.5(1+1)+0.5(1+1)=2$ | $-10$ | Slow |

{{ slide lec07-08 43 | 从“总是 Slow”开始，评估后把 Cool 的动作改为 Fast }}

### 8.3.3 再评估、再检查

新策略为 Cool / Fast、Warm / Slow：

$$
\begin{aligned}
V^{\pi_1}(C)&=2+0.25V^{\pi_1}(C)+0.25V^{\pi_1}(W),\\
V^{\pi_1}(W)&=1+0.25V^{\pi_1}(C)+0.25V^{\pi_1}(W).
\end{aligned}
$$

相减得到 $V^{\pi_1}(C)-V^{\pi_1}(W)=1$，解得：

$$
V^{\pi_1}(C)=3.5,\qquad V^{\pi_1}(W)=2.5.
$$

再做一步前瞻：Cool 下 Slow 为 $2.75$、Fast 为 $3.5$；Warm 下 Slow 为 $2.5$、Fast 为 $-10$。策略不变，达到最优。

{{ slide lec07-08 44 | 第二次评估与改进检查：策略保持不变 }}

## 8.4 Convergence（收敛）

### 8.4.1 Value Function Space 与无穷范数

有限状态 MDP 的价值函数可以看作一个 $|\mathcal S|$ 维向量。两个价值函数之间的距离用：

$$
\|u-v\|_\infty=\max_s|u(s)-v(s)|.
$$

它关注所有状态中最大的误差。

### 8.4.2 Bellman Operators（贝尔曼算子）

定义期望算子：

$$
(T^\pi v)(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)
[r+\gamma v(s')],
$$

定义最优算子：

$$
(T^*v)(s)=\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma v(s')].
$$

在 $0\leq\gamma<1$ 时，它们都是 $\gamma$-contraction（压缩映射）：

$$
\|T^\pi u-T^\pi v\|_\infty\leq\gamma\|u-v\|_\infty,
$$

$$
\|T^*u-T^*v\|_\infty\leq\gamma\|u-v\|_\infty.
$$

{{ slide lec07-08 50 | Bellman 最优算子的压缩性质 }}

### 8.4.3 Fixed Point（不动点）

在完备度量空间上，压缩映射有唯一不动点，反复应用算子会收敛到该点。因此：

- $V^\pi=T^\pi V^\pi$：迭代策略评估收敛到 $V^\pi$。
- $V^*=T^*V^*$：价值迭代收敛到 $V^*$。
- 误差满足 $\|V_k-V^*\|_\infty\leq\gamma^k\|V_0-V^*\|_\infty$。
- $\gamma$ 越接近 1，这个理论误差界缩小得越慢。

!!! warning "压缩结论需要严格小于 1"

    $\gamma=1$ 时，上式最多给出不扩张，不能直接应用压缩映射定理。4×4 GridWorld 的随机策略评估能收敛，依赖其终止结构；它不是 $\gamma<1$ 定理的直接应用。

## 8.5 Value Iteration vs. Policy Iteration

| 对比 | Value Iteration | Policy Iteration |
| --- | --- | --- |
| 每轮工作 | 一次最优性备份 | 策略评估，再策略改进 |
| 策略处理 | 在 $\max$ 中隐式更新 | 显式维护策略 |
| 评估精度 | 通常只做一轮价值更新 | 经典形式评估到收敛 |
| 主要开销 | 每轮遍历所有动作 | 多轮评估与一次全动作改进 |
| 目标 | 求最优价值及其策略 | 求最优策略及其价值 |

两种方法都需要模型。课件最后提出下一步：如果不知道 $T$ 与 $R$，就从交互经验出发，用**采样回报的平均值**代替模型下的期望。这引出 Monte Carlo 方法。

## 8.6 本章检查

- 策略改进为什么比较的是 $Q^\pi$，而不要求事先知道 $Q^*$？
- 能否复算赛车从 $(2,2)$ 到 $(3.5,2.5)$ 的过程？
- 策略稳定与价值数值稳定是什么关系？
- 压缩映射结论使用了哪些前提？
