# Flight plans & fuel requirements / Plans de vol et exigences de carburant
<!-- concept: law-plan | level: PPL CPL -->

[Index](README.md) · concept `law-plan` · unit IDs are stable: never rename one.

***
#### Planning / fuel / go-no-go
<!-- id: law-planning-fuel-go-no-go | from: 03 | also: met-decide | level: CPL -->

- Plan: wx+NOTAM+CFS+fuel+W&B+perf+alternates/options+daylight/night+terrain/airspace.
- Fuel: taxi/start + trip + contingency + reserve + alternate/diversion + unusable.
- `T:` POH burn≠actual burn. marginal VFR + commercial pressure + unfamiliar terrain = trap.
***
#### Flight plan / itinerary
<!-- id: law-flight-plan-itinerary | from: 01, 04 | level: PPL CPL IR -->

- IFR: file IFR flight plan, except itinerary permitted in specified cases wholly/partly outside controlled airspace or where facilities inadequate. `[CAR 602.73]`
- VFR: flight plan or itinerary unless flight remains within `25 NM` of departure aerodrome. `[CAR 602.73]`
- International flight: flight plan.
- Flight plan filed with ATS/CARS; itinerary may be filed with responsible person, ATS or CARS. `[CAR 602.75]`
- Report required changes and file arrival report/close as required. `[CAR 602.76–602.78]`
- `T:` landing does not automatically close every plan/itinerary.
- `T:` itinerary needs responsible person.
- Arrival report: ident + plan/itinerary + dep + arr + date/time. `T:` close it.
- VFR pos report: ident-pos-time-alt-plan-dest. PIREP: loc/time-alt-type-cloud-temp-wind-turb-ice-rmk.
***
#### Fuel requirements
<!-- id: law-fuel-requirements | from: 04, 06 | level: PPL CPL IR -->

| Flight | Required fuel after reaching destination |
|---|---|
| VFR aeroplane day | normal cruise `30 min` |
| VFR aeroplane night | normal cruise `45 min` |
| IFR prop, no alternate | approach + missed + `45 min` |
| IFR prop, alternate | approach + missed → alternate → land + `45 min` |
| IFR turbojet/helicopter | same structure + `30 min` |

- Add taxi and foreseeable delays from weather, routing, traffic, system failure and other foreseeable conditions. `[CAR 602.88]`
- `T:` reserve begins after all required legs; legal reserve is not a target landing fuel.
- `T:` CAR text/current ops rules win; this is memory, not dispatch release.
***
#### Pebble
<!-- id: law-flight-plans-fuel-requirements-pebble | level: PPL CPL IR -->

- PLAN CAR 602.73 `IFR: flight plan (itinerary only in specified cases) | VFR: plan or itinerary unless within 25 NM of departure aerodrome | international: flight plan | itinerary needs responsible person | landing does not automatically close a plan`
- ARRIVAL REPORT `ident + type of plan/itinerary + departure + arrival + date/time`
- FUEL CAR 602.88 `VFR aeroplane day 30 min / night 45 min at normal cruise | IFR prop: approach + missed (→ alternate + land) + 45 min | turbojet/helicopter IFR 30 min | add taxi + foreseeable delays | reserve begins after all required legs`
- PLANNING `wx + NOTAM + CFS + fuel + W&B + perf + alternates | POH burn ≠ actual burn`
***
