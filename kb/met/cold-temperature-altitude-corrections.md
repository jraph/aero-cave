# Cold-temperature altitude corrections / Corrections d’altitude par temps froid
<!-- concept: met-cold | level: CPL IR -->

[Index](README.md) · concept `met-cold` · unit IDs are stable: never rename one.

***
#### Cold temperature / altitude error
<!-- id: wx-cold-temperature-altitude-error | from: 06 | kind: formula | level: CPL IR -->

- `M:` high to low, look out below; warm to cold, look out below.
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
