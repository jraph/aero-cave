import html,re
TRAPS=[]
def refine_memory_section(text,traps=None,total=369,noun="terms · termes"):
 if traps is None:traps=TRAPS
 e=html.escape
 old=re.search(r'<section id="notes" class="notes">([\s\S]*?)</section>',text)
 if not old:raise ValueError('Memory section missing')
 src=re.search(r'<article class="note"><h3>Sources / Références</h3><p>([\s\S]*?)</p></article>',old[1])
 rows=''.join(f'<div class="entry memory-entry" data-kind="trap"><span><strong class="memory-label">{e(label)}</strong> · {e(body)}</span></div>' for label,body in traps)
 section=f'<section class="group memory-group" id="notes" aria-labelledby="notes-heading"><h2 id="notes-heading">Memory traps &amp; examples / Pièges et exemples<span class="group-count">{len(traps)}</span></h2><div class="entries">{rows}</div></section>'
 text=text[:old.start()]+section+text[old.end():]
 text=text.replace('</select><div class="tools">','<option value="notes">Memory traps &amp; examples / Pièges et exemples</option></select><div class="tools">',1)
 text=text.replace('<a href="#notes">Memory traps','<a id="notes-link" href="#notes">Memory traps',1)
 if src:text=text.replace('<footer>','<footer><p class="source-note">'+src[1]+'</p>',1)
 css='.memory-entry:not([hidden]){display:block!important;grid-template-columns:none!important;line-height:1.25;padding:.14rem .55rem}.memory-label{color:var(--accent)}.source-note{margin:.2rem 0 .7rem}.memory-group{scroll-margin-top:10rem}'
 text=text.replace('</style>',css+'\n</style>',1)
 text=text.replace('let n=0;const q=','let n=0,traps=0;const q=',1)
 text=text.replace('g.querySelector(\'.group-count\').textContent=hits;n+=hits',"g.querySelector('.group-count').textContent=hits;if(g.id==='notes')traps+=hits;else n+=hits",1)
 text=re.sub(r"n\+' / \d+ entries · (?:termes|phrases)'",f"n+' / {total} {noun}; '+traps+' / {len(traps)} traps · pièges'",text,count=1)
 text=text.replace("$('empty').hidden=n!==0", "$('empty').hidden=(n+traps)!==0",1)
 hook="$('notes-link').addEventListener('click',()=>{$('topic').value='notes';$('search').value='';filter()});"
 text=text.replace('let before=null;',hook+'let before=null;',1)
 return text
