# Approach types, briefing & flying the approach / Types d’approche, exposé et exécution
<!-- concept: ifr-app-fly | level: IR -->

[IFR index / Index IFR](README.md) · concept `ifr-app-fly` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Approach brief
<!-- id: ifr-approach-brief | from: 09 -->

- `P:` plate/eff date→airport/runway/proc→freq/nav source→MSA/RASS/cold temp→IAF/IF/FAF→altitudes/stepdowns→DA/MDA/HAT/HAA/vis→MAP→missed→runway/LDA/lights→threats.
- `M:` plate-wx-nav-alt-min-MAP-missed-rwy-threats.
- `T:` CDI source errors kill. brief both lateral/vertical mode and missed nav setup.
***
#### Approach types
<!-- id: ifr-approach-types | from: 09, 10 -->

- Precision: ILS with lateral+vertical guidance; uses `DA/DH`.
- APV: vertical guidance but not precision; e.g., `LPV`, `LNAV/VNAV`; uses `DA`.
- NPA: lateral guidance only; e.g., LOC/VOR/NDB/LNAV; uses `MDA`.
- SCDA/CDFA: stable descent technique on NPA; do not descend below MDA without visual reference.
- CAP minima box lists nav type, MDA/DA, HAA/HAT/HATh/DH, advisory visibility by aircraft category.
- `T:` LPV is not ILS. Baro-VNAV temperature limits matter; uncompensated altimetry can invalidate VNAV minima.
***
#### ILS / LOC / VOR / NDB / DME
<!-- id: ifr-ils-loc-vor-ndb-dme | from: 10 | also: nav-radio -->

- ILS: localizer lateral + glideslope vertical; identify frequency/course; beware false GS from above.
- LOC: localizer lateral only; no glideslope; use LOC minima/MDA.
- VOR: radials FROM station; set correct course; TO/FROM flag matters.
- NDB/ADF: bearing to station; wind correction/relative bearing; high workload; needle points to station, not necessarily desired track.
- DME: slant range; DME arcs require lead/radial orientation.
- `T:` reverse sensing only if display/source/course logic mishandled; know equipment.
***
#### RNAV / GNSS
<!-- id: ifr-rnav-gnss | from: 09, 10 | also: nav-gnss -->

- Verify database current, correct airport/runway/procedure/transition, RAIM/WAAS, mode/sensitivity, OBS/SUSP, missed approach sequencing.
- CDI sensitivity: enroute → terminal → approach; ensure unit arms/activates correct mode.
- Alternate planning with GNSS: verify availability/integrity and current Canadian rules; ground NAVAID fallback may be required depending equipment/approval.
- Alternate with satellite approach: verify expected RAIM/WAAS integrity at ETA; destination+alternate satellite-use separation rules may apply.
- `T:` “direct-to FAF” may delete procedure sequencing/protection. `OBS/SUSP` misuse is an INRAT classic.
- `T:` “GPS direct” ≠ cleared route unless ATC cleared.
***
#### Descent / approach math
<!-- id: ifr-descent-approach-math | from: 10 | also: study-formulas -->

- `F:` 3° path ≈ `300 ft/NM`; required ROD ≈ `GS × 5`.
- `F:` descent gradient ft/NM → `ROC/ROD fpm = GS × ft/NM / 60`.
- `F:` descent distance NM ≈ altitude to lose / `300` for 3°. `T:` add level segments, stepdowns, wind, configuration.
- `F:` time min = distance/GS×60. `T:` groundspeed, not IAS.
***
#### Pebble
<!-- id: ifr-approaches-pebble | also: study-pebble -->

- BRIEF `plate-wx-nav-alt-min-MAP-missed-rwy-threats | CDI source errors kill`
- TYPES `precision = ILS, lateral + vertical, DA/DH | APV = LPV, LNAV/VNAV, vertical guidance but not precision, DA | NPA = LOC/VOR/NDB/LNAV, MDA | SCDA/CDFA ≠ permission below MDA | LPV ≠ ILS | uncompensated Baro-VNAV: temperature limits`
- NAVAIDS `ILS: beware false GS from above | LOC: no glideslope, LOC minima/MDA | VOR radials FROM station | ADF needle points to station, not necessarily desired track | DME slant range`
- GNSS `database current, correct procedure/transition, RAIM/WAAS, mode/sensitivity enroute → terminal → approach, missed sequencing | direct-to FAF may delete sequencing/protection | OBS/SUSP misuse | “GPS direct” ≠ cleared route`
- MATH `3° ≈ 300 ft/NM | ROD ≈ GS × 5 | fpm = GS × ft/NM / 60 | groundspeed, not IAS`
***
