# Aero CAVE

Compact Canadian pilot study notes for **PPL (PPAER) · CPL (CPAER) · instrument rating (INRAT) · multi-engine**, in English and French. Personal study aids, not flight authority.

**[Open Aero CAVE](https://jraph.github.io/aero-cave/)**: works offline once opened, installable from the browser menu.

## Finding things

| Entry point | What you get |
|---|---|
| Subjects | Top concepts of the ontology; the topic graph links broader / narrower / related, and a note can sit under several parents |
| Training path | TC guides in training order: PSTAR → PPAER → PPL flight test → CPAER → CPL flight test → ME flight test → INRAT → IFR flight test. Each opens its item-by-item coverage and the sections its items cite |
| Phase of flight | Weather brief, planning, departure, enroute, approach, emergencies, quick reference, Pebbles |
| Badges | ✈ = cited by an item TC marks essential; PPL / CPL / IR / ME = levels of the guides that cite the note (dashed = set by hand, no guide cites it yet) |
| Search | Full text plus synonyms and abbreviations; **✕ Clear** or Esc resets |
| Legacy reader links | Collections transitioning to the explorer: pilot qualifications, CPAER formulas, abbreviations |

## Repository layout

| Path | Content |
|---|---|
| [`kb/`](kb/README.md) | Knowledge: one file per concept, each ending with a Pebble |
| [`cheatsheets/`](cheatsheets/) | Procedures, QRCs, the C150M POH card, and the three reader-paired notes |
| [`readers/`](readers/) | Legacy bilingual HTML pages pending replacement by the explorer |
| `explorer/ontology.json` | Concepts, levels, phase-of-flight views |
| `explorer/syllabus.json` | TC guide items mapped to unit IDs, with status and gap notes |
| `explorer/template.html`, `build_explorer.py` | Generate `index.html` (all notes embedded) |
| [`CONTENT_REVIEW.md`](CONTENT_REVIEW.md) | Review log: sources, editions, what was and was not verified |
| [`CPAER_COVERAGE.md`](CPAER_COVERAGE.md) · [matrix](CPAER_COVERAGE_MATRIX.md) | CPAER coverage audit |

## Editing

Markdown is the source of truth. Style rules are in [AGENTS.md](AGENTS.md); the file format is in [`kb/README.md`](kb/README.md).

```sh
python3 explorer/build_explorer.py   # regenerate index.html (no dependencies)
node --test tests/*.cjs               # ontology, IDs, staleness, offline cache, layout
```

Then bump `VERSION` in `service-worker.js`. Record source or review changes in `CONTENT_REVIEW.md`. Publish new knowledge in `kb/` and regenerate the explorer. The explorer is replacing the three standalone bilingual readers. Retire each legacy pair after its bilingual content, memory traps, search, deep links and offline access are verified in the explorer. During migration, apply corrections to both published formats.

## Sources

Use current official publications and the aircraft POH/AFM for any operational decision. A commit date does not establish regulatory currency.

- [TC flight test guides](https://tc.canada.ca/en/aviation/licensing-pilots-personnel/getting-trained-pilot-crew-member/flight-test-guides)
- [TC study & reference guides](https://tc.canada.ca/en/aviation/licensing-pilots-personnel/flight-crew-licences-permits-ratings/study-reference-guides-sample-examinations)
- [Transport Canada Aeronautical Information Manual](https://tc.canada.ca/en/aviation/publications/transport-canada-aeronautical-information-manual-tc-aim)
- [Canadian Aviation Regulations](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/)
- [NAV CANADA operational guides](https://www.navcanada.ca/en/aeronautical-information/operational-guides.aspx)
