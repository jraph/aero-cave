# Radio navigation (VOR / ADF / DME / ILS) / Radionavigation (VOR / ADF / DME / ILS)
<!-- concept: nav-radio | level: IR -->

[IFR index / Index IFR](README.md) · concept `nav-radio` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Navigation aid checks
<!-- id: ifr-navigation-aid-checks | from: 10 -->

- VOR: identify Morse/voice, correct frequency/course/TO-FROM, service volume and NOTAM.

##### VOR receiver checks — 4–6–4

| Check | Maximum acceptable error / difference |
|---|---|
| VOT / designated ground checkpoint | **±4°** from the reference indication (FAA AIM reference; see Canadian scope below) |
| Airborne landmark / published-radial check | **±6°** from the published radial |
| Dual independent VOR receivers, same station | **4° total difference** between indicated bearings |

- `M:` **4 ground — 6 airborne — 4 between receivers.**
- `P VOT:` with CDI centred, reference indication is **000° FROM** or **180° TO**; apply ±4°. A designated ground checkpoint uses its published radial instead.
- `T dual:` NAV1 030° / NAV2 034° = at the limit; 030° / 035° = exceeds tolerance. This is **4° between receivers**, not ±4° each. Compare using the same TO/FROM sense.
- `T airborne:` ±6° is a **receiver-check tolerance**, not permission to track 6° off course.
- **Canadian scope:** TC AIM 2026-1 COM 4.5.1–4.5.2 specifies the dual comparison and airborne check: difference greater than 4° requires investigation/correction before IFR use; airborne error greater than 6° means the equipment should not be used for IFR navigation. The ground/VOT ±4° and VOT indications above are explicitly sourced to the FAA AIM; do not infer U.S. checking intervals or recordkeeping requirements for Canada.
- **Sources:** [TC AIM 2026-1, COM 4.5.1–4.5.2](https://tc.canada.ca/en/aviation/publications/transport-canada-aeronautical-information-manual-tc-aim-tp-14371); [FAA AIM 1-1-4, VOR Receiver Check](https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap1_section_1.html). Reviewed 2026-10-19.


- ILS: identify LOC; set front course; GS alive from below; marker/DME/fixes per plate.
- NDB: identify; station passage/needle swing; ADF errors near TS/coast/night/mountain.
- GNSS: current DB, RAIM/WAAS, correct mode, CDI scaling, annunciations.
- `T:` failed identification = unusable navaid for approach.
***
#### Navigation aids — ADF / VOR / DME / intercepts
<!-- id: nav-navigation-aids-adf-vor-dme-intercepts | from: 06 | kind: formula | level: CPL IR -->

| Memory | Calculation / example |
|---|---|
| Conventions | MH = magnetic heading; RB = clockwise relative bearing from nose; BTS/BFS = bearing TO/FROM station. Use one north reference throughout. |
| Wrap / Normaliser | wrap(x) = x modulo 360; add/subtract 360 until 0–359°. North may be written 000° or 360°. |
| BTS = MH + RB | BTS = wrap(MH + RB). MH 350°, RB 040° → BTS 030°. |
| BFS = BTS ±180 | BFS = wrap(BTS +180°). BTS 030° → BFS 210°: aircraft southwest of station. |
| RB = BTS − MH | RB = wrap(BTS − MH). BTS 020°, MH 080° → RB 300° (60° left of nose). |
| MH = BTS − RB | MH = wrap(BTS − RB). BTS 100°, RB 250° → MH 210°. |
| ADF card / Rose | Fixed card: read RB. Movable card: set current MH under index to read magnetic BTS. RMI: correctly referenced needle head = BTS, tail = BFS. |
| Turn / Virage | At essentially unchanged position, right turn +30° → RB decreases 30°; left turn → RB increases. BTS stays nearly unchanged. |
| Homing ≠ tracking | RB 000° points the nose at the station. In crosswind, holding RB 000° gives a curved homing path. Tracking needs wind correction. |
| VOR radial | Radial = bearing FROM station. On R-090: outbound course 090°; inbound course 270°. Identify aid and north reference (true-reference exceptions exist in Canada). |
| TO / FROM | With CDI centred: selected course toward station → TO; reciprocal → FROM. Flag describes selected-course geometry, not aircraft heading or actual travel. |
| 30° intercept setup | C = desired direction of travel, NOT always radial. Choose H = C ±30° toward the course line. Sketch station, current BFS and target line first; heading alone cannot select the side. No-wind examples below. |
| Capture: inbound | At capture BTS = C; RB = wrap(C − H). H=C+30 → RB330; H=C−30 → RB030. Start rollout with appropriate lead. |
| Capture: outbound | At capture BTS = wrap(C+180); RB = wrap(C+180−H). H=C+30 → RB150; H=C−30 → RB210. |
| Inbound example | Aircraft west-northwest of NDB (BFS285), intercept C090 inbound: H120 toward line. At capture BTS090, RB330. Turn left toward 090, then correct wind. |
| Outbound example | Aircraft northeast (BFS045), intercept C090 outbound: H120. At capture BFS090, BTS270, RB150. Turn left toward 090, then correct wind. |
| Wind trap / Vent | 30° is a chosen training intercept, not a universal rule. Wind changes the ground intercept angle. Always compute capture RB from actual heading; after capture fly the wind-corrected heading. |
| Cross-track distance | Lateral offset = ground range × sin(angular error); small angle ≈ range × error°/60. At 30 NM, 4° → about 2 NM. |
| VOR dots | Conventional VOR CDI: normally 2° per dot, ±10° full scale. Two dots at 30 NM ≈ 2 NM. LOC and GNSS scales differ; check equipment/mode. |
| DME geometry | Slant NM = √(ground NM² + height NM²); height NM = height above station(ft)/6076. Over station at 6076 ft above it → about 1 DME, not zero. |
| DME ground range | Ground NM = √(DME² − height NM²). DME 5 NM, height 6076 ft → √24 ≈4.90 NM. DME speed/time meaningful toward/away from station; unreliable for along-track speed on an arc. |
| 30° closing time | For a 30° GROUND-track intercept: closing speed = GS × sin30 = GS/2. Time(min)=120 × lateral NM/GS. 2 NM off at 120 kt → 2 min. Wind-correct heading to obtain that ground track. |
***
- `M VOR checks:` **4–6–4** = ground/VOT ±4° (FAA reference), airborne ±6°, dual receivers ≤4° total difference. Receiver accuracy ≠ tracking allowance. See [VOR receiver checks and Canadian source scope](navaid-checks.md#navigation-aid-checks).
***
#### Pebble
<!-- id: ifr-navaid-checks-pebble -->

- VOR CHECK `4 ground — 6 airborne — 4 between receivers | VOT: 000° FROM or 180° TO, ±4° (FAA AIM source) | airborne ±6° from published radial | dual: 4° TOTAL difference, same TO/FROM sense | Canada (TC AIM COM 4.5.1–4.5.2): dual >4° or airborne >6° → not for IFR until corrected`
- T `±6° = receiver-check tolerance ≠ permission to track off course | failed identification = unusable navaid for approach | do not infer U.S. intervals/recordkeeping for Canada`
***
