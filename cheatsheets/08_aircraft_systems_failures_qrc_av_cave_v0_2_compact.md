### AIRCRAFT SYSTEMS / FAILURES QRC — AV-CAVE v0.2 COMPACT
`TARGETED CPAER REVIEW: 2026-09-06` | see `00_CPAER_REVIEW_NOTES.md` for scope and remaining gaps
`P` procedure | `S` symptom | `T` trap | `M` memory | `!` safety | `?` verify | trainer/light-aircraft generic; POH/AFM/SOP wins
`RELEASE:` `STUDY / AIRCRAFT-DEPENDENT` | `NOT FLIGHT AUTHORITY`
***
#### Source / discipline / scan

- `SRC:` exact POH/AFM §3 + systems, current checklist/SOP; FTM/TP guidance.
- Memorize only aircraft-designated memory items; abnormal checklists normally read-and-do.
- `P:` control→power/sound→fuel→oil→electrical→pitot/static/gyro→controls/config→smoke/fire/odour; confirm instrument failure with `≥2` independent indications.
- `M:` `CONTROL-DIAGNOSE-MEMORY-CHECKLIST-DECLARE-LAND` | `POWER-FUEL-OIL-ELECTRIC-AIR-DIRECTION-CONTROLS`.
- `T:` preserve control/landing options; same symptom may have several causes.
***
#### Engine essentials

- Piston engine needs: air + fuel + ignition + compression + correct timing.
- Power loss scan: throttle/mixture/carb heat/fuel selector/quantity/primer/mags/boost pump as installed.
- `M:` `AIR-FUEL-SPARK-COMPRESSION`.
- `T:` partial power may be temporary. Keep a landing area continuously available.
***
#### Magnetos / ignition

- Mags are battery/alternator-independent; dual mags/plugs add redundancy/efficiency. Engine running with master OFF is normal.
- One-mag roughness: plug fouling, mag/lead or mixture. `!:` bad P-lead can leave mag live—moving prop may start engine.
- `T:` electrical failure may spare engine but remove radios/lights/flaps/gear/instruments.
***
#### Magneto roughness in flight

- `P:` control→mixture adjust→carb heat as appropriate→select mags individually briefly per POH→return BOTH if worse→land/divert.
- `T:` switching to OFF in flight may load exhaust with fuel; returning to BOTH can cause backfire/damage. Follow POH.
- `!:` severe vibration/power loss/fire indications = treat as engine emergency, not merely a mag check.
***
#### Mixture

- Too rich: rough/fouling/high burn/power loss aloft; too lean: rough/power loss/high temps/detonation risk at high power.
- Lean by POH RPM/EGT/monitor method. `T:` full rich may be over-rich for high-DA TKOF.
***
#### Carburetor icing

- Can occur in moist air from about `-13°C to +38°C`; risk high in humid partial-power operation.
- `S:` fixed-pitch: unexplained RPM↓, then roughness/airspeed↓. Constant-speed: manifold pressure↓.
- `P:` full carb heat→expect initial power loss/roughness→leave full hot until ice clears→re-adjust power/mixture per POH.
- `M:` initial worse, then better = ice melting.
- `T:` partial heat without carb-air-temperature guidance may place air in icing range. Heated air is usually unfiltered and reduces power.
- `T:` structural icing conditions and carb-ice conditions are related but not identical.
***
#### Aviation fuel grades / FSII — L4

| Key | Recall |
|---|---|
| `T` OCTANE | AVGAS **antiknock/detonation resistance**, not fuel energy; **80/87 = lean/rich ratings**, likewise **100/130** (rich performance number >100 ≠ % octane). |
| `M` AVGAS | **80/87 RED** | **100/130 GREEN** | **100LL BLUE** (`LL` = low lead, **≠ unleaded**; rated 100 lean / 130 rich). |
| `M` JET A | Kerosene-type turbine fuel; **max freezing point −40°C**. |
| `M` JET A-1 | Kerosene-type turbine fuel; **max freezing point −47°C**. |
| `T` JET B | Wide-cut gasoline/kerosene-type turbine fuel, more volatile; fuel specification / AFM approval required. |
| `R` FSII | **Fuel System Icing Inhibitor:** lowers freezing point of **water in fuel** → prevents fuel-line/filter ice; **not fuel freeze-point improver or airframe de-icer**; use approved additive/concentration only. |
| `T` ICE | **Fuel freezing (wax/crystals) ≠ entrained/free WATER freezing**; FSII addresses latter. |
| `!` FUEL | Confirm **correct grade/type** against AFM/POH, placards and delivery; sample/check water/debris, no-go contaminated/wrong fuel; AVGAS↔JET misfuel may cause ENG failure; **colour alone insufficient**. |

- `SRC:` [FAA AMT General · AVGAS grades/colour + JET types](https://www.faa.gov/sites/faa.gov/files/regulations_policies/handbooks_manuals/aviation/amt_general_handbook.pdf) · [Canadian SCC · JET A/A-1 freeze points](https://scc-ccn.ca/standards/notices-of-intent/canadian-general-standards-board-cgsb/aviation-turbine-fuel-grades-4) · [FAA AC 20-29C · FSII](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20_29C.pdf); **POH/AFM wins**.
- `M · L4` **FUEL: OCTANE=knock resistance | 80/87 RED; 100/130 GREEN (lean/rich); 100LL BLUE (low lead≠unleaded) | JET A −40°C / A-1 −47°C (max freeze) | JET B wide-cut | FSII inhibits water ice ≠ fuel/airframe de-ice | verify approved grade/type; colour≠proof.**

***
#### Fuel / starvation / contamination

- Know total/usable/unusable, geometry, selector, vents, drains, pumps/crossfeed and gauge limits.
- Starvation: fuel aboard but not reaching engine; exhaustion: none usable. `M:` starvation may be recoverable, exhaustion is not.
- `S:` rough/power or flow loss, selected tank empty, vent blocked, selector wrong/OFF, water/wrong fuel.
- `P:` heat/alternate air→proper/fullest tank→mixture→pump→primer locked→mags, while preserving landing path.
- Drain all POH sumps after required events; one clear sample proves only that point. Wrong/contaminated fuel=no-go.
- `T:` gauges≠measured fuel+time/burn; late tank changes may add delay/air.
***
#### Oil pressure / temperature

| Indication | Likely concern | Action memory |
|---|---|---|
| low oil pressure + high temp | lubrication loss / impending seizure | reduce power, land ASAP |
| low pressure + normal temp | gauge/sender or early failure | treat seriously, monitor, land |
| high temp + normal pressure | cooling, low oil, prolonged climb | enrich/increase airflow/reduce power |
| pressure fluctuation | low quantity, aeration, sensor, manoeuvre | stabilize, assess, land |

- `T:` “gauge fault” is a diagnosis of exclusion. Plan for engine stoppage.
- `!:` abnormal noise/vibration + oil indication = immediate landing priority.
***
#### Cylinder-head / engine temperature

- High temperature: excessive power, lean mixture, poor airflow, high OAT, prolonged low-speed climb, cowl-flap/config issue.
- `P:` lower nose/increase airspeed→enrich as appropriate→reduce power→open cowl flaps if fitted→land if unresolved.
- `T:` cooling by excessive mixture/power changes can create other problems; POH limits/procedure win.
***
#### Engine roughness — generic flow

- `P:` control/landing area→carb heat or alternate air→mixture adjust→fuel selector/pump→primer locked→mags→engine gauges→declare/divert.
- `M:` `HEAT-MIX-FUEL-PRIMER-MAGS`.
- `T:` do not spend altitude cycling controls repeatedly. One deliberate diagnostic pass, then land.
***
#### Complete engine failure

- `P:` nose→best glide `[POH]`→field/landing path→restart flow if time→MAYDAY/7700→pax/secure→land.
- Restart generic: carb heat→fuel selector→mixture→pump→primer→mags/start as applicable.
- `T:` best glide gives options only if established immediately.
- `!:` after takeoff: lower nose and land ahead-ish; turnback only with trained/proven margin and suitable conditions.
***
#### Powerplant / PROP · L4 CAVE

| Key | Recall |
|---|---|
| `R` Cycle | Gas turbine: **INTAKE→COMPRESS→continuous COMBUST→TURBINE→EXHAUST**; turbine drives compressor; remaining energy → thrust/shaft. Piston: intermittent combustion. |
| `M` Turbojet | Core airflow → exhaust jet = principal thrust; no bypass fan. |
| `M` Turbofan | Fan + core; bypass air adds thrust; **BPR = bypass mass flow ÷ core mass flow** (5:1 = 5 bypass/1 core; **≠ thrust ratio**). |
| `M` Turboprop | Gas turbine → power shaft + reduction gearbox → **PROP** principal thrust (e.g. ATR); exhaust contributes some thrust. |
| `M` Turboshaft | Turbine → output shaft → rotor/accessory load; output not principally jet thrust. |
| `T` AFR ≠ BPR | **AFR = air mass ÷ fuel mass** (fuel mixture); **BPR = bypass/core airflow** (turbofan). |
| `R` Compressor | **Axial** successive rotor/stator rows; **centrifugal** impeller→radial diffuser. |
| `T` STAGE ≠ SPOOL | Compressor STAGE≈rotor+stator; turbine STAGE≈stator/nozzle+rotor. SPOOL=compressor+shaft+driving turbine; multi-stage spool ≠ multi-spool. |
| `R` N1/N2 | Typical two-spool turbofan: **N1 LP/fan**, **N2 HP/core** speeds; exact indications/configuration ACFT-specific. Free power turbine mechanically independent of gas-generator compressor spool. |
| `R` Pitch | Blade angle ↑ → **COARSE/HIGH** → PROP load ↑, RPM tendency ↓; angle ↓ → **FINE/LOW** → load ↓, RPM tendency ↑ (**given comparable power/airspeed**). Pitch≠blade AOA. |
| `R` Types | Fixed: no FLT pitch control; ground-adjustable: ground only; pilot variable: selectable angle; **constant-speed governor varies pitch to hold selected RPM** within stops; full-feathering or reversible only if installed. |
| `P` CS PROP | Typical piston: throttle→power/MP; PROP lever→governed RPM; lever FWD→high RPM/fine, AFT→lower RPM/coarse; pitch stops may prevent RPM hold. |
| `R` Feather | Near edge-on to airflow→**windmilling drag↓** after ENG failure; **≠ reverse**. |
| `R` ALPHA | Turboprop flight range: PROP governor varies blade angle to maintain selected RPM. |
| `R` BETA | Ground range aft of FLT idle: power lever schedules PROP blade angle (outside normal RPM governing). |
| `R` GROUND FINE | Low blade angle→low/near-zero forward thrust for taxi. |
| `R` REVERSE | Further BETA→negative blade angle→reverse thrust for ground deceleration; **BETA ≠ REVERSE** (reverse ⊂ beta, on equipped ACFT). |
| `!` BETA LIMIT | Normally **ground only**; observe FLT-idle gate and AFM limits; in-FLT BETA may cause loss of control/overspeed.
| `T` SE vs ME | **Typical piston** SE non-feathering: governor oil P↑→pitch↑/RPM↓; **typical piston** ME full-feathering: oil P↑→pitch↓/RPM↑; oil P loss→counterweights/springs drive feather. **Not universal**; POH/AFM wins. |
| `!` OEI | Windmilling unfeathered failed PROP→large drag / climb loss; **control→identify→verify→feather→secure per POH**, never feather unverified ENG; feather locks/accumulator/prop architecture vary. |

- `SRC:` [FAA AFH Ch 15 · Alpha/Beta](https://www.faa.gov/sites/faa.gov/files/regulations_policies/handbooks_manuals/aviation/airplane_handbook/16_afh_ch15.pdf) · [FAA PHAK · engines/PROP](https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/faa-h-8083-25c.pdf) · [FAA AFH · ME governor/feather](https://www.faasafety.gov/files/events/SO/SO15/2022/SO15118118/TransitionToMultiengineAirplanes.pdf) · [FAA AMT Powerplant · PROP](https://www.faa.gov/sites/faa.gov/files/09_amtp_ch7.pdf); aircraft POH/AFM controls.
- `M · L4` **JET=exhaust | FAN=bypass+core | T-PROP=gearbox+PROP | T-SHAFT=shaft | BPR=bypass/core ≠ AFR=air/fuel | STAGE≠SPOOL | FINE=angle↓/RPM↑; COARSE=angle↑/RPM↓ | FEATHER drag↓ ≠ REVERSE | TURBOPROP ALPHA=governed RPM; BETA=ground lever→blade angle; GROUND FINE=low thrust; REVERSE=negative thrust⊂BETA; AFM limits | SE oil→coarse vs ME oil→fine (typical piston only) | verify ENG before feather.**

***
#### Manifold pressure · MP — L4

| Key | Recall |
|---|---|
| `R` MP | **Absolute** intake-manifold P, **inHg**; **MP ≠ MAP** (missed approach point). |
| `M` OFF→IDLE | ENG OFF: **MP≈ambient P** (29.92 inHg at standard SL) → IDLE: throttle nearly closed + intake pumping → **MP↓↓** (typically ~10–15 inHg; ACFT-specific). |
| `R` POWER | Throttle↑→MP↑; constant-speed PROP lever→selected RPM; power depends on **MP+RPM+mixture/conditions**. |
| `R` ALT / TURBO | Naturally aspirated ALT↑→max MP↓; turbocharged ENG may maintain commanded MP up to critical ALT, within limits. |
| `S` ICE | Carb ice: fixed-pitch **RPM↓**; constant-speed **MP↓**, RPM initially governed. |
| `T` SQUARE / BOOST | **Over-square:** MP(inHg) > RPM/100 (25 inHg / 2300 RPM → 25>23); numerical only, often permitted. **Overboost:** MP above approved limit **for operating conditions / RPM** (may occur below redline); damaging. POH/AFM MP–RPM limits + sequence win. |

- `SRC:` [FAA PHAK · manifold pressure / constant-speed PROP](https://www.faa.gov/sites/faa.gov/files/pilot_handbook_1.pdf) · POH/AFM governs.
- `M · L4` **MP absolute inHg | OFF≈ambient→IDLE↓↓ | throttle↑ MP↑ | non-turbo ALT↑→MPmax↓ | CS PROP→RPM | carb ice: CS MP↓ / fixed RPM↓ | over-square=MP>RPM/100 (may be OK) | overboost=MP>approved limit (RPM-dependent) | POH wins.**

***
#### Propeller / governor — constant-speed

- Throttle controls manifold pressure; prop control governs RPM/blade angle; mixture controls fuel-air ratio.
- `S overspeed:` RPM↑, noise↑. `P:` throttle reduce→prop control reduce RPM if effective→airspeed/power manage→land.
- `S underspeed/governor fault:` RPM low/unresponsive. Use power setting that avoids vibration/limits; land.
- `T:` power-setting order and manifold-pressure/RPM limitations are aircraft-specific.
***
#### Propeller vibration

- Causes: ice, damage, spinner, engine/prop fault.
- `P:` reduce power/RPM to minimize vibration→check ice systems if fitted→land ASAP.
- `!:` severe vibration: throttle idle may prevent separation/damage; secure engine if required by POH.
- `T:` do not cycle prop aggressively unless checklist directs.
***
#### Electrical / alternator failure

- Alternator/generator+regulator powers bus/recharges battery; battery supplies start/emergency energy.
- `S:` ALT/low-voltage light, discharge/low volts, weakening equipment.
- `P:` confirm→shed→one reset only if POH permits→if no recovery ALT OFF→preserve essentials→declare/divert/land. `M:` `SHED-CALCULATE-COMMUNICATE-LAND`.
- `F rough:` endurance h≈usable Ah/essential A; reduce for age/temp/voltage. Precompute IFR/night loads; repeated resets may worsen fault.
***
#### Fire / smoke

| Event | Generic memory—exact POH wins |
|---|---|
| electrical smoke/fire | master/ALT OFF→vents/heat per checklist→extinguish→restore only essential circuits after smoke stops→land now |
| start fire | continue cranking to draw fire inward→MIX ICO/fuel/throttle/master/mags per POH→evacuate/extinguish if persistent |
| engine fire flight | fuel/MIX/pump OFF→throttle/prop/mags + cabin heat/air per POH→specified airspeed→forced landing; no restart unless survival requires and fire confirmed out |
| cabin fire | control→source OFF→extinguish→vent after out if directed→land |

- `!:` fire/smoke can rapidly damage structure/controls or poison occupants; nearest suitable landing. Extinguisher/ventilation effects are agent- and aircraft-specific.
***
#### Carbon monoxide

- Sources: exhaust/heater leak. Symptoms: headache, nausea, dizziness, drowsiness, impaired judgment.
- `P:` cabin heat off→fresh air/vents/windows as safe→oxygen if available→land ASAP→medical evaluation.
- `T:` symptoms mimic fatigue/illness; colour/smell unreliable. Detector is valuable.
***
#### Pitot / static

- Pitot→ASI; static→ASI/ALT/VSI. Pitot heat normally does not heat static ports; preflight for covers/bugs/water/ice/tape.

| Failure | ASI | ALT | VSI |
|---|---|---|---|
| pitot blocked, drain open | →`0` | normal | normal |
| pitot+drain blocked | climb high/descent low | normal | normal |
| static blocked | climb low/descent high | frozen | →`0` |
| alternate static | often ASI/ALT higher | aircraft-specific | momentary/specific |

- `P:` heat→alternate static per POH→attitude/power/GPS trend→ATC→land. Exact errors vary.
***
#### Altimeter failure / unreliable altitude

- Cross-check against genuinely independent sources. GPS altitude differs from barometric altitude; ATC-displayed pressure altitude may share the aircraft static-system fault. ALT/VSI/ASI can all share one blocked static source.
- `P IFR:` declare→request block altitude/vectors→use reliable backup/standby→avoid terrain/icing→land.
- `T:` GPS altitude is not barometric altitude and normally cannot replace required altimeter.
***
#### Vacuum / gyro failure

- Legacy vacuum often powers AI+DG; turn coordinator often electric. `S:` low suction, slow/precessing/frozen or conflicting indications.
- `P:` identify/cover→use reliable pitot-static/turn/compass/power cues→ATC/no-gyro vectors→land.
- AI failed: ASI/ALT/VSI/turn/compass/power; DG failed: compass/timed turns/GPS supplementary; TC failed: AI/DG/compass.
- `T:` gradual failure looks plausible; know common power sources.
***
#### Magnetic compass

- Errors: variation/deviation, oscillation, acceleration/turning/dip.
- Northern hemisphere: on east/west headings, acceleration causes a false north indication and deceleration a false south indication (`ANDS`); turning-error rollout memory is `UNOS`: undershoot north/overshoot south.
- `T:` turbulence and turns make compass difficult; roll out using timed/lead technique.
***
#### Flight-control malfunction

- `P:` maintain control with remaining surfaces→reduce speed/load→trim/power/flap asymmetry awareness→declare→long straight-in landing.
- Jammed elevator: power + trim may control pitch. Jammed aileron: rudder/dihedral may assist roll. Jammed rudder: bank/power carefully.
- `!:` aircraft-specific controllability varies. Avoid abrupt inputs.
- `T:` autopilot/trim system may be source of apparent control jam.
***
#### Trim runaway / jam

- `P:` hold control firmly→disconnect autopilot/electric trim→pull breaker/switch per POH→retrim manually→slow as appropriate→land.
- `T:` electric trim may continue after autopilot disconnect depending fault; know separate trim disconnect.
- `!:` do not release control pressure while troubleshooting.
***
#### Flap malfunction / asymmetry

- `S:` roll/yaw, unequal indication, motor noise/no movement.
- `P:` stop flap movement→do not reverse unless POH directs→control speed/bank→leave flaps→calculate landing distance→long runway.
- `T:` asymmetric flaps can create severe roll; cycling may worsen.
***
#### Landing-gear malfunction

- `P:` slow within limits→check breaker/selector/indicator/light bulbs→recycle only if POH permits→emergency extension→verify visually/ATC→brief landing/evacuation.
- Gear-up landing: secure fuel/electrical per POH, doors/occupants brief, land under control on suitable surface.
- `T:` repeated cycling consumes electrical/hydraulic energy and may worsen jam.
***
#### Brake failure

- `P:` release/reapply→use opposite brake/rudder cautiously→reduce speed→mixture cutoff/engine shutdown if necessary→avoid obstacles.
- One brake failed: plan runway/taxi direction; use aerodynamic control and minimum braking.
- Hot brakes: stop clear, avoid parking brake, keep people away from wheel area.
- `T:` brake pumping may not help every system; POH/system type wins.
***
#### Tire failure

- Takeoff roll: reject if controllable/runway permits.
- Landing: keep failed tire light as long as possible, aerodynamic braking, directional control, avoid heavy braking.
- `T:` do not taxi fast after suspected failure.
***
#### Door / window open

- `P:` fly aircraft→normal safe speed→land or close only if low workload/POH procedure.
- Usually noise/vibration more than structural emergency in trainers.
- `T:` reaching/fighting door can cause loss of control.
***
#### Windshield / bird strike

- `P:` control→slow as appropriate→protect eyes→assess engine/controls/visibility→land.
- Windshield penetration: goggles/sunglasses, head away from airflow, use side view/instruments.
- `T:` hidden prop/leading-edge/control damage may exist even if engine runs.
***
#### Structural icing

- `P:` exit immediately toward known non-icing air→systems on per POH→declare→increase margins/speed as specified→nearest suitable landing.
- Effects: stall speed↑, drag↑, climb↓, prop/engine/antenna/static blockage, control anomalies.
- `T:` do not use autopilot to hide control-force change; avoid flap changes if tailplane icing concern/POH directs.
***
#### Induction / alternate air

- Fuel-injected engines may use alternate induction air instead of carb heat.
- `S:` intake filter blockage/ice → power loss; alternate air may restore.
- `T:` alternate air often warmer/unfiltered and changes mixture/power.
***
#### Cabin pressurization / outflow — L4

| Key | Recall |
|---|---|
| `T` CABIN ALT | Pressure-equivalent **cabin** ALT ≠ ACFT ALT; cabin ALT governs altitude-dependent O₂ use, subject to separate rules. |
| `R` OUTFLOW | Regulates cabin P by controlling **air discharged**, with conditioned/pressurizing air supplied. |
| `M` CLOSE | Outflow closes→less air escapes→cabin **P↑ / ALT↓** (other factors equal). |
| `M` OPEN | Outflow opens→more air escapes→cabin **P↓ / ALT↑** (other factors equal). |
| `F` ΔP | Differential P = **cabin P − ambient P**; AFM structural limit. |
| `T` RELIEF | **Positive** relief protects against excess cabin P; **negative** relief protects against excess outside P. |
| `!` FAILURE | Depressurization→cabin ALT↑→O₂ / emergency DESC per AFM; **O₂ thresholds/supply: [card 04 · CAR 605.31–32](04_canadian_air_law_core_av_cave_v0_2_compact.md#oxygen--oxygène--car-60531-32)** (not duplicated). |

- `SRC:` [FAA PHAK · pressurization systems](https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak) · [CAR 605.31–32](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/section-605.31.html); ACFT AFM/checklists control.
- `M · L4` **PRESSURIZATION: outflow CLOSE→cabin P↑/ALT↓; OPEN→P↓/ALT↑ | ΔP=cabin−ambient | +relief excess cabin P; −relief excess outside P | decompression→O₂/emergency DESC per AFM.**

***
#### Cabin heat / defrost

- Often uses exhaust-shroud heat; exhaust crack can introduce CO.
- `S:` exhaust smell, headache, detector alert.
- `P:` heat/defrost off→fresh air→land.
- `T:` windshield fogging may compete with CO response; safety of occupants first, land promptly.
***
#### ELT / emergency equipment

- Know activation, remote switch, antenna, battery/inspection status, survival equipment and extinguisher.
- After forced landing: ELT confirm ON, evacuate, fire risk, first aid, shelter/signalling.
- `T:` ELT does not replace flight plan/itinerary closure or survival planning.
***
#### Radio failure

- `P:` audio panel/volume/squelch/headset/mic/PTT/frequency/breaker→other radio→121.5/FSS/relay→transmit blind/listen→squawk `7600`.
- VFR controlled: comply with light signals/land when safe. IFR: published/specific lost-comms procedure.
- `T:` receiver failure vs transmitter failure may be different; keep listening.
***
#### Transponder failure

- `P:` recycle/change code only if appropriate→check breaker/Mode C→advise ATC→comply with instructions/airspace restrictions.
- `T:` do not select `7500/7600/7700` casually.
***
#### Checklist / declaration

- Memory items stop immediate threat; flow organizes; current checklist verifies/finishes. Outdated memorization is hazardous.
- `PAN PAN` urgent/reduced safety; `MAYDAY` serious/imminent danger. State callsign/problem/position-altitude/intentions/fuel/persons/assistance.
- `T:` declaration is a resource, not failure.
***
#### Symptom quick map

| Symptom | First suspects |
|---|---|
| RPM↓ fixed-pitch, humid/partial power | carb ice |
| MP↓ constant-speed, RPM stable | carb ice/induction/power |
| rough + low fuel flow | starvation/selector/pump |
| rough on one mag | plug/mag/lead |
| low oil P + high T | lubrication failure |
| discharge/low volts | alternator/gen failure |
| AI+DG disagree, suction low | vacuum failure |
| ASI odd, ALT/VSI normal | pitot failure |
| ASI+ALT+VSI odd | static failure |
| headache + heater | CO |
| smoke/odour + electrical anomaly | electrical fire |

- `T:` map starts diagnosis; POH/checklist determines action.
***
#### Pebble

- PRESSURIZATION `outflow CLOSE→cabin P↑/ALT↓; OPEN→P↓/ALT↑ | ΔP=cabin−ambient | +relief excess internal P; −relief excess external P | decompression→O₂/emergency DESC per AFM; O₂ rules card 04`
- FUEL `octane=knock resistance | AVGAS 80/87 RED; 100/130 GREEN (lean/rich); 100LL BLUE (LL=low lead) | JET A max freeze −40°C / A-1 −47°C; B wide-cut | FSII water-ice inhibitor ≠ fuel/airframe de-ice | approved fuel/grade per POH; colour alone≠proof`
- MP `absolute intake P inHg | OFF≈ambient→IDLE↓↓ | throttle↑ MP↑ | non-turbo ALT↑→MPmax↓; turbo may hold MP to critical ALT | CS throttle→MP/PROP→RPM | carb ice CS MP↓ vs fixed RPM↓ | over-square=MP>RPM/100 (may be OK); overboost=MP>approved limit (RPM-dependent); POH wins`
- POWERPLANT `JET exhaust | FAN bypass/core; BPR≠AFR | T-PROP gearbox→PROP | T-SHAFT output | STAGE≠SPOOL | fine low pitch/high RPM ↔ coarse high pitch/low RPM | feather drag↓ ≠ reverse | constant-speed governor holds RPM within stops | turboprop ALPHA=governed RPM / BETA=ground blade-angle lever (ground fine→reverse); BETA≠REVERSE; AFM limits | typical piston SE oil→coarse, ME oil→fine/feather on oil loss; POH wins`
- `CONTROL-DIAGNOSE-MEMORY-CHECKLIST-DECLARE-LAND` | engine=`AIR-FUEL-SPARK-COMPRESSION` | rough=`HEAT-MIX-FUEL-PRIMER-MAGS` | mags independent of master | carb ice: full heat, worse→better | fuel gauges + clock, not gauges alone | low oil P+high T=land ASAP | alternator fail=`SHED-CALCULATE-COMMUNICATE-LAND` | pitot affects ASI; static affects ASI/ALT/VSI | vacuum often AI+DG | smoke/fire=land now | CO heat off/fresh air/land | flap asymmetry stop movement | controls first, checklist second | POH wins.
