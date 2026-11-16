# PA-30 Twin Comanche — Aircraft data / Données avion
> **TRAINING ONLY / ÉTUDE SEULEMENT — NOT AN IN-FLIGHT CHECKLIST.** C-FMCV, S/N **30-1732**. Source PA-30 compilation covers normally aspirated S/N 30-1–30-2000; its preamble identifies **Section 2 only** as FAA-approved. Current aircraft AFM, approved supplements, placards, equipment list, latest W&B and checklist prevail. **Do not apply unverified configuration-specific numbers in flight.**

#### Identity & aircraft W&B / Identification et masse et centrage
<!-- id: pa30-cfmcv-wb | concepts: agk-wb, me-oei | level: ME | kind: aircraft -->

| C-FMCV | Recorded value / Valeur consignée |
|---|---:|
| Registration / Immatriculation | **C-FMCV** |
| Model / Modèle; serial / série | Piper PA-30; **30-1732** |
| Type certificate / Certificat de type | **A1EA** |
| Registered MTOW / Masse maximale au décollage (CCAR, user-supplied) | **1,723.65 kg ≈ 3,800 lb** |
| Empty weight / Masse à vide (2021 W&B #14) | **2,429.51 lb** |
| Empty CG arm / Bras du CG à vide | **83.27 in** |
| Empty moment / Moment à vide | **202,311.35 lb-in** |
| Gross / landing weight (2021 W&B #14) | **3,800 / 3,800 lb** |
| Useful load / Charge utile (W&B #14) | **1,370.49 lb** |

- `SRC:` **C-FMCV W&B amendment #14, 2021-10-07**, left-engine composite spinner/backplate (STC **SA00735AT**). This amendment does **not** establish the aircraft's complete STC/supplement inventory or that the 2021 empty weight remains current.
- `!:` **3,800 lb registered MTOW ≠ approved performance data.** Supplied generic manual is **3,600 lb**, with a separate **3,725 lb tip-tank** provision. The basis of **3,800 lb**, its CG envelope, applicable procedures and performance charts **remain unverified**. Robertson STOL is a hypothesis, **not** an identified C-FMCV modification; no tip tanks are confirmed.
- `G:` Before W&B or performance use: verify latest W&B + equipment changes; **approved flight-manual supplement/STC** for 3,800 lb; fuel configuration; actual engine/propellers; and applicable CG and performance charts.

#### Reference handbook limitations / Limites du manuel de référence
<!-- id: pa30-handbook-limits | concepts: agk-vspeeds, agk-wb, agk-fuel | level: ME | kind: aircraft -->

| L (reference configuration ONLY) | Handbook value / Valeur du manuel |
|---|---|
| Engines / Moteurs | 2 × Lycoming IO-320-B1A; 160 bhp each @ 2,700 rpm |
| Generic MTOW / MLW | **3,600 / 3,600 lb** — **NOT C-FMCV's registered MTOW** |
| Baggage / Bagages, S/N 30-1732 | **250 lb** reference limit |
| Reference CG @3,600 lb | 86.5–92.0 in; **NOT established at 3,800 lb** |
| Flaps / Volets | Takeoff 0–15°; landing 0–27° |
| Basic fuel / Carburant de base | 60 US gal total / **54 usable** |
| Optional internal reserve / Réservoirs auxiliaires intérieurs | +30 US gal usable (if installed) |
| Optional tip tanks / Réservoirs d'extrémité | +30 US gal usable (if installed); **not confirmed on C-FMCV** |

- `T:` Tank capacity ≠ installed capacity; visual evidence does not certify fuel configuration. Inspect aircraft and approved documents.
- `T:` Source speeds may be in **mph**; IAS ≠ CAS. All values in following table are **KIAS**, unless explicitly marked. Minimum speeds rounded up, maximum speeds rounded down.

#### Airspeeds — generic manual / Vitesses — manuel générique
<!-- id: pa30-speeds | concepts: agk-vspeeds, me-oei, me-vmc | level: ME | kind: aircraft -->

| KIAS | Speed | Scope / Portée |
|---:|---|---|
| **77** | **VMCA** | §2: 88 mph IAS / 77 KIAS (76.5, rounded up: minimum); 90 mph / 78 kt **CAS** — do not confuse |
| **85** | **VSSE** | §4, 97 mph IAS (84.3, rounded up: minimum); minimum intentional one-engine training speed |
| **91** | **VYSE / blue line** | 105 mph IAS |
| **82** | **VXSE** | §4, 94 mph IAS |
| **78** | **VR**, flaps 0° | §4, 90 mph IAS |
| **97** | **VY** | §4, 112 mph IAS |
| **83** | **VAPP** | §4, 95 mph IAS; context-specific, not universal single-engine approach speed |
| **107** | **VFE** | §2, 124 mph IAS |
| **129** | **VLO / VLE** | §2, 149 mph IAS |
| **140** | **VA at 3,600 lb** | §2, 162 mph IAS (140.8, rounded down: maximum); **not established for 3,800 lb** |
| **171** | **VNO** | §2, 197 mph IAS |
| **203** | **VNE** | §2, 234 mph IAS |

- `!:` **These speeds are reference-manual data, not certified for C-FMCV's unverified 3,800 lb configuration.** Check actual approved AFM/supplement and instrumentation before operational use.
- `T:` §3 uses 90 mph IAS in takeoff discussion while §2 labels VMCA 90 mph **CAS** (88 mph IAS): do not collapse them into the same measurement.

#### Engine-out logic — study reference / Panne moteur — rappel d'étude
<!-- id: pa30-engine-out | concepts: me-fail, me-vmc | level: ME | kind: aircraft -->

- `P:` **Aviate / Piloter** → control yaw/bank and airspeed; generic §3 describes **105 mph IAS (91 KIAS)** SE climb and about **5° bank toward operative engine**.
- `P:` **Identify / Identifier** (dead foot) → **verify / vérifier** using suspect throttle response → troubleshoot if controllable/altitude permits → secure/feather when failure confirmed, following **actual installed checklist**.
- `T:` **Never feather an unverified engine.** One-engine climb depends on configuration, density altitude, weight and performance.
- `T:` Generic §3: crossfeed for **single-engine emergency in level flight**; **never both selectors on CROSSFEED**; return operative engine to inboard main before landing.
- `!:` Generic §3: delay landing gear / flap extension until landing assured; **do not count on a climb with gear and flaps extended after an engine-out go-around**.
- `!:` If directional control is threatened at low speed with asymmetric thrust, prioritize controllability over climb.
- `T:` Detailed emergency and feather/restart flows intentionally **not** presented as aircraft-authoritative checklist.

#### Other POH traps / Autres pièges du manuel
<!-- id: pa30-traps | concepts: agk-fuel, me-fail | level: ME | kind: aircraft -->

- `L:` §2: slip/uncoordinated manoeuvre ≥30 s or fast taxi turn immediately before takeoff may interrupt engine fuel supply when the selected tank is **<¼ full**.
- `T:` Generic §3 best glide with **both engines inoperative** at **3,600 lb**: 110 mph IAS ≈ **96 KIAS**, propellers feathered; not validated at 3,800 lb.
- `!:` Manual landing-gear extension is mechanism-specific; follow aircraft checklist and placard, not a compressed memory mnemonic.

#### Pebble
<!-- id: pa30-pebble | concepts: agk-vspeeds, me-fail, me-oei | level: ME | kind: pebble -->

- **C-FMCV** `SN 30-1732 | CCAR MTOW 3,800 lb | W&B #14 (2021): EW 2429.51 / CG 83.27 / useful 1370.49 | 3,800-lb AFM/STC basis + CG/perf = VERIFY`.
- **PA-30 REF 3,600 lb ONLY** `VMCA 77 KIAS / 78 KCAS | VSSE 85 | blue 91 | VXSE 82 | VR 78 | VFE 107 | gear 129 | VA 140 @3600 | VNO 171 | VNE 203`.
- **ENGINE OUT (study)** `CONTROL → IDENTIFY → VERIFY → TROUBLESHOOT/SECURE | FEATHER only confirmed | crossfeed emergency level only, never both | gear/flaps when landing assured`.

#### Sources / Sources
<!-- id: pa30-sources | concepts: me-oei, agk-wb | level: ME | kind: source -->

- Uploaded *Piper PA-30 Twin Comanche Pilot's Operating Handbook and FAA Approved Airplane Flight Manual*, compiled second issue 1993/1996, applicable S/N 30-1–30-2000; preamble; §2 limitations, §3 emergency procedures, §4 normal procedures/speeds. Source file: `Piper-PA-30-Flight-Manual-AV8.pdf`.
- Uploaded `C-FMCV-PA-30-WB.pdf`, Amendment #14, Oct. 7, 2021, one-page W&B change.
- CCAR MTOW 1,723.65 kg for C-FMCV: **reported by aircraft user**, not independently inspected in this card.
