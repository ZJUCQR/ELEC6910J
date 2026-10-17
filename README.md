# ELEC6910J · 期中复习笔记

[在线阅读](https://zjucqr.github.io/ELEC6910J/)

维护范围为 **Lecture 1–12 与 Lecture 13 Exam Review**：课程首页集中考试安排、复习重点、公式、术语和课件下载；12 章保留例题与 53 项检查题答案。期中复习课件保留 Lecture 13 的 37 页，包含最后两页 Checklist。

[期中模拟卷与解答](https://zjucqr.github.io/ELEC6910J/mock-exam/)共 100 分：16 道单选（每题 1 分）、8 道填空、8 道计算。每题下方附折叠解答；计算题独立给出完整条件和示意图。

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
| docs/index.md | 考试安排、复习重点、公式、术语与课件下载 |
| docs/mock-exam.md | 期中模拟卷与逐题解答 |
| docs/chapters/ | 12 章笔记与答案 |
| docs/assets/pdf/ | 7 份 PDF，每份只保存一次 |
| docs/assets/figures/ | 课件截图与模拟卷 SVG 示意图；模拟卷图使用 mock- 前缀 |
| docs/assets/theme/ | 页面样式 site.css 与交互脚本 site.js |
| docs/assets/math/ | KaTeX 公式渲染、许可证与 fonts/ 字体 |
| course.json | 课件页数、章节范围与 SHA-256 |
| hooks.py | 必需的构建钩子：渲染课件图片、校验 PDF、生成旧链接跳转 |

依赖统一放在 requirements.txt。PDF 是课件原页的完整存档，不再维护逐页截图副本、提取文本、独立公式表或术语表。

## 检查与发布

~~~sh
python -m mkdocs build --strict
~~~

构建时检查内部链接、锚点和 PDF 校验值。推送 main 后，GitHub Actions 自动构建并发布。

## 编辑

正文引用课件原图：

~~~text
{{ slide lec01-02 16 | 房价回归 }}
~~~

截图按“讲次＋页码”保存在 docs/assets/figures/，只保留正文实际引用的图片。更换 PDF 时同步 course.json 中的页数和 SHA-256。

site/ 与 __pycache__/ 是可删除的构建和缓存产物，不提交到仓库。

课件版权和公开版本说明见[首页资料说明](docs/index.md#sources)。
