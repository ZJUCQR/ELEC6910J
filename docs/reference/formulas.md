# Formula Sheet · 公式速查

<p class="chapter-subtitle">先确认条件，再选择公式</p>

本页统一使用 $R_{t+1}$ 表示执行 $A_t$ 后获得的奖励；$T$ 表示回合终止时刻。概率和期望均按相关事件有定义、所需矩存在的条件使用。

## 1. Probability（概率）

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

[天气联合表与计算](../chapters/02-probability.md#weather-table)

## 2. Bandit & Incremental Mean

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

## 3. Returns & Values（回报与价值）

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

## 4. Bellman Equations

### 4.1 固定策略：对动作加权平均

$$
V^\pi(s)=\sum_a\pi(a\mid s)
\sum_{s',r}p(s',r\mid s,a)[r+\gamma V^\pi(s')].
$$

$$
Q^\pi(s,a)=\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma\sum_{a'}\pi(a'\mid s')Q^\pi(s',a')\right].
$$

### 4.2 最优策略：对动作取最大值

$$
V^*(s)=\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma V^*(s')].
$$

$$
Q^*(s,a)=\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma\max_{a'}Q^*(s',a')\right].
$$

若使用 $T(s,a,s')$ 与条件期望奖励 $R(s,a,s')$，把对 $(s',r)$ 的和改成对 $s'$ 的和，并在括号内代入 $R$。

## 5. Dynamic Programming

### 5.1 Value Iteration

$$
V_{k+1}(s)\leftarrow
\max_a\sum_{s'}T(s,a,s')[R(s,a,s')+\gamma V_k(s')].
$$

### 5.2 Policy Evaluation

$$
V_{k+1}(s)\leftarrow
\sum_a\pi(a\mid s)\sum_{s'}T(s,a,s')
[R(s,a,s')+\gamma V_k(s')].
$$

固定策略的矩阵形式：

$$
(I-\gamma P^\pi)V^\pi=r^\pi.
$$

### 5.3 Policy Improvement

$$
\pi'(s)\in\arg\max_a
\sum_{s'}T(s,a,s')[R(s,a,s')+\gamma V^\pi(s')].
$$

如果 $Q^\pi(s,\pi'(s))\geq V^\pi(s)$ 对所有状态成立，则在定理适用条件下有 $V^{\pi'}\geq V^\pi$。

### 5.4 Contraction

$$
\|T^*u-T^*v\|_\infty\leq\gamma\|u-v\|_\infty,\qquad 0\leq\gamma<1.
$$

同样的界适用于 $T^\pi$。$\gamma=1$ 时不能直接套用压缩映射定理。

## 6. Monte Carlo

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

## 7. Exploration（探索）

共 $m$ 个动作、一个指定贪心动作时：

$$
\pi(a\mid s)=
\begin{cases}
1-\epsilon+\epsilon/m,&a=a^*,\\
\epsilon/m,&a\ne a^*.
\end{cases}
$$

$\epsilon$-soft 要求 $\pi(a\mid s)\geq\epsilon/m$。固定正 $\epsilon$ 会保留探索，因而最优性的策略类也受到约束。
