# CAP plate reading / Lecture des cartes CAP
<!-- concept: ifr-plates | level: IR -->

[IFR index / Index IFR](README.md) · concept `ifr-plates` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### CAP plate read flow
<!-- id: ifr-cap-plate-read-flow | from: 10 -->

- `P:` title/effective→airport/runway/proc→nav source/freq/course→MSA/Safe100/terrain→RASS/cold temp→IAF/IF/FAF/FAP→stepdowns→DA/MDA/HAT/HAA/HATh/DH→advisory vis→MAP→missed→lighting/runway/LDA→notes.
- `T:` wrong frequency/source/course = common trap. Always verify CDI source and loaded procedure.
- `T:` plan view altitude is not enough; profile and minima notes can modify it.
***
#### CAP transition watch
<!-- id: ifr-cap-transition-watch | from: 09 | also: nav-pubs -->

- AIC `013/2026`: PFAF/glidepath-intercept depiction using a lightning-bolt symbol.
- Incremental implementation from `2026-10-29`, the cycle current at last review (14 Nov 2026). `?` not yet confirmed on a printed chart.
- Conversion is incremental: read the symbols printed on the chart in hand; do not assume either convention.
***
#### Publication cycle
<!-- id: ifr-current-publication-cycle | from: 09 | also: nav-pubs, study-src -->

- AIRAC cycle at last review (14 Nov 2026) for `CAP/CAP GEN/CFS/AIP/DAH/charts`: effective `2026-10-29` through `2026-12-24`. `T:` this line ages every 56 days; read the effective dates printed on the product.
- These publications update every `56 days`; AIP SUP/AIC publish on a `14-day` cycle.
- `P preflight:` current publication→NOTAM→AIP SUP/AIC→airport/procedure page→aircraft data.
- Trigger NOTAM = notice that source material changed; retrieve the referenced amendment/Supplement. It may expire while the underlying AIP SUP remains active.
- `[NAV CANADA publication schedule; AIC 009/2026]`
***
#### Publication-currency exam traps
<!-- id: ifr-publication-currency-exam-traps | from: 10 | also: nav-pubs, study-traps -->

- Check effective date/cycle first. Then NOTAM and AIP SUP; Trigger NOTAM only points to changed material.
- AIP SUP can remain active with no current Trigger NOTAM.
- PFAF lightning-bolt depiction is an incremental standard from `2026-10-29`; answer from the symbology printed on the chart given.
- `T:` wrong-cycle plate may produce a numerically correct but operationally invalid answer.
***
#### Pebble
<!-- id: ifr-cap-plates-publications-pebble | also: study-pebble -->

- CYCLE `publications every 56 days; AIP SUP/AIC every 14 days | cycle dates age: read the effective dates printed on the product | preflight: current publication → NOTAM → AIP SUP/AIC → airport/procedure page → ACFT data`
- TRIGGER NOTAM `only announces changed source material: open the referenced source | AIP SUP can remain active after the Trigger NOTAM expires`
- PLATE `title/effective → airport/RWY/proc → nav source/freq/course → MSA → RASS/cold temp → fixes → stepdowns → minima → MAP → missed → lighting/RWY → notes | plan-view altitude not enough: profile and minima notes can modify it`
- T `wrong-cycle plate = numerically correct, operationally invalid | PFAF lightning-bolt (AIC 013/2026): incremental from 2026-10-29, use the symbols printed on the chart`
***
