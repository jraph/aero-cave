# GNSS / RNAV
<!-- concept: nav-gnss | level: IR -->

[Index](README.md) · concept `nav-gnss` · unit IDs are stable: never rename one.

***
#### RNAV / GNSS
<!-- id: ifr-rnav-gnss | from: 09, 10 | also: ifr-app-fly -->

- Verify database current, correct airport/runway/procedure/transition, RAIM/WAAS, mode/sensitivity, OBS/SUSP, missed approach sequencing.
- CDI sensitivity: enroute → terminal → approach; ensure unit arms/activates correct mode.
- Alternate with a satellite approach: approach-level RAIM or WAAS integrity expected at ETA (predicted outages considered); TSO-C129 avionics: re-check RAIM at destination/alternate ETA during flight, at least once before mid-point; satellite approaches at both destination and alternate → aerodromes ≥ `100 NM` apart (`75 NM` in Nunavut or north of 56°N in QC/NL). Credit by minima line: see `ifr-rnav-minima-lines`. [CAP GEN, Operating minima – alternate]
- `T:` “direct-to FAF” may delete procedure sequencing/protection. `OBS/SUSP` misuse is an INRAT classic.
- `T:` “GPS direct” ≠ cleared route unless ATC cleared.
***
#### GNSS / RNAV plate traps
<!-- id: plate-gnss-rnav-plate-traps | from: 11 | also: ifr-app-fly, ifr-plates | kind: trap | level: IR -->

- Setup checks (database, procedure/transition, RAIM/WAAS, mode, CDI sensitivity, OBS/SUSP, direct-to FAF): see `ifr-rnav-gnss`. Plate-specific: approach mode must be armed/active.
- Do not use expired database for IFR approach unless explicitly permitted/verified by approved procedure and data.
- `T:` missed approach may not auto-sequence until SUSP cancelled correctly.
***
#### GNSS principles — AIM COM 5
<!-- id: nav-gnss-principles-com-5 | level: IR -->

- GNSS = worldwide position + time: satellites + aircraft receivers + integrity monitoring. [COM 5.1]
- Space: GPS design 24 satellites, 6 planes × 4. Control: USAF centre + global monitor/uplink stations. User: receiver computes position. [COM 5.2.1]
- Position: time-of-arrival → pseudoranges; **4** needed for 3-D position + clock. [COM 5.2.1]
- **RAIM** ≥5 satellites (detect); **FDE** ≥6 (exclude). [COM 5.3.1]
- **WAAS** (SBAS): ground stations → corrections + integrity via geostationary satellites; enables vertical guidance (LPV). [COM 5.3.2]
- `M:` `4 FIX · 5 DETECT · 6 EXCLUDE`.
***
#### T-routes
<!-- id: nav-t-routes-rnav | level: CPL -->

- T-route = **low-level controlled fixed RNAV route**. Protection widths, airspace and no-splay: see `nav-airways-air-routes-rac-2-7`.
- `?:` T-route equipment/GNSS requirements not read for this note: check RAC 2.7.1(c) and the CFS before flight planning.

- Sources: [TC AIM RAC](https://tc.canada.ca/sites/default/files/2026-10/aim-2026-2_rac_en.pdf) 2.7.1(c).
***
#### Pebble
<!-- id: nav-gnss-rnav-pebble -->

- RNAV `database current, correct procedure/transition, RAIM/WAAS, mode/sensitivity enroute → terminal → approach, OBS/SUSP, missed sequencing | expired database: no IFR approach unless approved | GNSS alternate: RAIM/WAAS at ETA, C129 re-check before mid-point, dest–alt ≥100 NM (75 north)`
- T `direct-to FAF may delete sequencing/protection | missed may not sequence until SUSP cancelled | “GPS direct” ≠ cleared route`
- GNSS `4 FIX · 5 DETECT (RAIM) · 6 EXCLUDE (FDE) | WAAS = SBAS corrections + integrity → LPV`
- T-ROUTE `low-level controlled fixed RNAV route | check RAC 2.7.1(c) + CFS for equipment`
***
