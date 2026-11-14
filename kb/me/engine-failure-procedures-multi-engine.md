# Engine-failure procedures (multi-engine) / Procédures de panne moteur (multimoteur)
<!-- concept: me-fail | level: ME -->

[Index](README.md) · concept `me-fail` · unit IDs are stable: never rename one.

***
#### Engine failure flow — generic
<!-- id: me-engine-failure-flow-generic | from: 13 | also: emg-engine | level: ME -->

- `P:` MAINTAIN CONTROL → POWER AS REQ → PITCH `Vyse/Vxse` → GEAR/FLAPS UP as appropriate → IDENTIFY → VERIFY → FEATHER → SECURE → CHECKLIST → PLAN.
- `M:` Control–Config–Identify–Verify–Feather–Secure–Checklist.
- `T:` in critical phase, memory items first; full checklist only after control and drag clean-up.
- `T:` do not rush feather below safe altitude if procedure/aircraft/training says simulate only.
***
#### Engine failure on takeoff / overshoot
<!-- id: me-engine-failure-on-takeoff-overshoot | from: 13 | also: emg-engine | level: ME -->

- `P:` recognize → control → power/config/drag in proper order → identify/verify → bank good engine → maintain heading ± practical → positive climb if capable → `Vxse` obstacle or `Vyse` rate → trim.
- TC test tolerances: heading control within about `±20°`; speed `Vxse/Vyse +10/-5` for overshoot scenario.
- `T:` gear/flap movement during power change is high workload; control first.
- `T:` OEI go-around may not climb. If not climbing, land under control.
***
#### Engine failure in cruise
<!-- id: me-engine-failure-in-cruise | from: 13 | also: emg-engine | level: ME -->

- `P:` control → maintain heading/alt if capable → set power/config → identify/verify → cause checks → feather/secure if no restart → trim → evaluate restart/divert.
- Turns OEI: bank not >`30°` in TC test context; use appropriate pitch/bank/trim.
- `T:` trying to hold altitude below OEI capability causes speed decay to Vmc/stall. Descend if required.
***
#### Precautionary shutdown
<!-- id: me-precautionary-shutdown | from: 13 | also: emg-engine | level: ME -->

- Reasons: oil pressure loss, severe vibration, fire risk, runaway prop, uncontrollable temps/pressures.
- `P:` confirm need → stabilize → identify/verify affected engine → reduce power → feather/secure per checklist → monitor live engine → divert/land.
- `T:` not every roughness = immediate shutdown; not every problem can wait. Decide by fire/mechanical damage/controllability.
***
#### PROP governor / feather — L4 cross-ref
<!-- id: me-prop-governor-feather-l4-cross-ref | from: 13 | also: agk-prop | level: ME -->

- `M` Typical **piston SE CS non-feather**: governor oil P↑→COARSE/pitch↑→RPM↓ | **piston ME CS full-feather**: oil P↑→FINE/pitch↓→RPM↑; oil P↓→counterweights/springs→FEATHER; **architecture varies**.
- `T` FINE low blade angle ≠ low RPM: low angle→RPM tendency↑ | COARSE high angle→RPM tendency↓ | FEATHER near airflow→drag↓; REVERSE negative thrust (ground only if approved).
- `!` OEI: windmilling low-pitch PROP→drag↑/climb↓ | **IDENTIFY→VERIFY→FEATHER** per POH; feather locks, unfeather pumps, accumulators ACFT-specific.
- `SRC:` [FAA AFH · ME propeller](https://www.faasafety.gov/files/events/SO/SO15/2022/SO15118118/TransitionToMultiengineAirplanes.pdf) | [08 Aircraft Systems · Powerplant / PROP](../../cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md).
***
#### Restart / unfeather
<!-- id: me-restart-unfeather | from: 13 | also: agk-prop | level: ME -->

- `P:` assess altitude/time/fire/damage/prop status/fuel/electrical. If feasible: restart checklist; if not: leave secured and land.
- `T:` restarting a damaged/fire engine can make problem worse. checklist and scenario drive.
***
#### OEI approach / landing
<!-- id: me-oei-approach-landing | from: 13 | level: ME -->

- `P:` brief long final, avoid rushed configuration, maintain `Vyse` or POH speed until landing assured, configure late/controlled, anticipate asymmetric power.
- Gear/flap only when landing assured unless procedure says otherwise. Power changes gradual; trim cautiously.
- `T:` full flap/gear early can remove climb escape. OEI go-around may be unavailable.
- `M:` stable > pretty. no salvage below minima/unstable.
***
#### OEI missed / go-around
<!-- id: me-oei-missed-go-around | from: 13 | also: ifr-missed | level: ME -->

- `P:` max allowable power live engine → control yaw/bank → pitch `Vyse/Vxse` → drag up in sequence → verify failed engine secure/feathered → trim.
- `T:` if unable climb, lower nose and land ahead/within available area. Do not pull below `Vyse` toward `Vmc`.
- `T:` high power + low speed + dirty config = Vmc trap.
***
#### Pebble
<!-- id: me-engine-failure-procedures-multi-engine-pebble | also: study-pebble | level: ME -->

- FLOW `Control–Config–Identify–Verify–Feather–Secure–Checklist | dead foot = dead engine | identify before verify; verify before feather | control first, checklist second | clean + feather + blue line`
- OEI `pitch Vyse/Vxse | bank toward good engine | cannot climb → land under control; do not pull below Vyse toward Vmc | high power + low speed + dirty = Vmc trap | gear/flap only when landing assured | OEI go-around may be unavailable`
- PROP `piston ME full-feather: oil pressure↑ → fine/RPM↑; oil loss → feather; architecture varies | windmilling drag↑, feather drag↓ | restarting a damaged/fire engine can make it worse`
***
