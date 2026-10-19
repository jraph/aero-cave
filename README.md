# Aero CAVE

Compact aviation memory cards and offline bilingual EN/FR readers for Canadian CPAER, INRAT and flight-training study.

## Start here

| Reader | Contents |
|---|---|
| [CPAER formulas and quick recall](https://jraph.github.io/aero-cave/readers/CPAER_Formulas_Recall_EN_FR.html) | ADF/VOR/DME, bearings and intercepts, formulas, time/distance, climb/descent/turns, hydroplaning, CFS services, communications, NOTAMs, twilight and time zones |
| [MANAB / CFS bilingual reader](https://jraph.github.io/aero-cave/readers/MANAB_CFS_EN_FR_Reader.html) | Aviation abbreviations and terminology with memory reminders |

Use the reader links above to open the rendered HTML after GitHub Pages is enabled. Readers are self-contained and also work offline when downloaded, with search, topic filters, CAVE/light themes, font controls and print support.


## Study cards

- [01_vfr_knowledge_core_av_cave_v0_6.md](cheatsheets/01_vfr_knowledge_core_av_cave_v0_6.md)
- [02_vfr_ftm_proc_av_cave_v0_2.md](cheatsheets/02_vfr_ftm_proc_av_cave_v0_2.md)
- [03_cpl_knowledge_core_av_cave_v0_2.md](cheatsheets/03_cpl_knowledge_core_av_cave_v0_2.md)
- [04_canadian_air_law_core_av_cave_v0_2_compact.md](cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md)
- [05_weather_decoding_go_nogo_qrc_av_cave_v0_2_compact.md](cheatsheets/05_weather_decoding_go_nogo_qrc_av_cave_v0_2_compact.md)
- [06_aviation_formulas_conversions_av_cave_v0_2.md](cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md)
- [07_c150m_poh_core_av_cave_v0_2_compact.md](cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md)
- [08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md](cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md)
- [09_ifr_knowledge_core_av_cave_v0_2.md](cheatsheets/09_ifr_knowledge_core_av_cave_v0_2.md)
- [10_inrat_knowledge_core_av_cave_v0_3.md](cheatsheets/10_inrat_knowledge_core_av_cave_v0_3.md)
- [11_cap_plate_reading_qrc_av_cave_v0_2.md](cheatsheets/11_cap_plate_reading_qrc_av_cave_v0_2.md)
- [12_ifr_procedures_qrc_av_cave_v0_2.md](cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md)
- [13_multi_engine_knowledge_core_av_cave_v0_1.md](cheatsheets/13_multi_engine_knowledge_core_av_cave_v0_1.md)
- [16_weather_knowledge_core_av_cave_v0_1.md](cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md)
- [CPAER_Formulas_Recall_EN_FR.md](cheatsheets/CPAER_Formulas_Recall_EN_FR.md)
- [MANAB_CFS_Essential_EN_FR.md](cheatsheets/MANAB_CFS_Essential_EN_FR.md)

## Organization

- `cheatsheets/`: editable Markdown cards and bilingual reader companion text.
- `readers/`: offline HTML study readers.
- `archive/`: historical source-validation and NAV CANADA cycle notes, retained for context. They do not establish current validity.

The older formula card is archived; its original link points to the active cards. See [content review and remaining overlap](CONTENT_REVIEW.md) for ownership and review scope. Individual cards have different review dates and coverage.

## Essential cautions

These are personal study aids, not approved operational publications or a complete syllabus. Some material is provisional or has not had a full line-by-line audit. Always use current CARs/Standards, NOTAMs, AIP/CFS/CAP, the exact aircraft POH/AFM and instructor guidance as applicable. A repository commit date is not a regulatory validation date.

Approximation symbols, assumptions, units and source dates matter. Examples include dynamic hydroplaning estimates of `9√psi` for rotating tyres and `7.7√psi` for non-rotating tyres; climb/descent ground gradients use groundspeed, while turn geometry uses TAS. Local civil-time rules and aerodrome REF entries take precedence over generic time-zone tables.

Historical documents may reference release notes or source files not included in this initial import. Source PDFs and aircraft manuals are not redistributed here. Original source publishers retain their rights; no licence for third-party material is implied.

## Authoritative references

- [Transport Canada CPAER study guide, TP 12881](https://tc.canada.ca/en/aviation/publications/study-reference-guide-written-examinations-commercial-pilot-licence-aeroplane-tp-12881)
- [Transport Canada Aeronautical Information Manual](https://tc.canada.ca/en/aviation/publications/transport-canada-aeronautical-information-manual-tc-aim)
- [Canadian Aviation Regulations](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/)
- [NAV CANADA operational guides](https://www.navcanada.ca/en/aeronautical-information/operational-guides.aspx)
- [NRC sunrise/sunset interpretation](https://nrc.canada.ca/en/research-development/products-services/software-applications/interpreting-results-sunrisesunset-calculator)

## Updating

For the formula reader, edit `data/formulas.json`, then run:

```sh
python3 scripts/build_all.py
```

This builds the bilingual Markdown and HTML together and refreshes the navigation/ETE blocks in `06`. Do not hand-edit generated outputs or marked blocks. Other sections of `06` and other subject cards remain editable Markdown. The MANAB reader is still maintained separately.

Run `python3 scripts/check_formulas.py` before committing. Record sources and review scope in [CONTENT_REVIEW.md](CONTENT_REVIEW.md). Preserve units, approximation signs, EN/FR meaning and the compact reader controls.

Initial collection imported 19 October 2026.
