### IFR KNOW — AV-CAVE v0.2
`SEPTEMBER CPAER REVIEW: retained reference, not freshly revalidated` | use exact aircraft/current operational sources
`R` rule | `P` proc | `T` trap | `M` memory | `!` safety | Canada IFR study; current CAP/NOTAM/POH/SOP win
`RELEASE:` `OPS/EXAM-REF PROVISIONAL` | `CANONICAL SOURCE:` `ifr_knowledge_core_av_cave_v0_2.md` | `NOT FLIGHT AUTHORITY`
***
#### Current publication cycle

- Current `CAP/CAP GEN/CFS/AIP/DAH/charts` AIRAC cycle: effective `2026-07-09` through `2026-09-03`.
- These publications update every `56 days`; AIP SUP/AIC publish on a `14-day` cycle.
- `P preflight:` current publication→NOTAM→AIP SUP/AIC→airport/procedure page→aircraft data.
- Trigger NOTAM = notice that source material changed; retrieve the referenced amendment/Supplement. It may expire while the underlying AIP SUP remains active.
- `[NAV CANADA publication schedule; AIC 009/2026]`
***
#### Source / mindset

- AIM = guidance, not law. Current CAP/CAP GEN, CFS, AIP SUP and NOTAM govern published operational data.
- Local `CAP_GEN_03-19-2026.pdf` is expired; current cycle began `2026-07-09`.
- `T:` CAP is amended by NOTAM/AIP SUP. A Trigger NOTAM only announces changed source material; open the referenced source.
- IFR = clearance + obstacle clearance + nav accuracy + comms + fuel/alternate logic + workload discipline.
***
#### Clearance / readback

- Clearance memory: `CRAFT-ish` = clearance limit, route, altitude, frequency, transponder, plus void/release/hold-for-release if issued.
- `T:` clearance ≠ takeoff clearance. “climb/maintain” ≠ terrain clearance on visual/VFR restriction if you accepted separation duties.
***
#### IFR in VMC / VFR restriction

- IFR clearance with VFR restriction may be issued if pilot requests, outside Class A, within applicable B/C/D/E, and weather permits.
- `T:` during VFR restriction/release, pilot provides own separation incl wake; if unable, advise ATC/request amended clearance.
***
#### Lost comms — general

- `P:` squawk `7600`; listen; try other ATC/aircraft relay; comply with CAP/CFS/specific comm-fail instructions; phone ATS if all else fails.
- `T:` specific SID/STAR/IAP comm-fail procedure overrides generic. judgment required if uncovered case.
***
#### Lost comms — IFR route / altitude / time

- VMC after fail: continue VFR, land as soon as practicable. `T:` practicable≠nearest unsuitable field.
- IMC route: assigned → vectored direct to specified fix/route/airway → expected → filed.
- IMC altitude: highest of assigned / minimum IFR altitude / expected. If vectored below published IFR altitude, climb immediately to appropriate minimum IFR altitude.
- Descent: maintain enroute altitude to nav facility/approach fix; start descent at latest of filed/amended ETA, last ATC-ack ETA, or EAT. If holding instruction: hold as directed; approach at EAT/EFC.
- `M:` route = `A-V-E-F`; alt = `highest A-M-E`; time = latest `ETA/EAT/EFC`.
***
#### Minimum altitudes / terrain

- MEA = nav+obstacle; MOCA = obstacle + limited nav; MSA = emergency/sector; MVA not published to pilots.
- `T:` cleared direct ≠ terrain guaranteed unless ATC/radar/MEA logic valid. cold/RASS/temp corrections can raise minima.
***
#### Holds

- Hold clearance: fix, direction, radial/course/bearing/airway, leg length/time, altitude, EFC.
- Entries: direct / teardrop / parallel. `T:` entry method is aid; protected airspace matters more than pretty drawing.
- Timing: outbound adjusted to make inbound leg; wind correction triple outbound rough rule.
- `T:` no EFC? ask. fuel clock starts early.
***
#### CAP transition watch

- AIC `013/2026` announces a future PFAF/glidepath-intercept depiction using a lightning-bolt symbol.
- Incremental implementation starts `2026-10-29`, not in the current July cycle.
- Until a current chart actually shows it, read the symbols printed on that chart; do not assume the future convention.
***
#### Approach brief

- `P:` plate/eff date→airport/runway/proc→freq/nav source→MSA/RASS/cold temp→IAF/IF/FAF→altitudes/stepdowns→DA/MDA/HAT/HAA/vis→MAP→missed→runway/LDA/lights→threats.
- `M:` plate-wx-nav-alt-min-MAP-missed-rwy-threats.
- `T:` CDI source errors kill. brief both lateral/vertical mode and missed nav setup.
***
#### Approach types / minima

- Precision: lateral+vertical guidance with DA/DH. APV: vertical guidance but not precision. NPA: MDA/MAP.
- CAP minima box lists nav type, MDA/DA, HAA/HAT/HATh/DH, advisory visibility by aircraft category.
- `T:` LPV ≠ ILS; LNAV/VNAV temp limits matter if uncompensated Baro-VNAV.
***
#### RASS / altimeter

- Before IAP: current usable altimeter required; local or authorized remote. older than 60min caution; 90min current limit concept.
- RASS “when using X add N ft” ⇒ add to intermediate/final/missed segment minimum altitudes. “circling minima apply” ⇒ straight-in minima not usable under that RASS case.
- `T:` cold/remote/falling pressure corrections affect obstacle margin.
***
#### Landing minima / visual reference

- Do not continue below DH/DA or descend below MDA unless required visual reference established and maintained for safe landing.
- Visual refs include runway/markings/threshold/TDZ/approach lights/VGSI/RIL/threshold-end lights/edge/centreline/TDZL.
- Published landing visibilities are advisory only subject to approach ban; use to judge success probability.
- `!:` missed after MAP: obstacle clearance not assured.
***
#### Missed approach

- At DA/MDA/MAP without required visual reference, or unstable/unsafe, execute missed. Fly published lateral/vertical exactly.
- `T:` configure/power/pitch before nav cleanup. missed point is obstacle-clearance origin.
- Circling lost visual reference: follow circling missed logic; initially turn toward landing runway unless procedure/SOP directs otherwise, then intercept missed.
***
#### Alternate minima

| Facilities | Weather requirement |
|---|---|
| 2+ usable precision, separate suitable runways | `400-1` or `+200/+1/2` above lowest usable HAT/vis, greater |
| 1 usable precision | `600-2*` or `+300/+1` above lowest HAT/vis, greater |
| NPA only | `800-2*` or `+300/+1` above lowest HAT/HAA and vis, greater |
| No IFR approach | forecast ≥`500 ft` above min IFR alt permitting VFR approach/landing |

- Standard alternate minima: `600-2` or `800-2` as applicable; if standard applies, other authorized lower-vis options may apply from CAP table.
- TAF logic: improving `BECMG` at end; deteriorating `BECMG` at start; `TEMPO` not below alternate minima; `PROB` not below landing minima.
- GFA alternate: no cloud <`1000 ft` above lowest usable HAT/HAA, no CB, vis ≥`3 mi`. Advisory forecast alternate: ≥`500 ft` above lowest usable HAT/HAA and vis ≥`3 mi`.
- `T:` alternate use depends on aircraft performance, nav equipment, NAVAIDs/NOTAM, forecast type, wind/runway, and chart “alternate not authorized.”
***
#### GNSS / RNAV

- Check database current, RAIM/WAAS availability, correct procedure, correct sensitivity/mode, and missed approach sequencing.
- Alternate with satellite approach: verify expected RAIM/WAAS integrity at ETA; destination+alternate satellite-use separation rules may apply.
- `T:` “GPS direct” ≠ cleared route unless ATC cleared. OBS/SUSP misuse common.
***
#### RVR / approach ban

- RVR = automated runway visual range for landing/takeoff direction. Use current approach-ban rules; category/operator-specific.
- `T:` advisory vis not same as approach-ban controlling visibility. CAP/CAR/operator ops spec wins.
***
#### IFR emergencies

- Emergency: aviate; declare; ATC expects necessary action and will assist. If no comm, `7700` can indicate emergency but may not be detected.
- Equipment fail: report nav/comm malfunctions to ATC. Partial panel: attitude-power-performance; reduce workload, ask vectors/no-gyro if needed.
- Icing: exit conditions early; climb/descend/turn; approach speed/config per POH/SOP. `T:` “trace” can become performance problem fast in trainer.
***
#### Pebble

- clearance CRAFT | lost comm 7600/listen/relay/phone | VMC land practicable | IMC route A-V-E-F | altitude highest A-M-E | descent latest ETA/EAT/EFC | hold direct/teardrop/parallel | brief plate-wx-nav-alt-min-MAP-missed-rwy-threats | DA/MDA needs visual refs | missed after MAP no assured OC | alternate 400-1 / 600-2 / 800-2 | BECMG end/start, TEMPO alt-min, PROB landing-min | current CAP/NOTAM wins.

***
#### Current-source notes — v0.2

- CAP/CFS/AIP cycle validated effective `2026-07-09` to `2026-09-03`.
- Trigger-NOTAM workflow validated against AIC `009/2026`.
- PFAF depiction transition dated from AIC `013/2026`; first implementation `2026-10-29`.
