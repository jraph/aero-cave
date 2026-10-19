### AVIATION FORMULAS / CONVERSIONS — AV-CAVE v0.2
`TARGETED CPAER REVIEW: 2026-09-06` | see `00_CPAER_REVIEW_NOTES.md` for scope and remaining gaps
`F` formula | `M` memory | `T` trap | `?` verify | Canada PPL/CPL/INRAT/IR mental math
`RELEASE:` `DERIVED/STUDY-REF PROVISIONAL` | `CANONICAL SOURCE:` `aviation_formulas_conversions_av_cave_v0_2.md` | `NOT FLIGHT AUTHORITY`
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

`F:` ETE (minutes) = distance (NM) × fraction below. Use **GS**, including wind.

| GS | NM/min | ETE fraction of NM | Mental calculation | 10 NM | 30 NM | 60 NM |
|---:|---:|---:|---|---:|---:|---:|
| `60 kt` | `1` | `×1` | same number | `10 min` | `30 min` | `60 min` |
| `75 kt` | `1¼` | `×⅘` | `÷5 ×4` | `8 min` | `24 min` | `48 min` |
| `90 kt` | `1½` | `×⅔` | `÷3 ×2` | `6 min 40 s` | `20 min` | `40 min` |
| `100 kt` | `1⅔` | `×⅗` | `÷5 ×3` | `6 min` | `18 min` | `36 min` |
| `120 kt` | `2` | `×½` | `÷2` | `5 min` | `15 min` | `30 min` |
| `150 kt` | `2½` | `×⅖` | `÷5 ×2` | `4 min` | `12 min` | `24 min` |
| `180 kt` | `3` | `×⅓` | `÷3` | `3 min 20 s` | `10 min` | `20 min` |

- `M:` `90 kt`: two-thirds of the NM gives minutes; `30 NM ÷3 ×2 = 20 min`.
- `T:` `6.7 min` is approximately `6 min 42 s`, not `6 min 7 s`; exact 10 NM at 90 kt is `6 min 40 s`.
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
#### Top of descent

- `F:` `TOD distance ≈ altitude to lose / 300` for 3°.
- `F:` `altitude to lose = current altitude - target altitude`.
- `M:` lose `6000 ft` ⇒ start about `20 NM` out on 3°.
- `T:` terrain/MEA/stepdowns/CAP profile can override simple 3° TOD.
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
#### Mental math shortcuts

- Divide by 60: `NM at 60 kt = minutes`.
- `GS 90`: minutes ≈ `NM × 2/3`.
- `GS 120`: minutes ≈ `NM / 2`.
- `GS 100`: minutes = `NM × ⅗` (`÷5 ×3`).
- `GS 150`: minutes = `NM × ⅖` (`÷5 ×2`).
- `GS 180`: minutes = `NM × ⅓` (`÷3`).
- `6 gph`: `1 gal/10 min`; `9 gph`: `1.5 gal/10 min`; `12 gph`: `2 gal/10 min`.
***
#### Pebble

- `D=GS×t` | `t=min=D/GS×60` | `fuel=t×burn` | `CG=ΣM/ΣW` | `PA=elev+(29.92-alt)×1000` | `DA≈PA+120(OAT-ISA)` | `1-in-60: err=off×60/flown` | `WCA≈60×XW/TAS` | `ROC=GS×ft/NM/60` | `3° ROD=GS×5` | `TOD=alt lose/300` | `n=1/cosφ` | `Vsφ=Vs√n` | `+10%V=+21%E` | `1°lat=60NM` | `0.1h=6min`.

***
#### Validated-source notes — v0.2

- Holding timing: TC AIM `2026-1`, RAC 10.3/10.6.
- General approach ban: CAR `602.129`, live consolidation checked `2026-07-10`.
- C150M glide: provided `1977 Model 150M POH`, Figure 3-1.
- Turn-radius and glide-ratio equations: derived unit-consistent formulas; POH/chart data wins.
