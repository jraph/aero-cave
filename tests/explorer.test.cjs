// Run with: node --test tests/explorer.test.cjs (needs python3 for the staleness check).
const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {spawnSync} = require('node:child_process');
const root = path.join(__dirname, '..');
const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
const data = JSON.parse(/<script id="data" type="application\/json">([\s\S]*?)<\/script>/.exec(html)[1]);

test('index.html matches the current cards, concept files and ontology', () => {
  const r = spawnSync('python3', ['explorer/build_explorer.py', '--check'], {cwd: root, encoding: 'utf8'});
  if (r.error) return; // python unavailable: skip
  assert.equal(r.status, 0, r.stderr || r.stdout);
});
test('every section has a valid card, path and concept; every concept link resolves', () => {
  const ids = new Set(data.concepts.map(c => c.id)), cards = new Set(data.cards.map(c => c.id)), paths = new Set(data.paths.map(p => p.id));
  assert.equal(ids.size, data.concepts.length);
  for (const c of data.concepts) for (const ref of [...c.broader, ...c.related]) assert.ok(ids.has(ref), `${c.id} → ${ref}`);
  for (const s of data.sections) {
    assert.ok(cards.has(s.card)); assert.ok(s.c.length && s.c.every(c => ids.has(c)), s.id);
    const lv = s.p.length ? s.p : s.ph || []; assert.ok(lv.length && lv.every(p => paths.has(p)), s.id); assert.ok(s.md.trim(), s.id);
    assert.ok(!(s.p.length && s.ph), s.id + ': hand level only as a fallback');
  }
});
test('guide items point at existing stable unit IDs; ID comments never leak into content', () => {
  const units = new Map(data.sections.filter(s => s.u).map(s => [s.u, s]));
  assert.equal(units.size, data.sections.filter(s => s.u).length, 'duplicate unit id');
  assert.ok(data.sections.every(s => s.u), 'every unit has a stable ID');
  assert.equal(data.sections.some(s => s.card === '16'), false, 'card 16 is retired');
  for (const c of data.cards.filter(c => c.kb)) for (const f of Object.keys(c.files)) { const us = data.sections.filter(x => x.f === f), n = us.filter(x => x.h === 'Pebble').length; assert.ok(n <= 1, f + ': at most one Pebble'); if (n) assert.equal(us[us.length - 1].h, 'Pebble', f + ': Pebble last'); }
  for (const s of data.sections) assert.equal(s.md.includes('<!-- id:'), false, s.id);
  for (const g of data.guides) for (const grp of g.groups) for (const it of grp.items) {
    assert.ok('CPME'.includes(it.s)); for (const u of it.u) assert.ok(units.has(u), `${grp.code} ${it.n} → ${u}`);
    if (it.s === 'C' || it.s === 'P') assert.ok(it.u.length, `${grp.code} ${it.n}`);
  }
});
test('no card heading is dropped and the page loads nothing external', () => {
  for (const c of data.cards) for (const file of c.kb ? Object.keys(c.files) : [c.file]) {
    const lines = fs.readFileSync(path.join(root, file), 'utf8').split('\n');
    const have = new Set(data.sections.filter(s => s.card === c.id && (!c.kb || s.f === file)).map(s => s.h));
    lines.forEach((l, i) => {
      if (!/^#{2,4}\s+\S/.test(l)) return;
      const h = l.replace(/^#+\s+/, '').trim(), next = lines.slice(i + 1).find(x => x.trim());
      if (h === c.title || /^→ Moved/.test(next || '')) return; // title or pointer stub (target checked by the build)
      assert.ok(have.has(h), `${file}: ${h}`);
    });
  }
  assert.equal(/<script[^>]+src=|<link[^>]+stylesheet|@import|fetch\(/.test(html), false);
});

test('formula tables and memory traps render in each selected language', () => {
  const vm = require('node:vm');
  const renderer = html.slice(html.indexOf('function href('), html.indexOf('function pebble('));
  const formulas = data.sections.filter(s => s.card === 'F' || s.md.includes('| Label | English | Français |'));
  const tableLines = formulas.flatMap(s => s.md.split('\n')).filter(line => line.startsWith('|') && !line.startsWith('| Label') && !line.startsWith('|---'));
  const traps = formulas.flatMap(s => s.md.split('\n')).filter(line => /^\*\*.+?\*\* · /.test(line));
  assert.equal(tableLines.length, 265);
  assert.equal(traps.length, 11);
  for (const lang of ['en', 'fr', 'both']) {
    const render = vm.runInNewContext(renderer + '\nmd', {lang, esc: s => s, URL, REPO: 'https://example.org/'});
    for (const row of tableLines) {
      const output = render('| Label | English | Français |\n|---|---|---|\n' + row, {id:'F'});
      assert.equal((output.match(/<td>/g) || []).length, lang === 'both' ? 3 : 2);
    }
    for (const line of traps) {
      const [, en, fr] = /\*\* · (.+?) \/ (.+)$/.exec(line);
      const output = render(line, {id:'F'});
      assert.equal(output.includes(en), lang !== 'fr');
      assert.equal(output.includes(fr), lang !== 'en');
    }
  }
});

test('abbreviation collection keeps bilingual rows, TC scope and searchable memory reminders', () => {
  const vm = require('node:vm');
  const renderer = html.slice(html.indexOf('function href('), html.indexOf('function pebble('));
  const glossary = data.sections.filter(s => s.card === 'A');
  const norm = s => s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const render = (unit, lang, tokens = []) => vm.runInNewContext(renderer + '\nmd', {
    lang, tokens, norm, esc: s => s, URL, REPO: 'https://example.org/'
  })(unit.md, {id:'A', heading:unit.h});
  for (const lang of ['en', 'fr', 'both']) {
    const views = glossary.map(unit => render(unit, lang));
    const count = views.join('').match(/<td>/g).length;
    assert.equal(count, (369 + 79 + 54) * (lang === 'both' ? 3 : 2));
    assert.equal(views.at(-1).includes('<th>English · TC exam</th>'), lang !== 'fr');
    assert.equal(views.at(-1).includes('<th>Français · étude</th>'), lang !== 'en');
  }
  const traps = glossary.find(s => s.u.startsWith('abbr-memory-traps'));
  const result = render(traps, 'fr', ['tempo']);
  assert.equal((result.match(/<tbody><tr>/g) || []).length, 1);
  assert.equal((result.match(/<td>/g) || []).length, 2);
  assert.match(result, /la moitié de la période TEMPO/);
});
