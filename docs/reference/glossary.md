# Glossary · 术语对照

<p class="chapter-subtitle">保留英文术语，对齐中文含义</p>

## 1. Learning & Decision Making

| English | 中文 | 本课程中的含义 |
| --- | --- | --- |
| Agent | 智能体 | 感知环境并采取行动的实体 |
| Environment | 环境 | 对动作作出响应并产生反馈的系统 |
| Rationality | 理性 | 根据已有信息最大化期望效用 |
| Supervised Learning | 监督学习 | 从输入与标签的配对中学习 |
| Unsupervised Learning | 无监督学习 | 从无标签数据中发现结构 |
| Reinforcement Learning | 强化学习 | 从交互与奖励中学习决策 |
| Regression | 回归 | 预测连续数值 |
| Classification | 分类 | 预测离散类别 |
| Feature | 特征 | 用于预测或决策的输入属性 |
| Exploration | 探索 | 通过尝试获得更多信息 |
| Exploitation | 利用 | 根据现有估计选择较好动作 |
| Regret | 遗憾 | 相对于最优选择的机会损失 |

## 2. Probability

| English | 中文 | 说明 |
| --- | --- | --- |
| Sample Space | 样本空间 | 全部可能结果 |
| Event | 事件 | 样本空间的子集 |
| Random Variable | 随机变量 | 样本点到数值或取值的函数 |
| Joint Distribution | 联合分布 | 多个变量共同取值的概率 |
| Marginalization | 边缘化 | 对其他变量求和或积分 |
| Conditional Probability | 条件概率 | 已知某事件发生后的概率 |
| Normalization | 归一化 | 调整总概率质量为 1 |
| Prior / Posterior | 先验／后验 | 观察证据前后的分布 |
| Independence | 独立 | 联合概率可分解为边缘概率之积 |
| Expectation | 期望 | 按概率加权的平均 |
| Variance | 方差 | 与均值的平方偏差的期望 |
| Standard Deviation | 标准差 | 方差的平方根 |

## 3. MDP & Values

| English | 中文 | 说明 |
| --- | --- | --- |
| State | 状态 | 描述决策所需的当前信息 |
| Observation | 观察 | 智能体实际接收到的信息 |
| Action | 动作 | 智能体可作出的选择 |
| Policy | 策略 | 状态到动作或动作分布的映射 |
| Plan | 计划 | 预先给定的动作序列 |
| Transition Dynamics | 转移动力学 | 环境状态如何随动作变化 |
| Markov Property | 马尔可夫性 | 给定当前状态后无需额外历史 |
| Reward | 奖励 | 一次交互的标量反馈 |
| Return | 回报 | 未来奖励的累计，通常带折扣 |
| Discount Factor | 折扣因子 | 控制未来奖励权重的 $\gamma$ |
| Episode | 回合 | 从起点到终止的一段交互 |
| Terminal State | 终止态 | 回合已结束，无后续回报 |
| State Value | 状态价值 | 从状态出发的期望回报 |
| Action Value / Q-value | 动作价值 | 先做指定动作、之后遵循策略的期望回报 |
| Prediction | 预测／评估 | 计算给定策略的价值 |
| Control | 控制 | 改进策略、寻找最优行为 |

## 4. Algorithms

| English | 中文 | 说明 |
| --- | --- | --- |
| Dynamic Programming | 动态规划 | 利用已知模型与 Bellman 关系求解 |
| Backup | 备份／回传更新 | 将后继信息合并为当前价值 |
| Bootstrapping | 自举 | 用已有估计构造新的更新目标 |
| Value Iteration | 价值迭代 | 反复进行 Bellman 最优备份 |
| Policy Evaluation | 策略评估 | 计算固定策略的价值 |
| Policy Improvement | 策略改进 | 根据当前价值构造更好的策略 |
| Policy Iteration | 策略迭代 | 交替执行评估与改进 |
| Policy Extraction | 策略提取 | 从价值函数中选出动作 |
| Contraction | 压缩映射 | 按严格小于 1 的比例缩小距离 |
| Fixed Point | 不动点 | 经过算子作用后不变的点 |
| Monte Carlo | 蒙特卡洛 | 用采样回报平均估计价值 |
| First-Visit | 首次访问 | 每回合只使用某状态或状态—动作对的第一次访问 |
| Every-Visit | 每次访问 | 使用回合中的全部相应访问 |
| Exploring Starts | 探索性起始 | 各相关状态—动作对都有机会成为起点 |
| Soft Policy | 软策略 | 各可用动作均有正概率 |
| On-policy | 同策略 | 数据生成策略与被评估／改进策略相同 |
| Off-policy | 异策略 | 两种策略可以不同 |
| Usable Ace | 可用 Ace | 在不爆牌的前提下可按 11 计的 Ace |

## 5. 常用符号

| 符号 | 含义 |
| --- | --- |
| $S_t,A_t,R_{t+1}$ | 当前状态、动作、动作之后得到的奖励 |
| $s',a'$ | 后继状态、后继状态中的动作 |
| $\pi(a\mid s)$ | 在 $s$ 下选择 $a$ 的概率 |
| $T(s,a,s')$ | 转移概率；注意与终止时刻 $T$ 区分 |
| $p(s',r\mid s,a)$ | 下一状态与奖励的联合条件分布 |
| $G_t$ | 从时刻 $t$ 开始的回报 |
| $V^\pi,Q^\pi$ | 固定策略下的价值 |
| $V^*,Q^*$ | 最优价值 |
| $\alpha$ | 学习率／步长 |
| $\epsilon$ | 探索概率或软策略参数 |
| $\gamma$ | 折扣因子 |
| $N(s),N(s,a)$ | 纳入统计的访问计数 |
