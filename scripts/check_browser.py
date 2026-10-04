"""Browser acceptance checks. Serve site at /ELEC6910J/ before running."""
from pathlib import Path
import argparse
import json
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--base-url", default="http://127.0.0.1:8765/ELEC6910J/")
args = parser.parse_args()
base = args.base_url.rstrip("/") + "/"
shots = ROOT / ".work/screenshots"
shots.mkdir(parents=True, exist_ok=True)
routes = [""] + [str(p.relative_to(ROOT/"site").parent)+"/" for p in sorted((ROOT/"site/chapters").glob("*/index.html"))]
routes += ["examples/", "reference/formulas/", "reference/glossary/", "reference/sources/", "slides/"]
routes += [f"slides/lecture-{i:02}/" for i in range(1,11)]
report = {"pages": [], "search": {}, "checks": []}

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(viewport={"width":1512,"height":1050},device_scale_factor=1)
    page = context.new_page()
    js_errors = []
    page.on("pageerror", lambda e: js_errors.append(str(e)))
    for route in routes:
        response = page.goto(base+route, wait_until="networkidle")
        assert response.status == 200, route
        assert page.locator(".katex-error").count() == 0, (route,page.locator(".katex-error").all_text_contents())
        assert page.locator(".arithmatex:not([data-rendered])").count() == 0, route
        count = page.locator(".katex").count()
        report["pages"].append({"route":route,"math":count})
        if route == "":
            assert count >= 1, "Home equation is not rendered"
            page.screenshot(path=str(shots/"home-desktop.png"), full_page=True)
        print("DESKTOP",route or "home","math",count,flush=True)
    assert not js_errors, js_errors

    page.goto(base+"chapters/02-probability/",wait_until="networkidle")
    page.locator(".slide-zoom").first.click()
    page.locator("dialog").wait_for(state="visible")
    assert page.locator("dialog img").evaluate("(img) => img.complete && img.naturalWidth > 0")
    page.keyboard.press("Escape")
    assert not page.locator("dialog").is_visible()
    report["checks"].append("image dialog and Escape")

    page.goto(base+"slides/lecture-02/#p064",wait_until="networkidle")
    assert page.locator("#p064").get_attribute("open") is not None
    assert page.locator("#p064 img").evaluate("(img) => img.complete && img.naturalWidth > 0")
    page.locator("#slide-filter").fill("064")
    assert page.locator("details.slide-page:not([hidden])").count() == 1
    assert "1 / 36" in page.locator("#slide-filter-count").inner_text()
    page.locator("#slide-filter").fill("no-such-slide")
    assert page.locator("details.slide-page:not([hidden])").count() == 0
    page.locator("#slide-filter").fill("")
    assert page.locator("details.slide-page:not([hidden])").count() == 36
    report["checks"].append("archive hash, image and filter")

    page.goto(base+"chapters/06-value-iteration/#racing-lab",wait_until="networkidle")
    page.locator("#race-step").click()
    assert page.locator("#race-cool").inner_text() == "2.000"
    page.locator("#race-step").click()
    assert page.locator("#race-cool").inner_text() == "3.500"
    assert page.locator("#race-warm").inner_text() == "2.500"
    page.locator("#race-gamma").fill("0.5")
    assert page.locator("#race-cool").inner_text() == "0.000"
    page.locator("#race-step").click()
    page.locator("#race-step").click()
    assert page.locator("#race-cool").inner_text() == "2.750"
    assert page.locator("#race-warm").inner_text() == "1.750"
    page.locator("[data-racing-lab]").screenshot(path=str(shots/"racing-demo.png"))
    report["checks"].append("racing iterations, discount change, reset")

    # Start Chinese search on a fresh page, and reject stale previous results.
    page.goto(base+"chapters/02-probability/", wait_until="networkidle")
    for term in ["蒙特卡洛", "Bellman", "餐厅"]:
        query = page.locator(".md-search__input")
        previous = page.locator(".md-search-result__list").text_content()
        query.fill(term)
        page.wait_for_function("""({term, previous}) => {
            const list = document.querySelector('.md-search-result__list');
            const first = document.querySelector('.md-search-result__item');
            return list && first && list.textContent !== previous &&
                first.textContent.replace(/\u200b/g, '').includes(term);
        }""", arg={"term":term, "previous":previous})
        result = page.locator(".md-search-result__list").inner_text()
        assert len(result.strip()) > 0, term
        report["search"][term] = {"matches":page.locator(".md-search-result__item").count(),"excerpt":result[:180]}
        print("SEARCH",term,report["search"][term]["matches"],flush=True)
        page.keyboard.press("Escape")
    report["checks"].append("fresh Chinese search and input without keyup")

    page.goto(base+"chapters/09-mc-prediction/",wait_until="networkidle")
    page.locator('label[title="切换到深色模式"]').click()
    assert page.locator("body").get_attribute("data-md-color-scheme") == "slate"
    page.screenshot(path=str(shots/"chapter-dark.png"))
    page.locator('label[title="切换到浅色模式"]').click()
    report["checks"].append("dark and light themes")

    page.set_viewport_size({"width":390,"height":844})
    for route in routes[:15]:
        page.goto(base+route,wait_until="networkidle")
        dimensions = page.evaluate("({width:innerWidth,scroll:document.documentElement.scrollWidth})")
        if dimensions["scroll"] > dimensions["width"]+1:
            bad = page.evaluate("Array.from(document.querySelectorAll('article *')).filter(x=>x.getBoundingClientRect().right > innerWidth+1).map(x=>({tag:x.tagName,cls:x.className,text:x.textContent.slice(0,80)})).slice(0,15)")
            raise AssertionError((route,dimensions,bad))
        if route == "":
            page.screenshot(path=str(shots/"home-mobile.png"),full_page=True)
        print("MOBILE",route or "home","no overflow",flush=True)
    page.goto(base,wait_until="networkidle")
    page.locator('label.md-header__button[for="__drawer"]').click()
    assert page.locator("#__drawer").is_checked()
    page.locator(".md-nav--primary").get_by_role("link",name="2: Probability Basics",exact=True).click()
    page.wait_for_url("**/chapters/02-probability/")
    page.screenshot(path=str(shots/"chapter-mobile.png"))
    report["checks"].append("mobile layout and drawer navigation")
    assert not js_errors, js_errors
    browser.close()

(ROOT/".work/browser-report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2))
print("PASS",len(report["pages"]),"pages;",sum(row["math"] for row in report["pages"]),"math expressions;",report["checks"])
