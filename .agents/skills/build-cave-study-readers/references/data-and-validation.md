# Dataset and validation

## Dataset

```json
{
  "title": "Topic · EN / FR",
  "eyebrow": "Study / Étude",
  "summary": "Compact bilingual reference / Référence bilingue condensée",
  "label": "Code / Situation",
  "key": "unique-reader-key",
  "groups": [{"title": "Section / Section", "rows": [["LABEL", "English text", "Texte français"]]}],
  "memory": [["Short label / Repère", "English reminder / Rappel français"]],
  "sources": [["Official source", "https://example.org/source"]]
}
```

Use a unique key per reader for saved font/theme preferences. Use plain text; the renderer escapes HTML. Include at least one content group and one memory reminder. Add valid source URLs and edition/check dates for real study materials. Distinguish templates from verbatim official examples. Keep placeholders rather than invented operational details. For amendment dates verify the coming-into-force clause and publication date; do not confuse registration or advisory-circular dates with the legal effective date.

## Verification

Run the renderer on a small sample before delivering. Check row counts against the dataset, topic labels, memory navigation, diacritic-insensitive searches, and both language columns. Test long labels and long tokens for wrapping.

Use a real browser when available: 390px, 195px, 780px, maximum font, light/dark themes and print. For pinch zoom test visualViewport width=195, layout width=390, scale=2, offsetLeft=50; test offset bounds and restoration to width390/offset0/scale1. A mocked DOM verifies event logic only, not actual layout or mobile gestures. Report that limitation accurately when browser testing is unavailable.

Confirm that memory reminders are normal searchable/filterable sections, with a separate count and no forced horizontal line. Ensure zero-result visibility uses content plus reminders. Print all rows, then restore the prior filters.
