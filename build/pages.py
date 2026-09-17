# -*- coding: utf-8 -*-
"""
Niche site pages (seosem-servisy family).

Every page is (rel_path, html). Content comes from config.py; copy adapts
to the niche through NICHE copy dicts defined here. Language: SK primary
(root + /sk/), CZ mirror (/cz/).
"""
from engine import (base, page_hero, cta_band, faq_block, faq_schema, roi_band,
                    steps_block, benefit_cards, kw_band, org_schema,
                    schema_service, results_slider, gicon, EMAIL, MAIN_SITE)
import config as cfg
from copy import COPY
from content import (SERVICE_DEFS, SERVICE_DEFS_TEXT, SERVICE_DEFS_ICON,
                     SERVICE_DEFS_COLOR, SERVICE_DEFS_TAG, SLIDES, PROCESS,
                     FAQ, DETAIL, DETAIL_FAQ, BLOG_POSTS)

SK_ROOT = "/sk/"


# ---------------------------------------------------------------- helpers

def _svc_card(href, title, text, icon, color, tag, delay):
    return f"""
<div class="benefit-card card-hover reveal" data-delay="{delay}">
  <span class="benefit-icon">{gicon(icon, color, 26)}</span>
  <h3><a href="{href}" style="color:var(--text);">{title}</a></h3>
  <p>{text}</p>
  <div class="project-tags"><span class="project-tag {tag}">Služba</span></div>
</div>"""


def _process_steps(market):
    t = PROCESS[market]
    return steps_block([
        {"title": t["s1_t"], "text": t["s1_x"]},
        {"title": t["s2_t"], "text": t["s2_x"]},
        {"title": t["s3_t"], "text": t["s3_x"]},
        {"title": t["s4_t"], "text": t["s4_x"]},
    ])


# ---------------------------------------------------------------- page: home

def home(market: str = "sk") -> tuple[str, str]:
    c = COPY[market]
    root = cfg.engine.MARKET_ROOTS[market]
    hero_ctas = f"""
<div class="hero-ctas">
  <a href="tel:+421917316105" class="btn btn-primary btn-lg">Zavolajte +421 917 316 105</a>
  <a href="{root}kontakt/" class="btn btn-outline btn-lg">{c['hero_cta2']}</a>
</div>"""

    svc_cards = []
    for i, ((p, lbl, txt), icon, color, tag) in enumerate(zip(_svc_items(market), SERVICE_DEFS_ICON, SERVICE_DEFS_COLOR, SERVICE_DEFS_TAG)):
        svc_cards.append(_svc_card(cfg.engine._market_url(market, p), lbl, txt, icon, color, tag, (i + 1) * 100))
    svc_cards = "".join(svc_cards)

    body = f"""
<section class="hero">
  <div class="container">
    <div class="hero-flex">
      <div class="hero-content">
        <span class="hero-label">{c['hero_label']}</span>
        <h1>{c['h1']}</h1>
        <p class="hero-sub">{c['hero_sub']}</p>
        {hero_ctas}
        <p class="hero-scarcity">Alebo napíšte: <a href="{root}kontakt/" style="font-weight:700; color:var(--text); text-decoration:none;">kontaktný formulár</a> · <a href="mailto:{EMAIL}" style="font-weight:700; color:var(--text); text-decoration:none;">{EMAIL}</a></p>
        <p class="hero-scarcity" style="margin-top:6px;">Kapacita na nové projekty: otvorené od októbra 2026.</p>
      </div>
      <div class="hero-photo">
        <img src="/assets/img/simon.png" alt="Šimon Štermenský, SEO špecialista a majiteľ Nokto Studio" width="220" height="220" loading="eager">
        <span class="hero-photo-cap">Šimon Štermenský<br>SEO špecialista · Nokto Studio</span>
      </div>
    </div>
  </div>
</section>

{kw_band(cfg.KW_PROOF_SK if market == 'sk' else cfg.KW_PROOF_CZ, market)}

{results_slider(market, SLIDES)}

<!-- SERVICES -->
<section class="section section-alt" id="sluzby">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Služby</span>
      <h2>{c['svc_head']}</h2>
      <p class="section-subheading">{c['svc_sub']}</p>
    </div>
    <div class="grid-2">{svc_cards}</div>
    <div style="text-align:center; margin-top:36px;">
      <a href="{root}cennik/" class="btn btn-outline">{c['svc_cta']}</a>
    </div>
  </div>
</section>

{roi_band(market)}
{cta_band(c['cta_t'], c['cta_x'], market)}
"""
    canonical = cfg.engine.BASE + cfg.engine.MARKET_HOME[market]
    rel = "index.html" if market == "sk" else "cz/index.html"
    pre = "" if market == "sk" else ".."
    html = base(market=market, path="" if market == "sk" else "",
                title=c['title'], desc=c['desc'], canonical=canonical,
                body=body, prefix=pre, extra_head=org_schema(c['org_desc']))
    return (rel, html)


# ---------------------------------------------------------------- page: sluzby hub

def sluzby(market: str = "sk") -> tuple[str, str]:
    c = COPY[market]
    root = cfg.engine.MARKET_ROOTS[market]
    cards = "".join(
        _svc_card(cfg.engine._market_url(market, p), lbl, txt, icon, color, tag, (i + 1) * 100)
        for i, ((p, lbl, txt), icon, color, tag)
        in enumerate(zip(_svc_items(market), SERVICE_DEFS_ICON, SERVICE_DEFS_COLOR, SERVICE_DEFS_TAG))
    )
    body = f"""
{page_hero("Služby", c['hub_h1'], c['hub_sub'], [("Domov", cfg.engine.MARKET_HOME[market]), ("Služby", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2">{cards}</div>
  </div>
</section>
{faq_section(market, 'sluzby')}
{cta_band(c['cta_t'], c['cta_x'], market)}
"""
    path = "sluzby/" if market == "sk" else "sluzby/"
    html = base(market=market, path=path, title=c['hub_title'], desc=c['hub_desc'],
                canonical=cfg.engine.BASE + cfg.engine.MARKET_ROOTS[market] + path,
                body=body, prefix="../..", extra_head=org_schema(c['org_desc']))
    return ((root + path + "index.html").lstrip('/'), html)


def _svc_items(market):
    pairs = []
    for i, ((p_sk, p_cz, lbl_sk, lbl_cz), (txt_sk, txt_cz)) in enumerate(zip(SERVICE_DEFS, SERVICE_DEFS_TEXT)):
        if market == "sk":
            pairs.append((p_sk, lbl_sk, txt_sk))
        else:
            pairs.append((p_cz, lbl_cz, txt_cz))
    return pairs


# ---------------------------------------------------------------- page: service detail

def service_detail(idx: int, market: str = "sk") -> tuple[str, str]:
    """One service detail page, built from SERVICE_DEFS[idx] + DETAIL copy."""
    c = COPY[market]
    (p_sk, p_cz, lbl_sk, lbl_cz) = SERVICE_DEFS[idx]
    d = DETAIL[idx][market]
    path = p_sk if market == "sk" else p_cz
    label = lbl_sk if market == "sk" else lbl_cz
    root = cfg.engine.MARKET_ROOTS[market]

    body = f"""
{page_hero(c['svc_label'], d['h1'], d['sub'], [("Domov", cfg.engine.MARKET_HOME[market]), ("Služby", cfg.engine.MARKET_ROOTS[market] + "sluzby/"), (label, None)])}
<section class="section">
  <div class="container">
    <div class="grid-2">
      <div class="benefit-card card-hover">
        <span class="benefit-icon">{gicon(SERVICE_DEFS_ICON[idx], SERVICE_DEFS_COLOR[idx], 26)}</span>
        <h3>{d['b1_t']}</h3>
        <p>{d['b1_x']}</p>
      </div>
      <div class="benefit-card card-hover">
        <span class="benefit-icon icon-orange">{gicon(SERVICE_DEFS_ICON[(idx + 1) % 4], SERVICE_DEFS_COLOR[(idx + 1) % 4], 26)}</span>
        <h3>{d['b2_t']}</h3>
        <p>{d['b2_x']}</p>
      </div>
    </div>
    <h2 style="margin-top:42px;">{d['what_t']}</h2>
    <p class="section-subheading">{d['what_x']}</p>
    {_process_steps(market)}
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Cenník</span>
      <h2>12 EUR za hodinu. Platíte len za prácu.</h2>
    </div>
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>za hodinu práce</small></div>
        <p style="margin-top:8px; max-width:520px;">Balíčky sú len odporúčané rozsahy. Kedykoľvek ich môžete meniť, bez sankcií.</p>
      </div>
      <a href="{root}cennik/" class="btn btn-primary btn-lg">Pozrieť celý cenník</a>
    </div>
  </div>
</section>
{faq_section(market, 'detail', DETAIL_FAQ[idx][market])}
{cta_band(c['cta_t'], c['cta_x'], market)}
"""
    html = base(market=market, path=path, title=d['title'], desc=d['desc'],
                canonical=cfg.engine.BASE + cfg.engine.MARKET_ROOTS[market] + path,
                body=body, prefix="../../../",
                extra_head=org_schema(c['org_desc']) + schema_service(label, d['desc'],
                    cfg.engine.BASE + cfg.engine.MARKET_ROOTS[market] + path))
    return ((cfg.engine.MARKET_ROOTS[market] + path + "index.html").lstrip('/'), html)


# ---------------------------------------------------------------- page: cennik

def cennik(market: str = "sk") -> tuple[str, str]:
    c = COPY[market]
    root = cfg.engine.MARKET_ROOTS[market]
    price_dir = "cennik" if market == "sk" else "cenik"
    cards = c['price_cards']
    out = []
    for card in cards:
        feat = " featured" if card.get('featured') else ""
        badge = f'<span class="price-badge">{c["price_badge"]}</span>' if card.get('featured') else ""
        lis = "".join(f"<li>{i}</li>" for i in card['items'])
        out.append(f"""
<div class="price-card{feat}">
  {badge}
  <span class="price-hours">{card['name']}</span>
  <div class="price-amount">{card['price']}<small> EUR / {c['price_period']}</small></div>
  <div class="price-monthly"><strong>{card['hours']}</strong> × 12 EUR / hod.</div>
  <ul>{lis}</ul>
  <a href="{root}kontakt/" class="btn btn-primary">{c['price_cta']}</a>
</div>""")
    body = f"""
{page_hero("Cenník", c['price_h1'], c['price_sub'], [("Domov", cfg.engine.MARKET_HOME[market]), (c['price_label'], None)])}
<section class="section">
  <div class="container">
    <div class="pricing-grid">{"".join(out)}</div>
    <p style="text-align:center; margin-top:26px; color:var(--text-muted);">{c['price_note']}</p>
  </div>
</section>
{faq_section(market, 'cennik')}
{roi_band(market)}
{cta_band(c['cta_t'], c['cta_x'], market)}
"""
    html = base(market=market, path=price_dir + "/", title=c['price_title'], desc=c['price_desc'],
                canonical=cfg.engine.BASE + ("sk/" if market == "sk" else "cz/") + price_dir + "/",
                body=body, prefix="../../", extra_head=org_schema(c['org_desc']))
    return (("sk/" if market == "sk" else "cz/") + price_dir + "/index.html", html)


# ---------------------------------------------------------------- page: jak pracujeme

def jak_pracujeme(market: str = "sk") -> tuple[str, str]:
    c = COPY[market]
    price_dir = "cennik" if market == "sk" else "cenik"
    body = f"""
{page_hero("Proces", c['proc_h1'], c['proc_sub'], [("Domov", cfg.engine.MARKET_HOME[market]), ("Ako pracujem" if market == 'sk' else "Jak pracuji", None)])}
<section class="section">
  <div class="container">
    {_process_steps(market)}
    <div class="rate-band" style="margin-top:40px;">
      <div>
        <div class="rate-big">12 EUR <small>za hodinu práce</small></div>
        <p style="margin-top:8px; max-width:520px;">Každá hodina je vykázaná v mesačnom reporte. Žiadne paušály, žiadne skryté položky.</p>
      </div>
      <a href="/{price_dir}/" class="btn btn-primary btn-lg">Pozrieť celý cenník</a>
    </div>
  </div>
</section>
{faq_section(market, 'proces')}
{cta_band(c['cta_t'], c['cta_x'], market)}
"""
    html = base(market=market, path="jak-pracujeme/", title=c['proc_title'], desc=c['proc_desc'],
                canonical=cfg.engine.BASE + cfg.engine.MARKET_ROOTS[market] + "jak-pracujeme/",
                body=body, prefix="../..", extra_head=org_schema(c['org_desc']))
    return (cfg.engine.MARKET_ROOTS[market].lstrip('/') + "jak-pracujeme/index.html", html)


# ---------------------------------------------------------------- page: blog hub

def blog(market: str = "sk") -> tuple[str, str]:
    c = COPY[market]
    root = cfg.engine.MARKET_ROOTS[market]
    rows = ""
    for slug, art in _content.BLOG_ARTICLES.items():
        a = art[market]
        rows += f"""
<div class="project-card card-hover">
  <div class="project-card-body">
    <h3><a href="{root}blog/{slug}/" style="color:var(--text);">{a['h1']}</a></h3>
    <p>{a['answer'][:160]}...</p>
    <div class="project-tags"><span class="project-tag tag-violet">{a['label']}</span></div>
  </div>
</div>"""
    body = f"""
{page_hero("Blog", c['blog_h1'], c['blog_sub'], [("Domov", cfg.engine.MARKET_HOME[market]), ("Blog", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2">{rows}</div>
  </div>
</section>
{cta_band(c['cta_t'], c['cta_x'], market)}
"""
    html = base(market=market, path="blog/", title=c['blog_title'], desc=c['blog_desc'],
                canonical=cfg.engine.BASE + cfg.engine.MARKET_ROOTS[market] + "blog/",
                body=body, prefix="../..", extra_head=org_schema(c['org_desc']))
    return (cfg.engine.MARKET_ROOTS[market].lstrip('/') + "blog/index.html", html)


# ---------------------------------------------------------------- page: kontakt

def kontakt(market: str = "sk") -> tuple[str, str]:
    c = COPY[market]
    root = cfg.engine.MARKET_ROOTS[market]
    goals = "".join(f'<option>{g}</option>' for g in c['form_goals'])
    body = f"""
{page_hero("Kontakt", c['k_h1'], c['k_sub'], [("Domov", cfg.engine.MARKET_HOME[market]), ("Kontakt", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="card" style="text-align:center;">
        <span class="section-label">{c['k_call_label']}</span>
        <a href="tel:+421917316105" class="btn btn-primary btn-lg contact-phone-btn" style="width:100%; margin-top:14px; font-size:1.25rem;">+421 917 316 105</a>
        <p style="margin:14px 0 6px; color:var(--text-muted);">{c['k_call_note']}</p>
        <ul class="deliv-list" style="text-align:left; margin-top:20px;">
          <li><span class="check">✓</span><span>{c['k_li1']}</span></li>
          <li><span class="check">✓</span><span>{c['k_li2']}</span></li>
          <li><span class="check">✓</span><span>{c['k_li3']}</span></li>
          <li><span class="check">✓</span><span>{c['k_li4']}</span></li>
        </ul>
        <p style="margin-top:22px; border-top:1px solid var(--border-light); padding-top:18px;">
          Email: <a href="mailto:{EMAIL}" style="font-weight:700; color:var(--text);">{EMAIL}</a>
        </p>
        <a href="mailto:{EMAIL}" class="btn btn-outline" style="width:100%; margin-top:10px;">{c['k_email_btn']}</a>
      </div>
      <div class="card contact-form-wrap">
        <span class="section-label">{c['k_form_label']}</span>
        <form class="contact-form-el" style="margin-top:16px;">
          <div class="form-grid">
            <div class="form-field"><label class="form-label" for="name">{'Meno a firma *' if market == 'sk' else 'Jméno a firma *'}</label><input class="form-input" id="name" name="name" type="text" required></div>
            <div class="form-field"><label class="form-label" for="email">{'Email *' if market == 'sk' else 'E-mail *'}</label><input class="form-input" id="email" name="email" type="email" required></div>
            <div class="form-field full"><label class="form-label" for="url">{'Adresa webu (ak máte)' if market == 'sk' else 'Adresa webu (pokud máte)'}</label><input class="form-input" id="url" name="url" type="url" placeholder="https://"></div>
            <div class="form-field full"><label class="form-label" for="goal">{'Čo je váš cieľ? *' if market == 'sk' else 'Co je váš cíl? *'}</label>
              <select class="form-select" id="goal" name="goal" required>
                <option value="">{c['form_select_placeholder']}</option>
                {goals}
              </select>
            </div>
            <div class="form-field full"><label class="form-label" for="msg">{'Správa' if market == 'sk' else 'Zpráva'}</label><textarea class="form-textarea" id="msg" name="msg" placeholder="{c['form_placeholder']}"></textarea></div>
          </div>
          <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
          <input type="hidden" name="_subject" value="{c['form_subject']}">
          <button type="submit" class="btn btn-primary" style="margin-top:18px; width:100%;">{c['form_btn']}</button>
          <p class="form-note">{c['form_note'].replace('{privacy_link}', root + 'privacy/')}</p>
        </form>
        <div class="form-success" style="display:none; margin-top:16px; background:#F5F1FC; color:var(--brand-cool-deep); padding:16px; border-radius:10px;">
          ✓ {c['form_success']}
        </div>
      </div>
    </div>
  </div>
</section>
"""
    html = base(market=market, path="kontakt/", title=c['k_title'], desc=c['k_desc'],
                canonical=cfg.engine.BASE + root + "kontakt/",
                body=body, prefix="../..", extra_head=org_schema(c['org_desc']))
    return (root.lstrip('/') + "kontakt/index.html", html)


# ---------------------------------------------------------------- page: privacy + terms

def privacy(market: str = "sk") -> tuple[str, str]:
    c = COPY[market]
    body = f"""
{page_hero("Súkromie", c['pr_h1'], c['pr_sub'], [("Domov", cfg.engine.MARKET_HOME[market]), ("Ochrana súkromia" if market == 'sk' else "Zásady ochrany osobních údajů", None)])}
<section class="section">
  <div class="container prose">
    <h2>{c['pr_who_t']}</h2>
    <p>{c['pr_who_x']}</p>
    <h2>{c['pr_what_t']}</h2>
    <ul><li>{c['pr_li1']}</li><li>{c['pr_li2']}</li><li>{c['pr_li3']}</li></ul>
    <h2>{c['pr_ret_t']}</h2>
    <p>{c['pr_ret_x']}</p>
    <h2>{c['pr_rights_t']}</h2>
    <p>{c['pr_rights_x']}</p>
    <h2>Cookies</h2>
    <p>{c['pr_cookies']}</p>
  </div>
</section>
"""
    html = base(market=market, path="privacy/", title=c['pr_title'], desc=c['pr_desc'],
                canonical=cfg.engine.BASE + cfg.engine.MARKET_ROOTS[market] + "privacy/",
                body=body, prefix="../..", extra_head="")
    return (cfg.engine.MARKET_ROOTS[market].lstrip('/') + "privacy/index.html", html)


def terms(market: str = "sk") -> tuple[str, str]:
    c = COPY[market]
    body = f"""
{page_hero("Podmienky", c['tm_h1'], c['tm_sub'], [("Domov", cfg.engine.MARKET_HOME[market]), ("Obchodné podmienky" if market == 'sk' else "Obchodní podmínky", None)])}
<section class="section">
  <div class="container prose">
    <h2>{c['tm1_t']}</h2>
    <p>{c['tm1_x']}</p>
    <h2>{c['tm2_t']}</h2>
    <p>{c['tm2_x']}</p>
    <h2>{c['tm3_t']}</h2>
    <p>{c['tm3_x']}</p>
  </div>
</section>
"""
    html = base(market=market, path="terms/", title=c['tm_title'], desc=c['tm_desc'],
                canonical=cfg.engine.BASE + cfg.engine.MARKET_ROOTS[market] + "terms/",
                body=body, prefix="../..", extra_head="")
    return (cfg.engine.MARKET_ROOTS[market].lstrip('/') + "terms/index.html", html)


# ---------------------------------------------------------------- FAQ plumbing

def faq_section(market: str, kind: str, items=None) -> str:
    """Renders FAQ block only; schema is injected per page via extra_head when needed."""
    if items is None:
        items = FAQ[market].get(kind) or FAQ[market].get("common") or []
    return f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">{'Časté otázky' if market == 'sk' else 'Časté otázky'}</span>
      <h2>{COPY[market]['faq_h2']}</h2>
    </div>
    {faq_block(items)}
  </div>
</section>"""


def faq_schema_head(market: str, kind: str, page_url: str) -> str:
    items = FAQ[market].get(kind) or []
    return faq_schema(items, page_url)


# ---------------------------------------------------------------- build all

def build_all() -> list[tuple[str, str]]:
    pages: list[tuple[str, str]] = []
    pages.append(home("sk"))
    pages.append(home("cz"))
    pages.append(sluzby("sk"))
    pages.append(sluzby("cz"))
    for i in range(len(SERVICE_DEFS)):
        pages.append(service_detail(i, "sk"))
        pages.append(service_detail(i, "cz"))
    pages.append(cennik("sk"))
    pages.append(cennik("cz"))
    pages.append(jak_pracujeme("sk"))
    pages.append(jak_pracujeme("cz"))
    pages.append(blog("sk"))
    pages.append(blog("cz"))
    pages.append(kontakt("sk"))
    pages.append(kontakt("cz"))
    pages.append(privacy("sk"))
    pages.append(privacy("cz"))
    pages.append(terms("sk"))
    pages.append(terms("cz"))
    pages.extend(build_all_blogposts())
    return pages

# ---------------------------------------------------------------- blog posts

import re as _re
import content as _content


def blog_post(slug: str, market: str = "sk") -> tuple[str, str]:
    """One blog post page: direct answer first, sections, FAQ, related, CTA.
    Content comes from content.BLOG_ARTICLES[slug][market]."""
    art = _content.BLOG_ARTICLES[slug][market]
    root = cfg.engine.MARKET_ROOTS[market]
    related = ""
    for rslug, rtitle in art["related"]:
        related += (f'<div class="benefit-card card-hover related-card">'
                    f'<h3><a href="{root}blog/{rslug}/" style="color:var(--text);">{rtitle}</a></h3></div>')
    sections = _re.sub(r"<h2>Stručná odpoveď</h2>\s*<p>.*?</p>", "", art["sections"], count=1, flags=_re.S)
    body = f"""
<section class="post-hero">
  <div class="container" style="max-width:820px;">
    <a href="{root}blog/" class="post-back">← Blog</a>
    <span class="section-label">{art['label']}</span>
    <h1>{art['h1']}</h1>
    <p class="post-meta">{art['date_display']} · Šimon Štermenský · Nokto Studio</p>
  </div>
</section>

<article class="section" style="padding-top:16px;">
  <div class="container" style="max-width:820px;">
    <div class="prose">
      <div class="post-answer"><p>{art['answer']}</p></div>
{sections}
    </div>
  </div>
</article>

<section class="section" style="padding-top:0;">
  <div class="container" style="max-width:820px;">
    <div class="section-head"><span class="section-label">FAQ</span><h2>{COPY[market]['faq_h2']}</h2></div>
    {faq_block(art['faq'])}
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container" style="max-width:820px;">
    <div class="section-head"><span class="section-label">{'Prečítať aj' if market == 'sk' else 'Přečtěte také'}</span><h2>{'Súvisiace články' if market == 'sk' else 'Související články'}</h2></div>
    <div class="grid-2">{related}</div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band(COPY[market]['cta_t'], COPY[market]['cta_x'], market)}
  </div>
</section>
"""
    url = cfg.engine.BASE + root + f"blog/{slug}/"
    from engine import article_schema
    html = base(market=market, path=f"blog/{slug}/", title=art["title"], desc=art["desc"],
                canonical=url, body=body, prefix="../../../", og_type="article",
                extra_head=org_schema(COPY[market]['org_desc']) + article_schema(url=url, title=art["title"],
                                                       desc=art["desc"], date_iso=art["date_iso"], lang=market)
                          + faq_schema(art["faq"], url))
    return (root.lstrip('/') + f"blog/{slug}/index.html", html)


def build_all_blogposts() -> list[tuple[str, str]]:
    out = []
    for slug in _content.BLOG_ARTICLES:
        for market in ("sk", "cz"):
            out.append(blog_post(slug, market))
    return out
