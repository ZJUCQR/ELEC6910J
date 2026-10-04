---
hide:
  - toc
---

# L5 · Value Functions & Bellman Equations

价值函数与贝尔曼方程 · PDF 第 **1–35** 页 · 共 **35** 页。

[下载本组 PDF](../assets/pdf/ELEC6910J_Lec_5_6.pdf){ .md-button }

点击页标题展开原页，点击图片放大。页码采用 PDF 的物理页序，便于与文件对应。


<div class="archive-tools"><label for="slide-filter">定位课件</label><input id="slide-filter" type="search" placeholder="输入页码或英文标题" autocomplete="off"><span id="slide-filter-count" role="status" aria-live="polite"></span></div>

<details class="slide-page" id="p001" open>
<summary><span class="page-number">001</span> ELEC6910J</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/001.webp" class="slide-zoom" aria-label="放大：第 1 页 ELEC6910J"><img src="../../assets/slides/lec05-06/001.webp" alt="第 1 页：ELEC6910J" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 1 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=1">在 PDF 中查看</a> · <a href="#p001">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p002">
<summary><span class="page-number">002</span> Recap: Multi-Armed Bandits</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/002.webp" class="slide-zoom" aria-label="放大：第 2 页 Recap: Multi-Armed Bandits"><img src="../../assets/slides/lec05-06/002.webp" alt="第 2 页：Recap: Multi-Armed Bandits" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 2 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=2">在 PDF 中查看</a> · <a href="#p002">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p003">
<summary><span class="page-number">003</span> Recap: Exploration/Exploitation Dilemma</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/003.webp" class="slide-zoom" aria-label="放大：第 3 页 Recap: Exploration/Exploitation Dilemma"><img src="../../assets/slides/lec05-06/003.webp" alt="第 3 页：Recap: Exploration/Exploitation Dilemma" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 3 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=3">在 PDF 中查看</a> · <a href="#p003">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p004">
<summary><span class="page-number">004</span> Recap: Forming Action-Value Estimates</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/004.webp" class="slide-zoom" aria-label="放大：第 4 页 Recap: Forming Action-Value Estimates"><img src="../../assets/slides/lec05-06/004.webp" alt="第 4 页：Recap: Forming Action-Value Estimates" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 4 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=4">在 PDF 中查看</a> · <a href="#p004">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p005">
<summary><span class="page-number">005</span> Recap: Epsilon-Greedy Action Selection</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/005.webp" class="slide-zoom" aria-label="放大：第 5 页 Recap: Epsilon-Greedy Action Selection"><img src="../../assets/slides/lec05-06/005.webp" alt="第 5 页：Recap: Epsilon-Greedy Action Selection" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 5 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=5">在 PDF 中查看</a> · <a href="#p005">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p006">
<summary><span class="page-number">006</span> Recap: Markov Decision Process (MDP)</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/006.webp" class="slide-zoom" aria-label="放大：第 6 页 Recap: Markov Decision Process (MDP)"><img src="../../assets/slides/lec05-06/006.webp" alt="第 6 页：Recap: Markov Decision Process (MDP)" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 6 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=6">在 PDF 中查看</a> · <a href="#p006">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p007">
<summary><span class="page-number">007</span> Recap: Markov Decision Process (MDP)</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/007.webp" class="slide-zoom" aria-label="放大：第 7 页 Recap: Markov Decision Process (MDP)"><img src="../../assets/slides/lec05-06/007.webp" alt="第 7 页：Recap: Markov Decision Process (MDP)" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 7 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=7">在 PDF 中查看</a> · <a href="#p007">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p008">
<summary><span class="page-number">008</span> Recap: Markov Decision Process (MDP)</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/008.webp" class="slide-zoom" aria-label="放大：第 8 页 Recap: Markov Decision Process (MDP)"><img src="../../assets/slides/lec05-06/008.webp" alt="第 8 页：Recap: Markov Decision Process (MDP)" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 8 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=8">在 PDF 中查看</a> · <a href="#p008">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p009">
<summary><span class="page-number">009</span> Recap: Discounted Return</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/009.webp" class="slide-zoom" aria-label="放大：第 9 页 Recap: Discounted Return"><img src="../../assets/slides/lec05-06/009.webp" alt="第 9 页：Recap: Discounted Return" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 9 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=9">在 PDF 中查看</a> · <a href="#p009">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p010">
<summary><span class="page-number">010</span> Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/010.webp" class="slide-zoom" aria-label="放大：第 10 页 Value Functions"><img src="../../assets/slides/lec05-06/010.webp" alt="第 10 页：Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 10 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=10">在 PDF 中查看</a> · <a href="#p010">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p011">
<summary><span class="page-number">011</span> Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/011.webp" class="slide-zoom" aria-label="放大：第 11 页 Value Functions"><img src="../../assets/slides/lec05-06/011.webp" alt="第 11 页：Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 11 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=11">在 PDF 中查看</a> · <a href="#p011">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p012">
<summary><span class="page-number">012</span> Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/012.webp" class="slide-zoom" aria-label="放大：第 12 页 Value Functions"><img src="../../assets/slides/lec05-06/012.webp" alt="第 12 页：Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 12 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=12">在 PDF 中查看</a> · <a href="#p012">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p013">
<summary><span class="page-number">013</span> 𝑉∗(𝑠)Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/013.webp" class="slide-zoom" aria-label="放大：第 13 页 𝑉∗(𝑠)Value Functions"><img src="../../assets/slides/lec05-06/013.webp" alt="第 13 页：𝑉∗(𝑠)Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 13 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=13">在 PDF 中查看</a> · <a href="#p013">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p014">
<summary><span class="page-number">014</span> 𝑉∗(𝑠)Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/014.webp" class="slide-zoom" aria-label="放大：第 14 页 𝑉∗(𝑠)Value Functions"><img src="../../assets/slides/lec05-06/014.webp" alt="第 14 页：𝑉∗(𝑠)Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 14 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=14">在 PDF 中查看</a> · <a href="#p014">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p015">
<summary><span class="page-number">015</span> 𝑉∗(𝑠)Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/015.webp" class="slide-zoom" aria-label="放大：第 15 页 𝑉∗(𝑠)Value Functions"><img src="../../assets/slides/lec05-06/015.webp" alt="第 15 页：𝑉∗(𝑠)Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 15 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=15">在 PDF 中查看</a> · <a href="#p015">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p016">
<summary><span class="page-number">016</span> Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/016.webp" class="slide-zoom" aria-label="放大：第 16 页 Value Functions"><img src="../../assets/slides/lec05-06/016.webp" alt="第 16 页：Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 16 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=16">在 PDF 中查看</a> · <a href="#p016">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p017">
<summary><span class="page-number">017</span> Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/017.webp" class="slide-zoom" aria-label="放大：第 17 页 Value Functions"><img src="../../assets/slides/lec05-06/017.webp" alt="第 17 页：Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 17 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=17">在 PDF 中查看</a> · <a href="#p017">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p018">
<summary><span class="page-number">018</span> Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/018.webp" class="slide-zoom" aria-label="放大：第 18 页 Value Functions"><img src="../../assets/slides/lec05-06/018.webp" alt="第 18 页：Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 18 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=18">在 PDF 中查看</a> · <a href="#p018">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p019">
<summary><span class="page-number">019</span> Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/019.webp" class="slide-zoom" aria-label="放大：第 19 页 Value Functions"><img src="../../assets/slides/lec05-06/019.webp" alt="第 19 页：Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 19 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=19">在 PDF 中查看</a> · <a href="#p019">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p020">
<summary><span class="page-number">020</span> Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/020.webp" class="slide-zoom" aria-label="放大：第 20 页 Value Functions"><img src="../../assets/slides/lec05-06/020.webp" alt="第 20 页：Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 20 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=20">在 PDF 中查看</a> · <a href="#p020">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p021">
<summary><span class="page-number">021</span> Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/021.webp" class="slide-zoom" aria-label="放大：第 21 页 Value Functions"><img src="../../assets/slides/lec05-06/021.webp" alt="第 21 页：Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 21 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=21">在 PDF 中查看</a> · <a href="#p021">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p022">
<summary><span class="page-number">022</span> Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/022.webp" class="slide-zoom" aria-label="放大：第 22 页 Value Functions"><img src="../../assets/slides/lec05-06/022.webp" alt="第 22 页：Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 22 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=22">在 PDF 中查看</a> · <a href="#p022">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p023">
<summary><span class="page-number">023</span> Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/023.webp" class="slide-zoom" aria-label="放大：第 23 页 Value Functions"><img src="../../assets/slides/lec05-06/023.webp" alt="第 23 页：Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 23 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=23">在 PDF 中查看</a> · <a href="#p023">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p024">
<summary><span class="page-number">024</span> Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/024.webp" class="slide-zoom" aria-label="放大：第 24 页 Value Functions"><img src="../../assets/slides/lec05-06/024.webp" alt="第 24 页：Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 24 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=24">在 PDF 中查看</a> · <a href="#p024">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p025">
<summary><span class="page-number">025</span> Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/025.webp" class="slide-zoom" aria-label="放大：第 25 页 Value Functions"><img src="../../assets/slides/lec05-06/025.webp" alt="第 25 页：Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 25 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=25">在 PDF 中查看</a> · <a href="#p025">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p026">
<summary><span class="page-number">026</span> Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/026.webp" class="slide-zoom" aria-label="放大：第 26 页 Value Functions"><img src="../../assets/slides/lec05-06/026.webp" alt="第 26 页：Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 26 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=26">在 PDF 中查看</a> · <a href="#p026">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p027">
<summary><span class="page-number">027</span> Markov Decision Process (MDP)</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/027.webp" class="slide-zoom" aria-label="放大：第 27 页 Markov Decision Process (MDP)"><img src="../../assets/slides/lec05-06/027.webp" alt="第 27 页：Markov Decision Process (MDP)" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 27 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=27">在 PDF 中查看</a> · <a href="#p027">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p028">
<summary><span class="page-number">028</span> Optimal Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/028.webp" class="slide-zoom" aria-label="放大：第 28 页 Optimal Value Functions"><img src="../../assets/slides/lec05-06/028.webp" alt="第 28 页：Optimal Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 28 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=28">在 PDF 中查看</a> · <a href="#p028">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p029">
<summary><span class="page-number">029</span> Bellman Equation for V</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/029.webp" class="slide-zoom" aria-label="放大：第 29 页 Bellman Equation for V"><img src="../../assets/slides/lec05-06/029.webp" alt="第 29 页：Bellman Equation for V" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 29 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=29">在 PDF 中查看</a> · <a href="#p029">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p030">
<summary><span class="page-number">030</span> σ𝑎𝜋𝑎𝑠…</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/030.webp" class="slide-zoom" aria-label="放大：第 30 页 σ𝑎𝜋𝑎𝑠…"><img src="../../assets/slides/lec05-06/030.webp" alt="第 30 页：σ𝑎𝜋𝑎𝑠…" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 30 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=30">在 PDF 中查看</a> · <a href="#p030">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p031">
<summary><span class="page-number">031</span> Summary: Bellman equation for Q</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/031.webp" class="slide-zoom" aria-label="放大：第 31 页 Summary: Bellman equation for Q"><img src="../../assets/slides/lec05-06/031.webp" alt="第 31 页：Summary: Bellman equation for Q" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 31 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=31">在 PDF 中查看</a> · <a href="#p031">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p032">
<summary><span class="page-number">032</span> Optimal Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/032.webp" class="slide-zoom" aria-label="放大：第 32 页 Optimal Value Functions"><img src="../../assets/slides/lec05-06/032.webp" alt="第 32 页：Optimal Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 32 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=32">在 PDF 中查看</a> · <a href="#p032">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p033">
<summary><span class="page-number">033</span> Optimal Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/033.webp" class="slide-zoom" aria-label="放大：第 33 页 Optimal Value Functions"><img src="../../assets/slides/lec05-06/033.webp" alt="第 33 页：Optimal Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 33 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=33">在 PDF 中查看</a> · <a href="#p033">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p034">
<summary><span class="page-number">034</span> Value Functions</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/034.webp" class="slide-zoom" aria-label="放大：第 34 页 Value Functions"><img src="../../assets/slides/lec05-06/034.webp" alt="第 34 页：Value Functions" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 34 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=34">在 PDF 中查看</a> · <a href="#p034">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p035">
<summary><span class="page-number">035</span> Problem: How to solve these equations?</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec05-06/035.webp" class="slide-zoom" aria-label="放大：第 35 页 Problem: How to solve these equations?"><img src="../../assets/slides/lec05-06/035.webp" alt="第 35 页：Problem: How to solve these equations?" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 35 · <a href="../../assets/pdf/ELEC6910J_Lec_5_6.pdf#page=35">在 PDF 中查看</a> · <a href="#p035">本页链接</a></figcaption>
</figure>
</details>
