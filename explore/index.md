---
title: 探索
---

<section class="concept-explore-card" data-concept-widget="explore">
  <div class="concept-explore-kicker">概念漫游</div>
  <h2 class="concept-explore-heading">今天从哪里开始？</h2>
  <p class="concept-explore-meta">随机打开一个概念，或者让两个不同领域的概念撞在一起。</p>

  <div class="concept-explore-grid">
    <button type="button" class="concept-explore-button" data-action="random">随机概念</button>
    <button type="button" class="concept-explore-button" data-action="hub">随机枢纽</button>
    <button type="button" class="concept-explore-button" data-action="quiet">随机孤岛</button>
    <button type="button" class="concept-explore-button" data-action="collision">概念对撞</button>
  </div>

  <div class="concept-explore-result" data-role="result">
    <span>点一个按钮开始。</span>
  </div>
</section>

<script type="module">
  const widget = document.querySelector('[data-concept-widget="explore"]')
  if (widget) {
    const indexUrl = new URL("../static/contentIndex.json", window.location.href)
    const result = widget.querySelector('[data-role="result"]')
    const conceptUrl = (slug) => new URL(slug, window.location.origin + "/").pathname
    const domainOf = (slug) => slug.split("/")[2] ?? "unknown"
    const linkCount = (item) => Array.isArray(item.links) ? item.links.length : 0
    const pick = (items) => items[Math.floor(Math.random() * items.length)]
    const renderConcept = (item, label) => {
      result.innerHTML = `<div class="concept-explore-kicker">${label}</div>
        <a class="concept-explore-title" href="${conceptUrl(item.slug)}">${item.title}</a>
        <div class="concept-explore-meta">${domainOf(item.slug)} · ${linkCount(item)} outgoing links</div>`
    }

    fetch(indexUrl)
      .then((response) => response.json())
      .then((index) => {
        const concepts = Object.values(index)
          .filter((item) => item.slug?.startsWith("wiki/concepts/") && !item.slug.endsWith("/index"))
          .sort((a, b) => a.slug.localeCompare(b.slug))
        const hubs = concepts.filter((item) => linkCount(item) >= 50)
        const quiet = concepts.filter((item) => linkCount(item) <= 3)

        widget.querySelector('[data-action="random"]')?.addEventListener("click", () => {
          renderConcept(pick(concepts), "随机概念")
        })

        widget.querySelector('[data-action="hub"]')?.addEventListener("click", () => {
          renderConcept(pick(hubs.length ? hubs : concepts), "随机枢纽")
        })

        widget.querySelector('[data-action="quiet"]')?.addEventListener("click", () => {
          renderConcept(pick(quiet.length ? quiet : concepts), "随机孤岛")
        })

        widget.querySelector('[data-action="collision"]')?.addEventListener("click", () => {
          const first = pick(concepts)
          const differentDomain = concepts.filter((item) => domainOf(item.slug) !== domainOf(first.slug))
          const second = pick(differentDomain.length ? differentDomain : concepts)
          result.innerHTML = `<div class="concept-explore-kicker">概念对撞</div>
            <div class="concept-collision">
              <a href="${conceptUrl(first.slug)}">${first.title}</a>
              <span>×</span>
              <a href="${conceptUrl(second.slug)}">${second.title}</a>
            </div>
            <div class="concept-explore-meta">${domainOf(first.slug)} · ${domainOf(second.slug)}</div>`
        })
      })
  }
</script>

## 也可以直接看索引

- [概念索引](../bases/concepts.md)
- [理论索引](../bases/theories.md)
- [方法索引](../bases/methods.md)
- [人物索引](../bases/persons.md)
- [事实索引](../bases/facts.md)
- [论证索引](../bases/arguments.md)
