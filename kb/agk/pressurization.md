# Pressurization / Pressurisation
<!-- concept: agk-press | level: CPL ME -->

[Index](README.md) · concept `agk-press` · unit IDs are stable: never rename one.

***
#### Cabin pressurization / outflow — L4
<!-- id: sys-cabin-pressurization-outflow-l4 | from: 08 | level: CPL ME -->

| Key | Recall |
|---|---|
| `T` CABIN ALT | Pressure-equivalent **cabin** ALT ≠ ACFT ALT; cabin ALT governs altitude-dependent O₂ use, subject to separate rules. |
| `R` OUTFLOW | Regulates cabin P by controlling **air discharged**, with conditioned/pressurizing air supplied. |
| `M` CLOSE | Outflow closes→less air escapes→cabin **P↑ / ALT↓** (other factors equal). |
| `M` OPEN | Outflow opens→more air escapes→cabin **P↓ / ALT↑** (other factors equal). |
| `F` ΔP | Differential P = **cabin P − ambient P**; AFM structural limit. |
| `T` RELIEF | **Positive** relief protects against excess cabin P; **negative** relief protects against excess outside P. |
| `!` FAILURE | Depressurization→cabin ALT↑→O₂ / emergency DESC per AFM; **O₂ thresholds/supply: [card 04 · CAR 605.31–32](../../kb/law/oxygen-requirements.md)** (not duplicated). |

- `SRC:` [FAA PHAK · pressurization systems](https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak) · [CAR 605.31–32](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/section-605.31.html); ACFT AFM/checklists control.
- `M · L4` **PRESSURIZATION: outflow CLOSE→cabin P↑/ALT↓; OPEN→P↓/ALT↑ | ΔP=cabin−ambient | +relief excess cabin P; −relief excess outside P | decompression→O₂/emergency DESC per AFM.**

***
