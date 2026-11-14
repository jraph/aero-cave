# Pilot navigation & dead reckoning / Navigation à l’estime
<!-- concept: nav-dr | level: PPL CPL -->

[Index](README.md) · concept `nav-dr` · unit IDs are stable: never rename one.

***
#### Navigation
<!-- id: nav-navigation | from: 01 | level: PPL CPL -->

- Track=ground path. Heading=nose. Bearing=direction to object. Course=planned line.
- `T±V=M±D=C`; true→mag: east least, west best.
- `F:` time=dist/GS; fuel=time×burn; 1-in-60 error°≈offtrack×60/dist flown.
- Divert: decide early→dest→line feature→track/dist/GS/ETA/fuel→inform. Lost: climb safe→communicate→conserve→confess→comply.
***
#### Nav / MET / systems
<!-- id: nav-nav-met-systems | from: 03 | also: met-decide | level: CPL -->

- ETA uses actual GS. `1-in-60:` track error≈off×60/distance flown; closing angle≈off×60/distance remaining; destination correction=error+closing angle. Double-track-error is a separate intercept technique, not a universal destination correction.
- Divert early→MTRK/dist/GS/ETA/fuel→terrain/airspace/wx→advise.
- MET trends > snapshot. Cold front=sudden/showers/TS/gusts; warm=layer/low ceiling/steady precip.
- Systems: fuel/oil/electrical/ignition/vacuum/pitot-static/flaps/brakes/heat/vent. `T:` checklist item without system model = weak oral.
***
#### Time / speed / distance
<!-- id: nav-time-speed-distance | from: 06 | also: study-formulas | level: PPL CPL IR -->

- `F:` `distance = GS × time(hr)`.
- `F:` `time(hr)=distance/GS`; `time(min)=distance/GS×60`.
- `F:` `GS=distance/time(hr)`.
- `M:` `120 kt = 2 NM/min`; `90 kt = 1.5 NM/min`; `60 kt = 1 NM/min`.
- `T:` navigation timing uses `GS`, not IAS/TAS.
***
#### Quick ETE table
<!-- id: nav-quick-ete-table | from: 06 | also: study-formulas | level: PPL CPL IR -->

Distance in NM × fraction = ETE in minutes. Use GS, including wind.

| GS | ETE fraction | Mental calculation | 10 NM | 30 NM | 60 NM |
|---:|---:|---|---:|---:|---:|
| 60 kt | ×1 | same number | 10 min | 30 min | 60 min |
| 75 kt | ×4/5 | ÷5 ×4 | 8 min | 24 min | 48 min |
| 90 kt | ×2/3 | ÷3 ×2 | 6 min 40 s | 20 min | 40 min |
| 100 kt | ×3/5 | ÷5 ×3 | 6 min | 18 min | 36 min |
| 120 kt | ×1/2 | ÷2 ×1 | 5 min | 15 min | 30 min |
| 150 kt | ×2/5 | ÷5 ×2 | 4 min | 12 min | 24 min |
| 180 kt | ×1/3 | ÷3 ×1 | 3 min 20 s | 10 min | 20 min |

90 kt: two-thirds of the NM gives minutes. Decimal minutes are not minutes:seconds.
***
#### Crosswind / headwind
<!-- id: nav-crosswind-headwind | from: 06 | also: study-formulas | level: PPL CPL IR -->

- `F:` `headwind = wind speed × cos(angle)`.
- `F:` `crosswind = wind speed × sin(angle)`.
- `M:` `30° = 1/2 wind`; `45° ≈ 0.7 wind`; `60° ≈ 0.87 wind`; `90° = full wind`.
- `M:` headwind component: `30°≈0.87`, `45°≈0.7`, `60°=0.5`, `90°=0`.
- `T:` gusts matter. max demonstrated crosswind ≠ legal limit unless POH says; still operational limit/SOP/personal.
***
#### Wind correction / nav triangle
<!-- id: nav-wind-correction-nav-triangle | from: 06 | also: study-formulas | level: PPL CPL IR -->

- `F exact idea:` WCA depends wind angle, wind speed, TAS.
- `F rough:` `WCA° ≈ 60 × crosswind / TAS`, for small WCA, with wind components resolved relative to desired track. Exact: `sin(WCA) = crosswind/TAS`; use a flight computer for large corrections.
- `F:` `heading = track ± WCA`.
- `M:` wind from right blows left ⇒ crab right.
- `T:` variation/deviation are separate from WCA.
***
#### 1-in-60 rule
<!-- id: nav-1-in-60-rule | from: 06 | also: study-formulas | level: PPL CPL IR -->

- `F:` `track error° ≈ offtrack × 60 / distance flown`.
- `F:` `closing correction to destination° ≈ offtrack × 60 / distance remaining`.
- `F:` total correction = track error + closing correction.
- `M:` halfway off by 1 NM after 30 NM ⇒ error `2°`; if 30 NM left, add `2°`; total `4°`.
- `T:` use distance flown for error; distance remaining for correction.
***
#### Coordinates / distance / map
<!-- id: nav-coordinates-distance-map | from: 06 | also: nav-units, study-formulas | level: PPL CPL IR -->

- `1° latitude = 60 NM`.
- `1' latitude = 1 NM`.
- Longitude distance = `60 NM × cos(latitude)` per degree.
- `F:` map distance real = measured distance × scale.
- `T:` longitude spacing shrinks toward poles.
***
#### Clocks / logbook
<!-- id: nav-clocks-logbook | from: 06 | also: nav-units, study-formulas | level: PPL CPL IR -->

- `0.1 hr = 6 min`; `0.2=12`; `0.3=18`; `0.4=24`; `0.5=30`; `0.6=36`; `0.7=42`; `0.8=48`; `0.9=54`.
- `F:` decimal hours = minutes/60.
- `T:` flight time / air time / block time / night time / instrument time are different records.
***
