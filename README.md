# ELEC6910J · 期中复习笔记

[在线阅读](https://zjucqr.github.io/ELEC6910J/)

维护范围为 **Lecture 1–12 与 Lecture 13 Exam Review**：课程首页集中考试安排、复习重点、公式和术语；12 章保留例题与 53 项检查题答案。Lecture 13–14 原 PDF 完整归档，其中 Lecture 14 不另行扩展为笔记。

## 使用

~~~sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m mkdocs serve
~~~

## 目录

| 路径 | 用途 |
| --- | --- |
| docs/index.md | 考试安排、原图、复习重点、公式与术语 |
| docs/chapters/ | 12 章笔记与答案 |
| docs/slides/index.md | 统一课件下载及资料说明 |
| docs/assets/pdf/ | 7 份 PDF，每份只保存一次 |
| docs/assets/slides/ | 仅保留正文实际引用的截图 |
| course.json | 课件页数、章节范围与 SHA-256 |
| scripts/ | 引用渲染、截图生成、静态检查和浏览器检查 |

依赖统一放在 requirements.txt。PDF 是课件原页的完整存档，不再维护逐页截图副本、提取文本、独立公式表或术语表。

## 检查与发布

~~~sh
python -m mkdocs build --strict
python scripts/check_site.py
~~~

浏览器检查：

~~~sh
python -m playwright install chromium
python -m http.server 8765 --bind 127.0.0.1 --directory site
~~~

在另一个已激活虚拟环境的终端运行 python scripts/check_browser.py。推送 main 后，GitHub Actions 构建、检查并发布。

## 编辑

正文引用课件原图：

~~~text
{{ slide lec13-14 3 | Core Checklist for the Exam }}
~~~

更新引用后运行 python scripts/prepare_materials.py：只生成被引用的截图，并移除未使用的图片。更换 PDF 时同步 course.json 中的页数和 SHA-256；日常构建直接使用已提交的资源。

site/、.work/、__pycache__/ 都是可删除的构建、检查或缓存产物。旧网页书签的跳转在构建时自动生成，不占用额外源文档。

课件版权和公开版本说明见[原课件](docs/slides/index.md#sources)。
