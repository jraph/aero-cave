# Headings: true / magnetic / compass / Caps : vrai / magnétique / compas
<!-- concept: nav-compass | level: PPL CPL IR -->

[Index](README.md) · concept `nav-compass` · unit IDs are stable: never rename one.

***
#### True / magnetic / compass
<!-- id: nav-true-magnetic-compass | from: 01, 06 | kind: formula | level: PPL CPL IR -->

- `F:` `TC ± WCA = TH`; `TH ± variation = MH`; `MH ± deviation = CH`.
- Alternatively convert TC→MC, then apply WCA to obtain MH before deviation. Never substitute magnetic course for magnetic heading.
- `M:` true→mag: east is least, west is best.
- `M:` TVMDC = True Virgins Make Dull Company; reverse = Can Dead Men Vote Twice.
- `T:` track/course/heading/bearing are different. Track = ground path; heading = nose. Bearing = direction to object; course = planned line.
***
#### Magnetic compass
<!-- id: sys-magnetic-compass | from: 08 | level: PPL CPL -->

- Errors: variation/deviation, oscillation, acceleration/turning/dip.
- Northern hemisphere: on east/west headings, acceleration causes a false north indication and deceleration a false south indication (`ANDS`); turning-error rollout memory is `UNOS`: undershoot north/overshoot south.
- `T:` turbulence and turns make compass difficult; roll out using timed/lead technique.
***
#### Magnetic compass — principle and use
<!-- id: nav-magnetic-compass-principle-use | also: agk-inst | level: PPL CPL IR -->

- Magnetized bar on float in fluid aligns with Earth's field; card read against lubber line. Liquid damps swing.
- Use: read in straight, level, unaccelerated flight; correct with deviation card; HI set from it.
- Errors: variation, deviation, dip (strongest near poles), acceleration (`ANDS`), turning (`UNOS`), oscillation.
- Lightning can induce permanent compass error. [AIM AIR 2.7.1]
- Timed turns: rate one = 3°/s when compass unreliable mid-turn.
- `?:` mechanics = general knowledge; errors already in `sys-magnetic-compass`.
***
#### Pebble
<!-- id: nav-headings-true-magnetic-compass-pebble | level: PPL CPL IR -->

- HEADINGS `TC ± WCA = TH | TH ± variation = MH | MH ± deviation = CH | east is least, west is best | TVMDC | track = ground path, heading = nose, bearing = direction to object, course = planned line | never substitute magnetic course for magnetic heading`
- COMPASS `read straight, level, unaccelerated | ANDS · UNOS | lightning may cause permanent error`
***
