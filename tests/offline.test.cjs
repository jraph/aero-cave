// Run with: node --test tests/offline.test.cjs (no dependencies).
const {test} = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const path = require('node:path');
const source = fs.readFileSync(path.join(__dirname, '..', 'service-worker.js'), 'utf8');
function harness({failInstall=false}={}) {
  const handlers={}, stores=new Map(); let offline=false, requests=0, claimed=false, skipped=false;
  const key=r=>typeof r==='string'?r:r.url;
  const caches={
    async keys(){return [...stores.keys()]},
    async delete(name){return stores.delete(name)},
    async open(name){
      if(!stores.has(name)) stores.set(name,new Map());
      const data=stores.get(name);
      return {
        async addAll(requests){
          const pending=requests.map(r=>{
            const file=path.join(__dirname,'..',new URL(r.url).pathname.replace('/aero-cave/',''));
            if(failInstall || !fs.existsSync(file)) throw Error('Download failed');
            return [r.url,new Response(fs.readFileSync(file))];
          });
          for(const [url,response] of pending) data.set(url,response);
        },
        async match(r){return data.get(key(r))?.clone()},
        async put(r,response){data.set(key(r),response.clone())}
      };
    }
  };
  const self={location:{href:'https://example.test/aero-cave/service-worker.js'},
    addEventListener:(name,fn)=>handlers[name]=fn,
    skipWaiting:async()=>{skipped=true},clients:{claim:async()=>{claimed=true}}
  };
  vm.runInNewContext(source,{self,caches,URL,Request,Response,fetch:async()=>{requests++;if(offline)throw Error('Offline');return new Response('recovered')}});
  async function lifecycle(name){let promise;handlers[name]({waitUntil:p=>promise=p});await promise}
  async function fetchPage(url,method='GET'){
    let result;handlers.fetch({request:new Request(url,{method}),respondWith:p=>result=p});return result;
  }
  async function status(type='OFFLINE_STATUS'){let result,promise;handlers.message({data:{type},ports:[{postMessage:r=>result=r}],waitUntil:p=>promise=p});await promise;return result}
  return {stores,caches,lifecycle,fetchPage,status,goOffline:()=>offline=true,info:()=>({requests,claimed,skipped})};
}
test('installation precaches every reader and serves them without network, including directory/query URLs',async()=>{
  const h=harness();await h.lifecycle('install');await h.lifecycle('activate');h.goOffline();
  for(const file of ['','index.html?home=1','readers/CPAER_Formulas_Recall_EN_FR.html','readers/17_Pilot_Qualifications_Operator_Checks_EN_FR.html','readers/Aviation_Abbreviations_MANAB_CFS_TC_EN_FR.html?mode=fr','manifest.json','icons/icon-192.png']){
    const r=await h.fetchPage('https://example.test/aero-cave/'+file);assert.equal(r.status,200);assert.ok((await r.arrayBuffer()).byteLength);
  }
  assert.equal((await h.status()).ready,true);assert.deepEqual(h.info(),{requests:0,claimed:true,skipped:true});
});
test('failed install preserves the old version and never claims readiness',async()=>{
  const h=harness({failInstall:true});h.stores.set('aero-cave:/aero-cave/:old',new Map());
  await assert.rejects(h.lifecycle('install'));
  assert.deepEqual([...h.stores.keys()],['aero-cave:/aero-cave/:old']);assert.equal(h.info().skipped,false);
});
test('activation only clears this application’s superseded caches',async()=>{
  const h=harness();h.stores.set('aero-cave:/other-app/:old',new Map());h.stores.set('unrelated',new Map());h.stores.set('aero-cave:/aero-cave/:old',new Map());
  await h.lifecycle('install');await h.lifecycle('activate');assert.equal(h.stores.has('aero-cave:/aero-cave/:old'),false);assert.equal(h.stores.has('unrelated'),true);assert.equal(h.stores.has('aero-cave:/other-app/:old'),true);
});
test('external sources, sibling apps, unknown pages and mutations are not intercepted',async()=>{
  const h=harness();
  for(const url of ['https://tc.canada.ca/source.pdf','https://example.test/other-app/index.html','https://example.test/aero-cave/missing.html'])assert.equal(await h.fetchPage(url),undefined);
  assert.equal(await h.fetchPage('https://example.test/aero-cave/index.html','POST'),undefined);
});
test('readiness detects missing data and a successful fetch repairs it',async()=>{
  const h=harness();await h.lifecycle('install');
  const data=[...h.stores.values()][0];data.delete('https://example.test/aero-cave/index.html');assert.equal((await h.status()).ready,false);
  await h.fetchPage('https://example.test/aero-cave/index.html');assert.equal((await h.status()).ready,true);
});
test('Save offline restores evicted files even when the worker version has not changed',async()=>{
  const h=harness();await h.lifecycle('install');
  const data=[...h.stores.values()][0];data.clear();assert.equal((await h.status()).ready,false);
  assert.equal((await h.status('CACHE_OFFLINE')).ready,true);
});
