# Radio navigation (VOR / ADF / DME / ILS) / Radionavigation (VOR / ADF / DME / ILS)
<!-- concept: nav-radio | level: IR -->

[IFR index / Index IFR](README.md) · concept `nav-radio` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Navigation aid checks
<!-- id: ifr-navigation-aid-checks | from: 10 -->

- VOR: identify Morse/voice, correct frequency/course/TO-FROM, service volume and NOTAM.

##### VOR receiver checks — 4–6–4

| Check | Maximum acceptable error / difference |
|---|---|
| VOT / designated ground checkpoint | **±4°** from the reference indication (FAA AIM reference; see Canadian scope below) |
| Airborne landmark / published-radial check | **±6°** from the published radial |
| Dual independent VOR receivers, same station | **4° total difference** between indicated bearings |

- `M:` **4 ground — 6 airborne — 4 between receivers.**
- `P VOT:` with CDI centred, reference indication is **000° FROM** or **180° TO**; apply ±4°. A designated ground checkpoint uses its published radial instead.
- `T dual:` NAV1 030° / NAV2 034° = at the limit; 030° / 035° = exceeds tolerance. This is **4° between receivers**, not ±4° each. Compare using the same TO/FROM sense.
- `T airborne:` ±6° is a **receiver-check tolerance**, not permission to track 6° off course.
- **Canadian scope:** TC AIM 2026-1 COM 4.5.1–4.5.2 specifies the dual comparison and airborne check: difference greater than 4° requires investigation/correction before IFR use; airborne error greater than 6° means the equipment should not be used for IFR navigation. The ground/VOT ±4° and VOT indications above are explicitly sourced to the FAA AIM; do not infer U.S. checking intervals or recordkeeping requirements for Canada.
- **Sources:** [TC AIM 2026-1, COM 4.5.1–4.5.2](https://tc.canada.ca/en/aviation/publications/transport-canada-aeronautical-information-manual-tc-aim-tp-14371); [FAA AIM 1-1-4, VOR Receiver Check](https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap1_section_1.html). Reviewed 2026-10-19.


- ILS: identify LOC; set front course; GS alive from below; marker/DME/fixes per plate.
- NDB: identify; station passage/needle swing; ADF errors near TS/coast/night/mountain.
- GNSS: current DB, RAIM/WAAS, correct mode, CDI scaling, annunciations.
- `T:` failed identification = unusable navaid for approach.
***
#### Pebble
<!-- id: ifr-navaid-checks-pebble | also: study-pebble -->

- VOR CHECK `4 ground — 6 airborne — 4 between receivers | VOT: 000° FROM or 180° TO, ±4° (FAA AIM source) | airborne ±6° from published radial | dual: 4° TOTAL difference, same TO/FROM sense | Canada (TC AIM COM 4.5.1–4.5.2): dual >4° or airborne >6° → not for IFR until corrected`
- T `±6° = receiver-check tolerance ≠ permission to track off course | failed identification = unusable navaid for approach | do not infer U.S. intervals/recordkeeping for Canada`
***
