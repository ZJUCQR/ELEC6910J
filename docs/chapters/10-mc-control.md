# 10: Monte-Carlo Control

<p class="chapter-subtitle">蒙特卡洛控制 · 一边探索，一边改进策略</p>

!!! info "本章对应课件"

    Lecture 10 · <strong>ELEC6910J_Lec_9_10.pdf，p. 24–41</strong>。
    [查看本讲全部课件](../slides/lecture-10.md) · [下载 PDF](../assets/pdf/ELEC6910J_Lec_9_10.pdf)

## 10.1 From Prediction to Control

Prediction 给定策略并估计其价值；Control 还要根据价值改善策略。

Monte Carlo 版本沿用策略迭代的结构：

1. 根据当前策略采集 episode。
2. 使用实际回报估计 $Q^\pi(s,a)$。
3. 根据估计的动作价值改进策略。
4. 继续采集经验并更新。

$$
\pi(s)\in\arg\max_a Q(s,a).
$$

这里使用 $Q$，是因为没有模型时不方便从 $V$ 做一步前瞻。实际算法通常让估计和改进交替进行，不会在每次改进前采集无穷多回合来得到精确 $Q^\pi$。

## 10.2 Monte Carlo with Exploring Starts（MC ES）

ES 假设所有相关状态—动作对都有机会成为回合起点。即使后续策略是确定性的，也能通过起点随机性探索不同动作。

{{ slide lec09-10 26 | MC Exploring Starts：随机选择起始状态—动作对，再评估与改进 }}

基本算法：

~~~text
initialize Q(s,a), counts N(s,a), and policy π
repeat:
    choose a starting pair (S0,A0), with coverage of all relevant pairs
    generate a complete episode; follow π after the first action
    compute every return G_t
    for each first visit to (S_t,A_t) in this episode:
        increment N(S_t,A_t)
        Q(S_t,A_t) += [G_t - Q(S_t,A_t)] / N(S_t,A_t)
        π(S_t) = a greedy action under Q(S_t,·)
~~~

!!! warning "ES 的现实限制"

    它要求能够把环境从不同状态—动作对启动。很多实际任务没有这种重置能力，因此不能把 ES 当作默认可用的机制。持续探索可以由策略本身来实现。

## 10.3 On-policy & Off-policy（同策略与异策略）

- On-policy：评估或改进的策略，就是用于产生数据的策略。
- Off-policy：评估或改进的目标策略，与生成数据的行为策略不同。

本讲主要讨论 on-policy soft-policy MC。课件引入了 off-policy 的概念，但没有展开 importance sampling 等具体推导，本章保持这一范围。

## 10.4 Soft Policies（软策略） {#soft-policies}

### 10.4.1 Soft 与 $\epsilon$-Soft

Soft Policy：对每个可用动作都给出正概率：

$$
\pi(a\mid s)>0.
$$

$\epsilon$-Soft Policy：为每个动作规定更明确的概率下界：

$$
\pi(a\mid s)\geq\frac{\epsilon}{|\mathcal A(s)|},
\qquad 0<\epsilon\leq1.
$$

原课件 p. 30 的一处符号写成严格大于；按照前页定义及 $\epsilon$-greedy 的边界取值，应使用大于等于。

### 10.4.2 $\epsilon$-Greedy

若有一个指定的贪心动作 $a^*$，令 $m=|\mathcal A(s)|$：

$$
\pi(a\mid s)=
\begin{cases}
1-\epsilon+\epsilon/m,&a=a^*,\\
\epsilon/m,&a\ne a^*.
\end{cases}
$$

如果有多个并列最优动作，可以将剩余的 $1-\epsilon$ 在它们之间分配，保证总概率为 1。

理解为两部分：

- $\epsilon$ 的概率质量用于均匀探索。
- $1-\epsilon$ 的概率质量可以自由分配；$\epsilon$-greedy 把它全部用于最大化动作。

{{ slide lec09-10 30 | epsilon-soft 的概率预算：均匀探索与动作偏好 }}

!!! example "笔记补充：两个动作的 Blackjack"

    若 $\epsilon=0.1$，当前估计 Hit 更好，则
    $\pi(\mathrm{Hit}\mid s)=0.95$，
    $\pi(\mathrm{Stick}\mid s)=0.05$。
    这样即使目前偏好 Hit，仍会继续收集 Stick 的结果。

### 10.4.3 为什么能改进 $\epsilon$-Soft 策略？

令 $q_a=Q^\pi(s,a)$。任何 $\epsilon$-soft 策略都可以写成：

$$
\pi(a\mid s)=\frac\epsilon m+(1-\epsilon)\bar\pi(a\mid s),
$$

其中 $\bar\pi$ 是一个概率分布（$\epsilon=1$ 时直接退化为均匀策略）。于是：

$$
\begin{aligned}
V^\pi(s)
&=\frac\epsilon m\sum_aq_a
+(1-\epsilon)\sum_a\bar\pi(a\mid s)q_a\\
&\leq\frac\epsilon m\sum_aq_a+(1-\epsilon)\max_aq_a.
\end{aligned}
$$

右侧就是对 $Q^\pi$ 采用 $\epsilon$-greedy 的一步价值。再应用策略改进定理，得到不差于原策略的结论。

### 10.4.4 On-policy MC Control

算法结构与 MC ES 类似，但：

- 回合按照当前 $\epsilon$-soft 策略生成。
- 每次根据回报更新 $Q$。
- 改进为相对于 $Q$ 的 $\epsilon$-greedy 策略，保留探索。

{{ slide lec09-10 31 | Soft-policy MC control：改进为 epsilon-greedy，而非完全贪心 }}

!!! note "最优性的范围"

    固定 $\epsilon>0$ 时，即使估计充分准确，也受到持续探索的约束，目标是相应策略类中的最好表现，不应直接等同于无约束的确定性最优策略。实际采样算法还需要相关状态可达、充分访问和合适的更新条件；“动作概率为正”本身不能保证所有状态都会被访问。

## 10.5 Blackjack（二十一点） {#blackjack}

### 10.5.1 Rules（原课件规则）

- 目标：牌面点数和尽可能大，但不能超过 21。
- J、Q、K 计为 10。
- Ace 可计为 1 或 11。
- Hit：继续要牌。
- Stick：停止要牌，轮到庄家。
- 爆牌即输；庄家在点数至少为 17 时停牌，否则继续要牌。

{{ slide lec09-10 34 | Blackjack：玩家的两个动作与庄家的固定策略 }}

### 10.5.2 State Representation（状态表示）

课件的简化状态包含：

| 分量 | 取值数 | 范围 |
| --- | ---: | --- |
| 玩家点数和 | 10 | 12–21 |
| 庄家明牌 | 10 | Ace、2–10 |
| Usable Ace | 2 | 有／无可按 11 计且不爆牌的 Ace |

因此有 $10\times10\times2=200$ 个决策状态。

低于 12 时不会因为再要一张牌而爆牌，课件模型把这一阶段作为自动要牌处理。是否存在 usable ace 会影响后续风险，因此不能仅用玩家点数与庄家明牌表示状态。

{{ slide lec09-10 35 | 200 个状态：玩家点数、庄家明牌与可用 Ace }}

!!! note "模型约定"

    这是课件采用的简化 episodic MDP。若使用有限牌堆并让已出现的牌影响未来发牌概率，就需要考虑剩余牌信息；不能直接假定三元组仍是完整状态。

### 10.5.3 Rewards & Returns

- 一局游戏就是一个 episode。
- 胜、负、平的终局奖励分别是 $+1,-1,0$。
- 中间奖励均为 0。
- $\gamma=1$，因此本局任一决策时刻的回报就是终局奖励。

例如，某状态在不同回合首次出现后的结果分别为赢、输、赢，其样本价值为 $(1-1+1)/3=1/3$。这一数值是平均收益，不是直接的胜率，因为输局也贡献 $-1$。

### 10.5.4 先评估一个固定策略

课件给定策略：点数为 20 或 21 时 Stick，否则 Hit。

1. 按该策略模拟很多局。
2. 记录每个状态出现后的终局收益。
3. 按状态平均，得到该策略的价值函数。
4. 将 usable ace 与无 usable ace 的情形分开观察。

{{ slide lec09-10 36 | 固定 Blackjack 策略的 MC 评估：更多回合使估计更稳定 }}

这张图展示的是**固定策略的预测**。若要做控制，则要估计两个动作各自的 $Q(s,a)$，再用 $\epsilon$-greedy 持续改进；不要把这张固定策略图误读成已经求得最优控制策略。

## 10.6 Dynamic Programming vs. Monte Carlo

| 特性 | DP | MC |
| --- | --- | --- |
| 是否需要模型 | 需要转移与奖励模型 | 只需经验 |
| 备份范围 | 所有一步后继 | 一条采样轨迹直到终止 |
| 更新目标 | 模型期望中的 $r+\gamma V(s')$ | 实际回报 $G_t$ |
| Bootstrapping | 使用已有价值估计 | 不使用 |
| 是否要等回合结束 | 不需要 | 标准 episodic MC 需要 |
| 主要限制 | 模型和枚举开销 | 采样方差、回合长度和覆盖 |

{{ slide lec09-10 38 | DP 与 MC：模型期望和样本回报的两种估计路径 }}

## 10.7 本章检查

- ES 和 soft policy 分别在哪个环节提供探索？
- $\epsilon$-soft 是否都属于 $\epsilon$-greedy？不是，前者是更大的策略类。
- 为什么 $\epsilon$-soft 的概率下界必须允许等号？
- Blackjack 中 $V^\pi(s)$ 是胜率，还是胜负奖励的期望？
- 如果不想等回合结束才学习，怎样用后继价值构造更新目标？下一章进入 [TD Prediction](11-td-prediction.md)。
