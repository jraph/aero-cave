# GNSS / RNAV
<!-- concept: nav-gnss | level: IR -->

[Index](README.md) · concept `nav-gnss` · unit IDs are stable: never rename one.

***
#### RNAV / GNSS
<!-- id: ifr-rnav-gnss | from: 09, 10 | also: ifr-app-fly -->

- Verify database current, correct airport/runway/procedure/transition, RAIM/WAAS, mode/sensitivity, OBS/SUSP, missed approach sequencing.
- CDI sensitivity: enroute → terminal → approach; ensure unit arms/activates correct mode.
- Alternate planning with GNSS: verify availability/integrity and current Canadian rules; ground NAVAID fallback may be required depending equipment/approval.
- Alternate with satellite approach: verify expected RAIM/WAAS integrity at ETA; destination+alternate satellite-use separation rules may apply.
- `T:` “direct-to FAF” may delete procedure sequencing/protection. `OBS/SUSP` misuse is an INRAT classic.
- `T:` “GPS direct” ≠ cleared route unless ATC cleared.
***
#### GNSS / RNAV plate traps
<!-- id: plate-gnss-rnav-plate-traps | from: 11 | also: ifr-app-fly, ifr-plates | kind: trap | level: IR -->

- Verify database current, correct airport/runway/procedure/transition, approach mode armed/active, RAIM/WAAS, CDI sensitivity, OBS/SUSP.
- Do not use expired database for IFR approach unless explicitly permitted/verified by approved procedure and data.
- `T:` `Direct-To FAF` can destroy sequencing; missed approach may not auto-sequence until SUSP cancelled correctly.
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
