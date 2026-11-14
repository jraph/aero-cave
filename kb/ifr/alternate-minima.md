# Alternate minima / Minimums de dégagement
<!-- concept: ifr-alt | level: IR -->

[IFR index / Index IFR](README.md) · concept `ifr-alt` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Alternate minima
<!-- id: ifr-alternate-minima | from: 09 -->

| Facilities | Weather requirement |
|---|---|
| 2+ usable precision, separate suitable runways | `400-1` or `+200/+1/2` above lowest usable HAT/vis, greater |
| 1 usable precision | `600-2*` or `+300/+1` above lowest HAT/vis, greater |
| NPA only | `800-2*` or `+300/+1` above lowest HAT/HAA and vis, greater |
| No IFR approach | forecast ≥`500 ft` above min IFR alt permitting VFR approach/landing |

- Standard alternate minima: `600-2` or `800-2` as applicable; if standard applies, other authorized lower-vis options may apply from CAP table.
- TAF logic: improving `BECMG` at end; deteriorating `BECMG` at start; `TEMPO` not below alternate minima; `PROB` not below landing minima.
- GFA alternate: no cloud <`1000 ft` above lowest usable HAT/HAA, no CB, vis ≥`3 mi`. Advisory forecast alternate: ≥`500 ft` above lowest usable HAT/HAA and vis ≥`3 mi`.
- `T:` alternate use depends on aircraft performance, nav equipment, NAVAIDs/NOTAM, forecast type, wind/runway, and chart “alternate not authorized.”
***
#### Alternate minima core
<!-- id: ifr-alternate-minima-core | from: 10 -->

| Facility at alternate | Weather memory |
|---|---|
| 2+ usable precision, separate suitable runways | `400-1` or `+200/+1/2` above lowest usable HAT/vis, greater |
| 1 usable precision | `600-2` or `+300/+1` above lowest HAT/vis, greater |
| NPA only | `800-2` or `+300/+1` above lowest HAT/HAA and vis, greater |
| No IFR approach | forecast ≥`500 ft` above min IFR altitude permitting VFR app/landing |

- `600-2` and `800-2` are standard alternate minima. If standard applies, other authorized minima may be available from CAP table.
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
