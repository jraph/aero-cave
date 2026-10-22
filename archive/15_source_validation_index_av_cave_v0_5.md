### SOURCE VALIDATION INDEX — AV-CAVE v0.5
`HISTORICAL JULY 2026 DOCUMENT` | September corrections and review scope: `00_CPAER_REVIEW_NOTES.md`. This document does not establish current validity.
`VALIDATED` current authoritative source checked | `PROVISIONAL` sound study content, line audit incomplete | `STALE` source expired/outdated | `AIRCRAFT` exact POH/AFM/SOP required | `FIX` known correction required
`RELEASE:` `AUDIT-REF` | `CANONICAL SOURCE:` `source_validation_index_av_cave_v0_5.md` | `NOT FLIGHT AUTHORITY`
`Audit date:` `2026-07-10` | `Use:` study-development control document; not an operational publication
***
#### Authority hierarchy

| Level | Source | Use |
|---:|---|---|
| `A1` | current CARs / incorporated Standards / exemptions in force | legal requirement |
| `A2` | current AIP Canada / CAP / CFS / NOTAM / AIP SUP-AIC | current operational data/procedure |
| `B` | exact aircraft POH/AFM + supplements + placards + approved checklist | aircraft limitations/procedures/performance |
| `C` | current TC AIM / TC advisory material / flight-test guides | authoritative guidance, not law |
| `D` | TC Flight Training Manual / instructor technique / school SOP | training method; SOP may be locally controlling |
| `E` | derived formula, mnemonic, mental approximation | memory aid only; verify before operational use |

- `R:` higher authority wins. Current data wins over expired copies. Exact-aircraft data wins over generic technique.
- `T:` AIM/FTM/TP guide wording must not be presented as regulation unless mapped to the CAR/Standard.
***
#### Current authoritative baseline

| Source | Status on audit date | Pack treatment |
|---|---|---|
| Justice Laws `SOR/96-433` | live consolidation observed current to `2026-05-26`; last amended `2026-01-05` | use live sections for every legal claim |
| TC Standard 421 | official page updated `2026-01-07` | primary licensing source |
| TC AIM `2026-1` | effective `2026-03-19` to `2026-10-01` | current guidance source |
| CAP/CAP GEN | current cycle effective `2026-07-09` to `2026-09-03` | required for IFR minima/procedure validation |
| CFS | current cycle effective `2026-07-09` to `2026-09-03` | required for airspace/aerodrome/planning validation |
| AIP Canada | current issue effective `2026-07-09` to `2026-09-03` | current state aeronautical source |
| NOTAM/AIP SUP/AIC | live/current at time of use | always required for operational release |
***
#### Local source inventory

| Local/reference file | Effective/current status | Classification | Action |
|---|---|---|---|
| `aim-2026-1_access_en.pdf` | current to `2026-10-01` | `C VALIDATED` | retain; cite section/page |
| `CAP_GEN_03-19-2026.pdf` | expired `2026-05-14` | `A2 STALE` | reference/layout only; replace with `2026-07-09` CAP GEN |
| `CFSGENERAL_06-12-2025.pdf` | expired `2025-08-07` | `A2 STALE` | reference only; replace current CFS |
| `CFSPLANNING-UPDATING-RESTRICTIONS_06-12-2025.pdf` | expired `2025-08-07` | `A2 STALE` | revalidate all copied minima/codes/procedures |
| `SOR-96-433.pdf` | current only to `2024-11-26` | `A1 STALE` | never use as final legal authority |
| `Flight Training Manual - 4th edition...2004.pdf` | 2004; explicitly guidance | `D PROVISIONAL` | use for principles/technique, not law/current procedure |
| `CESSNA_150_POH.pdf` in File Library | 1977 `Model 150M`; exact model source | `B AIRCRAFT` | verify serial/configuration/change status/supplements before operational release |

- `T:` the 150M POH itself states the handbook must be kept current and should not be used operationally until update status is confirmed.
***
#### Release labels

| Label | Meaning |
|---|---|
| `STUDY` | useful for learning; may include approximation/generic technique |
| `EXAM` | validated against current exam guide/source, but not necessarily operational |
| `OPS-REF` | current procedural source mapped; still requires current NOTAM/aircraft data |
| `AIRCRAFT-REF` | exact model/configuration/POH verified |
| `FLIGHT-READY` | legal/current/aircraft/NOTAM dependencies checked for intended operation |

- Current package overall: `STUDY / PROVISIONAL`; not yet `FLIGHT-READY`.
***
#### File audit matrix

| File | Current status | Primary dependencies | Required work |
|---|---|---|---|
| `flight_training_procedures_av_cave_v0_2.md` | `PROVISIONAL / AIRCRAFT` | FTM + POH + SOP | map each procedure to C150M POH/SOP; separate generic from aircraft action |
| `c150m_speed_patch_av_cave_v0_2.md` | `SUPERSEDED-STUDY` | 1977 C150M POH | retained for history; use full POH core instead |
| `c150m_poh_core_av_cave_v0_1.md` | `AIRCRAFT-REF PROVISIONAL` | provided 1977 C150M POH | model-level audit completed; confirm exact serial/configuration/change status/supplements before flight |
| `flight_theory_vfr_knowledge_av_cave_v0_6.md` | `LEGAL/CYCLE-REF PROVISIONAL` | live CARs + AIM 2026-1 + current CFS cycle | cycle/source workflow updated; route-specific data still requires current briefing |
| `canadian_air_law_core_av_cave_v0_1.md` | `LEGAL-REF PROVISIONAL` | live CARs current to 2026-05-26 + Standard 421 | core sections mapped; future amendment/regression audit required before flight use |
| `licensing_performance_operations_av_cave_v0_2.md` | `EXAM-PROVISIONAL` | Standard 421.30 + CPL test guide | licensing values mostly sourced; label flight-test stabilization criteria as guide only |
| `ifr_knowledge_core_av_cave_v0_2.md` | `CYCLE-REF PROVISIONAL` | CARs + AIM 2026-1 + current CAP cycle/AICs | cycle/Trigger/PFAF transition updated; full line audit still required |
| `inrat_knowledge_core_av_cave_v0_3.md` | `EXAM/CYCLE-REF PROVISIONAL` | TP 691E + CARs + AIM 2026-1 + current cycle/AICs | current publication workflow updated; broader line audit still required |
| `aviation_formulas_conversions_av_cave_v0_2.md` | `PROVISIONAL-CORRECTED` | derived math + AIM 2026-1 + CAR 602.129 + C150M POH | known turn/glide errors repaired; flagged hold/RVR items resolved |
| `multi_engine_knowledge_core_av_cave_v0_1.md` | `EXAM / AIRCRAFT` | Standard 421.38 + TP 219E + twin POH | generic theory usable; no operational speeds/procedures without exact twin POH |
| `cap_plate_reading_qrc_av_cave_v0_2.md` | `OPS/CYCLE-REF PROVISIONAL` | current CAP/eCAPGEN cycle + AIC 009/013 | cycle/Trigger/future PFAF transition validated; specific plate still requires live check |
| `ifr_procedures_qrc_av_cave_v0_2.md` | `CYCLE-REF PROVISIONAL / AIRCRAFT` | AIM/CAP current cycle + IR guide + POH/SOP | publication workflow updated; aircraft/SOP and broader procedure audit remain |
| `weather_decoding_go_nogo_qrc_av_cave_v0_1.md` | `PROVISIONAL` | AIM 2026-1 MET + CAP/CAR | product decoding strong; revalidate alternate legality and exact legal thresholds |
| `aircraft_systems_failures_qrc_av_cave_v0_1.md` | `STUDY / AIRCRAFT` | FTM + exact POH/checklist | keep symptom logic; remove any implied universal emergency sequence |
***
#### Known corrections — immediate

| File/item | Problem | Corrective action |
|---|---|---|
| formulas: turn radius | `RESOLVED v0.2` | `radius ft=TAS²/(11.26×tan bank)`; NM conversion added |
| formulas: glide distance | `RESOLVED v0.2` | exact ratio formula + C150M POH Fig. 3-1 memory value |
| formulas/INRAT: hold timing | `RESOLVED v0.2` | AIM 2026-1 RAC 10.3/10.6 |
| formulas/INRAT: GA RVR memory | `RESOLVED v0.2` | live CAR 602.129 |
| INRAT: takeoff visibility logic | `RESOLVED v0.2` | live CAR 602.126 |
| INRAT: VOR tolerances | `RESOLVED v0.2` | AIM 2026-1 COM 4.5.1–4.5.2 |
| C150M speed patch | mixed `KIAS/CAS` risk | preserve exact POH units per table; do not normalize silently |
| IFR/CPL stable gates | different values appear | label context: CPL VFR test vs IFR test/SOP; never merge |
***
#### High-risk content classes

- `LEGAL:` fuel, minima, approach ban, takeoff visibility, licences, recency, equipment, flight plan/itinerary.
- `CURRENT DATA:` CAP/CFS/AIP/NOTAM, runway/lighting/NAVAID, airspace, procedures.
- `AIRCRAFT:` speeds, memory items, flap/gear/prop/electrical/fuel actions, W&B/performance.
- `CALCULATION:` formula constants, units, chart interpolation, gradient/turn/glide calculations.
- `T:` no high-risk line may be promoted to `FLIGHT-READY` without source + effective date + exact condition/exception.
***
#### Citation schema for future files

- Regulatory: `[CAR 602.xxx | live checked YYYY-MM-DD]`.
- Standard: `[STD 421.xx | page updated YYYY-MM-DD]`.
- AIM: `[AIM 2026-1 RAC/MET/AIR §x.x]`.
- Operational: `[CAP GEN cycle YYYY-MM-DD]`, `[CFS cycle YYYY-MM-DD]`, `[NOTAM checked YYYY-MM-DD HHMMZ]`.
- Aircraft: `[C150M POH 1977 §x p.x-x | supplement/config checked]`.
- Training: `[FTM 4e 2004 ch.x]`, `[TP xxxx guide]`.
- Derived: `[DERIVED]` plus equation/assumptions.
***
#### Validation workflow

- `1 INVENTORY:` identify every factual line and source class.
- `2 AUTHORITY:` legal/current/aircraft/guidance/derived.
- `3 CONDITION:` retain applicability, exceptions, units and category.
- `4 FRESHNESS:` record effective/current date.
- `5 CROSS-CHECK:` second source for high-risk items where practical.
- `6 CORRECT:` update source file; increment version.
- `7 RELEASE:` assign `STUDY/EXAM/OPS-REF/AIRCRAFT-REF/FLIGHT-READY`.
- `8 REGRESSION:` search old value across all files after each correction.
***
#### Planned sequence

- `Step 1:` source-validation index — completed in this file.
- `Step 2:` repair known formula errors and flagged verification items — completed in `v0.2` formula/INRAT files.
- `Step 3:` build full `C150M POH CORE` from the provided 1977 Model 150M POH, with configuration caveats — completed.
- `Step 4:` build `CANADIAN AIR LAW CORE` against live CARs/Standards — completed.
- `Step 5:` update CAP/CFS-dependent files using current `2026-07-09` cycle — completed.
- `Step 6:` final cross-file consistency audit and release labels.
***
#### Current release statement

- The package is a strong condensed study system.
- It is not yet an independent legal or operational authority.
- Before flight: use current CARs/Standards, AIM, CAP/CFS/AIP/NOTAM and the exact aircraft POH/AFM/SOP.
- `M:` `MEMORY SHEET HELPS RECALL; PRIMARY SOURCE AUTHORIZES ACTION`.

***
#### Step 2 completion record

- Corrected turn-radius units/formula.
- Corrected glide-ratio distance formula and replaced generic trainer estimate with C150M POH Figure 3-1 value.
- Validated standard hold timing.
- Validated non-Part VII general approach-ban RVR thresholds and exceptions.
- Validated takeoff-visibility source precedence.
- Validated Canadian VOR receiver comparison and airborne-check tolerances.

***
#### Step 3 completion record

- Created `c150m_poh_core_av_cave_v0_1.md` from the provided 1977 Model 150M POH.
- Preserved exact `KIAS/KCAS` distinctions where stated.
- Covered limitations, normal/emergency procedures, systems, W&B and performance assumptions.
- Release remains `AIRCRAFT-REF PROVISIONAL` until the exact aircraft serial, revision status, supplements, placards, STCs and current W&B are verified.

***
#### Step 4 completion record

- Created `canadian_air_law_core_av_cave_v0_1.md` against the live Justice Laws CAR consolidation current to `2026-05-26`.
- Covered pilot responsibility, privileges, medical/recency, documents/equipment, fuel/oxygen, flight planning, right-of-way, minimum altitudes, aerodrome operations and VFR minima.
- Commercial pilot privilege was separated from operator/AOC authority.
- Release remains `LEGAL-REF PROVISIONAL`; check future amendments, exemptions, current Standards and operation-specific Parts before use.

***
#### Step 5 completion record

- Validated current NAV CANADA 56-day cycle: `2026-07-09` to `2026-09-03`.
- Added current publication→NOTAM→AIP SUP/AIC workflow to VFR/IFR/INRAT/QRC files.
- Added AIC `009/2026` Trigger-NOTAM limitation: pointer only; underlying SUP may remain active.
- Added AIC `013/2026` future PFAF depiction warning: incremental start `2026-10-29`, not current July-cycle convention.
- Created `nav_canada_cycle_update_2026-07-09.md` as the audit trace.
