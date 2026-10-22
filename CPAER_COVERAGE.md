### CPAER syllabus coverage and safe reorganization plan

**Status:** preliminary *file/section inventory*, **not** a completed line-by-line TP 12881 coverage assessment. **No moves, merges, deletions or content rewrites approved by this document.**

**Controlling syllabus:** [Transport Canada TP 12881, 7th edition, August 2026](https://tc.canada.ca/en/aviation/publications/study-reference-guide-written-examinations-commercial-pilot-licence-aeroplane-tp-12881). TC says its topic list is not exhaustive. The CPAER has four mandatory subject areas: Air Law; Navigation; Meteorology; Aeronautics — General Knowledge (Airframes, Engines and Systems; Theory of Flight; Flight Instruments; Flight Operations; Human Factors).

***
#### CPAER taxonomy — target, not yet folders

| CPAER mandatory area | Subarea in TP 12881 | Initial content owners to audit |
|---|---|---|
| Air Law | Air Law and Procedures | Card 04; overlaps cards 01, 03 |
| Navigation | Navigation and Radio Aids | Navigation portions of 01/03; shared calculations 06 |
| Meteorology | Meteorology | Theory 16; product decoding / decision gates 05; calculation index 06 |
| Aeronautics | Airframes, Engines and Systems | Card 08; type-specific example 07 |
| Aeronautics | Theory of Flight | Aerodynamics in 01; calculation index 06 |
| Aeronautics | Flight Instruments | Card 08 instrument failures; **full topic coverage not yet audited** |
| Aeronautics | Flight Operations | Card 02 procedures; card 03 performance/operations; related sections in 01/04/05 |
| Aeronautics | Human Factors | Scattered across 01/03; **full topic coverage not yet audited** |

**Caution:** Topic ownership listed here is a *proposed editorial decision*, not evidence of exhaustive coverage. Verify each official syllabus topic and depth before classifying it Covered / Partial / Missing / Needs verification.

***
#### Existing numbered cards — inventory

| Card | Current canonical file | Initial mapping | Preservation/overlap note |
|---|---|---|---|
| 01 Flight theory & VFR | [Open](cheatsheets/01_flight_theory_vfr_knowledge_av_cave_v0_6.md) | Air Law; Navigation; Meteorology; Aeronautics (Theory of Flight, Operations, Human Factors) | Mixed overview: section-level split candidate; keep existing until audited |
| 02 Flight training & procedures | [Open](cheatsheets/02_flight_training_procedures_av_cave_v0_2.md) | Aeronautics / Flight Operations | Primarily practical training procedures; retain as procedural companion |
| 03 Licensing, performance & operations | [Open](cheatsheets/03_licensing_performance_operations_av_cave_v0_2.md) | Air Law; Navigation; Aeronautics / Flight Operations | Mixed summary; split only after owner mapping |
| 04 Canadian air law | [Open](cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md) | Air Law; Aeronautics / Flight Operations (some overlap) | Candidate authoritative home for legal requirements |
| 05 Weather decoding & go/no-go | [Open](cheatsheets/05_weather_decoding_go_nogo_qrc_av_cave_v0_2_compact.md) | Meteorology; Flight Operations | Weather product interpretation/operational decision companion; avoid recopying theory from 16 |
| 06 Formulas & conversions | [Open](cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md) | Navigation; Meteorology; Aeronautics / Flight Operations | Shared calculation reference; keep single formula index with syllabus tags |
| 07 C150M POH | [Open](cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md) | Aeronautics (aircraft-specific supplement) | Keep aircraft type-specific speeds/limits separate from generic theoretical guidance |
| 08 Systems & failures | [Open](cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md) | Aeronautics / Airframes, Engines and Systems; Flight Instruments; Operations | Owner candidate for aircraft systems; check overlapping POH procedures |
| 09 IFR knowledge | [Open](cheatsheets/09_ifr_knowledge_core_av_cave_v0_2.md) | INRAT; CPAER cross-reference only | Advanced IFR companion, not default CPAER content home |
| 10 INRAT knowledge | [Open](cheatsheets/10_inrat_knowledge_core_av_cave_v0_3.md) | INRAT | Keep exam-specific IFR scope intact |
| 11 CAP plate reading | [Open](cheatsheets/11_cap_plate_reading_qrc_av_cave_v0_2.md) | INRAT | Keep chart-reading companion |
| 12 IFR procedures | [Open](cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md) | INRAT | Keep procedural companion |
| 13 Multi-engine knowledge | [Open](cheatsheets/13_multi_engine_knowledge_core_av_cave_v0_1.md) | Multi-engine; Aeronautics cross-reference | Keep rating/type-specific matters separate; link generic theory |
| 16 Weather knowledge | [Open](cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md) | Meteorology | Candidate authoritative home for meteorological theory |

The three existing bilingual Markdown/HTML reader pairs remain separate *reading formats / indices*, not independent authoritative sources: CPAER formulas, aviation abbreviations, and MANAB/CFS. Preserve paired Markdown↔HTML parity. Existing numbered card filenames and all reader URLs remain unchanged during inventory.

***
#### Deduplication contract

1. **One canonical explanation per concept**, with a topic owner recorded *before* splitting. Other cards can contain a short exam-context reminder plus a relative link; do not copy full tables or paragraphs.
2. **Legal obligations** are owned by Air Law card 04, **meteorological theory** by card 16, **weather decoding** by 05, **generic formulas** by 06, **aircraft-type POH data** by 07, **aircraft systems** by 08, and **INRAT-specific details** by its dedicated collection, subject to topic-by-topic audit.
3. Preserve *different functions* even when facts overlap: formula derivation versus recall, concept versus operational checklist, generic theory versus POH-specific data. Redundancy is not automatically duplication.
4. For shared formulas, the bilingual CPAER reader is a **condensed view** of the primary formula explanation, not a separate competing version. Update Markdown and HTML together when either changes.
5. Do not auto-merge contradictory thresholds or rules. Label conflicts **Needs verification** and compare with current TC/CARs/AIM/POH before selecting canonical wording.
6. Retain material scope qualifiers, exceptions, examples, sources, all L4 Pebbles, and FR translations. No destructive summarization during migration.

***
#### Migration gates — must pass in order

- **Gate 0 — Baseline:** snapshot file tree and hashes at a known commit; list incoming/outgoing links, HTML reader count, PWA assets, and all current headings; retain archived content.
- **Gate 1 — Topic inventory:** expand this matrix to **each TP 12881 topic and each existing subsection**; assign one proposed owner, contributing files, exact source location, topic status, unresolved conflicts. Inventory is not complete.
- **Gate 2 — Dedup review:** identify exact duplicate text versus beneficial cross-references versus conflicting facts; do **not** delete until both versions are compared and all unique information is retained.
- **Gate 3 — Proposed target tree:** agree on folder structure and file naming after topic ownership is known. Produce a path-by-path move/split plan, including treatment of numbered card links and anchors.
- **Gate 4 — Pilot migration:** move **one small, low-risk topic**; preserve original path as redirect/link stub where possible; verify heading/line coverage, Markdown links, glossary and bilingual reader parity; test PWA caching, offline tests and browser rendering.
- **Gate 5 — Gradual migration:** repeat one topic group at a time with diff-based review, rollback point, zero lost unique facts, zero broken inbound links, and tests. Keep old and new content accessible until validated.
- **Gate 6 — Cutover:** update README/navigation and syllabus index; perform complete section-by-section completeness audit before retiring compatibility stubs.

**Stop conditions:** uncertain scope, missing unique examples/sources/qualifiers, unresolved legal conflicts, broken relative links, unexpectedly changed Pebble/HTML counts, failed offline test, or unclear source provenance.

***
#### Next audit output

For each TP 12881 item, record:

`TP section/subtopic | existing file#heading | status (Covered/Partial/Missing/Needs verification) | designated owner | overlap | missing facts / issue | source revision | reviewed date`

Do not call a topic Covered from a heading alone. Verify actual content against the **August 2026** syllabus and authoritative sources.

**Current state:** inventory registered; **no study content has been moved, deleted or replaced**.

***
#### Phase 2 — first content audit (22 October 2026)

[Open the content coverage matrix](CPAER_COVERAGE_MATRIX.md): syllabus topic-group screening across all eight subject/subsubject areas; individual checks for all **52 Flight Instruments** and **40 Human Factors** numbered items. Evidence links point to inspected content at the recorded baseline. Covered / Partial / Missing / Conflicting / Needs verification are distinguished; content presence is not regulatory validation.

Findings: HF physiology and instrument principles are thin despite useful failure/procedure reminders; electric propulsion, detailed EFB hazards, medevac fatigue and weather-chart interpretation need attention. Internal publication-currency and TEMPO wording conflicts, plus an ambiguous unusual-attitude instruction, are recorded for comparison before correction.

**Gate 1 remains open:** Air Law regulation-by-regulation and the remaining subject numbered-item expansion are outstanding. No overall coverage percentage, target folder approval, deduplication or study-content migration is claimed. Existing cards/readers/PWA remain unchanged.
