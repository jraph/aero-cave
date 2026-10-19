### VFR FTM PROC — AV-CAVE v0.2
`P` proc | `T` trap | `F` formula | `M` memory | `!` safety | `?` check | `POH>` aircraft-specific | `SOP>` school-specific
`RELEASE:` `STUDY / AIRCRAFT-DEPENDENT` | `CANONICAL SOURCE:` `vfr_ftm_proc_av_cave_v0_2.md` | `NOT FLIGHT AUTHORITY`
***
#### Core

- `P:` ATT→PWR→TRIM. LOOKOUT→ATT→PWR→PERF→TRIM→SCAN. Outside picture primary; instruments confirm.
- `T:` trim≠control. chasing ASI late; set attitude first.
***
#### Taxi / pre-takeoff

- `P:` brake chk→steer→wind ctrl→walk-ish speed→clear path. Runup/pre-TKOF before active.
- `!:` loose items/belts/doors/fuel/trim/controls/mags/carb heat/temps-pressures.
***
#### Normal takeoff

- `P:` line-up runway/HDG chk→heels floor→full pwr smooth→engine green→ASI alive→rudder centreline→rotate `[POH]`→climb attitude→track runway→after-TKOF.
- `T:` rudder keeps centreline. reject early if no full power/no ASI/rough while runway remains.
***
#### Crosswind takeoff

- `P:` aileron into wind→reduce as speed↑→rudder centreline→rotate+prevent drift→airborne crab to track runway.
- `T:` drift≠yaw. ground track matters.
***
#### Short / obstacle takeoff

- `P:` POH config→max usable runway→brakes?→full pwr→green→rotate POH→`Vx` until clear→`Vy/normal`.
- `M:` obstacle = height/distance ⇒ `Vx`.
- `T:` Vx long climb = poor cooling/visibility; use only as needed.
***
#### Soft / rough takeoff

- `P:` keep moving→nose light/up→liftoff in ground effect→level just clear→accelerate→climb `[POH]`.
- `M:` unstick early, don’t climb early.
- `T:` ground effect can lie; climb before safe speed ⇒ sink/stall.
***
#### Climb

- `P:` attitude+pwr set→trim→lookout→temps/pressures→track. `Vy/normal`; `Vx` obstacle.
- `T:` high nose = low energy/heat/poor vis. wind correction after departure.
***
#### Circuit

- `P:` TKOF→crosswind→downwind→base→final. default LH unless published/cleared. normal `1000 AAE`.
- `P:` after TKOF straight ~`500 AAE`→crosswind→circuit height. downwind parallel/spacing/pre-LDG. base by wind/spacing. final centreline/profile/speed/config/aimpoint.
- `T:` headings change with wind; ground track matters. lookout all legs.
***
#### Normal landing

- `P:` aligned→stabilized→speed `[POH]`→descent path→aimpoint fixed→flare→holdoff→land.
- `T:` aimpoint up=low/undershoot; down=high/overshoot. flare high=drop; late=flat/hard.
***
#### Crosswind landing

- `P:` crab to track OR wing-low sideslip. touchdown longitudinal axis aligned. rollout: more aileron into wind as speed↓.
- `T:` crab tracks; slip aligns. no side-load at touchdown.
***
#### Slip

- `P:` forward slip=bank+opposite rudder→↑ROD no ↑IAS. side slip=wing low into wind+opposite rudder→no drift.
- `T:` flap+slip only if POH allows. recover before flare unless side-slip XW landing.
***
#### Go-around

- `P:` power full/smooth→attitude climb→carb heat cold→stop sink→flaps staged POH→climb speed→track→communicate.
- `M:` Power–Attitude–Config–Track–Talk.
- `T:` trim may be nose-up; flap up too fast/low energy ⇒ sink.
***
#### Precautionary landing

- `P:` doubt site/wx/fuel/light/health/mech ⇒ inspect before commitment. overhead/normal circuit→safe low inspection beside runway/site→repeat if needed→land/leave.
- `T:` don’t rush unless fuel/dark/wx force abbreviated inspection. bad site? leave early.
***
#### Forced landing

- `!:` POH emergency checklist wins.
- `P:` engine fail=CONTROL→CARB HEAT→TRIM→FIELD→PLAN. then time permitting CAUSE→MAYDAY→PAX→SECURE→LAND.
- `M:` Control–Field–Plan–Cause–Mayday–Pax–Secure–Land.
- `T:` glide trimmed = judgement possible. troubleshooting never replaces landing plan.
***
#### EFATO

- `P:` nose down `Vg/POH`→landing path→small turns only→land. below safe turnback alt: NOSE–FIELD–LAND.
- `T:` impossible turn = pull+bank+low AS⇒spin.
***
#### Engine fail in circuit / from altitude

- `P:` glide speed→choose runway/field→forced pattern. key pattern: high key→low key abeam→base/final.
- `F:` high key AGL≈`2 min glide loss + 200 ft`. strong wind⇒key closer.
- `T:` high is fixable; low usually not. flap/slip once landing assured.
***
#### Mayday / pax / secure

- `P:` MAYDAY×3→ident→problem→position→intention→POB/fuel if time. xpdr `7700`; comm fail `7600`; unlawful `7500`.
- `P:` pax: glasses/sharp off→loose secure→belts tight→brace. secure: fuel off→mixture ICO→mags off→alt/gen off→master off after flaps set.
- `T:` master off before electric flaps set = self-own.
***
#### Spiral / stall

- `P spiral:` throttle closed→wings level→ease out→power after AS normal. `T:` pulling first=tighter/high-g.
- `P stall:` AoA↓ NOW→wings coordinated→power as req/full if low→recover attitude. `T:` stall=AoA, not speed; yaw aggravates spin.
***
#### VFR nav / diversion / lost

- `P dep:` overhead/geopoint/enroute climb. set heading: over point→time hack→compass HDG→visual departure angle→DI/compass chk→checkpoint ETA.
- `P enroute:` altitude→planned speed→trim→OAT→lean→DI→engine/fuel scan. map: orient→anticipate→confirm→pinpoint.
- `P divert:` decide early→choose dest→line feature if possible→track/dist/GS/ETA/fuel→inform.
- `P lost:` climb if safe→communicate→conserve→confess→comply.
***
#### Pebble

- TKOF line-up→pwr→green→alive→rotate→climb | XW aileron wind+rudder centre | SOFT keep moving→GE accel | SHORT Vx→clear→Vy | CCT 500/1000 | LDG align-profile-speed-flare | GO power-att-config-track-talk | PREC inspect-decide | FORCED control-field-plan-cause-MAYDAY-pax-secure-land | EFATO nose-field-land | SPIRAL idle-level-ease | STALL AoA↓ | LOST C5.
