# 6: Value Iteration

<p class="chapter-subtitle">动态规划与价值迭代 · 让价值逐步传播</p>

**主要内容**：动态规划、价值迭代、赛车与 GridWorld 中的价值传播。

## 6.1 Dynamic Programming（动态规划）

DP 使用已知环境模型，利用 Bellman 关系求解 MDP。它要求能够枚举状态、动作以及相应转移，因此本节重点是 Tabular Setting（表格型设置）。

两种基本求解思路：

- 固定策略后，直接解线性方程组。
- 把 Bellman 递归关系变成迭代更新，从初始估计不断逼近解。

### 6.1.1 原课件例子：五状态方程组 {#linear-system}

课件有 $A,B,C,D,T$ 五个状态，$T$ 为终止态。这一例子采用未折扣形式，给定各分支权重，已经把策略选择纳入方程。

{{ slide lec05-06 39 | 五状态例子：终止态价值为 0，其余状态联立求解 }}

把原图的分支展开并整理：

$$
\begin{aligned}
V_A&=0.4V_B+0.48V_C+0.12V_D+0.04,\\
V_B&=0.9V_A-1.7,\\
V_C&=V_D+2,\\
V_D&=0.5V_B+1,\\
V_T&=0.
\end{aligned}
$$

例如，$A$ 右侧分支先以 $0.6$ 的权重到达机会节点，再以 $0.8$ / $0.2$ 分别到达 $C$ / $D$，所以对应系数为 $0.48$ 与 $0.12$。

联立解得近似值：

$$
(V_A,V_B,V_C,V_D,V_T)
\approx(1.11,-0.70,2.65,0.65,0).
$$

价值可以为负。不要把每个状态的价值限制在某个奖励区间内；它是未来多次奖励的累计期望。

## 6.2 Value Iteration（价值迭代）

令 $V_0(s)=0$。在相同终端约定下，$V_k(s)$ 可以解释为只剩 $k$ 步时的最优期望回报。

$$
V_{k+1}(s)=
\max_a\sum_{s'}T(s,a,s')
\left[R(s,a,s')+\gamma V_k(s')\right].
$$

- 每次更新都使用上一轮的后继价值。
- 枚举动作时，先计算每个动作的期望，再取最大值。
- 在有限折扣 MDP 中，重复更新收敛到 $V^*$。
- 价值对应的贪心策略可能比价值数值更早稳定。

### 6.2.1 同步更新的伪代码

~~~text
V(s) = 0 for every state
repeat:
    old = copy(V)
    for each non-terminal state s:
        V(s) = max over a of Σ T(s,a,s') [R(s,a,s') + γ old(s')]
    keep terminal values at 0
until max_s |V(s) - old(s)| < tolerance
~~~

!!! warning "这一轮不要混用新旧数值"

    课件逐轮演示采用同步更新。计算 $V_{k+1}(s)$ 时应使用所有状态的 $V_k$。原地更新也是一种方法，但中间数值会不同，不能拿它与课件同步迭代的每一轮直接比较。

## 6.3 Racing：逐轮计算 {#racing-iterations}

使用[赛车转移表](04-mdp.md#racing)，并按照本讲例子设 $\gamma=1$。

### 6.3.1 第一轮

初始值都为 0：

$$
V_1(C)=\max\{1,\;0.5\times2+0.5\times2\}=2,
$$

$$
V_1(W)=\max\{0.5\times1+0.5\times1,\;-10\}=1.
$$

### 6.3.2 第二轮

$$
\begin{aligned}
Q_2(C,\mathrm{Slow})&=1+2=3,\\
Q_2(C,\mathrm{Fast})&=0.5(2+2)+0.5(2+1)=3.5,\\
Q_2(W,\mathrm{Slow})&=0.5(1+2)+0.5(1+1)=2.5,\\
Q_2(W,\mathrm{Fast})&=-10.
\end{aligned}
$$

因此：

| 轮数 $k$ | Cool | Warm | Overheated |
| --- | ---: | ---: | ---: |
| 0 | 0 | 0 | 0 |
| 1 | 2 | 1 | 0 |
| 2 | 3.5 | 2.5 | 0 |

{{ slide lec05-06 52 | 赛车的两轮价值迭代：第二轮必须使用上一轮的 2 和 1 }}

!!! note "这里的 $\gamma=1$ 用于有限步演示"

    这个赛车模型能持续获得正奖励而不终止，因此 $\gamma=1$ 时不能据此宣称无限时域最优价值是有限数。下一讲改用 $\gamma=0.5$，可得到收敛的折扣价值。

### 6.3.3 动手观察价值传播 {#racing-lab}

下面是基于**同一课件模型**的补充演示。改变折扣后会从第 0 轮重新开始；每次只做一轮同步更新。

<div class="racing-lab" data-racing-lab>
  <div class="lab-heading"><span class="eyebrow">INTERACTIVE NOTE</span><strong>赛车 · 一步 Bellman backup</strong></div>
  <div class="lab-controls"><label for="race-gamma">折扣 γ <output id="race-gamma-value">1.00</output></label><input id="race-gamma" type="range" min="0" max="1" step="0.05" value="1"><span>0 — 1</span></div>
  <div class="race-states">
    <div><span class="state-dot cool"></span><span>Cool</span><strong id="race-cool">0.000</strong><small id="policy-cool">尚未更新</small></div>
    <div><span class="state-dot warm"></span><span>Warm</span><strong id="race-warm">0.000</strong><small id="policy-warm">尚未更新</small></div>
    <div><span class="state-dot terminal"></span><span>Overheated</span><strong>0.000</strong><small>终止态</small></div>
  </div>
  <div class="lab-actions"><button type="button" id="race-step">迭代一步 →</button><button type="button" id="race-reset" class="secondary">重置</button><span id="race-iteration" role="status" aria-live="polite">第 0 轮</span></div>
  <p id="race-detail">点击“迭代一步”，查看各动作如何得到新的价值。</p>
  <p id="race-caveat" class="lab-note">γ = 1：这里展示有限步价值，不能据此保证无限时域收敛。</p>
  <noscript>交互演示需要 JavaScript；上方表格已列出前两轮结果。</noscript>
</div>

## 6.4 GridWorld：从出口向外传播 {#gridworld-backup}

原课件使用 noise $=0.2$、discount $=0.9$、living reward $=0$。有奖励的出口格执行 exit 才获得终止奖励，因此“有数字的出口格”与“真正结束后的终止态”需要区分。

{{ slide lec05-06 55 | 第一轮：出口奖励先体现在出口格的价值中 }}

在第二轮，某状态向右以 $0.8$ 概率到达上一轮价值为 1 的格子；另外两个分支上一轮价值为 0。这个动作的价值为：

$$
0.8(0+0.9\times1)+0.1(0+0.9\times0)+0.1(0+0.9\times0)=0.72.
$$

还需要与其他动作的期望比较，才能得到该状态的新价值。

{{ slide lec05-06 56 | 第二轮：按转移概率和折扣系数，把出口价值传到相邻格 }}

{{ slide lec05-06 59 | 收敛后：价值信息从出口逐步传遍可达状态 }}

## 6.5 Policy Extraction & Cost（策略提取与开销）

求出价值后，通过一步前瞻提取动作：

$$
\pi(s)\in\arg\max_a\sum_{s'}T(s,a,s')
[R(s,a,s')+\gamma V(s')].
$$

若转移模型是稠密的，一轮价值迭代要遍历 $|\mathcal S|$ 个状态、$|\mathcal A|$ 个动作和 $|\mathcal S|$ 个后继，因此时间复杂度为：

$$
O(|\mathcal S|^2|\mathcal A|).
$$

稀疏转移可按实际非零分支计算，通常更便宜。

课件指出两个问题：每轮开销可能很大，而且策略常常早于价值收敛。下一章先固定策略做评估，再在第 8 章单独改进策略。

## 6.6 本章检查

- Bellman 最优方程与价值迭代更新式，区别在于哪里？
- 能否手算赛车的前两轮，解释为什么 Cool 的第二轮为 3.5？
- GridWorld 的 $0.72$ 来自哪三个因素？
- 为什么存在终止态的赛车，在 $\gamma=1$ 时仍可能有无限回报？

??? success "参考答案"

    1. **真实值与迭代估计**：Bellman 最优方程为 $V^*=T^*V^*$，左右两侧都是同一个解；同步价值迭代为 $V_{k+1}=T^*V_k$，用上一轮估计产生下一轮估计。有限状态与动作、奖励有界、$0\leq\gamma<1$ 时，迭代收敛到唯一的 $V^*$。
    2. **赛车前两轮**：本例 $\gamma=1$，初值全为 0，终止价值固定为 0。第一轮 $V_1(C)=\max(1,2)=2$，$V_1(W)=\max(1,-10)=1$。第二轮始终使用这组旧值：

        $$
        \begin{aligned}
        V_2(C)&=\max\{1+2,\;0.5(2+2)+0.5(2+1)\}=3.5,\\
        V_2(W)&=\max\{0.5(1+2)+0.5(1+1),\;-10\}=2.5.
        \end{aligned}
        $$

        Cool 的 $3.5$ 来自 Fast 的两个随机分支；不能在算 Warm 时改用刚得到的 $3.5$。
    3. **$0.72$ 的三个因素**：到达该后继的概率 $0.8$、折扣 $\gamma=0.9$、上一轮后继价值 $1$。即时奖励为 0，另外两个概率为 $0.1$ 的后继旧值也为 0，因此动作期望为 $0.8\times0.9\times1=0.72$。
    4. **存在终点不等于一定终止**：从 Cool 一直选 Slow，会始终留在 Cool，每步获得 $+1$。当 $\gamma=1$，累计回报为 $1+1+\cdots$，没有有限上界。本例的前两轮可解释为有限步最优回报，但不能据此断言无限时域价值有限。
