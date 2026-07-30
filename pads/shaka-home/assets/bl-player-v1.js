/* 🦋 bl-player.js — Butterflies and Love, everywhere. One line: <script src="https://shaka-home-cbhjr5ziii-ffieyo32.taur.link/assets/bl-player.js"></script> */
(function(){
if (document.getElementById('miniplayer')) return;
const SRC = 'https://shaka-anthem-gzdk4epeah-ffieyo32.taur.link/assets/i-open-sourced-my-whole-universe.mp3';
const wrap = document.createElement('div');
wrap.innerHTML = `
<div id="miniplayer" style="position:fixed;bottom:20px;right:20px;z-index:99999;display:flex;align-items:center;gap:12px;background:linear-gradient(150deg,rgba(240,180,41,.16),rgba(23,17,38,.92));border:1px solid #f0b429;border-radius:999px;padding:10px 20px 10px 12px;backdrop-filter:blur(8px);box-shadow:0 8px 40px rgba(240,180,41,.25);font-family:'Avenir Next','Segoe UI',system-ui,sans-serif">
  <button id="songbtn" style="width:44px;height:44px;border-radius:50%;border:none;background:#f0b429;color:#241a02;font-size:1.15rem;cursor:pointer;animation:blpulse 2s infinite">▶</button>
  <div style="line-height:1.3">
    <div id="songstatus" style="font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:#ffd97a">tap to play — Butterflies and Love</div>
    <div style="font-size:.82rem;color:#b9a8cf">demo recorded with Ethereum Singapore for Aya Miyaguchi 🦋</div>
  </div>
</div>
<audio id="thesong" src="${SRC}" preload="auto"></audio>
<style>@keyframes blpulse{0%,100%{box-shadow:0 0 0 0 rgba(240,180,41,.5)}50%{box-shadow:0 0 0 12px rgba(240,180,41,0)}}@keyframes bleq{0%,100%{transform:scaleY(.4)}50%{transform:scaleY(1)}}.blbars{display:inline-flex;gap:2.5px;align-items:flex-end;height:14px;margin-right:2px}.blbars i{width:3px;background:#f0b429;border-radius:2px;animation:bleq .9s ease-in-out infinite}.blbars i:nth-child(2){animation-delay:.2s}.blbars i:nth-child(3){animation-delay:.4s}</style>`;
document.body.appendChild(wrap);
const song = document.getElementById('thesong');
const btn = document.getElementById('songbtn');
const status = document.getElementById('songstatus');
const KEY = 'bl_song';
let playing = false;
const bc = ('BroadcastChannel' in window) ? new BroadcastChannel('bl_song') : null;
function fmt(t){ const m = Math.floor(t/60), s = Math.floor(t%60); return m + ':' + String(s).padStart(2,'0'); }
function saveState(){ try { localStorage.setItem(KEY, JSON.stringify({ t: song.currentTime || 0, playing: playing, at: Date.now() })); } catch(e){} }
function loadState(){ try { const d = JSON.parse(localStorage.getItem(KEY) || 'null'); return d && typeof d.t === 'number' ? d : null; } catch(e){ return null; } }
function setPlaying(on, broadcast){
  playing = on;
  btn.textContent = on ? '❚❚' : '▶';
  btn.style.animation = on ? 'none' : 'blpulse 2s infinite';
  status.innerHTML = on ? '<span class="blbars"><i></i><i></i><i></i></span> now playing' : (loadState() && loadState().t > 1 ? 'resume at ' + fmt(loadState().t) + ' — Butterflies and Love' : 'tap to play — Butterflies and Love');
  saveState();
  if (broadcast && bc) bc.postMessage({ type:'state', playing:on, t:song.currentTime });
}
function toggleSong(){
  if(playing){ song.pause(); setPlaying(false, true); }
  else { song.play().then(()=>setPlaying(true, true)).catch(()=>{}); }
}
btn.addEventListener('click', toggleSong);
song.addEventListener('ended', ()=>setPlaying(false, true));
setInterval(()=>{ if(playing) saveState(); }, 2000);
if (bc) bc.onmessage = (ev) => {
  const d = ev.data || {};
  if (d.type === 'state' && !playing && typeof d.t === 'number') {
    try { song.currentTime = d.t; } catch(e){}
    saveState(); setPlaying(false, false);
  }
};
window.addEventListener('load', ()=>{
  const urlT = parseFloat(new URLSearchParams(location.search).get('bl_t'));
  const st = loadState();
  const startT = (!isNaN(urlT) && urlT > 1) ? urlT : (st && st.t > 1 ? st.t : 0);
  if (startT > 1) { try { song.currentTime = startT; } catch(e){} }
  setPlaying(false, false);
  if (startT > 1) status.textContent = 'resume at ' + fmt(startT) + ' — Butterflies and Love';
  song.play().then(()=>setPlaying(true, true)).catch(()=>{});
});
window.addEventListener('beforeunload', saveState);
document.querySelectorAll('a[href]').forEach(a => {
  const href = a.getAttribute('href');
  if (!href || href.startsWith('#')) return;
  a.addEventListener('click', e => {
    saveState();
    let url = a.href;
    try {
      const u = new URL(url, location.href);
      if ((u.hostname.endsWith('taur.link') || u.hostname.endsWith('shakaleikaumaka.com')) && song.currentTime > 1) {
        u.searchParams.set('bl_t', song.currentTime.toFixed(1));
        url = u.toString();
      }
    } catch(err){}
    const w = window.open(url, '_blank', 'noopener');
    if (!w) location.href = url;
    e.preventDefault();
  });
});
})();
