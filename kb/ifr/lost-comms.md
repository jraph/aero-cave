# Lost communications / NORDO / Panne de communications / NORDO
<!-- concept: emg-comms | level: IR -->

[IFR index / Index IFR](README.md) · concept `emg-comms` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Lost comms — general
<!-- id: ifr-lost-comms-general | from: 09, 10 -->

- `P:` squawk `7600`; maintain listening watch; try alternate freq/FSS/other ATC/aircraft relay; comply with specific SID/STAR/IAP/CAP/CFS comm-fail instructions; phone ATS when practical / if all else fails.
- `T:` specific published SID/STAR/IAP comm-fail procedure overrides generic rules; judgment required if uncovered case.
- `T:` if ATC says “if no comm by X, expect Y,” that can become expected route/alt/time logic.
***
#### Lost comms — VMC / IMC route, altitude, time
<!-- id: ifr-lost-comms-ifr-route-altitude-time | from: 09, 10 -->

- VMC after fail: continue VFR, land as soon as practicable. `T:` practicable≠nearest unsuitable field.
- IMC route: assigned → vectored direct to specified fix/route/airway → expected → filed.
- IMC altitude: highest of assigned / minimum IFR altitude / expected. If vectored below published IFR altitude, climb immediately to appropriate minimum IFR altitude.
- Descent: maintain enroute altitude to nav facility/approach fix; start descent at latest of filed/amended ETA, last ATC-ack ETA, or EAT. If holding instruction acknowledged: hold as directed; approach at EAT/EFC.
- `M:` route = `A-V-E-F`; alt = `highest A-M-E`; time = latest `ETA/EAT/EFC`.
- `M:` lost comm = `7600 + VMC land / IMC AVEF + AME + latest time`.
***
#### Pebble
<!-- id: ifr-lost-comms-pebble | also: study-pebble -->

- LOST COMM `7600 + listening watch + alternate freq/FSS/relay/phone | specific published SID/STAR/IAP procedure overrides generic rules`
- VMC `continue VFR, land as soon as practicable | practicable ≠ nearest unsuitable field`
- IMC `route A-V-E-F = assigned → vectored direct to fix/route/airway → expected → filed | altitude = highest of A-M-E = assigned / minimum IFR altitude / expected | vectored below published IFR altitude → climb immediately`
- DESCENT `maintain enroute altitude to nav facility/approach fix | start at latest of filed/amended ETA, last ATC-acknowledged ETA, or EAT | holding acknowledged: hold as directed, approach at EAT/EFC`
***
