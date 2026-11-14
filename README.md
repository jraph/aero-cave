# Aero CAVE

Compact Canadian aviation study notes for **PPL (PPAER) · CPL (CPAER) · instrument rating (INRAT) · multi-engine**, in English and French. Personal study aids, not flight authority.

## Start here

**[Knowledge explorer](https://jraph.github.io/aero-cave/explorer.html)** (prototype, works offline once opened). Every note reachable from several directions:

| Entry point | What you get |
|---|---|
| **Training stage** | Pre-solo (PSTAR) → PPAER / PPL flight test → night & OTT → CPAER / CPL flight test → ME → INRAT → IFR flight test → first commercial seat; each stage names the TC guide it aims at |
| **Phase of flight** | Weather brief, planning, departure, enroute, approach, emergencies, quick reference, Pebbles |
| **Licence level** | PPL / CPL / IR / ME tags |
| **Topic graph** | 92 concepts with broader / narrower / related links; one note can sit under several parents |
| **TC guide coverage** | Item-by-item status against a TC study guide (so far: TP 12881 Meteorology for the CPAER, TP 691 for the INRAT) |
| **Search** | Full text, accent-insensitive; **✕ Clear** (or Esc) resets every filter |

Stage views and topic links are an editorial study structure, not a Transport Canada mapping.

## Bilingual readers

| Collection | Markdown | HTML reader |
|---|---|---|
| Pilot licensing · PIC/SIC · PPC/CC · type · recency | [Card 17](cheatsheets/17_pilot_qualifications_operator_checks_cave_en_fr.md) | [Reader](https://jraph.github.io/aero-cave/readers/17_Pilot_Qualifications_Operator_Checks_EN_FR.html) |
| CPAER formulas & quick recall | [Notes](cheatsheets/CPAER_Formulas_Recall_EN_FR.md) | [Reader](https://jraph.github.io/aero-cave/readers/CPAER_Formulas_Recall_EN_FR.html) |
| Abbreviations · MANAB / CFS / TC exams | [Notes](cheatsheets/Aviation_Abbreviations_MANAB_CFS_TC_EN_FR.md) | [Reader](https://jraph.github.io/aero-cave/readers/Aviation_Abbreviations_MANAB_CFS_TC_EN_FR.html) |

Readers offer EN / FR / both, search, topic filters, themes, text size and printing.

## Content

The collection is moving from numbered cards to **concept files**: one Markdown file per ontology concept, with per-concept Pebbles and a separate exam-traps file. The Meteorology migration is complete; other subjects are still numbered cards.

| Subject | Where |
|---|---|
| Meteorology | [`kb/met/`](kb/met/README.md): 14 concept files (atmosphere, stability, fog, fronts & wind, icing, carb ice, de-icing, thunderstorms, turbulence, products, METAR, TAF, GFA/SIGMET/PIREP/FB, exam traps) |
| Weather decisions | [05 · Go/no-go flows & gates](cheatsheets/05_weather_decoding_go_nogo_qrc_av_cave_v0_2_compact.md) |
| Flight theory & training | [01 · Flight theory & VFR](cheatsheets/01_flight_theory_vfr_knowledge_av_cave_v0_6.md) · [02 · Training procedures](cheatsheets/02_flight_training_procedures_av_cave_v0_2.md) |
| Licensing & air law | [03 · Licensing, performance & ops](cheatsheets/03_licensing_performance_operations_av_cave_v0_2.md) · [04 · Canadian air law](cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md) · [17 · Pilot qualifications](cheatsheets/17_pilot_qualifications_operator_checks_cave_en_fr.md) |
| Calculations | [06 · Formulas & conversions](cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md) |
| Aircraft | [07 · C150M POH](cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md) · [08 · Systems & failures](cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md) · [13 · Multi-engine](cheatsheets/13_multi_engine_knowledge_core_av_cave_v0_1.md) |
| IFR & INRAT | [`kb/ifr/`](kb/ifr/README.md): 16 concept files (rules & recency, planning & fuel, alternates, departure, enroute, holding, approaches, minima, missed & circling, CAP plates, RASS, lost comms, emergencies, navaid checks, IFR weather, recall) · procedures: [11 · CAP plates](cheatsheets/11_cap_plate_reading_qrc_av_cave_v0_2.md) · [12 · IFR procedures](cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md) |

**What goes where:** knowledge → concept file · ordered procedures, flows and QRCs → numbered card · aircraft-type data → its POH card.

## Status

- **Coverage:** [CPAER_COVERAGE.md](CPAER_COVERAGE.md) (plan and gates) and [CPAER_COVERAGE_MATRIX.md](CPAER_COVERAGE_MATRIX.md) (group-level audit, 22 Oct 2026). Item-level map: [`explorer/syllabus.json`](explorer/syllabus.json), TP 12881 Meteorology (CPAER) = 51 covered / 33 partial / 26 missing / 1 unchecked; TP 691 (INRAT, all 208 items) = 62 covered / 83 partial / 42 missing / 21 unchecked.
- **Review log:** [CONTENT_REVIEW.md](CONTENT_REVIEW.md) records sources, editions, what was checked and what was not. A commit date does not establish regulatory currency.
- **Open conflicts:** see the coverage matrix for X-01 and X-03. V-02 (TAF TEMPO) is closed.

## Authoritative references

- [TC study & reference guides](https://tc.canada.ca/en/aviation/licensing-pilots-personnel/flight-crew-licences-permits-ratings/study-reference-guides-sample-examinations) (TP 12880 PPL, TP 12881 CPL, TP 691 IR) and flight test guides (TP 13723 PPL, TP 13462 CPL, TP 219 ME, TP 9939 IR)
- [Transport Canada Aeronautical Information Manual](https://tc.canada.ca/en/aviation/publications/transport-canada-aeronautical-information-manual-tc-aim)
- [Canadian Aviation Regulations](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/)
- [NAV CANADA operational guides](https://www.navcanada.ca/en/aeronautical-information/operational-guides.aspx)
- [NRC sunrise/sunset interpretation](https://nrc.canada.ca/en/research-development/products-services/software-applications/interpreting-results-sunrisesunset-calculator)

Use current official publications and the aircraft POH/AFM for any operational decision.

## Editing

Markdown is the source of truth. Conventions are in [AGENTS.md](AGENTS.md) (CAVE style, Pebbles, MANAB/CFS codes); the concept-file format is in [`kb/met/README.md`](kb/met/README.md).

- **Unit IDs:** each section in a concept file or ID'd card carries `<!-- id: wx-fog | … -->` on the line under its heading. IDs are permanent: never rename or reuse one, because the syllabus map and explorer links depend on them.
- **Paired readers:** when a topic also appears in an HTML reader, update both in the same change.
- **After any content, ontology or syllabus edit:**
  ```sh
  python3 explorer/build_explorer.py   # regenerates explorer.html (no dependencies)
  node --test tests/*.cjs               # ontology, IDs, staleness, offline cache, layout
  ```
  then bump `VERSION` in `service-worker.js`. The build fails on unknown or duplicate IDs, unknown concepts, or a partial syllabus item without a gap note.
- Record material source or review changes in [CONTENT_REVIEW.md](CONTENT_REVIEW.md). Older material is in [archive](archive/).

| File | Role |
|---|---|
| `explorer/ontology.json` | Concepts, stage / phase views, card → concept mapping |
| `explorer/syllabus.json` | TC guide items → unit IDs, with status and gap notes |
| `explorer/template.html` | Explorer page; `build_explorer.py` embeds all content into `explorer.html` |

## Offline app

[Aero CAVE](https://jraph.github.io/aero-cave/) is a Progressive Web App: install it from the browser menu where supported. The service worker caches the home page, the explorer (one file holding every note, about 0.5 MB), the three readers and app assets. File count in the repo does not affect offline size.

Open the app online once, then **check it works offline before relying on it**: browsers may evict site data, and clearing browser storage removes it. GitHub links and external sources need a connection. Offline access does not make the content current.

Maintenance: bump `service-worker.js` `VERSION` whenever a cached file changes; add any new reader to `FILES`, the manifest shortcuts and `index.html`. A failed update keeps the installed version. Install and offline behaviour still need testing on real devices.
