# METAR / SPECI
<!-- concept: met-metar | level: PPL CPL IR -->

[Meteorology index / Index météo](README.md) · concept `met-metar` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### METAR / SPECI scan
<!-- id: wxp-metar | from: 05 -->

- `P:` type→ID→time→wind→vis/RVR→WX→cloud→T/TD→ALT→RMK. `M:` `ID-TIME-WIND-VIS-WX-CLOUD-T/TD-ALT-RMK`.
- Cloud heights: hundreds ft AGL; ceiling=lowest `BKN/OVC/VV`; `SCT`≠ceiling.
- `SPECI:` significant change; compare last `2–4` reports for ceiling/vis/wind/pressure/precip/convection.
- `T:` `AUTO` limits and remarks matter; recent SPECI can override comfort from older data.
***
#### Wind decoding
<!-- id: wxp-wind | from: 05 | also: met-systems -->

- `dddffGggKT`: direction/sustained/gust. `VRB` variable. `dddVddd` directional variation.
- METAR/TAF wind direction is true. Runway/ATC use requires magnetic/runway alignment awareness.
- `F:` XW=`wind×sin angle`; HW=`wind×cos angle`.
- `M:` 30° XW=½; 45°≈0.7; 60°≈0.87; 90°=full.
- `T:` use gust for control/landing margin; tailwind/XW/runway contamination stack risk.
***
#### Visibility / RVR
<!-- id: wxp-vis-rvr | from: 05 | also: met-fog, ifr-minima -->

- `P6SM` >6 SM. Fractions may be combined. Prevailing vis may hide directional/local variation in remarks.
- RVR gives runway visual range, usually hundreds/thousands ft with trend where reported.
- `T:` prevailing visibility, flight visibility, ground visibility, runway visibility and RVR are different legal/operational concepts.
***
#### Weather codes
<!-- id: wxp-wx-codes | from: 05 | kind: glossary -->

- Intensity: `-` light | no sign moderate | `+` heavy. Proximity `VC`.
- Descriptors: `MI` shallow | `BC` patches | `PR` partial | `DR` low drifting | `BL` blowing | `SH` showers | `TS` thunderstorm | `FZ` freezing.
- Precip: `DZ RA SN SG IC PL GR GS UP`.
- Obscuration: `BR FG FU VA DU SA HZ PY`.
- Other: `PO SQ FC SS DS`.
- `M:` `FZ` + liquid precip = immediate icing red flag.
***
#### Cloud groups
<!-- id: wxp-cloud-groups | from: 05 -->

- `FEW 1-2` | `SCT 3-4` | `BKN 5-7` | `OVC 8` oktas; `VV` obscured sky.
- `TCU/CB` appended to layer. `NSC/SKC/CLR` meanings depend station/reporting system.
- `T:` cloud base at destination may be legal while enroute terrain/cloud geometry is not.
***
#### Temperature / dew point
<!-- id: wxp-temp-dewpoint | from: 05 | also: met-stab -->

- Format `TT/DD`; `M` means minus. Spread small ⇒ saturation/fog/low cloud risk, especially cooling/night.
- `T:` dew-point spread alone does not predict fog; consider wind, cloud, moisture, terrain, advection and precipitation.
- `M:` freezing level + visible moisture/precip = icing analysis required.
***
#### Altimeter / pressure trend
<!-- id: wxp-altimeter | from: 05 | also: met-atmos -->

- `A2992` = 29.92 inHg. Remarks may show sea-level pressure and rapid rise/fall.
- `M:` high→low or warm→cold = actual lower than indicated.
- `T:` rapidly falling pressure often accompanies strengthening system/wind/weather deterioration.
***
#### Pebble
<!-- id: met-metar-pebble -->

- SCAN `ID-TIME-WIND-VIS-WX-CLOUD-T/TD-ALT-RMK`
- WIND `dddffGggKT, true direction | VRB | XW = wind×sin angle, HW = wind×cos angle | 30° = ½ / 45° ≈ 0.7 / 60° ≈ 0.87 / 90° = full | use gust for margin`
- VIS `P6SM = >6 SM | prevailing ≠ flight ≠ ground ≠ runway visibility ≠ RVR`
- WX `− light / no sign moderate / + heavy | VC proximity | FZ + liquid precip = icing red flag`
- CLOUD `FEW 1-2 / SCT 3-4 / BKN 5-7 / OVC 8 oktas | hundreds ft AGL | ceiling = lowest BKN/OVC/VV; SCT ≠ ceiling`
- T / ALT `TT/DD, M = minus | small spread alone ≠ fog | A2992 = 29.92 inHg`
***
