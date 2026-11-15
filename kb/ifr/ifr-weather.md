# IFR weather / Météo IFR
<!-- concept: ifr-wx | level: IR -->

[IFR index / Index IFR](README.md) · concept `ifr-wx` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Weather decoding — exam workflow
<!-- id: ifr-weather-decoding-exam-workflow | from: 10 | also: met-products -->

- METAR/SPECI: wind, vis, wx, cloud, temp/dew, altimeter, remarks; RVR if vis ≤`1 SM` and/or RVR ≤`6000 ft`.
- TAF: validity, FM, BECMG, TEMPO, PROB, wind/vis/wx/cloud. Ceiling = lowest BKN/OVC/VV.
- FD: interpolate wind/temp aloft; choose true altitude/level; use winds for GS/fuel/temp/icing.
- GFA: clouds/wx + icing/turb/freezing level; use time panels and expected movement.
- `T:` TAF legal but GFA/SIGMET/PIREPs ugly = operational no-go even if exam legal answer exists.
***
#### IFR weather traps
<!-- id: ifr-ifr-weather-traps | from: 10 | kind: trap -->

- Freezing level + cloud/precip = icing risk. Carb ice can exist above freezing in humid partial power.
- Warm front: layered cloud/low vis/steady precip/freezing rain risk. Cold front: convective showers/TS/gusts/wind shear.
- TS/CB: avoid; embedded CB in IMC is no-go for light trainer.
- Low-level wind shear/microburst: go-around may not save you if severe; avoid.
- `T:` altimetry errors from cold temps affect obstacle clearance, not just indicated altitude comfort.
***
#### Pebble
<!-- id: ifr-ifr-weather-pebble -->

- DECODE `METAR: RVR if vis ≤1 SM and/or RVR ≤6000 ft | ceiling = lowest BKN/OVC/VV | FD: interpolate wind/temp aloft | GFA: time panels and expected movement`
- T `TAF legal but GFA/SIGMET/PIREP ugly = operational no-go | freezing level + cloud/precip = icing risk | embedded CB in IMC = no-go for light trainer | cold-temp altimetry errors affect obstacle clearance`
***
