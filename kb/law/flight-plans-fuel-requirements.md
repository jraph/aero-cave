# Flight plans & fuel requirements / Plans de vol et exigences de carburant
<!-- concept: law-plan | level: PPL CPL -->

[Index](README.md) · concept `law-plan` · unit IDs are stable: never rename one.

***
#### Flight plan / itinerary / PIREP
<!-- id: law-flight-plan-itinerary-pirep | from: 01 | also: met-gfa | level: PPL CPL -->

- VFR flight plan/itinerary unless within `25 NM` dep AD. Intl = flight plan. `T:` itinerary needs responsible person.
- Arrival report: ident + plan/itinerary + dep + arr + date/time. `T:` close it.
- VFR pos report: ident-pos-time-alt-plan-dest. PIREP: loc/time-alt-type-cloud-temp-wind-turb-ice-rmk.
***
#### Planning / fuel / go-no-go
<!-- id: law-planning-fuel-go-no-go | from: 03 | also: met-decide | level: CPL -->

- Plan: wx+NOTAM+CFS+fuel+W&B+perf+alternates/options+daylight/night+terrain/airspace.
- Fuel: taxi/start + trip + contingency + reserve + alternate/diversion + unusable.
- `T:` POH burn≠actual burn. marginal VFR + commercial pressure + unfamiliar terrain = trap.
***
#### Flight plan / itinerary
<!-- id: law-flight-plan-itinerary | from: 04 | level: PPL CPL IR -->

- IFR: file IFR flight plan, except itinerary permitted in specified cases wholly/partly outside controlled airspace or where facilities inadequate. `[CAR 602.73]`
- VFR: flight plan or itinerary unless flight remains within `25 NM` of departure aerodrome. `[CAR 602.73]`
- International flight: flight plan.
- Flight plan filed with ATS/CARS; itinerary may be filed with responsible person, ATS or CARS. `[CAR 602.75]`
- Report required changes and file arrival report/close as required. `[CAR 602.76–602.78]`
- `T:` landing does not automatically close every plan/itinerary.
***
#### Fuel requirements
<!-- id: law-fuel-requirements | from: 04 | level: PPL CPL IR -->

| Flight | Required fuel after reaching destination |
|---|---|
| VFR aeroplane day | normal cruise `30 min` |
| VFR aeroplane night | normal cruise `45 min` |
| IFR prop, no alternate | approach + missed + `45 min` |
| IFR prop, alternate | approach + missed → alternate → land + `45 min` |
| IFR turbojet/helicopter | same structure + `30 min` |

- Add taxi and foreseeable delays from weather, routing, traffic, system failure and other foreseeable conditions. `[CAR 602.88]`
- `T:` reserve begins after all required legs; legal reserve is not a target landing fuel.
***
#### IFR fuel / reserve memory
<!-- id: law-ifr-fuel-reserve-memory | from: 06 | also: ifr-plan, study-formulas | level: IR -->

- Prop IFR with alternate: destination approach+missed → alternate → land → `45 min`.
- Prop IFR no alternate: destination approach+missed → `45 min`.
- Turbojet/helicopter: same structure but `30 min`.
- `T:` CAR text/current ops rules win; this is memory, not dispatch release.
***
