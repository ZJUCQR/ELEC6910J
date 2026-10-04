"""Expand verified slide references and add reading metadata at build time."""
from pathlib import Path
import html
import json
import math
import posixpath
import re

ROOT = Path(__file__).resolve().parents[1]
COURSE = json.loads((ROOT / 'course.json').read_text())
SOURCES = {s['id']: s for s in COURSE['sources']}
SLIDE = re.compile(r'^\{\{\s*slide\s+(lec\d{2}-\d{2})\s+(\d+)\s*\|\s*(.*?)\s*\}\}\s*$', re.M)


def on_page_markdown(markdown, page, config, files):
    def link(path):
        return posixpath.relpath(path, posixpath.dirname(page.file.src_uri) or '.')

    def figure(match):
        source_id, number, caption = match.groups()
        number = int(number)
        source = SOURCES[source_id]
        if not 1 <= number <= source['pages']:
            raise ValueError(f'Invalid source page: {source_id} {number}')
        chapter = next(c for c in COURSE['chapters'] if c['source'] == source_id and c['start'] <= number <= c['end'])
        image = link(f'assets/slides/{source_id}/{number:03}.webp')
        archive = link(f'slides/lecture-{chapter["number"]:02}.md') + f'#p{number:03}'
        pdf = link(f'assets/pdf/{source["file"]}') + f'#page={number}'
        text = html.escape(caption)
        return (
            '<figure class="slide-figure" markdown="1">\n'
            f'[{"!["+caption+"]("+image+")"}]({image}){{ .slide-zoom aria-label="放大：{text}" }}\n'
            f'<figcaption markdown="span">{text} · PDF p. {number} · '
            f'[逐页查看]({archive}) · [PDF]({pdf})</figcaption>\n</figure>\n'
        )

    markdown = SLIDE.sub(figure, markdown)
    if not page.file.src_uri.startswith('slides/'):
        chars = len(re.findall(r'[\u4e00-\u9fff]', markdown)) + len(re.findall(r'[A-Za-z]{2,}', markdown))
        page.meta['reading_time'] = max(1, math.ceil(chars/360))
    return markdown
