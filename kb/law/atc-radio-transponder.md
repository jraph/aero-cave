# ATC, radio & transponder / ATC, radio et transpondeur
<!-- concept: law-atc | level: PPL CPL -->

[Index](README.md) · concept `law-atc` · unit IDs are stable: never rename one.

***
#### Radio / transponder
<!-- id: law-radio-transponder | from: 01 | level: PPL CPL -->

- XPDR: `1200 ≤12500` | `1400 >12500` | `7600 comm` | `7700 emerg` | `7500 hijack`.
- Call: who-called | who-you-are | where | what-want. Readback: clearance/runway/hold-short/alt/hdg/squawk.
- `T:` “roger”≠cleared. listen before transmit. aviate before radio.
***
#### ATC clearances / instructions
<!-- id: law-atc-clearances-instructions | from: 04 | level: PPL CPL IR -->

- Comply with ATC clearances/instructions received and accepted, except emergency authority or amended clearance. `[CAR 602.31]`
- If unable/unsafe: advise ATC immediately; do not silently improvise.
- `T:` clearance ≠ information; “roger” does not mean approval to deviate.
***
#### ATS surveillance / wake / RVSM
<!-- id: law-ats-surveillance-wake-rvsm | from: 04 | level: CPL -->

| CAVE | Rule / trap |
|---|---|
| `G` ATS SEP | Surveillance **5 NM standard / 3 NM authorized terminal**; other minima may apply. [AIM RAC](https://tc.canada.ca/en/aviation/publications/transport-canada-aeronautical-information-manual-tc-aim) |
| `G` vertical | **1,000 ft below FL290**; RVSM **FL290–FL410 incl. 1,000 ft** for approved ACFT; higher non-RVSM generally **2,000 ft**. |
| `G` WAKE CAT | **S=A380 · H>136t · M>7t to <136t · L≤7t**. |
| `G` WAKE NM | Leader→follower: **S→S/H/M/L=4/6/7/8 · H→H/M/L=4/5/6 · M→L=4**; unspecified pairs still need normal ATS SEP. |
| `G` TKOF MIN | Specified same/close-parallel THLD: **H→following 2 min**; specified INTXN/downstream: **3 min**; **M→L same THLD advisory, INTXN 3 min**. Check configuration. |
| `G` WAKE AVOID | Strongest heavy+clean+slow; vortex ↓ and downwind drift; avoid behind/below/downwind · jet blast/propwash ≠ vortex WAKE. |

`M:` **ATS 5/3NM | RVSM FL290–410 1,000ft | WAKE S 4/6/7/8 · H 4/5/6 · M→L 4NM | H TKOF 2/3min cases**.
***
#### TWR light signals — NORDO
<!-- id: law-twr-light-signals-nordo | from: 04 | also: emg-comms | level: PPL CPL -->

| Signal | IN FLT | ON GND |
|---|---|---|
| Steady GN | LDG CLNC | TKOF CLNC |
| Flash GN | Return for LDG (not CLNC) | Taxi CLNC |
| Steady RED | Give way / circle | STOP |
| Flash RED | A/D unsafe / NO LDG | Taxi clear LDG area / RWY |
| Flash WHITE | — | Return starting point |
| Alternating RED/GN | Extreme caution | Extreme caution |

- `P:` ACK IN FLT → rock wings; night → flashing lights as prescribed. [TC AIM RAC](https://tc.canada.ca/en/aviation/publications/transport-canada-aeronautical-information-manual-tc-aim).
- `T:` Flash GN ≠ LDG CLNC; **steady GN** = LDG CLNC.
- `M:` **IN FLT GN steady=LDG/flash=return · RED steady=circle/flash=unsafe | GND GN steady=TKOF/flash=taxi · RED steady=STOP/flash=clear · WHITE=return**.
***
#### Pebble
<!-- id: law-atc-radio-transponder-pebble | level: PPL CPL IR -->

- XPDR `1200 ≤12,500 | 1400 >12,500 | 7600 comm | 7700 emergency | 7500 hijack`
- ATC CAR 602.31 `comply with clearances/instructions received and accepted, except emergency authority or amended clearance | unable → advise immediately | “roger” ≠ cleared`
- LIGHTS `in flight: steady green = LDG clearance / flashing green = return for landing / steady red = give way, circle / flashing red = unsafe, no landing | ground: steady green = TKOF / flashing green = taxi / steady red = STOP / flashing red = taxi clear / flashing white = return to start`
- ATS / WAKE `surveillance 5 NM standard / 3 NM authorized terminal | 1,000 ft below FL290; RVSM FL290–FL410 1,000 ft approved ACFT | wake S→S/H/M/L 4/6/7/8 NM · H→H/M/L 4/5/6 · M→L 4 | H ahead: 2 min same threshold, 3 min intersection`
***
