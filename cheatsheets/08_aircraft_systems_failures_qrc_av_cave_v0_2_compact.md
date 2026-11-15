### AIRCRAFT SYSTEMS / FAILURES QRC — AV-CAVE v0.2 COMPACT
`TARGETED CPAER REVIEW: 2026-09-06` | see `00_CPAER_REVIEW_NOTES.md` for scope and remaining gaps
`P` procedure | `S` symptom | `T` trap | `M` memory | `!` safety | `?` verify | trainer/light-aircraft generic; POH/AFM/SOP wins
`RELEASE:` `STUDY / AIRCRAFT-DEPENDENT` | `NOT FLIGHT AUTHORITY`
***
#### Source / discipline / scan
<!-- id: sys-source-discipline-scan | concepts: agk-systems, study-src | level: PPL CPL -->

- `SRC:` exact POH/AFM §3 + systems, current checklist/SOP; FTM/TP guidance.
- Memorize only aircraft-designated memory items; abnormal checklists normally read-and-do.
- `P:` control→power/sound→fuel→oil→electrical→pitot/static/gyro→controls/config→smoke/fire/odour; confirm instrument failure with `≥2` independent indications.
- `M:` `CONTROL-DIAGNOSE-MEMORY-CHECKLIST-DECLARE-LAND` | `POWER-FUEL-OIL-ELECTRIC-AIR-DIRECTION-CONTROLS`.
- `T:` preserve control/landing options; same symptom may have several causes.
***
#### Magneto roughness in flight
<!-- id: sys-magneto-roughness-in-flight | concepts: agk-engine, emg-engine | level: PPL CPL -->

- `P:` control→mixture adjust→carb heat as appropriate→select mags individually briefly per POH→return BOTH if worse→land/divert.
- `T:` switching to OFF in flight may load exhaust with fuel; returning to BOTH can cause backfire/damage. Follow POH.
- `!:` severe vibration/power loss/fire indications = treat as engine emergency, not merely a mag check.
***
#### Cylinder-head / engine temperature
<!-- id: sys-cylinder-head-engine-temperature | concepts: agk-engine | level: PPL CPL -->

- High temperature: excessive power, lean mixture, poor airflow, high OAT, prolonged low-speed climb, cowl-flap/config issue.
- `P:` lower nose/increase airspeed→enrich as appropriate→reduce power→open cowl flaps if fitted→land if unresolved.
- `T:` cooling by excessive mixture/power changes can create other problems; POH limits/procedure win.
***
#### Engine roughness — generic flow
<!-- id: sys-engine-roughness-generic-flow | concepts: agk-engine, emg-engine | level: PPL CPL -->

- `P:` control/landing area→carb heat or alternate air→mixture adjust→fuel selector/pump→primer locked→mags→engine gauges→declare/divert.
- `M:` `HEAT-MIX-FUEL-PRIMER-MAGS`.
- `T:` do not spend altitude cycling controls repeatedly. One deliberate diagnostic pass, then land.
***
#### Complete engine failure
<!-- id: sys-complete-engine-failure | concepts: emg-engine, emg-sys | level: PPL CPL -->

- `P:` nose→best glide `[POH]`→field/landing path→restart flow if time→MAYDAY/7700→pax/secure→land.
- Restart generic: carb heat→fuel selector→mixture→pump→primer→mags/start as applicable.
- `T:` best glide gives options only if established immediately.
- `!:` after takeoff: lower nose and land ahead-ish; turnback only with trained/proven margin and suitable conditions.
***
#### Propeller / governor — constant-speed
<!-- id: sys-propeller-governor-constant-speed | concepts: agk-prop | level: CPL ME -->

- Throttle controls manifold pressure; prop control governs RPM/blade angle; mixture controls fuel-air ratio.
- `S overspeed:` RPM↑, noise↑. `P:` throttle reduce→prop control reduce RPM if effective→airspeed/power manage→land.
- `S underspeed/governor fault:` RPM low/unresponsive. Use power setting that avoids vibration/limits; land.
- `T:` power-setting order and manifold-pressure/RPM limitations are aircraft-specific.
***
#### Propeller vibration
<!-- id: sys-propeller-vibration | concepts: agk-prop | level: PPL CPL -->

- Causes: ice, damage, spinner, engine/prop fault.
- `P:` reduce power/RPM to minimize vibration→check ice systems if fitted→land ASAP.
- `!:` severe vibration: throttle idle may prevent separation/damage; secure engine if required by POH.
- `T:` do not cycle prop aggressively unless checklist directs.
***
#### Electrical / alternator failure
<!-- id: sys-electrical-alternator-failure | concepts: agk-elec, emg-sys | level: PPL CPL IR -->

- Alternator/generator+regulator powers bus/recharges battery; battery supplies start/emergency energy.
- `S:` ALT/low-voltage light, discharge/low volts, weakening equipment.
- `P:` confirm→shed→one reset only if POH permits→if no recovery ALT OFF→preserve essentials→declare/divert/land. `M:` `SHED-CALCULATE-COMMUNICATE-LAND`.
- `F rough:` endurance h≈usable Ah/essential A; reduce for age/temp/voltage. Precompute IFR/night loads; repeated resets may worsen fault.
***
#### Fire / smoke
<!-- id: sys-fire-smoke | concepts: emg-fire | level: PPL CPL -->

| Event | Generic memory—exact POH wins |
|---|---|
| electrical smoke/fire | master/ALT OFF→vents/heat per checklist→extinguish→restore only essential circuits after smoke stops→land now |
| start fire | continue cranking to draw fire inward→MIX ICO/fuel/throttle/master/mags per POH→evacuate/extinguish if persistent |
| engine fire flight | fuel/MIX/pump OFF→throttle/prop/mags + cabin heat/air per POH→specified airspeed→forced landing; no restart unless survival requires and fire confirmed out |
| cabin fire | control→source OFF→extinguish→vent after out if directed→land |

- `!:` fire/smoke can rapidly damage structure/controls or poison occupants; nearest suitable landing. Extinguisher/ventilation effects are agent- and aircraft-specific.
***
#### Carbon monoxide
<!-- id: sys-carbon-monoxide | concepts: agk-hf, emg-fire | level: PPL CPL -->

- Sources: exhaust/heater leak. Symptoms: headache, nausea, dizziness, drowsiness, impaired judgment.
- `P:` cabin heat off→fresh air/vents/windows as safe→oxygen if available→land ASAP→medical evaluation.
- `T:` symptoms mimic fatigue/illness; colour/smell unreliable. Detector is valuable.
***
#### Altimeter failure / unreliable altitude
<!-- id: sys-altimeter-failure-unreliable-altitude | concepts: agk-pitot, emg-sys | level: PPL CPL IR -->

- Cross-check against genuinely independent sources. GPS altitude differs from barometric altitude; ATC-displayed pressure altitude may share the aircraft static-system fault. ALT/VSI/ASI can all share one blocked static source.
- `P IFR:` declare→request block altitude/vectors→use reliable backup/standby→avoid terrain/icing→land.
- `T:` GPS altitude is not barometric altitude and normally cannot replace required altimeter.
***
#### Vacuum / gyro failure
<!-- id: sys-vacuum-gyro-failure | concepts: agk-gyro, emg-sys | level: PPL CPL IR -->

- Legacy vacuum often powers AI+DG; turn coordinator often electric. `S:` low suction, slow/precessing/frozen or conflicting indications.
- `P:` identify/cover→use reliable pitot-static/turn/compass/power cues→ATC/no-gyro vectors→land.
- AI failed: ASI/ALT/VSI/turn/compass/power; DG failed: compass/timed turns/GPS supplementary; TC failed: AI/DG/compass.
- `T:` gradual failure looks plausible; know common power sources.
***
#### Flight-control malfunction
<!-- id: sys-flight-control-malfunction | concepts: agk-systems, emg-sys | level: PPL CPL -->

- `P:` maintain control with remaining surfaces→reduce speed/load→trim/power/flap asymmetry awareness→declare→long straight-in landing.
- Jammed elevator: power + trim may control pitch. Jammed aileron: rudder/dihedral may assist roll. Jammed rudder: bank/power carefully.
- `!:` aircraft-specific controllability varies. Avoid abrupt inputs.
- `T:` autopilot/trim system may be source of apparent control jam.
***
#### Trim runaway / jam
<!-- id: sys-trim-runaway-jam | concepts: agk-systems, emg-sys | level: PPL CPL -->

- `P:` hold control firmly→disconnect autopilot/electric trim→pull breaker/switch per POH→retrim manually→slow as appropriate→land.
- `T:` electric trim may continue after autopilot disconnect depending fault; know separate trim disconnect.
- `!:` do not release control pressure while troubleshooting.
***
#### Flap malfunction / asymmetry
<!-- id: sys-flap-malfunction-asymmetry | concepts: agk-systems, emg-sys | level: PPL CPL -->

- `S:` roll/yaw, unequal indication, motor noise/no movement.
- `P:` stop flap movement→do not reverse unless POH directs→control speed/bank→leave flaps→calculate landing distance→long runway.
- `T:` asymmetric flaps can create severe roll; cycling may worsen.
***
#### Landing-gear malfunction
<!-- id: sys-landing-gear-malfunction | concepts: agk-systems, emg-sys | level: CPL ME -->

- `P:` slow within limits→check breaker/selector/indicator/light bulbs→recycle only if POH permits→emergency extension→verify visually/ATC→brief landing/evacuation.
- Gear-up landing: secure fuel/electrical per POH, doors/occupants brief, land under control on suitable surface.
- `T:` repeated cycling consumes electrical/hydraulic energy and may worsen jam.
***
#### Brake failure
<!-- id: sys-brake-failure | concepts: agk-systems, emg-sys | level: PPL CPL -->

- `P:` release/reapply→use opposite brake/rudder cautiously→reduce speed→mixture cutoff/engine shutdown if necessary→avoid obstacles.
- One brake failed: plan runway/taxi direction; use aerodynamic control and minimum braking.
- Hot brakes: stop clear, avoid parking brake, keep people away from wheel area.
- `T:` brake pumping may not help every system; POH/system type wins.
***
#### Tire failure
<!-- id: sys-tire-failure | concepts: agk-systems, emg-sys | level: PPL CPL -->

- Takeoff roll: reject if controllable/runway permits.
- Landing: keep failed tire light as long as possible, aerodynamic braking, directional control, avoid heavy braking.
- `T:` do not taxi fast after suspected failure.
***
#### Door / window open
<!-- id: sys-door-window-open | concepts: emg-sys | level: PPL CPL -->

- `P:` fly aircraft→normal safe speed→land or close only if low workload/POH procedure.
- Usually noise/vibration more than structural emergency in trainers.
- `T:` reaching/fighting door can cause loss of control.
***
#### Windshield / bird strike
<!-- id: sys-windshield-bird-strike | concepts: emg-sys | level: PPL CPL -->

- `P:` control→slow as appropriate→protect eyes→assess engine/controls/visibility→land.
- Windshield penetration: goggles/sunglasses, head away from airflow, use side view/instruments.
- `T:` hidden prop/leading-edge/control damage may exist even if engine runs.
***
#### Structural icing
<!-- id: sys-structural-icing | concepts: met-icing | level: PPL CPL IR -->

- `P:` exit immediately toward known non-icing air→systems on per POH→declare→increase margins/speed as specified→nearest suitable landing.
- Effects: stall speed↑, drag↑, climb↓, prop/engine/antenna/static blockage, control anomalies.
- `T:` do not use autopilot to hide control-force change; avoid flap changes if tailplane icing concern/POH directs.
***
#### Cabin heat / defrost
<!-- id: sys-cabin-heat-defrost | concepts: agk-systems | level: PPL CPL -->

- Often uses exhaust-shroud heat; exhaust crack can introduce CO.
- `S:` exhaust smell, headache, detector alert.
- `P:` heat/defrost off→fresh air→land.
- `T:` windshield fogging may compete with CO response; safety of occupants first, land promptly.
***
#### Radio failure
<!-- id: sys-radio-failure | concepts: law-atc, emg-sys, emg-comms | level: PPL CPL IR -->

- `P:` audio panel/volume/squelch/headset/mic/PTT/frequency/breaker→other radio→121.5/FSS/relay→transmit blind/listen→squawk `7600`.
- VFR controlled: comply with light signals/land when safe. IFR: published/specific lost-comms procedure.
- `T:` receiver failure vs transmitter failure may be different; keep listening.
***
#### Transponder failure
<!-- id: sys-transponder-failure | concepts: law-atc, emg-sys | level: PPL CPL -->

- `P:` recycle/change code only if appropriate→check breaker/Mode C→advise ATC→comply with instructions/airspace restrictions.
- `T:` do not select `7500/7600/7700` casually.
***
#### Checklist / declaration
<!-- id: sys-checklist-declaration | concepts: emg | level: PPL CPL -->

- Memory items stop immediate threat; flow organizes; current checklist verifies/finishes. Outdated memorization is hazardous.
- `PAN PAN` urgent/reduced safety; `MAYDAY` serious/imminent danger. State callsign/problem/position-altitude/intentions/fuel/persons/assistance.
- `T:` declaration is a resource, not failure.
***
#### Symptom quick map
<!-- id: sys-symptom-quick-map | concepts: agk-systems, emg | level: PPL CPL -->

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
<!-- id: sys-pebble | concepts: agk-systems, study-pebble | level: PPL CPL IR -->

- PRESSURIZATION `outflow CLOSE→cabin P↑/ALT↓; OPEN→P↓/ALT↑ | ΔP=cabin−ambient | +relief excess internal P; −relief excess external P | decompression→O₂/emergency DESC per AFM; O₂ rules card 04`
- FUEL `octane=knock resistance | AVGAS 80/87 RED; 100/130 GREEN (lean/rich); 100LL BLUE (LL=low lead) | JET A max freeze −40°C / A-1 −47°C; B wide-cut | FSII water-ice inhibitor ≠ fuel/airframe de-ice | approved fuel/grade per POH; colour alone≠proof`
- MP `absolute intake P inHg | OFF≈ambient→IDLE↓↓ | throttle↑ MP↑ | non-turbo ALT↑→MPmax↓; turbo may hold MP to critical ALT | CS throttle→MP/PROP→RPM | carb ice CS MP↓ vs fixed RPM↓ | over-square=MP>RPM/100 (may be OK); overboost=MP>approved limit (RPM-dependent); POH wins`
- POWERPLANT `JET exhaust | FAN bypass/core; BPR≠AFR | T-PROP gearbox→PROP | T-SHAFT output | STAGE≠SPOOL | fine low pitch/high RPM ↔ coarse high pitch/low RPM | feather drag↓ ≠ reverse | constant-speed governor holds RPM within stops | turboprop ALPHA=governed RPM / BETA=ground blade-angle lever (ground fine→reverse); BETA≠REVERSE; AFM limits | typical piston SE oil→coarse, ME oil→fine/feather on oil loss; POH wins`
- `CONTROL-DIAGNOSE-MEMORY-CHECKLIST-DECLARE-LAND` | engine=`AIR-FUEL-SPARK-COMPRESSION` | rough=`HEAT-MIX-FUEL-PRIMER-MAGS` | mags independent of master | carb ice: full heat, worse→better | fuel gauges + clock, not gauges alone | low oil P+high T=land ASAP | alternator fail=`SHED-CALCULATE-COMMUNICATE-LAND` | pitot affects ASI; static affects ASI/ALT/VSI | vacuum often AI+DG | smoke/fire=land now | CO heat off/fresh air/land | flap asymmetry stop movement | controls first, checklist second | POH wins.
***
