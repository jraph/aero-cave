# Vmc, asymmetric thrust & critical engine / Vmc, poussée asymétrique et moteur critique
<!-- concept: me-vmc | level: ME -->

[Index](README.md) · concept `me-vmc` · unit IDs are stable: never rename one.

***
#### Core ME physics
<!-- id: me-core-me-physics | from: 13 | level: ME -->

- Two engines = thrust + yaw + roll problem after failure, not “half a single-engine airplane.”
- Failed engine side: thrust↓ + drag↑. Operating engine creates yaw toward failed engine.
- `T:` asymmetry increases with power on live engine, low speed, high AoA, aft CG, low weight, windmilling prop, gear/flaps drag.
- `M:` CONTROL before CHECKLIST; drag reduction before diagnosis obsession.
***
#### Critical engine
<!-- id: me-critical-engine | from: 13 | level: ME -->

- Critical engine = engine whose failure most adversely affects performance/handling.
- Conventional clockwise props viewed from cockpit: left engine often critical.
- Why: `P-factor` + accelerated slipstream + spiraling slipstream + torque effects usually make left-engine failure worse.
- `M:` left failed = right engine thrust line farther from CG ⇒ larger yaw arm.
- `T:` counter-rotating twins may have no “more critical” engine; aircraft-specific.
***
#### Vmc definition / certification memory
<!-- id: me-vmc-definition-certification-memory | from: 13 | level: ME -->

- `Vmc:` minimum flight speed where straight flight/control possible after sudden critical-engine failure with max rudder and ≤`5°` bank.
- TC guide conditions: max rated power on engines at failure, min practical test weight, rearmost CG, gear retracted, flaps takeoff, failed critical prop windmilling.
- Below `Vmc`: yaw/roll toward failed engine; regain by reducing live-engine power, increasing airspeed by lowering pitch, or both.
- `T:` `Vmc` is a control speed, not a climb speed. Above Vmc does not mean climb possible.
***
#### Vmc factors
<!-- id: me-vmc-factors | from: 13 | level: ME -->

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
<!-- id: me-zero-sideslip-best-oei-performance | from: 13 | level: ME -->

- Best OEI performance usually: slight bank toward operating engine + ball slightly displaced toward live engine / aircraft-specific.
- Common memory: `2–5°` bank toward good engine, rudder to stop yaw, trim.
- `M:` bank into good engine reduces rudder drag; level wings often requires lots of rudder and creates sideslip/drag.
- `T:` centre the ball blindly? not always best; use POH/AFM and instructor method.
***
#### Dead foot / dead engine
<!-- id: me-dead-foot-dead-engine | from: 13 | also: me-fail | level: ME -->

- Failure recognition: yaw/roll/noise/power instruments.
- `M:` dead foot = dead engine. Foot not pressing = failed side.
- Identify: mixture/prop/throttle or power lever suspected engine. Verify: reduce suspected throttle/power; no change confirms failed engine. Then feather/shutdown per checklist.
- `T:` never feather until verified. Wrong feather can make a bad day unrecoverable.
***
#### Drag hierarchy
<!-- id: me-drag-hierarchy | from: 13 | level: ME -->

- Worst drag: windmilling prop. Then gear, flaps, cowl flaps, sideslip, excessive bank/trim.
- `M:` clean + feather + blue line.
- `P:` gear up after positive climb/no runway; flaps up in stages as POH; prop feather after verify; cowl flaps as required.
- `T:` unfeathered failed prop can erase climb performance.
***
#### Vmc demo / reduced-speed training
<!-- id: me-vmc-demo-reduced-speed-training | from: 13 | also: me-train | level: ME -->

- Setup per POH/instructor/test guide; safe altitude; clearing; no real hazard; recover at first sign of loss of directional control/stall buffet/warning or prebriefed minimum.
- Recovery: reduce live-engine power enough to regain control + lower pitch/increase speed + wings/bank controlled.
- `T:` wrong instinct = add power/pull. Correct = reduce asymmetric thrust and increase airspeed.
- `T:` Vmc demo is not a macho manoeuvre; it is recognition and immediate recovery.
***
