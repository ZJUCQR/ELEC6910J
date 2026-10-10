# 12: Temporal Difference Control

<p class="chapter-subtitle">时序差分控制 · 从评估行动，到改进策略</p>

!!! info "本章对应课件"

    Lecture 12 · <strong>ELEC6910J_Lec_11_12.pdf，p. 51–96</strong>。
    [查看本讲全部课件](../slides/lecture-12.md) · [下载 PDF](../assets/pdf/ELEC6910J_Lec_11_12.pdf)
    重点是 SARSA、Q-learning、多步控制及探索条件；末尾衔接 DQN 的基本表示。

## 12.1 Prediction to Control（从预测到控制）

上一章在给定策略下估计价值。本章把“估计”与“改进”交替进行：

1. 根据当前 $Q$ 选择动作，与环境交互。
2. 从一步或多步经验更新 $Q$。
3. 让策略更偏好估计价值高的动作，同时维持必要探索。

这是 Generalized Policy Iteration（GPI，广义策略迭代）的思路。每次只更新一个状态—动作对，也可以逐步完成评估与改进，不必先把整张价值表评估到精确收敛。

## 12.2 SARSA：On-policy TD Control {#sarsa}

SARSA 的名字来自五个量：

$$
S_t,\quad A_t,\quad R_{t+1},\quad S_{t+1},\quad A_{t+1}.
$$

它的更新是：

$$
Q(S_t,A_t)\leftarrow Q(S_t,A_t)+
\alpha\left[R_{t+1}+\gamma Q(S_{t+1},A_{t+1})-Q(S_t,A_t)\right].
$$

关键是 $A_{t+1}$：它是**当前行为策略实际选出的下一个动作**，可能是探索动作，不一定使 $Q$ 最大。

{{ slide lec11-12 58 | SARSA 算法：先按当前策略选择下一动作，再用它的动作价值更新 }}

### 12.2.1 一个回合中的顺序

1. 初始化环境得到 $S$，按当前 $\epsilon$-greedy 策略选择 $A$。
2. 执行 $A$，观察 $R,S'$。
3. 若 $S'$ 尚未终止，按当前策略选择 $A'$。
4. 用 $R+\gamma Q(S',A')$ 更新 $Q(S,A)$；若已终止，目标只取 $R$。
5. 令 $S\leftarrow S',A\leftarrow A'$，继续执行已选出的动作。

这里不能在第 5 步重新随意抽取一个不同的动作，却仍声称上一目标用了实际后继动作。采样策略和被评估策略一致，正是 on-policy 的含义。

## 12.3 Convergence & GLIE（收敛与持续探索） {#glie}

课件 p. 59–65 强调三个条件：足够的访问、合适的步长，以及策略在极限下趋于贪心。

{{ slide lec11-12 65 | SARSA 的收敛条件：不能只看学习率，也要看访问覆盖与策略变化 }}

在有限表格、奖励有界及合适的折扣或 episodic 条件下，对每个相关 $(s,a)$ 的第 $k$ 次更新，常见步长要求为：

$$
\sum_{k=1}^{\infty}\alpha_k(s,a)=\infty,
\qquad
\sum_{k=1}^{\infty}\alpha_k(s,a)^2<\infty.
$$

- 第一条防止学习过早停止，例如 $\alpha_k=2^{-k}$ 的总和有限。
- 第二条控制累计采样噪声；固定正步长不满足它。
- $\alpha_k=1/k$ 满足这两个条件，$k$ 应按该状态—动作对的访问次数计。

GLIE（Greedy in the Limit with Infinite Exploration）还要求：

- Infinite Exploration：每个相关状态—动作对都被无限次访问。
- Greedy in the Limit：非贪心动作的总概率趋于 0；多个并列最优动作可采用一致的打破平局规则，或在它们之间分配概率。

!!! note "探索概率衰减，不等于已经保证覆盖"

    p. 64–65 用 $\epsilon_t=1/t$ 说明趋于贪心。但仅有 $\epsilon_t\to0$，不能自动保证任意 MDP 中每个 $(s,a)$ 都被无限次访问；某些状态可能需要连续多次探索才能到达。覆盖条件必须另外检查。

固定 $\epsilon>0$ 时，SARSA 的目标包含持续探索带来的后果，不能直接宣称它满足“趋于完全贪心”的条件。

## 12.4 Windy GridWorld（有风的网格世界） {#windy-gridworld}

课件用 7×10 网格展示 SARSA：从 S 到 G，不同列的风会把智能体向上吹。

{{ slide lec11-12 66 | Windy GridWorld：底部数字是各列风力，并比较四方向与八方向动作集合 }}

从左到右，图中的风力为：

$$
[0,0,0,1,1,1,2,2,1,0].
$$

动作产生位移，风也产生位移，因此“向右走”不一定只改变列坐标。课件还画出了 standard moves 与 king's moves；动作集合不同，所求策略也会不同。

!!! example "笔记补充：怎样把图写成一步转移？"

    采用常见的四方向、确定性风版本：行列从 0 开始，S 为 $(3,0)$，G 为 $(3,7)$；按**当前列**的风力施风，越界位置截断到网格内。
    若动作位移为 $(\Delta r,\Delta c)$，则

    $r'=\operatorname{clip}(r+\Delta r-w[c],0,6)$，
    $c'=\operatorname{clip}(c+\Delta c,0,9)$。

    例如，从 $(3,6)$ 向右移动，该列风力为 2，所以到达 $(1,7)$，并没有直接到 G。
    用每步奖励 $-1$、$\gamma=1$、到 G 终止的设定，最大化回报就对应减少到达目标的步数。这些约定用于说明图中的标准任务；改变风力或动作规则后，应重新计算转移。

{{ slide lec11-12 67 | Windy GridWorld 的学习曲线与一条学到的路径 }}

曲线横轴是累计 time steps，纵轴是完成的 episodes。斜率变大，表示单位交互步数内完成更多回合，即平均每回合更短；纵轴不是奖励。探索动作仍可能让训练中的回合比最终贪心路径更长。

## 12.5 n-Step SARSA（多步动作价值更新） {#n-step-sarsa}

将多步 TD 的末尾状态价值换成动作价值：

$$
G_{t:t+n}
=\sum_{k=0}^{n-1}\gamma^kR_{t+k+1}
+\gamma^nQ(S_{t+n},A_{t+n}),\qquad t+n<T.
$$

$$
Q(S_t,A_t)\leftarrow Q(S_t,A_t)
+\alpha[G_{t:t+n}-Q(S_t,A_t)].
$$

如果 $t+n\geq T$，只累加到 $R_T$，没有终止后的自举项；结束时还要处理尾部不足 $n$ 步的更新。

{{ slide lec11-12 70 | 稀疏奖励的传播：一次成功轨迹能增强最后一个动作，或最后 n 个动作 }}

图中初值为 0，除到达 G 的正奖励外，其余奖励都为 0。对图示这条轨迹，一步 SARSA 在首次前向经历中只把最后一个动作更新为正值；多步 SARSA 能让最后 $n$ 个动作的目标包含终点奖励。

!!! note "原页边界与更新范围"

    p. 69 的回报说明写了 $t+n>T$；在 $t+n=T$ 时同样已到终点，不应再自举。
    该页还用 $s\ne S_t$ **且** $a\ne A_t$ 描述其他表项。准确条件是 $(s,a)\ne(S_t,A_t)$，即二者至少一个不同；每次只更新目标表项。

## 12.6 Q-learning：Off-policy TD Control {#q-learning}

Bellman 最优方程要求后继状态选择最好的动作：

$$
Q^*(s,a)=\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma\max_{a'}Q^*(s',a')\right].
$$

Q-value iteration 通过已知模型计算这个期望。Q-learning 用实际转移 $(s,a,r,s')$ 代替模型求和：

$$
Y^{\mathrm Q}=r+\gamma\max_{a'}Q(s',a'),
$$

$$
Q(s,a)\leftarrow Q(s,a)+\alpha[Y^{\mathrm Q}-Q(s,a)].
$$

{{ slide lec11-12 73 | Q-learning：对采样得到的下一状态取最大动作价值，再修正当前表项 }}

行为上仍可采用 $\epsilon$-greedy，以便收集各动作的经验；但目标中使用的是 $\max_{a'}Q(s',a')$，不取决于接下来实际探索了哪个动作。

若 $s'$ 为终止态，目标是 $r$。不要对终止状态调用“选择下一动作”或把它的任意初始化值加入目标。

## 12.7 原课件例题：小狗、骨头与毒药 {#dog-grid}

{{ slide lec11-12 77 | 2×3 网格中的 Q-learning 任务：小骨头、食物与毒药对应不同奖励 }}

以左上角为 $(0,0)$：

| 进入位置或事件 | 奖励 | 回合是否结束 |
| --- | ---: | --- |
| 小骨头 $(0,1)$ | $+1$ | 否 |
| 大食物 $(1,2)$ | $+10$ | 是 |
| 毒药 $(1,1)$ | $-10$ | 是 |
| 其他移动 | $0$ | 课件另设“超过 5 步”结束 |

初始 Q 表全为 0，学习率 $\alpha=0.1$，折扣因子 $\gamma=0.99$。

### 12.7.1 第一步：向右拿小骨头

从 $(0,0)$ 向右到 $(0,1)$，得到 $+1$。下一状态的全部动作价值仍为 0：

$$
Q((0,0),\rightarrow)
=0+0.1[1+0.99\times0-0]=0.1.
$$

{{ slide lec11-12 80 | 首次正奖励把一个 Q 表项从 0 更新为 0.1 }}

这里更新的是**出发状态与所选动作**的表项，不是把到达状态整行都改成 0.1。

### 12.7.2 第二步：向下进入毒药

从 $(0,1)$ 向下到 $(1,1)$，奖励 $-10$ 且终止：

$$
Q((0,1),\downarrow)=0+0.1[-10-0]=-1.
$$

{{ slide lec11-12 84 | 进入毒药后终止：只更新对应向下动作，后继价值取 0 }}

之前的 $Q((0,0),\rightarrow)=0.1$ 不会在这一步自动变成负值。更早动作的价值，需要后续转移或多步目标把信息传回去。

!!! note "步数上限与状态表示"

    上面两步没有触及课件的步数上限。若上限是任务本身的终止规则，严格的有限时域状态还应包含剩余步数；若只是训练采样的时间截断，则不一定应该把后继价值清零。两者需要区分。

## 12.8 SARSA vs. Q-learning（实际动作与贪心目标） {#on-off-policy}

| 比较项 | SARSA | Q-learning |
| --- | --- | --- |
| 下一步动作价值 | $Q(S_{t+1},A_{t+1})$ | $\max_aQ(S_{t+1},a)$ |
| 是否使用实际下一动作 | 是 | 否 |
| 行为策略 | 如 $\epsilon$-greedy | 如 $\epsilon$-greedy |
| 目标对应的策略 | 当前行为策略 | 对当前 Q 贪心的策略 |
| 类型 | On-policy | Off-policy |

Behavior policy（行为策略）决定怎样收集数据；target policy（目标策略）决定在评估或优化谁。判断 on/off-policy，要看两者的关系，不能只看动作选择代码里有没有 $\epsilon$-greedy。

!!! example "笔记补充：同一转移，两个不同目标"

    设当前 $Q(s,a)=2$，奖励为 0，$\gamma=0.9,\alpha=0.1$。
    下一状态的最佳动作价值为 5，但探索实际选出的动作价值为 1。

    - SARSA：目标 $0+0.9\times1=0.9$，更新后 $2+0.1(0.9-2)=1.89$。
    - Q-learning：目标 $0+0.9\times5=4.5$，更新后 $2+0.1(4.5-2)=2.25$。

### 12.8.1 笔记补充：可直接核对的更新代码

~~~python
def sarsa_update(q, state, action, reward, next_state, next_action,
                 alpha, gamma, terminated=False):
    old = q.get((state, action), 0.0)
    future = 0.0 if terminated else q.get((next_state, next_action), 0.0)
    q[state, action] = old + alpha * (reward + gamma * future - old)


def q_learning_update(q, state, action, reward, next_state, next_actions,
                      alpha, gamma, terminated=False):
    old = q.get((state, action), 0.0)
    future = 0.0 if terminated else max(
        q.get((next_state, candidate), 0.0) for candidate in next_actions
    )
    q[state, action] = old + alpha * (reward + gamma * future - old)
~~~

q 用 $(state,action)$ 作为键；next_actions 是下一非终止状态的合法动作集合。终止时不需要下一动作，SARSA 可传 next_action=None，Q-learning 可传空的 next_actions。这是单次更新函数，动作选择、环境交互和回合循环仍由调用方完成。

### 12.8.2 Off-policy 也需要探索

课件 p. 88–89 的收敛结论有条件：有限表格、合适的任务条件、相关状态—动作对被充分访问，以及对每个表项满足步长条件。

Q-learning 可以在持续探索的行为策略下学习最优动作价值；它不要求行为策略最终与贪心目标策略完全一致。但是，从未采样的动作仍无从可靠估计。“可以用不同策略的数据”并不等于“怎样采样都无所谓”。

## 12.9 From Q-tables to DQN（从表格到神经网络） {#dqn-preview}

表格需要为每个 $(s,a)$ 单独存一个数，规模为 $|\mathcal S|\times|\mathcal A|$。状态很多时，存储、访问覆盖和跨状态的信息共享都会成为问题。

{{ slide lec11-12 91 | Pacman 的已发现与未发现状态：表格不会自动把一个局面的经验推广到其他局面 }}

课件 p. 92–93 引入 $Q(s,a;\theta)$：神经网络输入状态，输出各离散动作的 Q 值，用参数共享替代独立表项。

{{ slide lec11-12 93 | DQN 入门：用神经网络表示动作价值，并以 TD 目标构造平方误差 }}

把终止边界显式写出，目标可表示为：

$$
y=
\begin{cases}
r,&s'\text{ 是终止状态},\\
r+\gamma\max_{a'}Q(s',a';\theta),&\text{否则}.
\end{cases}
$$

$$
\mathcal L(\theta)=\mathbb E_{(s,a,r,s')\sim\mathcal D}
\left[(y-Q(s,a;\theta))^2\right].
$$

这是课件给出的基本表示与损失思路。实际 TD 回归通常把 $y$ 当作固定目标，避免沿目标分支反向传播；常见 DQN 还使用目标网络、经验回放等机制，这份材料没有展开完整训练算法。表格 Q-learning 的收敛保证也不能直接搬到任意神经网络上。

## 12.10 期中复习与本章检查

课件 p. 95 明确列出 TD Prediction、TD Control、on-policy SARSA 与 off-policy Q-learning。跨章节范围与复习安排见[首页期中复习](../index.md#midterm)。

- SARSA 为什么要先选 $A_{t+1}$，再更新 $Q(S_t,A_t)$？
- 风如何改变一步转移？Windy GridWorld 曲线斜率变大意味着什么？
- 一步与多步 SARSA 如何传播第一次遇到的终点奖励？
- 小狗例题中，$+1$、$0.1$、$-10$、$-1$ 分别是奖励还是更新后的 Q 值？
- Q-learning 使用贪心目标，为什么行为策略还可以探索？
- 学习率趋于 0、探索概率趋于 0，分别还需要哪些配套条件？
