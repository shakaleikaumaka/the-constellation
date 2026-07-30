/* 🐢 Terri's Tiny Turtle Cursor — dust poof on every bite (click).
   Lightweight: no libraries, no canvas, respects reduced-motion. */
(function () {
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (window.matchMedia && !window.matchMedia('(pointer: fine)').matches) return; // mice only

  document.addEventListener('mousedown', function (e) {
    for (var i = 0; i < 6; i++) {
      var p = document.createElement('div');
      p.className = 'turtle-poof';
      var angle = Math.random() * Math.PI * 2;
      var dist = 14 + Math.random() * 22;
      p.style.setProperty('--dx', Math.cos(angle) * dist + 'px');
      p.style.setProperty('--dy', Math.sin(angle) * dist - 8 + 'px');
      p.style.left = (e.clientX - 3) + 'px';
      p.style.top = (e.clientY - 3) + 'px';
      document.body.appendChild(p);
      (function (el) { setTimeout(function () { el.remove(); }, 600); })(p);
    }
  }, { passive: true });
})();
