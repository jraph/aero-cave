# Gyro & vacuum instruments / Instruments gyroscopiques et à dépression
<!-- concept: agk-gyro | level: PPL CPL IR -->

[Index](README.md) · concept `agk-gyro` · unit IDs are stable: never rename one.

***
#### Gyroscopic instruments — principles and errors
<!-- id: agk-gyro-instruments-principles-errors | also: ifr-emerg | level: PPL CPL IR -->

| Property | Meaning | Used by |
|---|---|---|
| Rigidity in space | spinning rotor holds its plane | attitude indicator, heading indicator |
| Precession | force acts 90° along rotation | turn indicator / coordinator |

- Power: vacuum/pressure (AI, HI typical) or electric (turn coordinator typical) — redundancy by different source.
- **AI** errors: small pitch/bank error after acceleration and turns; topples past limits (older units); slow erect after start.
- **HI** errors: drift (real precession + apparent drift from earth rotation, ~15°/h × sin latitude); reset to compass in straight, unaccelerated flight; can tumble past limits.
- **Turn coordinator** = rate + roll rate; ball = slip/skid (not gyro).
- `T:` HI has no north-seeking ability: re-align every ~15 min.
- `?:` general instrument knowledge; not checked against a TC source.
***
