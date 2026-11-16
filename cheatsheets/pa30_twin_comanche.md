# PA-30 Twin Comanche — Aircraft data / Données avion
> **TRAINING ONLY / ÉTUDE SEULEMENT — NOT AN IN-FLIGHT CHECKLIST.** Generic reference: compiled PA-30 handbook for normally aspirated S/N 30-1–30-2000; its preamble identifies **Section 2 only** as FAA-approved. Each aircraft's approved AFM, supplements/STCs, placards, equipment list, current W&B and checklist prevail.

#### Identity & weights / Identification et masses
<!-- id: pa30-identity-weights | concepts: agk-wb, me-oei | level: ME | kind: aircraft -->

| Item | Reference handbook / Manuel de référence |
|---|---|
| Model / Modèle | Piper PA-30 Twin Comanche, S/N 30-1–30-2000 |
| Type certificate / Certificat de type | **A1EA** |
| MTOW / MLW | **3,600 / 3,600 lb** |
| With tip tanks / Avec réservoirs d'extrémité | **3,725 lb** provision |

- `!:` **Modifications change limits.** STCs and supplements (e.g. higher gross weight) can change MTOW, CG envelope, speeds and performance: use the aircraft's own approved supplement and charts, never the generic figures.
- `G:` Before W&B or performance work on a specific aircraft: latest W&B + equipment list · approved AFM supplements/STCs · fuel configuration · engines/propellers installed · applicable CG and performance charts. Method: `see agk-weight-balance`.

#### Reference handbook limitations / Limites du manuel de référence
<!-- id: pa30-handbook-limits | concepts: agk-vspeeds, agk-wb, agk-fuel | level: ME | kind: aircraft -->

| L (reference configuration ONLY) | Handbook value / Valeur du manuel |
|---|---|
| Engines / Moteurs | 2 × Lycoming IO-320-B1A; 160 bhp each @ 2,700 rpm |
| Baggage / Bagages | **250 lb** reference limit; serial-dependent, check the aircraft's AFM |
| CG @3,600 lb | 86.5–92.0 in |
| Flaps / Volets | Takeoff 0–15°; landing 0–27° |
| Basic fuel / Carburant de base | 60 US gal total / **54 usable** |
| Optional internal reserve / Réservoirs auxiliaires intérieurs | +30 US gal usable (if installed) |
| Optional tip tanks / Réservoirs d'extrémité | +30 US gal usable (if installed) |

- `T:` Tank capacity ≠ installed capacity; visual evidence does not certify fuel configuration. Inspect aircraft and approved documents.

#### Airspeeds — reference handbook / Vitesses — manuel de référence
<!-- id: pa30-speeds | concepts: agk-vspeeds, me-oei, me-vmc | level: ME | kind: aircraft -->

| mph IAS | KIAS | Speed | Scope / Portée |
|---:|---:|---|---|
| **88** | **77** | **VMCA** | §2; = 90 mph / 78 kt **CAS**: do not confuse |
| **97** | **85** | **VSSE** | §4; minimum intentional one-engine training speed |
| **105** | **91** | **VYSE / blue line** | |
| **94** | **82** | **VXSE** | §4 |
| **90** | **78** | **VR**, flaps 0° | §4 |
| **112** | **97** | **VY** | §4 |
| **95** | **83** | **VAPP** | §4; context-specific, not a universal single-engine approach speed |
| **124** | **107** | **VFE** | §2 |
| **149** | **129** | **VLO / VLE** | §2 |
| **162** | **140** | **VA at 3,600 lb** | §2; lower at lighter weight |
| **197** | **171** | **VNO** | §2 |
| **234** | **203** | **VNE** | §2 |

- `T:` Handbook speeds are **mph IAS**; KIAS converted (× 0.869): minimum speeds rounded up, maximum speeds rounded down. Read the units on the aircraft's ASI before using either column.
- `T:` §3 uses 90 mph IAS in the takeoff discussion while §2 labels VMCA 90 mph **CAS** (88 mph IAS): do not collapse them into the same measurement.
- `!:` Reference-configuration data: modified aircraft may have different speeds; the aircraft's AFM/supplement and ASI markings prevail.

#### Engine-out — PA-30 specifics / Panne moteur — particularités PA-30
<!-- id: pa30-engine-out | concepts: me-fail, me-vmc | level: ME | kind: aircraft -->

- Generic flow (control → identify → verify → feather) and its traps: `see me-engine-failure-flow-generic`.
- §3: single-engine climb **105 mph IAS (91 KIAS)**, about **5° bank toward the operative engine**.
- `T:` §3: crossfeed for **single-engine emergency in level flight** only; **never both selectors on CROSSFEED**; return operative engine to inboard main before landing.
- `!:` §3: delay gear/flap extension until landing is assured; **do not count on a climb with gear and flaps extended after an engine-out go-around**.
- Feather/restart and full emergency flows: follow the aircraft's installed checklist; not reproduced here.

#### Other handbook traps / Autres pièges du manuel
<!-- id: pa30-traps | concepts: agk-fuel, me-fail | level: ME | kind: aircraft -->

- `L:` §2: slip/uncoordinated manoeuvre ≥30 s or fast taxi turn immediately before takeoff may interrupt engine fuel supply when the selected tank is **<¼ full**.
- `T:` §3 best glide with **both engines inoperative** at **3,600 lb**: **110 mph IAS ≈ 96 KIAS**, propellers feathered.
- `!:` Manual landing-gear extension is mechanism-specific; follow the aircraft checklist and placard, not a compressed memory mnemonic.

#### Sources / Sources
<!-- id: pa30-sources | concepts: me-oei, agk-wb | level: ME | kind: source -->

- *Piper PA-30 Twin Comanche Pilot's Operating Handbook and FAA Approved Airplane Flight Manual*, compiled second issue 1993/1996, applicable S/N 30-1–30-2000: preamble; §2 limitations, §3 emergency procedures, §4 normal procedures/speeds.

#### Pebble
<!-- id: pa30-pebble | concepts: agk-vspeeds, me-fail, me-oei | level: ME | kind: pebble -->

- **PA-30 REF 3,600 lb** `mph IAS / KIAS: VMCA 88/77 (90 mph CAS) | VSSE 97/85 | blue 105/91 | VXSE 94/82 | VR 90/78 | VFE 124/107 | gear 149/129 | VA 162/140 | VNO 197/171 | VNE 234/203`.
- **ENGINE OUT** `generic flow → me-engine-failure-flow-generic | SE climb 105 mph, ~5° bank to live engine | crossfeed level flight only, never both | gear/flaps when landing assured`.
- **AIRCRAFT-SPECIFIC** `STC/supplement may change MTOW, CG, speeds | own AFM + current W&B prevail`.
