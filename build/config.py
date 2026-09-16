# -*- coding: utf-8 -*-
"""
Niche site configuration. Edit THIS file per niche domain, then run
`python3 build_site.py` from the repo root.

Everything the engine and pages need that differs per niche lives here:
brand name, domain, keyword families with real Marketing Miner volumes,
service nav, hreflang map, verification tokens.
"""
import engine
from engine import _json_str

# ---------------------------------------------------------------- identity

BASE = "https://seoprewordpress.info"
BRAND = "SEO pre WordPress"
BRAND_TAGLINE = "SEO optimalizácia WordPress webov. Nokto Studio."

NICHE_KEY = "wordpress"
MAIN_DOMAIN = "seoprewordpress.info"

# ---------------------------------------------------------------- keywords
# Real Marketing Miner monthly search volumes (SK market unless noted).
# Used on home: demand-proof band + FAQ/heading coverage targets.
KW_PROOF_SK = [
    ("wordpress seo", 360),
    ("seo optimalizacia wordpress", 130),
    ("seo blog wordpress", 120),
    ("wordpress seo plugin", 40),
    ("seo optimalizácia web stránok", 500),
]
KW_PROOF_CZ = [
    ("seo optimalizace wordpress", 20),
    ("wordpress seo optimalizace", 10),
    ("seo optimalizace webu", 130),
]

# ---------------------------------------------------------------- services
# (sk_path, cz_path, SK label, CZ label) - nav dropdown + footer + sluzby hub
SERVICES = [
    ("sluzby/seo-optimalizacia/", "sluzby/seo-optimalizace/",
     "SEO optimalizácia WordPress webu", "SEO optimalizace WordPress webu"),
    ("sluzby/technicke-seo/", "sluzby/technicke-seo/",
     "Technické SEO a rýchlosť WordPressu", "Technické SEO a rychlost WordPressu"),
    ("sluzby/obsah-a-blog/", "sluzby/obsah-a-blog/",
     "Obsah a blog na WordPress", "Obsah a blog na WordPress"),
    ("sluzby/wordpress-audit/", "sluzby/wordpress-audit/",
     "SEO audit WordPress webu", "SEO audit WordPress webu"),
]

# ---------------------------------------------------------------- nav hookup
NICHE_NAV_SVC = {
    "sk": [(p_sk, lbl_sk) for (p_sk, _p_cz, lbl_sk, _lbl_cz) in SERVICES],
    "cz": [(p_cz, lbl_cz) for (_p_sk, p_cz, _lbl_sk, lbl_cz) in SERVICES],
}
engine.NICHE_NAV_SVC = NICHE_NAV_SVC

SK_PATHS = {
    "", "sluzby/", "cennik/", "jak-pracujeme/", "blog/", "kontakt/",
    "privacy/", "terms/",
} | {s[0] for s in SERVICES}
CZ_PATHS = {
    "", "sluzby/", "cenik/", "jak-pracujeme/", "blog/", "kontakt/",
    "privacy/", "terms/",
} | {s[1] for s in SERVICES}
engine.LANG_PATHS = {"sk": SK_PATHS, "cz": CZ_PATHS}

# hreflang 1:1 pairs: SK path -> CZ path
HREFLANG_PAIR = {
    "": "",
    "sluzby/": "sluzby/",
    "cennik/": "cenik/",
    "jak-pracujeme/": "jak-pracujeme/",
    "blog/": "blog/",
    "kontakt/": "kontakt/",
    "privacy/": "privacy/",
    "terms/": "terms/",
}
for s in SERVICES:
    HREFLANG_PAIR[s[0]] = s[1]
    HREFLANG_PAIR[s[1]] = s[0]
engine.HREFLANG_PAIR = HREFLANG_PAIR

# ---------------------------------------------------------------- branding
engine.BASE = BASE
engine.BRAND = BRAND
engine.LOGO = ('<span class="logo-n">S</span><span class="logo-o">E</span>'
               '<span class="logo-k">O</span> <span class="logo-t">WP</span>')

# ---------------------------------------------------------------- verify
# Paste GSC html-tag token content after creating the property, rebuild, push.
engine.GSC_TOKEN = ""
engine.BING_TOKEN = "3b43ea1af0ee49f082ab3c4e94ed5f4f"