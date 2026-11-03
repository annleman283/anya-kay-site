#!/usr/bin/env python3
"""Сборка anyakay.pl (версия 2, стиль «стекло и бордо»).
Запуск из корня репозитория:  python3 -I _build/build.py .
Тексты и цены правятся здесь. Даты курсов: в Google Таблице (SHEET_CSV) или в DATES ниже."""
import json, os, sys, html

B = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
SITE = 'https://anyakay.pl'
V = '50'
TG_I, WA_I, IG_I = json.load(open(os.path.join(B, 'svgs.json')))
TG = 'https://t.me/AnyaKayClientBot'
WA = 'https://wa.me/48788214369'
IG = 'https://www.instagram.com/anya.key_/'
MAP = 'https://www.google.com/maps/search/?api=1&query=Krucza+16%2F22+Warszawa'

# ---------- даты курсов (запасной вариант, если таблица недоступна) ----------
SHEET_CSV = ''
DATES = [
    {'c': 'basic', 'a': '2026-11-18', 'b': '2026-11-20', 'i': '2800', 'g': '', 'n': 'скидка'},
    {'c': 'basic', 'a': '2026-12-07', 'b': '2026-12-09', 'i': '3000', 'g': '2000', 'n': ''},
    {'c': 'vip', 'a': '2027-01-11', 'b': '2027-01-16', 'i': '4500', 'g': '3000', 'n': ''},
]
GROUP = 'Индивидуально или в мини-группе до 2 человек. Если на дату кто-то записывается индивидуально, группы на эту дату не будет.'
RISE = 'С 1 декабря 2026 цены на наращивание повышаются на 20 zł: 1D–4D будет 220 zł, 5D 250 zł. Запишитесь в ноябре по текущей цене.'


def e(s):
    return html.escape(s, quote=True)


# ---------- отзывы-скрины ----------
# (файл, имя, подпись, перевод)
OP_CLIENT = [
    ('otzyv-klient-4.jpg', 'Клиентка', 'после наращивания', ''),
    ('otzyv-klient-3.jpg', 'Клиентка', 'после наращивания', ''),
    ('otzyv-klient-2.jpg', 'Клиентка', 'после отпуска', ''),
    ('otzyv-klient-1.jpg', 'Марина', 'сторис в Instagram', ''),
]
OP_STUD = [
    ('otzyv-uchenica-praktika.jpg', 'Ученица', 'после курса', ''),
    ('otzyv-karina.jpg', 'Карина', 'ученица', ''),
    ('otzyv-sveta.jpg', 'Света', 'ученица', ''),
    ('otzyv-nastya.jpg', 'Настя', 'ученица', ''),
    ('otzyv-yana.jpg', 'Яна', 'ученица VIP, 6 дней', 'Хочу ещё раз поблагодарить за эти 6 дней. Они пролетели как 5 минут. Я бы ещё раз записалась к тебе на VIP-курс.'),
]


def ops(items):
    out = []
    for f, who, note, tr in items:
        t = f'<details class="tr"><summary>Перевод с украинского</summary><p>{e(tr)}</p></details>' if tr else ''
        out.append(f'<figure class="op"><button type="button" data-shot="{f}" data-alt="Отзыв: {e(who)}" aria-label="Открыть отзыв: {e(who)}"><img src="/img/{f}" alt="Отзыв: {e(who)}, {e(note)}" loading="lazy"></button>'
                   f'<figcaption><b>{e(who)}</b> · {e(note)}{t}</figcaption></figure>')
    return f'<div class="ops wrap n{len(items)}">' + ''.join(out) + '</div>'


# ---------- вопросы ----------
FAQ_LASH = [
    ('Сколько стоит наращивание ресниц?', 'Наращивание 1D–4D стоит 200 zł, 5D 230 zł. Изгибы L / M +20 zł. Снятие ресниц другого мастера с последующим наращиванием +30 zł. ' + RISE),
    ('Сколько длится процедура?', 'Само наращивание около 90 минут, вместе со снятием до 2 часов.'),
    ('Сколько держатся ресницы?', 'Носка 3–5 недель. Техника рассчитана на комфортное и аккуратное отрастание.'),
    ('Делаете коррекцию?', 'Коррекции не делаю, только полное перенаращивание. Так результат каждый раз свежий и аккуратный.'),
    ('Как выбрать эффект?', 'Эффект подбирается индивидуально: по форме глаз, состоянию ваших ресниц и тому, какой образ вам ближе. Можно прийти без идеи, подберём вместе.'),
    ('Где проходит процедура?', 'В центре Варшавы, Krucza 16/22. Запись через сайт, Telegram, WhatsApp или Instagram.'),
]
FAQ_EDU = [
    ('Можно учиться с нуля?', 'Да. BASIC и VIP рассчитаны на старт с нуля: сначала теория в Telegram в своём темпе с тестами после уроков, потом практика на 3D-манекене и живых моделях.'),
    ('Чем VIP отличается от BASIC?', 'VIP включает всё из BASIC и в два раза больше практики: 6 дней и 6 моделей вместо 3, отработку L- и M-изгибов, 2 трендовых эффекта на выбор, стартовый набор материалов и кубок VIP-мастера.'),
    ('Индивидуально или в группе: в чём разница?', 'Программа одна и та же. Индивидуально всё время только ваше, и темп подстраивается под вас. В мини-группе максимум 2 человека, поэтому внимания всё равно много, а цена ниже: BASIC 2000 zł вместо 3000 zł, VIP 3000 zł вместо 4500 zł с человека. Если на дату кто-то записывается индивидуально, группы не будет.'),
    ('Выдаёте сертификат?', 'Да, после обучения вы получаете именной сертификат с печатью.'),
    ('Будет поддержка после курса?', 'Да, после BASIC у вас неограниченная поддержка: можно присылать работы и задавать вопросы.'),
    ('Сколько можно зарабатывать после курса?', 'Зависит от вас, но вот пример: ученица Света за первые 2,5 недели после обучения обслужила 9 клиенток и заработала 800 zł, параллельно работая на заводе. Её модели возвращаются и становятся постоянными клиентками.'),
    ('Я уже работаю мастером. Что мне подойдёт?', 'Повышение квалификации: сначала я разбираю ваши работы, потом составляю программу под ваши ошибки и точки роста. Если нужен только разбор, подойдёт онлайн-консультация на 2 часа.'),
]
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
FAQ_HOME = [FAQ_LASH[0], FAQ_LASH[2], FAQ_EDU[0], FAQ_EDU[1], FAQ_EDU[2]]
LESSONS = ['Знакомство и организационные моменты', 'Строение ресниц', 'Материалы 1.0', 'Материалы 2.0', 'Организация рабочего места', 'Виды ресниц',
           'Правила наращивания', 'Клей, часть 1', 'Клей, часть 2', 'Моделирование взгляда', 'Работа с рядами', 'Снятие ресниц', 'Коррекция ресниц',
           'Ожог слизистой', 'Аллергия мастера и клиента', 'Стерилизация инструментов']

# вопросы помощника: тема, вопрос, ключевые слова, ответ, кнопка записи
CHAT = [
    ('lashes', FAQ_LASH[0][0], ['стоит', 'цена', 'цены', 'прайс', 'стоимость', 'наращивание'], FAQ_LASH[0][1], 'lashes'),
    ('lashes', 'Цены повысятся?', ['повыш', 'декабр', 'подорож', 'дороже'], RISE, 'lashes'),
    ('lashes', FAQ_LASH[1][0], ['длится', 'по времени', 'часа', 'долго'], FAQ_LASH[1][1], 'lashes'),
    ('lashes', FAQ_LASH[2][0], ['держатся', 'носка', 'носятся', 'недел'], FAQ_LASH[2][1], 'lashes'),
    ('lashes', FAQ_LASH[3][0], ['коррекц'], FAQ_LASH[3][1], 'lashes'),
    ('lashes', FAQ_LASH[4][0], ['эффект', 'выбрать', 'подобрать', 'объём', 'объем'], FAQ_LASH[4][1], 'lashes'),
    ('lashes', 'Снимаете ресницы другого мастера?', ['сним', 'снятие', 'другого мастера'], 'Да. Снятие ресниц другого мастера с последующим наращиванием +30 zł. Отметьте это в заявке, чтобы я заложила время.', 'lashes'),
    ('lashes', 'Что такое изгибы L / M?', ['изгиб', ' l ', ' m ', 'l/m', 'l / m'], 'Это изгибы с прямым основанием и подъёмом на кончике. Они раскрывают взгляд, особенно при прямых или опущенных ресницах. Стоят +20 zł к наращиванию.', 'lashes'),
    ('obuchenie', 'Ближайшие даты курсов?', ['дата', 'даты', 'когда', 'ближайш', 'поток', 'старт'], '@dates', 'basic'),
    ('obuchenie', 'Сколько стоит обучение?', ['стоит обучение', 'цена курса', 'стоимость курса', 'сколько курс', 'цена обучения'], 'BASIC: 3000 zł индивидуально или 2000 zł с человека в мини-группе. VIP «мастер под ключ»: 4500 zł индивидуально или 3000 zł с человека в группе. Повышение квалификации 1000 zł за день, онлайн-консультация 500 zł.', 'any'),
    ('obuchenie', FAQ_EDU[0][0], ['с нуля', 'нуля', 'новичок', 'без опыта', 'начинающ'], FAQ_EDU[0][1], 'basic'),
    ('obuchenie', FAQ_EDU[1][0], ['vip', 'вип', 'отличается', 'разница'], FAQ_EDU[1][1], 'vip'),
    ('obuchenie', FAQ_EDU[2][0], ['групп', 'индивидуально', 'вдвоём', 'вдвоем'], FAQ_EDU[2][1], 'basic'),
    ('obuchenie', FAQ_EDU[3][0], ['сертификат', 'диплом'], FAQ_EDU[3][1], 'basic'),
    ('obuchenie', FAQ_EDU[4][0], ['поддержк', 'после курса', 'после обучения'], FAQ_EDU[4][1], 'basic'),
    ('obuchenie', FAQ_EDU[5][0], ['зарабат', 'заработ', 'доход', 'окупит'], FAQ_EDU[5][1], 'basic'),
    ('obuchenie', 'Поможете найти первых клиенток?', ['клиентк', 'первых', 'найти клиент', 'продвиж', 'контент'], 'В BASIC входит бонусный курс по обработке контента и ретуши фото: как снимать работы и оформлять их так, чтобы к вам приходили клиентки. А ещё модели с курса часто становятся первыми постоянными клиентками.', 'basic'),
    ('obuchenie', FAQ_EDU[6][0], ['уже мастер', 'работаю мастером', 'повышени', 'квалификац'], FAQ_EDU[6][1], 'advanced'),
    ('obuchenie', 'Что такое онлайн-консультация?', ['консультац', 'разбор', 'созвон'], 'Это 2 часа онлайн лично со мной, 500 zł. Разбираем ваши работы, ошибки, носку, скорость, клей, программу своего курса или старт преподавания.', 'consultation'),
    ('materialy', FAQ_MAT[0][0], ['пособи', 'страниц'], FAQ_MAT[0][1], 'manual'),
    ('materialy', FAQ_MAT[1][0], ['canva', 'канва', 'редактир', 'печат'], FAQ_MAT[1][1], 'manual'),
    ('materialy', FAQ_MAT[2][0], ['telegram', 'телеграм', 'онлайн', 'теори', 'урок'], FAQ_MAT[2][1], 'theory'),
    ('materialy', FAQ_MAT[3][0], ['кому подойд'], FAQ_MAT[3][1], 'theory'),
    ('materialy', 'Сколько стоят онлайн-продукты?', ['стоят', 'стоит пособие', 'цена пособия'], 'Базовое пособие 200 zł, теория BASIC в Telegram 500 zł.', 'manual'),
    ('kontakt', 'Как записаться?', ['записат', 'запись', 'записаться'], 'Нажмите «Записаться»: пара коротких шагов, и сообщение откроется в WhatsApp или Telegram, останется нажать «Отправить». Можно и сразу написать мне в WhatsApp.', 'any'),
    ('kontakt', 'Где вы находитесь?', ['адрес', 'где', 'находит', 'krucza', 'крушa', 'метро'], 'В центре Варшавы, Krucza 16/22.', 'any'),
    ('kontakt', 'Как с вами связаться?', ['связат', 'телефон', 'whatsapp', 'ватсап', 'инстаграм', 'instagram'], 'WhatsApp +48 788 214 369, Telegram и Instagram @anya.key_. Отвечаю лично.', ''),
]


def faq_html(items):
    return '<div class="faq">' + ''.join(f'<details class="reveal"><summary>{e(q)}<i></i></summary><p>{e(a)}</p></details>' for q, a in items) + '</div>'


def faq_ld(items):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def course_ld(name, desc, price, path, mode='onsite'):
    return {"@type": "Course", "name": name, "description": desc, "inLanguage": "ru", "provider": {"@id": SITE + "/#business"}, "url": SITE + path,
            "offers": {"@type": "Offer", "price": price, "priceCurrency": "PLN", "category": "Paid", "url": SITE + path},
            "hasCourseInstance": {"@type": "CourseInstance", "courseMode": mode, "location": "Warszawa, Krucza 16/22"}}


ADDRESS = {"@type": "PostalAddress", "streetAddress": "Krucza 16/22", "addressLocality": "Warszawa", "addressCountry": "PL"}
BUSINESS = {"@type": "BeautySalon", "@id": SITE + "/#business", "name": "Anya Kay", "url": SITE + "/", "image": SITE + "/img/hero.jpg",
            "logo": SITE + "/img/avatar.jpg", "telephone": "+48788214369", "address": ADDRESS, "priceRange": "200–4500 zł",
            "description": "Наращивание ресниц и обучение lash-мастеров в Варшаве.", "sameAs": [IG, TG], "areaServed": "Warszawa",
            "founder": {"@type": "Person", "name": "Anya Kay", "jobTitle": "Lash-мастер и преподаватель"}}


# ---------- блоки ----------
def slider(cats, limit=''):
    lim = f' data-limit="{limit}"' if limit else ''
    return (f'<div class="sl" data-slider="{cats}"{lim}><div class="sl-t"></div><div class="wrap sl-bar"><div class="sl-c"></div>'
            '<div class="sl-n"><button class="sl-p" aria-label="Назад">←</button><button class="sl-x" aria-label="Дальше">→</button></div></div></div>')


def pcover(img, pos, eyebrow, h1, text, btns):
    b = ''.join(f'<a href="{h}" class="btn {c}">{t}</a>' for t, h, c in btns)
    return (f'<section class="pcover"><div class="ph" style="background-image:url(\'/img/{img}\');background-position:{pos}" role="img" aria-label=""></div>'
            f'<div class="in"><div class="eyebrow l">{eyebrow}</div><h1>{h1}</h1><p>{text}</p><div class="btns">{b}</div></div></section>')


def band(img, pos, eyebrow, h2, text, href, label):
    return (f'<section class="band"><div class="ph" style="background-image:url(\'/img/{img}\');background-position:{pos}"></div>'
            f'<div class="in wrap reveal"><div class="eyebrow l">{eyebrow}</div><h2>{h2}</h2><p>{text}</p><a href="{href}" class="btn glass">{label} ↗</a></div></section>')


def vid(name, cap, cls=''):
    return (f'<figure class="vid reveal {cls}"><video data-auto data-src="/video/{name}.mp4" poster="/video/{name}.jpg" muted loop playsinline preload="none" aria-label="{e(cap)}"></video>'
            f'<figcaption>{cap}</figcaption></figure>')


def vt(name, who, cap):
    return (f'<figure class="reveal"><div class="vt"><video controls playsinline preload="none" poster="/assets/videos/{name}_poster.jpg" aria-label="Видеоотзыв: {e(who)}">'
            f'<source src="/assets/videos/{name}.mp4" type="video/mp4"></video></div><figcaption><b>{who}</b><br>{cap}</figcaption></figure>')


def dates(course='', price=True, limit=''):
    p = ' data-price' if price else ''
    lim = f' data-limit="{limit}"' if limit else ''
    return f'<div class="dates" data-dates="{course}"{p}{lim}></div>'


def get(icon, b, s):
    return f'<div class="get reveal"><svg viewBox="0 0 32 32">{icon}</svg><b>{b}</b><span>{s}</span></div>'


IC_EYE = '<path d="M3 16s5-8 13-8 13 8 13 8-5 8-13 8S3 16 3 16z"/><circle cx="16" cy="16" r="4"/>'
IC_STAR = '<path d="M16 4l3.5 7.6 8.3.9-6.2 5.6 1.8 8.2L16 22l-7.4 4.3 1.8-8.2-6.2-5.6 8.3-.9z"/>'
IC_CERT = '<rect x="5" y="6" width="22" height="16" rx="1.5"/><path d="M9 11h14M9 15h9"/><circle cx="22" cy="22" r="3.5"/><path d="M20 25l-1 4 3-1.5 3 1.5-1-4"/>'
IC_USER = '<circle cx="16" cy="11" r="5"/><path d="M6 27c1-6 5-9 10-9s9 3 10 9"/>'
IC_BOOK = '<path d="M5 7c4-1 8-1 11 2 3-3 7-3 11-2v17c-4-1-8-1-11 2-3-3-7-3-11-2z"/><path d="M16 9v17"/>'
IC_CHAT = '<path d="M5 7h22v14H13l-6 5v-5H5z"/>'

CASE = '''<section class="sec dark"><div class="wrap"><div class="case gd reveal">
  <div class="case-copy"><div class="eyebrow l">Результат ученицы</div><div class="case-num">800 zł</div>
  <h3>за 2,5 недели после обучения</h3>
  <p>Света прошла обучение и за первые 2,5 недели обслужила 9 клиенток, работая параллельно на заводе. Её ценник на наращивание уже 100 zł, а модели возвращаются и становятся постоянными клиентками.</p></div>
  <button type="button" class="case-media" style="background-image:url('/img/otzyv-sveta-rezultat.jpg')" data-shot="otzyv-sveta-rezultat.jpg" data-alt="Переписка с ученицей Светой" aria-label="Открыть переписку"></button>
</div></div></section>'''

NAV = [('Наращивание', '/naraschivanie/'), ('Обучение', '/obuchenie/'), ('Онлайн-продукты', '/materialy/'), ('Запись', '/zapis/')]
MENU = [('Главная', '/'), ('Наращивание ресниц', '/naraschivanie/'), ('Обучение', '/obuchenie/'), ('Курс BASIC и VIP', '/basic-lash-course/'),
        ('Повышение квалификации', '/povyshenie-kvalifikacii/'), ('Онлайн-продукты', '/materialy/'), ('Запись', '/zapis/')]


def page(path, title, desc, body, ld=None, nav_on='', home=False, noindex=False):
    url = SITE + path
    navh = ''.join(f'<a href="{h}"{" aria-current=page" if nav_on == h else ""}>{t}</a>' for t, h in NAV)
    menuh = ''.join(f'<a href="{h}"{" aria-current=page" if h == path else ""}>{t}<small>{i + 1:02d}</small></a>' for i, (t, h) in enumerate(MENU))
    back = '' if home else '<a href="/" class="bk" data-hback aria-label="Назад">←</a>'
    canon = '<meta name="robots" content="noindex">' if noindex else f'<link rel="canonical" href="{url}">'
    head = f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{canon}
<meta name="theme-color" content="#2A0812">
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
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css?v={V}">
{'<link rel="preload" href="/img/hero.jpg" as="image">' if home else ''}
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": [BUSINESS] + (ld or [])}, ensure_ascii=False)}</script>
</head>
<body>
<header class="hdr g{' clear" data-clear' if home else '"'}>
  <div class="hl">{back}<a href="/" class="mono" aria-label="Anya Kay, на главную">AK</a></div>
  <nav class="nav" aria-label="Меню">{navh}</nav>
  <a href="/zapis/" class="btn wine">Записаться</a>
  <button class="menu-b" data-menu aria-label="Открыть меню">МЕНЮ <i></i></button>
</header>
<div class="mnu" id="mnu" role="dialog" aria-label="Меню">
  <div class="top"><a href="/" class="mono">AK</a><button class="x" data-menu-x aria-label="Закрыть меню">×</button></div>
  <nav>{menuh}</nav>
  <div class="foot"><a href="/zapis/" class="btn glass full">Записаться ↗</a><p>Krucza 16/22 · Варшава</p></div>
</div>
<main>
'''
    foot = f'''</main>
<footer class="ftr"><div class="wrap">
  <div class="top"><div class="brand">ANYA<br>KAY<small>lash-мастер и преподаватель · Варшава</small></div></div>
  <div class="cols">
    <div><h4>Наращивание</h4><a href="/naraschivanie/">Наращивание ресниц</a><a href="/naraschivanie/#prajs">Прайс</a><a href="/zapis/?w=lashes">Запись</a></div>
    <div><h4>Обучение</h4><a href="/basic-lash-course/">Курс с нуля BASIC и VIP</a><a href="/povyshenie-kvalifikacii/">Повышение квалификации</a><a href="/konsultaciya/">Онлайн-консультация</a><a href="/materialy/">Пособие и онлайн-теория</a></div>
    <div><h4>Где я работаю</h4><p><a href="{MAP}" target="_blank" rel="noopener">Krucza 16/22, Варшава ↗</a></p></div>
    <div><h4>Связаться</h4><a href="{WA}" target="_blank" rel="noopener">+48 788 214 369</a>
      <div class="soc"><a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_I}</a><a href="{TG}" target="_blank" rel="noopener" aria-label="Telegram">{TG_I}</a><a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{IG_I}</a></div></div>
  </div>
  <div class="fb"><span>© 2026 Anya Kay</span><span class="lg"><a href="/reglament-obucheniya/">Регламент обучения</a><a href="/politika-konfidencialnosti/">Политика конфиденциальности</a></span></div>
</div></footer>
<div class="mbar g" id="mbar"><a href="/zapis/" class="btn wine">Записаться</a><button class="ic" data-faq aria-label="Есть вопрос?">?</button><a class="ic wa2" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_I}</a></div>
<button class="fab g" id="fab" data-faq aria-haspopup="dialog"><i>?</i>Есть вопрос?</button>
<div class="chat g" id="chat" role="dialog" aria-label="Вопросы и ответы">
  <div class="ch-h"><div class="mono">AK</div><div><b>Anya Kay</b><span>Частые вопросы и быстрая связь</span></div><button id="chat-x" aria-label="Закрыть">×</button></div>
  <div class="ch-b" id="chat-b"></div>
  <form class="inp" id="chat-f"><input id="chat-i" placeholder="Или напишите свой вопрос…" autocomplete="off" aria-label="Ваш вопрос"><button aria-label="Отправить">↑</button></form>
</div>
<div class="lbx" id="lbx" role="dialog" aria-label="Фото"><button class="x" aria-label="Закрыть">×</button><button class="nv pv" aria-label="Назад">‹</button><div class="m"></div><button class="nv nx" aria-label="Дальше">›</button><div class="c"></div></div>
<script src="/app.js?v={V}" defer></script>
</body>
</html>
'''
    if path.endswith('/'):
        d = os.path.join(OUT, path.strip('/')); os.makedirs(d, exist_ok=True); fn = os.path.join(d, 'index.html')
    else:
        fn = os.path.join(OUT, path.strip('/'))
    open(fn, 'w', encoding='utf-8').write(head + body + foot)


# ================= ГЛАВНАЯ =================
home = f'''
<section class="cover">
  <div class="ph" role="img" aria-label="Anya Kay, lash-мастер и преподаватель"></div>
  <div class="mast" aria-hidden="true"><span>ANYA</span><span>KAY</span><small>lash-мастер и преподаватель · Варшава</small></div>
  <div class="tl"><h1>Наращивание ресниц и обучение <em>в Варшаве.</em></h1></div>
  <a href="/zapis/" class="btn glass cta">Записаться ↗</a>
</section>
<div class="to-light long"></div>

<section class="sec"><div class="wrap split">
  <div class="reveal"><div class="eyebrow">Выберите направление</div><h2 class="h2">Чем я могу <em>помочь?</em></h2><p class="lead">Наращивание ресниц в центре Варшавы и обучение наращиванию: с нуля и для мастеров, на месте и онлайн.</p></div>
  <div class="rows">
    <a class="row reveal" href="/naraschivanie/"><span class="n">01</span><span class="t"><small>Krucza 16/22 · 1D–5D</small>Наращивание ресниц</span><span class="arr">↗</span></a>
    <a class="row reveal" href="/obuchenie/"><span class="n">02</span><span class="t"><small>С нуля и для мастеров</small>Обучение</span><span class="arr">↗</span></a>
    <a class="row reveal" href="/materialy/"><span class="n">03</span><span class="t"><small>Пособие и теория в Telegram</small>Онлайн-продукты</span><span class="arr">↗</span></a>
  </div>
</div></section>

<section class="about-ed" id="obo-mne">
  <div class="media" role="img" aria-label="Anya Kay"></div>
  <div class="copy reveal">
    <div class="eyebrow">Обо мне</div>
    <h2 class="h2">Я работаю мастером. <em>И обучаю тому, что использую сама.</em></h2>
    <p class="t">В lash-индустрии с 2017 года. Сегодня я совмещаю работу мастера и преподавателя, а в обучении делаю ставку на понимание техники, сильную теорию и много практики.</p>
    <div class="sig">Anya</div>
    <div class="stats"><div><b data-to="9" data-suf="+">9+</b><span>лет в профессии</span></div><div><b data-to="100" data-suf="+">100+</b><span>обученных учениц</span></div><div><b data-to="2017">2017</b><span>год старта</span></div></div>
  </div>
</section>

<section class="sec to-dark"><div class="wrap">
  <div class="reveal"><div class="eyebrow">Обучение</div><h2 class="h2">Ближайшие <em>курсы</em></h2></div>
  {dates('', price=False, limit=3)}
  <p class="dates-note reveal">{GROUP} <a href="/obuchenie/" style="text-decoration:underline">Все форматы обучения ↗</a></p>
</div></section>

<section class="sec dark" style="padding-top:20px"><div class="wrap"><div class="eyebrow">Портфолио</div><h2 class="h2">Мои <em>работы</em></h2></div>
{slider('lash')}
<div class="wrap" style="margin-top:26px"><a href="/naraschivanie/" class="btn glass">Наращивание и прайс ↗</a></div>
<div class="wrap" style="margin-top:60px"><div class="eyebrow">Отзывы</div><h2 class="h2">Что говорят <em>клиентки и ученицы</em></h2></div>
{ops([OP_CLIENT[0], OP_CLIENT[1], OP_CLIENT[2], OP_STUD[0], OP_STUD[1], OP_STUD[3]])}
</section>
{CASE}
<div class="to-light"></div>
<section class="sec"><div class="wrap split">
  <div class="reveal"><div class="eyebrow">Вопросы</div><h2 class="h2">Коротко <em>о главном</em></h2></div>
  {faq_html(FAQ_HOME)}
</div></section>
{band('anya-kay-burgundy.jpg', '50% 20%', 'Запись', 'Запишитесь <em>или задайте вопрос</em>', 'Короткая заявка займёт минуту. Отвечу лично в WhatsApp или Telegram.', '/zapis/', 'Записаться')}
'''
page('/', 'Anya Kay — Обучение и наращивание ресниц, Варшава',
     'Anya Kay: наращивание ресниц в Варшаве от 200 zł (Krucza 16/22) и обучение наращиванию с нуля и для мастеров. Курсы BASIC и VIP, повышение квалификации, пособие и онлайн-теория.',
     home, [faq_ld(FAQ_HOME)], home=True)

# ================= НАРАЩИВАНИЕ =================
lash = f'''
{pcover('lash-1.jpg', '50% 40%', 'Наращивание · Варшава', 'Наращивание ресниц <em>в Варшаве</em>', 'Продуманная техника, эффект под вашу форму глаз и комфортная носка. Центр Варшавы, Krucza 16/22.', [('Записаться ↗', '/zapis/?w=lashes', 'glass')])}
<section class="sec dark" id="prajs" style="padding-top:40px"><div class="wrap split">
  <div class="reveal"><div class="eyebrow l">Прайс</div><h2 class="h2">Стоимость <em>наращивания</em></h2><p class="lead">Коррекции не делаю, только полное перенаращивание. Так результат каждый раз свежий.</p></div>
  <div class="reveal">
    <div class="prc">
      <div><span>Наращивание · 1D–4D</span><b>200 zł</b></div>
      <div><span>Наращивание · 5D</span><b>230 zł</b></div>
      <div><span>Изгибы L / M</span><b>+20 zł</b></div>
      <div><span>Снятие другого мастера<small>с последующим наращиванием</small></span><b>+30 zł</b></div>
    </div>
    <div class="notice gd"><b>С 1 декабря</b> цены на наращивание повышаются на 20 zł: 1D–4D будет 220 zł, 5D 250 zł. Запишитесь в ноябре по текущей цене.</div>
    <div class="facts"><div><b>90 мин</b><span>наращивание</span></div><div><b>до 2 ч</b><span>со снятием</span></div><div><b>3–5 нед.</b><span>носка</span></div></div>
    <div style="margin-top:26px"><a href="/zapis/?w=lashes" class="btn glass">Выбрать время ↗</a></div>
  </div>
</div></section>
<section class="sec dark" style="padding-top:10px"><div class="wrap"><div class="eyebrow l">Портфолио</div><h2 class="h2">Мои <em>работы</em></h2><p class="lead">Адаптивная техника, индивидуальный подбор эффекта, комфортное отрастание. Листайте, фото открываются на весь экран.</p></div>
{slider('lash')}
<div class="wrap" style="margin-top:60px"><div class="eyebrow l">Отзывы</div><h2 class="h2">Что говорят <em>клиентки</em></h2></div>
{ops(OP_CLIENT)}
</section>
<div class="to-light"></div>
<section class="sec"><div class="wrap split">
  <div class="reveal"><div class="eyebrow">Перед записью</div><h2 class="h2">Частые <em>вопросы</em></h2><p class="lead">Не нашли ответ? Нажмите «Есть вопрос?» или напишите мне.</p></div>
  {faq_html(FAQ_LASH)}
</div></section>
{band('lash-2.jpg', '50% 40%', 'Запись', 'Запись <em>на наращивание</em>', 'Выберите объём и удобное время. Подтвержу запись в WhatsApp или Telegram.', '/zapis/?w=lashes', 'Выбрать время')}
'''
page('/naraschivanie/', 'Наращивание ресниц в Варшаве · от 200 zł · Anya Kay',
     'Наращивание ресниц 1D–5D в центре Варшавы (Krucza 16/22): от 200 zł, 90 минут, носка 3–5 недель. Эффект подбирается индивидуально. Портфолио, отзывы, онлайн-запись.',
     lash, [faq_ld(FAQ_LASH), {"@type": "Service", "name": "Наращивание ресниц", "provider": {"@id": SITE + "/#business"}, "areaServed": "Warszawa",
            "offers": [{"@type": "Offer", "name": "Наращивание 1D–4D", "price": "200", "priceCurrency": "PLN"}, {"@type": "Offer", "name": "Наращивание 5D", "price": "230", "priceCurrency": "PLN"}]}],
     nav_on='/naraschivanie/')


# ================= ОБУЧЕНИЕ =================
def course(small, title, meta, fmt, claim, href, more, tag=''):
    t = f'<span class="tag">{tag}</span>' if tag else ''
    f = '<div class="fmt">' + ''.join(f'<div><span>{a}</span><b>{b}</b></div>' for a, b in fmt) + '</div>'
    return (f'<article class="course gd reveal">{t}<small>{small}</small><h3>{title}</h3><div class="meta">{meta}</div>{f}<p class="claim">{claim}</p>'
            f'<div class="btns"><a href="{more}" class="btn glass">Подробнее ↗</a><a href="{href}" class="btn line">Записаться</a></div></article>')


ZL = '<small>zł</small>'
C_BASIC = course('Хочу начать с нуля', 'Курс BASIC', '3 дня · 3 живые модели · сертификат',
                 [('Индивидуально', f'3 000{ZL}'), ('В группе до 2 человек', f'2 000{ZL}')],
                 'Сильная теория в Telegram, практика на манекене и 3 живых моделях, поддержка после курса.', '/zapis/?w=basic', '/basic-lash-course/')
C_VIP = course('Хочу больше практики', 'VIP «мастер<br>под ключ»', '6 дней · 6 живых моделей · стартовый набор',
               [('Индивидуально', f'4 500{ZL}'), ('В группе до 2 человек', f'3 000{ZL}')],
               'Всё из BASIC и вдвое больше практики: L- и M-изгибы, 2 трендовых эффекта, кубок VIP-мастера.', '/zapis/?w=vip', '/basic-lash-course/#vip', 'VIP')
C_ADV = course('Я уже работаю мастером', 'Повышение<br>квалификации', '1 день · индивидуально',
               [('Индивидуально', f'1 000{ZL}<small>/ день</small>')], 'Сначала разбор ваших работ, потом программа под ваши точки роста.', '/zapis/?w=advanced', '/povyshenie-kvalifikacii/')
C_KONS = course('Нужен разбор', 'Онлайн-<br>консультация', '2 часа · онлайн · 1:1',
                [('Онлайн', f'500{ZL}')], 'Работы, ошибки, носка, клей, программа своего курса или старт преподавания.', '/zapis/?w=consultation', '/konsultaciya/')

edu = f'''
{pcover('anya-kay-burgundy.jpg', '50% 25%', 'Обучение Anya Kay', 'Обучение <em>наращиванию ресниц</em>', 'Начать с нуля, усилить технику, разобрать ошибки или учиться самостоятельно. Обучаю тому, что использую в работе сама.', [('Ближайшие даты ↓', '#daty', 'glass')])}
<section class="sec dark" id="daty" style="padding-top:40px"><div class="wrap">
  <div class="reveal"><div class="eyebrow l">Расписание</div><h2 class="h2">Ближайшие <em>курсы</em></h2><p class="lead">{GROUP}</p></div>
  {dates('', price=True)}
</div></section>
<section class="sec dark" id="formaty" style="padding-top:10px"><div class="wrap">
  <div class="reveal"><div class="eyebrow l">Форматы</div><h2 class="h2">Выберите <em>под свою задачу</em></h2></div>
  <div class="courses">{C_BASIC}{C_VIP}{C_ADV}{C_KONS}</div>
  <p class="dates-note reveal">Хотите учиться самостоятельно? <a href="/materialy/" style="text-decoration:underline">Пособие и теория BASIC в Telegram ↗</a></p>
</div></section>
<section class="sec dark" style="padding-top:20px"><div class="wrap">
  <div class="reveal"><div class="eyebrow l">Почему у меня</div><h2 class="h2">Понимание техники, <em>а не повторение</em></h2></div>
  <div class="gets">{get(IC_BOOK, 'Сильная теория', 'уроки в Telegram и тест после каждого')}{get(IC_EYE, 'Много практики', 'на живых моделях под моим контролем')}{get(IC_USER, 'До 2 человек', 'внимание каждой ученице')}{get(IC_CHAT, 'Поддержка', 'после курса: работы и вопросы')}</div>
  <div class="vids">{vid('praktika-ruka', 'Ставлю руку на практике', 'wide')}{vid('kurs', 'Как проходит курс')}{vid('praktika-1', 'Практика на курсе')}</div>
</div></section>
<section class="sec dark" style="padding-top:10px"><div class="wrap"><div class="eyebrow l">Выпускницы</div><h2 class="h2">Мои <em>ученицы</em></h2><p class="lead">С сертификатом и кубком в руках, в моей студии на Krucza.</p></div>
{slider('cert')}</section>
<section class="sec dark" style="padding-top:10px"><div class="wrap"><div class="eyebrow l">Ученицы</div><h2 class="h2">Работы <em>моих учениц</em></h2></div>
{slider('uch')}
<div class="wrap" style="margin-top:60px"><div class="eyebrow l">Отзывы</div><h2 class="h2">Что говорят <em>ученицы</em></h2></div>
{ops(OP_STUD)}
</section>
{CASE}
<div class="to-light"></div>
<section class="sec"><div class="wrap split">
  <div class="reveal"><div class="eyebrow">Вопросы</div><h2 class="h2">Об <em>обучении</em></h2></div>
  {faq_html(FAQ_EDU)}
</div></section>
{band('uchenica-basic-2.jpg', '50% 50%', 'Запись', 'Выберите формат <em>и запишитесь</em>', 'Расскажите о своём опыте и удобных датах, предложу подходящий вариант.', '/zapis/?k=obuchenie', 'Записаться на обучение')}
'''
page('/obuchenie/', 'Обучение наращиванию ресниц в Варшаве · курсы с нуля и для мастеров · Anya Kay',
     'Обучение наращиванию ресниц в Варшаве у Anya Kay: курс с нуля BASIC (от 2000 zł) и VIP «мастер под ключ» (от 3000 zł), повышение квалификации, онлайн-консультация, теория в Telegram. 100+ учениц.',
     edu, [faq_ld(FAQ_EDU)], nav_on='/obuchenie/')

# ================= BASIC / VIP =================
STEPS = [('Теория в Telegram', 'В своём темпе, до практики.'), ('Тесты', 'После каждого урока.'), ('Пособие', 'Вся база остаётся у вас.'),
         ('Итоговая проверка', 'Перед выходом на практику.'), ('Практика', 'Манекен и живые модели: 3 на BASIC, 6 на VIP.'), ('Сертификат', 'Именной, с печатью, после завершения.')]
basic = f'''
{pcover('uchenica-basic-1.jpg', '50% 50%', 'Курс с нуля · BASIC и VIP', 'Курс наращивания ресниц <em>с нуля</em>', 'Для тех, кто хочет не просто научиться наращивать, а понимать, что и почему делает в работе.', [('Ближайшие даты ↓', '#daty', 'glass')])}
<section class="sec dark" id="daty" style="padding-top:40px"><div class="wrap">
  <div class="reveal"><div class="eyebrow l">Расписание</div><h2 class="h2">Ближайшие <em>даты</em></h2><p class="lead">{GROUP}</p></div>
  {dates('', price=True)}
</div></section>
<section class="sec dark" style="padding-top:10px"><div class="wrap">
  <div class="reveal"><div class="eyebrow l">Тарифы</div><h2 class="h2">BASIC <em>или VIP</em></h2></div>
  <div class="courses">
    <article class="course gd reveal"><small>3 дня · 21 час практики · 3 модели</small><h3>BASIC</h3>
      <div class="fmt"><div><span>Индивидуально</span><b>3 000{ZL}</b></div><div><span>В группе до 2 человек</span><b>2 000{ZL}<small>с человека</small></b></div></div>
      <ul><li>Углублённая теория в Telegram-боте</li><li>Практика на 3D-манекене и 3 живых моделях</li><li>Моделирование и схемы актуальных эффектов</li><li>Базовое пособие и дополнительные гайды</li><li>Неограниченная поддержка после обучения</li><li>Именной сертификат с печатью</li></ul>
      <p class="bonus"><b>Бонус:</b> курс по обработке контента и ретуши фото.</p>
      <div class="btns"><a href="/zapis/?w=basic" class="btn glass">Записаться на BASIC ↗</a></div></article>
    <article class="course gd reveal" id="vip"><span class="tag">VIP</span><small>6 дней практики · 6 моделей</small><h3>VIP «мастер под ключ»</h3>
      <div class="fmt"><div><span>Индивидуально</span><b>4 500{ZL}</b></div><div><span>В группе до 2 человек</span><b>3 000{ZL}<small>с человека</small></b></div></div>
      <ul><li>Всё из BASIC и в два раза больше практики</li><li>6 моделей для практики вместо 3</li><li>Отработка L- и M-изгибов</li><li>2 трендовых эффекта на выбор</li><li>Стартовый набор материалов</li><li>Кубок VIP-мастера</li></ul>
      <div class="btns"><a href="/zapis/?w=vip" class="btn glass">Записаться на VIP ↗</a></div></article>
  </div>
</div></section>
<div class="to-light"></div>
<section class="sec"><div class="wrap">
  <div class="reveal"><div class="eyebrow">Сравнение</div><h2 class="h2">Что входит <em>в каждый курс</em></h2></div>
  <div class="cmpw reveal"><table class="cmp">
    <thead><tr><th></th><th>BASIC</th><th class="v">VIP</th></tr></thead>
    <tbody>
      <tr><td>Дней практики</td><td>3</td><td class="v">6</td></tr>
      <tr><td>Живые модели</td><td>3</td><td class="v">6</td></tr>
      <tr><td>Теория в Telegram, тесты, пособие</td><td>✓</td><td class="v">✓</td></tr>
      <tr><td>Моделирование и схемы эффектов</td><td>✓</td><td class="v">✓ + 2 трендовых</td></tr>
      <tr><td>L- и M-изгибы</td><td>—</td><td class="v">✓</td></tr>
      <tr><td>Стартовый набор материалов</td><td>—</td><td class="v">✓</td></tr>
      <tr><td>Сертификат и поддержка</td><td>✓</td><td class="v">✓</td></tr>
      <tr><td>Индивидуально</td><td>3 000 zł</td><td class="v">4 500 zł</td></tr>
      <tr><td>В группе до 2 человек, с человека</td><td>2 000 zł</td><td class="v">3 000 zł</td></tr>
    </tbody>
  </table></div>
</div></section>
<section class="sec to-dark"><div class="wrap">
  <div class="reveal"><div class="eyebrow">Как проходит</div><h2 class="h2">Обучение <em>шаг за шагом</em></h2></div>
  <div class="prog-in"><div class="tlx">{''.join(f'<div class="day reveal"><div class="d">{i + 1}</div><div><h3>{a}</h3><p>{b}</p></div></div>' for i, (a, b) in enumerate(STEPS))}</div></div>
</div></section>
<section class="sec dark" style="padding-top:10px"><div class="wrap">
  <div class="reveal"><div class="eyebrow l">Программа теории</div><h2 class="h2">16 уроков <em>до практики</em></h2></div>
  <ol class="lessons">{''.join(f'<li><b>{i:02d}</b>{e(t)}</li>' for i, t in enumerate(LESSONS))}</ol>
  <div class="vids">{vid('praktika-ruka', 'Ставлю руку на практике', 'wide')}{vid('kurs', 'Как проходит курс')}{vid('praktika-1', 'Практика на курсе')}</div>
</div></section>
<section class="sec dark" style="padding-top:10px"><div class="wrap"><div class="eyebrow l">Выпускницы</div><h2 class="h2">Мои <em>ученицы</em></h2><p class="lead">С сертификатом и кубком в руках, в моей студии на Krucza.</p></div>
{slider('cert')}</section>
<section class="sec dark" style="padding-top:10px"><div class="wrap"><div class="eyebrow l">Ученицы</div><h2 class="h2">Работы <em>учениц</em></h2></div>
{slider('uch')}
<div class="wrap" style="margin-top:60px"><div class="eyebrow l">Отзывы</div><h2 class="h2">Что говорят <em>ученицы</em></h2>
<div class="vts">{vt('testimonial_1', 'Настя', 'прилетела на курс из Швеции, 6 дней обучения')}{vt('testimonial_2', 'Арина', 'курс 6 дней')}</div></div>
{ops(OP_STUD)}
</section>
{CASE}
<div class="to-light"></div>
<section class="sec"><div class="wrap split">
  <div class="reveal"><div class="eyebrow">Вопросы</div><h2 class="h2">О <em>курсе</em></h2><p class="lead">Условия записи и предоплаты в <a href="/reglament-obucheniya/" style="text-decoration:underline">регламенте обучения</a>.</p></div>
  {faq_html(FAQ_EDU[:6])}
</div></section>
{band('uchenica-basic-3.jpg', '50% 50%', 'Запись', 'Запишитесь <em>на курс</em>', 'Выберите дату и формат. Если удобной даты нет, напишите, подберём вместе.', '/zapis/?w=basic', 'Записаться')}
'''
page('/basic-lash-course/', 'Курс наращивания ресниц с нуля в Варшаве · BASIC и VIP · Anya Kay',
     'Курс наращивания ресниц с нуля в Варшаве: BASIC 3 дня, 3 живые модели, 3000 zł (в группе до 2 человек 2000 zł); VIP «мастер под ключ» 6 дней, 6 моделей, 4500 zł (в группе 3000 zł). Сертификат и поддержка.',
     basic, [faq_ld(FAQ_EDU[:6]), course_ld('BASIC LASH COURSE', 'Курс наращивания ресниц с нуля: теория в Telegram, 3 дня практики, 3 живые модели, сертификат.', '3000', '/basic-lash-course/'),
             course_ld('VIP «мастер под ключ»', 'Курс наращивания ресниц с нуля: 6 дней практики, 6 моделей, L/M-изгибы, 2 трендовых эффекта, стартовый набор.', '4500', '/basic-lash-course/#vip')],
     nav_on='/obuchenie/')

# ================= ПОВЫШЕНИЕ =================
adv = f'''
{pcover('povyshenie-1.jpg', '50% 40%', 'Обучение · для мастеров', 'Повышение <em>квалификации</em>', 'Сначала разбираю ваши работы, потом составляю программу обучения. Только то, что нужно именно вам.', [('Записаться ↗', '/zapis/?w=advanced', 'glass'), ('Сначала консультация', '/konsultaciya/', 'line')])}
<div class="to-light"></div>
<section class="sec"><div class="wrap split">
  <div class="reveal"><div class="eyebrow">Что прорабатываем</div><h2 class="h2">Ваши <em>точки роста</em></h2><p class="lead">Ошибки в технике, скорость, объёмы до 5D, моделирование взгляда и эффекты.</p></div>
  <div class="reveal forwho"><div class="tlx">
    <div class="day"><div class="d">1</div><div><h3>Присылаете работы</h3><p>Фото ваших наращиваний: так я вижу, на каком вы уровне и что мешает.</p></div></div>
    <div class="day"><div class="d">2</div><div><h3>Разбор и программа</h3><p>Нахожу ошибки и точки роста, составляю программу под них.</p></div></div>
    <div class="day"><div class="d">3</div><div><h3>Практика</h3><p>Стандартно 1 день. При необходимости программу можно расширить.</p></div></div>
  </div></div>
</div></section>
<section class="sec to-dark"><div class="wrap"><div class="eyebrow">Результаты</div><h2 class="h2">Работы <em>после обучения</em></h2>
  <div class="vids">{vid('povyshenie', 'Работа после повышения квалификации')}</div>
  <div class="pricebox gd reveal" style="margin-top:30px"><div class="eyebrow l">1 день · индивидуально</div><div class="big">1&nbsp;000<span> zł</span></div><p>Разбор работ заранее, программа под вас и практика.</p><a href="/zapis/?w=advanced" class="btn glass">Записаться ↗</a></div>
</div></section>
<section class="sec dark" style="padding-top:10px"><div class="wrap"><div class="eyebrow l">Отзывы</div><h2 class="h2">Что говорят <em>ученицы</em></h2></div>
{ops([OP_STUD[2], OP_STUD[0]])}
</section>
<div class="to-light"></div>
<section class="sec"><div class="wrap split">
  <div class="reveal"><div class="eyebrow">Вопросы</div><h2 class="h2">Повышение <em>квалификации</em></h2></div>
  {faq_html(FAQ_ADV)}
</div></section>
{band('povyshenie-2.jpg', '50% 40%', 'Запись', 'Разберём <em>ваши работы</em>', 'Напишите, что хотите улучшить, и пришлите пару работ. Предложу программу.', '/zapis/?w=advanced', 'Записаться')}
'''
page('/povyshenie-kvalifikacii/', 'Повышение квалификации lash-мастера в Варшаве · Anya Kay',
     'Повышение квалификации для lash-мастеров в Варшаве: разбор ваших работ и индивидуальная программа. Техника, скорость, объёмы до 5D, моделирование, эффекты. 1000 zł / день.',
     adv, [faq_ld(FAQ_ADV), course_ld('Повышение квалификации lash-мастера', 'Индивидуальная программа после разбора работ: техника, скорость, объёмы до 5D, моделирование, эффекты.', '1000', '/povyshenie-kvalifikacii/')],
     nav_on='/obuchenie/')

# ================= КОНСУЛЬТАЦИЯ =================
TOP = ['Технику', 'Носку', 'Скорость', 'Клей', 'Пучки', 'Программу своего курса', 'Старт преподавания', 'Поиск учениц']
kons = f'''
{pcover('uchenica-basic-4.jpg', '50% 50%', 'Обучение · онлайн', 'Онлайн-консультация <em>для lash-мастеров</em>', 'Разберём ваши работы, найдём ошибки и определим, что именно мешает двигаться дальше.', [('Записаться ↗', '/zapis/?w=consultation', 'glass')])}
<div class="to-light"></div>
<section class="sec"><div class="wrap split">
  <div class="reveal"><div class="eyebrow">Что можно разобрать</div><h2 class="h2">2 часа <em>лично со мной</em></h2>
    <div class="tags" style="margin-top:20px">{''.join(f'<span>{t}</span>' for t in TOP)}</div>
    <p class="lead" style="margin-top:22px">Если станет понятно, что нужна практика, можно продолжить на <a href="/povyshenie-kvalifikacii/" style="text-decoration:underline">повышении квалификации</a>.</p></div>
  <div class="pricebox gd reveal"><div class="eyebrow l">2 часа · онлайн · 1:1</div><div class="big">500<span> zł</span></div><p>Разбор работ, ошибок и ваших вопросов.</p><a href="/zapis/?w=consultation" class="btn glass">Записаться ↗</a></div>
</div></section>
{band('anya-kay-burgundy.jpg', '50% 20%', 'Запись', 'Готовы <em>разобрать работы?</em>', 'Оставьте заявку, договоримся о времени созвона.', '/zapis/?w=consultation', 'Записаться')}
'''
page('/konsultaciya/', 'Онлайн-консультация для lash-мастеров · разбор работ · Anya Kay',
     'Онлайн-консультация для мастеров по наращиванию ресниц: 2 часа, 500 zł. Разбор работ, ошибок, носки, скорости, клея, программы курса и старта преподавания.',
     kons, [{"@type": "Service", "name": "Онлайн-консультация для lash-мастеров", "provider": {"@id": SITE + "/#business"}, "offers": {"@type": "Offer", "price": "500", "priceCurrency": "PLN"}}],
     nav_on='/obuchenie/')

# ================= ОНЛАЙН-ПРОДУКТЫ =================
mat = f'''
{pcover('posobie-1.jpg', '50% 30%', 'Онлайн-продукты', 'Пособие и онлайн-теория <em>по наращиванию</em>', 'Для мастеров, которые хотят систематизировать базу, и преподавателей, которым нужна готовая основа для курса.', [('Пособие ↓', '#posobie', 'glass'), ('Теория в Telegram ↓', '#teoriya', 'line')])}
<div class="to-light"></div>
<section class="sec"><div class="wrap"><div class="prods">
  <article class="prod reveal" id="posobie">{slider('posobie')}<div class="bd">
    <h2>Базовое пособие</h2><div class="pr">200 zł</div>
    <p><b>51 страница углублённой теории по наращиванию ресниц.</b></p>
    <p>Полностью редактируется в Canva, без водяных знаков, подходит для печати. Для мастеров, которые хотят систематизировать базу, и преподавателей, которым нужна основа для собственного курса.</p>
    <div style="margin-top:20px"><a href="/zapis/?w=manual" class="btn wine">Купить пособие</a></div></div></article>
  <article class="prod reveal" id="teoriya">{slider('teoriya')}<div class="bd">
    <h2>Теория BASIC в Telegram</h2><div class="pr">500 zł</div>
    <p><b>Весь теоретический блок BASIC LASH COURSE в самостоятельном онлайн-формате.</b></p>
    <p>Урок → тест → следующий урок → финальная проверка. Внутри: видеоуроки, базовое пособие, тесты, прогресс, дополнительные гайды и курс по контенту.</p>
    <details><summary>Программа: 16 уроков ↓</summary><ol>{''.join(f'<li>{e(t)}</li>' for t in LESSONS)}</ol></details>
    <div style="margin-top:20px"><a href="/zapis/?w=theory" class="btn wine">Купить доступ</a></div></div></article>
</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap split">
  <div class="reveal"><div class="eyebrow">Вопросы</div><h2 class="h2">Об <em>онлайн-продуктах</em></h2></div>
  {faq_html(FAQ_MAT)}
</div></section>
{band('uchenica-basic-1.jpg', '50% 50%', 'Практика', 'Хотите <em>больше практики?</em>', 'Теорию можно продолжить на курсе BASIC или VIP с живыми моделями.', '/basic-lash-course/', 'Курс с нуля')}
'''
page('/materialy/', 'Пособие и онлайн-теория по наращиванию ресниц · Anya Kay',
     'Онлайн-продукты для lash-мастеров от Anya Kay: базовое пособие на 51 страницу (редактируется в Canva, 200 zł) и теория BASIC в Telegram: 16 уроков с тестами (500 zł).',
     mat, [faq_ld(FAQ_MAT), {"@type": "Product", "name": "Базовое пособие по наращиванию ресниц", "description": "51 страница углублённой теории, редактируется в Canva.", "brand": {"@type": "Brand", "name": "Anya Kay"},
           "offers": {"@type": "Offer", "price": "200", "priceCurrency": "PLN", "availability": "https://schema.org/InStock", "url": SITE + "/materialy/"}},
           course_ld('Теория BASIC в Telegram', '16 видеоуроков с тестами и финальной проверкой, пособие и гайды.', '500', '/materialy/#teoriya', 'online')],
     nav_on='/materialy/')

# ================= ЗАПИСЬ =================
zap = f'''
<section class="sec book" style="background:linear-gradient(180deg,var(--top) 0,var(--milk) 420px)"><div class="wrap book-in">
  <div class="reveal book-l">
    <div class="eyebrow">Запись</div>
    <h1 class="h2" style="font-size:clamp(40px,6vw,76px)">Запись <em>за минуту</em></h1>
    <p class="lead">Выберите услугу или курс и пару деталей. В конце сообщение откроется в WhatsApp или Telegram, останется нажать «Отправить». Отвечаю лично.</p>
    <div class="how"><div><b>1</b>Выберите услугу или курс</div><div><b>2</b>Дату и детали</div><div><b>3</b>Отправьте сообщение</div></div>
    <div class="direct"><b>Хотите написать сразу?</b><span>Krucza 16/22, Варшава</span><div class="soc"><a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_I}</a><a href="{TG}" target="_blank" rel="noopener" aria-label="Telegram">{TG_I}</a><a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{IG_I}</a></div></div>
  </div>
  <div class="form reveal" id="fapp" aria-live="polite"><noscript>Напишите мне в <a href="{TG}">Telegram</a> или <a href="{WA}">WhatsApp</a>.</noscript></div>
</div></section>
'''
page('/zapis/', 'Запись на наращивание ресниц и обучение · Anya Kay, Варшава',
     'Онлайн-запись к Anya Kay: наращивание ресниц в Варшаве, курсы BASIC и VIP, повышение квалификации, консультация, пособие. Заявка уходит в WhatsApp или Telegram.',
     zap, nav_on='/zapis/')

# ================= РЕГЛАМЕНТ (черновик, ждём условия Ани) =================
reg = f'''
<section class="legal"><div class="eyebrow">Anya Kay</div>
  <h1>Регламент обучения</h1>
  <p class="upd">Действует с 03.11.2026</p>
  <h2>1. Организатор</h2>
  <p>Обучение проводит Anya Kay, Krucza 16/22, Warszawa. Связь: WhatsApp <a href="{WA}">+48 788 214 369</a>, <a href="{TG}">Telegram</a>.</p>
  <h2>2. Курсы и цены</h2>
  <ul>
    <li><b>BASIC</b>: 3 дня, 3 живые модели. Индивидуально 3 000 zł, в мини-группе до 2 человек 2 000 zł с человека.</li>
    <li><b>VIP «мастер под ключ»</b>: 6 дней, 6 живых моделей. Индивидуально 4 500 zł, в мини-группе до 2 человек 3 000 zł с человека.</li>
    <li><b>Повышение квалификации</b>: 1 день, 1 000 zł. <b>Онлайн-консультация</b>: 2 часа, 500 zł.</li>
  </ul>
  <p>На отдельные даты может действовать специальная цена, она указана в расписании на сайте.</p>
  <h2>3. Индивидуально и в группе</h2>
  <p>В группе максимум 2 человека. Если на дату записывается ученица в индивидуальном формате, группы на эту дату не будет. Если вы выбрали группу, я ищу на дату второго человека и сообщаю, когда группа собрана.</p>
  <h2>4. Запись и предоплата</h2>
  <p>Вы отправляете заявку через сайт, WhatsApp или Telegram. Я подтверждаю дату и формат и присылаю данные для предоплаты. Размер предоплаты, сроки оплаты остатка, условия переноса и отмены уточняются при записи.</p>
  <h2>5. Сертификат и поддержка</h2>
  <p>После обучения вы получаете именной сертификат с печатью и поддержку: можно присылать работы и задавать вопросы.</p>
</section>
'''
page('/reglament-obucheniya/', 'Регламент обучения · Anya Kay',
     'Регламент обучения наращиванию ресниц у Anya Kay: курсы и цены, индивидуальный и групповой формат, запись и предоплата.', reg)

# ================= ПОЛИТИКА =================
pol = f'''
<section class="legal"><div class="eyebrow">Anya Kay</div>
  <h1>Политика конфиденциальности</h1>
  <p class="upd">Коротко и понятно: какие данные я получаю через сайт и как их использую. В соответствии с RODO (GDPR).</p>
  <h2>1. Кто отвечает за данные</h2>
  <p>Администратор персональных данных: Anya Kay, Krucza 16/22, Warszawa, Polska. Связь: <a href="{WA}">WhatsApp +48 788 214 369</a>, <a href="{TG}">Telegram</a>.</p>
  <h2>2. Какие данные и зачем</h2>
  <p>Через форму записи и помощник на сайте вы сами составляете сообщение (имя, телефон или ник, выбранная услуга, комментарий) и отправляете его мне в WhatsApp или Telegram. Сайт не сохраняет эти данные на сервере. Я использую их только чтобы ответить вам, записать на процедуру или обучение и выставить счёт (основание: art. 6 ust. 1 lit. b i f RODO).</p>
  <h2>3. Сколько храню</h2>
  <p>Переписку храню, пока она нужна для записи и обслуживания, данные для счетов столько, сколько требует польское налоговое право.</p>
  <h2>4. Кому передаются</h2>
  <p>Данные не продаются и не передаются третьим лицам для рекламы. Сообщения проходят через сервисы, которые вы выбираете сами: WhatsApp (Meta) и Telegram. Сайт подключает шрифты Google Fonts.</p>
  <h2>5. Ваши права</h2>
  <p>Вы можете запросить доступ к своим данным, их исправление или удаление, ограничить обработку или возразить против неё, а также подать жалобу в Prezes Urzędu Ochrony Danych Osobowych (UODO). Для этого просто напишите мне.</p>
  <h2>6. Cookies</h2>
  <p>Сайт не использует рекламные и аналитические cookies.</p>
</section>
'''
page('/politika-konfidencialnosti/', 'Политика конфиденциальности · Anya Kay',
     'Политика конфиденциальности сайта anyakay.pl: какие данные обрабатываются при записи и как, в соответствии с RODO (GDPR).', pol)

# ================= 404 =================
nf = pcover('lash-3.jpg', '50% 50%', 'Ошибка 404', 'Такой страницы <em>нет</em>', 'Возможно, ссылка устарела. Вот куда можно перейти:',
            [('На главную ↗', '/', 'glass'), ('Наращивание', '/naraschivanie/', 'line'), ('Обучение', '/obuchenie/', 'line')])
page('/404.html', 'Страница не найдена · Anya Kay', 'Страница не найдена.', nf, noindex=True)

# ================= статика =================
css = open(os.path.join(B, 'style.base.css'), encoding='utf-8').read() + open(os.path.join(B, 'anya.css'), encoding='utf-8').read()
open(os.path.join(OUT, 'style.css'), 'w', encoding='utf-8').write(css)
chat = [{'t': t, 'q': q, 'k': k, 'a': a, 'go': g} for t, q, k, a, g in CHAT]
js = open(os.path.join(B, 'app.src.js'), encoding='utf-8').read()
js = (js.replace("'__SHEET_CSV__'", json.dumps(SHEET_CSV)).replace('__DATES__', json.dumps(DATES, ensure_ascii=False))
      .replace('__ICONS__', json.dumps({'wa': WA_I, 'tg': TG_I}, ensure_ascii=False)).replace('__FAQ__', json.dumps(chat, ensure_ascii=False)))
assert '__' not in js.replace('__proto__', ''), 'placeholder left'
open(os.path.join(OUT, 'app.js'), 'w', encoding='utf-8').write(js)
open(os.path.join(OUT, 'CNAME'), 'w').write('anyakay.pl')
open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
URLS = [('/', '1.0'), ('/naraschivanie/', '0.9'), ('/obuchenie/', '0.9'), ('/basic-lash-course/', '0.9'), ('/povyshenie-kvalifikacii/', '0.8'),
        ('/konsultaciya/', '0.7'), ('/materialy/', '0.7'), ('/zapis/', '0.6'), ('/reglament-obucheniya/', '0.3'), ('/politika-konfidencialnosti/', '0.2')]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'  <url><loc>{SITE}{u}</loc><lastmod>2026-11-03</lastmod><priority>{p}</priority></url>\n' for u, p in URLS) + '</urlset>\n'
open(os.path.join(OUT, 'sitemap.xml'), 'w').write(sm)
print('ok')
