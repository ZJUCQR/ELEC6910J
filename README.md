# ELEC6910J · 深度强化学习笔记

[在线阅读](https://zjucqr.github.io/ELEC6910J/)

根据 HKUST Ling PAN 老师的课件整理，包含 12 章笔记、53 项检查题与答案、期中复习、公式速查及术语对照。保留 425 页课件档案、6 份 PDF 和原课件例题，支持搜索、图片放大、深浅主题与赛车价值迭代演示。

## 本地预览

~~~sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m mkdocs serve
~~~

访问终端显示的地址。PDF、截图和公式资源均在仓库内，常规构建无需重新生成课件。

## 构建与检查

~~~sh
python -m pip install -r requirements-dev.txt
python -m mkdocs build --strict
python scripts/check_site.py
~~~

静态检查覆盖链接、页码、全部课件及正文中的数值和算法示例。浏览器检查还覆盖公式、搜索、图片放大、赛车交互、主题和手机布局：

~~~sh
python -m playwright install chromium
python -m http.server 8765 --bind 127.0.0.1 --directory site
~~~

在另一个已激活虚拟环境的终端运行：

~~~sh
python scripts/check_browser.py
~~~

截图和报告写入 .work/；site/、.work/ 和 Python 缓存均为可删除的生成文件。

## 目录与维护

| 路径 | 用途 |
| --- | --- |
| docs/index.md | 课程首页、期中复习、公式与术语 |
| docs/chapters/ | 12 章正文与检查题答案 |
| docs/slides/ | 逐页课件档案 |
| docs/reference/ | 来源、勘误及旧地址跳转 |
| docs/assets/ | 公开 PDF、截图、样式、脚本与公式资源 |
| course.json | 课件文件、页数与章节划分 |
| scripts/ | 课件生成、引用渲染和验证脚本 |
| overrides/ | 阅读信息与跳转模板 |
| originals/ | 与公开副本不同的本地原始 PDF，不提交 Git |

正文插图语法：

~~~text
{{ slide lec03-04 64 | 折扣回报的例题 }}
~~~

从仓库中的公开 PDF 重新生成截图、档案与资源清单：

~~~sh
python scripts/prepare_materials.py --public
~~~

需要导入原始课件时，将文件放入 originals/，文件名与 course.json 对应，再运行不带 --public 的命令。脚本处理现有的原始文件；没有本地原件时沿用公开副本。Lecture 1 教学事务页中的会议访问凭据会在公开副本中移除，原件不变。

## 发布与来源

推送 main 后，GitHub Actions 完成严格构建和静态检查，再发布到 GitHub Pages。

课件、原图及其引用素材归原作者所有，保留原页署名；整理说明和公式勘误见[资料来源](docs/reference/sources.md)。
