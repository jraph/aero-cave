# Icing / Givrage
<!-- concept: met-icing | level: PPL CPL IR -->

[Meteorology index / Index météo](README.md) · concept `met-icing` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Structural icing
<!-- id: wx-icing | from: 16 -->

- Requires visible moisture + aircraft surface at/below freezing.
- **Rime:** small supercooled drops, rapid freeze, rough/opaque.
- **Clear:** larger drops, slower freeze/spread, smooth/heavy.
- **Mixed:** combination.
- Effects: lift↓, drag↑, stall speed↑, climb↓; prop/intake/static/control contamination.
- `!:` freezing rain/drizzle and severe icing require immediate escape.
- `T:` `OAT >0°C` at surface says nothing about cloud icing aloft.
***
#### Freezing level
<!-- id: wx-freezing-level | from: 16 | also: met-stab -->

- Altitude where `0°C`; may be multiple levels with inversions.
- `F exam parcel 0°C:` AGL ≈ `CB_exam + 1000×Td_surface/1.5` ft: assumes cloud-base parcel temperature ≈ surface dew point and SALR≈1.5°C/1000 ft.
- `F parcel 0°C:` `T_CB ≈ T_surface−3×CB_parcel/1000`; if `T_CB>0°C`, parcel reaches 0°C at `CB_parcel+1000×T_CB/1.5` ft AGL (approximate/variable SALR).
- `T:` parcel 0°C height ≠ atmospheric freezing level; use actual environmental temperature profile / GFA / temperatures aloft. Temperature inversions may create multiple 0°C levels.
- Freezing level ≠ guaranteed icing layer; requires moisture.
- Cloud + subzero temp + PIREP/AIRMET icing = stronger evidence.
***
#### Icing gate
<!-- id: wxp-icing | from: 05 | also: met-decide -->

- Visible moisture + subfreezing surface; `FZRA/FZDZ` especially severe. Types rime/clear/mixed; trace/light/moderate/severe.
- `!:` non-approved aircraft: avoid forecast/reported ice; exit at first indication.
- Red: `FZRA/FZDZ/PL`, freezing-level crossing in cloud/precip, warm-front overrunning, PIREP/AIRMET/SIGMET, tops above capability. `T:` surface >`0°C` does not clear icing aloft.
***
#### Snow / freezing precipitation
<!-- id: wxp-snow-fzra | from: 05 -->

- Snow reduces visibility rapidly; blowing snow may create whiteout/false horizon; contamination harms acceleration/braking/lift.
- Ice pellets imply warm layer aloft and possible nearby freezing rain/mixed icing.
- `!:` freezing rain = severe icing/ground contamination risk; avoid.
- `T:` light snow code can still produce unacceptable visual contrast/visibility.
***
