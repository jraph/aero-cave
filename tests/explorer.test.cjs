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
  assert.ok(data.sections.filter(s => s.card === '16').every(s => s.u || s.h === 'Overview'));
  for (const s of data.sections) assert.equal(s.md.includes('<!-- id:'), false, s.id);
  for (const g of data.guides) for (const grp of g.groups) for (const it of grp.items) {
    assert.ok('CPME'.includes(it.s)); for (const u of it.u) assert.ok(units.has(u), `${grp.code} ${it.n} → ${u}`);
    if (it.s === 'C' || it.s === 'P') assert.ok(it.u.length, `${grp.code} ${it.n}`);
  }
});
test('no card heading is dropped and the page loads nothing external', () => {
  for (const c of data.cards) {
    const src = fs.readFileSync(path.join(root, c.file), 'utf8');
    const heads = src.split('\n').filter(l => /^#{2,4}\s+\S/.test(l)).map(l => l.replace(/^#+\s+/, '').trim());
    const have = new Set(data.sections.filter(s => s.card === c.id).map(s => s.h));
    for (const h of heads) if (h !== c.title) assert.ok(have.has(h), `${c.id}: ${h}`);
  }
  assert.equal(/<script[^>]+src=|<link[^>]+stylesheet|@import|fetch\(/.test(html), false);
});
