// Run with: node --test tests/explorer.test.cjs (needs python3 for the staleness check).
const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {spawnSync} = require('node:child_process');
const root = path.join(__dirname, '..');
const html = fs.readFileSync(path.join(root, 'explorer.html'), 'utf8');
const data = JSON.parse(/<script id="data" type="application\/json">([\s\S]*?)<\/script>/.exec(html)[1]);

test('explorer.html matches the current cards and ontology', () => {
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
    assert.ok(s.p.length && s.p.every(p => paths.has(p)), s.id); assert.ok(s.md.trim(), s.id);
  }
});
test('guide items point at existing stable unit IDs; ID comments never leak into content', () => {
  const units = new Map(data.sections.filter(s => s.u).map(s => [s.u, s]));
  assert.equal(units.size, data.sections.filter(s => s.u).length, 'duplicate unit id');
  assert.ok(data.sections.filter(s => s.card === 'MET' || s.card === 'IFR' || s.card === '05').every(s => s.u || s.h === 'Overview'));
  assert.equal(data.sections.some(s => s.card === '16'), false, 'card 16 is retired');
  for (const f of [...Object.keys(data.cards.find(c => c.id === 'MET').files), ...Object.keys(data.cards.find(c => c.id === 'IFR').files)]) if (!/recall\.md$/.test(f)) assert.equal(data.sections.filter(s => s.f === f && s.h === 'Pebble').length, 1, f + ': one Pebble');
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
