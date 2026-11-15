# Weather products & decoding / Produits météo et décodage
<!-- concept: met-products | level: PPL CPL IR -->

[Meteorology index / Index météo](README.md) · concept `met-products` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Product roles
<!-- id: wx-products | from: 16, 05 -->

| Product | Tells you |
|---|---|
| `METAR` | observed aerodrome weather now |
| `SPECI` | significant observed change |
| `TAF` | forecast aerodrome conditions/time changes |
| `GFA` | regional clouds/weather + icing/turb/freezing level |
| `AIRMET` | potentially hazardous weather / significant change below SIGMET severity (lower-severity/unforecast hazard) |
| `SIGMET` | significant hazardous weather affecting flight safety |
| `PIREP` | actual conditions encountered |
| `FB/upper winds` | forecast wind/temp aloft |
| `Radar` | precipitation location/intensity/trend; not all turbulence/ice |
| `Satellite` | cloud structure/coverage; interpretation required |
| `RSC/CRFI` | runway contamination/condition/friction information |

- `T:` radar gap ≠ clear air. no PIREPs ≠ no hazard.
- METAR/TAF cloud heights = AGL; GFA heights generally ASL unless stated.
***
#### Weather trend logic
<!-- id: wx-trend | from: 16 | also: met-decide -->

- Observation = **now**; forecast = **expected**; trend = whether expectation is occurring.
- Compare several METAR/SPECI, not one snapshot.
- Falling ceiling/vis + pressure + increasing wind/precip often signals approaching system deterioration.
- `T:` forecast confidence drops when observations repeatedly diverge.
***
#### Pebble
<!-- id: met-products-pebble -->

- PRODUCTS `METAR now | SPECI significant change | TAF aerodrome forecast | GFA regional + icing/turb/freezing level | AIRMET below SIGMET severity | SIGMET hazardous | PIREP actual | FB wind/temp aloft`
- HEIGHTS `METAR/TAF cloud = AGL | GFA generally ASL unless stated`
- T `radar gap ≠ clear air | no PIREPs ≠ no hazard | observation = now / forecast = expected / trend = is the forecast happening | repeated divergence → confidence↓`
***
