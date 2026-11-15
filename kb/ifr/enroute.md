# Enroute: clearances, altitudes & reports / En route : autorisations, altitudes et comptes rendus
<!-- concept: ifr-enr | level: IR -->

[IFR index / Index IFR](README.md) · concept `ifr-enr` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Clearance / readback
<!-- id: ifr-clearance-readback | from: 09, 10 | also: law-atc -->

- Clearance contents (`M:` `CRAFT-ish`): clearance limit, route, altitude, departure/restrictions, frequency, squawk/transponder, plus void/release/hold-for-release if issued.
- `P:` read back clearance limit/route/altitude/restrictions/squawk/hold-short/runway.
- `T:` clearance ≠ takeoff clearance. “climb/maintain” ≠ terrain clearance on visual/VFR restriction if you accepted separation duties.
- `T:` “cleared for the approach” authorizes IAP but not visual descent below minima; “cleared to airport” may be clearance limit, not landing clearance.
***
#### Minimum IFR altitudes / route terms
<!-- id: ifr-ifr-route-altitude-terms | from: 09, 10 -->

| Term | Memory |
|---|---|
| `MEA` | obstacle + nav reception on airway/route |
| `MOCA` | obstacle clearance; nav reception usually limited near NAVAID |
| `MRA` | min altitude to receive/use fix-defining signal |
| `AMA` | area min altitude; replaced old `GASA`; standard temp/pressure |
| `MSA` | emergency/sector altitude near facility/ARP/waypoint |
| `MVA` | ATC radar/vector altitude, normally unpublished to pilots |

- `T:` cleared direct ≠ automatically safe at low altitude; compare minimum IFR altitude / terrain / cold temp / MEA logic.
- `T:` cleared direct ≠ terrain guaranteed unless ATC/radar/MEA logic valid. cold/RASS/temp corrections can raise minima.
***
#### Altimeter-setting / standard-pressure regions
<!-- id: ifr-altimeter-setting-standard-pressure-regions | from: 10 | also: law-airspace, met-atmos -->

- Altimeter-setting region: departure set aerodrome setting/elevation; enroute nearest station along route; arrival set destination setting if available.
- Standard-pressure region: set `29.92/1013.2` except departure/arrival transition procedures.
- Climbing into standard-pressure region: set standard immediately after entering. Descending into altimeter-setting region: set appropriate station immediately before descending into region.
- `T:` flight level = standard-pressure altimeter. “high-to-low/cold = look out below” still applies.
***
#### Enroute / position reports / ATC
<!-- id: ifr-enroute-position-reports-atc | from: 10 | also: law-atc -->

- IFR position report when required: position, time, altitude, next fix/ETA, ensuing fix, remarks.
- STAR lateral path forms part of route when filed/cleared; descent clearance still needed unless specifically cleared by ATC/procedure.
- ATC speed assignment supersedes charted speed until prohibited/cancelled; charted restrictions remain unless cancelled.
- `T:` STAR vertical restrictions above assigned altitude remain mandatory unless cancelled.
***
#### Designated mountainous regions — IFR altitudes
<!-- id: ifr-designated-mountainous-regions | also: ifr-plan | level: IR -->

- Outside established minimum IFR altitudes (incl. min vectoring altitudes): **2000 ft** above highest obstacle within **5 NM** in areas **1 and 5**; **1500 ft** in areas **2, 3, 4**. [AIM RAC 2.12; CAP GEN]
- On airways / air routes: published MEA/MOCA; in winter cold, fly ≥1000 ft above MEA/MOCA. [CAP GEN; RAC 2.12]
- Cold + mountain wave → altimeter may over-read by up to **3000 ft**. [AIM AIR 1.5.6–1.5.8; CAP GEN]
- Safe Altitude 100 NM uses 1500/2000 ft clearance in mountainous regions (1000 elsewhere). [CAP GEN]
- `M:` `1-5 = 2000 · 2-3-4 = 1500 · within 5 NM`.
***
#### Position reports, reporting points, fixes
<!-- id: ifr-position-reports-fixes-rac-8 | level: IR -->

- Report contents in CFS order (CAR 602.125): ident, position, time (UTC), altitude/FL, flight plan type, next point + ETA. [AIM RAC 8.1]
- Compulsory point = **solid triangle**; "on request" point = report only if ATC asks. [RAC 8.1]
- Non-radar without DCPC: report via FIC/nearest station. Identified on radar: compulsory reports stop until told to resume. [RAC 8.1]
- Altitude reports: reaching initial cleared altitude (outside surveillance); leaving / reaching assigned altitudes; to nearest 100 ft. [RAC 8.3]
- Fix terms: **intersection** = point from radials/bearings/DME of ground aids; **waypoint** = geographic point for RNAV; **significant point** = point defining ATS route/flight path; DME fixes on an airway may allow lower MEA for DME-equipped aircraft. [CAP GEN definitions; RAC 8.6.1.1]
- `T:` radar identification removes compulsory reports, not altitude-leaving reports unless told.
***
#### 1000-ft-on-top IFR — AIM RAC 8.7
<!-- id: ifr-1000-on-top-rac-8-7 | level: IR -->

- IFR "at least 1 000-ft-on-top" only if all: [RAC 8.7]
  - ≥1000 ft above all cloud, haze, smoke or other formation;
  - flight visibility above formation ≥3 miles;
  - top of formation well defined;
  - altitude appropriate to direction of flight when cruising level;
  - ATC authorized;
  - in Class B ≤12 500 ASL, or Class C, D, E.
- `M:` `1000 · 3 SM · TOPS CLEAR · CRUISE ALT · ATC · B≤125/C/D/E`.
- `T:` still IFR (clearance, reports) — not VFR OTT.
***
#### Pebble
<!-- id: ifr-enroute-pebble -->

- CLEARANCE `limit, route, altitude, departure/restrictions, frequency, squawk + void/release/hold-for-release | clearance ≠ takeoff clearance | “cleared for the approach” ≠ descent below minima | “cleared to airport” may be a clearance limit, not landing clearance`
- ALTITUDES `MEA obstacle + nav reception | MOCA obstacle, nav limited near NAVAID | MRA receive fix-defining signal | AMA area minimum (replaced GASA), standard temp/pressure | MSA emergency/sector | MVA ATC radar, normally unpublished`
- T `cleared direct ≠ terrain guaranteed | cold/RASS/temp corrections can raise minima`
- ALTIMETER `standard-pressure region 29.92/1013.2 | climbing in: set standard immediately after entering | descending out: set station immediately before descending into altimeter-setting region | FL = standard pressure`
- STAR `lateral path part of route when filed/cleared; descent clearance still needed | vertical restrictions above assigned altitude remain unless cancelled | ATC speed supersedes charted speed`
- POSITION REPORT `position, time, altitude, next fix/ETA, ensuing fix, remarks`
- ENROUTE `mountain areas 1/5 = 2000, 2/3/4 = 1500 above obstacle within 5 NM | compulsory point = solid triangle | identified → reports stop | 1000-on-top: 1000 above, 3 SM, ATC auth, B≤12 500/C/D/E`
***
