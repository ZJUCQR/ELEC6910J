"""Browser acceptance checks. Serve the built site locally before running."""
from pathlib import Path
import argparse
import json
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--base-url", default="http://127.0.0.1:8765/")
args = parser.parse_args()
base = args.base_url.rstrip("/") + "/"
shots = ROOT / ".work/screenshots"
shots.mkdir(parents=True, exist_ok=True)
routes = [""] + [str(p.relative_to(ROOT/"site").parent)+"/" for p in sorted((ROOT/"site/chapters").glob("*/index.html"))]
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
        if route.startswith("chapters/"):
            answers = page.locator("details.success").filter(has=page.get_by_text("参考答案", exact=True))
            answers.locator("summary").click()
            assert answers.get_attribute("open") is not None
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

    page.goto(base, wait_until="networkidle")
    page.locator(".exam-originals > summary").click()
    originals = page.locator(".exam-originals img")
    assert originals.count() == 2
    originals.last.scroll_into_view_if_needed()
    page.wait_for_function("Array.from(document.querySelectorAll('.exam-originals img')).every(img => img.complete && img.naturalWidth > 0)")
    page.locator(".exam-originals .slide-zoom").last.click()
    page.locator("dialog").wait_for(state="visible")
    page.keyboard.press("Escape")
    assert "6555" in page.locator("article").inner_text()
    report["checks"].append("exam information and original slide images")

    for name in ("formulas", "glossary"):
        page.goto(base + f"reference/{name}/")
        page.wait_for_url(base + f"#{name}")
    page.goto(base + "reference/sources/")
    page.wait_for_url(base + "#sources")
    page.goto(base + "slides/#sources")
    page.wait_for_url(base + "#sources")
    page.goto(base + "slides/")
    page.wait_for_url(base + "#slides", wait_until="networkidle")
    downloads = page.locator('#slides a[href$=".pdf"]')
    assert downloads.count() == 7
    downloads.first.wait_for(state="visible")
    report["checks"].append("legacy bookmark redirects")

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
    for term in ["蒙特卡洛", "Bellman", "餐厅", "时序差分", "Q-learning"]:
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
    for route in routes:
        page.goto(base+route,wait_until="networkidle")
        dimensions = page.evaluate("({width:innerWidth,scroll:document.documentElement.scrollWidth})")
        if dimensions["scroll"] > dimensions["width"]+1:
            bad = page.evaluate("Array.from(document.querySelectorAll('article *')).filter(x=>x.getBoundingClientRect().right > innerWidth+1).map(x=>({tag:x.tagName,cls:x.className,text:x.textContent.slice(0,80)})).slice(0,15)")
            raise AssertionError((route,dimensions,bad))
        if route == "":
            page.screenshot(path=str(shots/"home-mobile.png"),full_page=True)
        print("MOBILE",route or "home","no overflow",flush=True)
    page.goto(base,wait_until="networkidle")
    page.locator("#slides > summary").click()
    assert page.locator('#slides a[href$=".pdf"]').first.is_visible()
    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 1")
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
