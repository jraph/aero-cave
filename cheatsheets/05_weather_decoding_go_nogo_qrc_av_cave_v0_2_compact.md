### WEATHER DECODING / GO-NO-GO QRC — AV-CAVE v0.2 COMPACT
`TARGETED CPAER REVIEW: 2026-09-06` | see `00_CPAER_REVIEW_NOTES.md` for scope and remaining gaps
`P` procedure | `R` rule | `F` formula | `T` trap | `M` memory | `!` safety | `?` verify | Canada PPL/CPL/INRAT/IR
`RELEASE:` `STUDY/OPS-REF PROVISIONAL` | `NOT FLIGHT AUTHORITY`
`MOVED 2026-11-14:` knowledge sections now live in concept files under [`kb/met/`](../kb/met/README.md); headings below are kept as pointers so saved links still land. Go/no-go flows and gates remain here.
***
#### Source / master scan
<!-- id: wxp-master-scan -->

- `SRC:` current AIM MET + NAV CANADA/FIC + CARs/CAP/CFS/NOTAM. Products describe; PIC decides legal + safe.
- Review GFA/AIRMET/SIGMET→TAF/METAR/SPECI→PIREP/upper winds→radar/satellite/lightning→RSC/CRFI/cameras.
- `P:` big picture→route→DEP/enroute/DEST/ALT→escape→update. `M:` `SYNOPTIC-GFA-HAZARDS-TERMINALS-PIREP-WINDS-RUNWAY-TREND`.
- `T:` never one product: decode→compare→trend→threats→options.
***
#### Go/no-go gates
<!-- id: wxp-gates -->

- `LEGAL:` minima/alternate/approach ban/fuel/equipment/day-night.
- `AIRCRAFT:` icing approval/wind-XW/runway/performance/terrain/heat-defrost.
- `PILOT:` currency/recent IMC-night-XW-ice/fatigue/workload. `OPTIONS:` alternates/turn-back/fuel/route-alt-time.
- `T:` legal + no options = fragile.
***
#### Product roles

→ Moved / Déplacé : [Weather products & decoding / Produits météo et décodage](../kb/met/weather-products.md#product-roles)
***
#### METAR / SPECI scan

→ Moved / Déplacé : [METAR / SPECI](../kb/met/metar.md#metar--speci-scan)
***
#### Wind decoding

→ Moved / Déplacé : [METAR / SPECI](../kb/met/metar.md#wind-decoding)
***
#### Visibility / RVR

→ Moved / Déplacé : [METAR / SPECI](../kb/met/metar.md#visibility--rvr)
***
#### Weather codes

→ Moved / Déplacé : [METAR / SPECI](../kb/met/metar.md#weather-codes)
***
#### Cloud groups

→ Moved / Déplacé : [METAR / SPECI](../kb/met/metar.md#cloud-groups)
***
#### Temperature / dew point

→ Moved / Déplacé : [METAR / SPECI](../kb/met/metar.md#temperature--dew-point)
***
#### Altimeter / pressure trend

→ Moved / Déplacé : [METAR / SPECI](../kb/met/metar.md#altimeter--pressure-trend)
***
#### TAF scan / groups

→ Moved / Déplacé : [TAF](../kb/met/taf.md#taf-scan--groups)
***
#### TAF alternate / risk

→ Moved / Déplacé : [TAF](../kb/met/taf.md#taf-alternate--risk)
***
#### GFA

→ Moved / Déplacé : [GFA, SIGMET / AIRMET, PIREP & upper winds / GFA, SIGMET / AIRMET, PIREP et vents en altitude](../kb/met/gfa-sigmet-pirep-winds.md#gfa)
***
#### AIRMET / SIGMET / PIREP

→ Moved / Déplacé : [GFA, SIGMET / AIRMET, PIREP & upper winds / GFA, SIGMET / AIRMET, PIREP et vents en altitude](../kb/met/gfa-sigmet-pirep-winds.md#airmet--sigmet--pirep)
***
#### Upper winds / temperature

→ Moved / Déplacé : [GFA, SIGMET / AIRMET, PIREP & upper winds / GFA, SIGMET / AIRMET, PIREP et vents en altitude](../kb/met/gfa-sigmet-pirep-winds.md#upper-winds--temperature)
***
#### Stability / fronts / fog

→ Moved / Déplacé : [Air masses, fronts, pressure systems & wind / Masses d’air, fronts, systèmes de pression et vent](../kb/met/air-masses-fronts-wind.md#stability--fronts--fog)
***
#### Icing gate

→ Moved / Déplacé : [Icing / Givrage](../kb/met/icing.md#icing-gate)
***
#### Carburetor icing

→ Moved / Déplacé : [Carburettor icing & induction / Givrage du carburateur et admission](../kb/met/carburettor-icing.md#carburetor-icing--qrc)
***
#### Convection gate

→ Moved / Déplacé : [Thunderstorms & convection / Orages et convection](../kb/met/thunderstorms.md#convection-gate)
***
#### LLWS / microburst

→ Moved / Déplacé : [Turbulence, wind shear & mountain wave / Turbulence, cisaillement et ondes orographiques](../kb/met/turbulence-wind-shear.md#llws--microburst)
***
#### Turbulence

→ Moved / Déplacé : [Turbulence, wind shear & mountain wave / Turbulence, cisaillement et ondes orographiques](../kb/met/turbulence-wind-shear.md#turbulence--qrc)
***
#### Wind / runway gate
<!-- id: wxp-wind-runway -->

- Compute steady + gust XW/HW/TW; compare POH/SOP/personal limits.
- Add runway length/slope/surface/RSC/CRFI, obstacles, mechanical turbulence, wind shear.
- `T:` gusty XW + wet/contaminated short runway = compounded risk, not separate minor issues.
***
#### Snow / freezing precipitation

→ Moved / Déplacé : [Icing / Givrage](../kb/met/icing.md#snow--freezing-precipitation)
***
#### Mountain / terrain weather

→ Moved / Déplacé : [Turbulence, wind shear & mountain wave / Turbulence, cisaillement et ondes orographiques](../kb/met/turbulence-wind-shear.md#mountain--terrain-weather)
***
#### Night weather
<!-- id: wxp-night -->

- Raise minima for cloud/vis/terrain/precip. Horizon and cloud boundaries disappear; snow/black-hole effects worsen.
- Moon illumination, terrain lighting and cloud cover affect visual navigation.
- `T:` legal night VFR visibility may provide poor terrain/weather avoidance.
***
#### VFR go/no-go flow
<!-- id: wxp-vfr-flow -->

- `P:` ceiling/vis trend→terrain clearance→cloud layers/tops→precip/TS→wind/XW→daylight/night→diversion airports→fuel.
- Establish personal minimums by day/night, terrain, route familiarity and passenger pressure.
- `T:` scud running = shrinking options; turn around before valley/ceiling closes.
***
#### IFR go/no-go flow
<!-- id: wxp-ifr-flow -->

- `P:` departure minima/ODP→enroute MEA/icing/TS→destination TAF/RVR/wind→alternate legality→approach/runway/NOTAM→missed/climb→fuel/options.
- Single-engine IFR: terrain/icing/engine-failure landing options. Multi-engine: actual OEI climb/ceiling.
- `T:` legal approach at destination + unusable alternate + icing enroute = no robust plan.
***
#### Trend
<!-- id: wxp-trend -->

- Compare last `3` METAR/SPECI + TAF + GFA panels + radar/satellite + PIREPs; mark CIG/vis/wind/pressure `↑/↓` and precip/cell motion.
- `M:` observation=now; forecast=expected; trend=forecast performance. Worse observations→confidence↓.
***
#### Personal weather matrix
<!-- id: wxp-personal-matrix -->

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
<!-- id: wxp-fic -->

- Ask FIC: system timing/confidence, worst segment, bases/tops, ice layers/trend, convection motion, PIREPs, ALT/escape, next update; briefing does not transfer PIC responsibility.
- Before critical point: DEST/ALT METAR-TAF→SIGMET/AIRMET→PIREP→radar/lightning→fuel→decision. Predefine divert trigger; file useful PIREP.
- `M:` `UPDATE-FUEL-OPTIONS-DECIDE EARLY`.
***
#### Hard no-go / exit triggers — light GA
<!-- id: wxp-hard-no-go -->

- Freezing rain/drizzle, embedded/line TS, severe icing/turbulence, runway below performance/braking needs, wind/shear beyond limits, ceiling/vis below legal or personal minima, no legal/suitable alternate, insufficient fuel/options.
- `!:` unexpected ice, worsening VMC, rising terrain under lowering ceiling, cell growth/line closure, fuel below divert plan ⇒ exit now.
***
#### INRAT weather question method
<!-- id: wxp-inrat-method -->

- `1` locate ETA/time window; `2` decode prevailing/change groups; `3` identify legal threshold; `4` include TEMPO/PROB/BECMG rule; `5` check GFA/AIRMET/SIGMET/NOTAM; `6` calculate wind/fuel/temperature; `7` select legal answer, then note operational risk.
- `T:` common distractors use wrong time, AGL vs ASL, BKN vs SCT, prevailing vs TEMPO, alternate vs landing minima.
***
#### Pebble
<!-- id: wxp-pebble -->

- weather scan `SYNOPTIC-GFA-HAZARDS-TERMINALS-PIREP-WINDS-RUNWAY-TREND` | METAR now / TAF terminal future / GFA regional | METAR cloud AGL; GFA heights ASL unless stated | ceiling=BKN/OVC/VV | `FM` permanent exact | `BECMG` gradual | `TEMPO <1h each/≤half` | alternate BECMG improve=end/deteriorate=start | TEMPO≥alt min / PROB≥landing min | FZ liquid=red | visible moisture+subzero surface=ice | TS avoid | XW 30°=.5/45°=.7/60°=.87 | observations worse than forecast=confidence↓ | many amber=red.
***
#### De-/anti-icing · FPD · HOT / Dégivrage · antigivrage

→ Moved / Déplacé : [Ground de-/anti-icing & clean aircraft / Dégivrage / antigivrage au sol et aéronef propre](../kb/met/ground-deicing.md#de-anti-icing--fpd--hot--dégivrage--antigivrage)
