### WEATHER DECODING / GO-NO-GO QRC — AV-CAVE v0.2 COMPACT
`TARGETED CPAER REVIEW: 2026-09-06` | see `00_CPAER_REVIEW_NOTES.md` for scope and remaining gaps
`P` procedure | `R` rule | `F` formula | `T` trap | `M` memory | `!` safety | `?` verify | Canada PPL/CPL/INRAT/IR
`RELEASE:` `STUDY/OPS-REF PROVISIONAL` | `NOT FLIGHT AUTHORITY`
`MOVED 2026-11-14:` knowledge sections now live in concept files under [`kb/met/`](../kb/met/README.md); go/no-go flows and gates remain here.
***
#### Source / master scan
<!-- id: wxp-master-scan | concepts: met-products | kind: source | level: PPL CPL IR -->

- `SRC:` current AIM MET + NAV CANADA/FIC + CARs/CAP/CFS/NOTAM. Products describe; PIC decides legal + safe.
- Review GFA/AIRMET/SIGMET→TAF/METAR/SPECI→PIREP/upper winds→radar/satellite/lightning→RSC/CRFI/cameras.
- `P:` big picture→route→DEP/enroute/DEST/ALT→escape→update. `M:` `SYNOPTIC-GFA-HAZARDS-TERMINALS-PIREP-WINDS-RUNWAY-TREND`.
- `T:` never one product: decode→compare→trend→threats→options.
***
#### Go/no-go gates
<!-- id: wxp-gates | concepts: met-decide | level: PPL CPL IR -->

- `LEGAL:` minima/alternate/approach ban/fuel/equipment/day-night.
- `AIRCRAFT:` icing approval/wind-XW/runway/performance/terrain/heat-defrost.
- `PILOT:` currency/recent IMC-night-XW-ice/fatigue/workload. `OPTIONS:` alternates/turn-back/fuel/route-alt-time.
- `T:` legal + no options = fragile.
***
#### Wind / runway gate
<!-- id: wxp-wind-runway | concepts: met-decide | level: PPL CPL IR -->

- Compute steady + gust XW/HW/TW; compare POH/SOP/personal limits.
- Add runway length/slope/surface/RSC/CRFI, obstacles, mechanical turbulence, wind shear.
- `T:` gusty XW + wet/contaminated short runway = compounded risk, not separate minor issues.
***
#### Night weather
<!-- id: wxp-night | concepts: met-decide, law-night | level: PPL CPL IR -->

- Raise minima for cloud/vis/terrain/precip. Horizon and cloud boundaries disappear; snow/black-hole effects worsen.
- Moon illumination, terrain lighting and cloud cover affect visual navigation.
- `T:` legal night VFR visibility may provide poor terrain/weather avoidance.
***
#### VFR go/no-go flow
<!-- id: wxp-vfr-flow | concepts: met-decide | level: PPL CPL -->

- `P:` ceiling/vis trend→terrain clearance→cloud layers/tops→precip/TS→wind/XW→daylight/night→diversion airports→fuel.
- Establish personal minimums by day/night, terrain, route familiarity and passenger pressure.
- `T:` scud running = shrinking options; turn around before valley/ceiling closes.
***
#### IFR go/no-go flow
<!-- id: wxp-ifr-flow | concepts: met-decide, ifr-plan, ifr-wx | level: IR -->

- `P:` departure minima/ODP→enroute MEA/icing/TS→destination TAF/RVR/wind→alternate legality→approach/runway/NOTAM→missed/climb→fuel/options.
- Single-engine IFR: terrain/icing/engine-failure landing options. Multi-engine: actual OEI climb/ceiling.
- `T:` legal approach at destination + unusable alternate + icing enroute = no robust plan.
***
#### Trend
<!-- id: wxp-trend | concepts: met-decide | level: PPL CPL IR -->

- Compare last `3` METAR/SPECI + TAF + GFA panels + radar/satellite + PIREPs; mark CIG/vis/wind/pressure `↑/↓` and precip/cell motion.
- `M:` observation=now; forecast=expected; trend=forecast performance. Worse observations→confidence↓.
***
#### Personal weather matrix
<!-- id: wxp-personal-matrix | concepts: met-decide | level: PPL CPL IR -->

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
<!-- id: wxp-fic | concepts: met-products | level: PPL CPL IR -->

- Ask FIC: system timing/confidence, worst segment, bases/tops, ice layers/trend, convection motion, PIREPs, ALT/escape, next update; briefing does not transfer PIC responsibility.
- Before critical point: DEST/ALT METAR-TAF→SIGMET/AIRMET→PIREP→radar/lightning→fuel→decision. Predefine divert trigger; file useful PIREP.
- `M:` `UPDATE-FUEL-OPTIONS-DECIDE EARLY`.
***
#### Hard no-go / exit triggers — light GA
<!-- id: wxp-hard-no-go | concepts: met-decide | level: PPL CPL IR -->

- Freezing rain/drizzle, embedded/line TS, severe icing/turbulence, runway below performance/braking needs, wind/shear beyond limits, ceiling/vis below legal or personal minima, no legal/suitable alternate, insufficient fuel/options.
- `!:` unexpected ice, worsening VMC, rising terrain under lowering ceiling, cell growth/line closure, fuel below divert plan ⇒ exit now.
***
#### INRAT weather question method
<!-- id: wxp-inrat-method | concepts: ifr-wx | kind: trap | level: IR -->

- `1` locate ETA/time window; `2` decode prevailing/change groups; `3` identify legal threshold; `4` include TEMPO/PROB/BECMG rule; `5` check GFA/AIRMET/SIGMET/NOTAM; `6` calculate wind/fuel/temperature; `7` select legal answer, then note operational risk.
- `T:` common distractors use wrong time, AGL vs ASL, BKN vs SCT, prevailing vs TEMPO, alternate vs landing minima.
***
#### Pebble
<!-- id: wxp-pebble | concepts: met | kind: pebble | level: PPL CPL IR -->

- weather scan `SYNOPTIC-GFA-HAZARDS-TERMINALS-PIREP-WINDS-RUNWAY-TREND` | gates `LEGAL-AIRCRAFT-PILOT-OPTIONS`; legal + no options = fragile | observations worse than forecast=confidence↓ | many amber=red | `UPDATE-FUEL-OPTIONS-DECIDE EARLY` | scud running = shrinking options; turn around early | decoding and hazard recall: concept Pebbles in `kb/met/`.
***
