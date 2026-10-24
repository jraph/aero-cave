# Aero CAVE

Compact study notes for Canadian **CPAER · INRAT · flight training**, in English and French.

## Read now

| Collection | Read on GitHub | CAVE reader |
|---|---|---|
| **Pilot licensing · PIC/SIC · PPC/CC · Type · Recency** | [Open CAVE study card](cheatsheets/17_pilot_qualifications_operator_checks_cave_en_fr.md) | [Open bilingual HTML reader](https://jraph.github.io/aero-cave/readers/17_Pilot_Qualifications_Operator_Checks_EN_FR.html) |
| **CPAER — formulas & quick recall** | [Open study notes](cheatsheets/CPAER_Formulas_Recall_EN_FR.md) | [Open HTML reader](https://jraph.github.io/aero-cave/readers/CPAER_Formulas_Recall_EN_FR.html) |
| **Aviation abbreviations — MANAB / CFS / TC exams** | [Open study notes](cheatsheets/Aviation_Abbreviations_MANAB_CFS_TC_EN_FR.md) | [Open HTML reader](https://jraph.github.io/aero-cave/readers/Aviation_Abbreviations_MANAB_CFS_TC_EN_FR.html) |

HTML readers offer search, topic filters, dark/light themes, adjustable text and printing. Download an HTML file to read offline. Markdown opens directly on GitHub.

## Browse by subject

| Subject | Study cards |
|---|---|
| Flight theory & training | [01 · Flight Theory & VFR Knowledge](cheatsheets/01_flight_theory_vfr_knowledge_av_cave_v0_6.md) · [02 · Flight Training and Procedures](cheatsheets/02_flight_training_procedures_av_cave_v0_2.md) |
| Licensing & operations | [17 · Pilot qualifications & checks](cheatsheets/17_pilot_qualifications_operator_checks_cave_en_fr.md) · [03 · Licensing, Performance & Operations](cheatsheets/03_licensing_performance_operations_av_cave_v0_2.md) · [04 · Canadian air law](cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md) |
| Weather | [05 · Decoding & decisions](cheatsheets/05_weather_decoding_go_nogo_qrc_av_cave_v0_2_compact.md) · [16 · Weather knowledge](cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md) |
| Calculations | [06 · Formulas & conversions](cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md) |
| Aircraft | [07 · C150M POH](cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md) · [08 · Systems & failures](cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md) · [13 · Multi-engine](cheatsheets/13_multi_engine_knowledge_core_av_cave_v0_1.md) |
| IFR & INRAT | [09 · IFR knowledge](cheatsheets/09_ifr_knowledge_core_av_cave_v0_2.md) · [10 · INRAT](cheatsheets/10_inrat_knowledge_core_av_cave_v0_3.md) · [11 · CAP plates](cheatsheets/11_cap_plate_reading_qrc_av_cave_v0_2.md) · [12 · IFR procedures](cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md) |

## Sources & review status

Personal study aids. Use current official publications and the applicable aircraft POH/AFM for operational decisions. [Review notes](CONTENT_REVIEW.md) identify checked topics, source editions and remaining gaps; a commit date does not establish regulatory currency.

## Authoritative references

- [Transport Canada CPAER study guide, TP 12881](https://tc.canada.ca/en/aviation/publications/study-reference-guide-written-examinations-commercial-pilot-licence-aeroplane-tp-12881)
- [Transport Canada Aeronautical Information Manual](https://tc.canada.ca/en/aviation/publications/transport-canada-aeronautical-information-manual-tc-aim)
- [Canadian Aviation Regulations](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/)
- [NAV CANADA operational guides](https://www.navcanada.ca/en/aeronautical-information/operational-guides.aspx)
- [NRC sunrise/sunset interpretation](https://nrc.canada.ca/en/research-development/products-services/software-applications/interpreting-results-sunrisesunset-calculator)

## Editing

Edit the Markdown directly on GitHub. When a topic appears in an HTML reader or another card, update those copies in the same change. Markdown is the editorial source; HTML is the reading edition. No JSON, build step or script is required.

Keep the compact layout, bilingual meaning, units and source dates. Original paths are retained so saved links continue to work. Earlier material is in [archive](archive/).

Record future changes in descriptive commit messages. Keep historical review notes in [CONTENT_REVIEW.md](CONTENT_REVIEW.md), and keep study cards and readers focused on study content and source references.


## Offline app & language

[Aero CAVE](https://jraph.github.io/aero-cave/) uses the cross-platform **Progressive Web App (PWA)** approach: a Web App Manifest specifies installation/standalone presentation, while a service worker caches the homepage, two HTML readers and required app assets for offline access. Installation, when supported, is offered through the browser's native menu or controls; no device-specific install button or `beforeinstallprompt` dependency is required.

**EN / FR / BOTH** in each reader switches definitions and memory reminders immediately; BOTH is the default. The shared choice is saved when local storage is available. Search follows the selected language; labels remain bilingual. Printing includes all rows in the selected language and restores search/topic filters afterward. Downloaded standalone HTML files retain the toggle and embedded layout without a build step.

Open the app online once to allow its assets to cache, and **verify access offline before relying on it**. Browsers/operating systems may evict site data; clearing browser storage removes cached assets. External source publications and GitHub Markdown links require a connection. Offline access does not establish source currency.

Maintenance: update `service-worker.js` VERSION whenever a precached file changes; add new readers to FILES and manifest shortcuts/index. A failed download does not replace the installed version. Cache cleanup is restricted to this app's scope.

Run the dependency-free cache regression checks with `node --test tests/offline.test.cjs`. Actual installation and offline behaviour still require testing on supported browsers/devices.
