# Knowledge base

One Markdown file per ontology concept (`explorer/ontology.json`), grouped by domain.

| Domain | Concept files |
|---|---:|
| [Air law & procedures](law/README.md) | 15 |
| [Navigation](nav/README.md) | 4 |
| [Meteorology](met/README.md) | 16 |
| [Aeronautics: general knowledge](agk/README.md) | 13 |
| [IFR & INRAT](ifr/README.md) | 16 |
| [Multi-engine](me/README.md) | 4 |

## File format

```markdown
# English title / Titre français
<!-- concept: met-fog | level: PPL CPL IR -->

#### Unit heading
<!-- id: wx-fog | also: met-decide | level: IR -->

- content
***
#### Pebble
<!-- id: met-fog-pebble | also: study-pebble | level: PPL CPL IR -->

- TOPIC `token | token | token`
```

- **Unit** = one `####` section. Its comment sits on the line under the heading.
- `id` is required and permanent: never rename or reuse one. `explorer/syllabus.json` and saved links depend on it.
- The file's `concept:` is every unit's primary concept. `also:` adds other concepts; `level:` overrides the file's level (PPL, CPL, IR, ME). The explorer shows a unit's level from the TC guides that cite it; the hand-set `level:` is shown (dashed) only when no guide cites the unit.
- `from:` (optional) records which retired card a unit came from.
- **Pebble** = the last unit of a concept file: dense recall of that file only, introducing nothing new. One per file, no separate Pebble files.
- Ordered procedures, QRCs and aircraft-type data stay in `cheatsheets/`, with `<!-- id: … | concepts: a, b | level: … -->` under each heading.
