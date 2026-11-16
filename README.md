# Aero CAVE

Compact Canadian pilot study notes for **PPL (PPAER) · CPL (CPAER) · instrument rating (INRAT) · multi-engine**, in English and French. Personal study aids, not flight authority.

**[Open Aero CAVE](https://jraph.github.io/aero-cave/)**: works offline once opened, installable from the browser menu.

## Finding things

| Entry point | What you get |
|---|---|
| Subjects | The ontology's top concepts. A concept page groups its notes by type, shows the TC items filed under it with their coverage and gaps, and links broader, narrower and related concepts |
| Training path | The TC guides in training order: PSTAR → PPAER → PPL flight test → CPAER → CPL flight test → ME flight test → INRAT → IFR flight test. Each shows item-by-item coverage (Covered / Partial / Missing), the guide's essential (✈) and commercial-depth marks, and the notes its items cite |
| Phase of flight | Weather brief, planning, departure, enroute, approach, emergencies, quick reference, Pebbles |
| Note types | Knowledge, procedures and QRCs, formulas, exam traps, Pebbles, abbreviations and codes, aircraft data, sources: each is a filter across all subjects |
| Search | Full text plus synonyms and abbreviations; **✕ Clear** or Esc resets |
| Badges | ✈ = cited by an item TC marks essential; PPL / CPL / IR / ME = levels of the guides that cite the note (dashed = set by hand, no guide cites it yet) |

EN, FR or both: bilingual tables show the chosen language column.

## How it fits together

- **Concept** (`explorer/ontology.json`): a subject, with EN/FR labels, broader concepts (several allowed), search synonyms. Related links are derived from shared notes and TC items.
- **Note**: one `####` section with a permanent ID. It belongs to concepts and has a kind (knowledge, procedure, formula, trap, Pebble, glossary, aircraft, source).
- **Knowledge** lives in [`kb/`](kb/README.md), one file per concept, ending with a Pebble. **Procedures, aircraft data, formulas and the glossary** live in [`cheatsheets/`](cheatsheets/).
- **TC guides** (`explorer/syllabus.json`): every guide group names its concept; every item has a status and cites note IDs. Levels and ✈ on notes come from these citations.

## Repository layout

| Path | Content |
|---|---|
| [`kb/`](kb/README.md) | Knowledge by domain: air law, navigation, meteorology, aeronautics, IFR, multi-engine |
| [`cheatsheets/`](cheatsheets/) | Flight procedures (02), weather go/no-go (05), C150M POH (07), PA-30 aircraft data, systems failures (08), IFR procedures (12), formulas and calculations, abbreviations |
| `explorer/ontology.json` | Concepts, note kinds, levels, phase-of-flight views |
| `explorer/syllabus.json` | TC guides: items, status, gap notes, cited note IDs, TC marks |
| `explorer/template.html`, `build_explorer.py` | Generate `index.html`, the offline explorer with every note embedded |
| [`readers/`](readers/) | Abbreviations reader; older reader URLs redirect to the explorer |
| [`CONTENT_REVIEW.md`](CONTENT_REVIEW.md) | Open verification items and the review log: sources, editions, what was and was not verified |

## Editing

Markdown is the source of truth. Rules are in [AGENTS.md](AGENTS.md); the note format is in [`kb/README.md`](kb/README.md).

```sh
python3 explorer/build_explorer.py          # regenerate index.html (no dependencies)
python3 explorer/build_explorer.py --audit  # concepts without kb files or knowledge notes, uncited notes
node --test tests/*.cjs                      # ontology, IDs, staleness, rendering, offline cache
```

Then bump `VERSION` in `service-worker.js` and record source or review changes in `CONTENT_REVIEW.md`.

## Sources

Use current official publications and the aircraft POH/AFM for any operational decision. A commit date does not establish regulatory currency.

- [TC study & reference guides](https://tc.canada.ca/en/aviation/licensing-pilots-personnel/flight-crew-licences-permits-ratings/study-reference-guides-sample-examinations)
- [TC flight test guides](https://tc.canada.ca/en/aviation/licensing-pilots-personnel/getting-trained-pilot-crew-member/flight-test-guides)
- [Transport Canada Aeronautical Information Manual](https://tc.canada.ca/en/aviation/publications/transport-canada-aeronautical-information-manual-tc-aim)
- [Canadian Aviation Regulations](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/)
- [NAV CANADA operational guides](https://www.navcanada.ca/en/aeronautical-information/operational-guides.aspx)
