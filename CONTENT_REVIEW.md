# Content review

## Open verification items

Carried from the retired CPAER coverage matrix; still open on 14 November 2026. Resolve each by source comparison in its own change.

| ID | Where | Issue | Compare against |
|---|---|---|---|
| X-01 | [`kb/ifr/cap-plates-publications.md`](kb/ifr/cap-plates-publications.md#publication-cycle) vs [`kb/nav/publications-cfs-cap-notam-currency.md`](kb/nav/publications-cfs-cap-notam-currency.md) | One says these publications update every 56 days; the other says schedules differ by product. | NAV CANADA product-specific schedules and edition dates. |
| X-03 | [Card 12 · unusual attitude, nose high](cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md#unusual-attitude--nose-high) | "reduce if near stall?" sits inside a generic memory flow. | Applicable TC training guidance and the AFM/instructor procedure; do not make it a universal memory action. |
| V-04 | [Card 07 · source / status](cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md#source--status) | C150M serial and configuration not confirmed. | Exact POH revision, supplements, equipment/STCs and W&B before treating figures as fleet data. |
| V-05 | [`kb/ifr/navaid-checks.md`](kb/ifr/navaid-checks.md) | Canadian and FAA VOR-check scopes are cross-referenced. | Keep the origins separate; do not import US intervals or recordkeeping. Not a contradiction. |
| V-06 | `kb/met` cloud base / freezing level and the formulas collection | Classroom and parcel models given side by side. | Keep both assumptions and the environmental freezing-level caveat. Not a contradiction. |

The item-by-item coverage that replaced the matrix is in `explorer/syllabus.json` and the explorer's guide pages; `python3 explorer/build_explorer.py --audit` lists concepts with TC items but no knowledge note.

## Ontology as hub; formulas and card 17 reworked — 14 November 2026

Text moved or re-laid out, not re-validated; unit IDs kept unless a repeat was retired.

- **Ontology:** note types (`study-*`, `type-c150`) are no longer concepts; each note has a `kind`. Every TC guide group names its concept, so a concept page shows its TC coverage and gaps. Related links are derived from shared notes and TC items. Build rejects a knowledge note in a card, an unknown kind, a guide group without a concept and a concept with no note and no narrower concept; `--audit` reports the rest.
- **Formulas collection** renamed `Formulas_Calculations_EN_FR.md` ("Formulas & calculations") and reduced to 11 formula sections. Six sections replaced their English-only twin in `kb` with the bilingual text (same rows; flight duty time gains 9 rows the twin lacked): ADF/VOR/DME intercepts, oxygen, passenger weights, flight duty time, de-/anti-icing, over-water survival. Six moved as bilingual units: twilight/time zones to `law-night`; CFS servicing, NOTAM header and NOTAM codes to `nav-pubs`; communications/weather services and FIR/FIC to `law-atc`.
- **Card 17 retired** into `kb/law`: licence → type requirements to `law-lic`; recency clocks to `law-recency` (CAR column folded into the label); operator checks, 703 single-pilot IFR, traps and sources to `law-type`; its Pebble line joined that file's Pebble. The 11-column operator table is now one block per operation with a PIC / SIC table (same cells, re-arranged). Source basis as recorded on the card: CARs consolidation current to 2026-09-30, Standard 421, TC AIM 2026-2 (reviewed 2026-10-24).
- **Readers:** the formulas and qualifications HTML pages now redirect to the explorer; the card 17 layout test is removed; the `MANAB_CFS_Essential` pointer stub is deleted. The abbreviations readers are unchanged.
- **New concept files:** `kb/law/night-vfr-ott.md` (twilight, night definition, VFR OTT) and `kb/nav/gnss-rnav.md`.
- **Open gaps from `--audit`:** no knowledge note yet for electrical systems, gyro instruments, other weather hazards, load factor (formulas only) or takeoff; airframe systems, propellers and the emergency concepts hold procedures only.

507 units (was 513).

## Cards 08, 11 and 12 consolidated into kb — 14 November 2026

Text moved, not re-validated; unit IDs kept.

- **Card 08:** 14 system-knowledge units moved to concept files: `kb/agk/engines-powerplant.md` (new: engine essentials, magnetos, mixture, oil pressure/temperature, powerplant, manifold pressure), `kb/agk/pitot-static-instruments.md` (new), `kb/agk/pressurization.md` (new), fuel grades and starvation to `agk-fuel`, carburettor icing and alternate air to `carb-ice`, magnetic compass to `nav-compass`, ELT equipment to `law-elt`. The 27 failure QRCs stay in card 08. The three new files have no Pebble yet.
- **Card 11 retired.** 21 knowledge units moved to `kb/ifr` (plate anatomy to `ifr-plates`, segments/FAF/profile/timing/navaid traps to `ifr-app-fly`, minima box/straight-in/lighting to `ifr-minima`, MAP to `ifr-missed`, INRAT plate method to the recall file), cold temperature to `met-cold`, landing distance to `agk-perfcalc`. "Frequencies / nav source" moved to card 12. 14 units were repeats and were retired into their `kb/ifr` or card 12 twin; lines not already present were carried into the survivor (minima `Vis` row, circling row in approach types, RASS source line, missed-approach brief and level-past-MAP trap, circling checks and category trap, plate-scan mnemonic, currency gate, spoken brief, before-FAF items, plate Pebble traps). Guide items and coverage-matrix links re-pointed.
- **Card 12:** its publication-cycle unit (identical to `kb/ifr`) retired.
- **Kept as cards after review:** 17 (bilingual operator-check tables with their own reader and tests) and the formulas collection, whose four air-law rows (oxygen, passenger weights, flight duty time, over-water) are the EN/FR versions of EN-only `kb/law` units; removing them would lose the French.

513 units (was 528).

## TC essential marks; levels from the guides — 14 November 2026

**Essential and depth marks** read from the TC HTML editions on this date (aeroplane icon = essential; shading = commercial depth): TP 12881 CPAER 181 essential items (93 C / 56 P / 32 M) and 303 shaded; TP 12880 PPAER 221 essential (112 C / 74 P / 35 M). Item positions matched the guides one-to-one (CAR numbers and per-group counts). TP 691, PSTAR and the flight test guides carry no such marks. Guide pages show ✈ and shading with filters; 167 notes cited by an essential item carry ✈ in result lists.

**Levels:** PPL / CPL / IR / ME badges now come from the guides citing a note (PSTAR, PPAER, PPL flight test → PPL; CPAER, CPL flight test → CPL; INRAT, IFR flight test → IR; ME flight test → ME); Pebbles take their file's levels. 388 notes derived; 140 not cited by any guide keep the hand tag, shown dashed. The licence-level views were removed from the views list (the guides replace them).

## Training stages replaced by the TC guides — 14 November 2026

The ten hand-made "training stage" views are removed. The home page now opens with the ontology's subjects, then the eight TC guides in training order (PSTAR, PPAER, PPL flight test, CPAER, CPL flight test, ME flight test, INRAT, IFR flight test), then phases of flight and the bilingual collections. Each guide is also a view: the units its items cite (e.g. INRAT 96 sections, where the old stage's concept list gave 297), so a guide view shows only what the syllabus mapping found. The two stages with no TC guide moved into the ontology: night and VFR OTT is a new concept `law-night` (five units tagged: VFR OTT, night definition, night VFR equipment, night go/no-go, twilight formulas); first commercial seat was already `law-commercial`.

## TC guide maps extended to all exams and flight tests — 14 November 2026

`explorer/syllabus.json` now holds eight guides. Item counts (Covered / Partial / Missing):

- **TP 12881 CPAER**, all four subjects in one guide (`tp12881`, replaces `tp12881-met`): 855 items, 254 / 254 / 347. Air law 318, Navigation 125, Meteorology 111, Aeronautics 301.
- **TP 12880 PPAER** (6th ed., May 2025): 605 items, 215 / 202 / 188.
- **TP 11919 PSTAR** (7th ed., Dec 2022): 73 topic items, 39 / 15 / 19. The guide is a question bank; items are the topics its 14 sections test.
- **Flight tests:** TP 13723 PPL 32 items (25 / 7 / 0); TP 13462 CPL 32 (24 / 8 / 0); TP 219 ME 24 (16 / 6 / 2); TP 9939 IFR 16 (16 / 0 / 0). Exercises are matched to procedure units; a unit supports practice and the oral, it does not replace the guide's performance criteria.
- **TP 691 INRAT:** unchanged except stale "card without IDs" notes resolved (ATIS, pitot-static, CFIT now point to units).

**Method, stated plainly:** CPAER air law, navigation and aeronautics, and PSTAR, were decided by hand from CAR-number citations, unit headings and matched text, **without a line-by-line read of every unit**. That is lighter than the Meteorology and INRAT reads. PPAER items reuse the CPAER decision for the same item (matched by CAR number or label within the section); PPAER-only items (301.06, 401.26, 606.02, electric motors, battery types, unapproved information) were decided by hand. The CPAER Meteorology "Elsewhere" status is gone: ATIS, hoar frost and altimeter settings re-judged against units. Item lists were read from the TC HTML editions on this date; nothing is validated against the CARs or AIM.

Topics found in no unit (text search): ADS-B, hyperventilation, situational awareness, wildlife areas, Bernoulli / Newton, radar clock position, rotating beacon, readability scale, student-permit privileges, how runways are numbered. Explorer: guide tiles grouped as written exams / flight tests, section headers and method line in each guide, and stage views 1–3 and 5–9 link to their guide.

## Abbreviations in the explorer — 14 November 2026

The abbreviations tile and PWA shortcut open collection A. The explorer selects EN/FR/both columns for MANAB/CFS and supplementary TC exam entries. All 54 individually labelled bilingual memory reminders from the legacy reader are available in the memory-traps unit, alongside its original grouped examples, which contain additional context. The existing reader URL remains published. Migration only; source editions and aviation wording carried forward.

## CPAER formulas in the explorer — 14 November 2026

The home collection tile and installed-app shortcut open the formulas card in the explorer. EN/FR/both selects the language columns and memory-trap explanations. The published standalone reader remains available through its existing URL and section links during migration. Study text and source references were carried forward without an aviation accuracy review.

## Consolidation completed; ontology and landing page — 14 November 2026

**Navigation, aeronautics, multi-engine consolidated** (no fact added, none re-validated): `nav-navigation` (01) and `nav-nav-met-systems` (03) retired into `nav-diversion-lost` (new, both divert lines combined), `nav-true-magnetic-compass`, `nav-1-in-60-rule` and `agk-systems-oral-list` (new); the card 03 MET summary line dropped as restated in `kb/met`. `agk-performance-w-b` (01) and `-c03` (03) retired into `agk-weight-balance` and `agk-performance-factors` (new). `agk-human-emergency` / `agk-emerg-human` regrouped as “Human factors / ADM” and “Emergency priorities” (duplicate CO lines combined). 18 per-concept Pebbles added.

**Pebble architecture:** one `#### Pebble` per concept file, nothing else. `kb/study/` removed: whole-card Pebbles (01, 03, 06, 13) and the ME memory atoms retired into the per-concept Pebbles; three units with real content moved (`ref-source-authority-c04` → `kb/law/air-law-procedures.md`, `ref-current-publication-cycle-c01` → `kb/nav/publications…`, `ref-source-rating-frame-c13` → `kb/me/me-training…`), each minus its historical-review sentence. Units added to `kb/met` / `kb/ifr` from cards 01 / 06 remain as separate units.

**Ontology:** heading-regex matching, path rules and per-card fallbacks removed. Every unit (cards included: 17, formulas and abbreviations Markdown gained ID comments) now declares its concepts and level in its ID comment; the build output was identical before and after (528 units: text, concepts, levels). Concepts gained `alt` search terms. Card header blocks (legend / release lines) are no longer indexed.

**Landing page:** `index.html` is now the generated explorer with a readers row; `explorer.html` redirects to it. READMEs reduced to indexes and format; provenance stays in this log.

## Air law consolidated — 14 November 2026

`kb/law`: six overlapping units retired, 14 per-concept Pebbles added, card 04's whole-card Pebble retired from `kb/study`.

Retired (content kept in the survivor unless noted): `law-vfr-minima-cruise-altitude` (01; every value restated by the 602.114 / 602.115 / 602.34 units); `law-airspace` (01) → `law-airspace-entry-memory` (adds “class rules ≠ weather minima” and the separation-matrix link); `law-docs-legal` (01) → `law-core-aircraft-documents` (adds licences/medical on board, valid-document trap) and `law-passenger-briefing` (adds the SAFETY brief memory line); `law-flight-plan-itinerary-pirep` (01) → `law-flight-plan-itinerary` (adds arrival-report, VFR position-report and PIREP formats); `law-ifr-fuel-reserve-memory` (06) → `law-fuel-requirements`; `law-instrument-rating-recency` (04) removed as a word-for-word duplicate of `ifr-instrument-rating-recency`, which stays filed under the recency concept.

**Checked against the project copy of the CARs (SOR/96-433) and CFS on this date:** 602.115 uncontrolled VFR minima (values match; **added the qualifier “unless otherwise authorized in an AOC” to the day 2 SM <1000 ft AGL value**, per 602.115(c)(i)); 602.88 fuel (VFR 30 / 45 min, IFR prop 45 min, turbojet/helicopter IFR 30 min: match; note 602.88(3)(b) gives helicopters 20 min VFR, not in the card, which is aeroplane-scoped); arrival-report contents, VFR position report and PIREP order (match CFS Planning section). **Everything else in `kb/law` is unverified consolidation.** Noted but not added: itinerary arrival-report deadline (602.77(2): SAR time, else 24 h after last reported ETA).

## Remaining knowledge cards moved to concept files; all cards ID'd — 14 November 2026

Cards 01, 03, 04, 06 and 13 moved into concept files (`kb/law`, `kb/nav`, `kb/agk`, `kb/me`, `kb/study`, plus additions to `kb/met` and `kb/ifr`) and deleted: 138 sections, **text unchanged** (machine-compared; one exact duplicate, card 06's sources line, kept once), concept links and level tags preserved, all other cards byte-identical. Each unit's primary concept was chosen automatically (most specific concept; card 04 prefers `law-…`, card 13 prefers `me-…`) and **has not been reviewed unit by unit**; the other concepts are in `also:`. Whole-card Pebbles and source notes are in `kb/study/`. 61 coverage-matrix links re-pointed.

Cards 02, 07, 08, 11 and 12 (procedures, POH, QRC) keep their place and now carry stable IDs. Cards 17, formulas and abbreviations are unchanged (paired with HTML readers; no IDs).

Not done for law / nav / agk / me: merging units that overlap across former cards, per-concept Pebbles, any validation against CARs / AIM. Units added to existing `kb/met` and `kb/ifr` files are not yet reflected in those files' Pebbles.

TP 691 map: the 21 formerly unchecked items re-judged against the new law units and cards 11 / 12: now **70 Covered, 91 Partial, 47 Missing**.

## TP 691 (INRAT) item map — 14 November 2026

`explorer/syllabus.json` now maps all 208 items of TP 691E (17th ed., 2013; item list read from the TC HTML edition on 14 Nov 2026) to unit IDs: **62 Covered, 83 Partial, 42 Missing, 21 Elsewhere**. Judged by reading `kb/ifr`, `kb/met` and card 05 only; **not validated against CARs / AIM / CAP**; CAR items judged on study coverage, not legal completeness. *Elsewhere* = cards without IDs (04 air law, 06, 08, 11, 12), not item-checked. Item labels are our own short wording under the guide's order.

Largest gaps: instruments and radio aids (principles of pitot-static, gyro and compass instruments; ILS / GPS principles; RMI, HSI, radar altimeter, flight director, surveillance radar, lightning detection), weather maps and prognostic charts (6), departure and arrival ATC procedures (ATIS, radar / non-radar departure, radar vectors), en route items (changes to flight plan, adherence to TAS, 1,000 on top, shuttle), Class F / special use airspace, reduced visibility operations, PEDs, situational awareness, CFIT.

Naming: exam codes used consistently in the explorer and README (PPAER, CPAER, INRAT).

## IFR: merged near-duplicates, per-concept Pebbles, X-01 cycle dates — 14 November 2026

**No fact re-validated against CARs / AIM / CAP**; consolidation of existing text, same rule as Meteorology (keep every distinct fact and qualifier; drop a line only when fully restated).

Merged (survivor ← retired): `ifr-ifr-in-vmc-vfr-restriction` ← `…-visual-restriction`; `ifr-alternate-minima` ← `…-core` (TAF/GFA lines left to `ifr-taf-alternate-logic`; table keeps card 09's `600-2*` / `800-2*`); `ifr-clearance-readback` ← `…-inrat`; `ifr-ifr-route-altitude-terms` ← `ifr-minimum-altitudes-terrain`; `ifr-holding` ← `ifr-holds`; `ifr-approach-types` ← `…-minima`; `ifr-rnav-gnss` ← `ifr-gnss-rnav`; `ifr-landing-minima-visual-reference` ← `…-inrat`; `ifr-approach-ban-rvr-general-aviation` ← `ifr-rvr-approach-ban`; `ifr-missed-approach` ← `…-inrat` (circling-lost-reference line left to `ifr-circling`); `ifr-rass-remote-altimeter` ← `ifr-rass-altimeter`; `ifr-lost-comms-general` ← `…-inrat`; `ifr-lost-comms-ifr-route-altitude-time` ← `ifr-lost-comms-vmc-imc` (adds card 10's “holding instruction **acknowledged**”). Reworded while merging: the clearance-contents line and the lost-comm `P:` line (both lists combined).

Pebbles: 15 per-concept Pebbles (`ifr-<file>-pebble`); the two card Pebbles are retired.

**X-01 (stale cycle):** cycle statements in `kb/ifr` and cards 11 / 12 now read “at last review (14 Nov 2026): 2026-10-29 through 2026-12-24” with a trap that the line ages every 56 days. These dates are **computed** from the 56-day cycle stated in the cards (9 Jul → 3 Sep → 29 Oct → 24 Dec), **not read from the NAV CANADA schedule**. PFAF lightning-bolt lines (AIC 013/2026) no longer call 29 Oct “future”; implementation is flagged `?` as not confirmed on a printed chart. Card 01 and 04 mentions of July 2026 are already marked historical and were left.

## IFR / INRAT moved to concept files — 14 November 2026

Cards 09 and 10 moved into 16 concept files under `kb/ifr/` (60 units, new permanent IDs `ifr-…`), then deleted. **Unit text unchanged** (machine-compared: every old section's text present; no concept link lost; all other cards byte-identical). Three units identical in both cards kept once: Instrument-rating recency, Current publication cycle, Sources & review status. Card 10 headings that collided with card 09 in the same file carry a `· INRAT` suffix. Six coverage-matrix link definitions re-pointed.

Not done: near-duplicate units (clearance, IFR in VMC, lost comms, holding, RASS, landing minima, missed approach, alternate minima, approach ban, GNSS) are side by side, **not merged**; no per-concept Pebbles (both card Pebbles are in `kb/ifr/recall.md`); nothing re-validated against CARs / AIM / CAP. **X-01 still open and now lives in `kb/ifr/cap-plates-publications.md`**: the "current" AIRAC cycle reads 9 Jul–3 Sep 2026. Cards 11 and 12 (procedures) unchanged.

## V-02 closed — 14 November 2026

Verified against Transport Canada AIM 2026-2, MET 7.3, printed p. 158 (TEMPO). Each occurrence lasts less than one hour. Their combined duration may equal half of the indicated TEMPO window. Updated the TAF unit and Pebble, EN/FR glossary and reader, syllabus note and coverage records. Earlier entries below are historical snapshots.

## Meteorology: merged overlapping units, per-concept Pebbles, card 16 removed — 14 November 2026

Branch `feat/kb-met-concepts`. **No fact was added and nothing was re-validated against the AIM**; this is consolidation of existing card text.

Merged (survivor ← retired ID): `wx-fronts` ← `wxp-stability-fronts-fog`; `wx-icing` ← `wxp-icing`; `wx-carb-ice` ← `wxp-carb-ice`; `wx-turbulence` ← `wxp-turbulence`; `wx-microburst` ← `wxp-llws`; `wx-mountain-wave` ← `wxp-mountain` (heading now “Mountain wave / terrain weather”); `wx-thunderstorms` ← `wxp-convection` (heading now “Thunderstorms”); `wx-products` ← `wxp-product-roles` (heading now “Product roles”). Rule applied: keep every distinct fact, qualifier, tag and procedure line; drop a line only when the surviving text already states all of it; where a dropped line held one extra fragment, that fragment was appended to the surviving line in the source's own words (`broad ice` on the stable-air line; `well above freezing` and `descent` for carb ice; `then recovery`; `TCU/CB/showers` for convective turbulence; `strong inversion/low-level jet, large surface-vs-aloft wind difference` in microburst clues; `instrument errors` in TS hazards; `large margin: cells/lines/embedded TS`; `lower-severity/unforecast hazard` on the AIRMET row; icing intensity `trace/light/moderate/severe`). Dropped outright: card 16's pointer line to the old QRC, and summary lines for fronts, fog and stability that restated card 16. All other units byte-identical (machine-compared).

Pebbles: each concept file except `recall.md` now ends with a `#### Pebble` (13 new units, `<concept>-pebble`) recapping only that file; card 16's whole-card Pebble (`wx-pebble`) was distributed into them and retired; card 05's Pebble now recaps only its remaining flow/gate sections. The TAF Pebble repeats the unit's `TEMPO … ≤½` and flags the unresolved V-02 conflict with `?`; **V-02 is still open** (the AIM MET text could not be retrieved this session; ICAO/WMO-derived sources read “less than half”).

Removed for simplicity (owner decision, early-stage project): `cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md` and the pointer headings in card 05. Coverage-matrix link definitions for cards 05/16 (29) re-pointed to the concept files. `explorer/syllabus.json` IDs updated; Meteorology counts unchanged (51 C / 33 P / 26 M / 1 E). Explorer: persistent “✕ Clear” button beside search (also Esc).

## Meteorology concept-file pilot — 14 November 2026

Branch `feat/kb-met-concepts`. Moved 54 knowledge units (all 32 of card 16; 22 of card 05) into 14 concept files under `kb/met/`, one per ontology concept, theory units first then decoding/QRC units. **Unit text is unchanged**: before/after builds compared per unit ID gave 67 → 67 units, 0 text differences, 0 lost concept links, 0 level changes (one relative link in the de-icing unit re-pointed `../` → `../../`). Two headings gained a `· QRC` suffix to avoid duplicate headings in one file (Turbulence, Carburetor icing). Card 16 is now a pointer page; card 05 keeps its 12 flow/gate sections and Pebble, with pointers under the moved headings so existing anchors still land. Card headers (legend, release status, source line) are reproduced in `kb/met/README.md`.

Not done: overlapping units from the two cards (fog, fronts, icing, carb icing, turbulence, microburst/LLWS, trend) sit side by side and are **not merged**; no per-concept Pebbles yet (card 16's Pebble and exam traps are in `kb/met/recall.md`; card 05's Pebble still summarizes units that moved). The de-icing unit remains duplicated in the formulas Markdown/HTML reader. Explorer reads `kb/` directly (concept and level from file/unit comments, no heading regex); build fails on a missing ID, unknown concept, or a pointer whose target heading does not exist. AGENTS.md gained three authoring rules for concept files and unit IDs.

## Card 05 stable IDs; Meteorology map completed — 14 November 2026

Card 05: 34 sections given stable IDs (`wxp-…`, invisible comment under each heading); card 06: `calc-temperature` on the Temperature section only. No study text changed. `explorer/syllabus.json` re-judged the 18 formerly unchecked TP 12881 Meteorology items against card 05 and added card 05 evidence to existing rows: now **51 Covered, 33 Partial, 26 Missing, 1 Elsewhere** (weather information from ATS: ATIS mentions in cards 04 / 12 / 13, not checked). Still judged by content read only, not validated against AIM MET. FCST 4 (TAF) carries the open V-02 TEMPO wording conflict as a note. Explorer topic graph opens by default again, replaces the duplicate chip rows while open, and gains an “All topics” node above the broader concepts.

## Stable unit IDs (card 16) and TP 12881 Meteorology item map — 14 November 2026

Pilot of ID-anchored mapping. Card 16: each of the 32 sections now carries a stable ID as an invisible comment on the line under its heading (`<!-- id: wx-fog -->`); no study text, Pebble or heading changed. IDs are card-independent (`wx-…`), must stay unique, and must not be renamed once referenced.

`explorer/syllabus.json`: all 111 Meteorology items of TP 12881 (7th ed., Aug 2026; item list read from the TC HTML edition on 14 Nov 2026) mapped to unit IDs with status and gap note: **41 Covered, 27 Partial, 25 Missing, 18 Elsewhere**. Item labels are our own short wording under the guide's group order and numbering; the guide text governs. *Elsewhere* = topic belongs to a card without IDs yet (mainly 05 decoding, also 01/04/06/10/12) and was **not** checked at item level. Covered/Partial judged against card 16 text only, by content read, not against AIM/MANAB for accuracy. Collection-wide absences confirmed by text search: CFPS, trowal, isothermal layers, latent heat, hoar frost (MET sense), analysis/prog charts, other-hazards group. Supersedes the group-level Meteorology rows of the 22 Oct matrix for card 16 evidence; matrix file itself unchanged. Gate 1 remains open for other subjects.

Explorer: guide coverage screen (status filter, per-group bars, tap-through to the unit), `#u-<id>` deep links, guide-item chips on each ID'd section. Build fails on unknown/duplicate IDs or a Partial item without a gap note.

## Explorer views and card 08 table format — 14 November 2026

Explorer: replaced the single path filter with **views** defined in `explorer/ontology.json`: ten training stages (pre-solo to first commercial seat), eight phase-of-flight quick-access sets, and the four licence-level tags. Each stage names the TC guide it is aimed at (TP 11919, 12880, 13723, 12881, 13462, 219 / 11575, 691, 9939, 13524); TP numbers checked against the TC publications list on 14 Nov 2026. Stage membership is a **topic-based approximation, not an item-by-item mapping** to those guides. Topic graph now starts collapsed; Pebble sections display as wrapped tokens (display only, Markdown unchanged).

Card 08, format only: AVGAS row in the fuel-grade table contained unescaped `|`, so GitHub dropped the 100/130 and 100LL cells; separators changed to `·`. Added a missing closing `|` on one Powerplant row. No fact, qualifier or Pebble changed.

## Knowledge explorer prototype — 14 November 2026

Added generated `explorer.html` (single offline file) with `explorer/ontology.json`, `template.html` and `build_explorer.py`. 527 sections from all 14 numbered cards plus the formulas and abbreviations Markdown are embedded unchanged and indexed by 92 SKOS-style concepts (broader / narrower / related, polyhierarchy), four study paths (PPL / CPL / IR / ME) and source card. Mapping is heading-regex based and **editorial**: not a TP 12881 item mapping, not a coverage claim, and PPL tagging is by judgment (no PPL syllabus audit). No study content, Pebble or reader changed. Added to index, manifest shortcut, PWA precache (VERSION bumped) and offline test; `tests/explorer.test.cjs` checks ontology integrity and that the generated file is current. Checked in headless Chrome at 390 px and 1100 px; not tested on a device or installed PWA.

## CAR 703 single-pilot IFR 50-hour minima — 26 October 2026

Card 17 Markdown/HTML: added a separate, prominently labelled 723.86 single-pilot IFR passenger-operation requirement: 1,000 hours total, 100 hours ME if multi-engine, 50 hours actual/simulated IMC and 50 hours on aeroplane type; PPC autopilot assessment and FL250 limit for pressurized aeroplanes. Explicitly not a blanket CAR 703 PIC requirement. Source: Transport Canada Standard 723.86 (aeroplanes). PWA cache bumped. Visual tests not run.


## Illustrative aircraft models in operating-category matrix — 26 October 2026

Added a model-examples column to all 10 PIC/SIC entries in Card 17 Markdown and bilingual HTML. Covers representative 604 private piston twin/pressurized piston/single turbine/jet/large business jet; 702 aerial-work aircraft; 703 single- and multi-engine air taxi; 704 19-seat commuter aircraft and qualifying business jet; 705 regional and airline aircraft. Examples are non-exhaustive and do not confer a regulatory subpart: actual type, certification, seats, mission, aircraft weights and air-operator approvals control. Manufacturer references added; HTML mobile layout updated and offline cache version bumped. Not browser- or device-tested.


## CAR 604 scope versus private-operator registration — 26 October 2026

Clarified both 604 rows in Card 17 Markdown and HTML: section 604.02 is a logical **OR** across four aircraft categories (large, turbine-powered, pressurized, multi-engine). Section 604.03 is a *separate* registration obligation when carrying passengers or goods in large aeroplanes, turbojets, or turbine-powered pressurized aeroplanes with more than six certificated passenger seats, subject to specified exceptions. Clarified that a small unpressurized piston twin can meet 604.02 without itself triggering 604.03 registration. Source: live CAR 604.02/604.03 (current to 2026-09-30). PWA cache bumped; mobile/browser tests not run.


## Aircraft applicability and dual-unit limits — 26 October 2026

Card 17 Markdown and bilingual HTML: added aircraft applicability to each PIC/SIC row of Table 1, with metric and regulatory pound equivalents: large aeroplane >5,700 kg (>12,566 lb); 703/704 multi-engine MCTOW ≤8,618 kg (19,000 lb); 704 turbojet MZFW ≤22,680 kg (50,000 lb); 705 aeroplane MCTOW >8,618 kg (>19,000 lb) or type certificate ≥20 pax. Distinguished 604.02 aircraft scope from 604.03 private-operator registration; noted 702 work-based applicability and applicable authorization exceptions. Verified against current online CAR 101.01, 604.02–.03, 702.01, 703.01, 704.01, 705.01 (CARs current to 2026-09-30). Existing operator/seat/PPC/CC content retained. Updated HTML mobile table layout and PWA cache version. Browser and offline device testing outstanding.


## Pilot licensing / PPC / CC / type-rating decision card — 24 October 2026

Added Card 17 as a **bilingual CAVE quick-reference** (standalone Markdown + HTML reader), referencing authoritative Card 04 rather than moving or deleting legal material. Cross-checked operative PIC/SIC distinctions against CAR 702.65, 703.88, 704.108, 705.106; check validity against 604.139, 702.67, 703.91, 704.111, 705.113; current instrument recency under 401.05; type requirements in Standard 421.40; licence headline hours in TC AIM 2026-2. Live CARs consolidation noted current to 2026-09-30 (last amended 2026-06-17). Exam summary deliberately excludes complete Ops Specs, Part IV aircraft-specific limits and alternate programs. Added index, README, manifest shortcut, PWA cache entry/version and offline cache-test path. Browser/device rendering not independently verified.

## CPAER Phase 2 content audit — 22 October 2026

Added CPAER coverage matrix (since removed), based on repository commit `3dbd013ba1e93160727d40b6fde8f4a0e50ca0f4` and official TC TP 12881 seventh edition, August 2026 (HTML/PDF edition verified). Topic-group screening across the syllabus; individual rows for 52 Flight Instruments and 40 Human Factors items. Active Markdown evidence inspected, including all 14 numbered cards and supplementary bilingual recall/glossary content. Not a fresh regulatory/medical/POH validation or an exam-completeness claim.

Logged publication-currency conflict in cards 09–12 versus 01; TEMPO ≤half/<half wording difference; ambiguous nose-high recovery wording in card 12. Authoritative resolution remains pending. Distinguished qualified VOR source scopes and cloud/freezing calculation models from harmful duplication. Gate 1 remains open for other numbered-item expansion; no study facts, Pebbles, reader code, HTML or PWA assets changed.

## Manoeuvring speed / stall speed — 22 October 2026

Card 06, bilingual CPAER formulas Markdown and HTML reader: added theoretical `VA_est=VS(clean)√n_limit`, legacy Normal-category +3.8g `VA_est≈1.95 VS1` (mental shortcut ≈2×VS1; not a range of VA values), matching-weight `VA₂≈VA₁√(W₂/W₁)`, and `VS` (generic) / `VS1` (specified, commonly clean) / `VS0` (landing) distinctions. This theoretical intersection is not necessarily published certified `VA`; POH/AFM wins and `VA` offers no blanket structural protection. Card 06 Pebble updated; HTML stall group 9→12 and total 248→251; PWA cache bumped.

## Cloud-base and freezing-level calculation clarification — 22 October 2026

Corrected bilingual `CPAER_Formulas_Recall_EN_FR.md` and matching HTML reader (weather rows 10→13; overall entries 245→248). Separated classroom convective-base shortcut `1000(T−Td)/3` (assumes parcel Td constant), parcel LCL `1000(T−Td)/(3−0.5)` (parcel dew point falls ≈0.5°C/1000 ft; temperature–dew-point spread closes ≈2.5°C/1000 ft), classroom parcel 0°C height `CB+1000 Td_surface/1.5`, and fuller parcel calculation using estimated temperature at cloud base. All are simplified parcel estimates, **not** an observed/forecast environmental freezing level; GFA/vertical temperature profile governs. Synchronized weather card 16 and its Pebble; updated PWA cache version. Bilingual rows/HTML refetched, not tested on a mobile browser.

## Canadian flight authorities — 22 October 2026

Card 04: added a two-column CAR 507 flight-authority classification/meaning table (C of A; Special C of A provisional, restricted, amateur-built, limited, owner-maintenance; Flight Permit experimental/specific purpose), distinguished type-certification categories and passenger privileges, and updated the final Pebble. No categorical PAX permission column; actual authorization depends on flight-authority conditions, operating limitations, pilot privileges and CARs.

## Airfoil / washout / aspect ratio — 22 October 2026

Card 01: added five compact L4 rows on airfoil geometry (chord, camber, thickness, critical AOA), geometric washout versus dihedral (generally root-first stall, not guaranteed), aspect ratio `b²/S` and rectangular `b/c`, induced-drag relation `CDi=CL²/(πeAR)` with equal-CL/span-efficiency scope, and airfoil/stall traps. Updated the final Pebble. FAA PHAK aerodynamics source pointer retained; no paired HTML reader.

## Cards 01–03 scope, aerodynamics and filenames — 22 October 2026

Renamed cards and canonical filenames: **01 Flight Theory & VFR Knowledge**, **02 Flight Training and Procedures**, **03 Licensing, Performance & Operations**. Card 01 gained essential lift, CP/CG/AC, pitching moments, induced and parasite/form drag, equilibrium, and bank/load-factor relations, including final Pebble. Cards 02–03 had display titles updated; content otherwise unchanged. README, review links and archived source-index pointers migrated to new filenames.

## Weather fronts consolidation — 22 October 2026

Card 16 remains the canonical weather theory source, including cold/warm frontal passage tables, hazards and memory traps. Removed duplicate bilingual `cheatsheets/Weather_Fronts_EN_FR.md` and `readers/Weather_Fronts_EN_FR.html`; cleaned README, app index, PWA manifest, service-worker precache and offline test references. Existing historical review entries retained; bilingual reader functionality discontinued rather than duplicating card content.

## TKOF speeds / OEI / tire speed · L4 CAVE — 22 October 2026

Card 13: five compact rows for V1 reject/continue and accelerate-stop, VR rotation, V2 One Engine Inoperative (OEI) takeoff safety/climb rather than braking, Vtire as maximum certificated tire **groundspeed**, and GW/RWY/conditions/transport-category-versus-light-twin scope; revised final Pebble. Existing light-twin accelerate-stop/go and Vmc/Vyse references preserved. FAA Airplane Flying Handbook Chapter 16 cited; aircraft AFM/POH remains controlling. Markdown-only card, no paired HTML.

## Turboprop ALPHA / BETA / ground fine / reverse — 22 October 2026

Card 08: replaced the short BETA mention with concise separate ALPHA normal governed-flight range, BETA ground power-lever blade-angle control, ground-fine low forward thrust, reverse negative blade angle subset of BETA on equipped ACFT, and FLT-idle/AFM limitations. Updated local L4 and final Pebble; retained distinction from feathering. Reviewed FAA Airplane Flying Handbook turboprop operations; limitations are aircraft-specific. Card 08 has no paired HTML reader.

## Cabin pressurization / outflow valve · L4 CAVE — 22 October 2026

Added seven concise rows to card 08 and final Pebble: cabin altitude versus aircraft altitude; outflow valve control of cabin pressure by modulating discharged air; close/open effects; differential pressure ΔP = cabin − ambient; positive/negative relief; loss of pressurization with O₂/emergency descent per AFM. Cross-referenced oxygen requirements already present in card 04 CAR 605.31–32 without repeating thresholds. Source pointers: FAA PHAK pressurization systems and CAR 605.31–32. Card 08 has no paired HTML reader; AFM/checklists prevail.

## Aviation fuels / FSII · L4 CAVE — 22 October 2026

Added 8 compressed fuel-grade/FSII rows to card 08 and its final Pebble: octane = detonation resistance, dual 80/87 and 100/130 lean/rich ratings, 100LL low-lead (not unleaded), AVGAS grade colours, Jet A and A-1 maximum freezing points (−40°C and −47°C), Jet B wide-cut volatility, FSII water-ice inhibition (not fuel freezing point or airframe anti-icing), and approved-fuel/misfuelling warning. Aircraft-specific AFM/POH approval prevails; legacy grades are study recognition, not universal current availability or compatibility. FAA fuel guidance, FAA FSII guidance, and Canadian turbine-fuel specifications linked within card. No paired HTML reader for card 08.

Current editing workflow: edit Markdown directly; update matching HTML/cards in the same change. The earlier JSON/build experiment described below has been removed. Study content and reader features are retained.

## VREF and CFS PF additions — 20 October 2026

Added the landing reference speed definition, the `1.3 VSO` fallback with a worked example, and the square-root-of-weight adjustment to card 06 and both bilingual reader editions. The text distinguishes published POH/AFM VREF from a fallback calculation, approach-category speed at maximum certificated landing weight, and an operational wind/gust additive. Sources checked: TC AIM 2026-1 RAC 9.21 and AWM Chapters 500/525.

Expanded the CFS servicing block with the separate `PF` public-facilities legend: location letters A–D, facility numbers 1–8, and a decoding example. Source: supplied CFS General (12 June–7 August 2025), consistent with the existing MANAB/CFS card; use the current CFS for flight. The bilingual formulas reader now contains 236 rows and 11 reminders.

## VFR airspace separation matrix — 20 October 2026

Added a Class A–G VFR entry and ATC-service matrix to card 04 and linked it from card 01. It distinguishes formal separation, traffic information and conflict resolution; covers the Class C/D-to-E change outside ATC operating hours; and separates runway separation from airborne VFR separation. Checked against TC AIM 2026-2 RAC 2.8.1–2.8.7 and Standard 821.01. The TC AIM 2026-2 explanation of changes lists no change to RAC 2.8 from 2026-1.

## Air-law Cave audit / correction — 21 October 2026

Corrected card 04 after reviewing repository `AGENTS.md`: replaced prose-heavy insertions with compact rule/trap tables and L4 memory lines. Coverage: CoR/CoA and transfer/interim/temporary/provisional registration; technical records (**variable-pitch PROP only**); ELT scope/exemptions/tests; AME/AMO and abnormal-occurrence inspections; DML/MPM/MCM/MSA; ATS/wake/RVSM; tower light signals; TSB reporting. Existing numbered-card `#### Pebble` retained and updated; no standalone air-law HTML reader exists. Regulatory source pointers embedded in card; review based on CAR/TC AIM references, not an operational dispatch authority. Original update commit: `9ed75e8`.

## L4 Pebble authoring skill — 21 October 2026

Added `.agents/skills/write-l4-pebble/SKILL.md` and linked it from `AGENTS.md`. The skill specifies scan-first L4 memory lines, MANAB/CFS abbreviation verification, legally significant scope/exception preservation, a mandatory `#### Pebble` recap for numbered cards, paired reader synchronization, and a pre-commit accuracy checklist. Complements the existing `build-cave-study-readers` skill; no study-card content changes in this commit.

## PRM / PRMCS addition — 21 October 2026

Card 04: added AMO PRM and AOC maintenance-control PRMCS distinctions, PRM experience (STD 573.04: six years; six months within prior two years), regulatory knowledge test and exceptions, PRM acceptance within 30 days, non-delegable accountability, and combined AOC+AMO same-person requirement. Updated subsection L4 memory and final `#### Pebble`. Sources: current CAR 573.03–.04, 706.03 and TC Standard 573.04 (verified 21 October 2026). No air-law HTML reader paired with card 04.

## CoR certificate fields — 21 October 2026

Card 04: added CoR document fields (REG marks; manufacturer, model and serial number; registered-owner name/address; purpose PVT/COM/State; issuer/issue details). Distinguished purpose classification from operational authorization and the CoR from CCAR-only MTOW (not printed on the certificate). Updated section L4 recall and numbered-card `#### Pebble`. Source: TC AC 202-002 §3, §7.2; verified 21 October 2026. No paired HTML air-law reader.

## AAIR continuing airworthiness — 21 October 2026

Card 04: added annual airworthiness information report (AAIR) CAR 501 / STD 501 in compact CAVE table and final `#### Pebble`: owner/report applicability, MAR 30 deadline for JAN–DEC (or prior agreed date), CAWIS/form 24-0059, data and Part IV/VII inspection-reporting distinctions, qualifying out-of-service exception and return-to-service notification. Clarified `PROP` in AAIR may cover fixed- or variable-pitch where applicable, whereas **separate technical record applies to variable-pitch PROP only** under CAR 605.92. Source links embedded in card; verified against CAR 501.01/501.03 and Standard 501.02, 21 October 2026. No paired HTML air-law reader.

## Commercial night VFR with PAX — 21 October 2026

Card 04: expanded night-VFR equipment into compact CAVE rows: baseline 605.16(1), conditional LDG light with PAX, 605.16(4) additional AI/VSI/ASI anti-ice/OAT for Subpart 604 and commercial 702–705 **irrespective of PAX**, 703 night-specific equipment, and CAR 703.22 / STD 723.22 AOC authority + turbine / approved STC + equipment for SE transport of PAX IFR/night VFR. Includes current 723.22 amendment effective 2026-09-01 and airborne WX radar amendment effective 2026-04-10; updated section memory and final Pebble. Sources checked: current CAR 605.16; CAR 703.22/703.64; TC Standard 723.22 (last amended 2026-09-10). No paired HTML reader for card 04.

## MP over-square / overboost precision — 22 October 2026

Card 08: distinguished over-square numerical relation (MP inHg > RPM/100; may be permitted) from overboost (MP above approved operating-condition/RPM-dependent limit). Added 25 inHg / 2300 RPM example; updated section L4 and final Pebble. Specific POH/AFM MP–RPM limitations control; no corresponding HTML reader.

## Aviation abbreviations · MANAB / CFS / TC examinations — 22 October 2026

Renamed canonical bilingual glossary and HTML reader to `cheatsheets/Aviation_Abbreviations_MANAB_CFS_TC_EN_FR.md` and `readers/Aviation_Abbreviations_MANAB_CFS_TC_EN_FR.html`. Retained 369 MANAB/CFS entries and added 79 TC flight-crew examination entries in a separate searchable bilingual topic. Shared symbols remain source-qualified (`AD` directive vs aerodrome, `MP` manifold pressure vs `MAP` missed approach point, `FD` upper winds vs flight director, `CARs/CARS`, `FPD/FDP`, turbine N conventions). English expansions are study mappings based on TC examination abbreviation list; French additions are study translations, not claimed official TC terminology. Previous filenames now redirect/link to canonical renamed editions. Updated README, home page, manifest shortcut, precache path/version, offline test fixture and repository authoring skill path. No separate source-code generator introduced. Reader markup and category/search wiring verified structurally, not in a real mobile browser.

Primary source: https://tc.canada.ca/en/aviation/licensing-pilots-personnel/flight-crew-licences-permits-ratings/flight-crew-examinations/abbreviations-acronyms-flight-crew-examinations

## Turbine engine architecture / PROP governor / feather L4 — 22 October 2026

Card 08: ultra-dense Powerplant/PROP CAVE table + local L4 + final Pebble; core turbine cycle, turbojet/turbofan/turboprop/turboshaft, BPR vs AFR, axial/centrifugal compressor, stage vs spool/free turbine, fine/coarse/feather/reverse/beta and constant-speed governors. Card 13: short ME governor/feather cross-reference + final Pebble. Qualified opposing oil-pressure directions as **typical piston non-feather SE** versus **typical piston full-feather ME**, not universal: POH/AFM/SOP authority remains controlling. Sources reviewed 22 Oct 2026: FAA PHAK (FAA-H-8083-25C), FAA Airplane Flying Handbook transition-to-ME chapter, FAA AMT Powerplant Chapter 7. Both numbered cards Markdown-only; no matching HTML reader.

## HP / two-crew type-rating eligibility and PPC transition — 21 October 2026

Added compact CAVE table and final Pebble in air-law card 04. Verified current CAR 400.01 HP/complex definitions, STD 421.40(1)–(3) (including integrated ATP(A) alternative effective 17 Dec 2025), TC IATRA study guide (70%, 24-mo exam window), and TC ACP/AQPE Bulletin 01/26 (704 PPC transition 01 Nov 2026). Kept HP 12-mo qualifying FLT, two-crew 12-mo PPC/AQP/604 PCC route, exam-to-application window, and recurring operator checks separate. No dedicated card-04 HTML pair exists; CPAER formulas bilingual reader has separate scope and was not altered in this edit.

Sources: https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/section-400.01.html ; https://tc.canada.ca/en/corporate-services/acts-regulations/list-regulations/canadian-aviation-regulations-sor-96-433/standards/standard-421-flight-crew-permits-licences-ratings-canadian-aviation-regulations-cars ; https://tc.canada.ca/en/aviation/commercial-air-services/approved-check-pilot-acp-advanced-qualification-program-aqp/acp-aqpe-bulletins/approved-check-pilot-acp-advanced-qualification-program-aqp-evaluator-bulletin-no-01-26

## CAR 604 / 700 FDP, split duty and unforeseen extensions — 21 October 2026

Added scan-first 604/700 comparison to card 04 with L4 Pebble; synchronized nine bilingual rows in the CPAER formulas Markdown and HTML reader. Covers: 604.99 base 14 h or 15 h if preceding 30 d FDP ≤70 h OR prior REST ≥24 h; 604.100 ≥4 h split credit half capped +4 h; 604.102 UOC after FDP start capped +3 h; 700.28 time-of-day/sector FDP table; 700.50 ≥60 min split less 45 min and 100% night/50% day credit; 700.63 early UOC PIC/crew conditions and crew-dependent +1/+2/+3 h; 700.64 unforeseen split replanning; subsequent REST increases where explicitly required. Distinguishes FDP extension from unchanged FLT time limits, and Part 700 Division III from Division IV MEDEVAC. Checked Canadian Aviation Regulations online 21 Oct 2026 (sections 604.98–.102, 700.27–.28, .40, .50, .63–.64). HTML content structure manually checked; browser behavior not exercised.

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
| Bilingual formulas, quick recall, navigation, ETE | CPAER_Formulas_Recall_EN_FR.md | CPAER_Formulas_Recall_EN_FR.md + HTML; navigation/ETE also present in 06 |
| Additional calculations and IFR reminders in 06 | 06 MD | 06 MD |
| MANAB terminology | Aviation_Abbreviations_MANAB_CFS_TC_EN_FR.md and matching reader | Still a manually maintained pair |
| Subject-specific cards 01–16 | Their existing Markdown files | Subject-specific review sheets |
| Older formulas | archive/CPAER_CAVE_Formulas.md | Historical only |

The 06 card and bilingual dataset still overlap outside navigation/ETE. Consolidating them completely requires reconciling unique content and translating it; this review does not silently drop those sections. MANAB/communications, weather cards 05/16, and IFR cards 09/10/12 also have thematic overlap. Brief reminders may be useful, but detailed rules should eventually have one maintained home and links from other cards.

## Still requiring a full review

This is a targeted navigation/formula and structure review, not a completed line-by-line regulatory audit of the repository. Existing legal minima, fuel reserves, holding, approach bans, time-zone observance, NOTAM conventions, aircraft data and examination eligibility retain their previous review status. Verify against current Canadian sources before marking them reviewed. In particular, the earlier 2026-1 AIM and supplied September CFS are dated editions; commit dates do not refresh their validity.

Sources: [TC TP 975](https://tc.canada.ca/en/aviation/publications/flight-instructor-guide-aeroplane-tp-975), [FAA Instrument Flying Handbook](https://www.faa.gov/sites/faa.gov/files/pilots/FAA-H-8083-15B.pdf). New geometric examples are independently derived. No new legal requirements are asserted.

Validation: build reproducibility, preserved-entry coverage, generated-block synchronization, arithmetic and HTML structural checks. Browser rendering/interaction has not been tested in this review.


## Operational additions — 19 October 2026

Added 57 bilingual rows (230 total, 11 reminders): oxygen supply versus use; passenger standard and segmented weights; flight time/FDT/FDP, baseline 700.28 tables and rest; de-/anti-icing types, FPD, LOUT and HOT; over-water flotation, rafts and land survival.

- Oxygen: CAR 605.31–32 live text, consolidation current to 30 September 2026. Pressurized emergency quantities are referred to the full table rather than reduced to a misleading universal number.
- Passenger weights: supplied AIM 2026-1, RAC 3.4.7 Tables 3.1–3.3 (printed p.213), cross-checked against live AC 700-022. Adult female values are 172/178 lb, not older or conflicting search-result values. Segmented figures transcribed from the supplied AIM. This is an explicit edition reference, not a claim that the latest AIM edition was fully reviewed.
- Fatigue: live CAR 604.98, 700.28 and 700.40; TC prescriptive summary for 700.27/29. Baseline table is included with its three flight-duration/count groupings and day-VFR exception. Special extensions, reserve, acclimatization and FRMS require their complete provisions; this is not a complete roster-compliance calculator.
- Fluids: TP 14052 March 2026, plus TC's current HOT landing page identifying winter 2026–27. No product-specific holdover minutes were invented or copied from an older winter. Current seasonal fluid tables must be consulted for an actual HOT.
- Water: live CAR 602.61–63 and 703.83. Aeroplane thresholds are covered; helicopter-specific raft/suit rules are outside this CPAER table. Recommendation rows are distinguished from legal requirements.

The shared JSON now generates oxygen, weights, fatigue and water sections in card 04, and fluid/HOT content in card 05, in addition to the reader MD/HTML. Prior short oxygen/survival blocks and duplicate flight-time table were replaced. These targeted subjects supersede the corresponding pending-review status above; unrelated regulatory sections remain pending.

Validation: reproducible outputs across reader MD/HTML and cards 04/05/06; total rows, topic/control markup, LOUT and raft examples. Browser interaction/layout was not tested in this update.


## Reader-first organization

README now opens with GitHub-readable notes and HTML reader links, followed by descriptive subject links. Bilingual Markdown topics use headings for GitHub navigation. JSON, build scripts and the unused renderer template were removed; their history remains in git. No study rows were removed. Future edits must update overlapping Markdown/HTML content together.

## Historical source review notes

Moved from the study cards on 19 October 2026. These are historical review records; moving them does not revalidate the content or update its source dates.

### [10_inrat_knowledge_core_av_cave_v0_3.md](cheatsheets/10_inrat_knowledge_core_av_cave_v0_3.md)

##### Validated-source notes — v0.2

- Takeoff visibility precedence: CAR `602.126`, live consolidation checked `2026-07-10`.
- General non-Part VII approach ban: CAR `602.129`, live consolidation checked `2026-07-10`.
- Holding timing: TC AIM `2026-1`, RAC 10.3/10.6.
- VOR checks: TC AIM `2026-1`, COM 4.5.1–4.5.2.

***
##### Current-source notes — v0.3

- Current publication cycle and 56/14-day update cadence validated against NAV CANADA.
- Trigger NOTAM logic validated against AIC `009/2026`.
- PFAF depiction timing validated against AIC `013/2026`.

### [09_ifr_knowledge_core_av_cave_v0_2.md](cheatsheets/09_ifr_knowledge_core_av_cave_v0_2.md)

##### Current-source notes — v0.2

- CAP/CFS/AIP cycle validated effective `2026-07-09` to `2026-09-03`.
- Trigger-NOTAM workflow validated against AIC `009/2026`.
- PFAF depiction transition dated from AIC `013/2026`; first implementation `2026-10-29`.

### [12_ifr_procedures_qrc_av_cave_v0_2.md](cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md)

##### Current-source notes — v0.2

- Current CAP/CFS cycle validated `2026-07-09` to `2026-09-03`.
- NOTAM + AIP SUP check added because Trigger NOTAMs may expire while SUP remains active.

### [01_flight_theory_vfr_knowledge_av_cave_v0_6.md](cheatsheets/01_flight_theory_vfr_knowledge_av_cave_v0_6.md)

##### Current-source notes — v0.6

- Cycle status and product scope checked against NAV CANADA current pages on `2026-07-10`.
- Stable legal minima remain mapped to live CARs; airport/airspace details must come from current CFS/chart/NOTAM.

### [06_aviation_formulas_conversions_av_cave_v0_2.md](cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md)

##### Validated-source notes — v0.2

- Holding timing: TC AIM `2026-1`, RAC 10.3/10.6.
- General approach ban: CAR `602.129`, live consolidation checked `2026-07-10`.
- C150M glide: provided `1977 Model 150M POH`, Figure 3-1.
- Turn-radius and glide-ratio equations: derived unit-consistent formulas; POH/chart data wins.

- Navigation: TC TP 975, Exercise 24 (September 2004 edition), checked 19 October 2026; FAA Instrument Flying Handbook Ch. 9 (2012). Intercept, lateral-distance and DME examples are derived geometry, not operational clearances.

### [11_cap_plate_reading_qrc_av_cave_v0_2.md](kb/ifr/README.md)

##### Current-source notes — v0.2

- Current CAP/eCAPGEN cycle and product limitations checked `2026-07-10`.
- Trigger NOTAM/AIP SUP workflow: AIC `009/2026`.
- Future PFAF/lightning-bolt depiction: AIC `013/2026`, implementation begins `2026-10-29`.
