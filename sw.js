const CACHE = 'maeuse-filmliste-v77';
const CORE = ['./','./index.html','./manifest.webmanifest','./icon-180.png','./icon-512.png'];
self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE).catch(()=>{})));
});
self.addEventListener('activate', event => {
  event.waitUntil((async()=>{
    const keys=await caches.keys();
    await Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k)));
    await self.clients.claim();
  })());
});
self.addEventListener('fetch', event => {
  const req=event.request;
  if(req.method!=='GET') return;
  const url=new URL(req.url);
  if(url.origin!==self.location.origin) return;
  const isFresh = req.mode==='navigate' || url.pathname.endsWith('/index.html') || url.pathname.endsWith('/suggestions.json') || url.pathname.endsWith('/movies.json');
  if(isFresh){
    event.respondWith((async()=>{
      try{
        const res=await fetch(req,{cache:'no-store'});
        if(res && res.ok){const c=await caches.open(CACHE);c.put(req,res.clone());}
        return res;
      }catch(e){return (await caches.match(req)) || (await caches.match('./index.html'));}
    })());
    return;
  }
  event.respondWith((async()=>{
    const cached=await caches.match(req);
    if(cached)return cached;
    const res=await fetch(req);
    if(res&&res.ok){const c=await caches.open(CACHE);c.put(req,res.clone());}
    return res;
  })());
});
