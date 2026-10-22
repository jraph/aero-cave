### AVIATION FORMULAS / CONVERSIONS — AV-CAVE v0.2
Navigation calculations reviewed 2026-10-19. Other sections retain their review dates; see [review status](../CONTENT_REVIEW.md).
`F` formula | `M` memory | `T` trap | `?` verify | Canada PPL/CPL/INRAT/IR mental math
`RELEASE:` `DERIVED/STUDY-REF PROVISIONAL` | `NOT FLIGHT AUTHORITY`
***
#### Units / constants

| Item | Memory |
|---|---|
| `1 NM` | `6076 ft` ≈ `1.852 km` |
| `1 SM` | `5280 ft` ≈ `1.609 km` |
| `1 NM` | ≈ `1.15 SM` |
| `1 kt` | `1 NM/hr` ≈ `1.15 mph` ≈ `1.852 km/h` |
| `1 hr` | `60 min`; `0.1 hr = 6 min` |
| `1 gal US` | `3.785 L` |
| `1 gal Imp` | `4.546 L` |
| `1 US gal avgas` | ≈ `6 lb` |
| `1 L avgas` | ≈ `1.6 lb` |
| `1 kg` | `2.205 lb` |
| `1 lb` | `0.454 kg` |
| `1 inHg` | ≈ `33.86 hPa` |
| `1 hPa` | ≈ `30 ft` pressure altitude rough |

- `T:` US gal ≠ Imperial gal. POH fuel units may differ from pump/club logs.
***
#### Time / speed / distance

- `F:` `distance = GS × time(hr)`.
- `F:` `time(hr)=distance/GS`; `time(min)=distance/GS×60`.
- `F:` `GS=distance/time(hr)`.
- `M:` `120 kt = 2 NM/min`; `90 kt = 1.5 NM/min`; `60 kt = 1 NM/min`.
- `T:` navigation timing uses `GS`, not IAS/TAS.
***
#### Quick ETE table

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
#### Fuel

- `F:` `fuel = time(hr) × burn`.
- `F:` `time available = usable fuel / burn`.
- `F:` `fuel remaining = fuel on board - fuel used`.
- `F:` `fuel used = burn × minutes/60`.
- `M:` burn `6 gph` ⇒ `0.1 gal/min`; burn `9 gph` ⇒ `0.15 gal/min`; burn `12 gph` ⇒ `0.2 gal/min`.
- `T:` IFR reserve starts after required destination/alternate logic, not after takeoff.
***
#### Weight / balance

- `F:` `moment = weight × arm`.
- `F:` `CG = Σmoment / Σweight`.
- `F:` `new CG = (old moment ± added/removed/shifted moment) / new weight`.
- `F:` shifted load moment change = `weight × distance shifted`.
- `M:` forward load lowers arm? depends datum. Calculate, don’t feel it.
- `T:` within max gross ≠ within CG envelope. Check takeoff + landing + zero-fuel if near limit.
***
#### Pressure altitude / density altitude

- `F:` `PA ≈ field elev + (29.92 - altimeter) × 1000`.
- `F:` `ISA temp °C ≈ 15 - 2 × altitude(thousands ft)`.
- `F:` `DA ≈ PA + 120 × (OAT - ISA)`.
- `M:` hot/high/humid/low pressure ⇒ DA↑ ⇒ roll↑ climb↓. Heavy independently worsens performance; weight does NOT change DA.
- `T:` DA formula is approximation; POH chart wins.
***
#### Temperature

- `F:` `°C = (°F - 32) × 5/9`.
- `F:` `°F = °C × 9/5 + 32`.
- `M:` `0°C=32°F`; `10°C=50°F`; `20°C=68°F`; `30°C=86°F`.
- `T:` cold temp correction affects obstacle clearance; not just comfort.
***
#### Cold temperature / altitude error

- `M:` high to low, look out below; warm to cold, look out below.
- `F rough:` altitude error ≈ `4 ft × height above station(thousands ft) × °C below ISA`.
- Example rough: `2000 ft above station`, `20°C colder than ISA` ⇒ `4×2×20=160 ft` low.
- `T:` use approved cold-temperature/CAP correction tables when required; rough formula is memory aid only.
***
#### Crosswind / headwind

- `F:` `headwind = wind speed × cos(angle)`.
- `F:` `crosswind = wind speed × sin(angle)`.
- `M:` `30° = 1/2 wind`; `45° ≈ 0.7 wind`; `60° ≈ 0.87 wind`; `90° = full wind`.
- `M:` headwind component: `30°≈0.87`, `45°≈0.7`, `60°=0.5`, `90°=0`.
- `T:` gusts matter. max demonstrated crosswind ≠ legal limit unless POH says; still operational limit/SOP/personal.
***
#### Wind correction / nav triangle

- `F exact idea:` WCA depends wind angle, wind speed, TAS.
- `F rough:` `WCA° ≈ 60 × crosswind / TAS`, for small WCA, with wind components resolved relative to desired track. Exact: `sin(WCA) = crosswind/TAS`; use a flight computer for large corrections.
- `F:` `heading = track ± WCA`.
- `M:` wind from right blows left ⇒ crab right.
- `T:` variation/deviation are separate from WCA.
***
#### True / magnetic / compass

- `F:` `TC ± WCA = TH`; `TH ± variation = MH`; `MH ± deviation = CH`.
- Alternatively convert TC→MC, then apply WCA to obtain MH before deviation. Never substitute magnetic course for magnetic heading.
- `M:` true→mag: east is least, west is best.
- `M:` TVMDC = True Virgins Make Dull Company; reverse = Can Dead Men Vote Twice.
- `T:` track/course/heading/bearing are different. Track = ground path; heading = nose.
***
#### Navigation aids — ADF / VOR / DME / intercepts

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
- `M VOR checks:` **4–6–4** = ground/VOT ±4° (FAA reference), airborne ±6°, dual receivers ≤4° total difference. Receiver accuracy ≠ tracking allowance. See [VOR receiver checks and Canadian source scope](10_inrat_knowledge_core_av_cave_v0_3.md#vor-receiver-checks--464).
***
#### 1-in-60 rule

- `F:` `track error° ≈ offtrack × 60 / distance flown`.
- `F:` `closing correction to destination° ≈ offtrack × 60 / distance remaining`.
- `F:` total correction = track error + closing correction.
- `M:` halfway off by 1 NM after 30 NM ⇒ error `2°`; if 30 NM left, add `2°`; total `4°`.
- `T:` use distance flown for error; distance remaining for correction.
***
#### Climb / descent gradient

- `F:` `ft/NM = ROC(fpm) × 60 / GS`.
- `F:` `ROC/ROD(fpm)=GS × gradient(ft/NM)/60`.
- `M:` `200 ft/NM ≈ 3.3%`.
- `M:` at `90 kt`, `300 ft/NM` needs `450 fpm`; at `120 kt`, needs `600 fpm`.
- `T:` gradient uses groundspeed. Tailwind increases GS and required fpm.
***
#### Percent gradient

- `F:` `% gradient = ft/NM / 60.76`.
- `F:` `ft/NM ≈ % × 60.76`.
- `M:` `3° glidepath ≈ 318 ft/NM ≈ 5.2%`.
- `M:` `3.3% ≈ 200 ft/NM`.
- `T:` degrees and percent are not the same.
***
#### Descent planning

- `F 3°:` `ROD ≈ GS × 5`.
- `F 3°:` descent distance NM ≈ `altitude to lose / 300`.
- `F:` time to descend = distance/GS×60.
- `M:` `90 kt` on 3° ⇒ `450 fpm`; `100 kt` ⇒ `500 fpm`; `120 kt` ⇒ `600 fpm`.
- `T:` add level-offs, stepdowns, tailwind, config, ATC restrictions.
***
#### Holding

- `F:` outbound timing adjusted to make inbound leg time.
- `R:` standard hold: outbound `1 min` at/below `14,000 ft ASL`; `1.5 min` above `14,000 ft ASL`. For DME holding, ATC/published procedure specifies distance instead of time. `[AIM 2026-1 RAC 10.3/10.6]`
- `M:` outbound wind correction ≈ `3×` inbound drift.
- `F:` DME leg time = leg distance / GS × 60.
- `T:` hold speed limits/published leg distances override memory.
***
#### Rate-one turn / turn geometry

- `F:` standard-rate turn = `3°/sec`; 360° in `2 min`.
- `F rough:` bank for rate-one ≈ `TAS/10 + 7`.
- `F:` turn radius `ft ≈ TAS² / (11.26 × tan(bank))`; radius `NM ≈ TAS² / (68,420 × tan(bank))`. `[DERIVED; TAS kt]`
- `M:` at `120 kt`, rate-one bank ≈ `19°`; at `90 kt`, ≈`16°`.
- `T:` high TAS needs more bank for standard rate.
***
#### Load factor / accelerated stall

- `F:` in a coordinated, constant-altitude turn, `n = 1 / cos(bank)`. The bank-only equation does not apply to every manoeuvre.
- `F:` `Vs_bank = Vs × √n`.
- `M:` `45°` bank ≈ `1.41g`, stall ×`1.19`; `60°` bank = `2g`, stall ×`1.41`.
- `T:` accelerated stall depends load factor/AoA, not just bank; POH chart wins.
***
#### Manoeuvring speed / stall-speed notation

- `VS` = generic stall speed in stated config; `VS1` = stall speed in specified config (**often clean**); `VS0` = stall speed in landing config. `VS` and `VS1` may denote the **same clean-config value** in context; do not substitute `VS0`.
- `F theoretical:` positive stall/limit-load intersection `VA_est ≈ VS(clean) × √n_limit`, using matching config/weight/speed basis; **not guaranteed published VA**.
- `M legacy normal:` `n_limit=+3.8` ⇒ `VA_est≈1.95×VS1` (mental shortcut `≈2×VS1`, **not a VA range**); e.g. `VS1=50 KIAS ⇒ ≈97.5 KIAS`.
- `F weight:` approximate `VA2≈VA1×√(W2/W1)` if same config/load-factor basis; lighter ⇒ lower speed.
- `T:` approved POH/AFM `VA` and weight schedule win; `VA` does **not** guarantee protection against multiple/abrupt control inputs or all turbulence.

***
#### VREF / landing reference speed

- `Definition:` `VREF` is the landing reference speed. Use the POH/AFM value for the specified landing configuration; certification bases differ. In landing-distance certification it is maintained to the `50 ft` screen height.
- `F fallback:` when `VREF` is not specified, use `VREF = 1.3 × VSO`. Example: `VSO 50 KIAS → VREF 65 KIAS`.
- `F weight:` for the same configuration and speed basis, `VREF₂ ≈ VREF₁ × √(W₂/W₁)`. Use POH/AFM landing-weight data when published.
- `Approach category:` use published `VREF`, or `1.3 VSO` if none is specified, at **maximum certificated landing weight**. Do not lower the category because today’s landing weight is lower. `[TC AIM 2026-1 RAC 9.21]`
- `T:` a wind/gust additive changes the operational approach target (`VAPP`), not the underlying `VREF`. Aircraft procedures and limitations govern.
***
#### Glide

- `F:` glide distance `NM = height AGL(ft) × glide ratio / 6076`.
- Example: `9:1` glide ratio ⇒ `1000 ft AGL ≈ 1.48 NM` still-air.
- `F:` time aloft ≈ height to lose / descent rate.
- `M C150M:` POH Fig. 3-1 shows approx `6000 ft AGL → 10 NM`; therefore `1000 ft ≈ 1.67 NM` at `60 KIAS`, flaps UP, prop windmilling, zero wind. `[C150M POH 1977 Fig. 3-1]`
- `T:` use height above terrain, not altitude ASL. Wind, configuration, propeller, speed and aircraft condition change actual range.
***
#### Runway / landing energy

- `F:` kinetic energy ∝ `V²`.
- `F:` speed increase energy factor = `(actual/target)²`.
- `M:` `+10% speed` ⇒ `+21% energy`; `+20% speed` ⇒ `+44% energy`.
- `T:` fast final burns runway and brakes. Tailwind hurts more than it feels.
***
#### IFR fuel / reserve memory

- Prop IFR with alternate: destination approach+missed → alternate → land → `45 min`.
- Prop IFR no alternate: destination approach+missed → `45 min`.
- Turbojet/helicopter: same structure but `30 min`.
- `T:` CAR text/current ops rules win; this is memory, not dispatch release.
***
#### Alternate minima memory

| Case | Weather memory |
|---|---|
| 2+ precision, separate suitable runways | `400-1` or `+200/+1/2`, greater |
| 1 precision | `600-2` or `+300/+1`, greater |
| NPA only | `800-2` or `+300/+1`, greater |
| no IFR approach | ≥`500 ft` above min IFR alt allowing VFR app/landing |

- `T:` check CAP alternate notes, NOTAM, NAVAID, runway suitability, forecast type.
***
#### TAF change groups

- `BECMG` improving: use new condition at end of period.
- `BECMG` deteriorating: use new condition at start of period.
- `TEMPO` must stay ≥ alternate minima.
- `PROB` must stay ≥ landing minima.
- `T:` alternate minima ≠ landing minima ≠ approach ban.
***
#### RVR / visibility quick memory

- `R non-Part VII aeroplane:` if both measured, below minimum when `RVR A <1200` **or** `RVR B <600`; if only A or B measured, below minimum when that RVR `<1200`. `[CAR 602.129]`
- Below-minimum RVR normally bars continuation beyond the applicable point, subject to listed exceptions: report received after FAF/final-course intercept, training no-landing, varying RVR, ground visibility ≥`1/4 SM`, or CAT III.
- Advisory visibility helps planning; DA/MDA visual reference controls descent/landing.
- `T:` this general rule excludes Part VII operations; ground visibility, runway visibility, RVR, advisory visibility and flight visibility are different.
***
#### Coordinates / distance / map

- `1° latitude = 60 NM`.
- `1' latitude = 1 NM`.
- Longitude distance = `60 NM × cos(latitude)` per degree.
- `F:` map distance real = measured distance × scale.
- `T:` longitude spacing shrinks toward poles.
***
#### Clocks / logbook

- `0.1 hr = 6 min`; `0.2=12`; `0.3=18`; `0.4=24`; `0.5=30`; `0.6=36`; `0.7=42`; `0.8=48`; `0.9=54`.
- `F:` decimal hours = minutes/60.
- `T:` flight time / air time / block time / night time / instrument time are different records.
***
#### Pebble

- `D=GS×t` | `t=min=D/GS×60` | `fuel=t×burn` | `CG=ΣM/ΣW` | `PA=elev+(29.92-alt)×1000` | `DA≈PA+120(OAT-ISA)` | `1-in-60: err=off×60/flown` | `WCA≈60×XW/TAS` | `ROC=GS×ft/NM/60` | `3° ROD=GS×5` | `TOD=alt lose/300` | `n=1/cosφ` | `Vsφ=Vs√n` | `VA_est=VS1√nlimit≈1.95VS1 @+3.8g; VS≈VS1 if same clean config ≠VS0` | `VREF=1.3VSO` if unpublished | `+10%V=+21%E` | `1°lat=60NM` | `0.1h=6min`.

***
#### Sources & review status

See the [separate review record](../CONTENT_REVIEW.md#historical-source-review-notes) for source editions, check dates and earlier validation notes.
