# Enroute: clearances, altitudes & reports / En route : autorisations, altitudes et comptes rendus
<!-- concept: ifr-enr | level: IR -->

[IFR index / Index IFR](README.md) · concept `ifr-enr` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Clearance / readback
<!-- id: ifr-clearance-readback | from: 09 | also: law-atc -->

- Clearance memory: `CRAFT-ish` = clearance limit, route, altitude, frequency, transponder, plus void/release/hold-for-release if issued.
- `T:` clearance ≠ takeoff clearance. “climb/maintain” ≠ terrain clearance on visual/VFR restriction if you accepted separation duties.
***
#### Clearance / readback · INRAT
<!-- id: ifr-clearance-readback-inrat | from: 10 | also: law-atc -->

- Clearance contents: clearance limit, route, altitude, departure/restrictions, frequency, squawk, void/release/hold-for-release if issued.
- `P:` read back clearance limit/route/altitude/restrictions/squawk/hold-short/runway.
- `T:` “cleared for the approach” authorizes IAP but not visual descent below minima; “cleared to airport” may be clearance limit, not landing clearance.
***
#### Minimum altitudes / terrain
<!-- id: ifr-minimum-altitudes-terrain | from: 09 -->

- MEA = nav+obstacle; MOCA = obstacle + limited nav; MSA = emergency/sector; MVA not published to pilots.
- `T:` cleared direct ≠ terrain guaranteed unless ATC/radar/MEA logic valid. cold/RASS/temp corrections can raise minima.
***
#### IFR route / altitude terms
<!-- id: ifr-ifr-route-altitude-terms | from: 10 -->

| Term | Memory |
|---|---|
| `MEA` | obstacle + nav reception on airway/route |
| `MOCA` | obstacle clearance; nav reception usually limited near NAVAID |
| `MRA` | min altitude to receive/use fix-defining signal |
| `AMA` | area min altitude; replaced old `GASA`; standard temp/pressure |
| `MSA` | emergency/sector altitude near facility/ARP/waypoint |
| `MVA` | ATC radar/vector altitude, normally unpublished to pilots |

- `T:` cleared direct ≠ automatically safe at low altitude; compare minimum IFR altitude / terrain / cold temp / MEA logic.
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
