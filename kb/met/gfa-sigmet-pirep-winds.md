# GFA, SIGMET / AIRMET, PIREP & upper winds / GFA, SIGMET / AIRMET, PIREP et vents en altitude
<!-- concept: met-gfa | level: PPL CPL IR -->

[Meteorology index / Index météo](README.md) · concept `met-gfa` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### GFA
<!-- id: wxp-gfa | from: 05 -->

- Most probable conditions ≤`24,000 ft`; issued `4×/day` approx `2330/0530/1130/1730Z`, valid `0000/0600/1200/1800Z`.
- Six charts: C&W + icing/turb/freezing at valid/`+6 h/+12 h`; final C&W adds `12 h` IFR outlook.
- `P:` region/time→system/motion→cloud bases/tops→vis/WX/wind→icing/turb/freezing→comments/outlook; interpolate snapshots with buffer.
- Heights hundreds ft `ASL` unless `CIG/AGL`; METAR/TAF clouds AGL. `LCA≤25% | PTCHY 26–50% | XTNSV/INTMT>50%`.
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
#### Weather maps and prognostic charts — AIM MET 3
<!-- id: wx-weather-maps-prog-charts | also: ifr-wx | level: CPL IR -->

| Chart | Shows | Times |
|---|---|---|
| Surface analysis | MSL isobars (close = strong wind), H/L, fronts (blue cold, red warm, red/blue stationary, purple occluded; dashed = upper), precip / obstructions | obs 00/06/12/18Z; out 2–3 h later |
| Upper analysis `ANAL` 850 / 700 / 500 / 250 hPa | reported wind, temperature, moisture; height contours 60 m (250 hPa: 120 m); isotherms 5 °C at 850/700 only; isotachs 250 hPa only | obs 00Z, 12Z |
| Upper prog `PROG` FL240/340/390/450 | forecast wind barbs (pennant 50, feather 10, half 5 kt; true) + temperature (negative unless marked) | issued 12 h before valid; valid 00/06/12/18Z |
| SigWx prog FL100–240, FL250–630 | mid: surface H/L/fronts + motion (kt), mod/sev icing, cloud layers, mountain waves, 0 °C level; high: TS, jets ≥80 kt, mod/sev non-convective turb, tropopause | issued 12 h before valid |

- Levels ≈ 850 hPa 5 000 ft · 700 hPa 10 000 ft · 500 hPa 18 000 ft · 250 hPa 34 000 ft. 1 mb = 1 hPa. [AIM MET 3.3]
- GFA: motion arrow + speed if ≥5 kt, else `STNR`; GFA symbols = SigWx symbols. [MET 4.5, 4.11] Charts detail: [MET 10.0–12.2]
- `T:` analysis = observed (past); prog = forecast (future valid time).
***
#### Pebble
<!-- id: met-gfa-pebble -->

- GFA `most probable conditions ≤24,000 ft | issued ≈2330/0530/1130/1730Z, valid 0000/0600/1200/1800Z | six charts: C&W + icing/turb/freezing at valid / +6 h / +12 h; final C&W adds 12 h IFR outlook | heights ASL unless CIG/AGL | LCA ≤25% / PTCHY 26–50% / XTNSV/INTMT >50%`
- AIRMET / SIGMET `AIRMET = moderate ice/turb, low CIG/vis, strong wind, mountain obscuration | SIGMET = TS, severe turb/LLWS/wave/ice, TC, dust/sand, VA; expired ≠ hazard ended`
- PIREP `match time/place/level/ACFT type | jet “light” may be severe for a trainer`
- FB `true direction | level nearest route altitude, interpolate | strongest tailwind may = icing/turbulence/terrain trap`
- CHARTS `surface ANAL 00/06/12/18Z · upper ANAL 850/700/500/250 hPa at 00/12Z · PROG issued 12 h ahead · SigWx FL100–240 / 250–630`
***
