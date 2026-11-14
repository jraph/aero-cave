# Alternate minima / Minimums de dégagement
<!-- concept: ifr-alt | level: IR -->

[IFR index / Index IFR](README.md) · concept `ifr-alt` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Alternate minima
<!-- id: ifr-alternate-minima | from: 09, 10 -->

| Facilities | Weather requirement |
|---|---|
| 2+ usable precision, separate suitable runways | `400-1` or `+200/+1/2` above lowest usable HAT/vis, greater |
| 1 usable precision | `600-2*` or `+300/+1` above lowest HAT/vis, greater |
| NPA only | `800-2*` or `+300/+1` above lowest HAT/HAA and vis, greater |
| No IFR approach | forecast ≥`500 ft` above min IFR alt permitting VFR approach/landing |

- Standard alternate minima: `600-2` or `800-2` as applicable; if standard applies, other authorized lower-vis options may apply from CAP table.
- `T:` alternate use depends on aircraft performance, nav equipment, NAVAIDs/NOTAM, forecast type, wind/runway, and chart “alternate not authorized.”
- `T:` “alternate not authorized” / NOTAM NAVAID out / runway not suitable / no forecast can kill an otherwise good alternate.
***
#### TAF alternate logic
<!-- id: ifr-taf-alternate-logic | from: 10 | also: met-taf, ifr-wx -->

- Improving `BECMG`: use new condition at END of BECMG period.
- Deteriorating `BECMG`: use new condition at START of BECMG period.
- `TEMPO` must not be below alternate minima.
- `PROB` must not be below appropriate landing minima.
- GFA alternate: no cloud <`1000 ft` above lowest usable HAT/HAA; no CB; vis ≥`3 SM`.
- Aerodrome advisory forecast alternate: ≥`500 ft` above lowest usable HAT/HAA and vis ≥`3 SM`.
- `T:` alternate minima ≠ landing minima ≠ approach-ban minima.
***
#### Alternate minima memory
<!-- id: ifr-alternate-minima-memory | from: 06 | also: study-formulas | level: IR -->

| Case | Weather memory |
|---|---|
| 2+ precision, separate suitable runways | `400-1` or `+200/+1/2`, greater |
| 1 precision | `600-2` or `+300/+1`, greater |
| NPA only | `800-2` or `+300/+1`, greater |
| no IFR approach | ≥`500 ft` above min IFR alt allowing VFR app/landing |

- `T:` check CAP alternate notes, NOTAM, NAVAID, runway suitability, forecast type.
***
#### Pebble
<!-- id: ifr-alternate-minima-pebble | also: study-pebble -->

- ALTERNATE `2+ usable precision, separate suitable RWYs: 400-1 or +200/+½ | 1 precision: 600-2 or +300/+1 | NPA only: 800-2 or +300/+1 | each = above lowest usable HAT (HAA for NPA)/vis, whichever greater | no IFR approach: forecast ≥500 ft above min IFR altitude permitting VFR approach/landing`
- TAF `BECMG improve = END / deteriorate = START | TEMPO ≥ alternate minima | PROB ≥ landing minima`
- GFA / ADVISORY `GFA: no cloud <1000 ft above lowest usable HAT/HAA, no CB, vis ≥3 SM | advisory forecast: ≥500 ft above lowest usable HAT/HAA, vis ≥3 SM`
- T `alternate minima ≠ landing minima ≠ approach-ban minima | “alternate not authorized” / NAVAID NOTAM / RWY not suitable / no forecast kills an alternate`
***
