# Content review — 19 October 2026

## Completed in this review

- Added 22 bilingual navigation entries: RB/MH/BTS/BFS arithmetic and wraparound, ADF cards/RMI, needle movement, homing/tracking, VOR radials and flags, 30° inbound/outbound intercepts, wind assumptions, lateral displacement, VOR scale, DME slant range and closing time.
- Independently calculated worked examples. Intercept examples state position and course, not merely heading; 30° is a training choice, not a general clearance or universal technique.
- TC TP 975 Exercise 24 (September 2004) checked online: magnetic heading + relative bearing = magnetic bearing to station; capture indication changes with intercept angle. FAA Instrument Flying Handbook Ch. 9 is a supplementary navigation reference, not Canadian regulatory authority.
- Preserved all 149 existing bilingual content rows and 10 reminders; added navigation, explicit ETE units, 75 kt and one reminder. New total: 173 rows and 11 reminders.
- Recovered the previously separately appended twilight section into the common build. The reader title now reports the targeted review scope, rather than implying every entry was revalidated.
- Shared JSON produces bilingual MD/HTML and the navigation/ETE blocks in 06. Editing one of these facts now updates all three outputs.
- Removed repeated top-of-descent and mental-math sections within 06; underlying formulas remain in descent, ETE and fuel sections.
- Moved the older CPAER_CAVE_Formulas content to archive, leaving a link at its original path.
- Replaced 06's missing source/review-file references with the actual review record.

## Ownership and remaining overlap

| Content | Maintained source | Views |
|---|---|---|
| Bilingual formulas, quick recall, navigation, ETE | data/formulas.json | CPAER_Formulas_Recall_EN_FR.md + HTML; navigation/ETE also generated in 06 |
| Additional calculations and IFR reminders in 06 | Non-generated sections of 06 MD | 06 MD |
| MANAB terminology | MANAB_CFS_Essential_EN_FR.md and existing reader | Still a manually maintained pair |
| Subject-specific cards 01–16 | Their existing Markdown files | Subject-specific review sheets |
| Older formulas | archive/CPAER_CAVE_Formulas.md | Historical only |

The 06 card and bilingual dataset still overlap outside navigation/ETE. Consolidating them completely requires reconciling unique content and translating it; this review does not silently drop those sections. MANAB/communications, weather cards 05/16, and IFR cards 09/10/12 also have thematic overlap. Brief reminders may be useful, but detailed rules should eventually have one maintained home and links from other cards.

## Still requiring a full review

This is a targeted navigation/formula and structure review, not a completed line-by-line regulatory audit of the repository. Existing legal minima, fuel reserves, holding, approach bans, time-zone observance, NOTAM conventions, aircraft data and examination eligibility retain their previous review status. Verify against current Canadian sources before marking them reviewed. In particular, the earlier 2026-1 AIM and supplied September CFS are dated editions; commit dates do not refresh their validity.

Sources: [TC TP 975](https://tc.canada.ca/en/aviation/publications/flight-instructor-guide-aeroplane-tp-975), [FAA Instrument Flying Handbook](https://www.faa.gov/sites/faa.gov/files/pilots/FAA-H-8083-15B.pdf). New geometric examples are independently derived. No new legal requirements are asserted.

Validation: build reproducibility, preserved-entry coverage, generated-block synchronization, arithmetic and HTML structural checks. Browser rendering/interaction has not been tested in this review.
