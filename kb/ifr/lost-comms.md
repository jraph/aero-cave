# Lost communications / NORDO / Panne de communications / NORDO
<!-- concept: emg-comms | level: IR -->

[IFR index / Index IFR](README.md) · concept `emg-comms` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Lost comms — general
<!-- id: ifr-lost-comms-general | from: 09 -->

- `P:` squawk `7600`; listen; try other ATC/aircraft relay; comply with CAP/CFS/specific comm-fail instructions; phone ATS if all else fails.
- `T:` specific SID/STAR/IAP comm-fail procedure overrides generic. judgment required if uncovered case.
***
#### Lost comms — general · INRAT
<!-- id: ifr-lost-comms-general-inrat | from: 10 -->

- `P:` squawk `7600`; maintain listening watch; try alternate freq/FSS/relay/phone when practical; comply with specific SID/STAR/IAP/CAP comm-fail instructions.
- `T:` specific published comm-fail procedure overrides generic rules.
- `T:` if ATC says “if no comm by X, expect Y,” that can become expected route/alt/time logic.
***
#### Lost comms — IFR route / altitude / time
<!-- id: ifr-lost-comms-ifr-route-altitude-time | from: 09 -->

- VMC after fail: continue VFR, land as soon as practicable. `T:` practicable≠nearest unsuitable field.
- IMC route: assigned → vectored direct to specified fix/route/airway → expected → filed.
- IMC altitude: highest of assigned / minimum IFR altitude / expected. If vectored below published IFR altitude, climb immediately to appropriate minimum IFR altitude.
- Descent: maintain enroute altitude to nav facility/approach fix; start descent at latest of filed/amended ETA, last ATC-ack ETA, or EAT. If holding instruction: hold as directed; approach at EAT/EFC.
- `M:` route = `A-V-E-F`; alt = `highest A-M-E`; time = latest `ETA/EAT/EFC`.
***
#### Lost comms — VMC / IMC
<!-- id: ifr-lost-comms-vmc-imc | from: 10 -->

- VMC after failure: continue VFR and land as soon as practicable. `T:` practicable≠nearest unsuitable field.
- IMC route: `A-V-E-F` = assigned → vectored direct to fix/route/airway → expected → filed.
- IMC altitude: highest of `A-M-E` = assigned / minimum IFR altitude / expected. If vectored below published IFR altitude, climb immediately to appropriate minimum IFR altitude.
- Descent: maintain enroute altitude to nav facility/approach fix; descend at latest ETA/EAT/EFC logic. If holding instruction acknowledged, hold as directed and approach at `EAT/EFC`.
- `M:` lost comm = `7600 + VMC land / IMC AVEF + AME + latest time`.
***
