"""Render only figures referenced by the notes; remove unused image copies."""
import hashlib

import pymupdf
from PIL import Image

from hooks import ROOT, SOURCES, SLIDE


def main():
    required = {source: set() for source in SOURCES}
    for path in (ROOT / 'docs').rglob('*.md'):
        for source_id, number, _ in SLIDE.findall(path.read_text()):
            number = int(number)
            source = SOURCES[source_id]
            assert 1 <= number <= source.get('review_end', source['pages']), path
            required[source_id].add(number)

    retained = set()
    for source_id, source in SOURCES.items():
        pdf_path = ROOT / 'docs/assets/pdf' / source['file']
        assert hashlib.sha256(pdf_path.read_bytes()).hexdigest() == source['sha256'], pdf_path
        with pymupdf.open(pdf_path) as pdf:
            assert len(pdf) == source['pages'], pdf_path
            for number in sorted(required[source_id]):
                path = ROOT / f'docs/assets/figures/{source_id}-p{number:03}.webp'
                path.parent.mkdir(parents=True, exist_ok=True)
                page = pdf[number - 1]
                scale = 1600 / page.rect.width
                pix = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), alpha=False)
                image = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
                image.save(path, 'WEBP', quality=88, method=6)
                retained.add(path)
        print(f'{source_id}: {len(required[source_id])} figures', flush=True)

    removed = 0
    for path in (ROOT / 'docs/assets/figures').glob('*.webp'):
        if path not in retained:
            path.unlink()
            removed += 1
    print(f'Kept {len(retained)} figures; removed {removed} unused images.')


if __name__ == '__main__':
    main()
