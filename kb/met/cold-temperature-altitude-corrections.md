# Cold-temperature altitude corrections / Corrections d’altitude par temps froid
<!-- concept: met-cold | level: CPL IR -->

[Index](README.md) · concept `met-cold` · unit IDs are stable: never rename one.

***
#### Cold temperature / altitude error
<!-- id: wx-cold-temperature-altitude-error | from: 06 | kind: formula | level: CPL IR -->

- Direction rule (`HIGH→LOW / HOT→COLD = LOOK OUT BELOW`): `wx-altimetry-traps`.
- `F rough:` altitude error ≈ `4 ft × height above station(thousands ft) × °C below ISA`.
- Example rough: `2000 ft above station`, `20°C colder than ISA` ⇒ `4×2×20=160 ft` low.
- `T:` use approved cold-temperature/CAP correction tables when required; rough formula is memory aid only.
***
#### Cold temperature
<!-- id: plate-cold-temperature | from: 11 | also: ifr-plates | level: IR -->

- Check CAP cold-temp notes / temperature limits / uncompensated Baro-VNAV restrictions.
- Apply required altitude corrections to procedure altitudes as applicable; ATC cleared altitude may need coordination if correction affects assigned altitude.
- `T:` cold correction protects obstacle clearance; it does not change aircraft altimeter reading.
- Apply when surface temp ≤**0 °C**, or ≤**+10 °C** when MDA/DA ≥1 000 ft HAA; add CAP table values to MSA/TAA, initial, intermediate, final, missed, MDA/DA. [CAP GEN Altitude correction chart]
- Accepted ATC-assigned altitudes: not corrected (refuse if unsafe). Vector altitudes: already corrected. Corrected mandatory/missed-hold altitude: tell ATC before the fix. [CAP GEN]
***
#### Pebble
<!-- id: met-cold-pebble -->

- ERROR `≈ 4 ft × height above station (1000 ft) × °C below ISA | rough memory aid only; CAP/approved tables when required | protects obstacle clearance; altimeter reading unchanged`
- CAP `apply when surface ≤0 °C, or ≤+10 °C if MDA/DA ≥1000 ft HAA | correct MSA/TAA, initial, intermediate, final, missed, MDA/DA | accepted ATC-assigned ALT: not corrected (refuse if unsafe) | vector ALT already corrected | corrected mandatory/missed-hold ALT: tell ATC before the fix`
***
