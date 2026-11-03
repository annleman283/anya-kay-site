(function () {
  'use strict';
  var WA = '48788214369';
  var TG = 'https://t.me/AnyaKayClientBot';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var IO = 'IntersectionObserver' in window;
  var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- шапка ---------- */
  var hdr = $('header');
  function hstate() { if (hdr) hdr.classList.toggle('scrolled', window.scrollY >= 80); }
  window.addEventListener('scroll', hstate, { passive: true }); hstate();

  /* ---------- меню на телефоне ---------- */
  var mm = $('#mmenu');
  $$('[data-menu]').forEach(function (b) { b.addEventListener('click', function () { mm.classList.add('on'); document.body.style.overflow = 'hidden'; }); });
  $$('[data-menu-x], #mmenu a').forEach(function (b) { b.addEventListener('click', function () { mm.classList.remove('on'); document.body.style.overflow = ''; }); });

  /* ---------- карусели ---------- */
  $$('.carousel').forEach(function (car) {
    var track = $('.carousel-track', car), items = $$('.carousel-item', car), dots = $('.carousel-dots', car), idx = 0;
    if (dots && !dots.children.length) items.forEach(function (_, i) { var d = document.createElement('button'); d.className = 'carousel-dot' + (i ? '' : ' active'); d.setAttribute('aria-label', 'Слайд ' + (i + 1)); dots.appendChild(d); });
    function upd() {
      track.style.transform = 'translateX(-' + (idx * 100) + '%)';
      if (dots) $$('.carousel-dot', dots).forEach(function (d, i) { d.classList.toggle('active', i === idx); });
      $$('video', track).forEach(function (v) { if (!v.paused) v.pause(); });
    }
    function go(n) { idx = (n + items.length) % items.length; upd(); }
    var p = $('.carousel-btn.prev', car), n = $('.carousel-btn.next', car);
    if (p) p.addEventListener('click', function () { go(idx - 1); });
    if (n) n.addEventListener('click', function () { go(idx + 1); });
    if (dots) $$('.carousel-dot', dots).forEach(function (d, i) { d.addEventListener('click', function () { go(i); }); });
    var sx = null;
    track.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; }, { passive: true });
    track.addEventListener('touchend', function (e) { if (sx === null) return; var dx = e.changedTouches[0].clientX - sx; if (dx > 40) go(idx - 1); else if (dx < -40) go(idx + 1); sx = null; });
  });

  /* ---------- появление при прокрутке ---------- */
  var rv = $$('.reveal');
  if (calm || !IO) rv.forEach(function (e) { e.classList.add('in-view'); });
  else {
    var ro = new IntersectionObserver(function (en) { en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in-view'); ro.unobserve(x.target); } }); }, { threshold: 0.12 });
    rv.forEach(function (e) { ro.observe(e); });
  }

  /* ---------- скрины отзывов ---------- */
  var lb = $('#lb');
  $$('[data-shot]').forEach(function (b) {
    b.addEventListener('click', function () { $('img', lb).src = b.dataset.shot; $('img', lb).alt = b.dataset.alt || 'Скрин отзыва'; lb.classList.add('on'); });
  });
  if (lb) {
    lb.addEventListener('click', function (e) { if (e.target === lb || e.target.closest('.lb-x')) lb.classList.remove('on'); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { lb.classList.remove('on'); closeChat(); } });
  }

  /* ---------- форма записи ---------- */
  var app = $('#fapp');
  var KIND = {
    lashes: 'Запись на наращивание',
    obuchenie: 'Обучение',
    materialy: 'Материалы для мастеров',
    vopros: 'Вопрос'
  };
  var OPTS = {
    lashes: [['1D–4D', 'Классика и объёмы до 4D', '200 zł', 'lashes'], ['5D', 'Самый пышный объём', '230 zł', 'lashes'], ['Подберём вместе', 'Посоветую эффект по форме глаз', '', 'lashes']],
    obuchenie: [['BASIC', 'С нуля · 3 дня · 3 модели', '2800 zł', 'basic'], ['VIP', 'С нуля · 6 дней · 6 моделей', '4000 zł', 'vip'], ['Повышение квалификации', 'Для мастеров · программа после разбора работ', '1000 zł / день', 'advanced'], ['Онлайн-консультация', '2 часа · разбор работ и вопросов', '500 zł', 'consultation']],
    materialy: [['Базовое пособие', '51 страница · редактируется в Canva', '200 zł', 'manual'], ['Теория BASIC в Telegram', '16 уроков, тесты, финальная проверка', '500 zł', 'theory']]
  };
  var W2KIND = { lashes: 'lashes', basic: 'obuchenie', vip: 'obuchenie', advanced: 'obuchenie', consultation: 'obuchenie', manual: 'materialy', theory: 'materialy' };
  var st = {};
  function prog(n) { var h = '<div class="prog">'; for (var i = 1; i <= 3; i++) h += '<span' + (i <= n ? ' class="on"' : '') + '></span>'; return h + '</div>'; }
  function err(t) { var e = $('#f-err'); if (e) e.textContent = t; }
  function seg(id, key, vals) {
    return '<div class="seg2" id="' + id + '">' + vals.map(function (v) { return '<button type="button" aria-pressed="' + (st.d[key] === v ? 'true' : 'false') + '">' + v + '</button>'; }).join('') + '</div>';
  }
  function bindSeg(id, key) {
    $$('#' + id + ' button').forEach(function (b, _, all) {
      b.addEventListener('click', function () { all.forEach(function (o) { o.setAttribute('aria-pressed', 'false'); }); b.setAttribute('aria-pressed', 'true'); st.d[key] = b.textContent; });
    });
  }
  function rows() {
    var d = st.d, r = [];
    if (d.wybor) r.push(['Выбор', d.wybor]);
    if (d.izgib) r.push(['Изгиб L / M', d.izgib]);
    if (d.snyatie) r.push(['Снятие другого мастера', d.snyatie]);
    if (d.opyt) r.push(['Опыт', d.opyt]);
    if (d.kogda) r.push([st.kind === 'lashes' ? 'Удобные дни и время' : 'Когда удобно', d.kogda]);
    return r;
  }
  function render() {
    if (!app) return;
    var h = '', k = st.kind;
    if (!k) {
      h = prog(1) + '<div class="q">Что вас интересует?</div><div class="h">Три коротких шага. В конце сообщение откроется в WhatsApp или Telegram, останется нажать «Отправить».</div><div class="opts">' +
        '<button type="button" class="opt" data-k="lashes"><b>Наращивание ресниц</b><small>Krucza 16/22, Варшава · 90 минут</small><em>от 200 zł</em></button>' +
        '<button type="button" class="opt" data-k="obuchenie"><b>Обучение</b><small>BASIC, VIP, повышение квалификации, консультация</small><em>от 500 zł</em></button>' +
        '<button type="button" class="opt" data-k="materialy"><b>Материалы для мастеров</b><small>Пособие и теория BASIC онлайн</small><em>от 200 zł</em></button>' +
        '<button type="button" class="opt" data-k="vopros"><b>Просто задать вопрос</b><small>Отвечу лично</small><em></em></button></div>';
      app.innerHTML = h;
      $$('.opt', app).forEach(function (b) { b.addEventListener('click', function () { st = { kind: b.dataset.k, step: b.dataset.k === 'vopros' ? 2 : 1, d: {} }; render(); }); });
      return;
    }
    if (st.step === 1) {
      h = prog(2) + '<div class="q">' + (k === 'lashes' ? 'Какой объём?' : k === 'obuchenie' ? 'Какой формат?' : 'Что именно?') + '</div><div class="opts">';
      OPTS[k].forEach(function (o, i) { h += '<button type="button" class="opt" data-i="' + i + '"><b>' + o[0] + '</b><small>' + o[1] + '</small><em>' + o[2] + '</em></button>'; });
      h += '</div>';
      if (k === 'lashes') h += '<div style="margin-top:22px"><div class="fld"><label>Изгиб L / M (+20 zł)?</label>' + seg('f-iz', 'izgib', ['Нет', 'Да', 'Не знаю']) + '</div><div class="fld"><label>Сейчас есть наращенные ресницы другого мастера?</label>' + seg('f-sn', 'snyatie', ['Нет', 'Да, нужно снять (+30 zł)']) + '</div><div class="fld"><label for="f-kogda">Удобные дни и время</label><input id="f-kogda" placeholder="например: будни после 17:00" value="' + esc(st.d.kogda || '') + '"></div></div>';
      if (k === 'obuchenie') h += '<div style="margin-top:22px"><div class="fld"><label>Ваш опыт</label>' + seg('f-op', 'opyt', ['С нуля', 'Уже работаю мастером']) + '</div><div class="fld"><label for="f-kogda">Когда хотите учиться?</label><input id="f-kogda" placeholder="месяц или даты" value="' + esc(st.d.kogda || '') + '"></div></div>';
      h += '<div class="f-row"><button type="button" class="back" data-back>← Назад</button></div><div class="f-err" id="f-err"></div>';
      app.innerHTML = h;
      bindSeg('f-iz', 'izgib'); bindSeg('f-sn', 'snyatie'); bindSeg('f-op', 'opyt');
      $$('.opt', app).forEach(function (b) {
        b.addEventListener('click', function () {
          var o = OPTS[k][+b.dataset.i]; st.d.wybor = o[0]; st.w = o[3];
          var kd = $('#f-kogda'); if (kd) st.d.kogda = kd.value.trim();
          st.step = 2; render();
        });
      });
      $('[data-back]', app).addEventListener('click', function () { st = {}; render(); });
      return;
    }
    if (st.step === 2) {
      var sum = rows();
      h = prog(3) + '<div class="q">Как с вами связаться?</div>' +
        (sum.length ? '<div class="sum">' + sum.map(function (x) { return '<span><b>' + x[0] + ':</b> ' + esc(x[1]) + '</span>'; }).join('') + '</div>' : '') +
        '<div class="fld"><label for="f-name">Имя</label><input id="f-name" autocomplete="given-name" value="' + esc(st.d.imya || '') + '"></div>' +
        '<div class="fld"><label for="f-tel">Телефон или ник в Telegram</label><input id="f-tel" autocomplete="tel" value="' + esc(st.d.tel || '') + '"></div>' +
        '<div class="fld"><label for="f-msg">' + (k === 'vopros' ? 'Ваш вопрос' : 'Комментарий (по желанию)') + '</label><textarea id="f-msg">' + esc(st.d.msg || '') + '</textarea></div>' +
        '<label class="chk"><input type="checkbox" id="f-ok"> <span>Согласна, чтобы мои данные использовались для ответа на заявку. <a href="/politika-konfidencialnosti/" target="_blank">Политика конфиденциальности</a></span></label>' +
        '<button type="button" class="btn btn-primary" style="width:100%" data-send>Подготовить сообщение</button>' +
        '<div class="f-err" id="f-err"></div><div class="f-row"><button type="button" class="back" data-back>← Назад</button></div>';
      app.innerHTML = h;
      $('[data-back]', app).addEventListener('click', function () { st.step = k === 'vopros' ? 0 : 1; if (!st.step) st = {}; render(); });
      $('[data-send]', app).addEventListener('click', send);
      return;
    }
  }
  function top() { var y = app.getBoundingClientRect().top + window.scrollY - 90; if (window.scrollY > y) window.scrollTo({ top: y, behavior: 'smooth' }); }
  function send() {
    var d = st.d;
    d.imya = $('#f-name').value.trim(); d.tel = $('#f-tel').value.trim(); d.msg = $('#f-msg').value.trim();
    if (!d.imya) return err('Напишите, как вас зовут.');
    if (d.tel.replace(/[^0-9a-zA-Z_]/g, '').length < 4) return err('Оставьте телефон или ник в Telegram.');
    if (st.kind === 'vopros' && !d.msg) return err('Напишите вопрос.');
    if (!$('#f-ok').checked) return err('Отметьте согласие, чтобы я могла ответить.');
    var lines = ['Здравствуйте, Аня! Заявка с сайта anyakay.pl', KIND[st.kind]];
    rows().forEach(function (x) { lines.push(x[0] + ': ' + x[1]); });
    lines.push('Имя: ' + d.imya, 'Контакт: ' + d.tel);
    if (d.msg) lines.push((st.kind === 'vopros' ? 'Вопрос: ' : 'Комментарий: ') + d.msg);
    var text = lines.join('\n');
    var wa = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(text);
    var tg = TG + (st.w ? '?start=' + st.w : '');
    app.innerHTML = prog(3) + '<div class="q">Спасибо, ' + esc(d.imya) + '!</div><div class="h">Сообщение готово. Выберите, где удобнее, и нажмите «Отправить» в мессенджере.</div>' +
      '<div class="send-row"><a class="btn btn-primary" href="' + wa + '" target="_blank" rel="noopener">Отправить в WhatsApp</a>' +
      '<a class="btn btn-outline" href="' + tg + '" target="_blank" rel="noopener" id="f-tg">Скопировать и открыть Telegram</a></div>' +
      '<div class="sum-all">' + esc(text) + '</div>' +
      '<p class="h" style="margin-top:12px">В Telegram текст скопируется сам, вставьте его в чат.</p>' +
      '<button type="button" class="back" id="f-new">Новая заявка</button>';
    $('#f-tg').addEventListener('click', function () { try { navigator.clipboard.writeText(text); } catch (e) {} });
    $('#f-new').addEventListener('click', function () { st = {}; render(); });
    top();
  }
  if (app) {
    var q = new URLSearchParams(location.search), k = q.get('k'), w = q.get('w');
    if (w && W2KIND[w]) {
      k = W2KIND[w];
      var o = OPTS[k].filter(function (x) { return x[3] === w; })[0];
      st = { kind: k, step: k === 'lashes' ? 1 : 2, d: {}, w: w };
      if (o && k !== 'lashes') st.d.wybor = o[0];
    } else if (k && KIND[k]) st = { kind: k, step: k === 'vopros' ? 2 : 1, d: {} };
    render();
  }

  /* ---------- помощник «Есть вопрос?» ---------- */
  var TOPICS = [['lashes', 'Наращивание'], ['obuchenie', 'Обучение'], ['materialy', 'Материалы'], ['kontakt', 'Запись и контакты']];
  var ADR = 'Я работаю в центре Варшавы: Krucza 16/22.';
  var FAQ = [
    { t: 'lashes', q: 'Сколько стоит наращивание?', k: ['стои', 'цен', 'прайс', 'zł', 'злот', '1d', '2d', '3d', '4d', '5d', 'объем', 'объём'], a: '1D–4D: 200 zł, 5D: 230 zł. Изгибы L / M: +20 zł. Снятие ресниц другого мастера с последующим наращиванием: +30 zł.', go: 'lashes' },
    { t: 'lashes', q: 'Сколько длится процедура?', k: ['длит', 'долго', 'времени', 'час', 'минут'], a: 'Само наращивание около 90 минут, вместе со снятием до 2 часов.', go: 'lashes' },
    { t: 'lashes', q: 'Сколько держатся ресницы?', k: ['держ', 'нос', 'недел'], a: 'Носка 3–5 недель. Работаю так, чтобы ресницы отрастали комфортно и аккуратно.', go: 'lashes' },
    { t: 'lashes', q: 'Делаете коррекцию?', k: ['коррек'], a: 'Коррекции не делаю, только полное перенаращивание. Так результат каждый раз аккуратный и свежий.', go: 'lashes' },
    { t: 'lashes', q: 'Какой эффект мне подойдёт?', k: ['эффект', 'подойд', 'выбра', 'лами', 'лиса', 'кукол'], a: 'Эффект подбираю индивидуально: по форме глаз, вашим ресницам и тому, как вы хотите выглядеть. Если не уверены, просто выберите «Подберём вместе» в записи.', go: 'lashes' },
    { t: 'lashes', q: 'Где вы принимаете?', k: ['где', 'адрес', 'кручa', 'krucza', 'метро', 'район'], a: ADR },
    { t: 'obuchenie', q: 'Какое обучение есть?', k: ['обуч', 'курс', 'форма', 'учит', 'научит'], a: 'BASIC с нуля: 3 дня, 3 модели, 2800 zł.\nVIP: 6 дней, 6 моделей, 4000 zł.\nПовышение квалификации для мастеров: 1000 zł / день.\nОнлайн-консультация: 2 часа, 500 zł.\nИ онлайн-теория BASIC в Telegram: 500 zł.', go: 'basic' },
    { t: 'obuchenie', q: 'Можно учиться с нуля?', k: ['нул', 'новичок', 'никогда', 'начина', 'без опыт'], a: 'Да, BASIC и VIP как раз для старта с нуля. Сначала теория в Telegram в своём темпе, с тестами после уроков, потом практика на манекене и живых моделях.', go: 'basic' },
    { t: 'obuchenie', q: 'Чем VIP отличается от BASIC?', k: ['vip', 'вип', 'отлич', 'разниц'], a: 'В VIP всё из BASIC и в два раза больше практики: 6 дней и 6 моделей вместо 3, отработка L- и M-изгибов, 2 трендовых эффекта на выбор, стартовый набор материалов и кубок VIP-мастера.', go: 'vip' },
    { t: 'obuchenie', q: 'Будет сертификат и поддержка?', k: ['сертиф', 'поддерж', 'после курса', 'помощь'], a: 'Да. После курса вы получаете именной сертификат с печатью, а после BASIC у вас неограниченная поддержка: можно присылать работы и задавать вопросы.', go: 'basic' },
    { t: 'obuchenie', q: 'Я уже мастер. Что мне подойдёт?', k: ['мастер', 'работаю', 'опыт', 'повыш', 'квалиф', 'ошибк', 'скорост'], a: 'Повышение квалификации: сначала разбираю ваши работы, потом составляю программу под ваши ошибки и точки роста (техника, скорость, объёмы до 5D, моделирование, эффекты). Стандартно 1 день, 1000 zł.\nЕсли нужен только разбор, есть онлайн-консультация на 2 часа за 500 zł.', go: 'advanced' },
    { t: 'materialy', q: 'Что внутри пособия?', k: ['пособ', 'canva', 'книг', 'pdf'], a: '51 страница углублённой теории по наращиванию. Полностью редактируется в Canva, без водяных знаков, подходит для печати. Подходит мастерам и преподавателям, которым нужна основа для своего курса. 200 zł.', go: 'manual' },
    { t: 'materialy', q: 'Как устроена теория в Telegram?', k: ['теор', 'телеграм', 'telegram', 'онлайн', 'урок', 'тест'], a: 'Весь теоретический блок BASIC онлайн: 16 видеоуроков, после каждого тест, в конце финальная проверка. Внутри пособие, дополнительные гайды и курс по контенту. 500 zł.', go: 'theory' },
    { t: 'kontakt', q: 'Как записаться?', k: ['запис', 'свобод', 'окошк', 'время', 'дата'], a: 'Оставьте короткую заявку на странице «Запись», сообщение откроется в WhatsApp или Telegram. Или напишите мне напрямую.', go: 'any' },
    { t: 'kontakt', q: 'Где вы находитесь?', k: [], a: ADR }
  ];
  var path = location.pathname;
  var HOME = /naraschivanie/.test(path) ? 'lashes' : /(obuchenie|basic|povyshenie|konsultac)/.test(path) ? 'obuchenie' : /materialy/.test(path) ? 'materialy' : /zapis/.test(path) ? 'kontakt' : '';
  var chat = $('#chat'), cb = $('#chat-b'), fab = $('#fab'), mbar = $('#mbar'), started = false;
  function bubble(t, me) { var m = document.createElement('div'); m.className = 'msg' + (me ? ' me' : ''); m.textContent = t; cb.appendChild(m); cb.scrollTop = cb.scrollHeight; }
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
    if (f && f.go) { var z = document.createElement('a'); z.className = 'a1'; z.href = '/zapis/' + (f.go === 'any' ? '' : '?w=' + f.go); z.textContent = 'Записаться'; w.appendChild(z); }
    var wa = document.createElement('a'); wa.target = '_blank'; wa.rel = 'noopener';
    wa.href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent('Здравствуйте, Аня! Вопрос с сайта: ' + q);
    wa.textContent = 'Спросить в WhatsApp'; w.appendChild(wa);
    var tg = document.createElement('a'); tg.target = '_blank'; tg.rel = 'noopener'; tg.href = TG; tg.textContent = 'Telegram'; w.appendChild(tg);
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
    setTimeout(function () { bubble(f ? f.a : 'Спасибо за вопрос! На него я отвечу лично. Напишите мне в WhatsApp, вопрос уже будет в сообщении.'); actions(q, f); }, 350);
  }
  function openChat() {
    chat.classList.add('on'); if (fab) fab.classList.add('hide'); if (mbar) mbar.classList.add('hide');
    if (!started) { started = true; bubble('Здравствуйте! Я Аня. О чём ваш вопрос?'); chips(''); }
  }
  function closeChat() { if (!chat) return; chat.classList.remove('on'); if (fab) fab.classList.remove('hide'); if (mbar) { mbar.classList.remove('hide'); barTop(true); } }
  if (chat) {
    $$('[data-faq]').forEach(function (b) { b.addEventListener('click', openChat); });
    $('#chat-x').addEventListener('click', closeChat);
    $('#chat-f').addEventListener('submit', function (e) { e.preventDefault(); var i = $('#chat-i'), v = i.value.trim(); if (!v) return; i.value = ''; ask(v); });
  }

  /* ---------- нижняя плашка ---------- */
  var topHide = null;
  function barTop(force) {
    var t = window.scrollY < window.innerHeight * 0.5 && !document.body.classList.contains('bar-always');
    if (t === topHide && !force) return; topHide = t;
    [mbar, fab].forEach(function (el) { if (el) el.classList.toggle('top', t); });
  }
  window.addEventListener('scroll', function () { barTop(); }, { passive: true }); barTop();
  var hideOn = $$('footer, #fapp');
  if (IO && mbar && hideOn.length) {
    var seen = [];
    var ho = new IntersectionObserver(function (en) {
      en.forEach(function (x) { var i = seen.indexOf(x.target); if (x.isIntersecting && i < 0) seen.push(x.target); if (!x.isIntersecting && i >= 0) seen.splice(i, 1); });
      if (chat && chat.classList.contains('on')) return;
      mbar.classList.toggle('hide', seen.length > 0);
    }, { threshold: 0.05 });
    hideOn.forEach(function (el) { ho.observe(el); });
  }
})();
