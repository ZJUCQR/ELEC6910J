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
total_pages = sum(source["pages"] for source in course["sources"])
assert sum(map(len, covered.values())) == manifest["total_pages"] == total_pages

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

# Exercise the displayed TD/control code against the lecture's transition traces.
def displayed_functions(filename):
    text = (ROOT/"docs/chapters"/filename).read_text()
    blocks = re.findall(r"~~~python\n(.*?)\n~~~", text, re.S)
    assert blocks, filename
    functions = {}
    for block in blocks:
        exec(compile(block, filename, "exec"), functions)
    return functions

td_update = displayed_functions("11-td-prediction.md")["td0_update"]
lake = {}
for state, successor in [((1, 1), (1, 2)), ((1, 2), (1, 3)), ((1, 3), (1, 2))]:
    td_update(lake, state, -0.4, successor, 0.1, 0.5)
assert all(math.isclose(lake[state], expected) for state, expected in
           [((1, 1), -0.04), ((1, 2), -0.04), ((1, 3), -0.042)])
terminal_values = {"s": 0.5, "terminal": 100}
td_update(terminal_values, "s", 0, "terminal", 0.1, 1.0, terminated=True)
assert math.isclose(terminal_values["s"], 0.45)

control = displayed_functions("12-td-control.md")
initial_q = {("s", "a"): 2, ("next", "explore"): 1, ("next", "best"): 5}
sarsa_q, optimal_q = initial_q.copy(), initial_q.copy()
control["sarsa_update"](sarsa_q, "s", "a", 0, "next", "explore", 0.1, 0.9)
control["q_learning_update"](optimal_q, "s", "a", 0, "next", ["explore", "best"], 0.1, 0.9)
assert math.isclose(sarsa_q["s", "a"], 1.89)
assert math.isclose(optimal_q["s", "a"], 2.25)
assert sarsa_q["next", "best"] == optimal_q["next", "best"] == 5

dog_q = {}
control["q_learning_update"](dog_q, (0, 0), "right", 1, (0, 1),
                             ["up", "down", "left", "right"], 0.1, 0.99)
control["q_learning_update"](dog_q, (0, 1), "down", -10, (1, 1), [],
                             0.1, 0.99, terminated=True)
assert dog_q == {((0, 0), "right"): 0.1, ((0, 1), "down"): -1.0}
terminal_q = {("terminal", None): 100}
control["sarsa_update"](terminal_q, "s", "a", -10, "terminal", None,
                        0.1, 0.99, terminated=True)
assert terminal_q["s", "a"] == -1.0

if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: {len(pages)} HTML pages; local links and anchors; {total_pages} archived slides; probability, discounting, GridWorld and displayed learning examples.")
