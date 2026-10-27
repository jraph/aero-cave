// Static regression test for the dense Card 17 table. Run: node --test tests/card17-table-layout.test.cjs
const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const html = fs.readFileSync(path.join(__dirname, '..', 'readers', '17_Pilot_Qualifications_Operator_Checks_EN_FR.html'), 'utf8');
test('operation table header aligns with every data row', () => {
  const table = html.match(/<table class="ops">([\s\S]*?)<\/table>/);
  assert.ok(table, 'main operation table exists');
  const header = table[1].match(/<thead>([\s\S]*?)<\/thead>/);
  const body = table[1].match(/<tbody>([\s\S]*?)<\/tbody>/);
  assert.ok(header && body);
  const columns = (header[1].match(/<th scope="col">/g) || []).length;
  assert.equal(columns, 11, '11 header titles, including aircraft applicability and examples');
  assert.equal((table[1].match(/<col style="width:/g) || []).length, columns, 'one fixed width per header column');
  const rows = [...body[1].matchAll(/<tr class="entry"[\s\S]*?<\/tr>/g)];
  assert.equal(rows.length, 10);
  for (const [index, row] of rows.entries()) {
    const cells = (row[0].match(/<(?:th|td)(?:\s[^>]*)?>/g) || []).length;
    assert.equal(cells, columns, `data row ${index + 1} must align with headers`);
  }
});
test('column headers do not overlap the first row', () => {
  assert.doesNotMatch(html, /thead\s*\{[^}]*position:\s*sticky/);
  assert.match(html, /thead\s*\{background:var\(--stripe\)\}/);
  assert.match(html, /\.ops\{table-layout:fixed;min-width:1260px\}/);
  assert.match(html, /\.ops\{min-width:0;table-layout:auto\}/);
});
