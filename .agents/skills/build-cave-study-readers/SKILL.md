---
name: build-cave-study-readers
description: Create or update compact bilingual EN/FR offline HTML study readers with CAVE mode, minimal spacing, rich formatting, searchable topic sections, inline memory traps, and zoom reflow. Use for aviation glossaries, VFR/IFR phraseology, MANAB/CFS sheets, or similar study documents in this established format; preserve existing content and file identity during edits.
---

# Cave Study Readers

Follow the repository `AGENTS.md`, including CAVE mode, Pebble sections, and MANAB/CFS wording rules.

## Choose the editing path

- **Existing reader:** treat its Markdown file as the editorial source. Update the paired Markdown and HTML manually and keep them synchronized. Do not introduce a JSON build dependency unless the user explicitly asks to migrate that reader.
- **New or already generator-backed reader:** use the JSON schema in [references/data-and-validation.md](references/data-and-validation.md) and render with `scripts/build_reader.py DATA.json --html OUTPUT.html --markdown OUTPUT.md`.
- Use compact `Pebble` recall sections for numbered CAVE cards. For bilingual readers, use short searchable memory traps where that established structure fits better.

## Workflow

1. Recover the current artifact and source. Preserve its identity, content, filenames, and working zoom behavior. Confirm scope only when necessary; do not impose a hard entry limit.
2. Verify content against primary sources. For Canadian aviation use the supplied editions and current official English/French NAV CANADA guides, TC AIM, MANAB, CFS, CARs, and Canada Gazette as appropriate. Separate legal requirements, recommendations, and adapted training examples. Do not create Canadian French phraseology by literal translation when official wording exists. Record source links, editions, and verification date in the artifact.
3. Edit using the selected path. Keep one label, English text, and French text per principal row. Split long memory blocks into brief, useful reminders. Put memory content in topic navigation and search results. Keep source attribution in the footer.
4. Preserve the established reader layout. Keep dependencies embedded and offline; escape dataset content. Retain bilingual text, tight spacing, colored labels, alternating rows, search, topics, font controls, theme, and print support. Keep a single document header.
5. Verify coverage, bilingual meaning, and safety-sensitive examples. Check search, topics including memory, counts, empty results, font controls, unavailable `localStorage`, theme, print restoration, and zoom behavior. When a browser is available, inspect narrow and wide widths. Distinguish real browser tests from simulated checks; do not claim Adobe Liquid compatibility without testing.
6. Return clickable links to both Markdown and HTML when both are maintained, with a concise description of changes and validation limitations.

## Layout invariants

- Use visible viewport width during mobile pinch zoom, updated by `visualViewport` resize/scroll and window resize through `requestAnimationFrame`. Bound the left offset and restore width/offset when zooming out. Retain a fallback without that API.
- Use container queries tied to reader width; viewport media queries alone miss pinch zoom. Keep `minmax(0,1fr)`, `min-width:0`, and word wrapping. Do not force reminders onto one physical line with `white-space:nowrap`.
- Use approximately `.12–.14rem` vertical row padding and line-height `1.24–1.25`. Avoid large card margins. Stack EN/FR progressively as width shrinks. Disable sticky toolbar positioning during pinch zoom.
- Keep search case- and diacritic-insensitive, display content and memory counts separately, and include all content for printing before restoring filters.
- Treat domain facts as reader content, not permanent skill rules. Reverify amendments on each new task rather than caching a dated legal conclusion in this skill.
