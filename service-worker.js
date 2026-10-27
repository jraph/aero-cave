/* Bump VERSION whenever a reader, layout, icon or app shell changes. */
'use strict';
const VERSION = '2026-10-26-13';
const BASE = new URL('./', self.location.href);
const PREFIX = 'aero-cave:' + BASE.pathname + ':';
const CACHE = PREFIX + VERSION;
const FILES = [
  'index.html', 'manifest.json',
  'icons/icon-192.png', 'icons/icon-512.png', 'icons/apple-touch-icon.png',
  'readers/CPAER_Formulas_Recall_EN_FR.html',
  'readers/Aviation_Abbreviations_MANAB_CFS_TC_EN_FR.html',
  'readers/17_Pilot_Qualifications_Operator_Checks_EN_FR.html'
];
const URLS = FILES.map(path => new URL(path, BASE).href);
self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE);
    try {
      // All-or-nothing installation; bypass the HTTP cache when updating.
      await cache.addAll(URLS.map(url => new Request(url, {cache: 'reload'})));
      await self.skipWaiting();
    } catch (error) {
      await caches.delete(CACHE);
      throw error;
    }
  })());
});
self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    await Promise.all((await caches.keys()).filter(key => key.startsWith(PREFIX) && key !== CACHE).map(key => caches.delete(key)));
    await self.clients.claim();
  })());
});
self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);
  if (url.origin !== BASE.origin || !url.pathname.startsWith(BASE.pathname)) return;
  if (url.pathname === BASE.pathname) url.pathname += 'index.html';
  url.search = ''; url.hash = '';
  if (!URLS.includes(url.href)) return; // External sources and unknown paths stay network-only.
  event.respondWith((async () => {
    const cache = await caches.open(CACHE);
    const hit = await cache.match(url.href);
    if (hit) return hit;
    const response = await fetch(new Request(url.href, {cache: 'reload'}));
    if (response.ok && response.type !== 'opaque') await cache.put(url.href, response.clone());
    return response;
  })());
});
self.addEventListener('message', event => {
  if (!['OFFLINE_STATUS', 'CACHE_OFFLINE'].includes(event.data?.type) || !event.ports[0]) return;
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE);
    if (event.data.type === 'CACHE_OFFLINE') {
      try { await cache.addAll(URLS.map(url => new Request(url, {cache: 'reload'}))); }
      catch (_) { event.ports[0].postMessage({ready:false, version:VERSION}); return; }
    }
    const ready = (await Promise.all(URLS.map(url => cache.match(url)))).every(Boolean);
    event.ports[0].postMessage({ready, version: VERSION});
  })());
});
