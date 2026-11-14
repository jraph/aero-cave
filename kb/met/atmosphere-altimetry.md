# Atmosphere, altimetry & density altitude / Atmosphère, altimétrie et altitude-densité
<!-- concept: met-atmos | level: PPL CPL IR -->

[Meteorology index / Index météo](README.md) · concept `met-atmos` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Atmosphere / ISA
<!-- id: wx-isa | from: 16 -->

- ISA SL: `15°C`, `29.92 inHg /1013.25 hPa`, density `1.225 kg/m³`.
- Standard temp lapse ≈ `2°C/1000 ft` to tropopause.
- Pressure/density decrease with altitude; warm air less dense than cold air.
- `F:` ISA temp ≈ `15 - 2×altitude(1000 ft)`.
- `T:` ISA is a reference model, not forecast weather.
***
#### Pressure altitude / density altitude
<!-- id: wx-pa-da | from: 16 -->

- Pressure altitude = altitude with altimeter `29.92`.
- Density altitude = pressure altitude corrected for non-standard temperature.
- `F rough:` `DA ≈ PA + 120 × (OAT - ISA temp)` ft.
- High `PA + temp + humidity` ⇒ DA↑ ⇒ takeoff roll↑, climb↓, TAS for same IAS↑.
- `M:` `HOT-HIGH-HUMID = PERFORMANCE LOW`.
***
#### Altimetry / pressure traps
<!-- id: wx-altimetry-traps | from: 16 | also: study-traps -->

- From high pressure→low without reset: true altitude lower than indicated.
- Warm→cold: true altitude lower than indicated.
- `M:` `HIGH→LOW / HOT→COLD = LOOK OUT BELOW`.
- Cold temperature increases obstacle/terrain error; apply published corrections where required.
***
#### Density / TAS
<!-- id: wx-density-tas | from: 16 -->

- For same IAS, TAS rises with altitude as density falls.
- Rule-of-thumb TAS ≈ `IAS + ~2% per 1000 ft` in lower atmosphere.
- Higher TAS at same IAS ⇒ larger turn radius and more ground distance during manoeuvre.
***
#### Altimetry / density altitude
<!-- id: wx-altimetry-density-altitude | from: 01 | level: PPL CPL -->

- ISA SL: `29.92 / 1013 / 15°C`; lapse≈`2°C/1000 ft`.
- High→low or warm→cold = actual lower. `M:` look out below.
- DA↑ with temperature/humidity/pressure altitude↑. Weight does NOT change DA; it independently worsens takeoff/climb. Higher DA: roll↑ climb↓; TAS↑ for the same IAS.
- `F:` PA≈elev+(29.92-altset)×1000. DA≈PA+120×(OAT-ISA). `T:` approximation only.
***
#### Pressure altitude / density altitude · card 06
<!-- id: wx-pressure-altitude-density-altitude | from: 06 | also: study-formulas | level: PPL CPL IR -->

- `F:` `PA ≈ field elev + (29.92 - altimeter) × 1000`.
- `F:` `ISA temp °C ≈ 15 - 2 × altitude(thousands ft)`.
- `F:` `DA ≈ PA + 120 × (OAT - ISA)`.
- `M:` hot/high/humid/low pressure ⇒ DA↑ ⇒ roll↑ climb↓. Heavy independently worsens performance; weight does NOT change DA.
- `T:` DA formula is approximation; POH chart wins.
***
#### Pebble
<!-- id: met-atmos-pebble | also: study-pebble -->

- ISA `15°C / 29.92 inHg / 1013.25 hPa / ≈2°C per 1000 ft to tropopause | ISA temp ≈ 15 − 2×ALT(1000 ft) | reference model ≠ forecast`
- DA `PA = altitude with 29.92 set | DA ≈ PA + 120×(OAT − ISA temp) ft | HOT-HIGH-HUMID → TKOF roll↑ climb↓ TAS↑ for same IAS`
- ALTIMETRY `HIGH→LOW / HOT→COLD = LOOK OUT BELOW (true ALT lower than indicated) | cold → apply published corrections where required`
- TAS `≈ IAS + ~2% per 1000 ft (lower atmosphere) | TAS↑ → turn radius↑`
***
