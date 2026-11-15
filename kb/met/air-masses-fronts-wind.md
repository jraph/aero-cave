# Air masses, fronts, pressure systems & wind / Masses d’air, fronts, systèmes de pression et vent
<!-- concept: met-systems | level: PPL CPL IR -->

[Meteorology index / Index météo](README.md) · concept `met-systems` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Air masses
<!-- id: wx-air-masses | from: 16 -->

- Classified by moisture/source: continental `c` dry, maritime `m` moist; Arctic/Polar/Tropical temp source.
- Weather changes as air mass moves over warmer/colder/moister terrain.
- Cold air over warm surface ⇒ instability/showers.
- Warm air over cold surface ⇒ stability/fog/stratus.
***
#### Pressure systems
<!-- id: wx-pressure-systems | from: 16 -->

- Northern Hemisphere:
  - Low: counter-clockwise + inward, rising air, cloud/precip.
  - High: clockwise + outward, sinking air, often fair/stable.
- Trough = elongated low pressure, often wind shift/cloud/showers.
- Ridge = elongated high pressure, generally more stable.
- Closely spaced isobars ⇒ stronger pressure-gradient wind.
***
#### Wind
<!-- id: wx-wind | from: 16 -->

- Pressure-gradient force drives high→low.
- Coriolis deflects right in Northern Hemisphere; increases with latitude/speed.
- Aloft, pressure gradient + Coriolis ≈ geostrophic/gradient flow, roughly parallel isobars.
- Surface friction slows wind ⇒ Coriolis↓ ⇒ wind crosses isobars toward low.
- `M:` surface wind angles **into LOW / out of HIGH**.
***
#### Local winds
<!-- id: wx-local-winds | from: 16 -->

- Sea breeze day: sea→land; land breeze night: land→sea.
- Valley/anabatic day: upslope/up-valley.
- Mountain/katabatic night: downslope/down-valley.
- Funnel/terrain effects can accelerate and redirect wind.
- `T:` airport wind may differ sharply from ridge/pass/valley wind.
***
#### Fronts
<!-- id: wx-fronts | from: 16, 05 -->

- **Cold:** cold undercuts warm; steeper/narrower; CU/CB, showers, gusts, turbulence, fast wind shift.
- **Warm:** warm overruns cold; broad layered cloud; lowering ceilings, steady precip, icing/FZRA risk.
- **Stationary:** little movement; prolonged cloud/precip.
- **Occluded:** cold front catches warm front; extensive mixed frontal weather.
- `M cold:` `fast-steep-convective`.
- `M warm:` `slow-wide-layered`.
- `T:` timing errors can rapidly change runway/wind/CIG; fog may form after departure.
***
#### CF — before / passing / after
<!-- id: wx-cold-front | from: 16 -->

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
<!-- id: wx-warm-front | from: 16 -->

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
<!-- id: wx-warm-front-sequence | from: 16 -->

- `Ci → Cs → As → Ns → St/fog`, ceilings lower and precip increases approaching front.
- Warm-layer-over-subfreezing-surface setup can produce `FZRA/PL`.
***
#### Front formation, trowal, upper fronts
<!-- id: wx-front-formation-trowal-upper-fronts | level: CPL -->

- Cold front = transition zone where cold air **advances and replaces** warm air. Forms as cold dense air wraps cyclonically (counter-clockwise) around a developing low, undercuts warm moist air → lift → often convective cloud and precipitation. Weakens as the low occludes.
- **Occlusion**: cold front overtakes warm front (fronts move at different speeds); warm air lifted aloft.
- **Trowal** (trough of warm air aloft): mid-level ribbon of warm air lifted over cooler air after occlusion → **elevated convective precipitation**, low visibility, heavy accumulation; winter: **freezing precipitation** at low levels beneath it. Chart: trowal symbol (red/blue hooks on Canadian surface charts) marks the weather aloft, not surface winds.
- **Upper front**: front aloft not reaching the surface (dashed on surface charts); turbulence possible in an upper cold front.
- `?:` frontogenesis (front forming/strengthening) / frontolysis (weakening/dissipating): standard meteorology terms, not found in a TC/NAV CANADA text.

- Sources: [NAV CANADA AvMet: cold front](https://avmet.navcanada.ca/en/cold-front.aspx), [trowal](https://avmet.navcanada.ca/en/trowal.aspx); [TC AIM MET](https://tc.canada.ca/sites/default/files/2026-10/aim-2026-2_met_en.pdf) 10.0.
***
#### Centrifugal force and gradient wind
<!-- id: wx-centrifugal-force-gradient-wind | level: CPL -->

- Around curved isobars, centrifugal force adds to the pressure-gradient / Coriolis balance → **gradient wind**.
- **Low** (cyclonic): centrifugal force acts with Coriolis against pressure gradient → wind **slower** than geostrophic for the same isobar spacing. **High** (anticyclonic): wind **faster** than geostrophic.
- `T` Same isobar spacing ≠ same wind around a high and a low.
- `?:` general knowledge; no free TC or NAV CANADA text found. Check against a TC-recognized text (e.g. *From the Ground Up*, TC Flight Training Manual) in the fact-check pass.


***
#### Pebble
<!-- id: met-systems-pebble -->

- AIR MASS `c dry / m moist; Arctic/Polar/Tropical | cold air over warm surface → instability/showers | warm air over cold surface → stability/fog/stratus`
- PRESSURE (NH) `low = CCW-IN-RISE, cloud/precip | high = CW-OUT-SINK | trough → wind shift/cloud/showers | closely spaced isobars → stronger wind`
- WIND `pressure gradient high→low | Coriolis deflects right (NH) | aloft ≈ parallel isobars | surface friction → wind crosses isobars toward low`
- LOCAL `sea breeze day sea→land; land breeze night land→sea | anabatic day upslope; katabatic night downslope`
- COLD FRONT `FAST-STEEP-CU | T↓ Td↓ P↑ WIND VEERS | passage ≠ instant clearing`
- WARM FRONT `SLOW-WIDE-LAYERED | Ci→Cs→As→Ns→St/fog | T↑ Td↑ WIND VEERS; P FALL STOPS | FZRA/PL if warm layer over subfreezing surface`
- T `tendencies, not guarantees | both fronts can have CB`
- FRONTS `cold front: cold replaces warm, undercuts | occlusion: cold overtakes warm | TROWAL: warm air aloft → heavy elevated precip, FZ precip below | upper front dashed, turbulence`
- GRADIENT WIND `centrifugal force on curved flow | low: < geostrophic | high: > geostrophic`
***
