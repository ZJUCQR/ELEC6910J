# 2: Probability Basics

<p class="chapter-subtitle">概率基础 · 用分布描述不确定性</p>

!!! info "本章对应课件"

    Lecture 2 · <strong>ELEC6910J_Lec_1_2_updated.pdf，p. 50–85</strong>。
    [查看本讲全部课件](../slides/lecture-02.md) · [下载 PDF](../assets/pdf/ELEC6910J_Lec_1_2_updated.pdf)

## 2.1 Uncertainty & Events（不确定性与事件）

课件以“航班起飞前 60 分钟出发去 HKG，能否赶上飞机”为例：路况无法完全观察，传感器有噪声，交通与安检过程复杂，环境模型也不完全已知。概率描述这些不确定性，效用衡量结果好坏，两者共同支持决策。

### 2.1.1 Sets（集合）

- Sample Space $\Omega$（样本空间）：所有可能结果的集合。
- Outcome $\omega$（样本点）：一次具体结果。
- Event $A\subseteq\Omega$（事件）：一组满足条件的结果。
- Union $A\cup B$（并）：$A$ 或 $B$ 至少一个发生。
- Intersection $A\cap B$（交）：两者都发生。
- Complement $A^c$（补）：$A$ 不发生。
- Mutually Exclusive（互斥）：$A\cap B=\varnothing$。

集合运算满足交换律、结合律和分配律。De Morgan's Laws（德摩根律）为：

$$
(A\cap B)^c=A^c\cup B^c,\qquad
(A\cup B)^c=A^c\cap B^c.
$$

### 2.1.2 Basic Laws（离散概率）

$$
P(\omega)\geq 0,\qquad
\sum_{\omega\in\Omega}P(\omega)=1,\qquad
P(A)=\sum_{\omega\in A}P(\omega).
$$

!!! example "原课件例子：公平骰子"

    $\Omega=\{1,2,3,4,5,6\}$，每个结果的概率都是 $1/6$。
    “点数小于 4”对应事件 $\{1,2,3\}$，所以其概率为 $3/6=1/2$。
    “点数为奇数”对应 $\{1,3,5\}$。事件是集合，概率是给这个集合分配的数。

## 2.2 Random Variables & Distributions（随机变量与分布）

Random Variable（随机变量）是定义在样本空间上的函数。结果 $\omega$ 一旦确定，$X(\omega)$ 就确定；不确定的是抽到了哪个结果。

- 布尔变量 Odd：骰子点数是否为奇数。
- 温度 $T\in\{\mathrm{hot},\mathrm{cold}\}$。
- 到机场的时间 $D\in[0,\infty)$。
- 游戏中幽灵的位置：二维网格坐标。

离散随机变量的 Probability Mass Function（PMF，概率质量函数）满足：

$$
P(X=x)=\sum_{\omega:X(\omega)=x}P(\omega).
$$

$P(X)$ 常表示整个分布；$P(X=x)$ 是某个取值的概率。

### 2.2.1 Joint & Marginal Distributions（联合与边缘分布） {#weather-table}

以下保留课件的 Temperature / Weather 联合分布：

| $W\backslash T$ | hot | cold | $P(W)$ |
| --- | ---: | ---: | ---: |
| sun | 0.45 | 0.15 | 0.60 |
| rain | 0.02 | 0.08 | 0.10 |
| fog | 0.03 | 0.27 | 0.30 |
| meteor | 0.00 | 0.00 | 0.00 |
| $P(T)$ | 0.50 | 0.50 | 1.00 |

Marginalization（边缘化，也叫 summing out）：对不关心的变量求和。

$$
P(X=x)=\sum_y P(X=x,Y=y).
$$

{{ slide lec01-02 60 | 天气与温度：沿行或列求和得到边缘分布 }}

!!! example "原课件问题：由联合表计算事件概率"

    1. **hot AND sunny**：直接读取交集，$P(\mathrm{hot},\mathrm{sun})=0.45$。
    2. **hot**：把 hot 列相加，$0.45+0.02+0.03=0.50$。
    3. **hot OR not foggy**：其补事件是 cold AND fog，因此概率为 $1-0.27=0.73$。

    已知联合分布，可以得到边缘分布；仅知道两个边缘分布，一般不能恢复联合分布，因为变量之间的依赖关系尚未确定。

## 2.3 Conditional Probability（条件概率）

在已知 $B$ 发生后，重新计算 $A$ 发生的概率：

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)},\qquad P(B)>0.
$$

!!! example "原课件例子：缩小样本空间"

    50 个等可能结果中，有 8 个属于 $A$，所以 $P(A)=8/50=0.16$。
    若已知 $B$ 发生，只剩下 14 个可能结果，其中 3 个同时属于 $A$，因此 $P(A\mid B)=3/14\approx0.214$。

{{ slide lec01-02 63 | 条件概率：在已知 B 的范围内重新计算比例 }}

### 2.3.1 Normalization（归一化） {#normalization}

已知 $T=\mathrm{cold}$ 时，截取联合表的 cold 列，再除以该列之和：

$$
P(W=\mathrm{sun}\mid T=\mathrm{cold})
=\frac{0.15}{0.50}=0.30.
$$

整列归一化后得到：

| 天气 | sun | rain | fog | meteor |
| --- | ---: | ---: | ---: | ---: |
| $P(W\mid T=\mathrm{cold})$ | 0.30 | 0.16 | 0.54 | 0.00 |
| $P(W\mid T=\mathrm{hot})$ | 0.90 | 0.04 | 0.06 | 0.00 |

每一行分别加起来等于 1；它们对应不同的条件，不能把两行合在一起要求总和为 1。

{{ slide lec01-02 65 | 归一化：固定 cold，乘以 1 / 0.5 }}

!!! warning "不要交换条件"

    $P(\mathrm{sun}\mid\mathrm{cold})=0.30$，而
    $P(\mathrm{cold}\mid\mathrm{sun})=0.15/0.60=0.25$。
    分母代表不同的条件事件。

## 2.4 Product Rule & Total Probability（乘法与全概率）

### 2.4.1 Product / Chain Rule（乘法／链式法则）

$$
P(A,B)=P(A\mid B)P(B)=P(B\mid A)P(A).
$$

例如，$P(\mathrm{sun}\mid\mathrm{hot})P(\mathrm{hot})=0.90\times0.50=0.45$，恢复联合表中的对应项。

对多个变量反复使用：

$$
P(x_1,\ldots,x_n)=\prod_{i=1}^{n}P(x_i\mid x_1,\ldots,x_{i-1}).
$$

链式法则不要求独立。只有得到独立性假设后，才能删去条件。

### 2.4.2 Total Probability（全概率公式）

若 $B_1,\ldots,B_n$ 两两互斥且覆盖整个样本空间，则：

$$
P(A)=\sum_{i=1}^{n}P(A\mid B_i)P(B_i).
$$

例如，天气表中 hot 和 cold 构成一个划分：

$$
P(\mathrm{sun})
=0.90\times0.50+0.30\times0.50=0.60.
$$

Bellman 方程中的“遍历所有动作、后继状态并加权求和”，就会使用这种思路。

## 2.5 Bayes' Rule（贝叶斯公式）

$$
P(B_j\mid A)
=\frac{P(A\mid B_j)P(B_j)}
{\sum_i P(A\mid B_i)P(B_i)}.
$$

- Prior（先验）：观察到证据之前的 $P(B_j)$。
- Likelihood（似然）：假设 $B_j$ 成立时，出现证据 $A$ 的概率。
- Posterior（后验）：看到 $A$ 之后对 $B_j$ 的更新。

!!! example "原课件例子：由症状推断疾病"

    医生可能更容易知道“患某病时出现某症状的概率”。观察到症状后，要反过来推断疾病，就使用 Bayes' Rule。
    分母要考虑所有可能导致该症状的原因；不能直接把“有病时出现症状的概率”当作“有症状时患病的概率”。

对天气表，$P(\mathrm{hot}\mid\mathrm{sun})=0.90\times0.50/0.60=0.75$。

## 2.6 Independence（独立性）

两个事件独立，当且仅当：

$$
P(A,B)=P(A)P(B).
$$

在条件概率有定义时，也等价于 $P(A\mid B)=P(A)$。公平且独立的两次掷骰中：

$$
P(\mathrm{Roll}_1=5,\mathrm{Roll}_2=3)=\frac16\times\frac16=\frac1{36}.
$$

- 独立的 $n$ 次抛硬币不必存一张有 $2^n$ 种组合的联合表，只需存各次的分布。
- 天气表中 $0.45\neq0.50\times0.60$，因此温度与天气不独立。
- **互斥与独立不同**：若两个非零概率事件互斥，发生一个就排除了另一个，它们不独立。

### 2.6.1 Conditional Independence（条件独立）

$$
X\perp Y\mid Z
\quad\Longleftrightarrow\quad
P(X,Y\mid Z)=P(X\mid Z)P(Y\mid Z).
$$

在相应条件概率有定义时，也可写为 $P(X\mid Y,Z)=P(X\mid Z)$。给定 $Z$ 后，$Y$ 不再提供关于 $X$ 的额外信息。第 4 章的 Markov Property 正是这一思想的应用。

## 2.7 Expectation, Variance & Standard Deviation

### 2.7.1 Expectation（期望）

$$
\mathbb E[X]=\sum_x xP(X=x).
$$

期望是按概率加权的平均值，不一定是随机变量实际可以取到的值。公平骰子的期望是 $3.5$，但骰子不会掷出 $3.5$。

### 2.7.2 Variance（方差）

$$
\operatorname{Var}(X)
=\mathbb E[(X-\mathbb E[X])^2]
=\mathbb E[X^2]-(\mathbb E[X])^2.
$$

均值相同的分布，波动范围仍可差别很大。课件用三个均值相同、分散程度不同的分布说明这一点。

{{ slide lec01-02 79 | 同样的期望，不同的分散程度 }}

### 2.7.3 Standard Deviation（标准差）

$$
\operatorname{Std}(X)=\sqrt{\operatorname{Var}(X)}.
$$

标准差与 $X$ 的单位相同，方差的单位则是其平方。例如，用分数衡量成绩时，标准差也以“分”为单位。

!!! tip "和后续章节的联系"

    价值函数是回报的**期望**；Monte Carlo 用样本平均估计期望，而样本回报的**方差**影响估计的稳定程度。理解这两个量，才能理解为什么相同平均表现的策略可能有不同风险。

## 2.8 本章检查

- 联合分布、边缘分布、条件分布分别如何计算？
- 为什么归一化必须除以当前保留部分的总概率？
- 条件独立是否意味着无条件独立？一般不意味着。
- 是否能从天气表独立复算 $0.73$、$0.30$、$0.25$ 和 $0.75$？
