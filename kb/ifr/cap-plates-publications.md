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

- AIC `013/2026` announces a future PFAF/glidepath-intercept depiction using a lightning-bolt symbol.
- Incremental implementation starts `2026-10-29`, not in the current July cycle.
- Until a current chart actually shows it, read the symbols printed on that chart; do not assume the future convention.
***
#### Current publication cycle
<!-- id: ifr-current-publication-cycle | from: 09 | also: nav-pubs, study-src -->

- Current `CAP/CAP GEN/CFS/AIP/DAH/charts` AIRAC cycle: effective `2026-07-09` through `2026-09-03`.
- These publications update every `56 days`; AIP SUP/AIC publish on a `14-day` cycle.
- `P preflight:` current publication→NOTAM→AIP SUP/AIC→airport/procedure page→aircraft data.
- Trigger NOTAM = notice that source material changed; retrieve the referenced amendment/Supplement. It may expire while the underlying AIP SUP remains active.
- `[NAV CANADA publication schedule; AIC 009/2026]`
***
#### Publication-currency exam traps
<!-- id: ifr-publication-currency-exam-traps | from: 10 | also: nav-pubs, study-traps -->

- Check effective date/cycle first. Then NOTAM and AIP SUP; Trigger NOTAM only points to changed material.
- AIP SUP can remain active with no current Trigger NOTAM.
- PFAF lightning-bolt depiction is a future incremental standard beginning `2026-10-29`; current July-cycle questions use current-chart symbology.
- `T:` wrong-cycle plate may produce a numerically correct but operationally invalid answer.
***
