# -*- coding: utf-8 -*-
"""
Niche site engine (seosem-servisy family).

Shared layout + components for the niche microsites, generated from the
noktostudio.com design system. Every page is plain HTML after the build,
no runtime dependencies. Two markets only: SK (root) + CZ (/cz/).

Google-colored design system, identical brand tokens to noktostudio.com:
  violet #7A50D6 / #6A3FC4, orange #F75940, cerulean #1DACD6.
"""
import html as _html

# ---------------------------------------------------------------- constants
# Overridden per niche site by build/config.py (BASE, BRAND, NICHE_*).
BASE = "https://example.invalid"
BRAND = "Niche"
BRAND_TAGLINE = ""

PHONE_DISPLAY = "+421 917 316 105"
PHONE_TEL = "tel:+421917316105"
EMAIL = "hello@noktostudio.com"
MAIN_SITE = "https://noktostudio.com"

# Verification tokens: paste the content values from Google Search Console
# and Bing Webmaster after creating each property, then rebuild.
GSC_TOKEN = ""     # e.g. "aBcD..." from the html-tag verification snippet
BING_TOKEN = "3b43ea1af0ee49f082ab3c4e94ed5f4f"  # reuse existing Bing token

OG_LOCALE = {"sk": "sk_SK", "cz": "cs_CZ"}

# Logo: N(violet) o(orange) k(cerulean) t(violet-light) + brand name
LOGO = '<span class="logo-n">N</span><span class="logo-o">o</span>' \
       '<span class="logo-k">k</span><span class="logo-t">t</span>o Studio'

MARKET_ROOTS = {"sk": "/sk/", "cz": "/cz/"}
MARKET_HOME = {"sk": "/", "cz": "/cz/"}

LANG_PATHS = {"sk": set(), "cz": set()}   # filled by config

# SK <-> CZ hreflang pairs, 1:1. Filled by config: SK path -> CZ path.
HREFLANG_PAIR = {}


def _market_url(m: str, sub: str) -> str:
    return BASE + (MARKET_HOME[m] if sub == "" else MARKET_ROOTS[m] + sub)


def hreflang_links(market: str, path: str) -> str:
    """Two-language hreflang (SK, CS) with x-default = SK. Both markets share
    every page, so a pair always exists."""
    pairs = {"sk": path, "cz": HREFLANG_PAIR.get(path)}
    if market == "cz":
        # find the SK path for this CZ path
        for sk_p, cz_p in HREFLANG_PAIR.items():
            if cz_p == path:
                pairs = {"sk": sk_p, "cz": path}
                break
    if pairs["sk"] is None or pairs["cz"] is None:
        return ""
    return "\n  ".join([
        f'<link rel="alternate" hreflang="sk" href="{_market_url("sk", pairs["sk"])}">',
        f'<link rel="alternate" hreflang="cs" href="{_market_url("cz", pairs["cz"])}">',
        f'<link rel="alternate" hreflang="x-default" href="{_market_url("sk", pairs["sk"])}">',
    ])


def logo(market: str) -> str:
    return f'<a href="{MARKET_HOME[market]}" class="nav-logo">{LOGO}</a>'


# ------------------------------------------------- svg icons
_GICON_PATHS = {
    "ai":     '<path d="M12 3a5 5 0 0 1 5 5c0 2.4-1.7 4.4-4 4.9V16h-2v-3.1c-2.3-.5-4-2.5-4-4.9a5 5 0 0 1 5-5Z"/><circle cx="12" cy="20.5" r="1.6"/>',
    "search": '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5"/>',
    "pin":    '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11Z"/><circle cx="12" cy="10" r="2.5"/>',
    "shop":   '<path d="M4 7h16l-1.5 13h-13L4 7Z"/><path d="M8.5 10V6.5a3.5 3.5 0 0 1 7 0V10"/>',
    "audit":  '<path d="M6 3h9l4 4v14H6V3Z"/><path d="M9 12h6M9 16h6M9 8h3"/>',
    "link":   '<path d="M10 14a4 4 0 0 0 6 .4l3-3a4 4 0 1 0-5.7-5.7l-1.5 1.5"/><path d="M14 10a4 4 0 0 0-6-.4l-3 3a4 4 0 1 0 5.7 5.7l1.5-1.5"/>',
    "mail":   '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "web":    '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M7 6.5h.01M10 6.5h.01"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="0.5"/>',
    "chart":  '<path d="M4 20h16"/><path d="M7 20v-6M12 20V9M17 20v-9"/>',
    "shield": '<path d="M12 3 5 6v6c0 4.5 3 7.6 7 9 4-1.4 7-4.5 7-9V6l-7-3Z"/>',
    "bolt":   '<path d="M13 2 5 13h6l-1 9 8-11h-6l1-9Z"/>',
    "check":  '<path d="m4.5 12.5 5 5L19.5 7"/>',
    "grow":   '<path d="M4 19 10 13l3.5 3.5L20 10"/><path d="M20 15v-5h-5"/>',
    "wp":     '<path d="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18Z"/><path d="m5 9 3.5 9L11 12l2 6 4-9"/><path d="M8 9h.01M16 9h.01"/>',
}

def gicon(kind: str, color: str = "#6A3FC4", size: int = 24) -> str:
    path = _GICON_PATHS[kind]
    return (f'<span class="gicon" style="color:{color};width:{size}px;height:{size}px;" aria-hidden="true">'
            f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{path}</svg></span>')


# ---------------------------------------------------------------- navs

def nav_items(market: str) -> list[tuple[str, str]]:
    """(label, href) pairs. Služby dropdown filled from NICHE config."""
    root = MARKET_ROOTS[market]
    svc_children = [(_market_url(market, p), n) for p, n in NICHE_NAV_SVC[market]]
    svc = ("Služby" if market == "sk" else "Služby", _market_url(market, "sluzby/"), svc_children)
    rest = [
        ("Cenník" if market == "sk" else "Ceník", _market_url(market, "cennik/" if market == "sk" else "cenik/")),
        ("Ako pracujem" if market == "sk" else "Jak pracuji", _market_url(market, "jak-pracujeme/")),
        ("Blog", _market_url(market, "blog/")),
        ("Kontaktujte ma" if market == "sk" else "Kontaktujte mě", _market_url(market, "kontakt/")),
    ]
    return [svc] + rest


def cta_label(market: str) -> str:
    return {"sk": "Kontaktuj ma", "cz": "Kontaktujte mě"}[market]


NICHE_NAV_SVC = {"sk": [], "cz": []}  # [(subpath, label)] per market


def google_review_band(market: str) -> str:
    head = {"sk": "Čo hovoria klienti", "cz": "Co říkají klienti"}[market]
    label = {"sk": "Google recenzia", "cz": "Google recenze"}[market]
    attr = {"sk": "Overená Google recenzia", "cz": "Ověřená Google recenze"}[market]
    link_lbl = {"sk": "Google profile", "cz": "Google profilu"}[market]
    more = {
        "sk": f"Viac recenzií na mojom <a href=\"https://www.google.com/maps/place/Nokto+Studio\" target=\"_blank\" rel=\"noopener\" style=\"font-weight:700; color:var(--brand-primary-deep);\">{link_lbl}</a>.",
        "cz": f"Více recenzí na mém <a href=\"https://www.google.com/maps/place/Nokto+Studio\" target=\"_blank\" rel=\"noopener\" style=\"font-weight:700; color:var(--brand-primary-deep);\">{link_lbl}</a>.",
    }[market]
    return f"""
<section class="section section-alt">
  <div class="container">
    <div class="section-head" style="text-align:center;">
      <span class="section-label">{label}</span>
      <h2>{head}</h2>
    </div>
    <div style="max-width:720px; margin:0 auto;">
      <div class="benefit-card card-hover" style="padding:32px;">
        <div style="font-size:1.4rem; color:var(--brand-warm); letter-spacing:2px;">★★★★★</div>
        <p style="font-size:1.05rem; line-height:1.75; margin-top:14px; color:var(--text);">„Šimon mi robil obsah na webovú stránku, články, produktový feed na e-shop a SEO optimalizáciu. Oceňujem jeho proaktívny prístup, ochotu vysvetliť a edukovať staršieho človeka, ktorý nemá taký prehľad v technológiách, a výbornú spoluprácu, okamžité reakcie a férové ceny. Veľmi som spokojný s poskytnutými službami."</p>
        <p style="margin-top:16px; font-weight:700; color:var(--text);">{attr}, 2026</p>
      </div>
      <p style="text-align:center; margin-top:20px; color:var(--text-muted); font-size:0.88rem;">{more}</p>
    </div>
  </div>
</section>
"""


def lang_toggle(market: str, path: str) -> str:
    pairs = []
    for m, label in (("sk", "SK"), ("cz", "CZ")):
        href = _market_url(m, path)
        active = " active" if m == market else ""
        pairs.append(f'<a href="{href}" class="lang-btn{active}">{label}</a>')
    return '<div class="lang-toggle">' + ' <span>|</span> '.join(pairs) + "</div>"


# ---------------------------------------------------------------- base template

def base(*, market: str, path: str, title: str, desc: str, canonical: str,
         body: str, prefix: str, extra_head: str = "", h1: bool = True,
         og_type: str = "website") -> str:
    nav = ""
    root = MARKET_ROOTS[market]
    cur = (root + path).rstrip('/')
    for item in nav_items(market):
        lbl, href = item[0], item[1]
        if len(item) > 2:
            is_active = bool(path) and (cur + '/').startswith(href.rstrip('/') + '/')
            drop_cls = 'nav-drop-link active' if is_active else 'nav-drop-link'
            dd = "".join('<li><a href="%s">%s</a></li>' % (u, n) for u, n in item[2])
            nav += ('<li class="nav-drop"><a href="%s" class="%s">%s'
                    '<svg width="10" height="10" viewBox="0 0 10 10" fill="none" aria-hidden="true">'
                    '<path d="M2 4l3 3 3-3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>'
                    '</svg></a><ul class="nav-dropdown">%s</ul></li>') % (href, drop_cls, lbl, dd)
        else:
            is_active = path and cur == href.rstrip('/')
            if not is_active:
                seg = href.rstrip('/').split('/')[-1]
                is_active = bool(path) and path.rstrip('/').split('/')[0] == seg and seg not in ("", "sk", "cz")
            cls = ' class="active"' if is_active else ''
            nav += '<li><a href="%s"%s>%s</a></li>' % (href, cls, lbl)
    mob_nav = ""
    for item in nav_items(market):
        lbl, href = item[0], item[1]
        mob_nav += '<a href="%s">%s</a>' % (href, lbl)
        if len(item) > 2:
            mob_nav += "".join('<a href="%s" class="mob-sub">%s</a>' % (u, n) for u, n in item[2])

    asset = (prefix.rstrip("/") + "/") if prefix else ""
    hreflang = hreflang_links(market, path)
    gsc_meta = f'  <meta name="google-site-verification" content="{GSC_TOKEN}">\n  ' if GSC_TOKEN else "  "

    return f"""<!DOCTYPE html>
<html lang="{ {'sk':'sk','cz':'cs'}[market] }">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{_html.escape(title)}</title>
  <meta name="description" content="{_html.escape(desc)}">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="{BRAND}">
  <meta property="og:locale" content="{OG_LOCALE[market]}">
  <meta property="og:title" content="{_html.escape(title)}">
  <meta property="og:description" content="{_html.escape(desc)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE}/assets/img/og-cover.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{_html.escape(title)}">
  <meta name="twitter:description" content="{_html.escape(desc)}">
  <meta name="twitter:image" content="{BASE}/assets/img/og-cover.png">
  <meta name="theme-color" content="#ffffff">
  <link rel="canonical" href="{canonical}">
{hreflang}
{gsc_meta}<meta name="msvalidate.01" content="{BING_TOKEN}">
  <link rel="icon" href="{asset}assets/img/favicon.svg" type="image/svg+xml">
  <link rel="icon" type="image/png" sizes="32x32" href="{asset}assets/img/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="{asset}assets/img/favicon-16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="{asset}assets/img/apple-touch-icon.png">
  <link rel="manifest" href="{asset}assets/img/site.webmanifest">
  <link rel="stylesheet" href="{asset}assets/css/main.css">
  <link rel="stylesheet" href="{asset}assets/css/components.css">
  <link rel="stylesheet" href="{asset}assets/css/animations.css">
  {extra_head}
</head>
<body>

<header class="site-header" id="site-header">
  <div class="container">
    <nav class="nav">
      {logo(market)}
      <ul class="nav-links">{nav}</ul>
      <div class="nav-right">
        {lang_toggle(market, path)}
        <a href="{PHONE_TEL}" class="btn btn-primary btn-sm nav-phone-btn">{PHONE_DISPLAY}</a>
        <button class="hamburger" id="hamburger" aria-label="Menu"><span></span><span></span><span></span></button>
      </div>
    </nav>
  </div>
</header>
<nav class="nav-mobile" id="nav-mobile">
  {mob_nav}
  <a href="{_market_url(market, 'kontakt/')}" class="btn btn-primary" style="margin-top:10px;">{cta_label(market)}</a>
  <a href="{PHONE_TEL}" class="mob-phone">{PHONE_DISPLAY}</a>
</nav>

{body}

{google_review_band(market)}

{footer(market, prefix)}

<script src="{asset}assets/js/clarity.js"></script>
<script src="{asset}assets/js/ga4.js"></script>
<script src="{asset}assets/js/nav.js"></script>
<script src="{asset}assets/js/animations.js"></script>
<script src="{asset}assets/js/forms.js"></script>
<script src="{asset}assets/js/audit-popup.js"></script>
<script src="{asset}assets/js/cookie-banner.js"></script>
</body>
</html>
"""


def footer(market: str, prefix: str) -> str:
    m_root = MARKET_ROOTS[market]
    o_root = MARKET_ROOTS["cz" if market == "sk" else "sk"]
    svc_cols = [("Služby", [(_market_url(market, p), n) for p, n in NICHE_NAV_SVC[market]])]
    col2 = ("Agentúra" if market == "sk" else "Agentura",
            [(_market_url(market, "jak-pracujeme/"), "Ako pracujem" if market == "sk" else "Jak pracuji"),
             (_market_url(market, "cennik/" if market == "sk" else "cenik/"), "Cenník" if market == "sk" else "Ceník"),
             (_market_url(market, "blog/"), "Blog"),
             (_market_url(market, "kontakt/"), "Kontaktný formulár" if market == "sk" else "Kontaktní formulář")])
    col3 = ("Sesterské weby",
            [(MAIN_SITE + "/", "Nokto Studio: hlavný web"),
             ("https://seoprewordpress.info/", "SEO pre WordPress"),
             ("https://seopreeshopy.pro/", "SEO pre e-shopy"),
             ("https://seoaudit.blog/", "SEO audit")])
    col4 = ("Kontakt",
            [(f"mailto:{EMAIL}", EMAIL),
             (PHONE_TEL, PHONE_DISPLAY),
             ("/sk/privacy/", "Ochrana súkromia" if market == "sk" else "Zásady ochrany osobních údajů"),
             ("/sk/terms/", "Obchodné podmienky" if market == "sk" else "Obchodní podmínky")])
    cols = svc_cols + [col2, col3, col4]
    rows = []
    for head, links in cols:
        lis = "".join(f'<li><a href="{u}">{n}</a></li>' for u, n in links)
        rows.append(f'<div class="footer-col"><h4>{head}</h4><ul>{lis}</ul></div>')
    copy = {"sk": "Nokto Studio. SEO pre podnikateľov.", "cz": "Nokto Studio. SEO pro podnikatele."}[market]
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">{"".join(rows)}</div>
    <div class="footer-bottom">
      <p>© 2026 {copy}</p>
      <p class="footer-links-inline"><a href="{_market_url(market, 'privacy/')}">{'Ochrana súkromia' if market == 'sk' else 'Zásady ochrany osobních údajů'}</a> · <a href="{_market_url(market, 'terms/')}">{'Obchodné podmienky' if market == 'sk' else 'Obchodní podmínky'}</a></p>
    </div>
  </div>
</footer>
"""


# ---------------------------------------------------------------- components

def page_hero(label: str, h1_html: str, sub: str, crumbs: list[tuple[str, str]] | None = None) -> str:
    crumb_html = ""
    if crumbs:
        parts = []
        for text, href in crumbs:
            if href:
                parts.append(f'<a href="{href}">{text}</a>')
            else:
                parts.append(f"<span>{text}</span>")
        crumb_html = '<nav class="breadcrumb" aria-label="Drobková navigácia">' + ' <span>›</span> '.join(parts) + "</nav>"
    return f"""
<section class="page-hero">
  <div class="container">
    {crumb_html}
    <span class="section-label">{label}</span>
    <h1>{h1_html}</h1>
    <div class="divider"></div>
    <p class="section-subheading">{sub}</p>
  </div>
</section>
"""


def cta_band(title: str, text: str, market: str) -> str:
    btn1 = {"sk": "Napíšte mi", "cz": "Napište mi"}[market]
    btn2 = {"sk": "Chcem bezplatný audit", "cz": "Chci bezplatný audit"}[market]
    call = {"sk": "Alebo zavolajte rovno:", "cz": "Nebo volejte rovnou:"}[market]
    audit_href = _market_url(market, "kontakt/") + "?audit=1"
    return f"""
<div class="cta-band">
  <div>
    <h2>{title}</h2>
    <p>{text}</p>
  </div>
  <div class="hero-ctas">
    <a href="{_market_url(market, 'kontakt/')}" class="btn btn-white btn-lg">{btn1}</a>
    <a href="{audit_href}" class="btn btn-outline btn-lg" style="border-color:rgba(255,255,255,0.3);color:#fff;">{btn2}</a>
  </div>
  <p class="cta-phone-line">{call} <a href="{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
</div>
"""


def faq_block(items: list[tuple[str, str]]) -> str:
    rows = "".join(
        f'<div class="faq-item"><button class="faq-question" type="button">{q}</button>'
        f'<div class="faq-answer"><p>{a}</p></div></div>' for q, a in items
    )
    return f'<div class="faq-list">{rows}</div>'


def faq_schema(items: list[tuple[str, str]], page_url: str) -> str:
    qas = ",".join(
        '{{"@type":"Question","name":{q},"acceptedAnswer":{{"@type":"Answer","text":{a}}}}}'.format(
            q=_json_str(q), a=_json_str(a)) for q, a in items
    )
    return f'<script type="application/ld+json">\n{{"@context":"https://schema.org","@type":"FAQPage","@id":"{page_url}#faq","mainEntity":[{qas}]}}\n</script>'


def _json_str(s: str) -> str:
    import json
    return json.dumps(s, ensure_ascii=False)


def steps_block(steps: list[dict]) -> str:
    nums = ["num-violet", "num-orange", "num-cerulean", "num-violet-light"]
    out = []
    for i, s in enumerate(steps):
        out.append(f"""
<div class="step">
  <span class="step-num {nums[i % 4]}">{i + 1}</span>
  <h3>{s['title']}</h3>
  <p>{s['text']}</p>
</div>""")
    return f'<div class="steps">{"".join(out)}</div>'


def benefit_cards(cards: list[dict]) -> str:
    icons = ["icon-violet", "icon-orange", "icon-cerulean", "icon-violet-light"]
    out = []
    for i, c in enumerate(cards):
        out.append(f"""
<div class="benefit-card card-hover reveal" data-delay="{(i + 1) * 100}">
  <span class="benefit-icon {icons[i % 4]}">{c['icon']}</span>
  <h3>{c['title']}</h3>
  <p>{c['text']}</p>
</div>""")
    return f'<div class="grid-3">{"".join(out)}</div>'


def kw_band(rows: list[tuple[str, int]], market: str) -> str:
    """Demand-proof band: real MM keyword volumes for this niche.
    rows: [(phrase, monthly_volume)], market = sk | cz."""
    if not rows:
        return ""
    head = {"sk": "Čo ľudia hľadajú (počty hľadaní za mesiac v Google)",
            "cz": "Co lidé hledají (počty hledání za měsíc v Google)"}[market]
    chips = "".join(
        f'<span class="logo-badge"><span style="font-weight:700; color:var(--text);">{_html.escape(k)}</span>'
        f'<span style="color:var(--brand-primary-deep); font-weight:800;">{v:,}</span></span>'.replace(",", " ")
        for k, v in rows
    )
    return f"""
<section class="logo-strip-section">
  <p class="logo-strip-heading">{head}</p>
  <div class="marquee-viewport">
    <div class="marquee-track">{chips}</div>
  </div>
</section>
"""


def org_schema(desc: str) -> str:
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "{BASE}/#organization",
  "name": "{BRAND}",
  "url": "{BASE}/",
  "logo": "{BASE}/assets/img/favicon.svg",
  "description": {_json_str(desc)},
  "email": "{EMAIL}",
  "areaServed": [{{"@type":"Country","name":"Slovakia"}},{{"@type":"Country","name":"Czech Republic"}}],
  "knowsLanguage": ["sk", "cs"]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "{BASE}/#website",
  "url": "{BASE}/",
  "name": "{BRAND}",
  "publisher": {{"@id": "{BASE}/#organization"}},
  "inLanguage": "sk"
}}
</script>"""


def roi_band(market: str, niche: str = "") -> str:
    """Return-on-investment band: what SEO can return for the monthly retainer.
    Numbers are honest examples, not promises: based on real client GSC data."""
    if market == "sk":
        title = "Predstava návratnosti: čo z toho môže mať váš web"
        rows = [
            ("120 EUR", "mesačne (10 hodín)", "Malý web: 5 až 10 nových zákazníkov mesačne z Google = návratnosť už pri jednej objednávke."),
            ("144 EUR", "mesačne (12 hodín)", "Web s obsahom: každý nový článok je dlhodobý zdroj zákazníkov, nie jednorazová reklama."),
            ("180 EUR", "mesačne (15 hodín)", "E-shop alebo blog: obsah, ktorý pracuje mesiace po zverejnení, bez platenej reklamy."),
        ]
    else:
        title = "Představa návratnosti investice do SEO"
        rows = [
            ("120 EUR", "měsíčně (10 hodin)", "Malý web: 5 až 10 nových zákazníků měsíčně z Google = návratnost už při jedné objednávce."),
            ("144 EUR", "měsíčně (12 hodin)", "Web s obsahem: každý článek je dlouhodobý zdroj zákazníků, ne jednorázová reklama."),
            ("180 EUR", "měsíčně (15 hodin)", "E-shop nebo blog: obsah, který pracuje měsíce po zveřejnění, bez placené reklamy."),
        ]
    cells = "".join(
        f'<div class="benefit-card card-hover reveal" data-delay="{(i + 1) * 100}" style="background:rgba(255,255,255,0.08); border:none;">'
        f'<div class="roi-num" style="color:#fff;">{amt}<small>{per}</small></div>'
        f'<p class="roi-note" style="color:rgba(255,255,255,0.92);">{note}</p>'
        f'</div>' for i, (amt, per, note) in enumerate(rows))
    return f"""
<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="roi-band" style="display:block; padding:44px 40px;">
      <h2 style="color:#fff; margin:0 0 8px; font-size:1.6rem;">{title}</h2>
      <p class="roi-note" style="margin:0 0 26px;">{'Retainer nie je náklad, ale investícia: jedna objednávka z Google ju zvyčajne pokryje.' if market == 'sk' else 'Retainer není náklad, ale investice: jedna objednávka z Google ji obvykle pokryje.'}</p>
      <div class="pricing-grid">{cells}</div>
      <p style="font-size:0.78rem; opacity:0.7; margin:18px 0 0;">{'Odhady na základe reálnych dát klientov z Google Search Console. Presný predik vám dá bezplatný audit.' if market == 'sk' else 'Odhady na základě dat klientů z Google Search Console. Přesnou predikci vám dá bezplatný audit.'}</p>
    </div>
  </div>
</section>"""


def schema_service(name: str, desc: str, url: str, offers_hours: int = 10) -> str:
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "{url}#service",
  "name": {_json_str(name)},
  "description": {_json_str(desc)},
  "provider": {{"@id": "{BASE}/#organization"}},
  "areaServed": ["SK", "CZ"],
  "url": "{url}",
  "offers": {{
    "@type": "Offer",
    "price": "12",
    "priceCurrency": "EUR",
    "unitText": "hour",
    "url": "{url}"
  }}
}}
</script>"""


# VIOLET constant for chart reuse
_VIOLET = "#7A50D6"
_ORANGE = "#F75940"
_CERULEAN = "#1DACD6"
_VIOLET_L = "#9B6FD9"


def _sparkline(points: list[int], color: str, w: int = 560, h: int = 120, pad: int = 10) -> str:
    mx, mn = max(points), min(points)
    rng = (mx - mn) or 1
    step = (w - 2 * pad) / max(1, len(points) - 1)
    pts = [round(pad + i * step, 1) for i in range(len(points))]
    ys = [round(h - pad - (v - mn) / rng * (h - 2 * pad), 1) for v in points]
    line = " ".join(f"{x},{y}" for x, y in zip(pts, ys))
    area = f"{pts[0]},{h-pad} {line} {pts[-1]},{h-pad}"
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-hidden="true" preserveAspectRatio="none">'
            f'<polygon points="{area}" fill="{color}" opacity="0.12"/>'
            f'<polyline points="{line}" fill="none" stroke="{color}" stroke-width="3" '
            f'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def _bars(values: list[int], color: str, labels: list[str] | None = None,
          w: int = 560, h: int = 140) -> str:
    n = len(values)
    bw = min(64, (w - 40) / (n * 1.6))
    gap = (w - 40 - n * bw) / max(1, n - 1)
    mx = max(values) or 1
    out = []
    for i, v in enumerate(values):
        bh = (v / mx) * (h - 54)
        x = 20 + i * (bw + gap)
        y = h - 26 - bh
        opacity = 1.0 if i == n - 1 else 0.45
        out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="4" fill="{color}" opacity="{opacity}"/>')
        if labels and i < len(labels):
            out.append(f'<text x="{x + bw / 2:.1f}" y="{h - 6}" text-anchor="middle" font-size="11" fill="#5F6368" font-family="Manrope,sans-serif">{labels[i]}</text>')
    return f'<svg viewBox="0 0 {w} {h}" role="img" aria-hidden="true">{"".join(out)}</svg>'


def _donut(parts: list[tuple[int, str, str]], w: int = 160, h: int = 160) -> str:
    import math
    total = sum(p[0] for p in parts)
    r = 60
    c = 2 * math.pi * r
    offset = 0.0
    out = []
    for val, color, _lbl in parts:
        dash = c * val / total
        out.append(f'<circle cx="{w//2}" cy="{h//2}" r="{r}" fill="none" stroke="{color}" stroke-width="24" '
                   f'stroke-dasharray="{dash:.1f} {c - dash:.1f}" stroke-dashoffset="{-offset:.1f}" transform="rotate(-90 {w//2} {h//2})"/>')
        offset += dash
    return f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-hidden="true" style="width:{w}px;height:{h}px;display:block;margin:0 auto;">{"".join(out)}</svg>'


def _slide(client: str, chip: str, period: str, nums: list[dict], chart: str,
           caption: str, market: str, logo: str | None = None) -> str:
    logo_html = ""
    if logo:
        logo_html = f'<img src="/assets/img/logos/{logo}" alt="{client}" loading="lazy" style="height:34px; width:auto; object-fit:contain;">'
    nums_html = "".join(
        f'<div class="rs-num"><strong style="color:{n["color"]};">{n["big"]}</strong><span>{n["label"]}</span></div>'
        for n in nums)
    chip_html = f'<span class="rs-chip">{chip}</span>' if chip and not logo else ""
    return f"""
<div class="rs-slide">
  <div class="rs-card">
    <div class="rs-head">
      <div><h3>{client}</h3><span class="rs-period">{period}</span></div>
      {chip_html}{logo_html}
    </div>
    <div class="rs-chart">{chart}</div>
    <div class="rs-nums">{nums_html}</div>
    <p class="rs-caption">{caption}</p>
    <p class="rs-source">Zdroj: Google Search Console</p>
  </div>
</div>"""


def results_slider(market: str, slides: list[dict] | None = None) -> str:
    """Slider of real client results. Pass niche-specific slides or get the
    default noktostudio set."""
    t = {
        "sk": {"label": "Moje výsledky", "head": "Čísla z praxe, nie obrázky zo šablóny",
               "sub": "Skutočné ukážky z Google Search Console a Google AI Mode mojich projektov a klientov. Čísla vám pred spoluprácou ukážem naživo.",
               "prev": "Predchádzajúci", "next": "Nasledujúci", "all": "Všetky výsledky", "case_url": "/sk/vysledky/"},
        "cz": {"label": "Moje výsledky", "head": "Čísla z praxe, ne obrázky ze šablony",
               "sub": "Skutečné ukázky z Google Search Console a Google AI Mode mých projektů a klientů. Čísla vám před spoluprací ukážu naživo.",
               "prev": "Předchozí", "next": "Další", "all": "Všechny výsledky", "case_url": "/cz/vysledky/"},
    }[market]
    if not slides:
        return ""
    built = []
    for s in slides:
        built.append(_slide(s["client"], s.get("chip", ""), s["period"], s["nums"], s["chart"],
                            s["caption"], market, logo=s.get("logo")))
    dots = '<span class="rs-dot active" data-i="0"></span>' + \
           "".join(f'<span class="rs-dot" data-i="{i}"></span>' for i in range(1, len(slides)))
    return f"""
<section class="section section-alt" id="vysledky">
  <div class="container">
    <div class="section-head">
      <span class="section-label">{t['label']}</span>
      <h2>{t['head']}</h2>
      <p class="section-subheading">{t['sub']}</p>
    </div>
    <div class="results-slider">
      <button class="rs-btn rs-prev" aria-label="{t['prev']}">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M12.5 4 6.5 10l6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <div class="rs-viewport" tabindex="0">{"".join(built)}</div>
      <button class="rs-btn rs-next" aria-label="{t['next']}">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="m7.5 4 6 6-6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <div class="rs-dots">{dots}</div>
    </div>
  </div>
</section>
"""

def article_schema(*, url: str, title: str, desc: str, date_iso: str,
                   lang: str = "sk") -> str:
    """BlogPosting JSON-LD for a blog post, referencing the Organization @id."""
    lang_name = {"sk": "Šimon Štermenský", "cz": "Šimon Štermenský"}[lang]
    return (
        '<script type="application/ld+json">\n'
        f'{{"@context":"https://schema.org","@type":"BlogPosting","@id":"{url}#article",'
        f'"mainEntityOfPage":{{"@type":"WebPage","@id":"{url}"}},'
        f'"headline":{_json_str(title)},"description":{_json_str(desc)},'
        f'"datePublished":"{date_iso}","dateModified":"{date_iso}",'
        f'"author":{{"@type":"Person","name":{_json_str(lang_name)},"url":"{BASE}/"}},'
        f'"publisher":{{"@id":"{BASE}/#organization"}},'
        f'"url":"{url}","image":"{BASE}/assets/img/og-cover.png","inLanguage":"{lang}"}}\n'
        "</script>"
    )
