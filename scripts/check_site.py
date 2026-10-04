"""Check built links, page anchors, slide coverage, and mathematical examples."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
from collections import defaultdict
import json
import math
import re

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
errors = []
pages = {p: BeautifulSoup(p.read_text(), "html.parser") for p in SITE.rglob("*.html")}

for path, soup in pages.items():
    for node in soup.select("a[href], img[src], script[src], link[href]"):
        value = node.get("href", node.get("src", ""))
        parsed = urlsplit(value)
        if parsed.scheme or parsed.netloc or not value:
            continue
        if parsed.path.startswith("/"):
            if not parsed.path.startswith("/ELEC6910J/"):
                errors.append(f"Unexpected absolute path in {path}: {value}")
                continue
            target = SITE / unquote(parsed.path.removeprefix("/ELEC6910J/"))
        else:
            target = path.parent / unquote(parsed.path)
        target = target.resolve()
        if target.is_dir():
            target /= "index.html"
        if not target.exists():
            errors.append(f"Missing target: {path.relative_to(SITE)} → {value}")
        elif parsed.fragment and target.suffix == ".html":
            doc = pages.get(target)
            if doc and not doc.find(id=unquote(parsed.fragment)):
                errors.append(f"Missing anchor: {path.relative_to(SITE)} → {value}")
    article = soup.select_one("article")
    if article:
        if "{{ slide" in article.get_text():
            errors.append(f"Unexpanded reference in {path}")
        for img in article.select("img"):
            if not img.get("alt"):
                errors.append(f"Missing image description in {path}")

course = json.loads((ROOT / "course.json").read_text())
manifest = json.loads((ROOT / "docs/assets/manifest.json").read_text())
covered = defaultdict(set)
for chapter in course["chapters"]:
    archive = SITE / f'slides/lecture-{chapter["number"]:02}/index.html'
    doc = pages[archive]
    ids = {int(s["id"][1:]) for s in doc.select("details.slide-page")}
    expected = set(range(chapter["start"], chapter["end"] + 1))
    assert ids == expected, f"Incomplete archive: {archive}"
    assert not covered[chapter["source"]] & ids, "Duplicate archive coverage"
    covered[chapter["source"]].update(ids)
for source in manifest["sources"]:
    assert covered[source["id"]] == set(range(1, source["pages"] + 1))
    for slide in source["slides"]:
        assert (SITE / slide["image"]).is_file()
assert sum(map(len, covered.values())) == manifest["total_pages"] == 329

# Independent numeric checks against the course examples.
weather = [(0.45, 0.15), (0.02, 0.08), (0.03, 0.27), (0, 0)]
assert math.isclose(sum(sum(row) for row in weather), 1)
assert math.isclose(weather[0][1] / sum(r[1] for r in weather), 0.3)
assert math.isclose(1-weather[2][1], 0.73)
assert math.isclose(10 * (1/math.sqrt(10))**2, 1)

# Check the displayed converged uniform-random GridWorld by Bellman residual.
grid = [[0,-14,-20,-22],[-14,-18,-20,-20],[-20,-20,-18,-14],[-22,-20,-14,0]]
for row in range(4):
    for col in range(4):
        if (row,col) in {(0,0),(3,3)}:
            continue
        expected = 0
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr,nc = row+dr,col+dc
            if not (0 <= nr < 4 and 0 <= nc < 4):
                nr,nc = row,col
            expected += (-1 + grid[nr][nc])/4
        assert math.isclose(grid[row][col], expected)

# Run the actual displayed MC implementation against a repeated-state episode.
markdown = (ROOT/"docs/chapters/09-mc-prediction.md").read_text()
code = re.search(r"~~~python\n(.*?)\n~~~", markdown, re.S).group(1)
namespace = {}
exec(compile(code, "displayed_mc_example", "exec"), namespace)
values, counts = {}, {}
namespace["first_visit_update"](["a","s","s","terminal"], [1,2,4], 1.0, values, counts)
assert values["s"] == 6 and counts["s"] == 1
namespace["first_visit_update"](["s","terminal"], [2], 1.0, values, counts)
assert values["s"] == 4 and counts["s"] == 2

if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: {len(pages)} HTML pages; local links and anchors; 329 archived slides; probability, discounting, GridWorld and displayed MC examples.")
