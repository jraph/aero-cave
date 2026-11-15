# Approach types, briefing & flying the approach / Types d’approche, exposé et exécution
<!-- concept: ifr-app-fly | level: IR -->

[IFR index / Index IFR](README.md) · concept `ifr-app-fly` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Approach types
<!-- id: ifr-approach-types | from: 09, 10 -->

- Precision: ILS with lateral+vertical guidance; uses `DA/DH`.
- APV: vertical guidance but not precision; e.g., `LPV`, `LNAV/VNAV`; uses `DA`.
- NPA: lateral guidance only; e.g., LOC/VOR/NDB/LNAV; uses `MDA`.
- SCDA/CDFA: stable descent technique on NPA; do not descend below MDA without visual reference.
- CAP minima box lists nav type, MDA/DA, HAA/HAT/HATh/DH, advisory visibility by aircraft category.
- `T:` LPV is not ILS. Baro-VNAV temperature limits matter; uncompensated altimetry can invalidate VNAV minima.
- Circling: visual manoeuvre; uses `MDA` / `HAA`.
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

- TYPES `precision = ILS, lateral + vertical, DA/DH | APV = LPV, LNAV/VNAV, vertical guidance but not precision, DA | NPA = LOC/VOR/NDB/LNAV, MDA | SCDA/CDFA ≠ permission below MDA | LPV ≠ ILS | uncompensated Baro-VNAV: temperature limits`
- NAVAIDS `LOC: no glideslope, LOC minima/MDA | VOR radials FROM station | ADF needle points to station, not necessarily desired track | DME slant range | DME arc: lead the turn | stepdown fix unidentified → stepdown unusable`
- FAF / MAP `“at or above” = floor, not target | after FAF workload jumps: not configured/briefed → go around or delay | timing: wind change on final, use primary MAP`
- STRAIGHT-IN `NoPT from marked point/sector | misplaced → FAF + request PT | vectors to final ≈2 NM before descent point | approach clearance = resume own nav`
***
