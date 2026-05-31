(function () {
  'use strict';

  /* === Sidebar toggle === */
  function initSidebar() {
    var btn = document.getElementById('menuToggle');
    var overlay = document.getElementById('sidebarOverlay');
    if (!btn) return;

    var open = function () {
      document.body.classList.add('sidebar-open');
      btn.setAttribute('aria-expanded', 'true');
    };
    var close = function () {
      document.body.classList.remove('sidebar-open');
      btn.setAttribute('aria-expanded', 'false');
    };
    var toggle = function () {
      if (document.body.classList.contains('sidebar-open')) close();
      else open();
    };

    btn.addEventListener('click', function (e) { e.preventDefault(); toggle(); });
    if (overlay) overlay.addEventListener('click', close);

    document.querySelectorAll('.sidenav a').forEach(function (a) {
      a.addEventListener('click', function () {
        if (window.matchMedia('(max-width: 900px)').matches) close();
      });
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close();
    });
  }

  /* === Copy buttons === */
  function makeBtn() {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'copy-btn';
    b.setAttribute('aria-label', '复制内容');
    b.textContent = '复制';
    return b;
  }

  function copyText(text, btn) {
    var done = function () {
      btn.textContent = '已复制';
      btn.classList.add('copied');
      setTimeout(function () { btn.textContent = '复制'; btn.classList.remove('copied'); }, 1500);
    };
    var fail = function () {
      btn.textContent = '复制失败';
      setTimeout(function () { btn.textContent = '复制'; }, 1500);
    };

    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(done, fail);
      return;
    }
    try {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      document.body.removeChild(ta);
      done();
    } catch (e) { fail(); }
  }

  function getBlockText(el) {
    var code = el.querySelector('code');
    return (code ? code.textContent : el.textContent);
  }
  function getQuoteText(el) {
    var clone = el.cloneNode(true);
    var btn = clone.querySelector('.copy-btn');
    if (btn) btn.remove();
    return clone.textContent.trim();
  }

  function initCopy() {
    document.querySelectorAll('article pre').forEach(function (pre) {
      var btn = makeBtn();
      pre.appendChild(btn);
      btn.addEventListener('click', function (e) { e.preventDefault(); copyText(getBlockText(pre), btn); });
    });
    document.querySelectorAll('article blockquote').forEach(function (q) {
      var btn = makeBtn();
      q.appendChild(btn);
      btn.addEventListener('click', function (e) { e.preventDefault(); copyText(getQuoteText(q), btn); });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initSidebar();
    initCopy();
  });
})();
