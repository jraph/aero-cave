#!/usr/bin/env python3
"""Build formula reader and synchronized navigation/ETE blocks; stdlib only."""
import json,re
from pathlib import Path
from build_reader import render
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'data/formulas.json').read_text())
render(d,ROOT/'readers/CPAER_Formulas_Recall_EN_FR.html',ROOT/'cheatsheets/CPAER_Formulas_Recall_EN_FR.md')
p=ROOT/'cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md'
s=p.read_text()
for key,title,rows in [('NAV','Navigation aids — ADF / VOR / DME / intercepts',next(g['rows'] for g in d['groups'] if g.get('id')=='navaids')),('ETE','Quick ETE table',next(g['rows'] for g in d['groups'] if g['title'].startswith('Timing')))]:
 block=f'<!-- BEGIN GENERATED {key} -->\n#### {title}\n\n| Memory | Calculation / example |\n|---|---|\n'+''.join('| '+r[0].replace('|',r'\|')+' | '+r[1].replace('|',r'\|')+' |\n' for r in rows)+f'<!-- END GENERATED {key} -->'
 if key=='ETE':
  from fractions import Fraction
  lines=['<!-- BEGIN GENERATED ETE -->','#### Quick ETE table','','Distance in NM × fraction = ETE in minutes. Use GS, including wind.','','| GS | ETE fraction | Mental calculation | 10 NM | 30 NM | 60 NM |','|---:|---:|---|---:|---:|---:|']
  for label,en,fr in rows:
   if not label.endswith(' kt'):continue
   gs=int(label.split()[0]);f=Fraction(60,gs)
   frac='1' if f.denominator==1 else f'{f.numerator}/{f.denominator}'
   calc='same number' if f==1 else f'÷{f.denominator} ×{f.numerator}'
   times=[]
   for distance in [10,30,60]:
    secs=round(distance*3600/gs);minutes,sec=divmod(secs,60)
    times.append(f'{minutes} min'+(f' {sec:02} s' if sec else ''))
   lines.append('| '+' | '.join([label,'×'+frac,calc]+times)+' |')
  lines+=['','90 kt: two-thirds of the NM gives minutes. Decimal minutes are not minutes:seconds.','<!-- END GENERATED ETE -->']
  block='\n'.join(lines)
 pattern=rf'<!-- BEGIN GENERATED {key} -->.*?<!-- END GENERATED {key} -->'
 assert len(re.findall(pattern,s,re.S))==1, f'Missing or duplicate {key} block'
 s=re.sub(pattern,lambda _:block,s,flags=re.S)
p.write_text(s)
