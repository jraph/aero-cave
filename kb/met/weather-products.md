# Weather products & decoding / Produits météo et décodage
<!-- concept: met-products | level: PPL CPL IR -->

[Meteorology index / Index météo](README.md) · concept `met-products` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Canadian product memory
<!-- id: wx-products | from: 16 -->

- `METAR/SPECI` observed aerodrome conditions.
- `TAF` terminal forecast.
- `GFA` regional cloud/weather + icing/turb/freezing level.
- `AIRMET` significant lower-severity/unforecast hazard.
- `SIGMET` significant hazardous weather.
- `PIREP` actual pilot-observed conditions.
- METAR/TAF cloud heights = AGL; GFA heights generally ASL unless stated.
- `T:` use the separate Weather Decoding / Go-No-Go QRC for exact code/timing/alternate logic.
***
#### Product roles
<!-- id: wxp-product-roles | from: 05 -->

| Product | Tells you |
|---|---|
| `METAR` | observed aerodrome weather now |
| `SPECI` | significant observed change |
| `TAF` | forecast aerodrome conditions/time changes |
| `GFA` | regional clouds/weather + icing/turb/freezing level |
| `AIRMET` | potentially hazardous weather / significant change below SIGMET severity |
| `SIGMET` | significant hazardous weather affecting flight safety |
| `PIREP` | actual conditions encountered |
| `FB/upper winds` | forecast wind/temp aloft |
| `Radar` | precipitation location/intensity/trend; not all turbulence/ice |
| `Satellite` | cloud structure/coverage; interpretation required |
| `RSC/CRFI` | runway contamination/condition/friction information |

- `T:` radar gap ≠ clear air. no PIREPs ≠ no hazard.
***
#### Weather trend logic
<!-- id: wx-trend | from: 16 | also: met-decide -->

- Observation = **now**; forecast = **expected**; trend = whether expectation is occurring.
- Compare several METAR/SPECI, not one snapshot.
- Falling ceiling/vis + pressure + increasing wind/precip often signals approaching system deterioration.
- `T:` forecast confidence drops when observations repeatedly diverge.
***
