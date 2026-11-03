#!/usr/bin/env python3
"""Сборка anyakay.pl. Запуск из корня репозитория: python3 -I _build/build.py .
Править тексты здесь, потом пересобрать. Фото лежат в /img, видео в /assets/videos."""
import json, os, shutil, sys, html

B = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
SITE = 'https://anyakay.pl'
V = '40'
SV = json.load(open(os.path.join(B, 'svgs.json')))
TG_I, WA_I, IG_I = SV
TG = 'https://t.me/AnyaKayClientBot'
WA = 'https://wa.me/48788214369'
IG = 'https://www.instagram.com/anya.key_/'
CHAT_I = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4 5h16v11H9l-5 4z" stroke-linejoin="round"/></svg>'

# ---------------- данные ----------------
CLIENT_Q = [
    ('Анечка, реснички просто космос, хожу кайфую! Спасибо большое.', None, 'Клиентка', 'после наращивания', '/img/otzyv-klient-4.jpg'),
    ('Хотела поблагодарить тебя за прекрасную работу. Я очень довольна. Приятно в зеркало смотреть.', None, 'Клиентка', 'после наращивания', '/img/otzyv-klient-3.jpg'),
    ('Реснички супер, прошли тест-драйв в Красном море.', None, 'Клиентка', 'после отпуска', '/img/otzyv-klient-2.jpg'),
    ('2,5 года не наращивала ресниц и доверилась @anya.key_. Новый эффект лами в наращивании.', None, 'Марина', 'сторис в Instagram', '/img/otzyv-klient-1.jpg'),
]
STUDENT_Q = [
    ('Ты рассказываешь всё чётко, грамотно, по делу. Ты реально сидишь и наращиваешь до посинения, а не как на курсах, смотришь, как мастер делает.', None, 'Карина', 'ученица', '/img/otzyv-karina.jpg'),
    ('Ты превзошла мои ожидания от обучения. Вопросов после курса не осталось, всё разложила по полочкам и без лишней воды.', None, 'Света', 'ученица', '/img/otzyv-sveta.jpg'),
    ('Так я научилась только благодаря тебе. Последние наращивания сделаны уже ровно за 2:40–3 максимум, для меня это рекорд.', None, 'Настя', 'ученица', '/img/otzyv-nastya.jpg'),
    ('Хочу ще раз подякувати за ці 6 днів. Вони просто пролетіли як 5 хвилин. Я би ще раз записалася до тебе на VIP курс.',
     'Хочу ещё раз поблагодарить за эти 6 дней. Они пролетели как 5 минут. Я бы ещё раз записалась к тебе на VIP-курс.', 'Яна', 'ученица VIP, 6 дней', '/img/otzyv-yana.jpg'),
]

FAQ_LASH = [
    ('Сколько стоит наращивание ресниц?', 'Наращивание 1D–4D стоит 200 zł, 5D 230 zł. Изгибы L / M +20 zł. Снятие ресниц другого мастера с последующим наращиванием +30 zł.'),
    ('Сколько длится процедура?', 'Само наращивание около 90 минут, вместе со снятием до 2 часов.'),
    ('Сколько держатся ресницы?', 'Носка 3–5 недель. Техника рассчитана на комфортное и аккуратное отрастание.'),
    ('Делаете коррекцию?', 'Коррекции не делаю, только полное перенаращивание. Так результат каждый раз свежий и аккуратный.'),
    ('Как выбрать эффект?', 'Эффект подбирается индивидуально: по форме глаз, состоянию ваших ресниц и тому, какой образ вам ближе. Можно прийти без идеи, подберём вместе.'),
    ('Где проходит процедура?', 'В центре Варшавы, Krucza 16/22. Запись через сайт, Telegram, WhatsApp или Instagram.'),
]
FAQ_EDU = [
    ('Можно учиться с нуля?', 'Да. BASIC и VIP рассчитаны на старт с нуля: сначала теория в Telegram в своём темпе с тестами после уроков, потом практика на 3D-манекене и живых моделях.'),
    ('Чем VIP отличается от BASIC?', 'VIP включает всё из BASIC и в два раза больше практики: 6 дней и 6 моделей вместо 3, отработку L- и M-изгибов, 2 трендовых эффекта на выбор, стартовый набор материалов и кубок VIP-мастера.'),
    ('Выдаёте сертификат?', 'Да, после обучения вы получаете именной сертификат с печатью.'),
    ('Будет поддержка после курса?', 'Да, после BASIC у вас неограниченная поддержка: можно присылать работы и задавать вопросы.'),
    ('Я уже работаю мастером. Что мне подойдёт?', 'Повышение квалификации: сначала я разбираю ваши работы, потом составляю программу под ваши ошибки и точки роста. Если нужен только разбор, подойдёт онлайн-консультация на 2 часа.'),
    ('Можно изучить только теорию?', 'Да, весь теоретический блок BASIC доступен онлайн в Telegram за 500 zł, а базовое пособие на 51 страницу можно купить отдельно за 200 zł.'),
]
FAQ_HOME = [FAQ_LASH[0], FAQ_LASH[2], FAQ_EDU[0], FAQ_EDU[1], FAQ_EDU[4]]
FAQ_ADV = [
    ('Как проходит повышение квалификации?', 'Вы присылаете свои работы, я разбираю их и нахожу точки роста. Под них составляю программу, и мы отрабатываем её на практике.'),
    ('Сколько длится и сколько стоит?', 'Стандартно 1 день, 1000 zł. Если задач больше, программу можно расширить.'),
    ('Что можно проработать?', 'Ошибки в технике, скорость, объёмы до 5D, моделирование взгляда и эффекты.'),
    ('А если мне нужен только разбор?', 'Тогда подойдёт онлайн-консультация: 2 часа, 500 zł. Разберём работы, ошибки и ваши вопросы.'),
]
FAQ_MAT = [
    ('Что внутри пособия?', '51 страница углублённой теории по наращиванию ресниц: рабочее место, материалы, клей, правила наращивания, работа с анагенами, ожог слизистой и другое.'),
    ('Пособие можно редактировать?', 'Да, оно полностью редактируется в Canva, без водяных знаков и подходит для печати. Подойдёт преподавателям как основа для своего курса.'),
    ('Как устроена теория BASIC в Telegram?', 'Урок, затем тест, затем следующий урок, в конце финальная проверка. Внутри видеоуроки, базовое пособие, дополнительные гайды и курс по контенту.'),
    ('Кому подойдёт онлайн-теория?', 'Мастерам, которые уже проходили практическое обучение, но хотят закрыть пробелы и систематизировать теорию.'),
]
LESSONS = ['Знакомство и организационные моменты', 'Строение ресниц', 'Материалы 1.0', 'Материалы 2.0', 'Организация рабочего места', 'Виды ресниц',
           'Правила наращивания', 'Клей, часть 1', 'Клей, часть 2', 'Моделирование взгляда', 'Работа с рядами', 'Снятие ресниц', 'Коррекция ресниц',
           'Ожог слизистой', 'Аллергия мастера и клиента', 'Стерилизация инструментов']

ADDRESS = {"@type": "PostalAddress", "streetAddress": "Krucza 16/22", "addressLocality": "Warszawa", "addressCountry": "PL"}
BUSINESS = {"@type": "BeautySalon", "@id": SITE + "/#business", "name": "Anya Kay", "url": SITE + "/", "image": SITE + "/img/hero.jpg",
            "logo": SITE + "/img/avatar.jpg", "telephone": "+48788214369", "address": ADDRESS, "priceRange": "200–4000 zł",
            "description": "Наращивание ресниц и обучение lash-мастеров в Варшаве.", "sameAs": [IG, TG], "areaServed": "Warszawa",
            "founder": {"@type": "Person", "name": "Anya Kay", "jobTitle": "Lash-мастер и преподаватель"}}


def e(s):
    return html.escape(s, quote=True)


def faq_html(items, dark=False):
    return '<div class="faq">' + ''.join(f'<details><summary>{e(q)}</summary><div class="ans">{e(a)}</div></details>' for q, a in items) + '</div>'


def faq_ld(items):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def course_ld(name, desc, price, path):
    return {"@type": "Course", "name": name, "description": desc, "inLanguage": "ru",
            "provider": {"@id": SITE + "/#business"}, "url": SITE + path,
            "offers": {"@type": "Offer", "price": price, "priceCurrency": "PLN", "category": "Paid", "url": SITE + path},
            "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "onsite" if 'online' not in path else "online", "location": "Warszawa, Krucza 16/22"}}


def quotes(items, scroll=False):
    out = []
    for q, tr, who, note, shot in items:
        out.append('<figure class="quote reveal"><blockquote>' + e(q) + '</blockquote>' + (f'<p class="tr">Перевод: {e(tr)}</p>' if tr else '') +
                   f'<figcaption class="quote-foot"><div><b>{e(who)}</b><span>{e(note)}</span></div>'
                   f'<button type="button" class="shot-btn" data-shot="{shot}" data-alt="Скрин отзыва: {e(who)}">Скрин ↗</button></figcaption></figure>')
    return f'<div class="{"quotes-scroll" if scroll else "quotes"}">' + ''.join(out) + '</div>'


def carousel(items, extra=''):
    sl = ''.join(f'<div class="carousel-item">{x}</div>' for x in items)
    return (f'<div class="carousel contain"{extra}><div class="carousel-track">{sl}</div>'
            '<button class="carousel-btn prev" aria-label="Назад">‹</button><button class="carousel-btn next" aria-label="Далее">›</button>'
            '<div class="carousel-dots"></div></div>')


def img(src, alt):
    return f'<img src="{src}" alt="{e(alt)}" loading="lazy" decoding="async">'


def vid(name, label):
    return (f'<video controls playsinline preload="none" poster="/assets/videos/{name}_poster.jpg" aria-label="{e(label)}">'
            f'<source src="/assets/videos/{name}.mp4" type="video/mp4"></video>')


CASE = '''<section class="sec"><div class="wrap"><div class="case reveal">
  <div class="case-copy"><p class="kick" style="color:var(--gold-light)">Результат ученицы</p><div class="case-num">800 zł</div>
  <h3>за 2,5 недели после обучения</h3>
  <p>Света прошла обучение и за первые 2,5 недели обслужила 9 клиенток, работая параллельно на заводе. Её ценник на наращивание уже 100 zł, а модели возвращаются и становятся постоянными клиентками.</p></div>
  <button type="button" class="case-media" style="background-image:url('/img/otzyv-sveta-rezultat.jpg')" data-shot="/img/otzyv-sveta-rezultat.jpg" data-alt="Переписка с ученицей Светой" aria-label="Открыть переписку"></button>
</div></div></section>'''


def final(title, text, btns):
    b = ''.join(f'<a class="btn {c}" href="{h}"{" target=_blank rel=noopener" if h.startswith("http") else ""}>{t}</a>' for t, h, c in btns)
    return f'<section class="final"><div class="wrap"><h2 class="reveal">{title}</h2><p class="reveal">{text}</p><div class="btn-row reveal">{b}</div></div></section>'


NAV = [('Наращивание', '/naraschivanie/'), ('Обучение', '/obuchenie/'), ('Материалы', '/materialy/'), ('Отзывы', '/#otzyvy'), ('Контакты', '#contacts')]


def page(path, title, desc, body, ld=None, cls='', nav_on=''):
    url = SITE + path
    ld_all = [BUSINESS] + (ld or [])
    navh = ''.join(f'<a href="{h}"{" class=on" if nav_on == h else ""}>{t}</a>' for t, h in NAV)
    head = f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#3E0E1A">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Anya Kay">
<meta property="og:locale" content="ru_RU">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,500&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css?v={V}">
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": ld_all}, ensure_ascii=False)}</script>
</head>
<body class="{cls}">
<header>
  <div class="header-inner">
    <a class="logo-mini" href="/" aria-label="Anya Kay, на главную"><img src="/img/avatar.jpg" alt="" width="40" height="40"><span>Anya Kay</span></a>
    <nav aria-label="Разделы">{navh}</nav>
    <div class="head-right">
      <a href="/zapis/" class="btn btn-primary head-cta">Записаться</a>
      <button class="burger" type="button" data-menu aria-label="Открыть меню"><i></i><i></i><i></i></button>
    </div>
  </div>
</header>
<div class="mmenu" id="mmenu" role="dialog" aria-label="Меню">
  <div class="mmenu-top"><span>ANYA KAY</span><button class="mmenu-x" type="button" data-menu-x aria-label="Закрыть меню">×</button></div>
  <div class="mmenu-links">
    <a href="/">Главная <small>Варшава</small></a>
    <a href="/naraschivanie/">Наращивание <small>от 200 zł</small></a>
    <a href="/obuchenie/">Обучение <small>4 формата</small></a>
    <a class="sub" href="/basic-lash-course/">Курс с нуля BASIC / VIP</a>
    <a class="sub" href="/povyshenie-kvalifikacii/">Повышение квалификации</a>
    <a class="sub" href="/konsultaciya/">Онлайн-консультация</a>
    <a href="/materialy/">Материалы <small>онлайн</small></a>
  </div>
  <div class="mmenu-bottom">
    <a class="btn btn-gold" href="/zapis/">Записаться</a>
    <div class="mmenu-soc footer-socials">
      <a class="footer-social" href="{TG}" target="_blank" rel="noopener" aria-label="Telegram">{TG_I}</a>
      <a class="footer-social" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_I}</a>
      <a class="footer-social" href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{IG_I}</a>
    </div>
  </div>
</div>
<main>
'''
    foot = f'''</main>
<footer id="contacts">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-logo footer-wordmark"><span>ANYA KAY</span></div>
      <div class="footer-links"><a href="/naraschivanie/">Наращивание</a><a href="/obuchenie/">Обучение</a><a href="/zapis/">Запись</a></div>
    </div>
    <div class="foot-nav"><a href="/basic-lash-course/">Курс с нуля BASIC / VIP</a><a href="/povyshenie-kvalifikacii/">Повышение квалификации</a><a href="/konsultaciya/">Онлайн-консультация</a><a href="/materialy/">Пособие и онлайн-теория</a></div>
    <div class="footer-bottom">
      <span><a href="https://www.google.com/maps/search/?api=1&query=Krucza+16%2F22+Warszawa" target="_blank" rel="noopener">Krucza 16/22, Варшава, Польша</a></span>
      <span>© 2026 Anya Kay</span>
    </div>
    <div class="footer-contact" aria-label="Связаться со мной">
      <div class="footer-contact-title">Связаться со мной</div>
      <div class="footer-socials">
        <a class="footer-social" href="{TG}" target="_blank" rel="noopener" aria-label="Telegram" title="Telegram">{TG_I}</a>
        <a class="footer-social" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp" title="WhatsApp">{WA_I}</a>
        <a class="footer-social" href="{IG}" target="_blank" rel="noopener" aria-label="Instagram" title="Instagram">{IG_I}</a>
      </div>
    </div>
    <p class="foot-legal"><a href="/politika-konfidencialnosti/">Политика конфиденциальности</a></p>
  </div>
</footer>
<div class="mbar top" id="mbar"><a class="m1" href="/zapis/">Записаться</a><button class="m2" type="button" data-faq>Есть вопрос?</button></div>
<button class="fab top" id="fab" type="button" data-faq>{CHAT_I}Есть вопрос?</button>
<div class="chat" id="chat" role="dialog" aria-label="Вопросы и ответы">
  <div class="chat-h"><img src="/img/avatar.jpg" alt=""><div><b>Есть вопрос?</b><span>Частые вопросы и быстрая связь</span></div><button class="chat-x" id="chat-x" type="button" aria-label="Закрыть">×</button></div>
  <div class="chat-b" id="chat-b"></div>
  <form class="chat-f" id="chat-f"><input id="chat-i" placeholder="Напишите свой вопрос" aria-label="Ваш вопрос" autocomplete="off"><button type="submit" aria-label="Отправить">↑</button></form>
</div>
<div class="lb" id="lb"><button class="lb-x" type="button" aria-label="Закрыть">×</button><img alt=""></div>
<script src="/app.js?v={V}" defer></script>
</body>
</html>
'''
    if path.endswith('/'):
        d = os.path.join(OUT, path.strip('/')); os.makedirs(d, exist_ok=True); fn = os.path.join(d, 'index.html')
    else:
        fn = os.path.join(OUT, path.strip('/'))
    open(fn, 'w', encoding='utf-8').write(head + body + foot)


def cover(crumb, h1, lead, facts=None, cta=None, cls=''):
    f = ''
    if facts:
        f = '<div class="cover-facts">' + ''.join(f'<div><strong>{a}</strong><span>{b}</span></div>' for a, b in facts) + '</div>'
    c = ''
    if cta:
        c = '<div class="cover-cta">' + ''.join(f'<a class="btn {k}" href="{h}">{t}</a>' for t, h, k in cta) + '</div>'
    cr = f'<p class="crumbs"><a href="/">Anya Kay</a> · {crumb}</p>' if crumb else ''
    return f'<section class="cover {cls}"><div class="wrap">{cr}<h1>{h1}</h1><p class="lead">{lead}</p>{f}{c}</div></section>'


def dir_card(href, small, title, text, price):
    return f'<a class="dir-card reveal" href="{href}"><small>{small}</small><h3>{title}</h3><p>{text}</p><div class="price">{price}</div><div class="go">Подробнее ↗</div></a>'


# ================= ГЛАВНАЯ =================
home = f'''
<section class="hero">
  <div class="hero-content">
    <h1 class="hero-brand">ANYA KAY<span class="sr"> · наращивание ресниц и обучение в Варшаве</span></h1>
    <p class="hero-subtitle">Наращивание ресниц и обучение в одном месте.</p>
    <div class="hero-links">
      <a href="/naraschivanie/" class="hero-link">Наращивание <span class="hero-link-arrow">↗</span></a>
      <a href="/obuchenie/" class="hero-link">Обучение <span class="hero-link-arrow">↗</span></a>
    </div>
  </div>
</section>
<section class="choice-section">
  <div class="wrap choice-wrap">
    <p class="choice-kicker reveal">Выберите направление</p>
    <div class="choice-list">
      <a class="choice-row reveal" href="/naraschivanie/"><span class="choice-num">01</span><span class="choice-title">Наращивание ресниц</span><span class="choice-arrow">↗</span></a>
      <a class="choice-row reveal" href="/obuchenie/"><span class="choice-num">02</span><span class="choice-title">Обучение</span><span class="choice-arrow">↗</span></a>
    </div>
    <p class="choice-note reveal">Процедуры для клиенток и обучение для начинающих и практикующих мастеров.</p>
  </div>
</section>
<section class="about-editorial">
  <div class="about-editorial-media reveal" aria-hidden="true"></div>
  <div class="about-editorial-copy reveal">
    <p class="about-editorial-kicker">Обо мне</p>
    <h2>Я работаю мастером.<br>И обучаю тому,<br>что использую сама.</h2>
    <p class="about-editorial-text">В lash-индустрии с 2017 года. Сегодня я совмещаю работу мастера и преподавателя, а в обучении делаю ставку на понимание техники, сильную теорию и практику.</p>
    <div class="about-editorial-stats">
      <div><strong>9+</strong><span>лет в профессии</span></div>
      <div><strong>100+</strong><span>обученных учениц</span></div>
      <div><strong>с 2017</strong><span>в lash-индустрии</span></div>
    </div>
  </div>
</section>
<section class="sec sec-soft" style="padding-top:110px">
  <div class="wrap">
    <div class="head-row"><div><p class="kick reveal">Услуги и обучение</p><h2 class="h2 reveal">Наращивание ресниц<br>и курсы в Варшаве</h2></div>
    <p class="sub reveal">Процедуры в центре Варшавы на Krucza 16/22 и обучение для тех, кто начинает с нуля или уже работает мастером.</p></div>
    <div class="dir-grid">
      {dir_card('/naraschivanie/', 'Для клиенток', 'Наращивание ресниц', '1D–5D, эффект подбирается индивидуально. 90 минут, носка 3–5 недель.', 'от 200 <span>zł</span>')}
      {dir_card('/basic-lash-course/', 'С нуля · 3 дня', 'Курс BASIC', 'Теория в Telegram, практика на манекене и 3 живых моделях, сертификат.', '2800 <span>zł</span>')}
      {dir_card('/basic-lash-course/#vip', 'С нуля · 6 дней', 'Курс VIP', 'Всё из BASIC и вдвое больше практики: 6 моделей, L/M-изгибы, трендовые эффекты.', '4000 <span>zł</span>')}
      {dir_card('/povyshenie-kvalifikacii/', 'Для мастеров', 'Повышение квалификации', 'Сначала разбор ваших работ, потом программа под ваши точки роста.', '1000 <span>zł / день</span>')}
      {dir_card('/konsultaciya/', 'Онлайн · 2 часа', 'Консультация', 'Разбор работ, ошибок, скорости, клея, старта преподавания.', '500 <span>zł</span>')}
      {dir_card('/materialy/', 'Учиться самостоятельно', 'Пособие и онлайн-теория', 'Пособие на 51 страницу и теория BASIC в Telegram с тестами.', 'от 200 <span>zł</span>')}
    </div>
  </div>
</section>
<section class="sec" id="otzyvy">
  <div class="wrap">
    <div class="head-row"><div><p class="kick reveal">Отзывы</p><h2 class="h2 reveal">Что говорят клиентки<br>и ученицы</h2></div>
    <p class="sub reveal">Настоящие сообщения из директа и Telegram. Нажмите «Скрин», чтобы увидеть оригинал.</p></div>
    {quotes([CLIENT_Q[0], CLIENT_Q[1], CLIENT_Q[2], STUDENT_Q[0], STUDENT_Q[1], STUDENT_Q[3]])}
  </div>
</section>
{CASE}
<section class="sec sec-soft">
  <div class="wrap">
    <p class="kick reveal">Частые вопросы</p><h2 class="h2 reveal">Коротко о главном</h2>
    {faq_html(FAQ_HOME)}
  </div>
</section>
{final('Запишитесь<br>или задайте вопрос', 'Короткая заявка займёт минуту. Отвечу лично в WhatsApp или Telegram.', [('Записаться', '/zapis/', 'btn-light'), ('Написать в Telegram', TG, 'btn-ghost')])}
'''
page('/', 'Anya Kay — Обучение и наращивание ресниц, Варшава',
     'Anya Kay: наращивание ресниц в Варшаве от 200 zł (Krucza 16/22) и обучение наращиванию с нуля и для мастеров. Курсы BASIC и VIP, повышение квалификации, пособие и онлайн-теория.',
     home, [faq_ld(FAQ_HOME)], cls='final-dark')

# ================= НАРАЩИВАНИЕ =================
lash = f'''
{cover('Наращивание', 'Наращивание ресниц в Варшаве', 'Продуманная техника, эффект под вашу форму глаз и комфортная носка. Центр Варшавы, Krucza 16/22.',
       [('90 мин', 'наращивание'), ('до 2 ч', 'вместе со снятием'), ('3–5 недель', 'носка'), ('от 200 zł', '1D–5D')],
       [('Записаться', '/zapis/?w=lashes', 'btn-light'), ('Есть вопрос?', '#faq', 'btn-ghost')])}
<div class="procedures-editorial">
  <section class="proc-price-section" style="padding-top:40px">
    <div class="wrap proc-price-grid">
      <div><h2 class="h2" style="color:var(--ivory);font-size:58px">Прайс</h2><p class="proc-price-note">Коррекции не делаю, только полное перенаращивание.</p></div>
      <div class="proc-prices">
        <div class="proc-price-row"><span>Наращивание · 1D–4D</span><strong>200 zł</strong></div>
        <div class="proc-price-row"><span>Наращивание · 5D</span><strong>230 zł</strong></div>
        <div class="proc-price-row"><span>Изгибы L / M</span><strong>+20 zł</strong></div>
        <div class="proc-price-row"><span>Снятие другого мастера <small>с последующим наращиванием</small></span><strong>+30 zł</strong></div>
      </div>
    </div>
  </section>
  <section class="proc-portfolio wrap">
    <div class="proc-section-head"><div><h2 class="h2">Портфолио</h2></div><p>Адаптивная техника · индивидуальный подбор эффекта · комфортное отрастание</p></div>
    {carousel([img('/img/lash-1.jpg', 'Наращивание ресниц, работа Anya Kay'), img('/img/lash-2.jpg', 'Наращивание ресниц в Варшаве, работа Anya Kay'), img('/img/lash-3.jpg', 'Эффект наращивания ресниц, работа Anya Kay'),
               vid('portfolio_1', 'Видео работы'), vid('portfolio_2', 'Видео работы'), vid('portfolio_3', 'Видео работы')], ' style="margin-bottom:70px"')}
  </section>
  <section class="proc-details">
    <div class="wrap proc-details-grid">
      <div><span>01</span><small>Адрес</small><strong>Krucza 16/22<br>Warszawa</strong></div>
      <div><span>02</span><small>Запись</small><strong>Сайт, Telegram,<br>WhatsApp, Instagram</strong></div>
      <div><span>03</span><small>Подход</small><strong>Эффект подбирается<br>индивидуально</strong></div>
    </div>
  </section>
</div>
<section class="sec">
  <div class="wrap">
    <div class="head-row"><div><p class="kick reveal">Отзывы</p><h2 class="h2 reveal">Что говорят клиентки</h2></div><p class="sub reveal">Оригинальные сообщения после процедуры и носки ресниц.</p></div>
    {quotes(CLIENT_Q[:3])}
  </div>
</section>
<section class="sec sec-soft" id="faq">
  <div class="wrap"><p class="kick reveal">Вопросы</p><h2 class="h2 reveal">Перед записью</h2>{faq_html(FAQ_LASH)}</div>
</section>
{final('Запись на наращивание', 'Выберите объём и удобное время. Подтвержу запись в WhatsApp или Telegram.', [('Выбрать время', '/zapis/?w=lashes', 'btn-light'), ('Telegram', TG + '?start=lashes', 'btn-ghost')])}
'''
page('/naraschivanie/', 'Наращивание ресниц в Варшаве · от 200 zł · Anya Kay',
     'Наращивание ресниц 1D–5D в центре Варшавы (Krucza 16/22): от 200 zł, 90 минут, носка 3–5 недель. Эффект подбирается индивидуально. Портфолио, отзывы, онлайн-запись.',
     lash, [faq_ld(FAQ_LASH), {"@type": "Service", "name": "Наращивание ресниц", "provider": {"@id": SITE + "/#business"}, "areaServed": "Warszawa",
            "offers": [{"@type": "Offer", "name": "Наращивание 1D–4D", "price": "200", "priceCurrency": "PLN"}, {"@type": "Offer", "name": "Наращивание 5D", "price": "230", "priceCurrency": "PLN"}]}],
     cls='final-dark', nav_on='/naraschivanie/')

# ================= ОБУЧЕНИЕ (хаб) =================
def trow(n, href, small, strong, em):
    return f'<a class="training-row reveal" href="{href}"><span class="training-num">{n}</span><span class="training-copy"><small>{small}</small><strong>{strong}</strong><em>{em}</em></span><span class="training-arrow">↗</span></a>'

edu = f'''
{cover('Обучение', 'Обучение наращиванию ресниц', 'Начать с нуля, усилить технику, разобрать конкретные ошибки или учиться самостоятельно. Обучаю тому, что использую в работе сама.',
       [('100+', 'учениц'), ('с 2017', 'в lash-индустрии'), ('3–6', 'живых моделей на курсе'), ('∞', 'поддержка после BASIC')], cls='to-dark')}
<section class="training-section" style="padding-top:20px">
  <div class="wrap training-wrap">
    <div class="training-head reveal"><p class="training-kicker">Обучение ANYA KAY</p><h2>Выберите формат<br>под свою задачу.</h2><p>Все форматы проходят в Варшаве или онлайн, программа строится вокруг практики.</p></div>
    <div class="training-list">
      {trow('01', '/basic-lash-course/', 'Хочу начать с нуля', 'Курс BASIC · 2800 zł', 'Сильная теория, практика на манекене и 3 живых моделях, сертификат.')}
      {trow('02', '/basic-lash-course/#vip', 'Хочу больше практики с нуля', 'Курс VIP · 4000 zł', '6 дней, 6 моделей, L/M-изгибы, 2 трендовых эффекта, стартовый набор.')}
      {trow('03', '/povyshenie-kvalifikacii/', 'Я уже работаю мастером', 'Повышение квалификации · 1000 zł / день', 'Индивидуальная программа после анализа работ и точек роста.')}
      {trow('04', '/konsultaciya/', 'Мне нужен индивидуальный разбор', 'Онлайн-консультация · 500 zł', 'Работы, ошибки, профессиональные вопросы и старт преподавания.')}
      {trow('05', '/materialy/', 'Хочу учиться самостоятельно', 'Онлайн-теория и пособие · от 200 zł', 'Теория BASIC в Telegram и готовое пособие для мастеров.')}
    </div>
    <div class="training-help reveal"><span>Не знаете, какой формат выбрать?</span><a href="#" data-faq>Подобрать обучение ↗</a></div>
  </div>
</section>
<div style="height:140px;background:linear-gradient(180deg,var(--burgundy-dark),#9b6673 55%,var(--ivory))"></div>
<section class="sec" style="padding-top:40px">
  <div class="wrap">
    <p class="kick reveal">Почему у меня</p><h2 class="h2 reveal">Понимание техники,<br>а не повторение</h2>
    <div class="for-grid reveal">
      <div><span>01</span><strong>Сильная теория до практики</strong><p>Уроки в Telegram в своём темпе, тест после каждого урока и итоговая проверка перед практикой.</p></div>
      <div><span>02</span><strong>Много практики на живых моделях</strong><p>Вы сами наращиваете под моим контролем: 3 модели на BASIC, 6 на VIP.</p></div>
      <div><span>03</span><strong>Поддержка после курса</strong><p>Присылаете работы и вопросы, я отвечаю. База и пособие остаются у вас.</p></div>
    </div>
  </div>
</section>
<section class="sec sec-dark">
  <div class="wrap">
    <div class="head-row"><div><p class="kick reveal">Ученицы</p><h2 class="h2 reveal">Что говорят ученицы</h2></div><p class="sub reveal">Сообщения после обучения, без правок.</p></div>
    {quotes(STUDENT_Q[:3])}
  </div>
</section>
{CASE}
<section class="sec sec-soft"><div class="wrap"><p class="kick reveal">Вопросы</p><h2 class="h2 reveal">Об обучении</h2>{faq_html(FAQ_EDU)}</div></section>
{final('Выберите формат<br>и запишитесь', 'Расскажите о своём опыте и удобных датах, предложу подходящий вариант.', [('Записаться на обучение', '/zapis/?k=obuchenie', 'btn-light'), ('Задать вопрос', TG, 'btn-ghost')])}
'''
page('/obuchenie/', 'Обучение наращиванию ресниц в Варшаве · курсы с нуля и для мастеров · Anya Kay',
     'Обучение наращиванию ресниц в Варшаве у Anya Kay: курс с нуля BASIC (2800 zł) и VIP (4000 zł), повышение квалификации, онлайн-консультация, теория в Telegram. 100+ учениц.',
     edu, [faq_ld(FAQ_EDU)], cls='final-dark', nav_on='/obuchenie/')

# ================= BASIC / VIP =================
basic = f'''
{cover('<a href="/obuchenie/">Обучение</a> · BASIC LASH COURSE', 'Курс наращивания ресниц с нуля', 'Для тех, кто хочет не просто научиться наращивать, а понимать, что и почему делает в работе.',
       [('3 / 6', 'дней практики'), ('21 ч', 'практики на BASIC'), ('3 / 6', 'живых моделей'), ('✓', 'именной сертификат')],
       [('Записаться на BASIC', '/zapis/?w=basic', 'btn-light'), ('Записаться на VIP', '/zapis/?w=vip', 'btn-ghost')])}
<div class="wrap panel-inner" style="padding-top:30px">
  <p class="kick">Тарифы</p><h2 class="h2">BASIC LASH COURSE</h2>
  <div class="tariff-grid">
    <div class="tariff-card">
      <div class="tariff-name">Basic</div>
      <div class="tariff-duration">3 дня · 21 час практики · 3 модели</div>
      <div class="tariff-price">2800 <span>zł</span></div>
      <ul class="tariff-list">
        <li>Углублённая теория в Telegram-боте</li>
        <li>Практика на 3D-манекене и 3 живых моделях</li>
        <li>Моделирование и схемы актуальных эффектов</li>
        <li>Базовое пособие + дополнительные гайды</li>
        <li>Неограниченная поддержка после обучения</li>
        <li>Именной сертификат с печатью</li>
      </ul>
      <p class="tariff-for"><b>Бонус:</b> курс по обработке контента и ретуши фото.</p>
      <a href="/zapis/?w=basic" class="btn btn-outline" style="width:100%; text-align:center;">Записаться на курс</a>
    </div>
    <div class="tariff-card featured prod-anchor" id="vip">
      <span class="featured-badge">VIP</span>
      <div class="tariff-name">VIP</div>
      <div class="tariff-duration">6 дней практики</div>
      <div class="tariff-price">4000 <span>zł</span></div>
      <p class="tariff-for" style="margin-top:12px;"><b>Всё из BASIC + в два раза больше практики</b></p>
      <ul class="tariff-list">
        <li>6 моделей для практики вместо 3</li>
        <li>Отработка L- и M-изгибов</li>
        <li>2 трендовых эффекта на выбор</li>
        <li>Стартовый набор материалов</li>
        <li>Кубок VIP-мастера</li>
      </ul>
      <a href="/zapis/?w=vip" class="btn btn-primary" style="width:100%; text-align:center;">Записаться на VIP</a>
    </div>
  </div>
  <div style="margin-top:70px">
    <p class="kick reveal">Сравнение</p><h2 class="h2 reveal" style="font-size:clamp(30px,4vw,44px)">BASIC или VIP</h2>
    <table class="cmp reveal">
      <thead><tr><th></th><th>Basic</th><th class="vip">VIP</th></tr></thead>
      <tbody>
        <tr><td>Дней практики</td><td>3</td><td class="vip">6</td></tr>
        <tr><td>Живые модели</td><td>3</td><td class="vip">6</td></tr>
        <tr><td>Теория в Telegram, тесты, пособие</td><td>✓</td><td class="vip">✓</td></tr>
        <tr><td>Моделирование и схемы эффектов</td><td>✓</td><td class="vip">✓ + 2 трендовых</td></tr>
        <tr><td>L- и M-изгибы</td><td>—</td><td class="vip">✓</td></tr>
        <tr><td>Стартовый набор материалов</td><td>—</td><td class="vip">✓</td></tr>
        <tr><td>Сертификат и поддержка</td><td>✓</td><td class="vip">✓</td></tr>
        <tr><td>Стоимость</td><td>2800 zł</td><td class="vip">4000 zł</td></tr>
      </tbody>
    </table>
  </div>
</div>
<div class="dark-block-full">
  <div class="wrap">
    <div class="process-head"><p class="eyebrow">Как проходит</p><h2 class="process-title">обучение <span>шаг за шагом</span></h2><p class="process-subtitle">От теории в Telegram до практики на моделях.</p></div>
    <div class="steps">
      <div class="step"><div class="step-num">01</div><div><div class="step-title">Теория в Telegram</div><div class="step-desc">В своём темпе</div></div></div>
      <div class="step"><div class="step-num">02</div><div><div class="step-title">Тесты</div><div class="step-desc">После каждого урока</div></div></div>
      <div class="step"><div class="step-num">03</div><div><div class="step-title">Пособие</div><div class="step-desc">Вся база остаётся у вас</div></div></div>
      <div class="step"><div class="step-num">04</div><div><div class="step-title">Итоговая проверка</div><div class="step-desc">Перед практикой</div></div></div>
      <div class="step"><div class="step-num">05</div><div><div class="step-title">Практика</div><div class="step-desc">3 или 6 живых моделей</div></div></div>
      <div class="step"><div class="step-num">06</div><div><div class="step-title">Сертификат</div><div class="step-desc">После завершения обучения</div></div></div>
    </div>
    <div style="max-width:900px;margin:80px auto 0">
      <p class="kick" style="color:var(--gold-light)">Программа теории</p>
      <h2 class="h2" style="color:var(--ivory);font-size:clamp(32px,4.4vw,48px)">16 уроков до практики</h2>
      <ol class="lessons">{''.join(f'<li><b>{i:02d}</b>{e(t)}</li>' for i, t in enumerate(LESSONS))}</ol>
    </div>
    <div class="video-grid" style="margin-top:60px;">
      <div class="video-card">{vid('process_1', 'Практика на курсе')}<p class="video-caption" style="color:rgba(243,233,225,0.75);">Практика на курсе</p></div>
      <div class="video-card">{vid('process_2', 'Практика на курсе')}<p class="video-caption" style="color:rgba(243,233,225,0.75);">Практика на курсе</p></div>
    </div>
  </div>
</div>
<div class="wrap panel-inner" style="padding-top:70px;">
  <p class="eyebrow">Результаты учениц</p>
  <h2 class="section-title" style="font-size:30px;">Работы учениц после BASIC</h2>
  <p class="section-intro">Результаты, выполненные ученицами во время и после обучения.</p>
  {carousel([img(f'/img/uchenica-basic-{i}.jpg', 'Работа ученицы после курса наращивания ресниц') for i in range(1, 5)])}
  <div id="course-reviews" style="margin-top:70px;">
    <p class="eyebrow">Отзывы</p>
    <h2 class="section-title" style="font-size:30px;">Что говорят ученицы</h2>
    <div class="video-grid">
      <div class="video-card">{vid('testimonial_1', 'Отзыв ученицы Насти')}<p class="video-caption"><b>Настя</b> прилетела на курс из Швеции, 6 дней обучения</p></div>
      <div class="video-card">{vid('testimonial_2', 'Отзыв ученицы Арины')}<p class="video-caption"><b>Арина</b>, курс 6 дней</p></div>
    </div>
    {quotes(STUDENT_Q)}
  </div>
</div>
{CASE}
<section class="sec sec-soft"><div class="wrap"><p class="kick reveal">Вопросы</p><h2 class="h2 reveal">О курсе</h2>{faq_html(FAQ_EDU[:4])}</div></section>
{final('Запишитесь на курс', 'Напишите, какой формат и месяц вам удобны, расскажу о ближайших датах.', [('Записаться на BASIC', '/zapis/?w=basic', 'btn-light'), ('Записаться на VIP', '/zapis/?w=vip', 'btn-ghost')])}
'''
page('/basic-lash-course/', 'Курс наращивания ресниц с нуля в Варшаве · BASIC и VIP · Anya Kay',
     'Курс наращивания ресниц с нуля в Варшаве: BASIC 3 дня, 3 живые модели, 2800 zł; VIP 6 дней, 6 моделей, 4000 zł. Теория в Telegram, сертификат, поддержка после обучения.',
     basic, [faq_ld(FAQ_EDU[:4]), course_ld('BASIC LASH COURSE', 'Курс наращивания ресниц с нуля: теория в Telegram, 3 дня практики, 3 живые модели, сертификат.', '2800', '/basic-lash-course/'),
             course_ld('VIP LASH COURSE', 'Курс наращивания ресниц с нуля: 6 дней практики, 6 моделей, L/M-изгибы, 2 трендовых эффекта, стартовый набор.', '4000', '/basic-lash-course/#vip')],
     cls='final-dark', nav_on='/obuchenie/')

# ================= ПОВЫШЕНИЕ =================
adv = f'''
{cover('<a href="/obuchenie/">Обучение</a> · Для мастеров', 'Повышение квалификации', 'Сначала разбираю ваши работы, потом составляю программу обучения. Только то, что нужно именно вам.',
       [('1000 zł', 'за день'), ('1 день', 'стандартно'), ('до 5D', 'объёмы'), ('1:1', 'индивидуально')],
       [('Записаться', '/zapis/?w=advanced', 'btn-light'), ('Сначала консультация', '/konsultaciya/', 'btn-ghost')])}
<section class="sec" style="padding-top:40px">
  <div class="wrap">
    <p class="kick reveal">Что прорабатываем</p><h2 class="h2 reveal">Ваши точки роста</h2>
    <div class="topic-tags reveal" style="margin-bottom:60px">{''.join(f'<span class="topic-tag">{t}</span>' for t in ['Ошибки в технике', 'Скорость', 'Объёмы до 5D', 'Моделирование', 'Эффекты'])}</div>
    <div class="for-grid reveal">
      <div><span>01</span><strong>Присылаете работы</strong><p>Фото ваших наращиваний: так я вижу, на каком вы уровне и что мешает.</p></div>
      <div><span>02</span><strong>Разбор и программа</strong><p>Нахожу ошибки и точки роста, составляю программу под них.</p></div>
      <div><span>03</span><strong>Практика</strong><p>Стандартно 1 день. При необходимости программу можно расширить.</p></div>
    </div>
  </div>
</section>
<section class="sec sec-soft">
  <div class="wrap">
    <p class="kick reveal">Результаты</p><h2 class="h2 reveal">Работы после повышения квалификации</h2>
    {carousel([img('/img/povyshenie-1.jpg', 'Работа мастера после повышения квалификации'), img('/img/povyshenie-2.jpg', 'Работа мастера после повышения квалификации'), vid('advanced_1', 'Работа после повышения квалификации')])}
  </div>
</section>
<section class="sec sec-dark"><div class="wrap"><p class="kick">Отзыв</p>{quotes([STUDENT_Q[2], STUDENT_Q[0]])}</div></section>
<section class="sec"><div class="wrap"><p class="kick reveal">Вопросы</p><h2 class="h2 reveal">Повышение квалификации</h2>{faq_html(FAQ_ADV)}</div></section>
{final('Разберём ваши работы', 'Напишите, что хотите улучшить, и пришлите пару работ. Предложу программу.', [('Записаться', '/zapis/?w=advanced', 'btn-light'), ('Telegram', TG + '?start=advanced', 'btn-ghost')])}
'''
page('/povyshenie-kvalifikacii/', 'Повышение квалификации lash-мастера в Варшаве · Anya Kay',
     'Повышение квалификации для lash-мастеров в Варшаве: разбор ваших работ и индивидуальная программа. Техника, скорость, объёмы до 5D, моделирование, эффекты. 1000 zł / день.',
     adv, [faq_ld(FAQ_ADV), course_ld('Повышение квалификации lash-мастера', 'Индивидуальная программа после разбора работ: техника, скорость, объёмы до 5D, моделирование, эффекты.', '1000', '/povyshenie-kvalifikacii/')],
     cls='final-dark', nav_on='/obuchenie/')

# ================= КОНСУЛЬТАЦИЯ =================
kons = f'''
{cover('<a href="/obuchenie/">Обучение</a> · Онлайн', 'Онлайн-консультация для lash-мастеров', 'Разберём ваши работы, найдём ошибки и определим, что именно мешает двигаться дальше.',
       [('500 zł', 'стоимость'), ('2 часа', 'онлайн'), ('1:1', 'лично с Аней')],
       [('Записаться на консультацию', '/zapis/?w=consultation', 'btn-light')])}
<section class="sec" style="padding-top:40px">
  <div class="wrap">
    <div class="offer-block">
      <div class="offer-left">
        <p class="kick reveal">Что можно разобрать</p>
        <div class="topic-tags reveal">{''.join(f'<span class="topic-tag">{t}</span>' for t in ['Технику', 'Носку', 'Скорость', 'Клей', 'Пучки', 'Программу своего курса', 'Старт преподавания', 'Поиск учениц'])}</div>
        <p class="sub reveal" style="margin-top:30px">Если после консультации станет понятно, что нужна практика, можно продолжить на <a class="more" href="/povyshenie-kvalifikacii/">повышении квалификации ↗</a></p>
      </div>
      <div class="offer-right reveal">
        <div class="offer-price">500 zł</div>
        <div class="offer-price-note">2 часа · онлайн</div>
        <a href="/zapis/?w=consultation" class="btn btn-primary" style="width:100%; text-align:center;">Записаться</a>
      </div>
    </div>
  </div>
</section>
{final('Готовы разобрать работы?', 'Оставьте заявку, договоримся о времени созвона.', [('Записаться', '/zapis/?w=consultation', 'btn-light'), ('Telegram', TG + '?start=consultation', 'btn-ghost')])}
'''
page('/konsultaciya/', 'Онлайн-консультация для lash-мастеров · разбор работ · Anya Kay',
     'Онлайн-консультация для мастеров по наращиванию ресниц: 2 часа, 500 zł. Разбор работ, ошибок, носки, скорости, клея, программы курса и старта преподавания.',
     kons, [{"@type": "Service", "name": "Онлайн-консультация для lash-мастеров", "provider": {"@id": SITE + "/#business"}, "offers": {"@type": "Offer", "price": "500", "priceCurrency": "PLN"}}],
     cls='final-dark', nav_on='/obuchenie/')

# ================= МАТЕРИАЛЫ =================
posobie_alts = ['Обложка пособия', 'Содержание пособия', 'Страница пособия: рабочее место', 'Страница пособия: работа с клеем', 'Страница пособия: наращивание на анагены', 'Страница пособия: ожог слизистой']
teor_alts = ['Anya Kay Basic Lash в Telegram', 'Урок в Telegram', 'Тест после урока', 'Видеоурок']
mat = f'''
{cover('Материалы', 'Пособие и онлайн-теория по наращиванию', 'Для мастеров, которые хотят систематизировать базу, и преподавателей, которым нужна готовая основа для курса.',
       [('51', 'страница в пособии'), ('16', 'уроков онлайн'), ('от 200 zł', 'стоимость')])}
<div class="wrap panel-inner" style="padding-top:30px">
  <div class="products-grid">
    <div class="product-card prod-anchor" id="posobie">
      <h2 class="product-title">Базовое пособие</h2>
      <div class="product-price">200 zł</div>
      {carousel([img(f'/img/posobie-{i+1}.jpg', a) for i, a in enumerate(posobie_alts)])}
      <p class="product-desc"><b>51 страница углублённой теории по наращиванию ресниц.</b></p>
      <p class="product-desc">Полностью редактируется в Canva · без водяных знаков · подходит для печати.</p>
      <p class="product-desc">Для мастеров, которые хотят систематизировать базу, и преподавателей, которым нужна готовая основа для собственного курса.</p>
      <a href="/zapis/?w=manual" class="btn btn-primary">Купить пособие</a>
    </div>
    <div class="product-card prod-anchor" id="teoriya">
      <h2 class="product-title">Теория BASIC в Telegram</h2>
      <div class="product-price">500 zł</div>
      {carousel([img(f'/img/teoriya-{i+1}.jpg', a) for i, a in enumerate(teor_alts)])}
      <p class="product-desc"><b>Весь теоретический блок BASIC LASH COURSE в самостоятельном online-формате.</b></p>
      <p class="product-desc" style="font-weight:700; letter-spacing:.04em;">УРОК → ТЕСТ → СЛЕДУЮЩИЙ УРОК → ФИНАЛЬНАЯ ПРОВЕРКА</p>
      <p class="product-desc"><b>Внутри:</b> видеоуроки · базовое пособие · тесты · прогресс · дополнительные гайды · курс по контенту.</p>
      <p class="product-desc">Для мастеров, которые уже проходили практическое обучение, но хотят закрыть пробелы и систематизировать теорию.</p>
      <details style="margin:18px 0 22px;">
        <summary style="cursor:pointer; font-weight:700; color:var(--burgundy);">Посмотреть программу курса ↓</summary>
        <ul class="tariff-list" style="margin-bottom:22px;">{''.join(f'<li>Урок {i}. {e(t)}</li>' for i, t in enumerate(LESSONS))}</ul>
      </details>
      <a href="/zapis/?w=theory" class="btn btn-primary">Купить доступ</a>
    </div>
  </div>
</div>
<section class="sec sec-soft"><div class="wrap"><p class="kick reveal">Вопросы</p><h2 class="h2 reveal">О материалах</h2>{faq_html(FAQ_MAT)}</div></section>
{final('Хотите больше практики?', 'Теорию можно продолжить на курсе BASIC или VIP с живыми моделями.', [('Курс с нуля', '/basic-lash-course/', 'btn-light'), ('Задать вопрос', TG, 'btn-ghost')])}
'''
page('/materialy/', 'Пособие и онлайн-теория по наращиванию ресниц · Anya Kay',
     'Материалы для lash-мастеров от Anya Kay: базовое пособие на 51 страницу (редактируется в Canva, 200 zł) и теория BASIC в Telegram: 16 уроков с тестами (500 zł).',
     mat, [faq_ld(FAQ_MAT), {"@type": "Product", "name": "Базовое пособие по наращиванию ресниц", "description": "51 страница углублённой теории, редактируется в Canva.", "brand": {"@type": "Brand", "name": "Anya Kay"},
           "offers": {"@type": "Offer", "price": "200", "priceCurrency": "PLN", "availability": "https://schema.org/InStock", "url": SITE + "/materialy/"}},
           course_ld('Теория BASIC в Telegram', '16 видеоуроков с тестами и финальной проверкой, пособие и гайды.', '500', '/materialy/#online')],
     cls='final-dark', nav_on='/materialy/')

# ================= ЗАПИСЬ =================
zap = f'''
{cover('Запись', 'Запись и вопросы', 'Короткая заявка за минуту. В конце сообщение откроется в WhatsApp или Telegram, останется нажать «Отправить».')}
<section class="sec" style="padding-top:20px">
  <div class="wrap zapis"><div class="fapp" id="fapp"><noscript>Напишите мне в <a href="{TG}">Telegram</a> или <a href="{WA}">WhatsApp</a>.</noscript></div></div>
</section>
<section class="proc-details">
  <div class="wrap proc-details-grid">
    <div><span>01</span><small>Адрес</small><strong><a href="https://www.google.com/maps/search/?api=1&query=Krucza+16%2F22+Warszawa" target="_blank" rel="noopener">Krucza 16/22<br>Warszawa ↗</a></strong></div>
    <div><span>02</span><small>Написать напрямую</small><strong><a href="{TG}" target="_blank" rel="noopener">Telegram</a> · <a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></strong></div>
    <div><span>03</span><small>Instagram</small><strong><a href="{IG}" target="_blank" rel="noopener">@anya.key_</a></strong></div>
  </div>
</section>
'''
page('/zapis/', 'Запись на наращивание ресниц и обучение · Anya Kay, Варшава',
     'Онлайн-запись к Anya Kay: наращивание ресниц в Варшаве, курсы BASIC и VIP, повышение квалификации, консультация, пособие. Заявка уходит в WhatsApp или Telegram.',
     zap, cls='bar-off')

# ================= ПОЛИТИКА =================
pol = f'''
{cover('Политика конфиденциальности', 'Политика конфиденциальности', 'Коротко и понятно: какие данные я получаю через сайт и как их использую. В соответствии с RODO (GDPR).')}
<section class="sec" style="padding-top:20px"><div class="wrap" style="max-width:760px">
<div class="sub" style="max-width:none">
<h2 class="h2" style="font-size:30px">1. Кто отвечает за данные</h2>
<p>Администратор персональных данных: Anya Kay, Krucza 16/22, Warszawa, Polska. Связь: <a href="{WA}">WhatsApp +48 788 214 369</a>, <a href="{TG}">Telegram</a>.</p><br>
<h2 class="h2" style="font-size:30px">2. Какие данные и зачем</h2>
<p>Через форму записи и помощник на сайте вы сами составляете сообщение (имя, телефон или ник, выбранная услуга, комментарий) и отправляете его мне в WhatsApp или Telegram. Сайт не сохраняет эти данные на сервере. Я использую их только чтобы ответить вам, записать на процедуру или обучение и выставить счёт (основание: art. 6 ust. 1 lit. b i f RODO).</p><br>
<h2 class="h2" style="font-size:30px">3. Сколько храню</h2>
<p>Переписку храню, пока она нужна для записи и обслуживания, данные для счетов столько, сколько требует польское налоговое право.</p><br>
<h2 class="h2" style="font-size:30px">4. Кому передаются</h2>
<p>Данные не продаются и не передаются третьим лицам для рекламы. Сообщения проходят через сервисы, которые вы выбираете сами: WhatsApp (Meta) и Telegram. Сайт подключает шрифты Google Fonts.</p><br>
<h2 class="h2" style="font-size:30px">5. Ваши права</h2>
<p>Вы можете запросить доступ к своим данным, их исправление или удаление, ограничить обработку или возразить против неё, а также подать жалобу в Prezes Urzędu Ochrony Danych Osobowych (UODO). Для этого просто напишите мне.</p><br>
<h2 class="h2" style="font-size:30px">6. Cookies</h2>
<p>Сайт не использует рекламные и аналитические cookies.</p>
</div></div></section>
'''
page('/politika-konfidencialnosti/', 'Политика конфиденциальности · Anya Kay',
     'Политика конфиденциальности сайта anyakay.pl: какие данные обрабатываются при записи и как, в соответствии с RODO (GDPR).', pol)

# ================= 404 =================
nf = f'''
{cover('', 'Такой страницы нет', 'Возможно, ссылка устарела. Вот куда можно перейти:', None,
       [('На главную', '/', 'btn-light'), ('Наращивание', '/naraschivanie/', 'btn-ghost'), ('Обучение', '/obuchenie/', 'btn-ghost')])}
'''
page('/404.html', 'Страница не найдена · Anya Kay', 'Страница не найдена.', nf)
# 404 не индексируем
p404 = os.path.join(OUT, '404.html')
s = open(p404, encoding='utf-8').read().replace('<link rel="canonical" href="https://anyakay.pl/404.html">', '<meta name="robots" content="noindex">')
open(p404, 'w', encoding='utf-8').write(s)

# ================= статика =================
css = open(os.path.join(B, 'base.css'), encoding='utf-8').read() + open(os.path.join(B, 'extra.css'), encoding='utf-8').read()
css += '\n.cover.to-dark{background:linear-gradient(180deg,var(--burgundy-darker) 0%,var(--burgundy-dark) 100%);padding-bottom:60px;}\n'
open(os.path.join(OUT, 'style.css'), 'w', encoding='utf-8').write(css)
shutil.copy(os.path.join(B, 'app.js'), os.path.join(OUT, 'app.js'))
if os.path.isdir(os.path.join(B, 'img')):
    shutil.copytree(os.path.join(B, 'img'), os.path.join(OUT, 'img'), dirs_exist_ok=True)
open(os.path.join(OUT, 'CNAME'), 'w').write('anyakay.pl')
open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
URLS = [('/', '1.0'), ('/naraschivanie/', '0.9'), ('/obuchenie/', '0.9'), ('/basic-lash-course/', '0.9'), ('/povyshenie-kvalifikacii/', '0.8'),
        ('/konsultaciya/', '0.7'), ('/materialy/', '0.7'), ('/zapis/', '0.6'), ('/politika-konfidencialnosti/', '0.2')]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'  <url><loc>{SITE}{u}</loc><lastmod>2026-11-03</lastmod><priority>{p}</priority></url>\n' for u, p in URLS) + '</urlset>\n'
open(os.path.join(OUT, 'sitemap.xml'), 'w').write(sm)
print('ok')
