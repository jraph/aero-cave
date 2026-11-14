# Holding / Attente
<!-- concept: ifr-hold | level: IR -->

[IFR index / Index IFR](README.md) · concept `ifr-hold` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Holding
<!-- id: ifr-holding | from: 09, 10 -->

- Clearance: fix, direction, radial/course/bearing/airway, leg length/time, altitude, EFC.
- Standard = right turns; non-standard = left. Published max speed inside hold wins.
- Entries: direct / teardrop / parallel. `T:` entry is a method; protected airspace matters.
- Timing: standard outbound leg `1 min` at/below `14,000 ft ASL`; `1.5 min` above. Adjust outbound to achieve the corresponding inbound time; DME holds use specified distances. `[AIM 2026-1 RAC 10.3/10.6]`
- Wind: outbound correction about `3×` inbound drift. `T:` EFC and fuel are exam-critical.
- `T:` no EFC? ask. fuel clock starts early.
***
#### Holding · card 06
<!-- id: ifr-holding-c06 | from: 06 | also: study-formulas | level: IR -->

- `F:` outbound timing adjusted to make inbound leg time.
- `R:` standard hold: outbound `1 min` at/below `14,000 ft ASL`; `1.5 min` above `14,000 ft ASL`. For DME holding, ATC/published procedure specifies distance instead of time. `[AIM 2026-1 RAC 10.3/10.6]`
- `M:` outbound wind correction ≈ `3×` inbound drift.
- `F:` DME leg time = leg distance / GS × 60.
- `T:` hold speed limits/published leg distances override memory.
***
#### Pebble
<!-- id: ifr-holding-pebble | also: study-pebble -->

- HOLD `clearance: fix, direction, radial/course/bearing/airway, leg length/time, altitude, EFC | standard = right turns | published max speed wins | entries direct/teardrop/parallel`
- TIMING `outbound 1 min at/below 14,000 ft ASL; 1.5 min above; adjust outbound to achieve inbound time | DME holds: specified distances | outbound wind correction ≈ 3× inbound drift`
- T `no EFC? ask | fuel clock starts early | protected airspace matters more than entry drawing`
***
