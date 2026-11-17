# Approach types, briefing & flying the approach / Types d’approche, exposé et exécution
<!-- concept: ifr-app-fly | level: IR -->

[IFR index / Index IFR](README.md) · concept `ifr-app-fly` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Approach types
<!-- id: ifr-approach-types | from: 09, 10 -->

| Approach | Lateral | Vertical | Class | Minimum | Height shown | Alternate row |
|---|---|---|---|---|---|---|
| `ILS` | localizer | glide path | precision | `DA` | `DH` / HAT | precision |
| `LPV` | WAAS | WAAS, approved | APV | `DA` | HAT | ✕ no credit |
| `LNAV/VNAV` | GPS or WAAS | Baro-VNAV or WAAS, approved | APV | `DA` | HAT | non-precision, baro-certified only `?` |
| `RNP AR` · chart `RNAV (RNP)` | RNP | approved | APV | `DA` | HAT | ✕ GA |
| `LOC` | localizer | — | non-precision | `MDA` | HAT | non-precision |
| `VOR` · `VOR/DME` | VOR | — | non-precision | `MDA` | HAT | non-precision |
| `NDB` · `NDB/DME` | NDB | — | non-precision | `MDA` | HAT | non-precision |
| `LNAV` (`+V` advisory) | GPS or WAAS | advisory only | non-precision | `MDA` | HAT | non-precision |
| `LP` (`+V` advisory) | WAAS | advisory only | non-precision | `MDA` | HAT | ✕ no credit |
| Circling | from the chart's non-precision part | — | visual manoeuvre | `MDA` | HAA | non-precision |

- `R:` `DA` = fly the vertical path and decide; `MDA` = level off, no descent below without the required visual reference, even on a `+V` or CDFA/SCDA path.
- RNAV detail (WAAS channel, temperature limits, RNP AR authorization, alternate conditions): see `ifr-rnav-minima-lines`. Alternate rows: see `ifr-alternate-minima`.
- CAP minima box: nav type, `DA`/`MDA`, `DH`/HAT/HATh/HAA, advisory visibility by aircraft category. [CAP GEN]
- `T:` LPV is not ILS. A `DA` does not make an approach precision.
- `R:` CAR 101.01: **precision approach** = azimuth **and glide path** information; **non-precision approach** = azimuth information; **APV** = approach procedure with vertical guidance (abbreviation only, no definition). CARs treat APV as a third category: "a non-precision approach, an APV or a CAT I or CAT II precision approach" [CAR 602.129(5), 700.10]. AC 700-023 classes LPV and LNAV/VNAV as APV, LP and LNAV as non-precision.
- `T:` the CAP GEN alternate table only has precision and non-precision rows: APV is not in it.
***
#### RNAV approach minima lines — LPV, LNAV/VNAV, LP, LNAV, +V, RNP AR
<!-- id: ifr-rnav-minima-lines | also: nav-gnss, ifr-plates, ifr-alt | level: IR -->

| Line | Lateral | Vertical | Minimum | Class | Alternate credit [CAP GEN] |
|---|---|---|---|---|---|
| `LPV` | WAAS | WAAS, approved | `DA` | APV | ✕ none |
| `LNAV/VNAV` | GPS or WAAS | Baro-VNAV or WAAS, approved | `DA` | APV | ✓ only if aircraft certified for **baro** LNAV/VNAV |
| `LP` | WAAS | none approved (advisory only) | `MDA` + stepdowns | NPA | ✕ none |
| `LNAV` | GPS or WAAS | none approved (advisory only) | `MDA` + stepdowns | NPA | ✓ |
| `LNAV+V` · `LP+V` | as LNAV · LP | **advisory** glidepath from the avionics | LNAV · LP `MDA` | NPA | as LNAV · LP |
| `RNP AR` — chart `RNAV (RNP)` | RNP | approved | `DA` | APV | ✕ GA; authorized operators: RNP 0.30 line only |

- `R:` chart title `RNAV (GNSS) RWY xx` = RNP APCH; minima lines show the extra requirement (`LPV`, `LP`, `LNAV/VNAV`). LPV or LP charted → approach summary shows `WAAS` + channel + reference path ID; otherwise `RNAV`. [CAP GEN]
- `R:` approved vertical guidance (LNAV/VNAV, LPV) → obstacle surface **sloped**, stabilized descent assumed, fly to `DA`. Advisory (LNAV, LP) → **level** surfaces: barometric altimeter governs; every stepdown and the `MDA` still apply. [AC 700-023 §4, §5.1]
- `T:` `+V` is an avionics label, not a CAP line of minima: it is LNAV or LP with advisory vertical guidance. Following the advisory path never permits descent below a stepdown or the `MDA`. [AC 700-023 §5.1; AC 606-001]
- `T:` `LP` is **not** a fail-down mode for LPV; it is published only where a vertically guided line is not possible. LPV lost → LP minima are not the fallback; apply the AFM/avionics supplement downgrade (e.g. to LNAV) or go missed. [AC 700-023 §4.4]
- `T:` LNAV/VNAV shows a temperature range: outside it, **not authorized** with uncompensated Baro-VNAV. Baro-VNAV is also not authorized with a remote altimeter setting (chart note). RNP AR carries a temperature limit too. [CAP GEN]
- `T:` RNP AR requires TC special authorization (`AUTHORIZATION REQUIRED`, AC 700-024). [CAP GEN]
- `N:` LPV, LP and WAAS-based LNAV/VNAV may carry a "fringe of WAAS coverage" note: occasional outages. Circling minima come from the non-vertically-guided (NPA) part of the chart. [CAP GEN]
- Sources: CAP GEN, Instrument approach procedures (identification, minima, operational notes) and Operating minima – alternate; [TC AC 700-023](https://tc.canada.ca/en/aviation/reference-centre/advisory-circulars/advisory-circular-ac-no-700-023) §4–5; [TC AC 606-001](https://tc.canada.ca/en/aviation/reference-centre/advisory-circulars/advisory-circular-ac-no-606-001).
***
#### ILS / LOC / VOR / NDB / DME
<!-- id: ifr-ils-loc-vor-ndb-dme | from: 10 | also: nav-radio -->

- ILS: localizer lateral + glideslope vertical; identify frequency/course; false GS from above: see `nav-ils-vortac-principles-com-4`.
- LOC: localizer lateral only; no glideslope; use LOC minima/MDA.
- VOR: radials FROM station; set correct course; TO/FROM flag matters.
- NDB/ADF: bearing to station; wind correction/relative bearing; high workload; needle points to station, not necessarily desired track.
- DME: slant range; DME arcs require lead/radial orientation.
- `T:` reverse sensing only if display/source/course logic mishandled; know equipment.
***
#### Initial / intermediate segment
<!-- id: plate-initial-intermediate-segment | from: 11 | also: ifr-plates | level: IR -->

- Identify crossing altitudes and restrictions before FAF/FAP.
- Stepdown fixes: confirm fix source and altitude. If fix cannot be identified, stepdown may be unusable.
- `T:` “at or above” altitude is a floor, not a target to duck under early.
***
#### FAF / FAP
<!-- id: plate-faf-fap | from: 11 | also: ifr-plates | level: IR -->

- FAF often Maltese-cross-like symbol on NPA; FAP for precision/APV intercept of final descent path.
- `P:` before FAF/FAP flow: see `proc-before-faf-fawp-gate`.
- `T:` after FAF, workload jumps; if not configured/briefed, go around or delay.
***
#### Profile view
<!-- id: plate-profile-view | from: 11 | also: ifr-plates | level: IR -->

- Read inbound course, crossing altitudes, stepdowns, descent angle, distance to threshold/MAP, MDA/DA relationship.
- For NPA: manage MDA, MAP, timing/DME/fix. For precision/APV: manage DA and vertical path.
- `T:` advisory descent angle/CDFA ≠ permission below MDA: see `ifr-approach-types`.
***
#### Timing
<!-- id: plate-timing | from: 11 | also: ifr-plates | level: IR -->

- Timing required if MAP based on time or as backup when published.
- `F:` time from distance and GS: see `nav-time-speed-distance`.
- `T:` wind change on final can make timing inaccurate; use primary MAP if available.
***
#### ILS / LOC traps
<!-- id: plate-ils-loc-traps | from: 11 | also: nav-radio, ifr-plates | kind: trap | level: IR -->

- Identify LOC frequency, set front course, intercept from below glidepath, verify GS alive/captured, monitor raw data.
- LOC-only minima: see `ifr-ils-loc-vor-ndb-dme`; false GS: see `nav-ils-vortac-principles-com-4`.
- `T:` back-course/reverse sensing depends equipment and procedure.
***
#### VOR / NDB / DME traps
<!-- id: plate-vor-ndb-dme-traps | from: 11 | also: nav-radio, ifr-plates | kind: trap | level: IR -->

- Radial/bearing/DME geometry: see `ifr-ils-loc-vor-ndb-dme`.
- DME arc: lead radial/turn anticipation; station passage/DME switch can confuse.
- `T:` unserviceable/unidentified navaid: see `ifr-navigation-aid-checks`.
***
#### Straight-in approaches and NoPT
<!-- id: ifr-straight-in-no-pt-rac-9-15 | level: IR -->

- Straight-in approach = positioned on final **without a procedure turn**. ATC uses the phrase in that sense. [AIM RAC 9.15]
- `NO PT` / `NoPT` on chart (usually at the IF or a TAA sector) = no PT or HILPT required from there. [RAC 9.16; CAP GEN TAA]
- Badly placed after straight-in clearance → go to FAF, request PT. FAF behind you → missed approach + new clearance. [RAC 9.16]
- Cleared straight-in on simultaneous parallels → PT not permitted. Big airports: vectors, PT never flown. [RAC 9.27, 9.7.2]
- `T:` NoPT applies from the marked point/sector only; outside it, course reversal may be required.
***
#### Radar vectors to final
<!-- id: ifr-radar-vectors-to-final-rac-9-7 | also: law-atc | level: IR -->

- Vectored to intercept final ≈ **2 NM** before final descent point. [AIM RAC 9.7.1]
- "ATS SURVEILLANCE REQUIRED" procedures: initial segment provided by vectors; may have no published initial segment. [RAC 9.7.2]
- Approach clearance while vectored to final = resume own navigation. [RAC 1.5.2]
- Comm failure while vectored: squawk `7600`; climb to published minimum altitude unless VMC. [RAC 1.5.5, 6.3.2]
- `T:` vector altitudes are ATC-temperature-corrected; no pilot cold correction on assigned vector altitudes. [CAP GEN altitude correction]
***
#### Pebble
<!-- id: ifr-approaches-pebble -->

- TYPES `precision = ILS, DA/DH | APV = LPV, LNAV/VNAV, RNP AR, DA, not precision | NPA = LOC/VOR/NDB/LNAV/LP, MDA | circling = MDA/HAA | DA ≠ precision | SCDA/CDFA ≠ permission below MDA | LPV ≠ ILS | uncompensated Baro-VNAV: temperature limits`
- RNAV LINES `LPV WAAS DA | LNAV/VNAV baro or WAAS DA | LP WAAS MDA, not LPV fail-down | LNAV MDA | +V = advisory only, MDA + stepdowns rule | RNP AR = RNAV (RNP), TC auth | alternate: LNAV ✓, baro LNAV/VNAV ✓, LPV/LP ✕`
- NAVAIDS `LOC: no glideslope, LOC minima/MDA | VOR radials FROM station | ADF needle points to station, not necessarily desired track | DME slant range | DME arc: lead the turn | stepdown fix unidentified → stepdown unusable`
- FAF / MAP `“at or above” = floor, not target | after FAF workload jumps: not configured/briefed → go around or delay | timing: wind change on final, use primary MAP`
- STRAIGHT-IN `NoPT from marked point/sector | misplaced → FAF + request PT | vectors to final ≈2 NM before descent point | approach clearance = resume own nav`
***
