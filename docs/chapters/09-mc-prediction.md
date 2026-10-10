# 9: Monte-Carlo Prediction

<p class="chapter-subtitle">蒙特卡洛预测 · 从完整经历估计价值</p>

**主要内容**：轨迹回报、首次访问与每次访问 MC、增量更新及动作价值估计。

## 9.1 From Models to Experience（从模型到经验）

DP 根据已知转移概率与奖励计算期望。实际环境中，这些模型往往未知，但可以运行策略、观察轨迹。

Monte Carlo（MC，蒙特卡洛）用经验均值估计期望：

$$
V^\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]
\quad\longrightarrow\quad
V(s)=\text{从 }s\text{ 出发的样本回报的平均值}.
$$

基本过程：

1. 固定待评估策略 $\pi$。
2. 按该策略生成完整 episode。
3. 回合结束后，计算访问各状态之后的回报。
4. 对对应状态的回报取平均。

标准 episodic MC 不要求知道 $T$ 和 $R$，但需要回合终止，才能得到完整回报。

## 9.2 Returns from a Trajectory（轨迹中的回报）

采用统一的奖励下标：

$$
S_0,A_0,R_1,S_1,A_1,R_2,\ldots,S_T.
$$

$$
G_t=\sum_{k=0}^{T-t-1}\gamma^kR_{t+k+1},\qquad G_T=0.
$$

可以从后向前递推 $G_t=R_{t+1}+\gamma G_{t+1}$。这里使用的是**本次真实观察到的奖励**，不是其他状态的估计价值。

## 9.3 First-Visit vs. Every-Visit（首次访问与每次访问） {#first-every}

同一回合可能多次进入状态 $s$。

- First-Visit MC：每个回合只使用**第一次**访问 $s$ 之后的回报。
- Every-Visit MC：使用该回合中**每次**访问 $s$ 之后的回报。
- “第一次”的范围是**当前回合**，不是训练过程中的第一次。

### 9.3.1 原课件例题：重复访问同一状态

课件中目标状态在 $t=1$ 与 $t=2$ 被访问，$t=3$ 结束：

$$
G_1=r_2+\gamma r_3,\qquad G_2=r_3,\qquad G_3=0.
$$

{{ slide lec09-10 14 | 同一回合重复访问状态：首次访问与每次访问使用不同样本集合 }}

首次访问只收集 $[G_1]$：

$$
V_{\mathrm{first}}(s)=r_2+\gamma r_3.
$$

每次访问收集 $[G_1,G_2]$：

$$
V_{\mathrm{every}}(s)
=\frac{G_1+G_2}{2}
=\frac{r_2+(1+\gamma)r_3}{2}.
$$

!!! note "原页公式核对"

    原页最后把分子写成了 $r_2+2\gamma r_3$。由其上方给出的 $G_1$ 与 $G_2$ 相加，一般应为 $r_2+(1+\gamma)r_3$；当 $\gamma=1$ 时两种写法才一致。截图保留原样，笔记使用展开后的表达式。

!!! example "笔记补充：代入数值"

    取 $r_2=2,r_3=4,\gamma=0.5$，则 $G_1=4$、$G_2=4$。
    First-Visit 和 Every-Visit 本回合都给出 4。
    若改为 $\gamma=1$，则首次访问为 6，每次访问平均为 $(6+4)/2=5$。

## 9.4 Incremental MC（增量更新）

无需保存全部历史回报，只需计数和均值：

$$
N(s)\leftarrow N(s)+1,
$$

$$
V(s)\leftarrow V(s)+\frac1{N(s)}[G-V(s)].
$$

这与 Bandit 的增量样本平均形式相同，只是目标从**即时奖励**换成了**整个回报**。

若希望更重视近期样本，可使用固定步长：

$$
V(s)\leftarrow V(s)+\alpha[G-V(s)].
$$

固定步长适合追踪变化，但不再是对所有历史样本的等权平均。

### 9.4.1 First-Visit 的实现顺序

下面把回报计算与访问判断分开，避免倒序遍历时把“最后一次访问”误当作“首次访问”。

~~~python
def first_visit_update(states, rewards, gamma, values, counts):
    # states includes the terminal state; rewards[t] is R_(t+1).
    returns = [0.0] * len(rewards)
    G = 0.0
    for t in reversed(range(len(rewards))):
        G = rewards[t] + gamma * G
        returns[t] = G

    seen = set()
    for t, state in enumerate(states[:-1]):
        if state in seen:
            continue
        seen.add(state)
        counts[state] = counts.get(state, 0) + 1
        old = values.get(state, 0.0)
        values[state] = old + (returns[t] - old) / counts[state]
~~~

这里假定 values 与 counts 跨回合保留，而 seen 每个回合重新创建。若去掉 seen 的判断与记录，就得到 Every-Visit 更新。

## 9.5 Statistical Properties（统计性质）

在固定策略、适当的终止与可访问性条件下，访问次数增加时，两类方法都能一致估计 $V^\pi$。

- First-Visit：独立生成的回合可提供独立同分布的首次访问回报。
- 若这些回报的方差为 $\sigma^2$，$n$ 个独立回报的样本均值方差为 $\sigma^2/n$。
- 标准误差随 $1/\sqrt n$ 缩小。把标准误差减半，通常需要约 4 倍样本。
- Every-Visit 的同一回合内多个回报通常相关，不能把它们直接当作相互独立的样本。

!!! note "关于课件 p. 21 的 convergence 表述"

    原页使用了“converge quadratically”。这里不把它理解为数值优化中的二次收敛。对独立、有限方差回报的普通样本平均，应区分均方误差的 $O(1/n)$ 与标准误差的 $O(1/\sqrt n)$；p. 17 的标准差表述与后者一致。

## 9.6 Backup & Bootstrapping（备份与自举）

{{ slide lec09-10 18 | MC 与 DP 的备份图：完整样本轨迹与一步全分支期望 }}

| 方法 | 更新目标的来源 | 是否使用已有价值估计 |
| --- | --- | --- |
| DP | 模型下的 $R+\gamma V(S')$ 的期望 | 是，bootstrapping |
| MC | 实际完整轨迹的 $G_t$ | 否 |

- MC 不依赖准确模型，算法直接。
- 估计一个状态时，不必遍历全部状态空间。
- 但它需要等待回合结束，长轨迹的回报可能方差较高。
- 不使用后继状态的已有价值，意味着各状态之间的信息共享较少，可能需要很多样本。

## 9.7 Action-Value Estimation（动作价值估计）

没有模型时，仅有 $V(s)$ 难以比较动作。因此控制问题通常直接估计：

$$
Q^\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a].
$$

把统计单位从状态 $s$ 换成状态—动作对 $(s,a)$：

- First-Visit：每回合第一次访问这个**状态—动作对**。
- Every-Visit：每次访问这个状态—动作对。
- 不同动作的样本分别计数与平均。

### 9.7.1 Exploring Starts（探索性起始）

若策略从不选择某些动作，就收集不到它们的回报。Exploring Starts（ES）假设每个相关状态—动作对都有非零概率成为回合起点，以保证长期覆盖。

ES 是对起始机制的假设，并不意味着真实机器人或游戏总能任意重置到每个状态。下一章将讨论由策略自身持续探索的方法。

## 9.8 本章检查

- MC 的更新目标为什么必须等到回合结束才完整可知？
- 首次访问到底相对于哪一个回合判断？
- 从后向前计算回报，是否意味着从后向前判断首次访问？
- 无模型控制为什么更适合直接学习 $Q(s,a)$？

??? success "参考答案"

    1. **MC 使用完整回报**：标准回合制 MC 的目标为 $G_t=\sum_{k=0}^{T-t-1}\gamma^kR_{t+k+1}$。回合未结束时，未来奖励和终止时刻仍未知，因而这个样本目标尚不完整。若提前用估计价值补上未来，就引入了自举，不再是这里的完整回报 MC。
    2. **每个回合内分别判断首次访问**：对一个状态，从当前回合开头向后找第一次出现的位置，只用该位置的回报更新。下一回合重新判断；不是整个训练过程中只更新一次。动作价值的 First-Visit 判断对象则是状态—动作对。
    3. **回报的计算方向不改变“首次”的定义**：可以从后向前用 $G\leftarrow R+\gamma G$ 计算回报，但仅当该状态未在当前时刻之前出现时才更新。若状态在 $t=1,2$ 出现，First-Visit 应选 $t=1$；倒序遍历时简单保留第一个遇到的状态，会误选最后一次访问 $t=2$。
    4. **$Q$ 能直接比较动作**：只有 $V(s)$ 时，要评价某个动作通常还需转移与奖励模型，计算 $\mathbb E[R+\gamma V(S')\mid s,a]$。直接从经验学习 $Q(s,a)$ 后，可通过 $\arg\max_aQ(s,a)$ 改进策略，无须显式模型；仍需探索，才能获得各动作的估计。
