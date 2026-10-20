#!/usr/bin/env python3
"""Render a bilingual JSON dataset to an offline HTML reader and Markdown source."""
import argparse,html,json,re
from pathlib import Path
from memory_section import refine_memory_section

def render(data,html_path,md_path):
    e=html.escape
    title=data['title'];groups=data['groups'];memory=data.get('memory',[])
    assert groups and memory, 'Provide content groups and a memory section'
    total=sum(len(g['rows']) for g in groups)
    options=['<option value="all">All topics / Tous les thèmes</option>'];sections=[]
    md=['# '+title,'',data.get('summary',''),'']
    for i,g in enumerate(groups):
        options.append(f'<option value="g{i}">{e(g["title"])}</option>')
        entries=[];md += ['***','',f'**{g["title"]}**','','| Label | English | Français |','|---|---|---|']
        for row in g['rows']:
            assert len(row)==3 and all(isinstance(v,str) and v.strip() for v in row), 'Rows need label, EN, FR'
            label,en,fr=row
            entries.append(f'<div class="entry"><strong class="code">{e(label)}</strong><div class="meaning en" lang="en-CA"><span class="lang">EN</span>{e(en)}</div><div class="meaning fr" lang="fr-CA"><span class="lang">FR</span>{e(fr)}</div></div>')
            vals=[v.replace('|',r'\|').replace('\n','<br>') for v in row]
            md.append('| '+' | '.join(vals)+' |')
        sections.append(f'<section class="group" id="g{i}" aria-labelledby="h{i}"><h2 id="h{i}">{e(g["title"])}<span class="group-count">{len(g["rows"])}</span></h2><div class="column-labels" aria-hidden="true"><span>{e(data.get("label","Label"))}</span><span>English</span><span>Français</span></div><div class="entries">'+''.join(entries)+'</div></section>')
    md += ['','***','','**Memory traps & examples / Pièges et exemples**','']
    for label,body in memory:md += [f'**{label}** · {body}','']
    sources=data.get('sources',[])
    for label,url in sources:
        assert url.startswith(('https://','http://')), 'Sources must use web URLs'
    links=' · '.join(f'<a href="{e(url,quote=True)}">{e(label)}</a>' for label,url in sources)
    md += [' · '.join(f'[{label}]({url})' for label,url in sources),'']
    template=(Path(__file__).resolve().parent.parent/'assets/reader.html').read_text()
    tokens={'TITLE':e(title),'EYEBROW':e(data.get('eyebrow','Study / Étude')),'SUMMARY':e(data.get('summary',f'{total} entries / entrées')),'OPTIONS':''.join(options),'SECTIONS':''.join(sections),'NOTES':'','SOURCES':links,'LABEL':e(data.get('label','Label')),'TOTAL':str(total),'KEY':re.sub('[^a-z0-9-]','',data.get('key','cave-study').lower())}
    for key,value in tokens.items():template=template.replace('@@'+key+'@@',value)
    assert not re.search(r'@@[A-Z]+@@',template),'Unresolved template placeholder'
    result=refine_memory_section(template,traps=memory,total=total,noun='entries · entrées')
    for path,body in [(html_path,result),(md_path,'\n'.join(md))]:
        path.parent.mkdir(parents=True,exist_ok=True);path.write_text(body)
    print(f'Created {total} bilingual entries and {len(memory)} memory reminders')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dataset',type=Path);parser.add_argument('--html',type=Path,required=True);parser.add_argument('--markdown',type=Path,required=True)
    args=parser.parse_args();render(json.loads(args.dataset.read_text()),args.html,args.markdown)
