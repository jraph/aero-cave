# Fuel & fuel systems / Carburant et circuits carburant
<!-- concept: agk-fuel | level: PPL CPL IR -->

[Index](README.md) · concept `agk-fuel` · unit IDs are stable: never rename one.

***
#### Fuel
<!-- id: agk-fuel | from: 06 | kind: formula | level: PPL CPL IR -->

- `F:` `fuel = time(hr) × burn`.
- `F:` `time available = usable fuel / burn`.
- `F:` `fuel remaining = fuel on board - fuel used`.
- `F:` `fuel used = burn × minutes/60`.
- `M:` burn `6 gph` ⇒ `0.1 gal/min`; burn `9 gph` ⇒ `0.15 gal/min`; burn `12 gph` ⇒ `0.2 gal/min`.
- `T:` IFR reserve starts after required destination/alternate logic, not after takeoff.
***
#### Aviation fuel grades / FSII — L4
<!-- id: sys-aviation-fuel-grades-fsii-l4 | from: 08 | level: CPL ME -->

| Key | Recall |
|---|---|
| `T` OCTANE | AVGAS **antiknock/detonation resistance**, not fuel energy; **80/87 = lean/rich ratings**, likewise **100/130** (rich performance number >100 ≠ % octane). |
| `M` AVGAS | **80/87 RED** · **100/130 GREEN** · **100LL BLUE** (`LL` = low lead, **≠ unleaded**; rated 100 lean / 130 rich). |
| `M` JET A | Kerosene-type turbine fuel; **max freezing point −40°C**. |
| `M` JET A-1 | Kerosene-type turbine fuel; **max freezing point −47°C**. |
| `T` JET B | Wide-cut gasoline/kerosene-type turbine fuel, more volatile; fuel specification / AFM approval required. |
| `R` FSII | **Fuel System Icing Inhibitor:** lowers freezing point of **water in fuel** → prevents fuel-line/filter ice; **not fuel freeze-point improver or airframe de-icer**; use approved additive/concentration only. |
| `T` ICE | **Fuel freezing (wax/crystals) ≠ entrained/free WATER freezing**; FSII addresses latter. |
| `!` FUEL | Confirm **correct grade/type** against AFM/POH, placards and delivery; sample/check water/debris, no-go contaminated/wrong fuel; AVGAS↔JET misfuel may cause ENG failure; **colour alone insufficient**. |

- `SRC:` [FAA AMT General · AVGAS grades/colour + JET types](https://www.faa.gov/sites/faa.gov/files/regulations_policies/handbooks_manuals/aviation/amt_general_handbook.pdf) · [Canadian SCC · JET A/A-1 freeze points](https://scc-ccn.ca/standards/notices-of-intent/canadian-general-standards-board-cgsb/aviation-turbine-fuel-grades-4) · [FAA AC 20-29C · FSII](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20_29C.pdf); **POH/AFM wins**.

***
#### Fuel / starvation / contamination
<!-- id: sys-fuel-starvation-contamination | from: 08 | level: PPL CPL -->

- Know total/usable/unusable, geometry, selector, vents, drains, pumps/crossfeed and gauge limits.
- Starvation: fuel aboard but not reaching engine; exhaustion: none usable. `M:` starvation may be recoverable, exhaustion is not.
- `S:` rough/power or flow loss, selected tank empty, vent blocked, selector wrong/OFF, water/wrong fuel.
- `P:` diagnostic flow: `see sys-engine-roughness-generic-flow` (fuel selector/pump step), while preserving landing path.
- Drain all POH sumps after required events; one clear sample proves only that point. Wrong/contaminated fuel=no-go.
- `T:` gauges≠measured fuel+time/burn; late tank changes may add delay/air.
***
#### Fuelling: static, bonding and grounding — AIR 1.3
<!-- id: agk-fuelling-static-bonding-grounding | level: CPL -->

- `R` **Bond and ground the ACFT before the nozzle nears the tank**, any temperature or fuel. Over-wing: nozzle bonded to ACFT **before the cap comes off**; funnels/filters bonded too; drums: bond pump to drum before removing bungs.
- Bonding equalizes potentials (no spark); it does **not** remove charge already in the fuel. Jet fuel builds more static than AVGAS (low conductivity) → let it rest; anti-static additive helps.
- `T` **Plastic jerry cans cannot be bonded or grounded.** Empty-tank vapour = most flammable. Blower heaters in cold dry air, enclosed spaces → charged dust; injuries and deaths reported.
- No fuelling with thunderstorms nearby; control ignition sources (smoking, portable electronics). Jet A-1 auto-ignites at **220 °C** (hot brakes, exhausts).

- Sources: [TC AIM AIR](https://tc.canada.ca/sites/default/files/2026-10/aim-2026-2_air_en.pdf) 1.3.2, 1.3.4.1.
***
#### Fuel heater
<!-- id: agk-fuel-heater | level: CPL -->

- Turbine fuel can hold water that **freezes** into ice crystals at low temperature → blocked filters. **Fuel heater** (often oil-to-fuel heat exchanger) keeps fuel above freezing at the filter; filter-bypass/icing warning in some types.
- `?:` general knowledge; no free TC or NAV CANADA text found. Check against a TC-recognized text (e.g. *From the Ground Up*, TC Flight Training Manual) in the fact-check pass.


***
#### Pebble
<!-- id: agk-fuel-fuel-systems-pebble | level: PPL CPL IR -->

- FUEL `fuel = time(h) × burn | time available = usable fuel / burn | 6 gph = 0.1 gal/min, 9 = 0.15, 12 = 0.2 | IFR reserve starts after destination/alternate logic, not after takeoff`
- GRADES `octane = knock resistance | 80/87 RED; 100/130 GREEN (lean/rich); 100LL BLUE (low lead ≠ unleaded) | JET A −40 °C / A-1 −47 °C max freeze; JET B wide-cut | FSII = water-ice inhibitor ≠ fuel/airframe de-ice | colour alone ≠ proof`
- STARVATION `fuel aboard not reaching engine (may recover) ≠ exhaustion (none usable) | one clear sample proves one point | gauges ≠ measured fuel + time/burn`
- FUELLING `bond + ground before nozzle near tank | nozzle bonded before cap off | plastic jerry can = no bond | no fuelling near TS | Jet A-1 220 °C`
- FUEL HEATER `turbine fuel water → ice crystals at filter | oil-to-fuel heat exchanger`
***
