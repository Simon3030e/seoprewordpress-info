# -*- coding: utf-8 -*-
"""
Niche site builder (seosem-servisy family).

Generates static HTML for one niche domain from build/config.py + build/pages.py.
Run from the repo root:

    python3 build_site.py

Writes: SK root + /sk/ pages, /cz/ mirror, sitemap.xml (hreflang pairs),
robots.txt (AI crawlers welcome). GSC + Bing verification files included.
"""
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO / "build"))

import config          # noqa: E402  (sets engine constants BEFORE pages import)
import engine          # noqa: E402
import pages           # noqa: E402

PAGES: list[tuple[str, str]] = []
for item in pages.build_all():
    PAGES.append(item)

LASTMOD = time.strftime("%Y-%m-%d")


def write_pages():
    for rel, html in PAGES:
        out = REPO / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"  wrote {rel}  ({len(html):,} B)")
    print(f"{len(PAGES)} pages written.")


def _mkurl(loc: str, priority: str, alts: str = "") -> str:
    return f"""  <url>
    <loc>{loc}</loc>
    {alts}<lastmod>{LASTMOD}</lastmod><priority>{priority}</priority>
  </url>"""


def _alts(sk_sub: str) -> str:
    """hreflang alternates for one logical page (SK + CZ)."""
    cz_sub = engine.HREFLANG_PAIR.get(sk_sub)
    out = []
    if sk_sub is not None:
        u = engine.BASE + ("/" if sk_sub == "" else "/sk/" + sk_sub)
        out.append(f'<xhtml:link rel="alternate" hreflang="sk" href="{u}"/>')
    if cz_sub is not None:
        u = engine.BASE + ("/cz/" + cz_sub)
        out.append(f'<xhtml:link rel="alternate" hreflang="cs" href="{u}"/>')
    if sk_sub is not None:
        u = engine.BASE + ("/" if sk_sub == "" else "/sk/" + sk_sub)
        out.append(f'<xhtml:link rel="alternate" hreflang="x-default" href="{u}"/>')
    return "".join(out)


def write_sitemap():
    rows = []
    # SK home = root
    rows.append(_mkurl(engine.BASE + "/", "1.0", _alts("")))
    for path in sorted(config.SK_PATHS):
        if path == "" or path in ("privacy/", "terms/"):
            continue
        pr = "0.9" if path in ("sluzby/", "cennik/", "sluzby/seo-optimalizacia/") else "0.7"
        rows.append(_mkurl(engine.BASE + "/sk/" + path, pr, _alts(path)))
    for path in sorted(config.CZ_PATHS):
        if path == "" or path in ("privacy/", "terms/"):
            continue
        pr = "0.9" if path in ("sluzby/", "cenik/", "sluzby/seo-optimalizace/") else "0.7"
        rows.append(_mkurl(engine.BASE + "/cz/" + path, pr, _alts(path)))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    (REPO / "sitemap.xml").write_text(xml, encoding="utf-8")
    print(f"  wrote sitemap.xml ({xml.count('<loc>'):,} urls)")


def write_robots():
    robots = f"""User-agent: *
Allow: /

# AI crawlers: welcome. We want to be cited.
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: CCBot
Allow: /

Sitemap: {engine.BASE}/sitemap.xml
"""
    (REPO / "robots.txt").write_text(robots, encoding="utf-8")
    print("  wrote robots.txt")


def write_verification_files():
    """GSC: file-based verification page. Bing: XML token file placeholder."""
    tok = engine.GSC_TOKEN
    if tok:
        (REPO / f"google{tok}.html").write_text(
            f"google-site-verification: google{tok}.html", encoding="utf-8")
        print(f"  wrote google{tok[:8]}...html (GSC file verification)")
    # Bing SiteAuth.xml: keep the existing token used on noktostudio.com
    (REPO / "BingSiteAuth.xml").write_text(
        '<?xml version="1.0"?>\n<users>\n  <user>3b43ea1af0ee49f082ab3c4e94ed5f4f</user>\n</users>\n',
        encoding="utf-8")
    print("  wrote BingSiteAuth.xml")


if __name__ == "__main__":
    print(f"Building {engine.BRAND} ({engine.BASE}) ...")
    write_pages()
    write_sitemap()
    write_robots()
    write_verification_files()
    print("Done.")