# OEI performance & takeoff planning / Performances OEI et planification du décollage
<!-- concept: me-oei | level: ME -->

[Index](README.md) · concept `me-oei` · unit IDs are stable: never rename one.

***
#### Essential speeds to know cold
<!-- id: me-essential-speeds-to-know-cold | from: 13 | also: agk-vspeeds | level: ME -->

| Symbol | Meaning |
|---|---|
| `Vmc` | min control speed airborne, critical engine failed |
| `Vsse` | safe intentional OEI speed; if POH none, TC guide says use `Vmc+10` |
| `Vyse` | OEI best rate-of-climb speed, blue line |
| `Vxse` | OEI best angle-of-climb speed |
| `Vs0` | stall speed landing config |
| `Va` | manoeuvring speed |
| `Vle` | max gear extended |
| `Vlo` | max gear operating |
| `Vfe` | max flap extended |

- `T:` quote aircraft numbers from memory for test; all other performance from POH/AFM charts.
***
#### OEI climb
<!-- id: me-oei-climb | from: 13 | also: agk-perfcalc | level: ME -->

- `Vyse` = best rate; `Vxse` = best angle. Use obstacle vs rate logic.
- `T:` positive climb may be zero or negative depending weight/DA/config/failed engine/prop/surface.
- POH required: OEI ROC, single-engine service ceiling, accelerate-stop/go if available, climb gradients.
- `M:` ME safety comes from precomputed options, not heroic rudder.
***
#### Accelerate-stop / accelerate-go
<!-- id: me-accelerate-stop-accelerate-go | from: 13 | also: agk-perfcalc | level: ME -->

- Accelerate-stop = accelerate to decision/engine-failure speed, reject, stop.
- Accelerate-go = accelerate to failure speed, continue takeoff, climb/clear obstacle OEI.
- Light twins often have long or unavailable accelerate-go margins at normal training weights/DA.
- `T:` balanced field/V1 thinking from transport category does not automatically apply to light twins.
- `P pre-TKOF brief:` below reject speed/runway remaining → stop; after liftoff/gear up/no runway → control, clean, climb if able, land ahead/nearby if not.
***
#### TKOF speeds · transport-category distinctions — L4
<!-- id: me-tkof-speeds-transport-category-distinctions-l4 | from: 13 | also: agk-vspeeds | level: CPL ME -->

| Key | Recall |
|---|---|
| `V1` | Reject/continue boundary; first reject action **by V1** to satisfy applicable accelerate-stop limits. |
| `VR` | Rotation speed → initiate nose-up rotation. |
| `V2` | TKOF safety speed → **OEI = One Engine Inoperative** climb/control margins; **≠ braking speed**. |
| `Vtire` | Maximum certificated **tire groundspeed** during TKOF roll; may limit max TKOF GW. |
| `T` | V1 depends on GW/ENG accel, RWY, wind, conditions/config; transport-category V1/V2 concepts **not automatically applicable to light twins**; AFM/POH wins. |

- `SRC:` [FAA AFH Ch 16 · takeoff speeds/accelerate-stop](https://www.faa.gov/sites/faa.gov/files/regulations_policies/handbooks_manuals/aviation/airplane_handbook/17_afh_ch16.pdf).
- `M · L4` **V1=reject/continue (accelerate-stop) | VR=rotate | V2=OEI safety/climb | Vtire=max tire GS | GW/RWY/conditions affect V1 | light twin ≠ automatic transport-category V-speeds | AFM wins.**
***
#### Takeoff briefing — ME
<!-- id: me-takeoff-briefing-me | from: 13 | level: ME -->

- `P:` runway/length/wind/DA/perf → rotate speed → `Vmc/Vyse/Vsse` → reject criteria → EF before liftoff → EF after liftoff with runway → EF airborne no runway → emergency return/straight-ahead plan.
- `M:` before power: “what kills us today?” runway, weight, DA, obstacles, weather, traffic.
- `T:` “continue no matter what” is wrong; “stop no matter what” is also wrong. runway remaining + energy + control decide.
***
#### Performance calculations required
<!-- id: me-performance-calculations-required | from: 13 | also: agk-perfcalc | level: ME -->

- Takeoff distance / obstacle. Accelerate-stop if available. Accelerate-go if available. Time/fuel to climb. Cruise power/KTAS/fuel. Landing distance. OEI ROC. OEI enroute performance.
- `T:` use actual weight, temp, pressure altitude, runway, wind, obstacle, configuration. Training “it climbs” assumption is unsafe.
- `M:` compare before flight: all-engine climb, OEI climb, terrain/obstacle, nearest runway/return.
***
#### W&B ME traps
<!-- id: me-w-b-me-traps | from: 13 | also: agk-wb | kind: trap | level: ME -->

- Multi-engine aircraft often have narrow CG/fuel/baggage constraints. Check takeoff, landing, zero-fuel if relevant.
- Aft CG worsens Vmc/control. Light weight can worsen Vmc but improves climb; heavy weight may improve Vmc but destroy climb.
- `T:` Vmc certification worst case is light/aft; performance worst case is heavy/hot/high/dirty.
***
#### Pebble
<!-- id: me-oei-performance-takeoff-planning-pebble | level: CPL ME -->

- SPEEDS `Vmc = min control speed, critical engine failed (red line) | Vsse = safe intentional OEI; Vmc + 10 if POH none | Vyse = OEI best rate, blue line | Vxse = OEI best angle`
- OEI CLIMB `may be zero or negative | single-engine service ceiling may be below terrain | above Vmc ≠ climb`
- TAKEOFF `accelerate-stop = accelerate, reject, stop | accelerate-go = continue and clear obstacle OEI | V1/V2 transport-category concepts ≠ automatic for light twins; AFM wins | brief: stop below reject speed/runway remaining; airborne no runway → control, clean, climb if able, land ahead if not`
- W&B `Vmc worst case light/aft; performance worst case heavy/hot/high/dirty`
***
