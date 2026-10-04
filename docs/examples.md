# Examples · 例题索引

<p class="chapter-subtitle">从一个具体问题，回到它背后的概念</p>

原课件例子保留在正文与逐页档案中。下表链接到讲解位置；每张截图下面另有对应 PDF 页码。带“补充”的条目为笔记新增的计算或演示。

## 1. Learning & Probability

| 例子 | 复习重点 | 讲解 |
| --- | --- | --- |
| Taxi Driver / PEAS | 分清评价、环境、执行器、传感器 | [第 1 章](chapters/01-introduction.md) |
| 房价、垃圾邮件、手写数字 | 回归、分类、特征与标签 | [第 1 章](chapters/01-introduction.md) |
| 机器翻译、目标检测、词向量 | 不同任务的输入与输出 | [第 1 章](chapters/01-introduction.md) |
| Atari、机器人、Go、Dota 2、StarCraft II | 交互、长时程、多智能体与可观测性 | [第 1 章](chapters/01-introduction.md) |
| 公平骰子 | 样本空间、事件、独立性 | [第 2 章](chapters/02-probability.md) |
| 天气与温度联合表 | 边缘化、交集与并集 | [概率表与事件计算](chapters/02-probability.md#weather-table) |
| 已知 cold 后的天气分布 | 条件概率与归一化 | [归一化例题](chapters/02-probability.md#normalization) |
| 症状与疾病 | 由结果反推原因，Bayes' Rule | [第 2 章](chapters/02-probability.md) |
| 相同期望、不同分散程度 | 方差与标准差 | [第 2 章](chapters/02-probability.md) |

## 2. Bandits & MDPs

| 例子 | 复习重点 | 讲解 |
| --- | --- | --- |
| 广告点击、LG1 / LG7 | 动作、奖励与状态演化的边界 | [餐厅与广告](chapters/03-bandits.md#restaurants) |
| 餐厅、钻井、游戏招法 | 探索与利用 | [第 3 章](chapters/03-bandits.md) |
| 4 个动作的 $\epsilon$-greedy（补充） | 随机分支也能选中贪心动作 | [概率计算](chapters/03-bandits.md#epsilon-greedy) |
| 从 $(1,1)$ 向 north 移动 | 噪声、撞墙与转移概率 | [GridWorld 建模](chapters/04-mdp.md#gridworld) |
| Cool / Warm / Overheated | 用状态表写出赛车 MDP | [赛车模型](chapters/04-mdp.md#racing) |
| 从 $d$ 走向 $a$ 或 $e$ | 延迟奖励与折扣指数 | [折扣 Quiz](chapters/04-mdp.md#discount-quiz) |

## 3. Dynamic Programming

| 例子 | 复习重点 | 讲解 |
| --- | --- | --- |
| GridWorld 的 $V,Q,\pi$ 图 | 价值与动作的三种表示 | [第 5 章](chapters/05-bellman.md) |
| 五状态线性系统 | 分支概率相乘、终止态取 0 | [方程与近似解](chapters/06-value-iteration.md#linear-system) |
| 赛车的前两轮更新 | 同步更新；$\gamma=1$ 的有限步演示 | [手算过程](chapters/06-value-iteration.md#racing-iterations) |
| 赛车交互演示（补充） | 改变折扣，观察数值与动作 | [动手迭代](chapters/06-value-iteration.md#racing-lab) |
| GridWorld 的 $0.72$ | 价值从出口向外传播 | [一步 backup](chapters/06-value-iteration.md#gridworld-backup) |
| $\gamma=0.5$ 的赛车 | 与未折扣有限步结果区分 | [折扣迭代表](chapters/07-policy-evaluation.md#discounted-racing) |
| 4×4 GridWorld | 评估均匀随机策略与期望步数 | [策略评估](chapters/07-policy-evaluation.md#gridworld-evaluation) |
| 赛车从 Slow / Slow 开始 | 先评估，再改进，最后稳定 | [策略迭代全过程](chapters/08-policy-iteration.md#racing-policy-iteration) |

## 4. Monte Carlo

| 例子 | 复习重点 | 讲解 |
| --- | --- | --- |
| 同一回合多次访问目标状态 | First-Visit 与 Every-Visit 的样本集合 | [原图与公式核对](chapters/09-mc-prediction.md#first-every) |
| 增量 MC 代码（补充） | 回报反向算，首次访问按正向判断 | [第 9 章](chapters/09-mc-prediction.md) |
| 软策略的概率预算 | $\epsilon$-soft 与 $\epsilon$-greedy | [定义与改进推导](chapters/10-mc-control.md#soft-policies) |
| Blackjack | 200 个状态、usable ace、终局回报 | [规则、建模与评估](chapters/10-mc-control.md#blackjack) |

!!! tip "练习方法"

    先根据文字独立列式，再看截图与讲解核对。赛车例题先写清 $\gamma$；GridWorld 先确认终止状态与 living reward；Monte Carlo 先标出每一次访问的时间点。
