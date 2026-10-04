(() => {
  "use strict";
  function renderMath() {
    if (!window.katex) return;
    document.querySelectorAll(".arithmatex").forEach((node) => {
      if (node.dataset.rendered) return;
      let source = node.textContent.trim();
      if (source.startsWith("\\(") || source.startsWith("\\[")) source = source.slice(2, -2);
      katex.render(source, node, {
        displayMode: node.tagName === "DIV",
        throwOnError: false, strict: "ignore", trust: false,
        output: "htmlAndMathml",
      });
      node.dataset.rendered = "true";
    });
  }
  let dialog;
  let lastTrigger;
  function ensureLightbox() {
    if (dialog) return;
    dialog = document.createElement("dialog");
    dialog.className = "image-dialog";
    dialog.setAttribute("aria-label", "课件图片预览");
    dialog.innerHTML = '<button type="button" class="dialog-close" aria-label="关闭图片预览">关闭 ×</button><img alt=""><p class="dialog-caption"></p>';
    document.body.appendChild(dialog);
    dialog.querySelector("button").addEventListener("click", () => dialog.close());
    dialog.addEventListener("click", (event) => {
      if (event.target === dialog) {
        const rect = dialog.getBoundingClientRect();
        if (event.clientX < rect.left || event.clientX > rect.right ||
            event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
      }
    });
    dialog.querySelector("img").addEventListener("click", () => dialog.classList.toggle("is-expanded"));
    dialog.addEventListener("close", () => {
      document.documentElement.style.overflow = "";
      dialog.classList.remove("is-expanded");
      if (lastTrigger?.isConnected) lastTrigger.focus();
    });
    document.addEventListener("click", (event) => {
      const trigger = event.target.closest("a.slide-zoom");
      if (!trigger || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      lastTrigger = trigger;
      const sourceImage = trigger.querySelector("img");
      const preview = dialog.querySelector("img");
      preview.src = trigger.href;
      preview.alt = sourceImage?.alt || "课件原页";
      dialog.querySelector(".dialog-caption").textContent = preview.alt + " · 点击图片查看原始大小 · Esc 关闭";
      dialog.showModal();
      document.documentElement.style.overflow = "hidden";
    });
  }
  function revealAnchor() {
    if (!location.hash) return;
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const target = document.getElementById(id);
    if (!target) return;
    const details = target.matches("details") ? target : target.closest("details");
    if (!details) return;
    details.hidden = false;
    details.open = true;
    requestAnimationFrame(() => details.scrollIntoView({ block: "start" }));
  }
  function setupArchive() {
    const input = document.getElementById("slide-filter");
    if (!input || input.dataset.bound) return;
    input.dataset.bound = "true";
    const slides = Array.from(document.querySelectorAll(".slide-page"));
    const output = document.getElementById("slide-filter-count");
    const update = () => {
      const query = input.value.trim().toLocaleLowerCase();
      let count = 0;
      for (const slide of slides) {
        const match = slide.querySelector("summary").textContent.toLocaleLowerCase().includes(query);
        slide.hidden = !match;
        count += Number(match);
      }
      output.textContent = "显示 " + count + " / " + slides.length + " 页";
    };
    input.addEventListener("input", update);
    update();
  }
  function setupRacing() {
    const lab = document.querySelector("[data-racing-lab]");
    if (!lab || lab.dataset.bound) return;
    lab.dataset.bound = "true";
    const gammaInput = document.getElementById("race-gamma");
    let cool = 0, warm = 0, iteration = 0;
    const el = (id) => document.getElementById(id);
    function reset() {
      cool = warm = iteration = 0;
      el("race-cool").textContent = el("race-warm").textContent = "0.000";
      el("policy-cool").textContent = el("policy-warm").textContent = "尚未更新";
      el("race-iteration").textContent = "第 0 轮";
      el("race-gamma-value").textContent = Number(gammaInput.value).toFixed(2);
      el("race-detail").textContent = "点击“迭代一步”，查看各动作如何得到新的价值。";
      el("race-caveat").textContent = Number(gammaInput.value) === 1
        ? "γ = 1：这里展示有限步价值，不能据此保证无限时域收敛。"
        : "γ < 1：这个有限 MDP 的价值迭代收敛到唯一最优价值。";
    }
    el("race-step").addEventListener("click", () => {
      const gamma = Number(gammaInput.value);
      const coolSlow = 1 + gamma * cool;
      const coolFast = 2 + gamma * (cool + warm) / 2;
      const warmSlow = 1 + gamma * (cool + warm) / 2;
      const warmFast = -10;
      cool = Math.max(coolSlow, coolFast);
      warm = Math.max(warmSlow, warmFast);
      iteration += 1;
      el("race-cool").textContent = cool.toFixed(3);
      el("race-warm").textContent = warm.toFixed(3);
      el("policy-cool").textContent = "本轮：" + (coolFast >= coolSlow ? "Fast" : "Slow");
      el("policy-warm").textContent = "本轮：" + (warmSlow >= warmFast ? "Slow" : "Fast");
      el("race-iteration").textContent = "第 " + iteration + " 轮";
      el("race-detail").textContent = "使用上一轮数值计算：Cool → Slow " + coolSlow.toFixed(3) + " / Fast " + coolFast.toFixed(3) + "；Warm → Slow " + warmSlow.toFixed(3) + " / Fast " + warmFast.toFixed(3) + "。各取较大值。";
    });
    gammaInput.addEventListener("input", reset);
    el("race-reset").addEventListener("click", reset);
    reset();
  }
  function init() {
    renderMath(); ensureLightbox(); setupArchive(); setupRacing();
    document.querySelectorAll(".slide-figure img").forEach((img) => {
      img.loading = "lazy"; img.decoding = "async";
    });
    revealAnchor();
  }
  window.addEventListener("hashchange", revealAnchor);
  if (typeof document$ !== "undefined") document$.subscribe(init);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
