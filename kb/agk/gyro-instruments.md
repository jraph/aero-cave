# Gyro & vacuum instruments / Instruments gyroscopiques et à dépression
<!-- concept: agk-gyro | level: PPL CPL IR -->

[Index](README.md) · concept `agk-gyro` · unit IDs are stable: never rename one.

***
#### Gyroscopic instruments — principles and errors
<!-- id: agk-gyro-instruments-principles-errors | also: ifr-emerg | level: PPL CPL IR -->

| Property | Meaning | Used by |
|---|---|---|
| Rigidity in space | spinning rotor holds its plane (AI ~15 000 rpm, HI ~10 000 rpm) | attitude indicator, heading indicator |
| Precession | force acts 90° ahead in direction of rotation; friction + manoeuvres → drift; excess force → tumble | turn indicator / coordinator |

- Power: AI + HI typically vacuum (engine pump, regulator, suction gauge); turn-and-slip normally electric (~8 000 rpm). Different sources = redundancy. [TP 2076 2.1.3 C]
- **AI** errors: turn error (precesses toward inside of turn; steep turns → pitch from VSI + altimeter) · acceleration → false pitch-up · deceleration → false pitch-down. Limits: newer 360° bank / 85° pitch, no tumble; older tumble at 100° bank or 70° pitch. AI does not show coordination: ball needed. [TP 2076 2.1.3 D.1]
- **HI**: no direction-seeking; set to compass on ground or steady unaccelerated flight. Drift = real precession (manoeuvres, friction) + apparent precession (aircraft movement, earth rotation). Check vs compass **at least every 15 min**. [TP 2076 2.1.3 D.2]
- **Turn coordinator**: gyro canted ~35° → senses roll rate + yaw rate; once bank steady, shows rate only. Standard rate 3°/s = wing on index. Ball = quality of turn (slip/skid), not gyro. Turn-and-slip needle shows rate only, not bank. [TP 2076 2.1.3 D.3]
- **Slaved (gyrosyn) compass**: remote magnetic sensor slaves the heading gyro; free/non-slaved mode for high latitudes (set by hand). [TP 2076 2.1.3 D.4]
- `T:` HI has no north-seeking ability: re-align every ≤15 min.
***
#### Control and performance instruments — attitude instrument flying
<!-- id: agk-control-performance-instrument-flying | also: agk-inst | level: CPL -->

- **Control** instruments: **attitude indicator + power** (RPM, MP, EPR) — set directly, in known amounts. **Performance**: airspeed, VSI, altimeter, HI, turn coordinator/turn-and-slip, compass — show the result, lag a little. **Navigation**: track/position.
- `P` Establish attitude + power on control instruments → **trim** (pressures neutral; ball centred with rudder trim) → **cross-check** performance → **adjust**.
- `M` **Attitude + power = performance.**

- Sources: [TP 2076](https://www.phoenixaviation.ca/IPM%20tp2076e.pdf) 2.3.1.
***