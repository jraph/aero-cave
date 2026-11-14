# IFR emergencies & instrument failures / Urgences IFR et pannes d’instruments
<!-- concept: ifr-emerg | level: IR -->

[IFR index / Index IFR](README.md) · concept `ifr-emerg` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### IFR emergencies
<!-- id: ifr-ifr-emergencies | from: 09 -->

- Emergency: aviate; declare; ATC expects necessary action and will assist. If no comm, `7700` can indicate emergency but may not be detected.
- Equipment fail: report nav/comm malfunctions to ATC. Partial panel: attitude-power-performance; reduce workload, ask vectors/no-gyro if needed.
- Icing: exit conditions early; climb/descend/turn; approach speed/config per POH/SOP. `T:` “trace” can become performance problem fast in trainer.
***
#### Instrument failures
<!-- id: ifr-instrument-failures | from: 10 | also: agk-inst -->

- Pitot blocked + drain open: ASI reads `0`. Pitot blocked + drain blocked: ASI acts altimeter-ish. Static blocked: ASI/ALT/VSI errors; alternate static changes readings.
- Vacuum fail: attitude/heading unreliable; use turn coordinator/compass/power/performance if electric TC.
- Compass: variation, deviation, dip, acceleration, turning errors. `ANDS/UNOS` for N hemisphere.
- Electrical fail: load shed, battery time, comm/nav loss planning. `T:` GPS/iPad not a full IFR electrical system.
***
#### Pebble
<!-- id: ifr-emergencies-instrument-failures-pebble | also: study-pebble -->

- EMERGENCY `aviate, declare | 7700 if no comm, may not be detected | report nav/comm malfunctions to ATC | partial panel: attitude-power-performance, ask vectors/no-gyro`
- PITOT-STATIC `pitot blocked + drain open: ASI 0 | pitot + drain blocked: ASI acts like altimeter | static blocked: ASI/ALT/VSI errors; alternate static changes readings`
- OTHER `vacuum fail: attitude/heading unreliable | compass ANDS/UNOS (N hemisphere) | electrical: load shed, battery time; GPS/iPad ≠ full IFR electrical system | icing: exit early`
***
