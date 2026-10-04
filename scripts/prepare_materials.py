"""Create the public PDFs, all slide images, and page-by-page archives.

Run once with local originals: python scripts/prepare_materials.py
Rebuild from checked-in public PDFs: python scripts/prepare_materials.py --public
"""
from pathlib import Path
import argparse
import hashlib
import html
import io
import json
import re

import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
COURSE = json.loads((ROOT / 'course.json').read_text())


def public_pdf(source):
    original = ROOT / source['file']
    target = DOCS / 'assets/pdf' / source['file']
    target.parent.mkdir(parents=True, exist_ok=True)
    if source['id'] != 'lec01-02':
        target.write_bytes(original.read_bytes())
        return
    doc = fitz.open(original)
    page = doc[1]
    # Redact complete lines containing meeting access details, including links.
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines', []):
            text = ''.join(span['text'] for span in line['spans'])
            if any(marker in text.lower() for marker in ('zoom.us', 'password:')) or re.search(r'\bID\s+\d', text):
                rect = fitz.Rect(line['bbox']) + (-2, -1, 2, 1)
                page.add_redact_annot(rect, text='[meeting access omitted]', fontsize=7, fill=(1, 1, 1))
    page.apply_redactions()
    for link in page.get_links():
        if 'zoom' in link.get('uri', '').lower():
            page.delete_link(link)
    doc.save(target, garbage=4, deflate=True)
    doc.close()
    with fitz.open(target) as check:
        assert not re.search(r'Password\s*:|\bID\s+\d', check[1].get_text(), re.I), 'Public PDF still contains meeting access details'


def title_for(page, number):
    lines = [s.strip() for s in page.get_text(sort=True).splitlines() if s.strip()]
    for text in lines:
        if len(text) > 3 and not text.isdigit():
            return text[:110]
    return f'课件图示 · 第 {number} 页'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--public', action='store_true', help='Use already reviewed public PDFs')
    args = parser.parse_args()
    manifest = {'total_pages': 0, 'sources': [], 'chapters': COURSE['chapters']}
    all_pages = {}
    for source in COURSE['sources']:
        if not args.public:
            public_pdf(source)
        pdf_path = DOCS / 'assets/pdf' / source['file']
        pages = []
        with fitz.open(pdf_path) as pdf:
            assert len(pdf) == source['pages']
            out = DOCS / 'assets/slides' / source['id']
            out.mkdir(parents=True, exist_ok=True)
            for index, page in enumerate(pdf):
                number = index + 1
                path = out / f'{number:03}.webp'
                # 1600px preserves equations and annotations when expanded.
                pix = page.get_pixmap(matrix=fitz.Matrix(1600 / page.rect.width, 1600 / page.rect.width), alpha=False)
                img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
                img.save(path, 'WEBP', quality=88, method=6)
                pages.append({'page': number, 'title': title_for(page, number), 'image': str(path.relative_to(DOCS)), 'width':pix.width, 'height':pix.height})
        all_pages[source['id']] = pages
        manifest['sources'].append({**source, 'sha256': hashlib.sha256(pdf_path.read_bytes()).hexdigest(), 'slides':pages})
        manifest['total_pages'] += len(pages)
        print(f"{source['id']}: {len(pages)} pages rendered", flush=True)

    archive_dir = DOCS / 'slides'
    archive_dir.mkdir(parents=True, exist_ok=True)
    source_map = {s['id']:s for s in COURSE['sources']}
    for ch in COURSE['chapters']:
        source = source_map[ch['source']]
        pages = all_pages[ch['source']][ch['start'] - 1:ch['end']]
        note = '\n!!! note "章节划分"\n\n    本文件第二部分的封面仍写作 Lecture 7。本站按文件 Lec 7–8 与主题顺序，将第 30–57 页归入第 8 章。\n' if ch['number'] == 8 else ''
        lines = [
            '---\nhide:\n  - toc\n---\n',
            f"# L{ch['number']} · {ch['title']}\n",
            f"{ch['zh']} · PDF 第 **{ch['start']}–{ch['end']}** 页 · 共 **{len(pages)}** 页。\n",
            f"[下载本组 PDF](../assets/pdf/{source['file']}){{ .md-button }}\n",
            '点击页标题展开原页，点击图片放大。页码采用 PDF 的物理页序，便于与文件对应。\n',
            note,
            '<div class="archive-tools"><label for="slide-filter">定位课件</label><input id="slide-filter" type="search" placeholder="输入页码或英文标题" autocomplete="off"><span id="slide-filter-count" role="status" aria-live="polite"></span></div>\n',
        ]
        for item in pages:
            n = item['page']
            title = html.escape(item['title'])
            opened = ' open' if n == ch['start'] else ''
            lines.extend([
                f'<details class="slide-page" id="p{n:03}"{opened}>',
                f'<summary><span class="page-number">{n:03}</span> {title}</summary>',
                '<figure class="slide-figure">',
                f'<a href="../../{item["image"]}" class="slide-zoom" aria-label="放大：第 {n} 页 {title}"><img src="../../{item["image"]}" alt="第 {n} 页：{title}" width="{item["width"]}" height="{item["height"]}" loading="lazy" decoding="async"></a>',
                f'<figcaption>PDF p. {n} · <a href="../../assets/pdf/{source["file"]}#page={n}">在 PDF 中查看</a> · <a href="#p{n:03}">本页链接</a></figcaption>',
                '</figure>\n</details>\n',
            ])
        (archive_dir / f"lecture-{ch['number']:02}.md").write_text('\n'.join(lines))
    (DOCS / 'assets/manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    print(f"Complete: {manifest['total_pages']} pages, 10 archives.")


if __name__ == '__main__':
    main()
