### WEATHER KNOWLEDGE CORE — AV-CAVE v0.1
`K` knowledge | `M` memory | `T` trap | `!` hazard | `F` formula | Canada PPL/CPL/INRAT
`RELEASE:` `STUDY-REF PROVISIONAL` | `SRC:` TC AIM 2026-1 + standard aviation meteorology | use current MET products for flight
***
#### Atmosphere / ISA

- ISA SL: `15°C`, `29.92 inHg /1013.25 hPa`, density `1.225 kg/m³`.
- Standard temp lapse ≈ `2°C/1000 ft` to tropopause.
- Pressure/density decrease with altitude; warm air less dense than cold air.
- `F:` ISA temp ≈ `15 - 2×altitude(1000 ft)`.
- `T:` ISA is a reference model, not forecast weather.
***
#### Pressure altitude / density altitude

- Pressure altitude = altitude with altimeter `29.92`.
- Density altitude = pressure altitude corrected for non-standard temperature.
- `F rough:` `DA ≈ PA + 120 × (OAT - ISA temp)` ft.
- High `PA + temp + humidity` ⇒ DA↑ ⇒ takeoff roll↑, climb↓, TAS for same IAS↑.
- `M:` `HOT-HIGH-HUMID = PERFORMANCE LOW`.
***
#### Temperature / dew point

- Dew point = temperature air must cool to reach saturation at constant pressure/water content.
- Small `T-Td` spread + cooling ⇒ fog/low cloud increasingly likely.
- Temperature inversion = temp increases with height; strongly stable, traps haze/smoke, can create wind shear.
- `T:` small spread alone does not guarantee fog.
***
#### Lapse rates / stability

- `DALR` unsaturated ≈ `3°C/1000 ft`.
- `SALR` saturated ≈ `1.5°C/1000 ft` average; varies with temp/moisture.
- Environment cools faster than DALR ⇒ absolutely unstable.
- Environment cools slower than SALR / inversion ⇒ absolutely stable.
- Between SALR/DALR ⇒ conditionally unstable.
- Stable: stratiform cloud, smooth air, poor vis, steady precip.
- Unstable: CU/TCU/CB, turbulence, showers, generally better between-cloud vis.
- `M:` steep lapse = vertical motion grows.
***
#### Moisture / cloud formation

- Need moisture + cooling to saturation.
- Cooling mechanisms: lifting, radiation, contact/advection, mixing.
- Lift: convection, fronts, terrain, convergence.
- Condensation nuclei help droplets form.
- Cloud base often near LCL; rising unsaturated air cools DALR until saturated, then SALR.
***
#### Cloud families

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
#### Fog

- **Radiation:** clear/light wind/moist ground/night cooling; burns with heating/mixing.
- **Advection:** moist air over colder surface; needs wind; can persist.
- **Upslope:** moist air forced uphill and cooled.
- **Steam:** cold air over warmer water.
- **Precipitation/frontal:** rain evaporates into cooler air.
- **Ice fog:** very cold air, ice crystals.
- `M:` radiation = cooling ground; advection = moving moist air.
***
#### Visibility

- Reduced by fog, mist, haze, smoke, dust, precip, blowing snow.
- Stable air tends to trap contaminants; unstable mixing often improves general visibility.
- `!:` whiteout = no discernible horizon/terrain cues over snow/cloud; visual attitude/height judgment can disappear.
***
#### Air masses

- Classified by moisture/source: continental `c` dry, maritime `m` moist; Arctic/Polar/Tropical temp source.
- Weather changes as air mass moves over warmer/colder/moister terrain.
- Cold air over warm surface ⇒ instability/showers.
- Warm air over cold surface ⇒ stability/fog/stratus.
***
#### Pressure systems

- Northern Hemisphere:
  - Low: counter-clockwise + inward, rising air, cloud/precip.
  - High: clockwise + outward, sinking air, often fair/stable.
- Trough = elongated low pressure, often wind shift/cloud/showers.
- Ridge = elongated high pressure, generally more stable.
- Closely spaced isobars ⇒ stronger pressure-gradient wind.
***
#### Wind

- Pressure-gradient force drives high→low.
- Coriolis deflects right in Northern Hemisphere; increases with latitude/speed.
- Aloft, pressure gradient + Coriolis ≈ geostrophic/gradient flow, roughly parallel isobars.
- Surface friction slows wind ⇒ Coriolis↓ ⇒ wind crosses isobars toward low.
- `M:` surface wind angles **into LOW / out of HIGH**.
***
#### Local winds

- Sea breeze day: sea→land; land breeze night: land→sea.
- Valley/anabatic day: upslope/up-valley.
- Mountain/katabatic night: downslope/down-valley.
- Funnel/terrain effects can accelerate and redirect wind.
- `T:` airport wind may differ sharply from ridge/pass/valley wind.
***
#### Fronts

[CF / WF · bilingual CAVE reader](../readers/Weather_Fronts_EN_FR.html) · [EN/FR study card](Weather_Fronts_EN_FR.md)

- **Cold:** cold undercuts warm; steeper/narrower; CU/CB, showers, gusts, turbulence, fast wind shift.
- **Warm:** warm overruns cold; broad layered cloud; lowering ceilings, steady precip, icing/FZRA risk.
- **Stationary:** little movement; prolonged cloud/precip.
- **Occluded:** cold front catches warm front; extensive mixed frontal weather.
- `M cold:` `fast-steep-convective`.
- `M warm:` `slow-wide-layered`.
***
#### CF — before / passing / after

- `K:` surface passage at one location; typical NH mid-latitude low, south of centre. Wind = FROM; directions illustrative.

| Element | Before | Passing | After |
|---|---|---|---|
| Pressure | ↓ | minimum → sharp ↑ | ↑, then levels |
| T / Td | warm / relatively high | T↓; Td usually↓ | colder / usually drier |
| Wind | S–SW; may strengthen | veers W–NW; gusts/squalls | W–NW; often gusty, later eases |
| Cloud | CU/TCU; CB if unstable | TCU/CB band; low ragged cloud | CU/SC; clearing trend |
| Precip | SH/TS may precede | brief heavy SH ± TS/hail | showers, then easing |
| CIG / VIS | deteriorate near band | low CIG / poor in precip | improve between showers |
| `!` | prefrontal squall line possible | turbulence / shear / icing / TS | gusts / turbulence; snow squalls possible |

- `M:` CF = `T↓ Td↓ P↑ WIND VEERS`.
- `T:` stable/slow CF may give layered cloud + prolonged precip; passage ≠ instant clearing.
***
#### WF — before / passing / after

| Element | Before | Passing | After |
|---|---|---|---|
| Pressure | steady ↓ | fall slows → levels | ~steady / slight ↑; may ↓ toward next low/CF |
| T / Td | cool / Td tends ↑ | T↑; Td steady→↑ | warmer / moist, Td higher |
| Wind | E–SE | veers toward S; variable near boundary | S–SW; speed varies |
| Cloud | Ci → Cs → As → Ns; St/fog below | low St / fog | St/SC; may lift/break; CB if unstable |
| Precip | widespread steady RA/SN; PL/FZRA possible | RA/DZ; may ease | often eases; DZ/SH may persist |
| CIG / VIS | progressively ↓ | often low / poor | usually improve; low cloud/haze/fog may persist |
| `!` | icing / embedded CB; FZRA if warm layer over subzero surface | low CIG / fog / shear | warm-sector low cloud / fog; possible TS |

- `M:` WF = `LAYERS LOWER → T↑ Td↑ WIND VEERS; P FALL STOPS`.
- `T:` tendencies, not guarantees: track/terrain/stability/season modify sequence. Both fronts can have CB; WF ≠ guaranteed clearing or strong P rise.
- `SRC:` [FAA PHAK — Weather Theory, Fronts (NWS-hosted)](https://www.weather.gov/media/zhu/ZHU_Training_Page/Met_Tutorials/Weather_Theory.pdf); [NWS — frontal analysis / pressure tendencies](https://www.weather.gov/media/zhu/ZHU_Training_Page/Met_Tutorials/AF-Trainee.pdf).
***
#### Typical warm-front sequence

- `Ci → Cs → As → Ns → St/fog`, ceilings lower and precip increases approaching front.
- Warm-layer-over-subfreezing-surface setup can produce `FZRA/PL`.
***
#### Precipitation

- Droplets/crystals grow by collision/coalescence or ice-crystal process.
- `RA` liquid; `DZ` tiny droplets; `SN`; `PL` ice pellets; `FZRA/FZDZ` supercooled liquid freezing on contact.
- `!:` freezing rain/drizzle = high-severity icing signal.
- Virga = precip evaporates before ground; may indicate downdrafts/microburst potential.
***
#### Structural icing

- Requires visible moisture + aircraft surface at/below freezing.
- **Rime:** small supercooled drops, rapid freeze, rough/opaque.
- **Clear:** larger drops, slower freeze/spread, smooth/heavy.
- **Mixed:** combination.
- Effects: lift↓, drag↑, stall speed↑, climb↓; prop/intake/static/control contamination.
- `!:` freezing rain/drizzle and severe icing require immediate escape.
- `T:` `OAT >0°C` at surface says nothing about cloud icing aloft.
***
#### Carburetor icing

- Fuel vaporization + venturi pressure drop can cool carb throat well below OAT.
- Possible even in warm weather; risk high with humidity and partial power.
- Fixed-pitch clue: RPM↓ then roughness.
- Apply carb heat per POH; initial RPM drop/roughness may worsen while ice melts.
- `T:` carb icing ≠ structural icing.
***
#### Thunderstorms — ingredients

- Moisture + instability + lift.
- Stages:
  1. **Cumulus:** updrafts only.
  2. **Mature:** up + downdrafts; precip; maximum hazards.
  3. **Dissipating:** downdrafts dominate.
- Hazards: extreme turbulence, hail, lightning, heavy precip, icing, tornado, wind shear/microburst.
- `!:` avoid; never use a visual/radar “gap” to thread active cells.
***
#### Microburst / LLWS

- Microburst = concentrated downdraft spreading outward at surface.
- Aircraft may see: headwind/IAS↑ → downdraft → tailwind/IAS↓.
- Most dangerous low during takeoff/landing.
- Virga, heavy showers, gust fronts and TS are clues.
- `M:` gain first can precede severe loss.
***
#### Turbulence

- Mechanical: wind over terrain/buildings; strongest low/lee side.
- Convective: thermal/CU/TS.
- Frontal: wind/shear + convection.
- Mountain wave/rotor: strong stable cross-ridge flow.
- CAT: often near jet stream/strong wind shear, without cloud.
- `T:` turbulence intensity depends on aircraft response; same air mass affects light aircraft more.
***
#### Mountain wave

- Favoured by strong wind roughly perpendicular to ridge + stable layer.
- Smooth wave aloft; severe rotor/turbulence below/lee; strong up/downdrafts.
- Lenticular `ACSL` = wave clue; rotor cloud may mark turbulence.
- `!:` downdraft may exceed climb capability.
***
#### Wind shear

- Rapid wind speed/direction change over short distance.
- Sources: fronts, inversions/low-level jets, terrain, TS/microbursts.
- Low-level shear changes IAS/flight path quickly near ground.
- `T:` surface wind can look acceptable while shear above is severe.
***
#### Jet stream / CAT

- Narrow band of strong upper wind near tropopause, usually strongest horizontal temp gradient.
- CAT favoured near jet core/shear zones, especially bends/entrance/exit regions.
- Jet position helps locate fronts/system movement.
***
#### Freezing level

- Altitude where `0°C`; may be multiple levels with inversions.
- Freezing level ≠ guaranteed icing layer; requires moisture.
- Cloud + subzero temp + PIREP/AIRMET icing = stronger evidence.
***
#### Altimetry / pressure traps

- From high pressure→low without reset: true altitude lower than indicated.
- Warm→cold: true altitude lower than indicated.
- `M:` `HIGH→LOW / HOT→COLD = LOOK OUT BELOW`.
- Cold temperature increases obstacle/terrain error; apply published corrections where required.
***
#### Density / TAS

- For same IAS, TAS rises with altitude as density falls.
- Rule-of-thumb TAS ≈ `IAS + ~2% per 1000 ft` in lower atmosphere.
- Higher TAS at same IAS ⇒ larger turn radius and more ground distance during manoeuvre.
***
#### Weather trend logic

- Observation = **now**; forecast = **expected**; trend = whether expectation is occurring.
- Compare several METAR/SPECI, not one snapshot.
- Falling ceiling/vis + pressure + increasing wind/precip often signals approaching system deterioration.
- `T:` forecast confidence drops when observations repeatedly diverge.
***
#### Canadian product memory

- `METAR/SPECI` observed aerodrome conditions.
- `TAF` terminal forecast.
- `GFA` regional cloud/weather + icing/turb/freezing level.
- `AIRMET` significant lower-severity/unforecast hazard.
- `SIGMET` significant hazardous weather.
- `PIREP` actual pilot-observed conditions.
- METAR/TAF cloud heights = AGL; GFA heights generally ASL unless stated.
- `T:` use the separate Weather Decoding / Go-No-Go QRC for exact code/timing/alternate logic.
***
#### Exam traps

- Stable ≠ “good”: can mean fog/stratus/poor vis/icing.
- Unstable ≠ “bad everywhere”: often better vis between showers but more turbulence/CB.
- Warm front generally broader/layered; cold front narrower/convective.
- Dew-point spread predicts saturation risk, not certainty.
- Freezing level alone does not equal icing.
- Wind direction aloft/surface differs due friction.
- Density altitude is a performance concept, not an indicated instrument altitude.
- Cloud base units: METAR AGL vs GFA ASL.
***
#### Pebble

- ISA `15°C /29.92 / -2°C per1000`
- DA `≈ PA +120×ΔT`
- DALR `3°/1000`; SALR `~1.5°/1000`
- stable=`STRATUS-SMOOTH-POOR VIS`; unstable=`CU-TURB-SHOWERS`
- low=`CCW-IN-RISE`; high=`CW-OUT-SINK`
- cold front=`FAST-STEEP-CU`; warm=`SLOW-WIDE-LAYERED`
- fog `RAD COOL / ADVECT MOVE / UPSLOPE LIFT`
- icing=`MOISTURE + ≤0 SURFACE`; `FZRA/FZDZ RED`
- TS=`MOISTURE+INSTABILITY+LIFT`; mature=worst
- microburst=`IAS↑ then ↓`
- `HIGH→LOW / HOT→COLD = BELOW`
- METAR/TAF AGL; GFA usually ASL.
