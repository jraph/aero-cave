### IFR PROCEDURES QRC — AV-CAVE v0.2
`SEPTEMBER CPAER REVIEW: retained reference, not freshly revalidated` | use exact aircraft/current operational sources
`P` procedure | `G` gate | `T` trap | `M` memory | `!` safety | `?` verify | Canada IFR; POH/AFM/SOP/current CAP/NOTAM win
`RELEASE:` `OPS/STUDY-REF / AIRCRAFT-DEPENDENT` | `CANONICAL SOURCE:` `ifr_procedures_qrc_av_cave_v0_2.md` | `NOT FLIGHT AUTHORITY`
***
#### Current publication cycle

- Current `CAP/CAP GEN/CFS/AIP/DAH/charts` AIRAC cycle: effective `2026-07-09` through `2026-09-03`.
- These publications update every `56 days`; AIP SUP/AIC publish on a `14-day` cycle.
- `P preflight:` current publication→NOTAM→AIP SUP/AIC→airport/procedure page→aircraft data.
- Trigger NOTAM = notice that source material changed; retrieve the referenced amendment/Supplement. It may expire while the underlying AIP SUP remains active.
- `[NAV CANADA publication schedule; AIC 009/2026]`
***
#### Scope / discipline

- `SRC:` current CARs/TC AIM/CAP/CFS/NOTAM + aircraft POH/AFM/SOP. TC flight-test guide = training/evaluation guidance, not legal authority.
- `M:` aviate→navigate→communicate; configure early; verify source/mode; brief missed before FAF.
- `T:` this QRC is generic. Aircraft memory items, speeds, automation logic, icing limitations and engine-out actions are aircraft-specific.
***
#### Before engine start — IFR readiness

- `P:` weather→current CAP/CFS/AIP→NOTAM→AIP SUP/AIC→RSC→route/altitudes→fuel/alternate→W&B/performance→database/RAIM-WAAS→equipment/defects→personal minima.
- Set paper/electronic backup, frequencies, route, departure plate, emergency/alternate plan.
- `G:` legal + equipped + current + fuel + performance + escape options.
- `T:` a valid clearance does not make an unsafe weather/icing/performance decision safe.
***
#### Clearance copy

- `M:` `CRAFT+` = clearance limit | route | altitude | frequency | transponder | release/void/EFC/restrictions.
- `P:` copy verbatim→compare filed/expected→mark initial altitude and top altitude→identify SID/transition→read back limit/route/altitude/restrictions/squawk.
- Ask immediately if ambiguous, impossible, below safe altitude, equipment-incompatible or route not understood.
- `T:` takeoff clearance is separate. “Expect” altitude is not authorization to climb.
***
#### IFR cockpit / instrument check

- `P:` documents/database/current plates→pitot/static heat as req→altimeters set/cross-check→heading indicators aligned→turn instrument/compass during taxi→nav/comms identified→GPS annunciations→autopilot disconnect/test per POH.
- Taxi turns: heading/compass turn correctly; attitude remains erect; turn coordinator/indicator responds; ball opposite turn; no abnormal flags.
- `T:` never accept a failed instrument because GPS “looks fine.”
***
#### Departure brief

- `P:` runway/TODA-ASDA if relevant→takeoff minima→SID/ODP→initial heading/track→first fix→initial altitude→top altitude→freq→climb gradient→terrain→weather→engine/instrument failure plan.
- `M:` `RWY-PATH-ALT-FREQ-GRAD-THREATS-FAIL`.
- State: reject criteria; failure before/after liftoff; return vs continue; lost-comms path; automation plan.
- `T:` ATC vector does not erase obstacle/climb-gradient requirements before radar protection is assured.
***
#### Before-takeoff IFR gate

- `G:` clearance understood/read back | runway verified | instruments green | nav source correct | departure loaded/activated | initial course/heading set | altitude bugged | squawk/Mode C | frequencies staged | timer/clock | takeoff brief complete.
- `P:` heading bug→initial altitude→first nav leg→departure frequency→transponder→lights/pitot heat→doors/checklist.
- `T:` wrong runway + correct SID is still wrong.
***
#### Takeoff / initial climb

- `P:` runway/heading cross-check→power set/engine instruments→airspeed alive→rotate/climb→positive rate/gear as applicable→track runway/SID→instrument transition→after-TKOF flow/checklist.
- TC flight-test context: instrument control once airborne and above `400 ft AAE`, unless departure procedure specifies otherwise.
- Maintain assigned heading/track/altitude; verify course indications correspond to selected equipment.
- `T:` do not chase needles immediately after liftoff; attitude/power first, then trim/nav.
***
#### Climb gradient check

- `F:` required `fpm = GS × ft/NM ÷ 60`.
- `P:` compare expected GS/ROC with published requirement before departure; monitor actual performance.
- `T:` tailwind raises GS and required fpm. If unable, advise ATC before takeoff or immediately when recognized.
***
#### Enroute flow

- `P:` level→power→trim→mixture/engine→altimeter setting→heading/nav cross-check→fuel/time→weather/icing→next frequency/fix/altitude.
- `M:` `A-P-T-N-E-F`: altitude, power, trim, nav, engine, fuel.
- Cross-check raw data vs GPS/autopilot; verify every direct-to/route amendment before EXEC/activate.
- `T:` automation follows the programming error precisely.
***
#### ATC amendment

- `P:` write→read back→confirm aircraft state→modify one system at a time→verify active leg/course/altitude→monitor turn/intercept.
- If saturated: “stand by,” request vector, delay descent, or ask for clarification.
- `T:` heads-down programming during turn/descent = loss-of-control/setup-error trap.
***
#### Arrival setup

- `P:` weather/ATIS→NOTAM/runway→approach choice→plate current→altimeter/RASS/cold temp→category/minima→landing performance→missed/alternate→fuel.
- Load procedure with correct transition; verify waypoint sequence against plate; stage frequencies/courses; set minimums and missed altitude.
- `M:` `WX-PLATE-NAV-MIN-MISSED-RWY-FUEL`.
- `T:` loading an approach is not clearance to fly it or descend.
***
#### Hold clearance copy

- `M:` `F-D-C-L-A-E` = fix | direction | course/radial/bearing | leg length/time | altitude | EFC.
- `P:` copy/read back→slow before fix→determine inbound course/turn direction→choose safe entry→brief wind/timing/fuel/EFC→report entry if required.
- `T:` no EFC or fuel ambiguity? ask.
***
#### Hold entry / execution

- `P:` cross fix→entry→correct side/protected airspace→time outbound abeam/wings-level as appropriate→intercept inbound→adjust timing/wind.
- Entry: direct / teardrop / parallel; any suitable entry that remains protected is acceptable.
- Wind rough rule: outbound drift correction ≈ `3×` inbound correction; adjust outbound time to achieve inbound target.
- TC test targets: track/course `±10°` or within ½-scale, airspeed `±10 kt`, altitude `±100 ft`.
- `T:` perfect entry sketch with poor fuel awareness is failure. Continuously compute max holding time and alternate fuel.
***
#### Approach clearance / vector-to-final

- `P:` hear approach/runway/route/altitude→read back→verify clearance does not descend below published/assigned minimum→set intercept heading/course/source→arm correct mode only when appropriate.
- On vectors: maintain last assigned altitude until cleared lower or established as required by clearance/procedure.
- `T:` approach clearance ≠ landing clearance.
***
#### Chart-symbol transition

- Use current-chart symbology. The future PFAF lightning-bolt depiction begins incrementally `2026-10-29`; do not apply it to July-cycle plates unless printed.
***
#### Approach brief — compact

- `P:` “[procedure/runway], current plate; nav/freq/course; IAF/FAF altitudes; RASS/cold correction; category/minima/vis; MAP; missed climb-turn-fix-altitude; runway/LDA/lights; threats.”
- `M:` `PROC-NAV-ALT-MIN-MAP-MISSED-RWY-THREATS`.
- Pilot-monitoring/self-brief challenge: source? mode? next altitude? next fix? missed action?
***
#### Approach setup gate

- `G:` plate current | NOTAM checked | altimeter source/correction | frequencies identified | CDI source correct | course set | procedure sequence verified | minimums bugged | missed altitude/nav briefed | landing checklist planned.
- `T:` green vs magenta needles; LOC vs ILS minima; LNAV vs LPV annunciation; wrong transition.
***
#### Before FAF / FAWP gate

- `P:` landing checklist→speed/config plan→altitude verified→approach mode active/armed correctly→course alive→timer if required→missed mentally rehearsed.
- RNAV: confirm approach-active mode within `2 NM` before FAWP inbound when required by TC test criteria.
- `G:` stable enough to continue; if behind, request delay/vector or go missed.
- `T:` do not descend because vertical guidance appears unless correct mode/procedure/altitude intercept conditions are verified.
***
#### Stable approach guide

- TC generic test guide: proper configuration, brief/checklist complete, appropriate power, lateral/vertical within ½-scale for ILS/LPV/LNAV-VNAV, sink ≤`1000 fpm`, speed within `+20/-0`, only small corrections.
- Stable by `1000 AGL` in IMC / `500 AGL` in VMC; otherwise missed/go-around.
- `CONTEXT:` TC instrument flight-test guide criterion; not a CAR approach minimum. Operator/school SOP may be tighter.
- `T:` training/SOP criteria may be tighter. Becoming unstable after the gate still requires a missed approach.
***
#### NPA / CDFA

- Prefer CDFA when practical for NPA with suitable slope.
- `P:` calculate descent→cross FAF at/above altitude→constant descent→respect every stepdown→level at/above MDA if required or treat MDA as decision-style altitude when visual references not imminent.
- No descent below MDA without required visual reference; no missed-approach turn before MAP.
- `T:` CDFA does not turn MDA into a legal DA. Prevent momentum from carrying below MDA.
***
#### ILS / LPV / LNAV-VNAV

- `P:` intercept lateral course→vertical path from valid position/below as applicable→confirm correct annunciation→small corrections→cross-check altitude/distance→DA decision.
- ILS/LPV: maintain no more than ½-scale deviations for test standard; at DH/DA without required visual reference→missed.
- `T:` false glideslope from above; LPV≠ILS; LNAV/VNAV temperature limits; automation downgrade can change minima.
***
#### LNAV / VOR / LOC / NDB

- `P:` identify source→course/raw-data check→FAF altitude→CDFA/stepdowns→MDA→MAP identification.
- Start timer when required; verify DME/GPS waypoint sequence; maintain MDA until visual descent or MAP.
- `T:` LOC approach uses LOC minima. “Glideslope available” does not authorize ILS minima if not cleared/equipped/identified.
***
#### Visual transition

- `G:` required visual reference established and maintained + normal descent/landing possible + runway/traffic/clearance understood.
- Transition with minimal manoeuvring; remain within limitations; confirm landing clearance at controlled airport.
- `T:` runway lights in sight do not automatically mean position/rate permit a safe landing.
***
#### Missed approach — universal flow

- `P:` POWER→ATTITUDE→CONFIG→TRACK→NAV→TALK→CHECKLIST.
- Initiate promptly at MAP/MAWP or DH/DA, or earlier if unstable/unsafe/unable.
- Follow published missed or ATC modification; report missed; climb to published/cleared altitude; advise if unable climb gradient/restriction.
- TC test targets: airspeed `+10/-5`, heading/track `±10°`, altitude `±100 ft`.
- `T:` first turn no earlier than published/MAP requirements. Do not level beyond MAP searching for runway.
***
#### Missed approach setup

- Before FAF know: initial climb altitude, straight-ahead requirement, turn altitude, direction, fix/hold, nav source, frequency, minimum climb gradient.
- GNSS: know `SUSP/OBS` sequencing and when to activate missed; verify unit-specific procedure.
- `T:` pressing buttons before pitch/power/config creates CFIT/loss-of-control risk.
***
#### Circling

- `P:` use correct category/minima→identify runway/traffic→remain visual/protected→configure conservatively→bank ≤aircraft/SOP limits→stable normal descent.
- Lost visual: execute missed; initially manoeuvre toward landing runway as appropriate, then intercept published missed per plate/SOP.
- `T:` speed above category may require higher category. Night/marginal circling deserves higher personal minima.
***
#### Lost communications — immediate

- `P:` maintain control/clearance→check volume/squelch/audio panel/mic/PTT/frequency/circuit breakers per POH→try last/next/121.5/FSS/relay→listen on NAV/voice→squawk `7600`.
- Transmit blind with intentions/position/altitude; monitor for light signals if applicable; use phone after landing.
- `T:` specific SID/STAR/IAP comm-fail instructions override generic memory.
***
#### Lost communications — route / altitude / time

- VMC after failure: continue VFR and land as soon as practicable.
- IMC route: `A-V-E-F` = assigned→vectored direct to specified fix/route/airway→expected→filed.
- IMC altitude: highest `A-M-E` = assigned / minimum IFR altitude / expected.
- Descent/approach timing: use applicable latest ETA/EAT/EFC logic and published procedure.
- `T:` generic mnemonic cannot answer every uncovered scenario; exercise judgment and comply with published instructions.
***
#### Vacuum / attitude-heading failure

- `P:` recognize flag/inconsistent indications→cover/ignore failed instruments→level using reliable instruments→power/trim→advise ATC→request vectors/no-gyro or suitable approach→reduce workload.
- Cross-check turn instrument, compass, ASI, ALT, VSI, GPS track if approved/reliable.
- `T:` slow-failing gyro can look plausible. Confirm with multiple instruments.
***
#### No-gyro vectors

- ATC may instruct “start turn/stop turn”; use standard-rate turns unless otherwise instructed, half-standard on final if directed/appropriate.
- `P:` acknowledge→stabilize altitude/speed→turn on command→stop promptly→monitor compass/turn instrument.
- `T:` no-gyro vector does not replace terrain/altitude responsibility outside ATC protection.
***
#### Pitot/static failure

- Pitot blocked + drain open: ASI→zero. Pitot+drain blocked: ASI altitude-like. Static blocked: ALT freezes; VSI zero; ASI errors with altitude changes.
- `P:` pitot heat→alternate static per POH→use attitude/power/GPS/known settings→advise ATC→land.
- `T:` alternate static may change indications; know aircraft correction.
***
#### Electrical failure

- `P:` confirm alternator/gen failure→reset only per POH→shed load→estimate battery endurance→preserve comm/nav/gear/flaps→declare/divert/land before total loss.
- Turn off nonessential lights/heaters/chargers; plan manual gear/flap or handheld backup if applicable.
- `T:` low-voltage light is time-critical in IMC/night.
***
#### Autopilot / trim runaway

- `P:` disconnect→override/control→pull appropriate breaker/switch per POH→retrim manually→advise ATC/request lower workload.
- `T:` autopilot masks developing attitude/trim problem until disconnect. Keep hand near disconnect during approach.
***
#### Unusual attitude — nose high

- `P:` recognize reliable instruments→power as required/reduce if near stall? aircraft-specific→lower pitch/AoA→level wings→recover to assigned attitude/altitude smoothly.
- Generic training memory: add power as appropriate, lower nose, level wings; avoid stall/yaw.
- `T:` exact sequence varies with aircraft/attitude; POH/instructor method wins.
***
#### Unusual attitude — nose low

- `P:` power idle/reduce→level wings→ease out→avoid overspeed/excess g→re-establish power/trim.
- `T:` pulling before levelling increases load factor/spiral.
***
#### Icing encounter

- `P:` exit immediately: turn/climb/descend toward known non-icing→pitot/static/prop/windshield/boots/heat per POH→advise ATC→increase speed/config margins per POH→plan nearest suitable landing.
- Avoid flap/config changes that create tailplane/handling risk unless POH directs.
- `T:` non-approved aircraft: “trace” is already an escape event, not a monitoring plan.
***
#### Convective / severe turbulence

- `P:` avoid; ask deviation early. If inadvertent: turbulence penetration speed/attitude per POH, autopilot off if required, accept altitude variation, do not chase, exit shortest safe route.
- `T:` onboard weather shows history/attenuation; never use it to thread cells.
***
#### Engine abnormal in IMC

- `P:` control/attitude→power/config→identify issue→checklist→declare→nearest suitable approach/landing.
- Single engine aircraft: maintain glide/partial-power option; avoid descending below terrain escape altitude prematurely.
- Multi-engine: maintain `Vyse`/control, clean/identify/verify/feather per aircraft; OEI missed may be impossible.
- `T:` troubleshooting fixation + IMC = spatial disorientation/CFIT.
***
#### ATC workload tools

- Use: “unable,” “stand by,” “request vectors,” “request lower,” “request block altitude,” “minimum fuel,” `PAN PAN`, `MAYDAY`.
- Declare early when safety margin reduced; state equipment failure, capability, fuel, souls, intentions.
- `T:` ATC cannot help with a problem you hide.
***
#### Final approach callouts — single pilot

- `P:` altitude/fix→source/mode→course alive→glidepath alive→FAF→gear/config→minimums approaching→minimums/MAP→land or missed.
- Speak next action: “At minimums: required visual reference or missed.”
- `T:` silence under high workload permits mode/altitude errors.
***
#### Post-landing

- `P:` clear runway fully→stop/after-landing flow→ground clearance→close flight plan if required→record defects/fuel/approach issues.
- `T:` do not reconfigure heads-down while still on runway.
***
#### Pebble

- preflight `legal-equipped-current-fuel-performance-options` | clearance `CRAFT+` | dep brief `RWY-PATH-ALT-FREQ-GRAD-THREATS-FAIL` | gate source/course/alt/freq/squawk | hold `F-D-C-L-A-E` | approach `PROC-NAV-ALT-MIN-MAP-MISSED-RWY-THREATS` | before FAF source-mode-alt-min-missed | stable guide `1000 IMC/500 VMC` | NPA CDFA but never below MDA | missed `POWER-ATT-CONFIG-TRACK-NAV-TALK` | lost comm `7600 + AVEF + highest AME` | partial panel reliable instruments + ATC help | icing exit now | unable early.

***
#### Current-source notes — v0.2

- Current CAP/CFS cycle validated `2026-07-09` to `2026-09-03`.
- NOTAM + AIP SUP check added because Trigger NOTAMs may expire while SUP remains active.
