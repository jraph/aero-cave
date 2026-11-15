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
- `F:` `PA ≈ field elev + (29.92 - altimeter setting) × 1000` ft.
- Density altitude = pressure altitude corrected for non-standard temperature.
- `F rough:` `DA ≈ PA + 120 × (OAT - ISA temp)` ft; ISA temp: `wx-isa`.
- High `PA` (incl. low pressure) `+ temp + humidity` ⇒ DA↑ ⇒ takeoff roll↑, climb↓, TAS for same IAS↑.
- `T:` weight does NOT change DA; heavy independently worsens takeoff/climb.
- `T:` formulas are approximations; POH performance chart wins.
- `M:` `HOT-HIGH-HUMID = PERFORMANCE LOW`.
***
#### Altimetry / pressure traps
<!-- id: wx-altimetry-traps | from: 16 | kind: trap -->

- From high pressure→low without reset: true altitude lower than indicated.
- Warm→cold: true altitude lower than indicated.
- `M:` `HIGH→LOW / HOT→COLD = LOOK OUT BELOW`.
- Cold temperature increases obstacle/terrain error; apply published corrections where required → `wx-cold-temperature-altitude-error`, `plate-cold-temperature`.
***
#### Density / TAS
<!-- id: wx-density-tas | from: 16 -->

- For same IAS, TAS rises with altitude as density falls.
- Rule-of-thumb TAS ≈ `IAS + ~2% per 1000 ft` in lower atmosphere.
- Higher TAS at same IAS ⇒ larger turn radius and more ground distance during manoeuvre.
***
#### Pebble
<!-- id: met-atmos-pebble -->

- ISA `15°C / 29.92 inHg / 1013.25 hPa / ≈2°C per 1000 ft to tropopause | ISA temp ≈ 15 − 2×ALT(1000 ft) | reference model ≠ forecast`
- DA `PA = altitude with 29.92 set ≈ elev + (29.92 − setting)×1000 | DA ≈ PA + 120×(OAT − ISA temp) ft | HOT-HIGH-HUMID → TKOF roll↑ climb↓ TAS↑ for same IAS | weight ≠ DA | POH chart wins`
- ALTIMETRY `HIGH→LOW / HOT→COLD = LOOK OUT BELOW (true ALT lower than indicated) | cold → apply published corrections where required`
- TAS `≈ IAS + ~2% per 1000 ft (lower atmosphere) | TAS↑ → turn radius↑`
***
