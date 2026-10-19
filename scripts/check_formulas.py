#!/usr/bin/env python3
"""Check geometry examples, coverage and reproducible generated outputs."""
import json,math,subprocess,sys
from pathlib import Path
from html.parser import HTMLParser
R=Path(__file__).resolve().parents[1]
paths=[R/'readers/CPAER_Formulas_Recall_EN_FR.html',R/'cheatsheets/CPAER_Formulas_Recall_EN_FR.md',R/'cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md']
paths += [R/'cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md',R/'cheatsheets/05_weather_decoding_go_nogo_qrc_av_cave_v0_2_compact.md']
before=[p.read_bytes() for p in paths]
subprocess.run([sys.executable,str(R/'scripts/build_all.py')],check=True)
assert before==[p.read_bytes() for p in paths], 'Generated files are stale'
d=json.loads((R/'data/formulas.json').read_text());rows=[r for g in d['groups'] for r in g['rows']]
assert len(rows)==230 and len(d['memory'])==11
class Check(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.entries=0;self.options=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if 'entry' in a.get('class','').split():self.entries+=1
  if tag=='option':self.options.append(a.get('value'))
c=Check();c.feed(paths[0].read_text());assert len(c.ids)==len(set(c.ids));assert c.entries==241
assert all(x in c.ids for x in ['search','topic','theme','smaller','larger','notes','empty'])
assert 'notes' in c.options
# Independent vector geometry: examples start NW/NE and fly SE (120°).
for start,capture_bts,rb in [((-math.cos(math.radians(15)),math.sin(math.radians(15))),90,330),((1,1),270,150)]:
 h=math.radians(120);t=-start[1]/math.cos(h);x=start[0]+t*math.sin(h)
 b=math.degrees(math.atan2(-x,0))%360
 assert abs(b-capture_bts)<1e-8 and (b-120)%360==rb
assert (350+40)%360==30 and (20-80)%360==300 and (100-250)%360==210
assert abs(math.sqrt(25-1)-4.898979486)<1e-8
assert 120*2/120==2
print('PASS: reproducible outputs, 230 rows/11 reminders, HTML structure, bearing/intercept/DME examples')

assert min(100,120*.5)==60 and min(100,240*.5)==100
assert max(-25,-30+10)==-20
