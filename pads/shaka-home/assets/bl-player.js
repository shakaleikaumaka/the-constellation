/* 🦋 bl-player.js v4.5 — one window, two tracks, sing-along everywhere. One line: <script src="https://shaka-home-cbhjr5ziii-ffieyo32.taur.link/assets/bl-player.js"></script>
   Track 1: Butterflies and Love · Track 2: A Planet We Share As One — both recorded with Ethereum Singapore.
   v4.5: perfectionist canon (Shaka, Jul 27 2026) — text column capped with ellipsis so the bar never touches the manifesto paper; sub line drops ≤1100px.
   v4.4/v4.3: desktop haircuts. v4.2: mobile compact + stack canon.
   v4.1: iframe guard (shaka-shell parent owns the music). v4: pop-out jukebox REMOVED; third button is SING-ALONG lyrics.
   v3: same-tab navigation. v1 (single-track) preserved at bl-player-v1.js. */
(function(){
if (document.getElementById('miniplayer')) return;
if (window !== window.top) return; // v4.1: inside the shaka-shell overlay, the PARENT owns the music — no player here
const TRACKS = [
  { title: 'Butterflies and Love', sub: 'demo recorded with Ethereum Singapore for Aya Miyaguchi 🦋',
    src: 'https://shaka-anthem-gzdk4epeah-ffieyo32.taur.link/assets/i-open-sourced-my-whole-universe.mp3',
    chords: 'G–Em–C–D', icon: '🦋',
    lyrics: `<p><strong>Hey Solana</strong><br>We can be your (blockchain)<br>(soy boy) big brother<br>We don't need to fight a war<br>for users and developers<br>We build apps that bridge us all together<br>Competition can be over<br>Because Ethereum<br>Is a positive Sum<br>Built by and for everyone</p>
<p><strong>Hey Bitcoin</strong><br>Lucky you were never called a shitcoin (altcoin)<br>you were the first to inspire<br>Our Ethereum co-creator<br>His magazine wasn't<br>just an ordinary page turner<br>Even though we don't<br>Know your founder<br>Vitalik found inspiration<br>From your ledger</p>
<p><strong>We should only wage war<br>with butterflies and love<br>The infinite garden isn't just a place for fun<br>Decentralized<br>Permission-less<br>and open-sourced<br>Even with the layer one as our shield,<br>and the layer two as our sword<br>All we need to wage in a war<br>Is butterflies and love</strong><br>Because Ethereum is a positive sum<br>Built by and for everyone</p>
<p><strong>Hey Ethereum</strong><br>I still love you most of all<br>You are the world computer<br>Built by all my brothers and sisters<br>Together we don't have to fight a war<br>All we need is butterflies and love<br>To pollinate the infinite-garden<br>Which grows strong and tall<br>And make us all look small<br>In the infinite garden</p>
<p><strong>Hey Aya 🌸</strong><br>Don't let the arrows pointed at ya<br>Ever pierce your lovely heart<br>From the start<br>you were the heart beat<br>Of the ethereum foundation<br>You taught us the power of subtraction<br>and your very first reaction<br>Was that you didn't want a title<br>That's why we have such fertile soil<br>For us all to grow equal<br>In the infinite garden</p>` },
  { title: 'A Planet We Share As One', sub: 'recorded with Ethereum Singapore 🌍',
    src: 'https://shaka-anthem-gzdk4epeah-ffieyo32.taur.link/assets/a-planet-we-share-as-one.mp3',
    chords: 'C–G–D–D', icon: '🌍',
    lyrics: `<p><strong>You know I had a frustration</strong><br>That I come from the nation<br>That dropped an atomic bomb<br><strong>On a planet we share as one</strong></p>
<p><strong>And I have a frustration</strong><br>They also tested those fucking bombs<br>In our ocean<br>And now you see with all the plastic<br>It's choking our reefs, you see<br><strong>Protection of creation<br>Must be a collaboration<br>Of every nation<br>For a planet we share as one</strong></p>
<p><strong>You know I had a frustration</strong><br>That two bordering nations<br>Have to fight for the greed<br>Of one fucking man's manipulations<br>Why does war have to be a typical situation<br>Can't we see a better resolution<br><strong>For a planet we share as one</strong></p>
<p><strong>It doesn't matter if you count up<br>To Web 1, 2 or 3</strong><br>We all can evolve<br>Like we evolve our technology<br>And now we see — like an experiment<br>With a Zuzalu pop-up city<br>We can build and dogfood<br>Our own technology<br>So we can see<br><strong>How we can be free</strong></p>
<p><strong>We can build it up like a layer one</strong><br>The world computer called Ethereum<br><strong>For a planet we share as one 🌍</strong></p>` }
];
const wrap = document.createElement('div');
wrap.innerHTML = `
<div id="miniplayer" style="position:fixed;bottom:14px;right:14px;z-index:99999;display:flex;align-items:center;gap:7px;background:linear-gradient(150deg,rgba(240,180,41,.16),rgba(23,17,38,.92));border:1px solid #f0b429;border-radius:999px;padding:6px 12px 6px 7px;backdrop-filter:blur(8px);box-shadow:0 8px 40px rgba(240,180,41,.25);font-family:'Avenir Next','Segoe UI',system-ui,sans-serif">
  <button id="songbtn" style="width:32px;height:32px;border-radius:50%;border:none;background:#f0b429;color:#241a02;font-size:.85rem;cursor:pointer;animation:blpulse 2s infinite">▶</button>
  <div style="line-height:1.25">
    <div id="songstatus" style="font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;color:#ffd97a">tap to play — ${TRACKS[0].title}</div>
    <div id="songsub" style="font-size:.64rem;color:#b9a8cf">${TRACKS[0].sub}</div>
  </div>
  <button id="trackbtn" title="switch track" style="width:24px;height:24px;border-radius:50%;border:1px solid #f0b429;background:transparent;color:#ffd97a;font-size:.56rem;cursor:pointer;letter-spacing:.05em">1·2</button>
  <button id="lyricsbtn" title="sing along — lyrics for the song playing" style="width:24px;height:24px;border-radius:50%;border:1px solid #2dd4bf;background:transparent;color:#2dd4bf;font-size:.66rem;cursor:pointer">🦋</button>
</div>
<div id="blyrics" style="display:none;position:fixed;bottom:68px;right:14px;z-index:99998;width:min(340px,86vw);max-height:52vh;overflow-y:auto;background:linear-gradient(160deg,rgba(23,17,38,.97),rgba(13,10,20,.97));border:1px solid rgba(45,212,191,.4);border-radius:16px;padding:18px 20px;box-shadow:0 12px 50px rgba(0,0,0,.6);font-family:'Avenir Next','Segoe UI',system-ui,sans-serif">
  <div id="blyricshead" style="font-size:.72rem;letter-spacing:.22em;text-transform:uppercase;color:#2dd4bf;margin-bottom:10px"></div>
  <div id="blyricsbody" style="font-size:.9rem;line-height:1.6;color:#b9a8cf"></div>
</div>
<audio id="thesong" preload="auto"></audio>
<style>@keyframes blpulse{0%,100%{box-shadow:0 0 0 0 rgba(240,180,41,.5)}50%{box-shadow:0 0 0 12px rgba(240,180,41,0)}}@keyframes bleq{0%,100%{transform:scaleY(.4)}50%{transform:scaleY(1)}}.blbars{display:inline-flex;gap:2.5px;align-items:flex-end;height:14px;margin-right:2px}.blbars i{width:3px;background:#f0b429;border-radius:2px;animation:bleq .9s ease-in-out infinite}.blbars i:nth-child(2){animation-delay:.2s}.blbars i:nth-child(3){animation-delay:.4s}#blyricsbody p{margin:0 0 14px}#blyricsbody strong{color:#f3ead8}
/* v4.5 perfectionist canon (Shaka, Jul 27 2026): cap the text column so the bar can NEVER grow wide enough to touch the manifesto paper */
#miniplayer > div{max-width:200px}
#songstatus,#songsub{white-space:nowrap !important;overflow:hidden !important;text-overflow:ellipsis !important;max-width:200px}
@media (max-width:1100px){
  /* narrower windows: drop the sub line entirely, tighter cap */
  #miniplayer > div > div:last-child{display:none !important}
  #miniplayer > div{max-width:160px}
  #songstatus{max-width:160px !important}
}
@media (max-width:640px){
  /* v4.2 mobile canon (Shaka, Jul 27 2026): shrink so jukebox + Devcon ticket sit side by side */
  #miniplayer{bottom:12px !important;right:12px !important;left:auto !important;padding:6px 10px 6px 7px !important;gap:7px !important;border-radius:999px !important}
  #miniplayer > div > div:last-child{display:none !important}
  #songbtn{width:30px !important;height:30px !important;font-size:.8rem !important;flex-shrink:0}
  #songstatus{font-size:.58rem !important;letter-spacing:.05em !important;white-space:nowrap;max-width:106px;overflow:hidden;text-overflow:ellipsis}
  #trackbtn,#lyricsbtn{width:24px !important;height:24px !important;font-size:.56rem !important;flex-shrink:0}
  #blyrics{bottom:82px !important;right:12px !important}
}
@media (max-width:400px){
  /* very narrow phones: ticket floats ABOVE the jukebox (stacked), so the bar gets a little room back */
  #songstatus{max-width:140px}
}
</style>`;
document.body.appendChild(wrap);
const song = document.getElementById('thesong');
const btn = document.getElementById('songbtn');
const status = document.getElementById('songstatus');
const sub = document.getElementById('songsub');
const trackBtn = document.getElementById('trackbtn');
const lyricsBtn = document.getElementById('lyricsbtn');
const lyricsBox = document.getElementById('blyrics');
const lyricsHead = document.getElementById('blyricshead');
const lyricsBody = document.getElementById('blyricsbody');
const KEY = 'bl_song';
let playing = false;
let ti = 0;
let lyricsOpen = false;
const q = new URLSearchParams(location.search);
const bc = ('BroadcastChannel' in window) ? new BroadcastChannel('bl_song') : null;
function fmt(t){ const m = Math.floor(t/60), s = Math.floor(t%60); return m + ':' + String(s).padStart(2,'0'); }
function saveState(){ try { localStorage.setItem(KEY, JSON.stringify({ track: ti, t: song.currentTime || 0, playing: playing, at: Date.now() })); } catch(e){} }
function loadState(){ try { const d = JSON.parse(localStorage.getItem(KEY) || 'null'); return d && typeof d.t === 'number' ? d : null; } catch(e){ return null; } }
function renderLyrics(){
  lyricsHead.textContent = TRACKS[ti].icon + ' ' + TRACKS[ti].title + ' · ' + TRACKS[ti].chords;
  lyricsBody.innerHTML = TRACKS[ti].lyrics;
}
function toggleLyrics(force){
  lyricsOpen = (typeof force === 'boolean') ? force : !lyricsOpen;
  if (lyricsOpen) renderLyrics();
  lyricsBox.style.display = lyricsOpen ? 'block' : 'none';
  lyricsBtn.style.background = lyricsOpen ? '#2dd4bf' : 'transparent';
  lyricsBtn.style.color = lyricsOpen ? '#0d0a14' : '#2dd4bf';
}
lyricsBtn.addEventListener('click', ()=>toggleLyrics());
function setTrack(i, keepTime){
  ti = ((i % TRACKS.length) + TRACKS.length) % TRACKS.length;
  song.src = TRACKS[ti].src;
  sub.textContent = TRACKS[ti].sub;
  trackBtn.textContent = (ti + 1) + '·' + TRACKS.length;
  trackBtn.title = 'switch track — next: ' + TRACKS[(ti + 1) % TRACKS.length].title;
  lyricsBtn.textContent = TRACKS[ti].icon;
  if (lyricsOpen) renderLyrics();
  if (!keepTime) { try { song.currentTime = 0; } catch(e){} }
}
function label(){
  const st = loadState();
  return (st && st.t > 1 && st.track === ti) ? 'resume at ' + fmt(st.t) + ' — ' + TRACKS[ti].title : 'tap to play — ' + TRACKS[ti].title;
}
function setPlaying(on, broadcast){
  playing = on;
  btn.textContent = on ? '❚❚' : '▶';
  btn.style.animation = on ? 'none' : 'blpulse 2s infinite';
  status.innerHTML = on ? '<span class="blbars"><i></i><i></i><i></i></span> now playing — ' + TRACKS[ti].title : label();
  saveState();
  if (broadcast && bc) bc.postMessage({ type:'state', playing:on, t:song.currentTime, track:ti });
}
function toggleSong(){
  if(playing){ song.pause(); setPlaying(false, true); }
  else { song.play().then(()=>setPlaying(true, true)).catch(()=>{}); }
}
btn.addEventListener('click', toggleSong);
trackBtn.addEventListener('click', ()=>{
  const wasPlaying = playing;
  setTrack(ti + 1);
  if (wasPlaying) { song.play().then(()=>setPlaying(true, true)).catch(()=>{}); }
  else setPlaying(false, true);
});
song.addEventListener('ended', ()=>{
  setTrack(ti + 1);
  song.play().then(()=>setPlaying(true, true)).catch(()=>setPlaying(false, true));
});
setInterval(()=>{ if(playing) saveState(); }, 2000);
if (bc) bc.onmessage = (ev) => {
  const d = ev.data || {};
  if (d.type === 'state' && !playing && typeof d.t === 'number') {
    if (typeof d.track === 'number' && d.track !== ti) setTrack(d.track, true);
    try { song.currentTime = d.t; } catch(e){}
    saveState(); setPlaying(false, false);
  }
};
window.addEventListener('load', ()=>{
  const urlT = parseFloat(q.get('bl_t'));
  const urlTrk = parseInt(q.get('bl_trk'), 10);
  const st = loadState();
  const startTrack = (!isNaN(urlTrk) && urlTrk >= 0 && urlTrk < TRACKS.length) ? urlTrk : (st && typeof st.track === 'number' ? st.track : 0);
  setTrack(startTrack, true);
  const startT = (!isNaN(urlT) && urlT > 1) ? urlT : (st && st.t > 1 && st.track === ti ? st.t : 0);
  if (startT > 1) { try { song.currentTime = startT; } catch(e){} }
  setPlaying(false, false);
  song.play().then(()=>setPlaying(true, true)).catch(()=>{});
});
window.addEventListener('beforeunload', saveState);
// v4.2: public API — songbook carousels can play a track directly
window.blPlay = function(i){
  if (typeof i === 'number') setTrack(i);
  song.play().then(()=>setPlaying(true, true)).catch(()=>{});
};
// same-tab navigation — position rides the URL
document.querySelectorAll('a[href]').forEach(a => {
  const href = a.getAttribute('href');
  if (!href || href.startsWith('#')) return;
  a.addEventListener('click', e => {
    if (a.target === '_blank' || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    saveState();
    let url = a.href;
    try {
      const u = new URL(url, location.href);
      if ((u.hostname.endsWith('taur.link') || u.hostname.endsWith('shakaleikaumaka.com')) && song.currentTime > 1) {
        u.searchParams.set('bl_t', song.currentTime.toFixed(1));
        u.searchParams.set('bl_trk', String(ti));
        url = u.toString();
      }
    } catch(err){}
    if (url !== a.href) { e.preventDefault(); location.href = url; }
  });
});
})();
