# ELEC6910J · 深度强化学习笔记

[在线阅读](https://zjucqr.github.io/ELEC6910J/) · [内容规划](PLAN.md)

根据 HKUST Ling PAN 老师的五份 ELEC6910J 课件整理的中文课程笔记。涵盖 Lecture 1–10：导论、概率、Bandits、MDP、Bellman 方程、动态规划与 Monte Carlo。

- 10 章中文讲解，保留英文术语、公式、原课件实例与页码。
- 329 页截图档案、5 份公开 PDF；公式速查与术语表汇总在课程笔记主页。
- 桌面三栏阅读、手机导航、中英文搜索、图片放大、深浅主题。
- 赛车价值迭代演示，使用与课件相同的转移模型。

## 本地预览

~~~sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m mkdocs serve
~~~

访问终端显示的本地地址。所有 PDF、截图与 KaTeX 资源已放在仓库中，常规构建无需重新渲染课件。

## 构建与检查

~~~sh
python -m pip install -r requirements-dev.txt
python -m mkdocs build --strict
python scripts/check_site.py
~~~

检查包括本地链接、页码锚点、329 页覆盖、示例计算，以及正文中的首次访问 MC 实现。

浏览器验收脚本为 scripts/check_browser.py。先安装 Chromium，再以实际 Pages 路径提供预览：

~~~sh
python -m playwright install chromium
mkdir -p .work/preview
ln -sfn ../../site .work/preview/ELEC6910J
python -m http.server 8765 --directory .work/preview
~~~

在另一个终端运行：

~~~sh
python scripts/check_browser.py
~~~

脚本检查全部页面公式、中文／英文搜索、课件定位、图片预览、赛车交互、主题与手机布局，截图和报告输出到被 Git 忽略的 .work 目录。

## 内容维护

| 路径 | 用途 |
| --- | --- |
| docs/index.md | 课程笔记主页、公式速查与术语对照 |
| docs/chapters/ | 十章正文 |
| docs/reference/ | 来源与勘误，以及公式、术语旧地址的跳转 |
| docs/slides/ | 按讲次划分的逐页档案 |
| docs/assets/pdf/ | 已检查的公开 PDF |
| docs/assets/slides/ | 1600px 课件截图 |
| docs/assets/manifest.json | 页码、标题、尺寸与公开 PDF 校验值 |
| course.json | 文件与章节映射 |
| scripts/prepare_materials.py | 生成公开 PDF、截图与档案 |
| scripts/hooks.py | 统一渲染正文中的课件引用 |
| docs/assets/stylesheets/extra.css | 视觉样式 |
| docs/assets/javascripts/site.js | 公式、图片预览、档案过滤、赛车演示 |

正文插图可使用以下语法，构建时会自动添加截图、说明、逐页档案与 PDF 链接：

~~~text
{{ slide lec03-04 64 | 折扣回报的原课件例题 }}
~~~

重新生成课件档案：

~~~sh
python scripts/prepare_materials.py --public
~~~

不带参数时读取根目录的本地原始 PDF，生成经检查的公开副本。原始文件被 Git 忽略；Lecture 1 教学团队页的会议访问凭据会被移除，原文件不作修改。实际内容与页码映射见 PLAN.md。

## 发布

GitHub Pages 使用 GitHub Actions 构建。推送 main 后，工作流严格构建、检查链接与覆盖，然后部署 site 目录。Pages 设置的构建来源应为 GitHub Actions。

## 来源与范围

课件、原图及其引用素材归原作者所有，保留原页署名；本站不为这些材料重新授予许可。新增讲解与原页差异在 [资料来源与说明](docs/reference/sources.md) 中记录。现有课件中的视频以 PDF 提供的静态页面保留。

课程大纲提到的 TD、Policy Gradient、Actor-Critic 等后续内容尚未提供，本站不将其列为已经覆盖。
