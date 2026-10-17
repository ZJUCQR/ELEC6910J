---
title: 期中模拟卷与解答
description: 按期中 Checklist 编排的 100 分模拟卷，包含选择、填空和课件例题改编计算；解答先列公式，再代入数值。
---

# 期中模拟卷

**100 分 · 建议用时 170 分钟 · 选择题 / 填空题 / 计算题**

范围对应期中复习课件第 3、36、37 页。计算题沿用课件情境，调整少量参数或缩小状态空间；具体条件均在题面给出。

| 题型 | 题号 | 分值 | 建议用时 |
| --- | --- | ---: | ---: |
| 单项选择 | 1–8 | 16 | 15 分钟 |
| 填空 | 9–16 | 24 | 25 分钟 |
| 计算 | 17–24 | 60 | 115 分钟 |
| 检查 | — | — | 15 分钟 |

计算题按 **公式 → 代入 → 结果** 作答，表格题写出逐步更新。统一用 $R_{t+1}$ 表示执行 $A_t$ 后的奖励；终止状态后续价值为 0。除明确复用模型外，各题独立，数值可保留分数或四位小数。

[开始答题](#questions) · [参考解答](#answers)

??? note "Checklist 覆盖与题目对应"

    ![Practical Problem-Solving：逐步表格价值更新、推导最优策略，以及矩阵和代数计算](assets/figures/lec13-14-p003-practical.webp)

    | 范围 | 对应题目 |
    | --- | --- |
    | Bandits；探索与利用；平稳与非平稳；ε-greedy | 2、7、10、17 |
    | MDP 建模；Markov 性；折扣对策略的影响 | 3、18 |
    | State / Action Value；Bellman 期望、最优方程与算子 | 4、9、18–21 |
    | VI；策略评估与改进；收敛；计算复杂度 | 8、16、19–21 |
    | First / Every-visit MC；MC control；Soft policy | 10、12、22 |
    | DP / MC / TD；偏差、方差；TD target / error；多步 TD | 5、11、13、23 |
    | SARSA / Q-learning；on / off-policy；实现与探索影响 | 6、24 |
    | GLIE；访问覆盖；步长条件 | 14、15 |
    | 监督学习与强化学习 | 1 |
    | **逐步表格更新、最优策略推导** | **17、19–24** |
    | **矩阵与代数计算** | **18、20、21** |

## 一、单项选择题 {#questions}

**每题 2 分，共 16 分；每题只有一个正确选项。**

**1. 关于监督学习与强化学习，下列哪项正确？**

- A. 强化学习在每个状态都会收到正确动作标签。
- B. 监督学习通常使用输入与目标标签；强化学习通过交互奖励学习，动作可能影响未来数据和回报。
- C. 强化学习只优化当前一步奖励。
- D. 没有标签的任务都属于强化学习。

**2. 餐厅的平均服务质量逐渐变化，哪种估计更适合追踪近期变化？**

- A. 永久固定最初的估计。
- B. 只使用第一次访问的奖励。
- C. 使用固定正步长，让较旧奖励的权重逐渐衰减。
- D. 使用全部历史样本的等权平均，且样本越多，对变化的反应一定越快。

**3. MDP 的 Markov property 表示：**

- A. 下一状态与当前状态无关。
- B. 给定当前状态和动作后，下一状态与奖励的条件分布不再依赖更早历史。
- C. 下一状态必须由当前动作唯一确定。
- D. 所有状态都应得到相同奖励。

**4. 对任意价值表 $V$，定义两个算子：**

$$
\begin{aligned}
(\mathcal A V)(s)&=\sum_a\pi(a\mid s)\sum_{s'}T(s,a,s')[R(s,a,s')+\gamma V(s')],\\
(\mathcal B V)(s)&=\max_a\sum_{s'}T(s,a,s')[R(s,a,s')+\gamma V(s')].
\end{aligned}
$$

- A. 两者都是 MC 更新。
- B. $\mathcal A$ 为最优算子，$\mathcal B$ 为期望算子。
- C. $\mathcal A=T^\pi$ 为固定策略的期望算子，$\mathcal B=T^*$ 为最优算子。
- D. 两者都必须等到一个回合结束才能计算。

**5. 对固定策略预测，关于 MC 与 TD(0) 的目标，下列哪项正确？**

- A. 完整 MC 回报是无偏目标；TD 目标依赖当前后继估值，可能有偏，通常方差较低。
- B. MC 使用后继价值自举，TD 不使用。
- C. TD 目标有偏，所以表格 TD 永远不能收敛到正确价值。
- D. 在任何 MDP 中，TD 目标的方差都严格小于 MC。

**6. 下一状态非终止，行为策略实际选择了一个非贪心动作。哪项正确？**

- A. SARSA 必须忽略这个动作，改用最大 Q 值。
- B. SARSA 使用实际下一动作的 Q 值；Q-learning 使用下一状态的最大 Q 值。
- C. Q-learning 必须重新采样一个贪心动作后，才能更新当前表项。
- D. 只要行为策略是 ε-greedy，两个算法的目标就一定相同。

**7. 在当前 Q 表不变、贪心动作唯一的情况下，增大 $\epsilon$ 通常会：**

- A. 增大折扣因子。
- B. 减小每次价值更新的步长。
- C. 增大非贪心动作的采样概率，增加探索，也可能降低短期收益。
- D. 保证当前每次行动都得到更高奖励。

**8. 有限 MDP、奖励有界、$0\leq\gamma<1$，同步 Value Iteration 的正确结论是：**

- A. 任意两轮得到相同贪心动作，就说明价值已精确收敛。
- B. 一轮更新就能得到 $V^*$。
- C. 同样的压缩系数结论可直接用于所有 $\gamma=1$ 任务。
- D. Bellman 最优算子为 $\gamma$-contraction，因此迭代收敛到唯一的 $V^*$。

## 二、填空题

**每题 3 分，共 24 分；每题三个空，每空 1 分，第 11 题六个空每空 0.5 分。**

**9. State Value 与 Action Value。** 补全定义与关系：

$$
V^\pi(s)=\underline{\qquad\qquad},\quad
Q^\pi(s,a)=\underline{\qquad\qquad},\quad
V^\pi(s)=\underline{\qquad\qquad}.
$$

**10. Soft policy。** 四个可用动作，$\epsilon=0.2$。ε-soft 对每个动作规定的概率下界是 \_\_\_\_\_\_；若贪心动作唯一，ε-greedy 赋予它的总概率是 \_\_\_\_\_\_；按蕴含方向排列 ε-greedy、ε-soft、soft：\_\_\_\_\_\_。

**11. DP / MC / TD。** 按“需要转移与奖励模型吗 / 使用已有价值自举吗”填写“是、否”：DP（\_\_\_\_\_\_ / \_\_\_\_\_\_）；标准 MC（\_\_\_\_\_\_ / \_\_\_\_\_\_）；TD(0)（\_\_\_\_\_\_ / \_\_\_\_\_\_）。

**12. MC 样本选择。** 同一回合多次访问状态 $s$，First-visit 使用 \_\_\_\_\_\_ 的回报，Every-visit 使用 \_\_\_\_\_\_ 的回报；标准 episodic MC 要在 \_\_\_\_\_\_ 后才能获得完整目标。

**13. TD(0)。** 非终止转移 $(s,r,s')$ 的 target 为 $y=$ \_\_\_\_\_\_，TD error 为 $\delta=$ \_\_\_\_\_\_，更新后 $V(s)=$ \_\_\_\_\_\_（右侧使用更新前的值）。

**14. GLIE。** 两项条件分别是 \_\_\_\_\_\_、\_\_\_\_\_\_；固定 $\epsilon=0.2$ 的 ε-greedy 在存在严格非贪心动作时，是否满足“Greedy in the Limit”：\_\_\_\_\_\_。

**15. 学习率。** 对每个表项的第 $n$ 次更新，常见随机逼近条件是 $\sum_n\alpha_n=$ \_\_\_\_\_\_、$\sum_n\alpha_n^2$ \_\_\_\_\_\_；在 $\alpha_n=1/n$ 与固定 $\alpha_n=0.1$ 中，同时满足两条的是 \_\_\_\_\_\_。

**16. 稠密模型的计算复杂度。** 令 $n=|\mathcal S|,m=|\mathcal A|$。一次 VI sweep 为 \_\_\_\_\_\_；已构造 $P^\pi,r^\pi$ 后，一次固定策略评估 sweep 为 \_\_\_\_\_\_；采用一般稠密线性求解进行精确评估，再做一次贪心改进，一轮 PI 为 \_\_\_\_\_\_。

## 三、计算题

**共 60 分。需要表格的题目请保留每一步的旧值、目标和新值。**

### 17. Bandits：餐厅选择（7 分） {#q17}

两个臂为 LG1、LG7。初始 $Q(\mathrm{LG1})=Q(\mathrm{LG7})=0$，计数均为 0。先按下面给定序列收集奖励：

| 全局步骤 | 餐厅 | 奖励 |
| ---: | --- | ---: |
| 1 | LG1 | 4 |
| 2 | LG7 | 2 |
| 3 | LG1 | 0 |
| 4 | LG7 | 6 |
| 5 | LG1 | 3 |

1. 使用按臂计数的样本平均，逐行列出 $N(\mathrm{LG1}),N(\mathrm{LG7}),Q(\mathrm{LG1}),Q(\mathrm{LG7})$。（3 分）
2. 根据最终估计，采用 $\epsilon=0.2$ 的 ε-greedy，求两家餐厅的选择概率。探索分支在两个臂中均匀选择。（1 分）
3. 若真实均值为 $q_*(\mathrm{LG1})=3,q_*(\mathrm{LG7})=5$，求下一步期望奖励及期望 regret。（1 分）
4. 独立地，仅对 LG1 的三个奖励从零开始使用固定 $\alpha=0.5$，列出三次估计。说明为何这更适合非平稳奖励。（2 分）

### 18. MDP：赛车的一步期望与折扣（7 分） {#q18}

第 18、19、21 题共用下表。$C$、$W$、$O$ 分别为 Cool、Warm、Overheated；$O$ 为终止态。除第 18 题第 4 小问外，**$\gamma=0.8$**。

| 状态 | 动作 | 后继状态 | 概率 | 奖励 |
| --- | --- | --- | ---: | ---: |
| $C$ | Slow | $C$ | 1 | 1 |
| $C$ | Fast | $C$ | 0.5 | 2 |
| $C$ | Fast | $W$ | 0.5 | 2 |
| $W$ | Slow | $C$ | 0.5 | 1 |
| $W$ | Slow | $W$ | 0.5 | 1 |
| $W$ | Fast | $O$ | 1 | −10 |

1. 写出本题的 MDP 五元组，说明 $O$ 的后续价值。（2 分）
2. 给定一张用于前瞻的价值表 $U(C)=4,U(W)=2,U(O)=0$，求四个 $q_U(s,a)$。这里 $U$ 是给定估计，不假设已等于某个策略的精确价值。（2 分）
3. 在 $C$ 以概率 $0.25$ 选 Fast、$0.75$ 选 Slow，求一次固定策略 backup $(T^\pi U)(C)$。（1 分）
4. 独立的两路径模型：路径 A 的奖励序列为 $[2]$，路径 B 为 $[0,0,8]$，之后均终止。求使两者回报相等的 $\gamma\in[0,1]$；分别判断 $\gamma=0.25,0.75$ 时选择哪条路径。（2 分）

### 19. Value Iteration：逐轮价值表（8 分） {#q19}

使用第 18 题赛车模型，$\gamma=0.8$，$V_0(C)=V_0(W)=V_0(O)=0$。

1. 写出 Value Iteration 公式，做 **三轮同步更新**。每轮先列 Cool / Slow、Cool / Fast、Warm / Slow、Warm / Fast 的动作前瞻值，再填 $V_{k+1}(C),V_{k+1}(W)$。（5 分）
2. 从第三轮价值 $V_3$ 再做一步前瞻，提取贪心策略。（2 分）
3. 说明本题为什么收敛；仅凭前三轮贪心动作不变，能否断定数值已精确等于 $V^*$？（1 分）

### 20. Policy Evaluation：GridWorld 与矩阵（8 分） {#q20}

将课件 GridWorld 缩小为 $2\times2$，布局如下：

|  | 左列 | 右列 |
| --- | --- | --- |
| 上行 | 终止态 $T$ | $A$ |
| 下行 | $B$ | $C$ |

四个动作上、下、左、右各以概率 $1/4$ 选择；移动确定，撞墙留在原格。**每次从非终止状态出发的奖励均为 $-1$，包括进入 $T$；$\gamma=1$，$V(T)=0$。**

1. 按 $(A,B,C)$ 的顺序，列出非终止部分的 $P^\pi$ 和奖励向量 $r^\pi$。指出前两行概率和为什么不是 1。（2 分）
2. 从零开始做两轮同步策略评估，列出每轮完整的 $(V(A),V(B),V(C))$。（2 分）
3. 写出 $(I-\gamma P^\pi)v=r^\pi$，用代数消元求精确价值。说明本题 $\gamma=1$ 时，为什么仍可评估这个策略。（4 分）

### 21. Policy Improvement：赛车的最优策略（8 分） {#q21}

回到第 18 题赛车模型，$\gamma=0.8$。初始策略 $\pi_0$ 在 $C,W$ 都选择 Slow。

1. 精确评估 $\pi_0$，列 Bellman 方程并求 $V^{\pi_0}(C),V^{\pi_0}(W)$。（2 分）
2. 根据这张旧策略价值表，列四个 $Q^{\pi_0}(s,a)$，做一次贪心改进得到 $\pi_1$。（2 分）
3. 对 $\pi_1$ 写出二维矩阵方程并求精确价值。（2 分）
4. 再比较全部动作，验证策略是否稳定，给出 $\pi^*$ 和 $V^*$。（2 分）

### 22. Monte Carlo：重复访问与 Soft Control（8 分） {#q22}

固定策略产生一条完整轨迹，$\gamma=0.5$：

$$
A\xrightarrow{R_1=1}B\xrightarrow{R_2=2}B\xrightarrow{R_3=6}T.
$$

$S_0=A,S_1=B,S_2=B,S_3=T$，$T$ 为终止态。

1. 从后向前计算 $G_0,G_1,G_2,G_3$。（2 分）
2. 只用这一回合，分别计算 First-visit 与 Every-visit 对 $B$ 的估计；给出 $A$ 的估计。（2 分）
3. 现在改为加入历史样本：两种方法各自独立地已有 $N(B)=2,V(B)=4$。加入本回合后，分别用增量均值算出新的计数与价值。（2 分）
4. 独立的 MC control 更新：状态 $B$ 有动作 $a_1,a_2$，当前 $Q(B,a_1)=1,Q(B,a_2)=2$。刚收集到 $(B,a_1)$ 的完整回报 5，以 $\alpha=0.5$ 更新该表项，其他项暂不更新。随后用 $\epsilon=0.2$ 改进为 ε-greedy，求两动作概率，并说明它是否为 ε-soft。（2 分）

### 23. TD Prediction：Lake 与多步目标（7 分） {#q23}

将 Lake 中三个位置 $(1,1),(1,2),(1,3)$ 简记为 $A,B,C$。初值全为 0，$\alpha=0.2,\gamma=0.5$。依次观察：

$$
A\xrightarrow{-0.4}B\xrightarrow{-0.4}C\xrightarrow{-0.4}B.
$$

这些状态均未终止。

1. 按在线 TD(0) 逐步更新，列出每步使用的后继价值、target、TD error、更新后表项，以及最终 $(V(A),V(B),V(C))$。（4 分）
2. 独立地重置所有估计为 0。只观察前两次转移，使用 **2-step TD** 更新 $A$；此时 $C$ 未终止，后继估计仍为 0。求目标与新值。（2 分）
3. 再独立重置初值：若轨迹改为 $A\xrightarrow{-0.4}B\xrightarrow{+1}T$，第二步到终点，求 2-step 目标与 $V(A)$ 的新值。（1 分）

### 24. SARSA / Q-learning：小狗 Q 表（7 分） {#q24}

沿用小狗网格，$A=(0,0)$，小骨头位置 $B=(0,1)$，毒药位置 $D=(1,1)$。到 $B$ 奖励 $+1$；进入 $D$ 奖励 $-10$ 并终止。四方向动作均可选，越界留在原格。

本题使用一张已有的 Q 表，$\alpha=0.2,\gamma=0.9$：

| 表项 | 初始 Q |
| --- | ---: |
| $Q(A,\rightarrow)$ | 2 |
| $Q(B,\rightarrow)$ | 4 |
| $Q(B,\downarrow)$ | 1 |
| 其余非终止表项 | 0 |

实际行为为 $A\xrightarrow{\rightarrow,+1}B\xrightarrow{\downarrow,-10}D$。SARSA 与 Q-learning **各从上述相同初值独立开始**。

1. 分别写出两个算法第一步的 target、TD error 与新 $Q(A,\rightarrow)$。（3 分）
2. 完成第二步终止更新，列出两个算法最终的三个非零表项。（2 分）
3. 若在 $B$ 按 $\epsilon=0.2$ 的 ε-greedy 选下一动作，第一次选到向下的概率是多少？用本题说明 on-policy / off-policy 的区别，以及两个算法实现顺序上的不同。（2 分）

## 四、参考解答 {#answers}

先完成题目，再逐项展开。计算解答依次列出通式、数值代入和结果。

### 选择题与填空题

??? success "1–8：选择题答案与解释"

    | 题号 | 答案 | 解释 |
    | ---: | :---: | --- |
    | 1 | B | 监督学习通常有目标标签；RL 的奖励可以延迟，且行动会影响后续状态与采样分布。 |
    | 2 | C | 固定步长赋予近期样本较大权重；等权平均的单个新样本权重随计数增多而减小。 |
    | 3 | B | Markov 性是条件分布的性质，允许随机转移，不要求奖励相同。 |
    | 4 | C | 对动作按 $\pi$ 平均是期望算子；在各动作期望之间取最大值是最优算子。 |
    | 5 | A | MC 采样完整回报；TD 自举，当前后继估值的误差可进入目标。低方差是通常情形，并非普遍严格不等式。 |
    | 6 | B | SARSA 的目标包含实际下一动作；Q-learning 的目标包含后继最大 Q，与实际探索动作可不同。 |
    | 7 | C | $\epsilon$ 控制行为探索，$\alpha$ 控制修正幅度，$\gamma$ 控制远期回报的权重。 |
    | 8 | D | 有限折扣 MDP 的 $T^*$ 为压缩映射。策略可能早于价值稳定，不能用短暂动作不变代替收敛验证。 |

??? success "9–16：填空题答案与公式"

    **9. 定义与关系：**

    $$
    V^\pi(s)=\mathbb E_\pi[G_t\mid S_t=s],\qquad
    Q^\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a],
    $$

    $$
    V^\pi(s)=\sum_a\pi(a\mid s)Q^\pi(s,a).
    $$

    $Q^\pi$ 的当前动作固定为 $a$，此后才按 $\pi$ 行动；$V^\pi$ 连当前动作也按 $\pi$ 平均。

    **10. 先列公式：** ε-soft 要求 $\pi(a\mid s)\geq\epsilon/m$；唯一贪心动作的 ε-greedy 概率为 $1-\epsilon+\epsilon/m$。

    **代入：** $0.2/4=\boxed{0.05}$；$1-0.2+0.2/4=\boxed{0.85}$。关系为 **ε-greedy ⇒ ε-soft ⇒ soft**（$\epsilon>0$）；反向一般不成立。

    **11.** DP：**是 / 是**；MC：**否 / 否**；TD(0)：**否 / 是**。这里 DP 指枚举模型分支的经典 full backup。

    **12.** 当前回合**首次访问**；当前回合**每次访问**；**回合终止**。首次访问的判定在每个新回合重新开始。

    **13.**

    $$
    y=r+\gamma V(s'),\qquad
    \delta=y-V(s),\qquad
    V_{\mathrm{new}}(s)=V(s)+\alpha\delta.
    $$

    **14.** 每个相关 $(s,a)$ **无限次访问**；策略在极限下**相对于当前 Q 趋于贪心**；固定 $\epsilon=0.2$ **不满足**后者。只令 $\epsilon_t\to0$，也不能自动保证所有相关状态—动作对的覆盖。

    **15.**

    $$
    \sum_n\alpha_n=\boxed{\infty},\qquad
    \sum_n\alpha_n^2\boxed{<\infty}.
    $$

    符合的是 $\boxed{\alpha_n=1/n}$：调和级数发散，平方倒数级数收敛。固定 $0.1$ 的平方和发散。这些是有限表格、充分访问及适当任务条件下的步长条件，不能单独保证任意算法收敛。

    **16.** $\boxed{O(n^2m)}$、$\boxed{O(n^2)}$、$\boxed{O(n^3+n^2m)}$。

    VI 遍历状态、动作和后继；固定策略评估使用已聚合的 $P^\pi$；PI 的最后一式包含稠密线性求解和全动作改进。若用 $K$ 次评估 sweep 近似求值，一轮相应为 $O(Kn^2+n^2m)$。总运行时间还要考虑迭代轮数。

### 计算题解答

??? success "17：Bandits 的逐步估计、探索与 regret"

    **（1）公式。** 仅更新本次选中的臂，计数先加 1：

    $$
    N(a)\leftarrow N(a)+1,\qquad
    Q_{\mathrm{new}}(a)=Q(a)+\frac{R-Q(a)}{N(a)}.
    $$

    **代入并逐行填表：**

    | 步骤 | 被更新表项的计算 | $N_1$ | $N_7$ | $Q_1$ | $Q_7$ |
    | ---: | --- | ---: | ---: | ---: | ---: |
    | 0 | 初值 | 0 | 0 | 0 | 0 |
    | 1 | $0+(4-0)/1=4$ | 1 | 0 | 4 | 0 |
    | 2 | $0+(2-0)/1=2$ | 1 | 1 | 4 | 2 |
    | 3 | $4+(0-4)/2=2$ | 2 | 1 | 2 | 2 |
    | 4 | $2+(6-2)/2=4$ | 2 | 2 | 2 | 4 |
    | 5 | $2+(3-2)/3=7/3$ | 3 | 2 | $7/3$ | 4 |

    这里下标 1、7 表示 LG1、LG7。最终估计下 LG7 为唯一贪心臂。

    **（2）公式。**

    $$
    \pi(a^*)=1-\epsilon+\frac\epsilon m,\qquad
    \pi(a\ne a^*)=\frac\epsilon m.
    $$

    **代入：**

    $$
    \pi(\mathrm{LG7})=0.8+0.2/2=\boxed{0.9},\qquad
    \pi(\mathrm{LG1})=0.2/2=\boxed{0.1}.
    $$

    **（3）公式。**

    $$
    \mathbb E[R]=\sum_a\pi(a)q_*(a),\qquad
    \ell=\max_aq_*(a)-\mathbb E[R].
    $$

    **代入：** $\mathbb E[R]=0.1\times3+0.9\times5=\boxed{4.8}$，$\ell=5-4.8=\boxed{0.2}$。这里使用真实均值计算 regret，不用当前估计或单次随机奖励替代。

    **（4）公式。**

    $$
    Q_{\mathrm{new}}=Q+\alpha(R-Q).
    $$

    **代入：**

    $$
    0+0.5(4-0)=\boxed{2},\quad
    2+0.5(0-2)=\boxed{1},\quad
    1+0.5(3-1)=\boxed{2}.
    $$

    固定步长下，第 $i$ 个奖励在第 $n$ 次更新后的权重为 $\alpha(1-\alpha)^{n-i}$。旧奖励的权重随更新衰减，因此更容易追踪变化；较大步长也会使噪声影响更明显。

??? success "18：MDP 建模、动作期望与折扣阈值"

    **（1）模型。** $\mathcal S=\{C,W,O\}$；$\mathcal A(C)=\mathcal A(W)=\{\mathrm{Slow},\mathrm{Fast}\}$；$T$ 与 $R$ 由题面转移表给出；$\gamma=0.8$。$O$ 无后续决策，$V(O)=0$。进入它时的 $-10$ 仍计入当前转移奖励。

    **（2）公式。**

    $$
    q_U(s,a)=\sum_{s'}T(s,a,s')[R(s,a,s')+\gamma U(s')].
    $$

    **代入：**

    $$
    \begin{aligned}
    q_U(C,\mathrm{Slow})&=1[1+0.8\times4]=\boxed{4.2},\\
    q_U(C,\mathrm{Fast})&=0.5[2+0.8\times4]+0.5[2+0.8\times2]=\boxed{4.4},\\
    q_U(W,\mathrm{Slow})&=0.5[1+0.8\times4]+0.5[1+0.8\times2]=\boxed{3.4},\\
    q_U(W,\mathrm{Fast})&=1[-10+0.8\times0]=\boxed{-10}.
    \end{aligned}
    $$

    Fast 的两条随机分支必须加权求和；环境后继不是由智能体自由挑选的动作。

    **（3）公式。**

    $$
    (T^\pi U)(s)=\sum_a\pi(a\mid s)q_U(s,a).
    $$

    **代入：**

    $$
    (T^\pi U)(C)=0.75\times4.2+0.25\times4.4=\boxed{4.25}.
    $$

    这是对给定 $U$ 的一次固定策略 backup，尚不能把结果称为精确 $V^\pi(C)$。

    **（4）公式。**

    $$
    G_0=\sum_{k=0}^{T-1}\gamma^kR_{k+1}.
    $$

    **代入并解方程：**

    $$
    G_A=2,\qquad G_B=0+\gamma\times0+\gamma^2\times8=8\gamma^2,
    $$

    $$
    2=8\gamma^2\quad\Rightarrow\quad\gamma^2=\frac14
    \quad\Rightarrow\quad\boxed{\gamma=0.5}.
    $$

    $\gamma=0.25$ 时，$G_B=8(0.25)^2=0.5<2$，选 **A**；$\gamma=0.75$ 时，$G_B=8(0.75)^2=4.5>2$，选 **B**。折扣越大，较晚的大奖励越有吸引力。

??? success "19：Value Iteration 的三轮完整表格"

    **（1）公式。**

    $$
    q_k(s,a)=\sum_{s'}T(s,a,s')[R(s,a,s')+\gamma V_k(s')],\qquad
    V_{k+1}(s)=\max_aq_k(s,a).
    $$

    **代入模型后，每轮都使用同一张旧表 $V_k$：**

    $$
    \begin{aligned}
    q_k(C,\mathrm{Slow})&=1+0.8V_k(C),\\
    q_k(C,\mathrm{Fast})&=2+0.4[V_k(C)+V_k(W)],\\
    q_k(W,\mathrm{Slow})&=1+0.4[V_k(C)+V_k(W)],\\
    q_k(W,\mathrm{Fast})&=-10.
    \end{aligned}
    $$

    | 使用旧表 | Cool / Slow | Cool / Fast | Warm / Slow | Warm / Fast |
    | --- | --- | --- | --- | ---: |
    | $V_0=(0,0)$ | $1+0.8(0)=1$ | $2+0.4(0+0)=2$ | $1+0.4(0+0)=1$ | −10 |
    | $V_1=(2,1)$ | $1+0.8(2)=2.6$ | $2+0.4(2+1)=3.2$ | $1+0.4(2+1)=2.2$ | −10 |
    | $V_2=(3.2,2.2)$ | $1+0.8(3.2)=3.56$ | $2+0.4(3.2+2.2)=4.16$ | $1+0.4(3.2+2.2)=3.16$ | −10 |

    **每个状态对动作取最大值，得到：**

    | 轮数 | $V_k(C)$ | $V_k(W)$ | $V_k(O)$ |
    | ---: | ---: | ---: | ---: |
    | 0 | 0 | 0 | 0 |
    | 1 | 2 | 1 | 0 |
    | 2 | 3.2 | 2.2 | 0 |
    | 3 | **4.16** | **3.16** | 0 |

    **（2）策略提取公式。**

    $$
    \pi_{V_3}(s)\in\arg\max_a\sum_{s'}T(s,a,s')[R(s,a,s')+\gamma V_3(s')].
    $$

    **代入第三轮的值：**

    $$
    \begin{aligned}
    q_3(C,\mathrm{Slow})&=1+0.8(4.16)=4.328,\\
    q_3(C,\mathrm{Fast})&=2+0.4(4.16+3.16)=4.928,\\
    q_3(W,\mathrm{Slow})&=1+0.4(4.16+3.16)=3.928,\\
    q_3(W,\mathrm{Fast})&=-10.
    \end{aligned}
    $$

    所以提取的策略为 **Cool → Fast，Warm → Slow**。

    **（3）收敛。** 在本题有限状态、有界奖励、$\gamma=0.8<1$ 的条件下：

    $$
    \|T^*u-T^*v\|_\infty\leq0.8\|u-v\|_\infty.
    $$

    因而同步迭代收敛到唯一 $V^*$。三轮后动作虽相同，价值仍为 $(4.16,3.16)$；第 21 题将验证精确最优价值为 $(8,7)$，不能把策略暂时稳定当作价值已收敛。

??? success "20：GridWorld 的迭代评估与矩阵消元"

    **（1）公式。** 固定策略下：

    $$
    P^\pi_{ij}=\sum_a\pi(a\mid s_i)T(s_i,a,s_j),\qquad
    r^\pi_i=\sum_a\pi(a\mid s_i)\sum_{s'}T(s_i,a,s')R(s_i,a,s').
    $$

    **代入四个等概率动作：**

    | 出发 | 上 | 下 | 左 | 右 |
    | --- | --- | --- | --- | --- |
    | $A$ | $A$ | $C$ | $T$ | $A$ |
    | $B$ | $T$ | $B$ | $B$ | $C$ |
    | $C$ | $A$ | $C$ | $B$ | $C$ |

    按 $(A,B,C)$ 排列，省略终止状态列：

    $$
    P^\pi=
    \begin{bmatrix}
    1/2&0&1/4\\
    0&1/2&1/4\\
    1/4&1/4&1/2
    \end{bmatrix},\qquad
    r^\pi=\begin{bmatrix}-1\\-1\\-1\end{bmatrix}.
    $$

    前两行的和为 $3/4$，剩余 $1/4$ 是进入 $T$ 的概率。完整转移矩阵的行和仍为 1；这里只保留非终止子矩阵。

    **（2）公式。**

    $$
    v_{k+1}=r^\pi+\gamma P^\pi v_k.
    $$

    **代入 $v_0=(0,0,0)^\top,\gamma=1$：**

    $$
    v_1=\begin{bmatrix}-1\\-1\\-1\end{bmatrix}
    +P^\pi\begin{bmatrix}0\\0\\0\end{bmatrix}
    =\begin{bmatrix}-1\\-1\\-1\end{bmatrix}.
    $$

    第二轮：

    $$
    \begin{aligned}
    V_2(A)&=-1+\tfrac12(-1)+\tfrac14(-1)=\boxed{-1.75},\\
    V_2(B)&=-1+\tfrac12(-1)+\tfrac14(-1)=\boxed{-1.75},\\
    V_2(C)&=-1+\tfrac14(-1)+\tfrac14(-1)+\tfrac12(-1)=\boxed{-2}.
    \end{aligned}
    $$

    | 轮数 | $V(A)$ | $V(B)$ | $V(C)$ | $V(T)$ |
    | ---: | ---: | ---: | ---: | ---: |
    | 0 | 0 | 0 | 0 | 0 |
    | 1 | −1 | −1 | −1 | 0 |
    | 2 | −1.75 | −1.75 | −2 | 0 |

    **（3）矩阵公式。**

    $$
    (I-\gamma P^\pi)v=r^\pi.
    $$

    **代入：**

    $$
    \begin{bmatrix}
    1/2&0&-1/4\\
    0&1/2&-1/4\\
    -1/4&-1/4&1/2
    \end{bmatrix}
    \begin{bmatrix}v_A\\v_B\\v_C\end{bmatrix}
    =\begin{bmatrix}-1\\-1\\-1\end{bmatrix}.
    $$

    两边乘 4，得到代数方程：

    $$
    2v_A-v_C=-4,\quad 2v_B-v_C=-4,\quad -v_A-v_B+2v_C=-4.
    $$

    前两式相减得 $v_A=v_B=x$；第三式给出 $v_C=x-2$。代回第一式：

    $$
    2x-(x-2)=-4\Rightarrow x=-6,\qquad v_C=-6-2=-8.
    $$

    因此 $\boxed{V^\pi(A)=V^\pi(B)=-6,\ V^\pi(C)=-8}$。每步奖励为 $-1$，它们分别对应期望还需 6、6、8 步终止。

    从任何非终止状态出发，都至少有 $1/8$ 的概率在接下来两步内终止：从 $C$ 可经上再左或左再上，两条路径总概率 $2(1/4)^2=1/8$；从 $A,B$ 下一步就有 $1/4$ 的终止概率。因此生存概率按两步区间至多以 $7/8$ 衰减，期望回合长度有限。本题靠终止结构保证价值有限与评估收敛，不能直接套用 $\gamma<1$ 的一步压缩结论。

??? success "21：从初始策略到最优策略的完整推导"

    **（1）策略评估公式。**

    $$
    V^{\pi_0}(s)=\sum_{s'}T(s,\pi_0(s),s')[R(s,\pi_0(s),s')+\gamma V^{\pi_0}(s')].
    $$

    **代入处处 Slow，记 $v_C=V^{\pi_0}(C),v_W=V^{\pi_0}(W)$：**

    $$
    v_C=1+0.8v_C\Rightarrow0.2v_C=1\Rightarrow\boxed{v_C=5},
    $$

    $$
    v_W=0.5(1+0.8v_C)+0.5(1+0.8v_W)
    =1+0.4(5)+0.4v_W,
    $$

    $$
    0.6v_W=3\Rightarrow\boxed{v_W=5}.
    $$

    **（2）改进公式。**

    $$
    Q^{\pi_0}(s,a)=\sum_{s'}T(s,a,s')[R(s,a,s')+\gamma V^{\pi_0}(s')],\quad
    \pi_1(s)\in\arg\max_aQ^{\pi_0}(s,a).
    $$

    **代入同一张旧策略价值 $(5,5)$：**

    | 状态 | Slow | Fast | 改进后动作 |
    | --- | --- | --- | --- |
    | $C$ | $1+0.8(5)=5$ | $2+0.4(5+5)=6$ | Fast |
    | $W$ | $1+0.4(5+5)=5$ | $-10+0.8(0)=-10$ | Slow |

    得 $\boxed{\pi_1(C)=\mathrm{Fast},\ \pi_1(W)=\mathrm{Slow}}$。这里的 6 是按旧策略后续行动的一步前瞻值，不是新策略的完整评估结果。

    **（3）矩阵公式。**

    $$
    (I-\gamma P^{\pi_1})v^{\pi_1}=r^{\pi_1}.
    $$

    **代入：**

    $$
    P^{\pi_1}=\begin{bmatrix}0.5&0.5\\0.5&0.5\end{bmatrix},\quad
    r^{\pi_1}=\begin{bmatrix}2\\1\end{bmatrix},
    $$

    $$
    \begin{bmatrix}0.6&-0.4\\-0.4&0.6\end{bmatrix}
    \begin{bmatrix}v_C\\v_W\end{bmatrix}
    =\begin{bmatrix}2\\1\end{bmatrix}.
    $$

    两式相减得 $v_C-v_W=1$；代回第一式：

    $$
    0.6(v_W+1)-0.4v_W=2\Rightarrow0.2v_W=1.4
    \Rightarrow\boxed{v_W=7,\ v_C=8}.
    $$

    也可核对逆矩阵：

    $$
    \begin{bmatrix}0.6&-0.4\\-0.4&0.6\end{bmatrix}^{-1}
    =\frac1{0.36-0.16}\begin{bmatrix}0.6&0.4\\0.4&0.6\end{bmatrix}
    =\begin{bmatrix}3&2\\2&3\end{bmatrix},
    $$

    $$
    \begin{bmatrix}3&2\\2&3\end{bmatrix}\begin{bmatrix}2\\1\end{bmatrix}
    =\begin{bmatrix}8\\7\end{bmatrix}.
    $$

    **（4）再次使用动作前瞻公式，代入新策略精确价值：**

    | 状态 | Slow | Fast | 贪心动作 |
    | --- | --- | --- | --- |
    | $C$ | $1+0.8(8)=7.4$ | $2+0.4(8+7)=8$ | Fast |
    | $W$ | $1+0.4(8+7)=7$ | $-10$ | Slow |

    策略不变，且当前价值满足 $V^{\pi_1}=T^*V^{\pi_1}$。由折扣 MDP 最优不动点的唯一性：

    $$
    \boxed{\pi^*(C)=\mathrm{Fast},\quad\pi^*(W)=\mathrm{Slow}},\qquad
    \boxed{V^*(C)=8,\quad V^*(W)=7,\quad V^*(O)=0}.
    $$

??? success "22：MC 的回报、重复访问与 ε-soft 改进"

    **（1）公式。**

    $$
    G_t=R_{t+1}+\gamma G_{t+1},\qquad G_T=0.
    $$

    **从末尾向前代入：**

    $$
    G_3=0,\quad G_2=6+0.5(0)=\boxed{6},\quad
    G_1=2+0.5(6)=\boxed{5},\quad G_0=1+0.5(5)=\boxed{3.5}.
    $$

    **（2）公式。** 选出相应访问时刻的回报，再取样本平均：

    $$
    V(s)=\frac1{N(s)}\sum_{i=1}^{N(s)}G^{(i)}(s).
    $$

    **代入：** $B$ 的首次访问在 $t=1$，每次访问在 $t=1,2$。

    $$
    V_{\mathrm{first}}(B)=G_1=\boxed{5},\qquad
    V_{\mathrm{every}}(B)=\frac{G_1+G_2}{2}=\frac{5+6}{2}=\boxed{5.5}.
    $$

    $A$ 只出现一次，两种方法均给出 $\boxed{V(A)=G_0=3.5}$。

    **（3）增量均值公式。**

    $$
    N\leftarrow N+1,\qquad V_{\mathrm{new}}=V+\frac{G-V}{N}.
    $$

    **First-visit：** 新计数为 3，只加入 $G_1=5$：

    $$
    V(B)=4+\frac{5-4}{3}=\boxed{\frac{13}{3}},\qquad\boxed{N(B)=3}.
    $$

    **Every-visit：** 从其自己的历史 $N=2,V=4$ 开始，依次加入 5、6：

    $$
    V^{(1)}=4+\frac{5-4}{3}=\frac{13}{3},
    $$

    $$
    V^{(2)}=\frac{13}{3}+\frac{6-13/3}{4}=\boxed{\frac{19}{4}=4.75},
    \qquad\boxed{N(B)=4}.
    $$

    可用累计和核对：历史总回报为 $2\times4=8$，最终 $(8+5+6)/4=4.75$。

    **（4）控制更新公式。**

    $$
    Q_{\mathrm{new}}(s,a)=Q(s,a)+\alpha[G-Q(s,a)].
    $$

    **代入：** $Q(B,a_1)=1+0.5(5-1)=\boxed{3}$，$Q(B,a_2)=2$，所以 $a_1$ 为贪心动作。

    **策略公式与代入：**

    $$
    \pi(a_1\mid B)=1-\epsilon+\epsilon/2=0.8+0.1=\boxed{0.9},\qquad
    \pi(a_2\mid B)=\epsilon/2=\boxed{0.1}.
    $$

    两个概率均不低于 $\epsilon/2=0.1$，所以它是 **ε-soft**，也保留了非贪心动作的采样机会。

??? success "23：在线 TD 表格与两步终止边界"

    **（1）公式。**

    $$
    y_t=R_{t+1}+\gamma V(S_{t+1}),\quad
    \delta_t=y_t-V(S_t),\quad
    V_{\mathrm{new}}(S_t)=V(S_t)+\alpha\delta_t.
    $$

    **逐步代入当时最新的价值：**

    | 步骤 | 转移 | 后继值 | Target $y$ | TD error $\delta$ | 更新后的出发表项 |
    | ---: | --- | ---: | --- | --- | --- |
    | 1 | $A\to B$ | 0 | $-0.4+0.5(0)=-0.4$ | $-0.4-0=-0.4$ | $0+0.2(-0.4)=-0.08$ |
    | 2 | $B\to C$ | 0 | $-0.4+0.5(0)=-0.4$ | $-0.4-0=-0.4$ | $0+0.2(-0.4)=-0.08$ |
    | 3 | $C\to B$ | −0.08 | $-0.4+0.5(-0.08)=-0.44$ | $-0.44-0=-0.44$ | $0+0.2(-0.44)=-0.088$ |

    最终 $\boxed{V(A)=-0.08}$，$\boxed{V(B)=-0.08}$，$\boxed{V(C)=-0.088}$。第三步读到的 $V(B)$ 是第二步已更新的值；每步仅修改出发状态。

    **（2）未终止的 2-step 公式。**

    $$
    G_{0:2}=R_1+\gamma R_2+\gamma^2V(S_2),\qquad
    V_{\mathrm{new}}(A)=V(A)+\alpha[G_{0:2}-V(A)].
    $$

    **重置后代入：**

    $$
    G_{0:2}=-0.4+0.5(-0.4)+0.5^2(0)=\boxed{-0.6},
    $$

    $$
    V_{\mathrm{new}}(A)=0+0.2(-0.6-0)=\boxed{-0.12}.
    $$

    **（3）恰好在第 2 步终止的公式。**

    $$
    G_{0:2}=R_1+\gamma R_2.
    $$

    **代入：**

    $$
    G_{0:2}=-0.4+0.5(1)=\boxed{0.1},\qquad
    V_{\mathrm{new}}(A)=0+0.2(0.1-0)=\boxed{0.02}.
    $$

    终止时没有自举项。一般 $n$ 步目标只在 $t+n<T$ 时使用第 $n$ 步的后继估值；$t+n\geq T$ 时只累计到最后一次奖励。

??? success "24：SARSA 与 Q-learning 的两步 Q 表"

    **（1）先列两个目标与共同更新式。**

    $$
    y_{\mathrm{SARSA}}=r+\gamma Q(s',a'),\qquad
    y_{\mathrm Q}=r+\gamma\max_bQ(s',b),
    $$

    $$
    \delta=y-Q(s,a),\qquad Q_{\mathrm{new}}(s,a)=Q(s,a)+\alpha\delta.
    $$

    **代入第一步：** $r=1$，实际下一动作为向下，$Q(B,\downarrow)=1$；最大值为 $Q(B,\rightarrow)=4$。

    | 算法 | Target | TD error | 新 $Q(A,\rightarrow)$ |
    | --- | --- | --- | --- |
    | SARSA | $1+0.9(1)=1.9$ | $1.9-2=-0.1$ | $2+0.2(-0.1)=\boxed{1.98}$ |
    | Q-learning | $1+0.9(4)=4.6$ | $4.6-2=2.6$ | $2+0.2(2.6)=\boxed{2.52}$ |

    **（2）终止更新公式。** 两者在后继终止时均用 $y=r$：

    $$
    Q_{\mathrm{new}}(s,a)=Q(s,a)+\alpha[r-Q(s,a)].
    $$

    **代入第二步：**

    $$
    y=-10,\qquad\delta=-10-1=-11,\qquad
    Q(B,\downarrow)=1+0.2(-11)=\boxed{-1.2}.
    $$

    | 表项 | SARSA 最终值 | Q-learning 最终值 |
    | --- | ---: | ---: |
    | $Q(A,\rightarrow)$ | 1.98 | 2.52 |
    | $Q(B,\rightarrow)$ | 4 | 4 |
    | $Q(B,\downarrow)$ | −1.2 | −1.2 |

    其余表项保持 0。第二步只更新 $(B,\downarrow)$，不会自动回头修改第一步的 $Q(A,\rightarrow)$。

    **（3）动作概率公式。** 非贪心动作的 ε-greedy 概率为 $\epsilon/m$。

    **代入：** 向下不是贪心动作，$\pi(\downarrow\mid B)=0.2/4=\boxed{0.05}$；向右总概率为 $0.8+0.05=0.85$。

    **SARSA（on-policy）**：到达非终止状态 $B$ 后，先按行为策略抽取下一动作向下，再用它的 Q 值构造目标，随后实际执行该动作。因此探索行为直接进入目标，第一步价值略下降。

    **Q-learning（off-policy）**：观察到 $(A,\rightarrow,1,B)$ 后即可用 $\max_bQ(B,b)$ 更新，不需要先知道实际下一动作；行为随后仍可探索向下。它学习的是贪心目标，第一步价值上升。

    终止后两者都无需再选择动作。探索仍决定数据覆盖；在相应有限表格条件下，Q-learning 需要充分访问与合适步长，SARSA 趋于最优还通常要求 GLIE。

## 题目与课件对应

??? note "查看范围页与例题改编说明"

    范围：[Core Checklist，第 3 页](assets/pdf/ELEC6910J_Lec_13_14.pdf#page=3)；[Checklist，第 36 页](assets/pdf/ELEC6910J_Lec_13_14.pdf#page=36)；[Checklist，第 37 页](assets/pdf/ELEC6910J_Lec_13_14.pdf#page=37)。

    | 题目 | 原例题 / 内容 | 本卷改编 |
    | --- | --- | --- |
    | 17 | Lecture 3–4：[餐厅选择 p. 11](assets/pdf/ELEC6910J_Lec_3_4.pdf#page=11)、[增量估计 p. 26](assets/pdf/ELEC6910J_Lec_3_4.pdf#page=26)、[固定步长 p. 32](assets/pdf/ELEC6910J_Lec_3_4.pdf#page=32) | 给定五次采样奖励，设 $\epsilon=0.2,\alpha=0.5$ |
    | 18、19 | Lecture 3–4：[赛车 p. 53](assets/pdf/ELEC6910J_Lec_3_4.pdf#page=53)、[折扣路径 p. 64](assets/pdf/ELEC6910J_Lec_3_4.pdf#page=64)；Lecture 5–6：[赛车迭代 p. 52](assets/pdf/ELEC6910J_Lec_5_6.pdf#page=52) | 保留赛车转移与奖励，改为 $\gamma=0.8$；路径奖励改为立即 2 与延迟 8 |
    | 20 | Lecture 7–8：[GridWorld p. 28–29](assets/pdf/ELEC6910J_Lec_7_8.pdf#page=28) | 缩为 $2\times2$，保留每步 −1、随机策略和撞墙停留，设单个终点 |
    | 21 | Lecture 7–8：[赛车策略迭代 p. 43–44](assets/pdf/ELEC6910J_Lec_7_8.pdf#page=43) | 保留处处 Slow 的初始策略，改为 $\gamma=0.8$，加入矩阵求解 |
    | 22 | Lecture 9–10：[重复访问 p. 14](assets/pdf/ELEC6910J_Lec_9_10.pdf#page=14)、[Soft control p. 29–31](assets/pdf/ELEC6910J_Lec_9_10.pdf#page=29) | 以 $A,B,B,T$ 标注状态，给定奖励、历史计数与单次 Q 更新 |
    | 23 | Lecture 11–12：[Lake p. 34–36](assets/pdf/ELEC6910J_Lec_11_12.pdf#page=34)、[多步 TD p. 47](assets/pdf/ELEC6910J_Lec_11_12.pdf#page=47) | 保留前三次转移，步长改为 0.2；另设两步终止小问 |
    | 24 | Lecture 11–12：[SARSA p. 58](assets/pdf/ELEC6910J_Lec_11_12.pdf#page=58)、[小狗 p. 77–84](assets/pdf/ELEC6910J_Lec_11_12.pdf#page=77) | 保留小骨头与毒药奖励，给定非零初始 Q，改为 $\alpha=0.2,\gamma=0.9$，比较两种控制目标 |
