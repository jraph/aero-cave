### WEATHER DECODING / GO-NO-GO QRC — AV-CAVE v0.2 COMPACT
`TARGETED CPAER REVIEW: 2026-09-06` | see `00_CPAER_REVIEW_NOTES.md` for scope and remaining gaps
`P` procedure | `R` rule | `F` formula | `T` trap | `M` memory | `!` safety | `?` verify | Canada PPL/CPL/INRAT/IR
`RELEASE:` `STUDY/OPS-REF PROVISIONAL` | `NOT FLIGHT AUTHORITY`
***
#### Source / master scan

- `SRC:` current AIM MET + NAV CANADA/FIC + CARs/CAP/CFS/NOTAM. Products describe; PIC decides legal + safe.
- Review GFA/AIRMET/SIGMET→TAF/METAR/SPECI→PIREP/upper winds→radar/satellite/lightning→RSC/CRFI/cameras.
- `P:` big picture→route→DEP/enroute/DEST/ALT→escape→update. `M:` `SYNOPTIC-GFA-HAZARDS-TERMINALS-PIREP-WINDS-RUNWAY-TREND`.
- `T:` never one product: decode→compare→trend→threats→options.
***
#### Go/no-go gates

- `LEGAL:` minima/alternate/approach ban/fuel/equipment/day-night.
- `AIRCRAFT:` icing approval/wind-XW/runway/performance/terrain/heat-defrost.
- `PILOT:` currency/recent IMC-night-XW-ice/fatigue/workload. `OPTIONS:` alternates/turn-back/fuel/route-alt-time.
- `T:` legal + no options = fragile.
***
#### Product roles

| Product | Tells you |
|---|---|
| `METAR` | observed aerodrome weather now |
| `SPECI` | significant observed change |
| `TAF` | forecast aerodrome conditions/time changes |
| `GFA` | regional clouds/weather + icing/turb/freezing level |
| `AIRMET` | potentially hazardous weather / significant change below SIGMET severity |
| `SIGMET` | significant hazardous weather affecting flight safety |
| `PIREP` | actual conditions encountered |
| `FB/upper winds` | forecast wind/temp aloft |
| `Radar` | precipitation location/intensity/trend; not all turbulence/ice |
| `Satellite` | cloud structure/coverage; interpretation required |
| `RSC/CRFI` | runway contamination/condition/friction information |

- `T:` radar gap ≠ clear air. no PIREPs ≠ no hazard.
***
#### METAR / SPECI scan

- `P:` type→ID→time→wind→vis/RVR→WX→cloud→T/TD→ALT→RMK. `M:` `ID-TIME-WIND-VIS-WX-CLOUD-T/TD-ALT-RMK`.
- Cloud heights: hundreds ft AGL; ceiling=lowest `BKN/OVC/VV`; `SCT`≠ceiling.
- `SPECI:` significant change; compare last `2–4` reports for ceiling/vis/wind/pressure/precip/convection.
- `T:` `AUTO` limits and remarks matter; recent SPECI can override comfort from older data.
***
#### Wind decoding

- `dddffGggKT`: direction/sustained/gust. `VRB` variable. `dddVddd` directional variation.
- METAR/TAF wind direction is true. Runway/ATC use requires magnetic/runway alignment awareness.
- `F:` XW=`wind×sin angle`; HW=`wind×cos angle`.
- `M:` 30° XW=½; 45°≈0.7; 60°≈0.87; 90°=full.
- `T:` use gust for control/landing margin; tailwind/XW/runway contamination stack risk.
***
#### Visibility / RVR

- `P6SM` >6 SM. Fractions may be combined. Prevailing vis may hide directional/local variation in remarks.
- RVR gives runway visual range, usually hundreds/thousands ft with trend where reported.
- `T:` prevailing visibility, flight visibility, ground visibility, runway visibility and RVR are different legal/operational concepts.
***
#### Weather codes

- Intensity: `-` light | no sign moderate | `+` heavy. Proximity `VC`.
- Descriptors: `MI` shallow | `BC` patches | `PR` partial | `DR` low drifting | `BL` blowing | `SH` showers | `TS` thunderstorm | `FZ` freezing.
- Precip: `DZ RA SN SG IC PL GR GS UP`.
- Obscuration: `BR FG FU VA DU SA HZ PY`.
- Other: `PO SQ FC SS DS`.
- `M:` `FZ` + liquid precip = immediate icing red flag.
***
#### Cloud groups

- `FEW 1-2` | `SCT 3-4` | `BKN 5-7` | `OVC 8` oktas; `VV` obscured sky.
- `TCU/CB` appended to layer. `NSC/SKC/CLR` meanings depend station/reporting system.
- `T:` cloud base at destination may be legal while enroute terrain/cloud geometry is not.
***
#### Temperature / dew point

- Format `TT/DD`; `M` means minus. Spread small ⇒ saturation/fog/low cloud risk, especially cooling/night.
- `T:` dew-point spread alone does not predict fog; consider wind, cloud, moisture, terrain, advection and precipitation.
- `M:` freezing level + visible moisture/precip = icing analysis required.
***
#### Altimeter / pressure trend

- `A2992` = 29.92 inHg. Remarks may show sea-level pressure and rapid rise/fall.
- `M:` high→low or warm→cold = actual lower than indicated.
- `T:` rapidly falling pressure often accompanies strengthening system/wind/weather deterioration.
***
#### TAF scan / groups

- `P:` ID→issue/valid→prevailing→`FM/BECMG/TEMPO/PROB` timeline covering DEP/ETA/ALT ETA + delay; do not average groups.
- `FM` permanent from minute | `BECMG` gradual permanent | `TEMPO` each `<1 h`, total `≤½` period | `PROB30/40` probability.
- `FM` begins a new self-contained forecast period. With `BECMG/TEMPO`, unchanged groups may carry forward, but a changed cloud group gives the complete new cloud picture; visibility/weather/obscuration form another related group. Do not retain an old cloud layer merely because it is absent after a change. `[AIM MET 7.4]`
***
#### TAF alternate / risk

- `BECMG` improve=end, deteriorate=start; `TEMPO`≥alternate minima; `PROB`≥landing minima.
- `T:` alternate≠landing≠approach-ban minima. `TEMPO` near ETA and `PROB30/40` high-consequence `TS/FZRA/low vis` require fuel/options; many short groups reduce confidence.
***
#### GFA

- Most probable conditions ≤`24,000 ft`; issued `4×/day` approx `2330/0530/1130/1730Z`, valid `0000/0600/1200/1800Z`.
- Six charts: C&W + icing/turb/freezing at valid/`+6 h/+12 h`; final C&W adds `12 h` IFR outlook.
- `P:` region/time→system/motion→cloud bases/tops→vis/WX/wind→icing/turb/freezing→comments/outlook; interpolate snapshots with buffer.
- Heights hundreds ft `ASL` unless `CIG/AGL`; METAR/TAF clouds AGL. `LCA≤25% | PTCHY 26–50% | XTNSV/INTMT>50%`; `P6SM`=>6 SM.
- Movement/`6 h`: `5 kt≈30 NM`, `10 kt≈60 NM`, `20 kt≈120 NM`. `T:` local/patchy hazard may sit on route.
***
#### AIRMET / SIGMET / PIREP

| Product | Use / trap |
|---|---|
| `AIRMET` | moderate ice/turb, low CIG/vis, strong wind, mountain obscuration/significant change; may exceed light-GA capability |
| `SIGMET` | TS, severe turb/LLWS/wave/ice, TC, dust/sand, VA/radioactive cloud; avoid; expired≠hazard ended |
| `PIREP` | actual `/OV /TM /FL /TP /SK /TA /WV /TB /IC /RM`; match time/place/level/type; jet “light” may be severe operationally for trainer |

- `P:` plot phenomenon/area/time/levels/movement/change; compare route/ETA and updates. UUA includes severe/extreme turb, severe ice, LLWS, tornado/funnel/waterspout, VA or other safety-critical condition.
***
#### Upper winds / temperature

- Use forecast level nearest route altitude; interpolate if needed. Wind is true direction/speed; temperature °C, omitted at low levels in some coding conventions.
- `P:` compute WCA/GS/fuel→compare freezing level/temp→select altitude balancing wind, terrain, cloud, icing, oxygen/performance.
- `T:` strongest tailwind route may place you in icing/turbulence/terrain trap.
***
#### Stability / fronts / fog

- Stable: layered/smooth/poor vis/steady precip/broad ice; unstable: CU/TCU/CB/turb/showers. `M:` moisture+lift+instability→convection.
- Warm front: broad lowering CIG/vis/steady precip/FZRA-PL risk; cold front: narrower SH/TS/gust/shift/turb/rapid change; occlusion: mixed/extensive.
- Fog: radiation=clear/light wind/moist cooling; advection=warm moist over cold; upslope=forced lift; steam=cold over warm water; precip fog=rain into cold air.
- `T:` timing errors can rapidly change runway/wind/CIG; fog may form after departure.
***
#### Icing gate

- Visible moisture + subfreezing surface; `FZRA/FZDZ` especially severe. Types rime/clear/mixed; trace/light/moderate/severe.
- `!:` non-approved aircraft: avoid forecast/reported ice; exit at first indication.
- Red: `FZRA/FZDZ/PL`, freezing-level crossing in cloud/precip, warm-front overrunning, PIREP/AIRMET/SIGMET, tops above capability. `T:` surface >`0°C` does not clear icing aloft.
***
#### Carburetor icing

- Possible in humid conditions and well above freezing, especially partial power/descent.
- `P:` apply carb heat per POH; expect initial RPM loss/roughness, then recovery if ice melts.
- `T:` structural icing forecast and carb icing risk are different.
***
#### Convection gate

- Hazards: extreme turb/hail/lightning/ice/heavy precip/shear-microburst/tornado/instrument errors.
- `!:` large-margin avoidance of cells/lines/embedded TS; never thread a radar gap.
- Assess SIGMET/GFA/TAF/PIREP/radar/lightning/satellite for movement/growth/line/escape. `T:` datalink delayed; attenuation hides cells.
***
#### LLWS / microburst

- TAF wind shear group describes significant shear in lowest `1500 ft AGL`.
- Red flags: TS/gust front, virga, strong inversion/low-level jet, large surface-vs-aloft wind difference.
- `!:` postpone/avoid severe shear; go-around may enter worse performance.
- `T:` increasing airspeed followed by rapid loss can be microburst signature; follow aircraft procedure.
***
#### Turbulence

- Mechanical: strong wind over rough terrain/obstacles; worst low/lee.
- Convective: CU/TCU/CB/showers. Mountain wave: strong cross-ridge stable flow. CAT: jet-stream/wind-shear zones aloft.
- `P:` choose altitude/route/time; slow to turbulence penetration speed per POH; secure cabin; report.
- `T:` Va changes with weight; published max-gross Va may be too high at lower weight.
***
#### Wind / runway gate

- Compute steady + gust XW/HW/TW; compare POH/SOP/personal limits.
- Add runway length/slope/surface/RSC/CRFI, obstacles, mechanical turbulence, wind shear.
- `T:` gusty XW + wet/contaminated short runway = compounded risk, not separate minor issues.
***
#### Snow / freezing precipitation

- Snow reduces visibility rapidly; blowing snow may create whiteout/false horizon; contamination harms acceleration/braking/lift.
- Ice pellets imply warm layer aloft and possible nearby freezing rain/mixed icing.
- `!:` freezing rain = severe icing/ground contamination risk; avoid.
- `T:` light snow code can still produce unacceptable visual contrast/visibility.
***
#### Mountain / terrain weather

- Check ridge wind angle/speed, mountain wave, rotor, obscuration, ceiling above pass, escape route, downdraft performance.
- `P:` cross ridge with margin/angle/escape; avoid lee rotor/cloud; no narrow-valley commitment without turnaround room.
- `T:` reported aerodrome ceiling may not clear enroute terrain.
***
#### Night weather

- Raise minima for cloud/vis/terrain/precip. Horizon and cloud boundaries disappear; snow/black-hole effects worsen.
- Moon illumination, terrain lighting and cloud cover affect visual navigation.
- `T:` legal night VFR visibility may provide poor terrain/weather avoidance.
***
#### VFR go/no-go flow

- `P:` ceiling/vis trend→terrain clearance→cloud layers/tops→precip/TS→wind/XW→daylight/night→diversion airports→fuel.
- Establish personal minimums by day/night, terrain, route familiarity and passenger pressure.
- `T:` scud running = shrinking options; turn around before valley/ceiling closes.
***
#### IFR go/no-go flow

- `P:` departure minima/ODP→enroute MEA/icing/TS→destination TAF/RVR/wind→alternate legality→approach/runway/NOTAM→missed/climb→fuel/options.
- Single-engine IFR: terrain/icing/engine-failure landing options. Multi-engine: actual OEI climb/ceiling.
- `T:` legal approach at destination + unusable alternate + icing enroute = no robust plan.
***
#### Trend

- Compare last `3` METAR/SPECI + TAF + GFA panels + radar/satellite + PIREPs; mark CIG/vis/wind/pressure `↑/↓` and precip/cell motion.
- `M:` observation=now; forecast=expected; trend=forecast performance. Worse observations→confidence↓.
***
#### Personal weather matrix

| Threat | Green | Amber | Red |
|---|---|---|---|
| ceiling/vis | well above personal min | close/trending down | below or no escape |
| wind/XW | stable below limit | gusty/near limit | above limit/shear |
| icing | none/clear escape | uncertain nearby | forecast/reported in route |
| convection | none/distant | isolated with wide escape | line/embedded/near route |
| runway | dry/long | wet/short margin | contam/braking unknown |
| options | many | limited | single point of failure |

- `T:` multiple amber items often equal red overall.
***
#### FIC / in-flight update

- Ask FIC: system timing/confidence, worst segment, bases/tops, ice layers/trend, convection motion, PIREPs, ALT/escape, next update; briefing does not transfer PIC responsibility.
- Before critical point: DEST/ALT METAR-TAF→SIGMET/AIRMET→PIREP→radar/lightning→fuel→decision. Predefine divert trigger; file useful PIREP.
- `M:` `UPDATE-FUEL-OPTIONS-DECIDE EARLY`.
***
#### Hard no-go / exit triggers — light GA

- Freezing rain/drizzle, embedded/line TS, severe icing/turbulence, runway below performance/braking needs, wind/shear beyond limits, ceiling/vis below legal or personal minima, no legal/suitable alternate, insufficient fuel/options.
- `!:` unexpected ice, worsening VMC, rising terrain under lowering ceiling, cell growth/line closure, fuel below divert plan ⇒ exit now.
***
#### INRAT weather question method

- `1` locate ETA/time window; `2` decode prevailing/change groups; `3` identify legal threshold; `4` include TEMPO/PROB/BECMG rule; `5` check GFA/AIRMET/SIGMET/NOTAM; `6` calculate wind/fuel/temperature; `7` select legal answer, then note operational risk.
- `T:` common distractors use wrong time, AGL vs ASL, BKN vs SCT, prevailing vs TEMPO, alternate vs landing minima.
***
#### Pebble

- weather scan `SYNOPTIC-GFA-HAZARDS-TERMINALS-PIREP-WINDS-RUNWAY-TREND` | METAR now / TAF terminal future / GFA regional | METAR cloud AGL; GFA heights ASL unless stated | ceiling=BKN/OVC/VV | `FM` permanent exact | `BECMG` gradual | `TEMPO <1h each/≤half` | alternate BECMG improve=end/deteriorate=start | TEMPO≥alt min / PROB≥landing min | FZ liquid=red | visible moisture+subzero surface=ice | TS avoid | XW 30°=.5/45°=.7/60°=.87 | observations worse than forecast=confidence↓ | many amber=red.

***
<!-- BEGIN GENERATED icingfluids -->
#### De-/anti-icing · FPD · HOT / Dégivrage · antigivrage

| Memory | Rule / example |
|---|---|
| De / Anti | De-icing removes contamination; anti-icing protects a clean surface temporarily. Clean-aircraft rule: CAR 602.11; ground fluid does not authorize flight in icing. |
| I / II / III / IV | I: thin, usually heated, orange, short protection. II: thickened, pale/yellow. III: thickened, lower-speed applications, bright yellow. IV: thickened, longer protection, green. Verify product/aircraft approval. |
| FPD / FDP | FPD = freezing-point depressant. FDP = flight duty period. ADF in fluid literature can mean aircraft deicing fluid, not the navigation receiver. |
| LOUT | Use the warmest limit: aerodynamic acceptance; freezing point +10°C (I) or +7°C (II/III/IV); for diluted thickened fluids, coldest published HOT temperature. |
| LOUT example | Type I: freezing point −30°C; aerodynamic limit −25°C → LOUT −20°C. OAT −22°C: too cold. Check aircraft skin temperature too. |
| HOT clock | Starts at BEGINNING of final fluid application. Two-step: start of anti-icing step, not completion. Product/dilution, temperature, precipitation/intensity determine table. |
| HOT judgement | HOT is an estimate, not assured protection. Fluid failure or changed conditions can end protection earlier. Expired HOT: approved inspection/re-treatment procedure; never automatic extra minutes. |
| Snow / Neige | Use TC snowfall-intensity/visibility table, including day/night and temperature. METAR −SN alone does not resolve very-light versus light HOT categories. |
| Annual tables | Use current winter 2026–27 HOT guidance and exact fluid table. No universal duration per type. Allowance-time rules for ice pellets/small hail differ from HOT. |
<!-- END GENERATED icingfluids -->

Shared additions reviewed 19 October 2026: [source editions and scope](../CONTENT_REVIEW.md#operational-additions--19-october-2026). Edit `data/formulas.json` and run `python3 scripts/build_all.py` for marked blocks.
