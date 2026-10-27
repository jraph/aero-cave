# Content review

## Illustrative aircraft models in operating-category matrix — 26 October 2026

Added a model-examples column to all 10 PIC/SIC entries in Card 17 Markdown and bilingual HTML. Covers representative 604 private piston twin/pressurized piston/single turbine/jet/large business jet; 702 aerial-work aircraft; 703 single- and multi-engine air taxi; 704 19-seat commuter aircraft and qualifying business jet; 705 regional and airline aircraft. Examples are non-exhaustive and do not confer a regulatory subpart: actual type, certification, seats, mission, aircraft weights and air-operator approvals control. Manufacturer references added; HTML mobile layout updated and offline cache version bumped. Not browser- or device-tested.


## CAR 604 scope versus private-operator registration — 26 October 2026

Clarified both 604 rows in Card 17 Markdown and HTML: section 604.02 is a logical **OR** across four aircraft categories (large, turbine-powered, pressurized, multi-engine). Section 604.03 is a *separate* registration obligation when carrying passengers or goods in large aeroplanes, turbojets, or turbine-powered pressurized aeroplanes with more than six certificated passenger seats, subject to specified exceptions. Clarified that a small unpressurized piston twin can meet 604.02 without itself triggering 604.03 registration. Source: live CAR 604.02/604.03 (current to 2026-09-30). PWA cache bumped; mobile/browser tests not run.


## Aircraft applicability and dual-unit limits — 26 October 2026

Card 17 Markdown and bilingual HTML: added aircraft applicability to each PIC/SIC row of Table 1, with metric and regulatory pound equivalents: large aeroplane >5,700 kg (>12,566 lb); 703/704 multi-engine MCTOW ≤8,618 kg (19,000 lb); 704 turbojet MZFW ≤22,680 kg (50,000 lb); 705 aeroplane MCTOW >8,618 kg (>19,000 lb) or type certificate ≥20 pax. Distinguished 604.02 aircraft scope from 604.03 private-operator registration; noted 702 work-based applicability and applicable authorization exceptions. Verified against current online CAR 101.01, 604.02–.03, 702.01, 703.01, 704.01, 705.01 (CARs current to 2026-09-30). Existing operator/seat/PPC/CC content retained. Updated HTML mobile table layout and PWA cache version. Browser and offline device testing outstanding.


## Pilot licensing / PPC / CC / type-rating decision card — 24 October 2026

Added Card 17 as a **bilingual CAVE quick-reference** (standalone Markdown + HTML reader), referencing authoritative Card 04 rather than moving or deleting legal material. Cross-checked operative PIC/SIC distinctions against CAR 702.65, 703.88, 704.108, 705.106; check validity against 604.139, 702.67, 703.91, 704.111, 705.113; current instrument recency under 401.05; type requirements in Standard 421.40; licence headline hours in TC AIM 2026-2. Live CARs consolidation noted current to 2026-09-30 (last amended 2026-06-17). Exam summary deliberately excludes complete Ops Specs, Part IV aircraft-specific limits and alternate programs. Added index, README, manifest shortcut, PWA cache entry/version and offline cache-test path. Browser/device rendering not independently verified.

## CPAER Phase 2 content audit — 22 October 2026

Added [CPAER coverage matrix](CPAER_COVERAGE_MATRIX.md), based on repository commit `3dbd013ba1e93160727d40b6fde8f4a0e50ca0f4` and official TC TP 12881 seventh edition, August 2026 (HTML/PDF edition verified). Topic-group screening across the syllabus; individual rows for 52 Flight Instruments and 40 Human Factors items. Active Markdown evidence inspected, including all 14 numbered cards and supplementary bilingual recall/glossary content. Not a fresh regulatory/medical/POH validation or an exam-completeness claim.

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

### [11_cap_plate_reading_qrc_av_cave_v0_2.md](cheatsheets/11_cap_plate_reading_qrc_av_cave_v0_2.md)

##### Current-source notes — v0.2

- Current CAP/eCAPGEN cycle and product limitations checked `2026-07-10`.
- Trigger NOTAM/AIP SUP workflow: AIC `009/2026`.
- Future PFAF/lightning-bolt depiction: AIC `013/2026`, implementation begins `2026-10-29`.
