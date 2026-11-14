# IFR planning, fuel & alternates / Planification IFR, carburant et dégagement
<!-- concept: ifr-plan | level: IR -->

[IFR index / Index IFR](README.md) · concept `ifr-plan` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### IFR flight planning workflow
<!-- id: ifr-ifr-flight-planning-workflow | from: 10 -->

- Route: CFS/CAP/LO chart/preferred routes/airways/direct fixes/MEA/MOCA/AMA/MSA/mountainous region/controlled airspace.
- Weather: METAR/SPECI actual; TAF legality; GFA area; FD winds/temp; SIGMET/AIRMET/PIREP; NOTAM; RSC/CRFI; freezing level.
- Leg calc: `TC±VAR=MC±DEV=CH`; `time=dist/GS`; `fuel=time×burn`; `ETA=dep+ETE`; `wind correction` and actual GS.
- `T:` simulated flight questions often test route feasibility, not one isolated fact.
***
#### IFR fuel — CAR 602.88 memory
<!-- id: ifr-ifr-fuel-car-602-88-memory | from: 10 | also: law-plan -->

- IFR prop with alternate: dest + approach + missed → alternate + land → `45 min`.
- IFR prop no alternate: dest + approach + missed → `45 min`.
- IFR turbojet/helicopter: same logic but `30 min`.
- Always add foreseeable taxi/delay/met/routing/traffic/other delays.
- `T:` fuel reserve is after required legs, not “fuel on board at destination.” Exam may hide missed approach before alternate leg.
***
#### Simulated IFR flight workflow
<!-- id: ifr-simulated-ifr-flight-workflow | from: 10 | also: ifr -->

- `1 Documents:` current CAP/CFS/LO/NOTAM/TAF/METAR/GFA/FD/SIGMET/PIREP.
- `2 Route:` dep SID/ODP → enroute MEA/MOCA/AMA → STAR/approach → alternate.
- `3 Weather:` dest legal? alternate legal? icing/TS/turb/wind/RVR/approach ban? freezing level? runway state?
- `4 Fuel:` taxi/delay + trip + app/missed + alternate + reserve + foreseeable.
- `5 Plates:` RASS/cold temp, minima, stepdowns, MAP, missed, lighting, runway length.
- `6 Calculations:` GS/ETE/fuel, climb gradient fpm, descent rate, hold timing, alternate minima.
- `7 Decision:` legal? safe? equipped? current? if no, what changes?
***
#### Pebble
<!-- id: ifr-planning-fuel-pebble | also: study-pebble -->

- FUEL CAR 602.88 `prop + alternate: dest + approach + missed → alternate + land → 45 min | prop no alternate: dest + approach + missed → 45 min | turbojet/helicopter: 30 min | add foreseeable taxi/delay/met/routing/traffic`
- T `reserve is after required legs ≠ fuel on board at destination | exam may hide the missed approach before the alternate leg`
- WORKFLOW `documents → route → weather → fuel → plates → calculations → decision: legal? safe? equipped? current?`
- LEG `TC±VAR=MC±DEV=CH | time = dist/GS | fuel = time×burn | ETA = dep + ETE`
***
