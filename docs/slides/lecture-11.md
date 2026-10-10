---
hide:
  - toc
---

# L11 · Temporal Difference Prediction

时序差分预测与多步回报 · PDF 第 **1–50** 页 · 共 **50** 页。

[下载本组 PDF](../assets/pdf/ELEC6910J_Lec_11_12.pdf){ .md-button }

点击页标题展开原页，点击图片放大。页码采用 PDF 的物理页序，便于与文件对应。


<div class="archive-tools"><label for="slide-filter">定位课件</label><input id="slide-filter" type="search" placeholder="输入页码或英文标题" autocomplete="off"><span id="slide-filter-count" role="status" aria-live="polite"></span></div>

<details class="slide-page" id="p001" open>
<summary><span class="page-number">001</span> ELEC6910J</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/001.webp" class="slide-zoom" aria-label="放大：第 1 页 ELEC6910J"><img src="../../assets/slides/lec11-12/001.webp" alt="第 1 页：ELEC6910J" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 1 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=1">在 PDF 中查看</a> · <a href="#p001">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p002">
<summary><span class="page-number">002</span> Announcements</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/002.webp" class="slide-zoom" aria-label="放大：第 2 页 Announcements"><img src="../../assets/slides/lec11-12/002.webp" alt="第 2 页：Announcements" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 2 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=2">在 PDF 中查看</a> · <a href="#p002">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p003">
<summary><span class="page-number">003</span> Recap: Policy Evaluation</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/003.webp" class="slide-zoom" aria-label="放大：第 3 页 Recap: Policy Evaluation"><img src="../../assets/slides/lec11-12/003.webp" alt="第 3 页：Recap: Policy Evaluation" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 3 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=3">在 PDF 中查看</a> · <a href="#p003">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p004">
<summary><span class="page-number">004</span> Recap: Policy Improvement</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/004.webp" class="slide-zoom" aria-label="放大：第 4 页 Recap: Policy Improvement"><img src="../../assets/slides/lec11-12/004.webp" alt="第 4 页：Recap: Policy Improvement" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 4 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=4">在 PDF 中查看</a> · <a href="#p004">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p005">
<summary><span class="page-number">005</span> Recap: Policy Iteration</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/005.webp" class="slide-zoom" aria-label="放大：第 5 页 Recap: Policy Iteration"><img src="../../assets/slides/lec11-12/005.webp" alt="第 5 页：Recap: Policy Iteration" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 5 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=5">在 PDF 中查看</a> · <a href="#p005">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p006">
<summary><span class="page-number">006</span> Recap: Problems of DP</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/006.webp" class="slide-zoom" aria-label="放大：第 6 页 Recap: Problems of DP"><img src="../../assets/slides/lec11-12/006.webp" alt="第 6 页：Recap: Problems of DP" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 6 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=6">在 PDF 中查看</a> · <a href="#p006">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p007">
<summary><span class="page-number">007</span> Recap: Monte-Carlo Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/007.webp" class="slide-zoom" aria-label="放大：第 7 页 Recap: Monte-Carlo Prediction"><img src="../../assets/slides/lec11-12/007.webp" alt="第 7 页：Recap: Monte-Carlo Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 7 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=7">在 PDF 中查看</a> · <a href="#p007">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p008">
<summary><span class="page-number">008</span> Recap: Monte-Carlo Control</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/008.webp" class="slide-zoom" aria-label="放大：第 8 页 Recap: Monte-Carlo Control"><img src="../../assets/slides/lec11-12/008.webp" alt="第 8 页：Recap: Monte-Carlo Control" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 8 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=8">在 PDF 中查看</a> · <a href="#p008">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p009">
<summary><span class="page-number">009</span> Recap: Monte-Carlo Control with Exploring Starts</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/009.webp" class="slide-zoom" aria-label="放大：第 9 页 Recap: Monte-Carlo Control with Exploring Starts"><img src="../../assets/slides/lec11-12/009.webp" alt="第 9 页：Recap: Monte-Carlo Control with Exploring Starts" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 9 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=9">在 PDF 中查看</a> · <a href="#p009">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p010">
<summary><span class="page-number">010</span> Recap: Monte-Carlo Control with Soft Policies</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/010.webp" class="slide-zoom" aria-label="放大：第 10 页 Recap: Monte-Carlo Control with Soft Policies"><img src="../../assets/slides/lec11-12/010.webp" alt="第 10 页：Recap: Monte-Carlo Control with Soft Policies" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 10 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=10">在 PDF 中查看</a> · <a href="#p010">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p011">
<summary><span class="page-number">011</span> Recap: Dynamic Programming v.s. Monte Carlo</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/011.webp" class="slide-zoom" aria-label="放大：第 11 页 Recap: Dynamic Programming v.s. Monte Carlo"><img src="../../assets/slides/lec11-12/011.webp" alt="第 11 页：Recap: Dynamic Programming v.s. Monte Carlo" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 11 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=11">在 PDF 中查看</a> · <a href="#p011">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p012">
<summary><span class="page-number">012</span> Temporal Difference (TD) Learning</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/012.webp" class="slide-zoom" aria-label="放大：第 12 页 Temporal Difference (TD) Learning"><img src="../../assets/slides/lec11-12/012.webp" alt="第 12 页：Temporal Difference (TD) Learning" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 12 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=12">在 PDF 中查看</a> · <a href="#p012">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p013">
<summary><span class="page-number">013</span> Motivation: Why Not Use Bellman Updates?</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/013.webp" class="slide-zoom" aria-label="放大：第 13 页 Motivation: Why Not Use Bellman Updates?"><img src="../../assets/slides/lec11-12/013.webp" alt="第 13 页：Motivation: Why Not Use Bellman Updates?" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 13 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=13">在 PDF 中查看</a> · <a href="#p013">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p014">
<summary><span class="page-number">014</span> Idea: Sample-based Updates</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/014.webp" class="slide-zoom" aria-label="放大：第 14 页 Idea: Sample-based Updates"><img src="../../assets/slides/lec11-12/014.webp" alt="第 14 页：Idea: Sample-based Updates" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 14 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=14">在 PDF 中查看</a> · <a href="#p014">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p015">
<summary><span class="page-number">015</span> Idea: Sample-based Updates</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/015.webp" class="slide-zoom" aria-label="放大：第 15 页 Idea: Sample-based Updates"><img src="../../assets/slides/lec11-12/015.webp" alt="第 15 页：Idea: Sample-based Updates" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 15 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=15">在 PDF 中查看</a> · <a href="#p015">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p016">
<summary><span class="page-number">016</span> Idea: Sampled-Based Bellman Updates</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/016.webp" class="slide-zoom" aria-label="放大：第 16 页 Idea: Sampled-Based Bellman Updates"><img src="../../assets/slides/lec11-12/016.webp" alt="第 16 页：Idea: Sampled-Based Bellman Updates" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 16 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=16">在 PDF 中查看</a> · <a href="#p016">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p017">
<summary><span class="page-number">017</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/017.webp" class="slide-zoom" aria-label="放大：第 17 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/017.webp" alt="第 17 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 17 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=17">在 PDF 中查看</a> · <a href="#p017">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p018">
<summary><span class="page-number">018</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/018.webp" class="slide-zoom" aria-label="放大：第 18 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/018.webp" alt="第 18 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 18 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=18">在 PDF 中查看</a> · <a href="#p018">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p019">
<summary><span class="page-number">019</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/019.webp" class="slide-zoom" aria-label="放大：第 19 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/019.webp" alt="第 19 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 19 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=19">在 PDF 中查看</a> · <a href="#p019">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p020">
<summary><span class="page-number">020</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/020.webp" class="slide-zoom" aria-label="放大：第 20 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/020.webp" alt="第 20 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 20 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=20">在 PDF 中查看</a> · <a href="#p020">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p021">
<summary><span class="page-number">021</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/021.webp" class="slide-zoom" aria-label="放大：第 21 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/021.webp" alt="第 21 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 21 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=21">在 PDF 中查看</a> · <a href="#p021">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p022">
<summary><span class="page-number">022</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/022.webp" class="slide-zoom" aria-label="放大：第 22 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/022.webp" alt="第 22 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 22 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=22">在 PDF 中查看</a> · <a href="#p022">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p023">
<summary><span class="page-number">023</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/023.webp" class="slide-zoom" aria-label="放大：第 23 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/023.webp" alt="第 23 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 23 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=23">在 PDF 中查看</a> · <a href="#p023">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p024">
<summary><span class="page-number">024</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/024.webp" class="slide-zoom" aria-label="放大：第 24 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/024.webp" alt="第 24 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 24 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=24">在 PDF 中查看</a> · <a href="#p024">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p025">
<summary><span class="page-number">025</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/025.webp" class="slide-zoom" aria-label="放大：第 25 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/025.webp" alt="第 25 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 25 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=25">在 PDF 中查看</a> · <a href="#p025">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p026">
<summary><span class="page-number">026</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/026.webp" class="slide-zoom" aria-label="放大：第 26 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/026.webp" alt="第 26 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 26 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=26">在 PDF 中查看</a> · <a href="#p026">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p027">
<summary><span class="page-number">027</span> Comparison</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/027.webp" class="slide-zoom" aria-label="放大：第 27 页 Comparison"><img src="../../assets/slides/lec11-12/027.webp" alt="第 27 页：Comparison" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 27 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=27">在 PDF 中查看</a> · <a href="#p027">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p028">
<summary><span class="page-number">028</span> Bias v.s. Variance</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/028.webp" class="slide-zoom" aria-label="放大：第 28 页 Bias v.s. Variance"><img src="../../assets/slides/lec11-12/028.webp" alt="第 28 页：Bias v.s. Variance" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 28 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=28">在 PDF 中查看</a> · <a href="#p028">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p029">
<summary><span class="page-number">029</span> Bias v.s. Variance</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/029.webp" class="slide-zoom" aria-label="放大：第 29 页 Bias v.s. Variance"><img src="../../assets/slides/lec11-12/029.webp" alt="第 29 页：Bias v.s. Variance" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 29 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=29">在 PDF 中查看</a> · <a href="#p029">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p030">
<summary><span class="page-number">030</span> Bias v.s. Variance</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/030.webp" class="slide-zoom" aria-label="放大：第 30 页 Bias v.s. Variance"><img src="../../assets/slides/lec11-12/030.webp" alt="第 30 页：Bias v.s. Variance" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 30 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=30">在 PDF 中查看</a> · <a href="#p030">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p031">
<summary><span class="page-number">031</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/031.webp" class="slide-zoom" aria-label="放大：第 31 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/031.webp" alt="第 31 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 31 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=31">在 PDF 中查看</a> · <a href="#p031">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p032">
<summary><span class="page-number">032</span> Comparison: TD Methods Bootstrap and Sample</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/032.webp" class="slide-zoom" aria-label="放大：第 32 页 Comparison: TD Methods Bootstrap and Sample"><img src="../../assets/slides/lec11-12/032.webp" alt="第 32 页：Comparison: TD Methods Bootstrap and Sample" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 32 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=32">在 PDF 中查看</a> · <a href="#p032">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p033">
<summary><span class="page-number">033</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/033.webp" class="slide-zoom" aria-label="放大：第 33 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/033.webp" alt="第 33 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 33 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=33">在 PDF 中查看</a> · <a href="#p033">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p034">
<summary><span class="page-number">034</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/034.webp" class="slide-zoom" aria-label="放大：第 34 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/034.webp" alt="第 34 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 34 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=34">在 PDF 中查看</a> · <a href="#p034">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p035">
<summary><span class="page-number">035</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/035.webp" class="slide-zoom" aria-label="放大：第 35 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/035.webp" alt="第 35 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 35 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=35">在 PDF 中查看</a> · <a href="#p035">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p036">
<summary><span class="page-number">036</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/036.webp" class="slide-zoom" aria-label="放大：第 36 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/036.webp" alt="第 36 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 36 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=36">在 PDF 中查看</a> · <a href="#p036">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p037">
<summary><span class="page-number">037</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/037.webp" class="slide-zoom" aria-label="放大：第 37 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/037.webp" alt="第 37 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 37 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=37">在 PDF 中查看</a> · <a href="#p037">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p038">
<summary><span class="page-number">038</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/038.webp" class="slide-zoom" aria-label="放大：第 38 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/038.webp" alt="第 38 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 38 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=38">在 PDF 中查看</a> · <a href="#p038">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p039">
<summary><span class="page-number">039</span> Temporal Difference Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/039.webp" class="slide-zoom" aria-label="放大：第 39 页 Temporal Difference Prediction"><img src="../../assets/slides/lec11-12/039.webp" alt="第 39 页：Temporal Difference Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 39 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=39">在 PDF 中查看</a> · <a href="#p039">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p040">
<summary><span class="page-number">040</span> Unified View of Reinforcement Learning</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/040.webp" class="slide-zoom" aria-label="放大：第 40 页 Unified View of Reinforcement Learning"><img src="../../assets/slides/lec11-12/040.webp" alt="第 40 页：Unified View of Reinforcement Learning" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 40 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=40">在 PDF 中查看</a> · <a href="#p040">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p041">
<summary><span class="page-number">041</span> Unifying MC and TD(0)</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/041.webp" class="slide-zoom" aria-label="放大：第 41 页 Unifying MC and TD(0)"><img src="../../assets/slides/lec11-12/041.webp" alt="第 41 页：Unifying MC and TD(0)" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 41 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=41">在 PDF 中查看</a> · <a href="#p041">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p042">
<summary><span class="page-number">042</span> Unifying MC and TD(0)</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/042.webp" class="slide-zoom" aria-label="放大：第 42 页 Unifying MC and TD(0)"><img src="../../assets/slides/lec11-12/042.webp" alt="第 42 页：Unifying MC and TD(0)" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 42 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=42">在 PDF 中查看</a> · <a href="#p042">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p043">
<summary><span class="page-number">043</span> Unifying MC and TD(0)</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/043.webp" class="slide-zoom" aria-label="放大：第 43 页 Unifying MC and TD(0)"><img src="../../assets/slides/lec11-12/043.webp" alt="第 43 页：Unifying MC and TD(0)" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 43 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=43">在 PDF 中查看</a> · <a href="#p043">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p044">
<summary><span class="page-number">044</span> Unifying MC and TD(0)</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/044.webp" class="slide-zoom" aria-label="放大：第 44 页 Unifying MC and TD(0)"><img src="../../assets/slides/lec11-12/044.webp" alt="第 44 页：Unifying MC and TD(0)" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 44 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=44">在 PDF 中查看</a> · <a href="#p044">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p045">
<summary><span class="page-number">045</span> 𝑛-Step TD Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/045.webp" class="slide-zoom" aria-label="放大：第 45 页 𝑛-Step TD Prediction"><img src="../../assets/slides/lec11-12/045.webp" alt="第 45 页：𝑛-Step TD Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 45 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=45">在 PDF 中查看</a> · <a href="#p045">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p046">
<summary><span class="page-number">046</span> 𝑛-Step TD Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/046.webp" class="slide-zoom" aria-label="放大：第 46 页 𝑛-Step TD Prediction"><img src="../../assets/slides/lec11-12/046.webp" alt="第 46 页：𝑛-Step TD Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 46 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=46">在 PDF 中查看</a> · <a href="#p046">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p047">
<summary><span class="page-number">047</span> 𝑛-Step TD Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/047.webp" class="slide-zoom" aria-label="放大：第 47 页 𝑛-Step TD Prediction"><img src="../../assets/slides/lec11-12/047.webp" alt="第 47 页：𝑛-Step TD Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 47 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=47">在 PDF 中查看</a> · <a href="#p047">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p048">
<summary><span class="page-number">048</span> 𝑛-Step TD Prediction</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/048.webp" class="slide-zoom" aria-label="放大：第 48 页 𝑛-Step TD Prediction"><img src="../../assets/slides/lec11-12/048.webp" alt="第 48 页：𝑛-Step TD Prediction" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 48 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=48">在 PDF 中查看</a> · <a href="#p048">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p049">
<summary><span class="page-number">049</span> Model-free Estimation</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/049.webp" class="slide-zoom" aria-label="放大：第 49 页 Model-free Estimation"><img src="../../assets/slides/lec11-12/049.webp" alt="第 49 页：Model-free Estimation" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 49 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=49">在 PDF 中查看</a> · <a href="#p049">本页链接</a></figcaption>
</figure>
</details>

<details class="slide-page" id="p050">
<summary><span class="page-number">050</span> Learning Action-Value Function</summary>
<figure class="slide-figure">
<a href="../../assets/slides/lec11-12/050.webp" class="slide-zoom" aria-label="放大：第 50 页 Learning Action-Value Function"><img src="../../assets/slides/lec11-12/050.webp" alt="第 50 页：Learning Action-Value Function" width="1600" height="901" loading="lazy" decoding="async"></a>
<figcaption>PDF p. 50 · <a href="../../assets/pdf/ELEC6910J_Lec_11_12.pdf#page=50">在 PDF 中查看</a> · <a href="#p050">本页链接</a></figcaption>
</figure>
</details>
