# Theory of flight / Théorie du vol
<!-- concept: agk-theory | level: PPL CPL -->

[Index](README.md) · concept `agk-theory` · unit IDs are stable: never rename one.

***
#### Aerodynamics — lift, drag & equilibrium
<!-- id: agk-aerodynamics-lift-drag-equilibrium | from: 01 | level: PPL CPL -->

| Key | Essential recall |
|---|---|
| `LIFT` | Force component ⟂ relative airflow; `L=½ρV²SCL` (V = TAS); AOA controls `CL` until critical AOA/stall. |
| `CP / CG / AC` | CP = location of resultant aero force on airfoil (moves with AOA); CG = weight acts here; AC ≈25% chord for typical subsonic airfoil (pitching moment approx constant with AOA). |
| `MOMENT` | Pitching moment about CG = force × perpendicular arm; trimmed unaccelerated FLT requires net pitching moment `ΣM(CG)=0` (tail force may balance wing/fuselage moment). |
| `DRAG` | Total = parasite + induced; parasite = form/pressure + skin friction + interference; induced = drag due to lift/downwash. |
| `SPD / DRAG` | At given GW/config/ALT in steady level FLT, IAS↓→AOA/induced drag↑; IAS↑→parasite drag↑; minimum total drag ≈ max `L/D`. |
| `EQUIL` | Straight/level/constant-speed simplified: `L=W; T=D; ΣM=0`; requires aligned thrust & negligible vertical thrust/tail geometry effects. |
| `BANK` | Coordinated level turn: `L cosφ=W`, `n=1/cosφ`, `Vs(turn)=Vs(level)√n` (same config/weight). |
| `AIRFOIL` | Wing cross-section: chord = LE→TE straight line; camber = curvature; thickness = upper/lower separation; `CL` varies with AOA up to critical AOA. |
| `WASHOUT` | Geometric twist: wingtip incidence < root incidence → generally promotes root-first stall/longer aileron effectiveness; not guaranteed. |
| `AR` | Aspect ratio `AR=b²/S` (span²/wing area); rectangular wing `AR=b/c` (span/chord). |
| `INDUCED / AR` | At equal `CL` and span efficiency, `AR↑→CDi↓`; `CDi=CL²/(πeAR)` (e = span-efficiency factor). |
| `T` | Washout ≠ dihedral; AR ≠ wing area; cambered airfoil may lift at geometric AOA 0°; stall at critical AOA. |
| `T` | CP ≠ CG ≠ AC; lift vector ⟂ relative wind, not necessarily vertical; stall = critical AOA, not a fixed IAS. |

- `SRC:` [FAA PHAK, Ch. 4–5 · Principles/Aerodynamics of Flight](https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak); general theory; aircraft POH/AFM governs performance.
***
#### Wing design devices, control balancing, roll upset
<!-- id: agk-wing-design-devices-control-balance | level: CPL -->

| Device | Effect | Trade-off |
|---|---|---|
| **Sweepback** | delays compressibility (high Mach); adds lateral stability | tip stalls first, pitch-up tendency; less lift at low speed |
| **Wing fence** | blocks spanwise flow on swept wing | delays tip stall |
| **Stall strip** | small wedge on inboard leading edge | forces **root stall first** → aileron control kept |
| **Spoilers** | spoil lift: roll control (one side) and/or descent/braking (both) | lift loss, drag |
| **Vortex generators** | re-energize boundary layer | delay separation, better low-speed control |
| **Winglets** | reduce wingtip vortices → **induced drag** | weight, structure |

- **Static balance**: mass ahead of hinge so the surface's CG is at/near the hinge line. **Dynamic (aerodynamic) balance**: horn or inset hinge reduces stick forces. Both guard against **flutter**.
- **Roll upset** (e.g. wake turbulence, asymmetric flap, aileron trim/runaway): unload, roll wings level with ailerons (rudder as needed) before pulling; then recover pitch and power.
- `?:` general knowledge; no free TC or NAV CANADA text found. Check against a TC-recognized text (e.g. *From the Ground Up*, TC Flight Training Manual) in the fact-check pass.


***
#### Pebble
<!-- id: agk-theory-of-flight-pebble | level: PPL CPL -->

- AERO `L ⟂ relative airflow; L = ½ρV²S·CL | CP ≠ CG ≠ AC (≈25% chord) | trim: ΣM(CG) = 0 | drag = parasite (form + friction + interference) + induced | IAS↓ → induced↑; IAS↑ → parasite↑; min drag ≈ max L/D | level: L = W, T = D | level turn n = 1/cosφ, Vs × √n | washout: tip incidence < root → root-first stall generally | AR = b²/S; AR↑ → induced drag↓ | stall = critical AOA, not a fixed IAS`
- WING DEVICES `sweepback: high Mach, tip stall | fence + stall strip: root stalls first | spoilers: roll or descent | VGs: delay separation | winglets: less induced drag | balance: mass vs flutter, horn vs forces`
***
