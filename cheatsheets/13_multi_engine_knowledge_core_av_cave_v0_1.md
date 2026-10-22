### MULTI-ENGINE KNOW — AV-CAVE v0.1
`SEPTEMBER CPAER REVIEW: retained reference, not freshly revalidated` | use exact aircraft/current operational sources
`R` rule | `F` formula | `P` procedure | `T` trap | `M` memory | `!` safety | `?` verify | Canada ME rating
`RELEASE:` `EXAM/STUDY-REF / AIRCRAFT-DEPENDENT` | `CANONICAL SOURCE:` `multi_engine_knowledge_core_av_cave_v0_1.md` | `NOT FLIGHT AUTHORITY`
***
#### Source / rating frame

- `SRC:` CAR/STD 421.38 = rating skill requirement; TP 219E = TC flight-test guide; POH/AFM/SOP wins aircraft-specific speeds/procedures.
- Canada ME class rating: applicant completes flight test as PIC of multi-engine class aeroplane per Standard 428 Schedule 7.
- `T:` ME rating ≠ Group 1 IFR. ME class lets you fly multi-engine class aeroplanes VFR/IFR only if licence/rating/equipment/recency/ops rules allow.
***
#### Essential speeds to know cold

| Symbol | Meaning |
|---|---|
| `Vmc` | min control speed airborne, critical engine failed |
| `Vsse` | safe intentional OEI speed; if POH none, TC guide says use `Vmc+10` |
| `Vyse` | OEI best rate-of-climb speed, blue line |
| `Vxse` | OEI best angle-of-climb speed |
| `Vs0` | stall speed landing config |
| `Va` | manoeuvring speed |
| `Vle` | max gear extended |
| `Vlo` | max gear operating |
| `Vfe` | max flap extended |

- `T:` quote aircraft numbers from memory for test; all other performance from POH/AFM charts.
***
#### Core ME physics

- Two engines = thrust + yaw + roll problem after failure, not “half a single-engine airplane.”
- Failed engine side: thrust↓ + drag↑. Operating engine creates yaw toward failed engine.
- `T:` asymmetry increases with power on live engine, low speed, high AoA, aft CG, low weight, windmilling prop, gear/flaps drag.
- `M:` CONTROL before CHECKLIST; drag reduction before diagnosis obsession.
***
#### Critical engine

- Critical engine = engine whose failure most adversely affects performance/handling.
- Conventional clockwise props viewed from cockpit: left engine often critical.
- Why: `P-factor` + accelerated slipstream + spiraling slipstream + torque effects usually make left-engine failure worse.
- `M:` left failed = right engine thrust line farther from CG ⇒ larger yaw arm.
- `T:` counter-rotating twins may have no “more critical” engine; aircraft-specific.
***
#### Vmc definition / certification memory

- `Vmc:` minimum flight speed where straight flight/control possible after sudden critical-engine failure with max rudder and ≤`5°` bank.
- TC guide conditions: max rated power on engines at failure, min practical test weight, rearmost CG, gear retracted, flaps takeoff, failed critical prop windmilling.
- Below `Vmc`: yaw/roll toward failed engine; regain by reducing live-engine power, increasing airspeed by lowering pitch, or both.
- `T:` `Vmc` is a control speed, not a climb speed. Above Vmc does not mean climb possible.
***
#### Vmc factors

| Factor | Vmc effect |
|---|---|
| live engine power ↑ | `Vmc ↑` |
| density altitude ↑ / power ↓ | `Vmc ↓` but performance worse |
| aft CG | `Vmc ↑` |
| lower weight | `Vmc ↑` |
| gear/flap down | often `Vmc ↓` due drag/stability, but performance worse |
| windmilling failed prop | yaw/drag ↑, performance worse |
| bank into live engine | `Vmc ↓`, performance ↑ |

- `T:` high DA may lower Vmc but makes OEI climb worse. “control easier” while performance gone.
***
#### Zero sideslip / best OEI performance

- Best OEI performance usually: slight bank toward operating engine + ball slightly displaced toward live engine / aircraft-specific.
- Common memory: `2–5°` bank toward good engine, rudder to stop yaw, trim.
- `M:` bank into good engine reduces rudder drag; level wings often requires lots of rudder and creates sideslip/drag.
- `T:` centre the ball blindly? not always best; use POH/AFM and instructor method.
***
#### Dead foot / dead engine

- Failure recognition: yaw/roll/noise/power instruments.
- `M:` dead foot = dead engine. Foot not pressing = failed side.
- Identify: mixture/prop/throttle or power lever suspected engine. Verify: reduce suspected throttle/power; no change confirms failed engine. Then feather/shutdown per checklist.
- `T:` never feather until verified. Wrong feather can make a bad day unrecoverable.
***
#### Engine failure flow — generic

- `P:` MAINTAIN CONTROL → POWER AS REQ → PITCH `Vyse/Vxse` → GEAR/FLAPS UP as appropriate → IDENTIFY → VERIFY → FEATHER → SECURE → CHECKLIST → PLAN.
- `M:` Control–Config–Identify–Verify–Feather–Secure–Checklist.
- `T:` in critical phase, memory items first; full checklist only after control and drag clean-up.
- `T:` do not rush feather below safe altitude if procedure/aircraft/training says simulate only.
***
#### Drag hierarchy

- Worst drag: windmilling prop. Then gear, flaps, cowl flaps, sideslip, excessive bank/trim.
- `M:` clean + feather + blue line.
- `P:` gear up after positive climb/no runway; flaps up in stages as POH; prop feather after verify; cowl flaps as required.
- `T:` unfeathered failed prop can erase climb performance.
***
#### OEI climb

- `Vyse` = best rate; `Vxse` = best angle. Use obstacle vs rate logic.
- `T:` positive climb may be zero or negative depending weight/DA/config/failed engine/prop/surface.
- POH required: OEI ROC, single-engine service ceiling, accelerate-stop/go if available, climb gradients.
- `M:` ME safety comes from precomputed options, not heroic rudder.
***
#### Accelerate-stop / accelerate-go

- Accelerate-stop = accelerate to decision/engine-failure speed, reject, stop.
- Accelerate-go = accelerate to failure speed, continue takeoff, climb/clear obstacle OEI.
- Light twins often have long or unavailable accelerate-go margins at normal training weights/DA.
- `T:` balanced field/V1 thinking from transport category does not automatically apply to light twins.
- `P pre-TKOF brief:` below reject speed/runway remaining → stop; after liftoff/gear up/no runway → control, clean, climb if able, land ahead/nearby if not.
***
#### Takeoff briefing — ME

- `P:` runway/length/wind/DA/perf → rotate speed → `Vmc/Vyse/Vsse` → reject criteria → EF before liftoff → EF after liftoff with runway → EF airborne no runway → emergency return/straight-ahead plan.
- `M:` before power: “what kills us today?” runway, weight, DA, obstacles, weather, traffic.
- `T:` “continue no matter what” is wrong; “stop no matter what” is also wrong. runway remaining + energy + control decide.
***
#### Engine failure on takeoff / overshoot

- `P:` recognize → control → power/config/drag in proper order → identify/verify → bank good engine → maintain heading ± practical → positive climb if capable → `Vxse` obstacle or `Vyse` rate → trim.
- TC test tolerances: heading control within about `±20°`; speed `Vxse/Vyse +10/-5` for overshoot scenario.
- `T:` gear/flap movement during power change is high workload; control first.
- `T:` OEI go-around may not climb. If not climbing, land under control.
***
#### Engine failure in cruise

- `P:` control → maintain heading/alt if capable → set power/config → identify/verify → cause checks → feather/secure if no restart → trim → evaluate restart/divert.
- Turns OEI: bank not >`30°` in TC test context; use appropriate pitch/bank/trim.
- `T:` trying to hold altitude below OEI capability causes speed decay to Vmc/stall. Descend if required.
***
#### Precautionary shutdown

- Reasons: oil pressure loss, severe vibration, fire risk, runaway prop, uncontrollable temps/pressures.
- `P:` confirm need → stabilize → identify/verify affected engine → reduce power → feather/secure per checklist → monitor live engine → divert/land.
- `T:` not every roughness = immediate shutdown; not every problem can wait. Decide by fire/mechanical damage/controllability.
***
#### PROP governor / feather — L4 cross-ref

- `M` Typical **piston SE CS non-feather**: governor oil P↑→COARSE/pitch↑→RPM↓ | **piston ME CS full-feather**: oil P↑→FINE/pitch↓→RPM↑; oil P↓→counterweights/springs→FEATHER; **architecture varies**.
- `T` FINE low blade angle ≠ low RPM: low angle→RPM tendency↑ | COARSE high angle→RPM tendency↓ | FEATHER near airflow→drag↓; REVERSE negative thrust (ground only if approved).
- `!` OEI: windmilling low-pitch PROP→drag↑/climb↓ | **IDENTIFY→VERIFY→FEATHER** per POH; feather locks, unfeather pumps, accumulators ACFT-specific.
- `SRC:` [FAA AFH · ME propeller](https://www.faasafety.gov/files/events/SO/SO15/2022/SO15118118/TransitionToMultiengineAirplanes.pdf) | [08 Aircraft Systems · Powerplant / PROP](08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md).

***
#### Restart / unfeather

- `P:` assess altitude/time/fire/damage/prop status/fuel/electrical. If feasible: restart checklist; if not: leave secured and land.
- `T:` restarting a damaged/fire engine can make problem worse. checklist and scenario drive.
***
#### OEI approach / landing

- `P:` brief long final, avoid rushed configuration, maintain `Vyse` or POH speed until landing assured, configure late/controlled, anticipate asymmetric power.
- Gear/flap only when landing assured unless procedure says otherwise. Power changes gradual; trim cautiously.
- `T:` full flap/gear early can remove climb escape. OEI go-around may be unavailable.
- `M:` stable > pretty. no salvage below minima/unstable.
***
#### OEI missed / go-around

- `P:` max allowable power live engine → control yaw/bank → pitch `Vyse/Vxse` → drag up in sequence → verify failed engine secure/feathered → trim.
- `T:` if unable climb, lower nose and land ahead/within available area. Do not pull below `Vyse` toward `Vmc`.
- `T:` high power + low speed + dirty config = Vmc trap.
***
#### Vmc demo / reduced-speed training

- Setup per POH/instructor/test guide; safe altitude; clearing; no real hazard; recover at first sign of loss of directional control/stall buffet/warning or prebriefed minimum.
- Recovery: reduce live-engine power enough to regain control + lower pitch/increase speed + wings/bank controlled.
- `T:` wrong instinct = add power/pull. Correct = reduce asymmetric thrust and increase airspeed.
- `T:` Vmc demo is not a macho manoeuvre; it is recognition and immediate recovery.
***
#### Stall / slow flight ME

- Slow flight near Vmc/VS margins with asymmetry is dangerous. Maintain coordination, power awareness, safe altitude.
- Stall recovery: reduce AoA, manage asymmetry, power as appropriate, avoid yaw.
- `T:` power-on stall with one engine/thrust asymmetry can roll/yaw aggressively.
***
#### Systems focus for ME

- Prop governors/feathering/unfeathering: oil pressure, accumulators/unfeather pumps depending aircraft.
- Fuel: selectors/crossfeed/aux pumps/boost pumps; know which positions are allowed for takeoff/landing.
- Electrical: two alternators? bus logic? battery endurance? gear/flap dependence?
- Vacuum/pressure: source from one/both engines? failure effect after engine shutdown?
- Hydraulics/gear: extension/retraction speed, emergency extension, gear warning.
- `T:` engine shutdown may remove systems powered by that engine.
***
#### Performance calculations required

- Takeoff distance / obstacle. Accelerate-stop if available. Accelerate-go if available. Time/fuel to climb. Cruise power/KTAS/fuel. Landing distance. OEI ROC. OEI enroute performance.
- `T:` use actual weight, temp, pressure altitude, runway, wind, obstacle, configuration. Training “it climbs” assumption is unsafe.
- `M:` compare before flight: all-engine climb, OEI climb, terrain/obstacle, nearest runway/return.
***
#### W&B ME traps

- Multi-engine aircraft often have narrow CG/fuel/baggage constraints. Check takeoff, landing, zero-fuel if relevant.
- Aft CG worsens Vmc/control. Light weight can worsen Vmc but improves climb; heavy weight may improve Vmc but destroy climb.
- `T:` Vmc certification worst case is light/aft; performance worst case is heavy/hot/high/dirty.
***
#### Flight test mindset

- TC test wants PIC-level control, memory vital actions, checklist discipline, POH knowledge, and decision-making.
- Essential speeds from memory. Charts and performance from approved data.
- `T:` examiner is testing whether you know when not to continue as much as whether you can keep it flying.
***
#### Memory atoms

- `dead foot = dead engine`
- `identify before verify; verify before feather`
- `blue line = best OEI rate`
- `red line = Vmc; below red line reduce power/lower nose`
- `clean + feather + blue line`
- `bank toward good engine`
- `control first, checklist second`
- `above Vmc ≠ climb`
- `single-engine service ceiling may be below terrain`
- `live engine can kill you if you cannot control it`
***
#### Pebble

- PROP `typical piston SE oil→coarse/RPM↓ vs ME oil→fine/RPM↑; ME oil loss→feather | fine RPM tendency↑, coarse RPM tendency↓ | windmill drag↑; feather drag↓ | verify before feather; POH wins`
- ME rating = skill flight test | ME≠Group1 IFR | Vmc control not climb | Vsse = Vmc+10 if POH none | Vyse blue line | critical engine worst handling/perf | Vmc worst: max pwr/light/aft/gear up/takeoff flap/windmilling | below Vmc: reduce live power + lower nose | zero sideslip = bank good engine | dead foot dead engine | identify-verify-feather | clean-feather-blue | OEI climb maybe negative | accelerate-stop/go prebrief | OEI go-around may not climb | POH speeds/procedures win.
