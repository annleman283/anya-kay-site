/* Anya Kay · сайт */
(function () {
  'use strict';

  /* ---------- настройки ---------- */
  var WA = '48788214369';
  var TG = 'https://t.me/AnyaKayClientBot';
  // Ссылка на Google Таблицу с датами (Файл → Поделиться → Опубликовать в интернете → CSV).
  // Пусто = берутся даты ниже.
  var SHEET_CSV = "";
  var DATES = [{"c": "basic", "a": "2026-11-18", "b": "2026-11-20", "i": "2800", "g": "", "n": "выгодная цена"}, {"c": "basic", "a": "2026-12-07", "b": "2026-12-09", "i": "3000", "g": "2000", "n": ""}, {"c": "vip", "a": "2027-01-11", "b": "2027-01-16", "i": "4500", "g": "3000", "n": ""}];

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var IO = 'IntersectionObserver' in window;
  var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROOT = (($('script[src*="app.js"]') || {}).getAttribute ? $('script[src*="app.js"]').getAttribute('src') : '/app.js').replace(/app\.js.*$/, '');
  function url(p) { return ROOT + p; }

  /* ---------- стрелка назад ---------- */
  $$('[data-hback]').forEach(function (b) {
    b.addEventListener('click', function (e) {
      var same = document.referrer && document.referrer.indexOf(location.host) > -1;
      if (same && history.length > 1) { e.preventDefault(); history.back(); }
    });
  });

  /* ---------- шапка и меню ---------- */
  var hdr = $('.hdr');
  if (hdr && hdr.dataset.clear !== undefined) {
    var onScroll = function () { hdr.classList.toggle('clear', window.scrollY < 60); };
    window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  }
  var mnu = $('#mnu');
  $$('[data-menu]').forEach(function (b) { b.addEventListener('click', function () { mnu.classList.add('on'); document.body.style.overflow = 'hidden'; }); });
  $$('[data-menu-x], #mnu nav a').forEach(function (b) { b.addEventListener('click', function () { mnu.classList.remove('on'); document.body.style.overflow = ''; }); });

  /* ---------- появление, счётчики, видео ---------- */
  function counter(el) {
    function nf(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '\u00a0'); }
    var to = +el.dataset.to, suf = el.dataset.suf || '', t0 = null;
    if (calm) { el.textContent = nf(to) + suf; return; }
    function f(t) { if (!t0) t0 = t; var p = Math.min(1, (t - t0) / 1600); el.textContent = nf(Math.round(to * (1 - Math.pow(1 - p, 3)))) + suf; if (p < 1) requestAnimationFrame(f); }
    requestAnimationFrame(f);
  }
  function watch() {
    var rv = $$('.reveal:not(.in-view)'), cn = $$('[data-to]:not([data-done])');
    if (!IO || calm) { rv.forEach(function (e) { e.classList.add('in-view'); }); cn.forEach(function (e) { e.textContent = String(e.dataset.to).replace(/\B(?=(\d{3})+(?!\d))/g, '\u00a0') + (e.dataset.suf || ''); }); return; }
    var obs = new IntersectionObserver(function (en) {
      en.forEach(function (x) {
        if (!x.isIntersecting) return;
        if (x.target.dataset.to) { x.target.dataset.done = 1; counter(x.target); } else x.target.classList.add('in-view');
        obs.unobserve(x.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    rv.concat(cn).forEach(function (e) { obs.observe(e); });
  }
  function autoVideos() {
    var vids = $$('video[data-auto]:not([data-w])');
    vids.forEach(function (v) { v.dataset.w = 1; });
    if (!IO) { vids.forEach(function (v) { v.src = v.dataset.src; }); return; }
    var vo = new IntersectionObserver(function (en) {
      en.forEach(function (x) {
        var v = x.target;
        if (x.isIntersecting) { if (!v.getAttribute('src')) v.src = v.dataset.src; if (!calm) { var p = v.play(); if (p && p.catch) p.catch(function () {}); } }
        else v.pause();
      });
    }, { threshold: 0.01, rootMargin: '400px 0px' });
    vids.forEach(function (v) { vo.observe(v); });
  }

  /* ---------- портфолио и ленты ---------- */
  // [файл, подпись, лента]; v: = видео
  var PH = [
    ['lash-1.jpg', 'Наращивание ресниц, работа Anya Kay', 'lash'],
    ['v:lash-1', 'Наращивание ресниц, видео', 'lash'],
    ['lash-2.jpg', 'Эффект наращивания ресниц', 'lash'],
    ['v:lash-2', 'Наращивание ресниц, видео', 'lash'],
    ['lash-3.jpg', 'Пушистый объём, работа Anya Kay', 'lash'],
    ['v:lash-3', 'Наращивание ресниц, видео', 'lash'],
    ['uchenica-basic-1.jpg', 'Работа ученицы после BASIC', 'uch'],
    ['otzyv-karina.jpg', 'Ученица Карина с сертификатом', 'uch'],
    ['uchenica-basic-2.jpg', 'Работа ученицы после BASIC', 'uch'],
    ['uchenica-basic-3.jpg', 'Работа ученицы после BASIC', 'uch'],
    ['povyshenie-1.jpg', 'Работа после повышения квалификации', 'uch'],
    ['uchenica-basic-4.jpg', 'Работа ученицы после BASIC', 'uch'],
    ['v:povyshenie', 'Работа после повышения квалификации, видео', 'uch'],
    ['povyshenie-2.jpg', 'Работа после повышения квалификации', 'uch'],
    ['sertifikat-1.jpg', 'Ученица Anya Kay с сертификатом', 'cert'],
    ['sertifikat-2.jpg', 'Ученица Anya Kay с сертификатом', 'cert'],
    ['sertifikat-3.jpg', 'Ученица Anya Kay с сертификатом', 'cert'],
    ['sertifikat-4.jpg', 'Ученица Anya Kay с сертификатом', 'cert'],
    ['sertifikat-5.jpg', 'Ученица Anya Kay с сертификатом', 'cert'],
    ['sertifikat-6.jpg', 'Ученица Anya Kay с сертификатом', 'cert'],
    ['sertifikat-7.jpg', 'Ученица Anya Kay с сертификатом', 'cert'],
    ['sertifikat-8.jpg', 'Ученица Anya Kay с сертификатом', 'cert'],
    ['sertifikat-9.jpg', 'Ученица Anya Kay с сертификатом', 'cert'],
    ['sertifikat-10.jpg', 'Ученица Anya Kay с сертификатом', 'cert'],
    ['posobie-1.jpg', 'Обложка пособия', 'posobie'],
    ['posobie-2.jpg', 'Содержание пособия', 'posobie'],
    ['posobie-3.jpg', 'Страница пособия: рабочее место', 'posobie'],
    ['posobie-4.jpg', 'Страница пособия: работа с клеем', 'posobie'],
    ['posobie-5.jpg', 'Страница пособия: наращивание на анагены', 'posobie'],
    ['posobie-6.jpg', 'Страница пособия: ожог слизистой', 'posobie'],
    ['teoriya-1.jpg', 'Anya Kay Basic Lash в Telegram', 'teoriya'],
    ['teoriya-2.jpg', 'Урок в Telegram', 'teoriya'],
    ['teoriya-3.jpg', 'Тест после урока', 'teoriya'],
    ['teoriya-4.jpg', 'Видеоурок', 'teoriya']
  ];
  var lb = $('#lbx'), lbList = [], lbI = 0;
  function lbShow(i) {
    lbI = (i + lbList.length) % lbList.length;
    var p = lbList[lbI], box = $('.m', lb);
    if (p[0].indexOf('v:') === 0) box.innerHTML = '<video src="' + url('video/' + p[0].slice(2) + '.mp4') + '" autoplay muted loop playsinline controls></video>';
    else box.innerHTML = '<img src="' + url('img/' + p[0]) + '" alt="' + esc(p[1]) + '">';
    $('.c', lb).textContent = lbList.length > 1 ? (lbI + 1) + ' / ' + lbList.length : '';
    $$('.nv', lb).forEach(function (b) { b.hidden = lbList.length < 2; });
  }
  function lbOpen(list, i) { lbList = list; lbShow(i); lb.classList.add('on'); }
  function lbClose() { lb.classList.remove('on'); $('.m', lb).innerHTML = ''; }
  if (lb) {
    $('.x', lb).addEventListener('click', lbClose);
    $('.pv', lb).addEventListener('click', function () { lbShow(lbI - 1); });
    $('.nx', lb).addEventListener('click', function () { lbShow(lbI + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) lbClose(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('on')) return;
      if (e.key === 'Escape') lbClose();
      if (e.key === 'ArrowLeft') lbShow(lbI - 1);
      if (e.key === 'ArrowRight') lbShow(lbI + 1);
    });
    var sx = 0;
    lb.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) { var dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50 && lbList.length > 1) lbShow(lbI + (dx < 0 ? 1 : -1)); });
  }
  $$('[data-shot]').forEach(function (b) { b.addEventListener('click', function () { lbOpen([[b.dataset.shot, b.dataset.alt || '']], 0); }); });
  $$('[data-slider]').forEach(function (sl) {
    var track = $('.sl-t', sl), cnt = $('.sl-c', sl);
    var cats = sl.dataset.slider.split(',');
    var list = PH.filter(function (p) { return cats.indexOf(p[2]) > -1; });
    track.innerHTML = list.map(function (p, i) {
      if (p[0].indexOf('v:') === 0) {
        var n = p[0].slice(2);
        return '<div class="vs"><video data-auto data-src="' + url('video/' + n + '.mp4') + '" poster="' + url('video/' + n + '.jpg') + '" muted loop playsinline preload="none" aria-label="' + esc(p[1]) + '"></video></div>';
      }
      return '<button type="button" data-i="' + i + '" aria-label="' + esc(p[1]) + '"><img src="' + url('img/' + p[0]) + '" alt="' + esc(p[1]) + '" loading="' + (i < 2 ? 'eager' : 'lazy') + '"></button>';
    }).join('');
    $$('button', track).forEach(function (b) { b.addEventListener('click', function () { lbOpen(list, +b.dataset.i); }); });
    function step() { var b = track.firstElementChild; return b ? b.getBoundingClientRect().width + 10 : 300; }
    function upd() {
      if (!cnt) return;
      var i = Math.round(track.scrollLeft / step());
      if (track.scrollLeft + track.clientWidth >= track.scrollWidth - 4) i = list.length - 1;
      cnt.innerHTML = (Math.min(i, list.length - 1) + 1) + ' <span>/ ' + list.length + '</span>';
    }
    track.addEventListener('scroll', function () { window.requestAnimationFrame(upd); }, { passive: true });
    var p = $('.sl-p', sl), n = $('.sl-x', sl);
    if (p) p.addEventListener('click', function () { track.scrollBy({ left: -step(), behavior: 'smooth' }); });
    if (n) n.addEventListener('click', function () { track.scrollBy({ left: step(), behavior: 'smooth' }); });
    upd();
  });

  /* ---------- ближайшие курсы ---------- */
  var MON = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'];
  var MSH = ['янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек'];
  var CNAME = { basic: 'BASIC · 3 дня', vip: 'VIP «под ключ» · 6 дней' };
  function pd(s) { s = String(s || '').trim(); var m = s.match(/^(\d{4})-(\d{1,2})-(\d{1,2})$/) || null; if (m) return new Date(+m[1], +m[2] - 1, +m[3]); m = s.match(/^(\d{1,2})[.\/](\d{1,2})[.\/](\d{4})$/); return m ? new Date(+m[3], +m[2] - 1, +m[1]) : null; }
  function iso(d) { return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }
  function range(a, b) {
    if (!b || +a === +b) return a.getDate() + ' ' + MON[a.getMonth()];
    if (a.getMonth() === b.getMonth()) return a.getDate() + '–' + b.getDate() + ' ' + MON[a.getMonth()];
    return a.getDate() + ' ' + MON[a.getMonth()] + ' – ' + b.getDate() + ' ' + MON[b.getMonth()];
  }
  function zl(n) { n = String(n || '').replace(/[^\d]/g, ''); return n ? n.replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + ' zł' : ''; }
  function upcoming(course) {
    var t = new Date(); t.setHours(0, 0, 0, 0);
    return DATES.map(function (d) { return { c: d.c, a: pd(d.a), b: pd(d.b) || pd(d.a), i: d.i, g: d.g, n: d.n || '' }; })
      .filter(function (d) { return d.a && d.b >= t && (!course || d.c === course); })
      .sort(function (x, y) { return x.a - y.a; });
  }
  function card(d, showPrice) {
    var price = showPrice ? '<div class="pr">Индивидуально: ' + zl(d.i) + (d.g ? ' · в группе: ' + zl(d.g) + ' с человека' : '') + '</div>' : '';
    var fmt = d.g ? 'Индивидуально или в группе до 2 человек' : 'Индивидуально';
    return '<article class="dt gd reveal in-view"><div class="when"><b>' + d.a.getDate() + (+d.a !== +d.b ? '–' + d.b.getDate() : '') + '</b><span>' + MSH[d.b.getMonth()] + ' ' + d.b.getFullYear() + '</span></div>' +
      '<h3>' + esc(CNAME[d.c] || d.c) + (d.n ? ' <span class="tag">' + esc(d.n) + '</span>' : '') + '</h3><div class="meta">' + range(d.a, d.b) + (showPrice ? ' · ' + fmt : '') + '</div>' + price +
      '<a class="btn glass go" href="' + url('zapis/?w=' + d.c + '&d=' + iso(d.a)) + '">Записаться на эту дату ↗</a></article>';
  }
  function renderDates() {
    $$('[data-dates]').forEach(function (box) {
      var list = upcoming(box.dataset.dates || ''), lim = +box.dataset.limit || 99;
      box.innerHTML = list.length ? list.slice(0, lim).map(function (d) { return card(d, box.dataset.price !== undefined); }).join('')
        : '<div class="dates-empty gd">Новые даты скоро появятся. Напишите, и я сообщу первой.</div>';
    });
  }
  function parseCSV(t) {
    var rows = [], row = [], f = '', q = false;
    for (var i = 0; i < t.length; i++) {
      var ch = t[i];
      if (q) { if (ch === '"') { if (t[i + 1] === '"') { f += '"'; i++; } else q = false; } else f += ch; }
      else if (ch === '"') q = true; else if (ch === ',') { row.push(f); f = ''; }
      else if (ch === '\n' || ch === '\r') { if (ch === '\r' && t[i + 1] === '\n') i++; row.push(f); rows.push(row); row = []; f = ''; }
      else f += ch;
    }
    if (f || row.length) { row.push(f); rows.push(row); }
    return rows;
  }
  function fromSheet(t) {
    var r = parseCSV(t).slice(1), out = [];
    r.forEach(function (x) {
      var c = (x[0] || '').toLowerCase();
      var key = /vip|вип/.test(c) ? 'vip' : /basic|базов|бейсик/.test(c) ? 'basic' : '';
      if (!key || !pd(x[1])) return;
      out.push({ c: key, a: x[1], b: x[2] || x[1], i: x[3], g: x[4], n: (x[5] || '').trim() });
    });
    return out;
  }
  renderDates();
  if (SHEET_CSV.indexOf('http') === 0 && window.fetch) {
    fetch(SHEET_CSV, { cache: 'no-store' }).then(function (r) { return r.ok ? r.text() : Promise.reject(); }).then(function (t) {
      var d = fromSheet(t); if (d.length) { DATES = d; renderDates(); if (app && st.kind === 'obuchenie') render(); }
    }).catch(function () {});
  }

  /* ---------- форма записи ---------- */
  var app = $('#fapp');
  var KIND = { lashes: 'Запись на наращивание', obuchenie: 'Обучение', materialy: 'Онлайн-продукты', vopros: 'Вопрос' };
  var OPTS = {
    lashes: [['1D–4D', 'Классика и объёмы до 4D', '200 zł', 'lashes'], ['5D', 'Самый пышный объём', '230 zł', 'lashes'], ['Подберём вместе', 'Посоветую эффект по форме глаз', '', 'lashes']],
    obuchenie: [['BASIC', 'С нуля · 3 дня · индивидуально или вдвоём', 'от 2 000 zł', 'basic'], ['VIP «мастер под ключ»', 'С нуля · 6 дней · индивидуально или вдвоём', 'от 3 000 zł', 'vip'], ['Повышение квалификации', 'Для мастеров · программа после разбора работ', '1 000 zł / день', 'advanced'], ['Онлайн-консультация', '2 часа · разбор работ и вопросов', '500 zł', 'consultation']],
    materialy: [['Базовое пособие', '51 страница · редактируется в Canva', '200 zł', 'manual'], ['Теория BASIC в Telegram', '16 уроков, тесты, финальная проверка', '500 zł', 'theory']]
  };
  var W2K = { lashes: 'lashes', basic: 'obuchenie', vip: 'obuchenie', advanced: 'obuchenie', consultation: 'obuchenie', manual: 'materialy', theory: 'materialy' };
  var st = {};
  function prog(n, of) { var h = '<div class="prog">'; for (var i = 1; i <= of; i++) h += '<span' + (i <= n ? ' class="on"' : '') + '></span>'; return h + '</div>'; }
  function opt(i, t, sub, p, data) { return '<button type="button" class="opt" data-v="' + esc(data) + '"><span class="n">' + ('0' + i).slice(-2) + '</span><span class="t">' + t + (sub ? '<small>' + sub + '</small>' : '') + '</span>' + (p ? '<span class="p">' + p + '</span>' : '') + '<span class="arr">↗</span></button>'; }
  function err(t) { var e = $('#f-err'); if (e) e.textContent = t; }
  function yn(id, key, vals) { return '<div class="yn" id="' + id + '">' + vals.map(function (v) { return '<button type="button" aria-pressed="' + (st.d[key] === v) + '">' + v + '</button>'; }).join('') + '</div>'; }
  function bindYn(id, key) { $$('#' + id + ' button').forEach(function (b, _, all) { b.addEventListener('click', function () { all.forEach(function (o) { o.setAttribute('aria-pressed', 'false'); }); b.setAttribute('aria-pressed', 'true'); st.d[key] = b.textContent; }); }); }
  function rows() {
    var d = st.d, r = [];
    [['Выбор', d.wybor], ['Дата', d.data], ['Формат', d.format], ['Изгиб L / M', d.izgib], ['Снятие другого мастера', d.snyatie], ['Опыт', d.opyt], [st.kind === 'lashes' ? 'Удобные дни и время' : 'Когда удобно', d.kogda]]
      .forEach(function (x) { if (x[1]) r.push(x); });
    return r;
  }
  function chipsSum() { var r = rows(); return r.length ? '<div class="sum">' + r.map(function (x) { return '<span><b>' + x[0] + ':</b> ' + esc(x[1]) + '</span>'; }).join('') + '</div>' : ''; }
  function scrollTop() { var y = app.getBoundingClientRect().top + window.scrollY - 90; if (window.scrollY > y + 10) window.scrollTo({ top: y, behavior: calm ? 'auto' : 'smooth' }); }
  // шаги: 0 выбор вида; 1 выбор варианта; 2 дата (курсы); 3 формат (курсы); 4 детали; 9 контакты
  function next() {
    var k = st.kind, w = st.w;
    if (st.step === 1 && k === 'obuchenie' && (w === 'basic' || w === 'vip')) st.step = 2;
    else if (st.step === 2) st.step = st.date && st.date.g ? 3 : 4;
    else if (st.step === 1 && k === 'lashes') st.step = 4;
    else if (st.step === 1 && k === 'obuchenie') st.step = 4;
    else if (st.step === 3) st.step = 4;
    else st.step = 9;
    if (st.step === 4 && k === 'materialy') st.step = 9;
    render(); scrollTop();
  }
  function back() { st.hist.pop(); var s = st.hist.pop(); if (s === undefined) { st = {}; } else st.step = s; render(); }
  function render() {
    if (!app) return;
    var k = st.kind, h;
    if (!k) {
      h = prog(1, 4) + '<div class="q">Что вас интересует?</div><div class="h">Пара коротких шагов. В конце сообщение откроется в WhatsApp или Telegram, останется нажать «Отправить».</div>' +
        opt(1, 'Наращивание ресниц', 'Krucza 16/22 · 90 минут', 'от 200 zł', 'lashes') + opt(2, 'Обучение', 'BASIC, VIP, повышение, консультация', '', 'obuchenie') +
        opt(3, 'Онлайн-продукты', 'Пособие и теория BASIC', 'от 200 zł', 'materialy') + opt(4, 'Задать вопрос', 'Отвечу лично', '', 'vopros');
      app.innerHTML = h;
      $$('.opt', app).forEach(function (b) { b.addEventListener('click', function () { st = { kind: b.dataset.v, step: b.dataset.v === 'vopros' ? 9 : 1, d: {}, hist: [0] }; render(); scrollTop(); }); });
      return;
    }
    if (st.hist[st.hist.length - 1] !== st.step) st.hist.push(st.step);
    if (st.step === 1) {
      h = prog(2, 4) + '<div class="q">' + (k === 'lashes' ? 'Какой объём?' : k === 'obuchenie' ? 'Какой формат обучения?' : 'Что именно?') + '</div><div class="h">' + KIND[k] + '</div>';
      OPTS[k].forEach(function (o, i) { h += opt(i + 1, o[0], o[1], o[2], i); });
      h += '<button type="button" class="back" data-back>← Назад</button>';
      app.innerHTML = h;
      $$('.opt', app).forEach(function (b) { b.addEventListener('click', function () { var o = OPTS[k][+b.dataset.v]; st.d.wybor = o[0]; st.w = o[3]; next(); }); });
    } else if (st.step === 2) {
      var list = upcoming(st.w);
      h = prog(2, 4) + chipsSum() + '<div class="q">Какая дата?</div><div class="h">Ближайшие даты курса.</div>';
      list.forEach(function (d, i) { h += opt(i + 1, range(d.a, d.b), (d.g ? 'индивидуально или вдвоём' : 'индивидуально') + (d.n ? ' · ' + esc(d.n) : ''), zl(d.i), i); });
      h += opt(list.length + 1, 'Другая дата', 'Подберём вместе', '', 'other') + '<button type="button" class="back" data-back>← Назад</button>';
      app.innerHTML = h;
      $$('.opt', app).forEach(function (b) {
        b.addEventListener('click', function () {
          if (b.dataset.v === 'other') { st.date = null; st.d.data = 'другая дата'; st.d.format = ''; }
          else { st.date = list[+b.dataset.v]; st.d.data = range(st.date.a, st.date.b); st.d.format = st.date.g ? '' : 'индивидуально, ' + zl(st.date.i); }
          next();
        });
      });
    } else if (st.step === 3) {
      var d = st.date;
      h = prog(3, 4) + chipsSum() + '<div class="q">Индивидуально или вдвоём?</div><div class="h">В группе максимум 2 человека.</div>' +
        opt(1, 'Индивидуально', 'Только вы и я', zl(d.i), 'i') + opt(2, 'В группе до 2 человек', 'Цена с человека', zl(d.g), 'g') + '<button type="button" class="back" data-back>← Назад</button>';
      app.innerHTML = h;
      $$('.opt', app).forEach(function (b) { b.addEventListener('click', function () { st.d.format = b.dataset.v === 'i' ? 'индивидуально, ' + zl(d.i) : 'в группе, ' + zl(d.g) + ' с человека'; next(); }); });
    } else if (st.step === 4) {
      h = prog(3, 4) + chipsSum();
      if (k === 'lashes') h += '<div class="q">Пара деталей</div><div class="fld"><span class="lb">Изгиб L / M (+20 zł)?</span>' + yn('f-iz', 'izgib', ['Нет', 'Да', 'Не знаю']) + '</div><div class="fld"><span class="lb">Сейчас есть наращенные ресницы другого мастера?</span>' + yn('f-sn', 'snyatie', ['Нет', 'Да, снять (+30 zł)']) + '</div><div class="fld"><label for="f-kogda">Удобные дни и время</label><input id="f-kogda" placeholder="например: будни после 17:00" value="' + esc(st.d.kogda || '') + '"></div>';
      else h += '<div class="q">Пара деталей</div><div class="fld"><span class="lb">Ваш опыт</span>' + yn('f-op', 'opyt', ['С нуля', 'Уже работаю мастером']) + '</div>' + (st.date === undefined || st.date === null ? '<div class="fld"><label for="f-kogda">Когда хотите учиться?</label><input id="f-kogda" placeholder="месяц или даты" value="' + esc(st.d.kogda || '') + '"></div>' : '');
      h += '<button type="button" class="next" data-next>Дальше →</button><button type="button" class="back" data-back>← Назад</button>';
      app.innerHTML = h;
      bindYn('f-iz', 'izgib'); bindYn('f-sn', 'snyatie'); bindYn('f-op', 'opyt');
      $('[data-next]', app).addEventListener('click', function () { var kd = $('#f-kogda'); if (kd) st.d.kogda = kd.value.trim(); next(); });
    } else {
      h = prog(4, 4) + chipsSum() + '<div class="q">Как с вами связаться?</div>' +
        '<div class="fld"><label for="f-name">Имя</label><input id="f-name" autocomplete="given-name" value="' + esc(st.d.imya || '') + '"></div>' +
        '<div class="fld"><label for="f-tel">Телефон или ник в Telegram</label><input id="f-tel" autocomplete="tel" value="' + esc(st.d.tel || '') + '"></div>' +
        '<div class="fld"><label for="f-msg">' + (k === 'vopros' ? 'Ваш вопрос' : 'Комментарий (по желанию)') + '</label><textarea id="f-msg">' + esc(st.d.msg || '') + '</textarea></div>' +
        '<label class="cons"><input type="checkbox" id="f-ok"><span>Согласна, чтобы мои данные использовались для ответа на заявку. <a href="' + url('politika-konfidencialnosti/') + '" target="_blank">Политика конфиденциальности</a></span></label>' +
        (k === 'obuchenie' && (st.w === 'basic' || st.w === 'vip') ? '<label class="cons"><input type="checkbox" id="f-reg"><span>Ознакомилась с <a href="' + url('reglament-obucheniya/') + '" target="_blank">регламентом обучения</a></span></label>' : '') +
        '<button type="button" class="next" data-send>Подготовить сообщение</button><div class="f-err" id="f-err"></div><button type="button" class="back" data-back>← Назад</button>';
      app.innerHTML = h;
      $('[data-send]', app).addEventListener('click', send);
    }
    var bk = $('[data-back]', app); if (bk) bk.addEventListener('click', back);
  }
  function send() {
    var d = st.d;
    d.imya = $('#f-name').value.trim(); d.tel = $('#f-tel').value.trim(); d.msg = $('#f-msg').value.trim();
    if (!d.imya) return err('Напишите, как вас зовут.');
    if (d.tel.replace(/[^0-9a-zA-Z_]/g, '').length < 4) return err('Оставьте телефон или ник в Telegram.');
    if (st.kind === 'vopros' && !d.msg) return err('Напишите вопрос.');
    if ($('#f-reg') && !$('#f-reg').checked) return err('Отметьте, что ознакомились с регламентом обучения.');
    if (!$('#f-ok').checked) return err('Отметьте согласие, чтобы я могла ответить.');
    var lines = ['Здравствуйте, Аня! Заявка с сайта anyakay.pl', KIND[st.kind]];
    rows().forEach(function (x) { lines.push(x[0] + ': ' + x[1]); });
    lines.push('Имя: ' + d.imya, 'Контакт: ' + d.tel);
    if (d.msg) lines.push((st.kind === 'vopros' ? 'Вопрос: ' : 'Комментарий: ') + d.msg);
    var text = lines.join('\n');
    var wa = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(text);
    var tg = TG + (st.w ? '?start=' + st.w : '');
    app.innerHTML = prog(4, 4) + '<div class="q">Спасибо, ' + esc(d.imya) + '!</div><div class="h">Сообщение готово. Выберите мессенджер и нажмите «Отправить».</div>' +
      '<a class="wa" href="' + wa + '" target="_blank" rel="noopener">' + ICON.wa + 'Отправить в WhatsApp</a>' +
      '<a class="tg" href="' + tg + '" target="_blank" rel="noopener" id="f-tg">' + ICON.tg + 'Скопировать и открыть Telegram</a>' +
      '<div class="sum-all">' + esc(text) + '</div><p class="h" style="margin-top:12px">В Telegram текст скопируется сам, вставьте его в чат.</p>' +
      '<button type="button" class="back" id="f-new">Новая заявка</button>';
    $('#f-tg').addEventListener('click', function () { try { navigator.clipboard.writeText(text).catch(function () {}); } catch (e) {} });
    $('#f-new').addEventListener('click', function () { st = {}; render(); });
    scrollTop();
  }
  var ICON = {"wa": "<svg viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path d=\"M12 2a9.8 9.8 0 0 0-8.4 14.9L2 22l5.2-1.6A10 10 0 1 0 12 2Zm0 18.2a8.1 8.1 0 0 1-4.1-1.1l-.3-.2-3.1 1 1-3-.2-.3a8.2 8.2 0 1 1 6.7 3.6Zm4.5-6.1c-.2-.1-1.5-.7-1.8-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.6.1a6.7 6.7 0 0 1-2-1.2 7.6 7.6 0 0 1-1.4-1.7c-.1-.3 0-.4.1-.5l.4-.5.3-.5c.1-.2 0-.4 0-.5l-.8-1.9c-.2-.5-.5-.5-.7-.5H8c-.2 0-.5.1-.7.3-.3.3-1 1-1 2.5s1 2.9 1.2 3.1c.1.2 2.1 3.2 5.2 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.2-.2-.5-.3Z\"/></svg>", "tg": "<svg viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path d=\"M21.8 3.4 18.6 19c-.2 1.1-.9 1.4-1.8.9l-4.9-3.6-2.4 2.3c-.3.3-.5.5-1 .5l.4-5 9-8.1c.4-.4-.1-.6-.6-.2L6.2 12.8 1.4 11.3c-1-.3-1-1 .2-1.5L20.3 2.6c.9-.3 1.7.2 1.5.8Z\"/></svg>"};
  if (app) {
    var q = new URLSearchParams(location.search), w = q.get('w'), dd = q.get('d'), kk = q.get('k');
    if (w && W2K[w]) {
      var k = W2K[w], o = OPTS[k].filter(function (x) { return x[3] === w; })[0];
      st = { kind: k, d: {}, hist: [0, 1], w: w, step: 1 };
      if (o && k !== 'lashes') { st.d.wybor = o[0]; next(); }
      if (dd && st.step === 2) {
        var m = upcoming(w).filter(function (x) { return iso(x.a) === dd; })[0];
        if (m) { st.hist.push(2); st.date = m; st.d.data = range(m.a, m.b); st.d.format = m.g ? '' : 'индивидуально, ' + zl(m.i); next(); }
      }
      if (k === 'lashes') render();
    } else if (kk && KIND[kk]) { st = { kind: kk, step: kk === 'vopros' ? 9 : 1, d: {}, hist: [0] }; render(); }
    else render();
    window.scrollTo(0, 0);
  }

  /* ---------- помощник «Есть вопрос?» ---------- */
  var TOPICS = [['lashes', 'Наращивание'], ['obuchenie', 'Обучение'], ['materialy', 'Онлайн-продукты'], ['kontakt', 'Запись и контакты']];
  var FAQ = [{"t": "lashes", "q": "Сколько стоит наращивание ресниц?", "k": ["стоит", "цена", "цены", "прайс", "стоимость", "наращивание"], "a": "Наращивание 1D–4D стоит 200 zł, 5D 230 zł. Изгибы L / M +20 zł. Снятие ресниц другого мастера с последующим наращиванием +30 zł. С 1 декабря 2026 цены на наращивание повышаются на 20 zł: 1D–4D будет 220 zł, 5D 250 zł. Запишитесь в ноябре по текущей цене.", "go": "lashes"}, {"t": "lashes", "q": "Цены повысятся?", "k": ["повыш", "декабр", "подорож", "дороже"], "a": "С 1 декабря 2026 цены на наращивание повышаются на 20 zł: 1D–4D будет 220 zł, 5D 250 zł. Запишитесь в ноябре по текущей цене.", "go": "lashes"}, {"t": "lashes", "q": "Сколько длится процедура?", "k": ["длится", "по времени", "часа", "долго"], "a": "Само наращивание около 90 минут, вместе со снятием до 2 часов.", "go": "lashes"}, {"t": "lashes", "q": "Сколько держатся ресницы?", "k": ["держатся", "носка", "носятся", "недел"], "a": "Носка 3–5 недель. Техника рассчитана на комфортное и аккуратное отрастание.", "go": "lashes"}, {"t": "lashes", "q": "Делаете коррекцию?", "k": ["коррекц"], "a": "Коррекции не делаю, только полное перенаращивание. Так результат каждый раз свежий и аккуратный.", "go": "lashes"}, {"t": "lashes", "q": "Как выбрать эффект?", "k": ["эффект", "выбрать", "подобрать", "объём", "объем"], "a": "Эффект подбирается индивидуально: по форме глаз, состоянию ваших ресниц и тому, какой образ вам ближе. Можно прийти без идеи, подберём вместе.", "go": "lashes"}, {"t": "lashes", "q": "Снимаете ресницы другого мастера?", "k": ["сним", "снятие", "другого мастера"], "a": "Да. Снятие ресниц другого мастера с последующим наращиванием +30 zł. Отметьте это в заявке, чтобы я заложила время.", "go": "lashes"}, {"t": "lashes", "q": "Что такое изгибы L / M?", "k": ["изгиб", " l ", " m ", "l/m", "l / m"], "a": "Это изгибы с прямым основанием и подъёмом на кончике. Они раскрывают взгляд, особенно при прямых или опущенных ресницах. Стоят +20 zł к наращиванию.", "go": "lashes"}, {"t": "obuchenie", "q": "Ближайшие даты курсов?", "k": ["дата", "даты", "когда", "ближайш", "поток", "старт"], "a": "@dates", "go": "basic"}, {"t": "obuchenie", "q": "Сколько стоит обучение?", "k": ["стоит обучение", "цена курса", "стоимость курса", "сколько курс", "цена обучения"], "a": "BASIC: 3000 zł индивидуально или 2000 zł с человека в мини-группе. VIP «мастер под ключ»: 4500 zł индивидуально или 3000 zł с человека в группе. Повышение квалификации 1000 zł за день, онлайн-консультация 500 zł.", "go": "any"}, {"t": "obuchenie", "q": "Что будет после курса?", "k": ["поддержк", "после курса", "после обучения", "на связи", "помощь"], "a": "Я всегда на связи. Не знаете, что нарастить конкретной клиентке, или что-то не получается в работе? Пишете мне, и я объясню, как сделать правильно. Вы не остаётесь одна: я рядом и поддержу даже в трудную минуту.", "go": "basic"}, {"t": "obuchenie", "q": "Чем VIP отличается от BASIC?", "k": ["vip", "вип", "отличается", "разница"], "a": "VIP включает всё из BASIC и в два раза больше практики: 6 дней и 6 моделей вместо 3, отработку L- и M-изгибов, 2 трендовых эффекта на выбор, стартовый набор материалов и кубок VIP-мастера.", "go": "vip"}, {"t": "obuchenie", "q": "Индивидуально или в группе: в чём разница?", "k": ["групп", "индивидуально", "вдвоём", "вдвоем"], "a": "Программа одна и та же. Индивидуально всё время только ваше, и темп подстраивается под вас. В мини-группе максимум 2 человека, поэтому внимания всё равно много, а цена ниже: BASIC 2000 zł вместо 3000 zł, VIP 3000 zł вместо 4500 zł с человека.", "go": "basic"}, {"t": "obuchenie", "q": "Нужна ли предоплата?", "k": ["предоплат", "перенос", "отмен", "вернуть", "бронь"], "a": "Да, дата бронируется после предоплаты 500 zł. Отменить или перенести запись можно не позже чем за 3 недели до начала, позже предоплата не возвращается. Перенести дату можно один раз, при втором переносе предоплата сгорает.", "go": "basic"}, {"t": "obuchenie", "q": "Выдаёте сертификат?", "k": ["сертификат", "диплом"], "a": "Да, после обучения вы получаете именной сертификат с печатью.", "go": "basic"}, {"t": "obuchenie", "q": "Сколько можно зарабатывать после курса?", "k": ["зарабат", "заработ", "доход", "окупит"], "a": "Зависит от вас, но вот пример: ученица Света за первые 2,5 недели после обучения обслужила 9 клиенток и заработала 800 zł, параллельно работая на заводе. Её модели возвращаются и становятся постоянными клиентками.", "go": "basic"}, {"t": "obuchenie", "q": "Поможете найти первых клиенток?", "k": ["клиентк", "первых", "найти клиент", "продвиж", "контент"], "a": "В BASIC входит бонусный курс по обработке контента и ретуши фото: как снимать работы и оформлять их так, чтобы к вам приходили клиентки. А ещё модели с курса часто становятся первыми постоянными клиентками.", "go": "basic"}, {"t": "obuchenie", "q": "Я уже работаю мастером. Что мне подойдёт?", "k": ["уже мастер", "работаю мастером", "повышени", "квалификац"], "a": "Повышение квалификации: сначала я разбираю ваши работы, потом составляю программу под ваши ошибки и точки роста. Если нужен только разбор, подойдёт онлайн-консультация на 2 часа.", "go": "advanced"}, {"t": "obuchenie", "q": "Что такое онлайн-консультация?", "k": ["консультац", "разбор", "созвон"], "a": "Это 2 часа онлайн лично со мной, 500 zł. Разбираем ваши работы, ошибки, носку, скорость, клей, программу своего курса или старт преподавания.", "go": "consultation"}, {"t": "materialy", "q": "Что внутри пособия?", "k": ["пособи", "страниц"], "a": "51 страница углублённой теории по наращиванию ресниц: рабочее место, материалы, клей, правила наращивания, работа с анагенами, ожог слизистой и другое.", "go": "manual"}, {"t": "materialy", "q": "Пособие можно редактировать?", "k": ["canva", "канва", "редактир", "печат"], "a": "Да, оно полностью редактируется в Canva, без водяных знаков и подходит для печати. Подойдёт преподавателям как основа для своего курса.", "go": "manual"}, {"t": "materialy", "q": "Как устроена теория BASIC в Telegram?", "k": ["telegram", "телеграм", "онлайн", "теори", "урок"], "a": "Урок, затем тест, затем следующий урок, в конце финальная проверка. Внутри видеоуроки, базовое пособие, дополнительные гайды и курс по контенту.", "go": "theory"}, {"t": "materialy", "q": "Кому подойдёт онлайн-теория?", "k": ["кому подойд"], "a": "Мастерам, которые уже проходили практическое обучение, но хотят закрыть пробелы и систематизировать теорию.", "go": "theory"}, {"t": "materialy", "q": "Сколько стоят онлайн-продукты?", "k": ["стоят", "стоит пособие", "цена пособия"], "a": "Базовое пособие 200 zł, теория BASIC в Telegram 500 zł.", "go": "manual"}, {"t": "kontakt", "q": "Как записаться?", "k": ["записат", "запись", "записаться"], "a": "Нажмите «Записаться»: пара коротких шагов, и сообщение откроется в WhatsApp или Telegram, останется нажать «Отправить». Можно и сразу написать мне в WhatsApp.", "go": "any"}, {"t": "kontakt", "q": "Где вы находитесь?", "k": ["адрес", "где", "находит", "krucza", "крушa", "метро"], "a": "В центре Варшавы, Krucza 16/22.", "go": "any"}, {"t": "kontakt", "q": "Как с вами связаться?", "k": ["связат", "телефон", "whatsapp", "ватсап", "инстаграм", "instagram"], "a": "WhatsApp +48 788 214 369, Telegram и Instagram @anya.key_. Отвечаю лично.", "go": ""}];
  function datesAnswer() {
    var l = upcoming('');
    return l.length ? 'Ближайшие курсы:\n' + l.slice(0, 4).map(function (d) { return '• ' + (CNAME[d.c] || d.c) + ': ' + range(d.a, d.b) + ', ' + zl(d.i) + (d.g ? ' (вдвоём ' + zl(d.g) + ' с человека)' : '') + (d.n ? ', ' + d.n : ''); }).join('\n') : 'Новые даты скоро появятся. Напишите мне, и я сообщу первой.';
  }
  var path = location.pathname;
  var HOME = /naraschivanie/.test(path) ? 'lashes' : /(obuchenie|basic|povyshenie|konsultac|reglament)/.test(path) ? 'obuchenie' : /materialy/.test(path) ? 'materialy' : /zapis/.test(path) ? 'kontakt' : '';
  var chat = $('#chat'), cb = $('#chat-b'), fab = $('#fab'), mbar = $('#mbar'), started = false;
  function bubble(t, me) { var m = document.createElement('div'); m.className = 'msg' + (me ? ' me' : ''); m.textContent = t; m.style.whiteSpace = 'pre-line'; cb.appendChild(m); cb.scrollTop = cb.scrollHeight; }
  function btn(w, t, cls, fn) { var b = document.createElement('button'); b.type = 'button'; b.textContent = t; if (cls) b.className = cls; b.addEventListener('click', fn); w.appendChild(b); }
  function chips(topic) {
    $$('.chips', cb).forEach(function (c) { c.remove(); });
    var w = document.createElement('div'); w.className = 'chips';
    if (!topic) {
      TOPICS.filter(function (tp) { return tp[0] === HOME; }).concat(TOPICS.filter(function (tp) { return tp[0] !== HOME; })).forEach(function (tp) {
        btn(w, tp[1], 'tp', function () { bubble(tp[1], true); w.remove(); setTimeout(function () { bubble('Выберите вопрос:'); chips(tp[0]); }, 250); });
      });
    } else {
      FAQ.forEach(function (f) { if (f.t === topic) btn(w, f.q, '', function () { ask(f.q, f); }); });
      btn(w, '← Другие темы', 'bk2', function () { w.remove(); bubble('О чём ваш вопрос?'); chips(''); });
    }
    cb.appendChild(w); cb.scrollTop = cb.scrollHeight;
  }
  function actions(q, f) {
    var w = document.createElement('div'); w.className = 'acts';
    if (f && f.go) { var z = document.createElement('a'); z.className = 'a1'; z.href = url('zapis/' + (f.go === 'any' ? '' : '?w=' + f.go)); z.textContent = 'Записаться'; w.appendChild(z); }
    var wa = document.createElement('a'); wa.className = 'a2'; wa.target = '_blank'; wa.rel = 'noopener';
    wa.href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent('Здравствуйте, Аня! Вопрос с сайта: ' + q);
    wa.textContent = 'Спросить в WhatsApp'; w.appendChild(wa);
    var more = document.createElement('button'); more.type = 'button'; more.className = 'a2'; more.textContent = 'Другой вопрос';
    more.addEventListener('click', function () { w.remove(); if (f) { bubble('Выберите вопрос:'); chips(f.t); } else { bubble('О чём ваш вопрос?'); chips(''); } });
    w.appendChild(more); cb.appendChild(w); cb.scrollTop = cb.scrollHeight;
  }
  function norm(s) { return s.toLowerCase().replace(/ё/g, 'е'); }
  function match(q) {
    var n = norm(q), best = null, score = 0;
    FAQ.forEach(function (f) { var s = 0; f.k.forEach(function (k) { if (n.indexOf(norm(k)) >= 0) s++; }); if (s > score) { score = s; best = f; } });
    return best;
  }
  function ask(q, f) {
    $$('.chips', cb).concat($$('.acts', cb)).forEach(function (c) { c.remove(); });
    bubble(q, true);
    f = f || match(q);
    setTimeout(function () { bubble(f ? (f.a === '@dates' ? datesAnswer() : f.a) : 'Спасибо за вопрос! На него я отвечу лично. Напишите мне в WhatsApp, вопрос уже будет в сообщении.'); actions(q, f); }, 350);
  }
  function openChat() {
    chat.classList.add('on'); if (fab) fab.classList.add('hide'); if (mbar) mbar.classList.add('hide');
    if (!started) { started = true; bubble('Здравствуйте! Я Аня. О чём ваш вопрос?'); chips(''); }
  }
  function closeChat() { chat.classList.remove('on'); if (fab) fab.classList.remove('hide'); if (mbar) mbar.classList.remove('hide'); }
  if (chat) {
    $$('[data-faq]').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); openChat(); }); });
    $('#chat-x').addEventListener('click', closeChat);
    $('#chat-f').addEventListener('submit', function (e) { e.preventDefault(); var i = $('#chat-i'), v = i.value.trim(); if (!v) return; i.value = ''; ask(v); });
  }

  /* ---------- нижняя плашка ---------- */
  var topHide = null;
  function barTop() {
    var t = window.scrollY < window.innerHeight * 0.5;
    if (t === topHide) return; topHide = t;
    [mbar, fab].forEach(function (el) { if (el) el.classList.toggle('top', t); });
  }
  window.addEventListener('scroll', barTop, { passive: true }); barTop();
  var hideOn = $$('.ftr, #fapp');
  if (IO && (mbar || fab) && hideOn.length) {
    var seen = [];
    var ho = new IntersectionObserver(function (en) {
      en.forEach(function (x) { var i = seen.indexOf(x.target); if (x.isIntersecting && i < 0) seen.push(x.target); if (!x.isIntersecting && i >= 0) seen.splice(i, 1); });
      if (chat && chat.classList.contains('on')) return;
      [mbar, fab].forEach(function (el) { if (el) el.classList.toggle('hide', seen.length > 0); });
    }, { threshold: 0.05 });
    hideOn.forEach(function (el) { ho.observe(el); });
  }

  watch(); autoVideos();
})();
