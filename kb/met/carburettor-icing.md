# Carburettor icing & induction / Givrage du carburateur et admission
<!-- concept: carb-ice | level: PPL CPL IR -->

[Meteorology index / Index météo](README.md) · concept `carb-ice` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Carburetor icing — cause / conditions
<!-- id: wx-carb-ice | from: 16, 05 -->

- Fuel vaporization + venturi pressure drop can cool carb throat well below OAT.
- Possible even in warm weather, well above freezing; risk high with humidity and partial power/descent.
- Range, symptoms, carb-heat procedure: `sys-carburetor-icing`.
- `T:` carb icing ≠ structural icing; structural icing forecast and carb icing risk are related but not identical.
***
#### Carburetor icing — range, symptoms, action
<!-- id: sys-carburetor-icing | from: 08 | level: PPL CPL -->

- Can occur in moist air from about `-13°C to +38°C`; risk high in humid partial-power operation, incl. descent. Cause: `wx-carb-ice`.
- `S:` fixed-pitch: unexplained RPM↓, then roughness/airspeed↓. Constant-speed: manifold pressure↓.
- `P:` full carb heat→expect initial power loss/roughness→leave full hot until ice clears→re-adjust power/mixture per POH.
- `M:` initial worse, then better = ice melting.
- `T:` partial heat without carb-air-temperature guidance may place air in icing range. Heated air is usually unfiltered and reduces power.
***
#### Induction / alternate air
<!-- id: sys-induction-alternate-air | from: 08 | level: PPL CPL -->

- Fuel-injected engines may use alternate induction air instead of carb heat.
- `S:` intake filter blockage/ice → power loss; alternate air may restore.
- `T:` alternate air often warmer/unfiltered and changes mixture/power.
***
#### Pebble
<!-- id: carb-ice-pebble -->

- CARB ICE `fuel vaporization + venturi → throat well below OAT | ≈ −13 to +38 °C, possible well above freezing | humid + partial power/descent | fixed pitch: RPM↓ then roughness; CS: MP↓ | full carb heat: worse first, then better; leave full hot until clear | partial heat may enter icing range | ≠ structural icing`
***
