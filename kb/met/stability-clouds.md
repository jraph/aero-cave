# Temperature, moisture, stability & cloud / Température, humidité, stabilité et nuages
<!-- concept: met-stab | level: PPL CPL IR -->

[Meteorology index / Index météo](README.md) · concept `met-stab` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Temperature / dew point
<!-- id: wx-temp-dewpoint | from: 16 -->

- Dew point = temperature air must cool to reach saturation at constant pressure/water content.
- Small `T-Td` spread + cooling ⇒ fog/low cloud increasingly likely.
- Temperature inversion = temp increases with height; strongly stable, traps haze/smoke, can create wind shear.
- `T:` small spread alone does not guarantee fog.
***
#### Lapse rates / stability
<!-- id: wx-lapse-stability | from: 16 -->

- `DALR` unsaturated ≈ `3°C/1000 ft`.
- `SALR` saturated ≈ `1.5°C/1000 ft` average; varies with temp/moisture.
- Environment cools faster than DALR ⇒ absolutely unstable.
- Environment cools slower than SALR / inversion ⇒ absolutely stable.
- Between SALR/DALR ⇒ conditionally unstable.
- Stable: stratiform cloud, smooth air, poor vis, steady precip, broad ice.
- Unstable: CU/TCU/CB, turbulence, showers, generally better between-cloud vis.
- `M:` steep lapse = vertical motion grows.
***
#### Moisture / cloud formation
<!-- id: wx-moisture-cloud | from: 16 -->

- Need moisture + cooling to saturation.
- Cooling mechanisms: lifting, radiation, contact/advection, mixing.
- Lift: convection, fronts, terrain, convergence.
- Condensation nuclei help droplets form.
- Cloud base often near LCL; rising unsaturated air cools DALR until saturated, then SALR.
- `F exam CB:` convective cloud base AGL ≈ `1000(T−Td)/3` ft, with surface `T,Td` °C; **simplified course shortcut** assumes Td ≈ constant during unsaturated ascent.
- `F parcel CB:` LCL/cloud base AGL ≈ `1000(T−Td)/(3−0.5)` ft; parcel T↓ ≈3°C/1000 ft, parcel Td↓ ≈0.5°C/1000 ft; both approximate.
- `T:` estimates apply to a surface-lifted convective parcel, not every observed ceiling/cloud base; field elevation + AGL = ASL only for same vertical datum.
***
#### Cloud families
<!-- id: wx-cloud-families | from: 16 -->

| Cloud | Typical significance |
|---|---|
| `Ci/Cs/Cc` | high ice cloud; system/front clues |
| `As/Ac` | mid-level layered/convective; possible icing |
| `St/Sc` | low stable layer; ceiling/vis concern |
| `Ns` | widespread steady precip, low ceilings |
| `Cu` | convective; benign→growing |
| `TCU` | strong convection, turbulence/icing |
| `CB` | TS hazards: turbulence/hail/ice/lightning/shear |

- `T:` cloud type often tells stability/lift mechanism.
***
#### Precipitation
<!-- id: wx-precip | from: 16 -->

- Droplets/crystals grow by collision/coalescence or ice-crystal process.
- `RA` liquid; `DZ` tiny droplets; `SN`; `PL` ice pellets; `FZRA/FZDZ` supercooled liquid freezing on contact.
- `!:` freezing rain/drizzle = high-severity icing signal.
- Virga = precip evaporates before ground; may indicate downdrafts/microburst potential.
***
#### Pebble
<!-- id: met-stab-pebble -->

- LAPSE `DALR ≈3°C/1000 ft | SALR ≈1.5°C/1000 ft average, varies | environment cools faster than DALR → absolutely unstable | slower than SALR / inversion → absolutely stable | between → conditionally unstable`
- AIR `stable = STRATUS-SMOOTH-POOR VIS-steady precip | unstable = CU/TCU/CB-TURB-SHOWERS, better vis between cloud`
- CLOUD BASE `exam AGL = 1000(T−Td)/3 | parcel AGL = 1000(T−Td)/(3−0.5) | surface-lifted convective parcel only ≠ every ceiling`
- DEW POINT `small T−Td + cooling → fog/low cloud more likely, not guaranteed | inversion = temp↑ with height: strongly stable, traps haze/smoke, possible wind shear`
- PRECIP `FZRA/FZDZ = supercooled liquid, freezes on contact → high-severity icing | virga → possible downdraft/microburst`
***
