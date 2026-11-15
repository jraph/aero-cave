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

- Float with two or more magnets aligns with Earth's field; case filled with kerosene damps oscillation; card tilts up to 18°. [TP 2076 2.1.4 B, D]
- Dip: field lines ~parallel to surface near equator, steep near magnetic poles → dip errors. [2.1.4 C]
- Errors: **deviation** (aircraft electrics, ferrous parts → swing compass, correction card) · **turning** (from north: card first shows turn the wrong way/lags; from south: leads; only while turning) · **acceleration** `ANDS` (most on E/W headings). Variation = chart, not instrument. [2.1.4 E]
- Use: read only wings-level, steady, unaccelerated; let card settle a few seconds after roll-out; HI set from it. [2.1.4 F]
- Lightning can induce permanent compass error. [AIM AIR 2.7.1]
- Timed turns: rate one = 3°/s (180° per minute) when compass unreliable mid-turn. [TP 2076 2.1.3 D.3]
***
#### Pebble
<!-- id: nav-headings-true-magnetic-compass-pebble | level: PPL CPL IR -->

- HEADINGS `TC ± WCA = TH | TH ± variation = MH | MH ± deviation = CH | east is least, west is best | TVMDC | track = ground path, heading = nose, bearing = direction to object, course = planned line | never substitute magnetic course for magnetic heading`
- COMPASS `read straight, level, unaccelerated | ANDS · UNOS | lightning may cause permanent error`
***
