### CPAER · CAVE FORMULAS
**Units:** kt = NM/h · time in h unless marked min · ≈ = shortcut · POH/chart values prevail.
***
#### TIME · DISTANCE · FUEL
| Find | Formula |
|---|---|
| Distance / time / GS | `D = GS × h` · `min = 60D/GS` · `GS = 60D/min` |
| Fuel / endurance | `fuel = flow × h` · `h = usable fuel/flow` |
| Specific range | `NM per fuel unit = GS/flow` |
***
#### NAV · WIND · 1-IN-60
| Find | Formula / cue |
|---|---|
| Wind components | `XW = W sin θ` · `HW = W cos θ` · θ = wind-from angle relative to course |
| WCA | `sin WCA = XW/TAS` · steer INTO wind |
| Heading | `TH = TC + signed WCA` |
| True → magnetic → compass | **East subtract / West add** variation, then deviation |
| Track error | `TE° ≈ 60 × off-track / distance flown` |
| Closing angle | `CA° ≈ 60 × off-track / distance remaining` |
| Destination correction | `TE + CA`, towards track · small-angle approximation |
***
#### WEIGHT · BALANCE
| Find | Formula |
|---|---|
| Moment / CG | `M = W × arm` · `CG = ΣM/ΣW` |
| Move weight | `ΔCG = w × distance moved / total W` |
| Weight to move | `w = total W × ΔCG / distance moved` |
| Add / remove | `new CG = (W × old CG ± w × arm)/(W ± w)` |
| % MAC | `100 × (CG − LEMAC)/MAC` |
**Signs:** aft positive if datum convention says so · matching units · account for moment-index scaling.
***
#### ALTITUDE · TEMPERATURE
| Find | Formula |
|---|---|
| ISA °C | `15 − 2 × altitude in thousands ft` (troposphere shortcut) |
| PA ft | `IALT + (29.92 − setting inHg) × 1000` |
| DA ft | `PA + 120 × (OAT − ISA temperature at PA)` |
| True-altitude temperature correction ft | `≈ 4 × height above setting source in thousands ft × ΔT°C` |
| °F / °C | `F = 1.8C + 32` · `C = (F − 32)/1.8` |
**True altitude:** ΔT = actual minus standard under question assumptions · warm ADD / cold SUBTRACT · representative column temperature assumed; operational cold corrections use approved tables. **Weight affects performance, not DA.**
***
#### MET · CLOUDS
| Find | Formula / rate |
|---|---|
| Dry rising parcel | `−3°C/1000 ft` |
| Saturated rising parcel | `≈ −1.5°C/1000 ft` · varies with conditions |
| Dew point, unsaturated rising parcel | `≈ −0.5°C/1000 ft` |
| Convective base AGL | `≈ 400 × (T − Td)` ft · convergence `3 − 0.5 = 2.5` |
| Height to 0°C | `1000 × T / lapse rate` · rate in °C/1000 ft |
**Parcel rates ≠ environmental lapse rate.** Freezing-level calculation needs the applicable profile; inversions/multiple levels invalidate the simple shortcut.
***
#### STALL · LOAD · AIRSPEED
| Find | Formula |
|---|---|
| Level coordinated turn load | `n = 1/cos bank` |
| Loaded stall | `Vs(new) = Vs × √n` |
| Weight-change stall | `Vs₂ = Vs₁ × √(W₂/W₁)` · same configuration/conditions |
| Approach rule | `≈ 1.3 Vs0` · POH governs |
| Lift / dynamic pressure | `L = ½ρV²SCL` · `q = ½ρV²` · consistent units |
| TAS from EAS | `TAS = EAS × √(ρ₀/ρ)` |
| Rough TAS | `CAS × [1 + 0.02(PA/1000)]` · use E6B for temperature-aware result |
| Bank | 30° | 45° | 60° |
|---|---|---|---|
| n | 1.15 | 1.41 | 2.00 |
| Vs multiplier | **1.07** | **1.19** | **1.41** |
***
#### CLIMB · DESCENT · TURN
| Find | Formula |
|---|---|
| Gradient ft/NM | `60 × vertical speed fpm / GS kt` |
| Required fpm | `gradient ft/NM × GS/60` |
| Gradient % | `100 × vertical/horizontal distance` · same units |
| % → ft/NM | `% × 60.76` |
| 3° descent fpm | `≈ 5.3 × GS` · rough mental rule `5 × GS` |
| 3° descent NM | `height to lose ft / 318` |
| Standard-rate turn | **3°/s · 180°/min · 360° in 2 min** |
| Turn rate °/s | `≈ 1091 × tan(bank)/TAS kt` |
| Turn radius ft | `≈ TAS²/(11.26 × tan bank)` |
Turn formulas: coordinated, level, still-air geometry; wind changes ground track.
***
#### RADIO · HYDROPLANING
| Find | Formula / units |
|---|---|
| VHF horizon NM | `≈ 1.23(√h₁ + √h₂)` · **1.25** also used · h in ft above surface |
| Station height negligible | `≈ 1.23√h` or question's coefficient |
| Dynamic hydroplaning kt | **`≈ 9√tyre pressure psi`** · 36 psi → **54 kt** |
Radio horizon ≠ guaranteed reception · terrain/equipment matter. Hydroplaning rule does not cover all wet-runway friction loss.
***
#### CONVERSIONS
| Quantity | Remember |
|---|---|
| NM | `1.852 km` · `6076 ft` · `1.151 statute mi` |
| Statute mile | `1.609 km` |
| US / Imperial gallon | `3.785 L / 4.546 L` |
| kg / metre | `2.205 lb / 3.281 ft` |
| Longitude / time | `15°/h` · `4 min/degree` |
| Latitude | `1 minute ≈ 1 NM` |
***
**FIRST RECALL:** `60D/GS` · `60×off-track/distance` · `ΣM/ΣW` · `29.92` · `120ΔT` · `400(T−Td)` · `Vs√n` · **`1.3Vs0`** · **`9√psi`**.
**References:** [TC CPAER TP12881](https://tc.canada.ca/en/aviation/publications/study-reference-guide-written-examinations-commercial-pilot-licence-aeroplane-tp-12881) · [TC reception approximation](https://tc.canada.ca/en/corporate-services/acts-regulations/list-regulations/canadian-aviation-regulations-sor-96-433/standards/standard-724-commuter-operations-helicopters-canadian-aviation-regulations-cars) · [TSB hydroplaning](https://tsb.gc.ca/eng/rapports-reports/aviation/2005/a05o0257/a05o0257.html).

