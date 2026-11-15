# Flight plans & fuel requirements / Plans de vol et exigences de carburant
<!-- concept: law-plan | level: PPL CPL -->

[Index](README.md) · concept `law-plan` · unit IDs are stable: never rename one.

***
#### Planning / fuel / go-no-go
<!-- id: law-planning-fuel-go-no-go | from: 03 | also: met-decide | level: CPL -->

- Pre-flight information (602.71): see `law-pre-flight-information`; add daylight/night, terrain and CFS review.
- Planning fuel build-up: taxi/start + trip + contingency + reserve + alternate/diversion + unusable. Legal minimum reserve: see `law-fuel-requirements`.
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
#### IFR flight plan contents and changes — CAR 602.74 / 602.76
<!-- id: law-ifr-flight-plan-contents-changes | also: ifr-plan, ifr-enr | level: IR -->

- Contents: as specified in the CFS (flight planning section). [CAR 602.74; AIM RAC 3.14.2]
- IFR plan: file preferably ≥30 min before departure; include suitable alternate meeting alternate minima; no intermediate stops in one IFR plan. [RAC 3.5.2, 3.9, 3.13]
- Route points: where speed, level, track or flight rules change. [RAC 3.15.6.2]
- Changes to notify (IFR plan/itinerary): cruising altitude/FL, route, destination, **TAS ≥5%** of filed TAS, **Mach ≥0.01**. [CAR 602.76(1)]
- Notify ATC (or responsible person) as soon as practicable; in controlled airspace get **clearance before** the change. [CAR 602.76(2); RAC 3.6.2, 8.2.2]
- IFR → VFR without new plan if destination unchanged; cancel IFR only in VMC and outside Class A/B. [RAC 6.2]
- `M:` `ALT-ROUTE-DEST-TAS5%-MACH.01`.
- `T:` TAS change counts against **filed** TAS, not last cruise speed.
***
#### Crew member instructions — 602.87
<!-- id: law-crew-member-instructions-602-87 | level: CPL -->

- `R` PIC ensures every crew member, before acting as crew, is instructed on **their duties** and the **location and use of all normal and emergency exits and all emergency equipment** on board.
- `T` 602.87 = crew instructions ≠ 602.89 passenger briefing.

- Sources: [602.87](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/section-602.87.html), [602.89](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/section-602.89.html).
***
#### Pebble
<!-- id: law-flight-plans-fuel-requirements-pebble | level: PPL CPL IR -->

- PLAN CAR 602.73 `IFR: flight plan (itinerary only in specified cases) | VFR: plan or itinerary unless within 25 NM of departure aerodrome | international: flight plan | itinerary needs responsible person | landing does not automatically close a plan`
- ARRIVAL REPORT `ident + type of plan/itinerary + departure + arrival + date/time`
- FUEL CAR 602.88 `VFR aeroplane day 30 min / night 45 min at normal cruise | IFR prop: approach + missed (→ alternate + land) + 45 min | turbojet/helicopter IFR 30 min | add taxi + foreseeable delays | reserve begins after all required legs`
- PLANNING `fuel = taxi + trip + contingency + reserve + alternate + unusable | POH burn ≠ actual burn`
- IFR PLAN `contents per CFS | file ≥30 min | no intermediate stops | notify + get clearance for ALT, ROUTE, DEST, TAS ≥5 %, Mach ≥0.01`
- CREW INSTRUCTIONS `602.87: before acting as crew → duties + exits + emergency equipment`
***
