"""Render selected slide figures and preserve old bookmarks without source copies."""
from pathlib import Path
import html
import json
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
        if not 1 <= number <= source.get('review_end', source['pages']):
            raise ValueError(f'Page outside the maintained scope: {source_id} {number}')
        image = link(f'assets/slides/{source_id}/{number:03}.webp')
        pdf = link(f'assets/pdf/{source["file"]}') + f'#page={number}'
        text = html.escape(caption)
        return (
            '<figure class="slide-figure" markdown="1">\n'
            f'[{"!["+caption+"]("+image+")"}]({image}){{ .slide-zoom aria-label="放大：{text}" }}\n'
            f'<figcaption markdown="span">{text} · [PDF p. {number}]({pdf})'
            '</figcaption>\n</figure>\n'
        )

    return SLIDE.sub(figure, markdown)


def on_post_build(config):
    def redirect(route, target, fallback_hash, hash_expression):
        path = Path(config['site_dir']) / route / 'index.html'
        path.parent.mkdir(parents=True, exist_ok=True)
        fallback = html.escape(target + fallback_hash, quote=True)
        path.write_text(
            '<!doctype html><html lang="zh"><meta charset="utf-8">'
            '<meta name="robots" content="noindex"><title>页面已迁移</title>'
            f'<script>location.replace({json.dumps(target)} + ({hash_expression}));</script>'
            f'<noscript><meta http-equiv="refresh" content="0; url={fallback}"></noscript>'
            f'<a href="{fallback}">前往页面</a></html>'
        )

    for name in ('formulas', 'glossary'):
        redirect(f'reference/{name}', '../../', f'#{name}',
                 f'location.hash || {json.dumps("#" + name)}')
    redirect('reference/sources', '../../slides/', '#sources', '"#sources"')
    for chapter in COURSE['chapters']:
        source = SOURCES[chapter['source']]
        fallback = f'#page={chapter["start"]}'
        expression = (
            r'/^#p\d+$/.test(location.hash) ? "#page=" + Number(location.hash.slice(2)) : '
            + json.dumps(fallback)
        )
        redirect(f'slides/lecture-{chapter["number"]:02}',
                 f'../../assets/pdf/{source["file"]}', fallback, expression)
