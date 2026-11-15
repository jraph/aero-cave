# Knowledge base

One Markdown file per ontology concept (`explorer/ontology.json`), grouped by domain.

| Domain | Concept files |
|---|---:|
| [Air law & procedures](law/README.md) | 16 |
| [Navigation](nav/README.md) | 5 |
| [Meteorology](met/README.md) | 16 |
| [Aeronautics: general knowledge](agk/README.md) | 14 |
| [IFR & INRAT](ifr/README.md) | 16 |
| [Multi-engine](me/README.md) | 4 |

## Note markers

A marker starts a line, in backticks. Table key letters use the same codes (`G` in a table = general). The explorer shows the meaning on hover and in the home-page legend.

| Marker | Meaning | Sens |
|---|---|---|
| `P:` | procedure / flow | procédure / séquence |
| `G:` | gate: check before continuing | vérification avant de continuer |
| `S:` | symptom | symptôme |
| `T:` | trap | piège |
| `M:` | memory aid | aide-mémoire |
| `F:` | formula | formule |
| `R:` | rule | règle |
| `L:` | POH limitation | limite du POH |
| `N:` | POH note | note du POH |
| `K:` | diagram key | légende du schéma |
| `!:` | safety-critical | sécurité critique |
| `?:` | verify: not checked against a TC source | à vérifier : non contrôlé contre une source TC |
| `SRC:` | source | source |

A marker may carry a short qualifier (`P stall:`, `F rough:`).

## File format

```markdown
# English title / Titre français
<!-- concept: met-fog | level: PPL CPL IR -->

#### Unit heading
<!-- id: wx-fog | also: met-decide | level: IR -->

- content
***
#### Pebble
<!-- id: met-fog-pebble | level: PPL CPL IR -->

- TOPIC `token | token | token`
```

- **Unit** = one `####` section. Its comment sits on the line under the heading.
- `id` is required and permanent: never rename or reuse one. `explorer/syllabus.json` and saved links depend on it.
- The file's `concept:` is every unit's primary concept. `also:` adds other concepts; `level:` overrides the file's level (PPL, CPL, IR, ME). The explorer shows a unit's level from the TC guides that cite it; the hand-set `level:` is shown (dashed) only when no guide cites the unit. A ✈ on a level badge (`PPL ✈`, `CPL ✈`) means that level's guide marks a citing item essential; each guide's marks stay with its own level.
- `kind:` says what the note is: `knowledge` (default in kb), `procedure`, `formula`, `trap`, `pebble` (default for a Pebble), `glossary`, `aircraft`, `source`. The subject is the concept; the kind is never a concept.
- A table headed `| Label | English | Français |` is bilingual: the explorer shows the column for the chosen language.
- `from:` (optional) records which retired card a unit came from.
- **Pebble** = the last unit of a concept file: dense recall of that file only, introducing nothing new. One per file, no separate Pebble files.
- Ordered procedures, QRCs and aircraft-type data stay in `cheatsheets/`, with `<!-- id: … | concepts: a, b | level: … -->` under each heading; the card's default kind is set in `explorer/ontology.json`.
