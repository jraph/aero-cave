# GFA, SIGMET / AIRMET, PIREP & upper winds / GFA, SIGMET / AIRMET, PIREP et vents en altitude
<!-- concept: met-gfa | level: PPL CPL IR -->

[Meteorology index / Index météo](README.md) · concept `met-gfa` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### GFA
<!-- id: wxp-gfa | from: 05 -->

- Most probable conditions ≤`24,000 ft`; issued `4×/day` approx `2330/0530/1130/1730Z`, valid `0000/0600/1200/1800Z`.
- Six charts: C&W + icing/turb/freezing at valid/`+6 h/+12 h`; final C&W adds `12 h` IFR outlook.
- `P:` region/time→system/motion→cloud bases/tops→vis/WX/wind→icing/turb/freezing→comments/outlook; interpolate snapshots with buffer.
- Heights hundreds ft `ASL` unless `CIG/AGL`; METAR/TAF clouds AGL. `LCA≤25% | PTCHY 26–50% | XTNSV/INTMT>50%`; `P6SM`=>6 SM.
- Movement/`6 h`: `5 kt≈30 NM`, `10 kt≈60 NM`, `20 kt≈120 NM`. `T:` local/patchy hazard may sit on route.
***
#### AIRMET / SIGMET / PIREP
<!-- id: wxp-airmet-sigmet-pirep | from: 05 -->

| Product | Use / trap |
|---|---|
| `AIRMET` | moderate ice/turb, low CIG/vis, strong wind, mountain obscuration/significant change; may exceed light-GA capability |
| `SIGMET` | TS, severe turb/LLWS/wave/ice, TC, dust/sand, VA/radioactive cloud; avoid; expired≠hazard ended |
| `PIREP` | actual `/OV /TM /FL /TP /SK /TA /WV /TB /IC /RM`; match time/place/level/type; jet “light” may be severe operationally for trainer |

- `P:` plot phenomenon/area/time/levels/movement/change; compare route/ETA and updates. UUA includes severe/extreme turb, severe ice, LLWS, tornado/funnel/waterspout, VA or other safety-critical condition.
***
#### Upper winds / temperature
<!-- id: wxp-upper-winds | from: 05 -->

- Use forecast level nearest route altitude; interpolate if needed. Wind is true direction/speed; temperature °C, omitted at low levels in some coding conventions.
- `P:` compute WCA/GS/fuel→compare freezing level/temp→select altitude balancing wind, terrain, cloud, icing, oxygen/performance.
- `T:` strongest tailwind route may place you in icing/turbulence/terrain trap.
***
