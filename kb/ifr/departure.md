# Departure: takeoff minima, SID / ODP & climb gradient / Départ : minimums de décollage, SID / ODP et pente de montée
<!-- concept: ifr-dep | level: IR -->

[IFR index / Index IFR](README.md) · concept `ifr-dep` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Departure / takeoff minima
<!-- id: ifr-departure-takeoff-minima | from: 10 -->

- Check CAP aerodrome chart/SID/ODP/diverse departure, climb gradient, obstacle notes, RVR/visibility, lighting, engine-out capability if applicable.
- `R:` takeoff visibility precedence: use runway `RVR` when reported at/above the applicable minimum; use aerodrome `ground visibility` when RVR is below minimum, varies below/above minimum, or is not reported; use PIC-observed `runway visibility` only when neither RVR nor ground visibility is reported. `[CAR 602.126]`
- Applicable minimum comes from the AOC/special authorization, or the current CAP for other operations.
- `T:` takeoff visibility ≠ landing/approach visibility. Departure obstacle climb gradient may be more restrictive than weather.
- `T:` “standard takeoff minima” is not “safe to climb over obstacles”; compare required climb gradient vs aircraft performance.
***
#### SID / ODP / climb gradient
<!-- id: ifr-sid-odp-climb-gradient | from: 10 -->

- SID = published ATC/obstacle/departure routing; may include altitude/speed/climb gradient.
- Diverse departure assumes obstacle environment supports generic departure; if obstacle DP exists, use it unless ATC assigns otherwise.
- Climb gradient in `ft/NM`; common 3.3% ≈ `200 ft/NM`. Formula (`ROC fpm = GS × ft/NM / 60`) and GS/tailwind trap: see `agk-climb-descent-gradient`.
***
#### Takeoff visibility / RVR trap
<!-- id: ifr-takeoff-visibility-rvr-trap | from: 10 | also: ifr-minima -->

- RVR report can be below takeoff minimum but ground visibility at/above minimum may govern; inverse also possible.
- If both lowest RVR and ground visibility are below required minimum, takeoff not authorized.
- If only RVR below minimum and no governing ground visibility at/above minimum, takeoff not authorized.
- `T:` “variable RVR” and “observed on-the-hour vs now” wording can flip the answer.
***
#### SIDs, radar and non-radar departures — AIM RAC 7
<!-- id: ifr-sid-radar-non-radar-departures | level: IR -->

- First contact: destination + planned initial cruise altitude. Clearance via CLNC DEL if listed, else ground after taxi auth. [RAC 7.3–7.4]
- SID types: **vector SID** (radar: ATC vectors to filed route/termination fix) · **pilot-nav SID** (non-radar: fly published tracks yourself) · PBN SID. Clearance names SID, transition, when to expect climb. [RAC 7.6; CAP GEN]
- SID in clearance → readback only call sign + code (+ amended altitude). Can refuse SID and ask for detailed clearance. Amended altitude does not cancel SID. [RAC 6.1, 7.6]
- No SID: departure procedure (ODP) or take-off minima premise: 35 ft at DER → straight to **400 AAE** → **200 ft/NM** to enroute altitude. `NOT ASSESSED` = pilot owns obstacles. [RAC 7.8; CAP GEN]
- "Right turn, climb on course" is not a departure procedure. [RAC 7.8]
- Release from tower: inside TCA tower hands off; outside, tell tower next agency/freq unless already given. [RAC 7.9]
- `T:` vector SID = expect vectors; still fly the published initial heading/altitude until vectored.
***
#### IFR departure from an uncontrolled aerodrome — AIM RAC 7.10
<!-- id: ifr-departure-uncontrolled-aerodrome-rac-7-10 | level: IR -->

- Into controlled airspace: get ATC clearance first (often via FIC/RCO or phone). [RAC 7.10]
- Broadcast departure intentions on MF/ATF before entering runway; confirm no conflict by radio + visually. [RAC 7.10]
- Keep listening watch on MF until beyond its distance/altitude; then contact ATC/en route frequency (second radio helps). [RAC 7.10]
- Clearance may be time-limited: "CLEARANCE CANCELLED IF NOT AIRBORNE BEFORE 1349". Not departing within 60 min of proposed time → tell ATC. [RAC 7.10]
- IFR clearance with VFR climb, or VFR release until IFR clearance: only on request, weather permitting. [RAC 6.2.1–6.2.2]
- `T:` uncontrolled departure = your own obstacle + traffic separation until in controlled airspace.
***
#### Pebble
<!-- id: ifr-departure-pebble -->

- TKOF VIS CAR 602.126 `RWY RVR when reported at/above minimum | ground visibility when RVR below minimum, varying, or not reported | PIC-observed runway visibility only when neither reported | minimum from AOC/special authorization, else current CAP`
- T `both lowest RVR and ground vis below minimum → no takeoff | takeoff vis ≠ landing/approach vis | standard takeoff minima ≠ obstacle clearance`
- GRADIENT `ft/NM | 3.3% ≈ 200 ft/NM | formula → agk-climb-descent-gradient`
- SID / ODP `SID may include altitude/speed/climb gradient | obstacle DP exists → use it unless ATC assigns otherwise`
- DEPARTURE `vector SID = radar · pilot-nav SID = own nav | no SID: 35 ft DER → 400 AAE → 200 ft/NM | uncontrolled: clearance first, broadcast, MF watch, void time`
***
