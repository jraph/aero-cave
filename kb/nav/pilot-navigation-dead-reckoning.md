# Pilot navigation & dead reckoning / Navigation à l’estime
<!-- concept: nav-dr | level: PPL CPL -->

[Index](README.md) · concept `nav-dr` · unit IDs are stable: never rename one.

***
#### Time / speed / distance
<!-- id: nav-time-speed-distance | from: 06 | kind: formula | level: PPL CPL IR -->

- `F:` `distance = GS × time(hr)`.
- `F:` `time(hr)=distance/GS`; `time(min)=distance/GS×60`.
- `F:` `GS=distance/time(hr)`.
- `M:` `120 kt = 2 NM/min`; `90 kt = 1.5 NM/min`; `60 kt = 1 NM/min`.
- `T:` navigation timing uses `GS`, not IAS/TAS.
***
#### Quick ETE table
<!-- id: nav-quick-ete-table | from: 06 | kind: formula | level: PPL CPL IR -->

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
<!-- id: nav-crosswind-headwind | from: 06 | kind: formula | level: PPL CPL IR -->

- `F:` `headwind = wind speed × cos(angle)`.
- `F:` `crosswind = wind speed × sin(angle)`.
- `M:` `30° = 1/2 wind`; `45° ≈ 0.7 wind`; `60° ≈ 0.87 wind`; `90° = full wind`.
- `M:` headwind component: `30°≈0.87`, `45°≈0.7`, `60°=0.5`, `90°=0`.
- `T:` gusts matter. max demonstrated crosswind ≠ legal limit unless POH says; still operational limit/SOP/personal.
***
#### Wind correction / nav triangle
<!-- id: nav-wind-correction-nav-triangle | from: 06 | kind: formula | level: PPL CPL IR -->

- `F exact idea:` WCA depends wind angle, wind speed, TAS.
- `F rough:` `WCA° ≈ 60 × crosswind / TAS`, for small WCA, with wind components resolved relative to desired track. Exact: `sin(WCA) = crosswind/TAS`; use a flight computer for large corrections.
- `F:` `heading = track ± WCA`.
- `M:` wind from right blows left ⇒ crab right.
- `T:` variation/deviation are separate from WCA.
***
#### 1-in-60 rule
<!-- id: nav-1-in-60-rule | from: 03, 06 | kind: formula | level: PPL CPL IR -->

- `F:` `track error° ≈ offtrack × 60 / distance flown`.
- `F:` `closing correction to destination° ≈ offtrack × 60 / distance remaining`.
- `F:` total correction = track error + closing correction.
- `M:` halfway off by 1 NM after 30 NM ⇒ error `2°`; if 30 NM left, add `2°`; total `4°`.
- `T:` use distance flown for error; distance remaining for correction.
- `T:` ETA uses actual GS. Double-track-error is a separate intercept technique, not a universal destination correction.
***
#### Coordinates / distance / map
<!-- id: nav-coordinates-distance-map | from: 06 | also: nav-units | kind: formula | level: PPL CPL IR -->

- `1° latitude = 60 NM`.
- `1' latitude = 1 NM`.
- Longitude distance = `60 NM × cos(latitude)` per degree.
- `F:` map distance real = measured distance × scale.
- `T:` longitude spacing shrinks toward poles.
***
#### Clocks / logbook
<!-- id: nav-clocks-logbook | from: 06 | also: nav-units | kind: formula | level: PPL CPL IR -->

- `0.1 hr = 6 min`; `0.2=12`; `0.3=18`; `0.4=24`; `0.5=30`; `0.6=36`; `0.7=42`; `0.8=48`; `0.9=54`.
- `F:` decimal hours = minutes/60.
- `T:` flight time / air time / block time / night time / instrument time are different records.
***
#### Diversion / lost
<!-- id: nav-diversion-lost | from: 01, 03 | level: PPL CPL -->

- Divert: decide early→dest→line feature→MTRK/dist/GS/ETA/fuel→terrain/airspace/wx→inform/advise.
- Lost: climb safe→communicate→conserve→confess→comply.
***
#### Pebble
<!-- id: nav-pilot-navigation-dead-reckoning-pebble | level: PPL CPL IR -->

- TSD `distance = GS × time | time(min) = distance/GS × 60 | 60 kt = 1 NM/min, 90 = 1.5, 120 = 2 | GS, not IAS/TAS`
- WIND `crosswind = wind × sin(angle), headwind = wind × cos(angle) | 30° = ½ / 45° ≈ 0.7 / 60° ≈ 0.87 / 90° = full | WCA° ≈ 60 × crosswind / TAS (small angles) | wind from right → crab right`
- 1-IN-60 `track error° ≈ off × 60 / distance flown | closing° ≈ off × 60 / distance remaining | total = error + closing | double-track-error ≠ destination correction`
- MAP / TIME `1° latitude = 60 NM, 1' = 1 NM | longitude = 60 NM × cos(latitude) | 0.1 h = 6 min | decimal minutes ≠ minutes:seconds`
- DIVERT / LOST `decide early → MTRK/dist/GS/ETA/fuel → terrain/airspace/wx → advise | lost: climb, communicate, conserve, confess, comply`
***
