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
