#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static site generator for bionut.az (no third-party dependencies).

    python3 tools/build.py          -> writes the full site into ./public

English lives at the site root, Azerbaijani under /az/, Russian under /ru/.
All copy is in tools/content.py.
"""
import html
import json
import math
import os
import re
import shutil
import subprocess
import zlib

import content as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public")
SITE = "https://bionut.az"
VERSION = "20261119"

e = html.escape


# ============================================================ routing
def page_path(key):
    if key == "home":
        return ""
    if key.startswith("product:"):
        return "products/%s/" % key.split(":", 1)[1]
    if key.startswith("article:"):
        return "insights/%s/" % key.split(":", 1)[1]
    return {"about": "about/", "products": "products/", "process": "process-quality/",
            "certifications": "certifications/", "contact": "contact/", "insights": "insights/"}[key]


def lang_prefix(lang):
    return "" if lang == C.DEFAULT_LANG else lang + "/"


class Ctx:
    def __init__(self, lang, key):
        self.lang = lang
        self.key = key
        self.full = lang_prefix(lang) + page_path(key)
        self.depth = self.full.count("/")
        self.rel = "../" * self.depth

    def url(self, key, lang=None, query=""):
        target = self.rel + lang_prefix(lang or self.lang) + page_path(key)
        return (target or "./") + query

    def asset(self, p):
        return self.rel + "assets/" + p

    def abs(self, key=None, lang=None):
        return SITE + "/" + lang_prefix(lang or self.lang) + page_path(key or self.key)

    def t(self, d):
        return d[self.lang] if isinstance(d, dict) else d


# ============================================================ images
_dims = {}


def dims(name):
    if name not in _dims:
        out = subprocess.check_output(["identify", "-format", "%w %h", os.path.join(ROOT, "assets", "img", name + ".webp")])
        w, h = out.decode().split()[:2]
        _dims[name] = (int(w), int(h))
    return _dims[name]


def pic(c, name, alt, cls="", loading="lazy", sizes="100vw", priority=False):
    w, h = dims(name)
    a = c.asset("img/" + name)
    attrs = 'src="%s.webp" alt="%s" width="%d" height="%d" decoding="async"' % (a, e(alt), w, h)
    if priority:
        attrs += ' fetchpriority="high"'
    else:
        attrs += ' loading="%s"' % loading
    if cls:
        attrs += ' class="%s"' % cls
    return '<picture><source type="image/avif" srcset="%s.avif"><img %s sizes="%s"></picture>' % (a, attrs, sizes)


# ============================================================ icons
ICON = {
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M7.5 12.5l3 3 6-6.5"/></svg>',
    "download": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 3v12M7 10l5 5 5-5M4 20h16"/></svg>',
    "lab": '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><path d="M15 4h10M17 4v11L7.5 31.5A3 3 0 0 0 10 36h20a3 3 0 0 0 2.5-4.5L23 15V4"/><path d="M11 26h18"/><circle cx="17" cy="31" r="1.2"/><circle cx="23" cy="29" r="1"/></svg>',
    "metal": '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><rect x="5" y="10" width="30" height="20" rx="1"/><path d="M5 20h30"/><path d="M12 6v4M20 6v4M28 6v4M12 30v4M20 30v4M28 30v4"/><path d="M15 15l2.5 2.5L22 13"/></svg>',
    "raw": '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><circle cx="17" cy="17" r="11"/><path d="M25 25l10 10"/><path d="M17 10c-3.5 2-5 5-4 9 3 .5 6-1 7.5-4 .8-1.8.6-3.6-.5-5z"/></svg>',
    "monitor": '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><path d="M6 28a14 14 0 1 1 28 0"/><path d="M20 28l7-9"/><circle cx="20" cy="28" r="2"/><path d="M10 28h-4M34 28h-4M20 14v-4M10.5 18.5l-2.8-2.8M29.5 18.5l2.8-2.8"/></svg>',
    "finished": '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><path d="M20 4l4 3.5 5-.5 1.5 5 4.5 2.5-1.5 5 1.5 5-4.5 2.5-1.5 5-5-.5L20 36l-4-3.5-5 .5-1.5-5L5 25.5l1.5-5-1.5-5L9.5 13l1.5-5 5 .5z"/><path d="M14 20.5l4 4 8-8.5"/></svg>',
    "trace": '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><circle cx="8" cy="8" r="3"/><circle cx="32" cy="20" r="3"/><circle cx="8" cy="32" r="3"/><path d="M11 8h9a6 6 0 0 1 6 6v0a6 6 0 0 0 3 4.5M29 21.5a6 6 0 0 0-3 4.5v0a6 6 0 0 1-6 6h-9"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M5 3h3.5l2 5-2.5 1.5a11 11 0 0 0 6.5 6.5L16 13.5l5 2V19a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 6l9 7 9-7"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
}


def tel(n):
    return "tel:" + re.sub(r"[^\d+]", "", n)


# ============================================================ layout
def head(c, title, desc, og_img="og-image.jpg", extra=""):
    alts = "".join('<link rel="alternate" hreflang="%s" href="%s">' % (C.LANG_HTML[l], c.abs(lang=l)) for l in C.LANGS)
    alts += '<link rel="alternate" hreflang="x-default" href="%s">' % c.abs(lang=C.DEFAULT_LANG)
    og_locale = {"en": "en_US", "az": "az_AZ", "ru": "ru_RU"}[c.lang]
    return f"""<!doctype html>
<html lang="{C.LANG_HTML[c.lang]}">
<head>
<meta charset="utf-8">
<script>document.documentElement.classList.add("js")</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{c.abs()}">
{alts}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Bionut">
<meta property="og:locale" content="{og_locale}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{c.abs()}">
<meta property="og:image" content="{SITE}/assets/img/{og_img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#2C1810">
<link rel="icon" type="image/png" href="{c.asset('brand/bionut-logo.png')}">
<link rel="apple-touch-icon" href="{c.asset('brand/bionut-logo.png')}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Manrope:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="{c.asset('css/main.css')}?v={VERSION}">
{extra}
</head>
<body>
<a class="skip" href="#main">{e(c.t(C.UI['skip']))}</a>
"""


def lang_switch(c):
    parts = []
    for l in C.LANGS:
        cur = ' aria-current="true"' if l == c.lang else ""
        parts.append('<a href="%s" hreflang="%s" lang="%s"%s>%s</a>' % (c.url(c.key, lang=l), l, l, cur, C.LANG_LABEL[l]))
    return '<div class="lang" role="navigation" aria-label="%s">%s</div>' % (e(c.t(C.UI["lang_label"])), "<span>/</span>".join(parts))


def section_of(key):
    if key.startswith("product:"):
        return "products"
    if key.startswith("article:"):
        return "insights"
    return key


def header(c):
    cur = section_of(c.key)
    items = "".join('<li><a href="%s"%s>%s</a></li>' % (c.url(k), ' aria-current="page"' if k == cur else "", e(c.t(lbl))) for k, lbl in C.NAV)
    return f"""<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{c.url('home')}" aria-label="Bionut, {e(c.t(C.NAV[0][1]))}">
      <img src="{c.asset('brand/bionut-logo.png')}" alt="BIONUT logo" width="106" height="102">
      <span class="brand-text"><strong>BIONUT</strong><span>{e(c.t(C.UI["tagline"]))}</span></span>
    </a>
    <nav class="main-nav" aria-label="Main"><ul>{items}</ul></nav>
    <div class="header-actions">
      {lang_switch(c)}
      <a class="btn btn-primary btn-sm" href="{c.url('contact')}">{e(c.t(C.UI['contact_btn']))}</a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-panel" aria-label="{e(c.t(C.UI['menu']))}"><span></span></button>
    </div>
  </div>
</header>
<div class="mobile-panel" id="mobile-panel">
  <ul>{items.replace('</a>', ' ' + ICON['arrow'].replace('<svg', '<svg width="20" height="20"') + '</a>')}</ul>
  {lang_switch(c)}
  <a class="btn btn-primary" href="{c.url('contact')}">{e(c.t(C.UI['contact_btn']))}</a>
</div>
"""


def footer(c):
    comp = "".join('<li><a href="%s">%s</a></li>' % (c.url(k), e(c.t(l))) for k, l in C.NAV[1:]) + \
        '<li><a href="%s">%s</a></li>' % (c.url("insights"), e(c.t(C.UI["insights"])))
    prods = "".join('<li><a href="%s">%s</a></li>' % (c.url("product:" + p["slug"]), e(c.t(p["name"]))) for p in C.PRODUCTS)
    phones = "".join('<a href="%s">%s</a>' % (tel(p), p) for p in C.COMPANY["phones"])
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <img src="{c.asset('brand/bionut-logo.png')}" alt="BIONUT logo" width="106" height="102" loading="lazy">
        <p>{e(c.t(C.UI['footer_tag']))}</p>
        <p class="legal">{e(c.t(C.COMPANY['legal']))}</p>
      </div>
      <div><h3>{e(c.t(C.UI['footer_company']))}</h3><ul>{comp}</ul></div>
      <div><h3>{e(c.t(C.UI['footer_products']))}</h3><ul>{prods}</ul></div>
      <div><h3>{e(c.t(C.UI['footer_contact']))}</h3>
        <ul class="footer-contact">
          <li><span class="k">{e(c.t(C.UI['address']))}</span><span>{e(c.t(C.COMPANY['address']))}</span></li>
          <li><span class="k">{e(c.t(C.UI['phone']))}</span>{phones}</li>
          <li><span class="k">{e(c.t(C.UI['email']))}</span><a href="mailto:{C.COMPANY['emails'][0]}">{C.COMPANY['emails'][0]}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>{e(C.COMPANY['copyright'])}</span>
      {lang_switch(c)}
    </div>
  </div>
</footer>
<script src="{c.asset('js/main.js')}?v={VERSION}" defer></script>
</body>
</html>
"""


def breadcrumb(c, trail):
    items = ['<li><a href="%s">%s</a></li>' % (c.url("home"), e(c.t(C.UI["breadcrumb_home"])))]
    for k, label in trail[:-1]:
        items.append('<li><a href="%s">%s</a></li>' % (c.url(k), e(label)))
    items.append('<li aria-current="page">%s</li>' % e(trail[-1][1]))
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": c.t(C.UI["breadcrumb_home"]), "item": c.abs("home")}] + [
        {"@type": "ListItem", "position": i + 2, "name": lbl, "item": c.abs(k)} for i, (k, lbl) in enumerate(trail)]}
    return '<nav aria-label="Breadcrumb"><ol class="breadcrumb">%s</ol></nav><script type="application/ld+json">%s</script>' % (
        "".join(items), json.dumps(ld, ensure_ascii=False))


def page_hero(c, eyebrow, h1, lead, trail, aside=""):
    return f"""<section class="page-hero">
  <div class="wrap">
    {breadcrumb(c, trail)}
    <div class="page-hero-grid">
      <div><span class="eyebrow">{e(eyebrow)}</span><h1>{e(h1)}</h1></div>
      <div><p class="lead">{e(lead)}</p>{aside}</div>
    </div>
  </div>
</section>"""


# ============================================================ shared blocks
def size_label(c, p):
    return c.t(C.UI["sizes"] if p["size_kind"] == "sizes" else C.UI["calibers"])


def product_card(c, p, i):
    ur = c.t(C.UI["upon_request"])
    sizes = ", ".join(p["sizes"]) if p["sizes"] else ur
    moist = p["moisture"] or ur
    return f"""<article class="product-card reveal reveal-d{i % 3}">
  <a class="pc-media" href="{c.url('product:' + p['slug'])}" tabindex="-1" aria-hidden="true">{pic(c, p['img'], c.t(p['name']), sizes='(max-width: 620px) 100vw, (max-width: 1000px) 50vw, 420px')}<span class="pc-index">{i + 1:02d}</span></a>
  <div class="pc-body">
    <h3><a href="{c.url('product:' + p['slug'])}">{e(c.t(p['name']))}</a></h3>
    <p>{e(c.t(p['short']))}</p>
    <dl class="pc-specs">
      <div><dt>{e(c.t(C.UI['moisture']))}</dt><dd>{e(moist)}</dd></div>
      <div><dt>{e(size_label(c, p))}</dt><dd>{e(sizes)}</dd></div>
    </dl>
    <a class="link-arrow" href="{c.url('product:' + p['slug'])}">{e(c.t(C.UI['view_product']))} {ICON['arrow']}</a>
  </div>
</article>"""


def steps_block(c):
    out = []
    for i, s in enumerate(C.STEPS):
        out.append(f"""<div class="step reveal reveal-d{i % 4}">
  <div class="step-media">{pic(c, s['img'], c.t(s['t']), sizes='(max-width: 560px) 100vw, (max-width: 1000px) 50vw, 320px')}</div>
  <div class="step-num">0{i + 1}</div>
  <h3>{e(c.t(s['t']))}</h3>
  <div class="step-sub">{e(c.t(s['s']))}</div>
  <p>{e(c.t(s['p']))}</p>
</div>""")
    return '<div class="steps">%s</div>' % "".join(out)


def quality_block(c, light=False):
    items = "".join('<div class="q-item reveal">%s<h3>%s</h3><p>%s</p></div>' % (ICON[k], e(c.t(t)), e(c.t(d))) for k, t, d in C.QUALITY)
    return '<div class="quality-grid%s">%s</div>' % (" light-quality" if light else "", items)


def cert_cards(c):
    return '<div class="cert-row">%s</div>' % "".join(
        '<div class="cert-card reveal reveal-d%d"><div class="seal" aria-hidden="true">%s</div><h3>%s</h3><p>%s</p></div>' % (
            i % 4, e(ct["mark"]), e(c.t(ct["name"])), e(c.t(ct["desc"]))) for i, ct in enumerate(C.CERTS))


_map = None


def world_map(c):
    global _map
    if _map is None:
        _map = json.load(open(os.path.join(ROOT, "tools", "data", "map.json")))
    m = _map
    market_ids = {mid: code for code, mid, _ in C.MARKETS}
    names = {code: c.t(n) for code, _, n in C.MARKETS}
    paths = []
    for cid, cd in m["countries"].items():
        if not cd["d"]:
            continue
        if cid in market_ids:
            code = market_ids[cid]
            paths.append('<path class="land market" data-code="%s" d="%s"><title>%s</title></path>' % (code, cd["d"], e(names[code])))
        elif cid == "031":
            paths.append('<path class="land origin" d="%s"><title>%s</title></path>' % (cd["d"], e(c.t(C.UI["azerbaijan"]))))
        else:
            paths.append('<path class="land" d="%s"/>' % cd["d"])
    ox, oy = m["points"]["AZ"]
    routes, pins = [], []
    for code, _, _ in C.MARKETS:
        x, y = m["points"][code]
        mx, my = (ox + x) / 2, (oy + y) / 2
        dist = math.hypot(x - ox, y - oy)
        lift = min(dist * 0.32, 90)
        cx, cy = mx, my - lift
        routes.append('<path class="route" data-code="%s" d="M%.1f,%.1fQ%.1f,%.1f %.1f,%.1f"/>' % (code, ox, oy, cx, cy, x, y))
        pins.append('<circle class="pin" data-code="%s" data-name="%s" cx="%.1f" cy="%.1f" r="4.2"/>' % (code, e(names[code]), x, y))
    origin = ('<circle class="origin-ring" cx="%.1f" cy="%.1f" r="7"/><circle class="origin-pin" cx="%.1f" cy="%.1f" r="5.5"><title>%s</title></circle>' % (ox, oy, ox, oy, e(c.t(C.UI["tagline"]).replace(" · ", ", "))))
    return ('<div class="map-wrap"><svg class="world-map" viewBox="170 12 690 250" role="img" aria-label="%s">%s<g>%s</g><g>%s</g>%s</svg><div class="map-tip" aria-hidden="true"></div></div>' % (
        e(c.t(C.HOME["markets_h"])), "".join(paths), "".join(routes), "".join(pins), origin))


def markets_block(c):
    lis = "".join('<li><button type="button" data-code="%s"><span>%s</span><span>%s</span></button></li>' % (code, e(c.t(n)), code) for code, _, n in C.MARKETS)
    return f"""<section class="section section-cream" id="markets">
  <div class="wrap markets">
    <div class="reveal">
      <span class="eyebrow">{e(c.t(C.HOME['markets_eyebrow']))}</span>
      <h2>{e(c.t(C.HOME['markets_h']))}</h2>
      <p class="lead" style="margin-top:20px">{e(c.t(C.HOME['markets_p']))}</p>
      <ul class="market-list">{lis}</ul>
      <div class="origin-note"><i></i>{e(c.t(C.HOME['markets_origin']))}</div>
    </div>
    <div class="reveal reveal-d1">{world_map(c)}</div>
  </div>
</section>"""


def insight_card(c, a):
    return f"""<article class="insight-card reveal">
  <a class="ic-media" href="{c.url('article:' + a['slug'])}" tabindex="-1" aria-hidden="true">{pic(c, a['img'], c.t(a['title']), sizes='(max-width: 800px) 100vw, 620px')}</a>
  <div class="ic-body">
    <div class="ic-meta"><span class="tag">{e(c.t(a['tag']))}</span><span>{e(c.t(a['date_label']))}</span><span>{a['read']} {e(c.t(C.UI['min_read']))}</span></div>
    <h3><a href="{c.url('article:' + a['slug'])}">{e(c.t(a['title']))}</a></h3>
    <p>{e(c.t(a['excerpt']))}</p>
    <a class="link-arrow" href="{c.url('article:' + a['slug'])}">{e(c.t(C.UI['read_more']))} {ICON['arrow']}</a>
  </div>
</article>"""


def cta_block(c, img="forklift-pallet"):
    phones = "".join('<a href="%s">%s</a>' % (tel(p), p) for p in C.COMPANY["phones"])
    return f"""<section class="cta">
  <div class="cta-media">{pic(c, img, 'Bionut warehouse', sizes='(max-width: 860px) 100vw, 50vw')}</div>
  <div class="cta-body on-dark">
    <span class="eyebrow light">{e(c.t(C.UI['contact_btn']))}</span>
    <h2>{e(c.t(C.HOME['cta_h']))}</h2>
    <p>{e(c.t(C.HOME['cta_p']))}</p>
    <div class="cta-actions">
      <a class="btn btn-gold" href="{c.url('contact')}">{e(c.t(C.UI['request_quote']))} {ICON['arrow']}</a>
      <a class="btn btn-ghost-light" href="{c.url('products')}">{e(c.t(C.UI['all_products']))}</a>
    </div>
    <div class="cta-contacts">{phones}<a href="mailto:{C.COMPANY['emails'][0]}">{C.COMPANY['emails'][0]}</a></div>
  </div>
</section>"""


# ============================================================ pages
def org_ld(c):
    return {
        "@context": "https://schema.org", "@type": "Organization", "name": "Bionut",
        "legalName": C.COMPANY["legal"]["az"], "url": SITE, "logo": SITE + "/assets/brand/bionut-logo.png",
        "foundingDate": "2005", "email": C.COMPANY["emails"][0], "telephone": C.COMPANY["phones"][0],
        "address": {"@type": "PostalAddress", "streetAddress": "Ə.Əliyev 4, Zarağan", "addressLocality": "Qəbələ",
                    "postalCode": "AZ3630", "addressCountry": "AZ"},
    }


def page_home(c):
    H = C.HOME
    stats = "".join(
        '<div class="stat reveal reveal-d%d"><div class="stat-num"><span data-count="%s">%s</span><sup>%s</sup></div><div class="stat-label">%s</div></div>' % (
            i, n, n, s, e(c.t(lbl))) for i, (n, s, lbl) in enumerate(H["stats"]))
    points = "".join("<li>%s<span>%s</span></li>" % (ICON["check"], e(c.t(p))) for p in H["intro_points"])
    cards = "".join(product_card(c, p, i) for i, p in enumerate(C.PRODUCTS))
    insights = "".join(insight_card(c, a) for a in C.ARTICLES)
    ld = '<script type="application/ld+json">%s</script>' % json.dumps(org_ld(c), ensure_ascii=False)
    hero_img = c.asset("img/hero-orchard")
    slides = "".join('<div class="hero-slide%s" data-cap="%s">%s</div>' % (
        " is-active" if i == 0 else "", e(c.t(cap)), pic(c, img, c.t(cap), sizes="100vw", priority=(i == 0), loading="eager" if i < 2 else "lazy"))
        for i, (img, lbl, cap) in enumerate(H["slides"]))
    dots = "".join('<button type="button" role="tab" class="hero-dot%s" aria-selected="%s" aria-label="%s"><span class="n">%02d</span><span class="l">%s</span><span class="bar"><i></i></span></button>' % (
        " is-active" if i == 0 else "", "true" if i == 0 else "false", e(c.t(lbl)), i + 1, e(c.t(lbl)))
        for i, (img, lbl, cap) in enumerate(H["slides"]))
    words = " ".join('<span class="w"><span style="--d:%d">%s</span></span>' % (i + 1, e(w)) for i, w in enumerate(c.t(H["h1"]).split()))
    marquee = "".join('<span>%s</span><i aria-hidden="true"></i>' % e(c.t(m)) for m in H["marquee"])
    preload = '<link rel="preload" as="image" type="image/avif" href="%s.avif" fetchpriority="high">' % hero_img
    return head(c, c.t(H["title"]), c.t(H["meta"]), extra=ld + preload).replace("<body>", '<body class="has-hero">') + header(c) + f"""<main id="main">
<section class="hero-full" aria-roledescription="carousel">
  <div class="hero-slides">{slides}</div>
  <div class="hero-scrim" aria-hidden="true"></div>
  <div class="wrap hero-inner">
    <div class="hero-content">
      <span class="eyebrow light hero-anim" style="--d:0">{e(c.t(H['eyebrow']))}</span>
      <h1>{words}</h1>
      <p class="lead hero-anim" style="--d:6">{e(c.t(H['lead']))}</p>
      <div class="hero-actions hero-anim" style="--d:8">
        <a class="btn btn-gold" href="{c.url('products')}">{e(c.t(H['cta1']))} {ICON['arrow']}</a>
        <a class="btn btn-ghost-light" href="{c.url('contact')}">{e(c.t(H['cta2']))}</a>
      </div>
    </div>
    <div class="hero-bottom hero-anim" style="--d:10">
      <div class="hero-dots" role="tablist">{dots}</div>
      <p class="hero-cap" aria-live="polite">{e(c.t(H['slides'][0][2]))}</p>
      <a class="hero-scroll" href="#intro"><span>{e(c.t(H['scroll']))}</span><i></i></a>
    </div>
  </div>
</section>
<section class="stats" aria-label="Bionut in numbers"><div class="wrap stats-grid">{stats}</div></section>
<div class="marquee" aria-hidden="true"><div class="marquee-track"><div class="marquee-group">{marquee}</div><div class="marquee-group">{marquee}</div></div></div>

<section class="section" id="intro">
  <div class="wrap split">
    <div class="split-media reveal">
      <div class="m1">{pic(c, 'orchard-rows', 'Bionut hazelnut orchard in Gabala', sizes='(max-width: 900px) 92vw, 600px')}</div>
      <div class="m2">{pic(c, 'catkins', 'Hazelnut catkins in early spring', sizes='280px')}</div>
    </div>
    <div class="reveal reveal-d1">
      <span class="eyebrow">{e(c.t(H['intro_eyebrow']))}</span>
      <h2>{e(c.t(H['intro_h']))}</h2>
      <p class="lead" style="margin-top:24px">{e(c.t(H['intro_p']))}</p>
      <ul class="check-list">{points}</ul>
      <a class="link-arrow" href="{c.url('about')}">{e(c.t(H['intro_link']))} {ICON['arrow']}</a>
    </div>
  </div>
</section>

<section class="section section-cream product-section" id="products">
  <div class="wrap">
    <div class="section-head reveal">
      <div><span class="eyebrow">{e(c.t(H['products_eyebrow']))}</span><h2>{e(c.t(H['products_h']))}</h2></div>
      <p>{e(c.t(H['products_p']))}</p>
    </div>
    <div class="product-grid">{cards}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <div><span class="eyebrow">{e(c.t(H['process_eyebrow']))}</span><h2>{e(c.t(H['process_h']))}</h2></div>
      <div class="head-actions"><a class="link-arrow" href="{c.url('process')}">{e(c.t(H['process_link']))} {ICON['arrow']}</a></div>
    </div>
    {steps_block(c)}
  </div>
</section>

<section class="section section-green on-dark">
  <div class="wrap">
    <div class="section-head reveal">
      <div><span class="eyebrow light">{e(c.t(C.PROCESS_PAGE['quality_eyebrow']))}</span><h2>{e(c.t(H['quality_h']))}</h2></div>
      <p>{e(c.t(C.PROCESS_PAGE['quality_p']))}</p>
    </div>
    {quality_block(c)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <div><span class="eyebrow">{e(c.t(H['cert_eyebrow']))}</span><h2>{e(c.t(H['cert_h']))}</h2></div>
      <div class="head-actions"><a class="link-arrow" href="{c.url('certifications')}">{e(c.t(H['cert_link']))} {ICON['arrow']}</a></div>
    </div>
    {cert_cards(c)}
  </div>
</section>

{markets_block(c)}

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <div><span class="eyebrow">{e(c.t(H['insights_eyebrow']))}</span><h2>{e(c.t(H['insights_h']))}</h2></div>
      <div class="head-actions"><a class="link-arrow" href="{c.url('insights')}">{e(c.t(C.UI['back_insights']))} {ICON['arrow']}</a></div>
    </div>
    <div class="insight-grid">{insights}</div>
  </div>
</section>

{cta_block(c)}
</main>
""" + footer(c)


def page_products(c):
    P = C.PRODUCTS_PAGE
    cards = "".join(product_card(c, p, i) for i, p in enumerate(C.PRODUCTS))
    return head(c, c.t(P["title"]) + " | Bionut", c.t(P["meta"])) + header(c) + f"""<main id="main">
{page_hero(c, c.t(P['eyebrow']), c.t(P['h1']), c.t(P['lead']), [('products', c.t(P['title']))])}
<section class="section section-cream"><div class="wrap"><div class="product-grid">{cards}</div></div></section>
<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <span class="eyebrow">{e(c.t(C.UI['spec_table']))}</span>
      <h2>{e(c.t(P['custom_h']))}</h2>
      <p class="lead" style="margin:24px 0 36px">{e(c.t(P['custom_p']))}</p>
      <div class="moq" style="margin-bottom:36px"><strong>{e(c.t(C.UI['moq_title']))}</strong>{e(c.t(C.UI['moq']))}</div>
      <a class="btn btn-primary" href="{c.url('contact')}">{e(c.t(C.UI['request_quote']))} {ICON['arrow']}</a>
    </div>
    <div class="split-media reveal reveal-d1">
      <div class="m1">{pic(c, 'big-bags', 'Bionut big bags in warehouse', sizes='(max-width: 900px) 92vw, 600px')}</div>
      <div class="m2">{pic(c, 'g-natural-carton2', 'Vacuum-packed hazelnut kernels', sizes='280px')}</div>
    </div>
  </div>
</section>
</main>
""" + footer(c)


def page_product(c, p):
    U = C.UI
    ur = c.t(U["upon_request"])
    name = c.t(p["name"])
    imgs = [p["img"]] + p["gallery"]
    thumbs = "".join('<button type="button" aria-pressed="%s" data-alt="%s" aria-label="%s %d">%s</button>' % (
        "true" if i == 0 else "false", e(name), e(name), i + 1, pic(c, im, "", sizes="120px")) for i, im in enumerate(imgs))
    rows = [
        (c.t(U["moisture"]), p["moisture"] or ur),
        (size_label(c, p), ", ".join(p["sizes"]) if p["sizes"] else ur),
        (c.t(U["packaging"]), c.t(p["packaging"]) if p["packaging"] else ur),
        (c.t(U["origin"]), c.t(U["origin_val"])),
    ]
    table = "".join("<tr><th scope=\"row\">%s</th><td>%s</td></tr>" % (e(k), e(v)) for k, v in rows)
    apps = "".join("<li>%s</li>" % e(c.t(a)) for a in p["apps"])
    idx = C.PRODUCTS.index(p)
    related = [C.PRODUCTS[(idx + k) % len(C.PRODUCTS)] for k in (1, 2, 3)]
    rel_cards = "".join(product_card(c, r, C.PRODUCTS.index(r)) for r in related)
    ld = {"@context": "https://schema.org", "@type": "Product", "name": name, "description": c.t(p["short"]),
          "image": SITE + "/assets/img/%s.webp" % p["img"], "brand": {"@type": "Brand", "name": "Bionut"},
          "countryOfOrigin": "AZ", "manufacturer": {"@type": "Organization", "name": "Bionut"}}
    spec_href = c.asset("specs/bionut-%s-specification.pdf" % p["slug"])
    return head(c, name + " | Bionut", c.t(p["short"]) + " " + c.t(U["moq"])[:80], og_img="og-image.jpg",
                extra='<script type="application/ld+json">%s</script>' % json.dumps(ld, ensure_ascii=False)) + header(c) + f"""<main id="main">
<section class="page-hero" style="padding-bottom:0;border:0">
  <div class="wrap">{breadcrumb(c, [('products', c.t(C.PRODUCTS_PAGE['title'])), (c.key, name)])}</div>
</section>
<section class="section section-cream" style="padding-top:clamp(24px,4vw,48px)">
  <div class="wrap pd">
    <div class="pd-gallery">
      <div class="pd-main">{pic(c, p['img'], name, sizes='(max-width: 900px) 100vw, 620px', priority=True)}</div>
      <div class="pd-thumbs">{thumbs}</div>
    </div>
    <div class="pd-info">
      <span class="eyebrow">{e(c.t(C.PRODUCTS_PAGE['eyebrow']))} · {idx + 1:02d}</span>
      <h1>{e(name)}</h1>
      <p class="lead">{e(c.t(p['long']))}</p>
      <table class="spec-table"><caption>{e(c.t(U['spec_table']))}</caption>{table}</table>
      <div class="pd-block"><h2>{e(c.t(U['applications']))}</h2><ul class="chips">{apps}</ul></div>
      <div class="pd-actions">
        <a class="btn btn-primary" href="{c.url('contact', query='?product=' + p['slug'])}">{e(c.t(U['request_quote']))} {ICON['arrow']}</a>
        <a class="btn btn-outline" href="{spec_href}" download>{ICON['download']} {e(c.t(U['download_spec']))}</a>
      </div>
      <div class="moq"><strong>{e(c.t(U['moq_title']))}</strong>{e(c.t(U['moq']))}</div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow">{e(c.t(C.PRODUCTS_PAGE['eyebrow']))}</span><h2>{e(c.t(U['related']))}</h2></div>
      <div class="head-actions"><a class="link-arrow" href="{c.url('products')}">{e(c.t(U['all_products']))} {ICON['arrow']}</a></div></div>
    <div class="product-grid">{rel_cards}</div>
  </div>
</section>
{cta_block(c, 'warehouse-pallets')}
</main>
""" + footer(c)


def page_process(c):
    P = C.PROCESS_PAGE
    return head(c, c.t(P["title"]) + " | Bionut", c.t(P["meta"])) + header(c) + f"""<main id="main">
{page_hero(c, c.t(P['eyebrow']), c.t(P['h1']), c.t(P['lead']), [('process', c.t(P['title']))])}
<div class="banner-img">{pic(c, 'hero-orchard', 'Bionut orchards in Gabala', sizes='100vw')}</div>
<section class="section">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow">01 / 04</span><h2>{e(c.t(P['stages_h']))}</h2></div><p>{e(c.t(C.HOME['process_h']))}</p></div>
    {steps_block(c)}
  </div>
</section>
<section class="section section-green on-dark">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow light">{e(c.t(P['quality_eyebrow']))}</span><h2>{e(c.t(P['quality_h']))}</h2></div><p>{e(c.t(P['quality_p']))}</p></div>
    {quality_block(c)}
  </div>
</section>
<section class="section">
  <div class="wrap gallery-strip">
    <figure class="reveal">{pic(c, 'warehouse-pallets', 'Palletised export shipments', sizes='(max-width: 760px) 100vw, 50vw')}</figure>
    <figure class="reveal reveal-d1">{pic(c, 'forklift-loading', 'Loading export pallets', sizes='(max-width: 760px) 50vw, 25vw')}</figure>
    <figure class="reveal reveal-d2">{pic(c, 'big-bags', '1000 kg big bags', sizes='(max-width: 760px) 50vw, 25vw')}</figure>
  </div>
</section>
{cta_block(c, 'warehouse-hall')}
</main>
""" + footer(c)


def page_certs(c):
    P = C.CERT_PAGE
    out = []
    for ct in C.CERTS:
        req = c.t(P["on_request"])
        meta = "".join('<div><dt>%s</dt><dd>%s</dd></div>' % (e(c.t(P[k])), e(ct[k] or req)) for k in ("number", "issuer", "valid"))
        if ct["pdf"]:
            act = '<a class="btn btn-primary" href="%s" download>%s %s</a>' % (c.asset("certificates/" + ct["pdf"]), ICON["download"], e(c.t(P["download"])))
        else:
            act = '<a class="btn btn-primary" href="%s">%s %s</a>' % (c.url("contact", query="?cert=" + ct["code"].replace(" ", "%20")), e(c.t(P["request"])), ICON["arrow"])
        out.append(f"""<article class="cert-detail reveal" id="{re.sub('[^a-z0-9]+', '-', ct['code'].lower())}">
  <div class="seal" aria-hidden="true">{e(ct['mark'])}</div>
  <div><h2>{e(c.t(ct['name']))}</h2><p>{e(c.t(ct['desc']))}</p><dl class="cert-meta">{meta}</dl><div class="cert-actions">{act}</div></div>
</article>""")
    return head(c, c.t(P["title"]) + " | Bionut", c.t(P["meta"])) + header(c) + f"""<main id="main">
{page_hero(c, c.t(P['eyebrow']), c.t(P['h1']), c.t(P['lead']), [('certifications', c.t(P['title']))])}
<section class="section"><div class="wrap">{''.join(out)}</div></section>
<section class="section section-cream">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow">{e(c.t(C.PROCESS_PAGE['quality_eyebrow']))}</span><h2>{e(c.t(C.PROCESS_PAGE['quality_h']))}</h2></div></div>
    {quality_block(c, light=True)}
  </div>
</section>
{cta_block(c)}
</main>
""" + footer(c)


def page_about(c):
    A = C.ABOUT
    facts = "".join('<div class="fact reveal reveal-d%d"><strong>%s</strong><span>%s</span></div>' % (i, f, e(c.t(t))) for i, (f, t) in enumerate(A["facts"]))
    story = "".join("<p>%s</p>" % e(c.t(p)) for p in A["story"])
    values = "".join('<div class="value reveal reveal-d%d"><h3>%s</h3><p>%s</p></div>' % (i, e(c.t(t)), e(c.t(d))) for i, (t, d) in enumerate(A["values"]))
    team = "".join(f"""<div class="member reveal"><div class="avatar" aria-hidden="true">{m['initials']}</div><div>
  <h3>{e(c.t(m['name']))}</h3><div class="role">{e(c.t(m['role']))}</div><a href="mailto:{m['email']}">{m['email']}</a></div></div>""" for m in A["team"])
    return head(c, c.t(A["title"]) + " | Bionut", c.t(A["meta"])) + header(c) + f"""<main id="main">
{page_hero(c, c.t(A['eyebrow']), c.t(A['h1']), c.t(A['lead']), [('about', c.t(A['title']))])}
<div class="banner-img">{pic(c, 'orchard-rows', 'Hazelnut orchard rows in Gabala', sizes='100vw', priority=True)}</div>
<section class="section">
  <div class="wrap">
    <div class="facts" style="margin-bottom:clamp(56px,8vw,96px)">{facts}</div>
    <div class="section-head reveal" style="margin-bottom:40px"><div><span class="eyebrow">2005 / 2026</span><h2>{e(c.t(A['story_h']))}</h2></div></div>
    <div class="story reveal">{story}</div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap gallery-strip">
    <figure class="reveal">{pic(c, 'orchard-young', 'Young hazelnut orchard', sizes='(max-width: 760px) 100vw, 50vw')}</figure>
    <figure class="reveal reveal-d1">{pic(c, 'orchard-tree', 'Hazelnut tree in Gabala', sizes='(max-width: 760px) 50vw, 25vw')}</figure>
    <figure class="reveal reveal-d2">{pic(c, 'hazel-branch', 'Hazelnuts ripening on the branch', sizes='(max-width: 760px) 50vw, 25vw')}</figure>
  </div>
</section>
<section class="section section-choc on-dark">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow light">Bionut</span><h2>{e(c.t(A['values_h']))}</h2></div></div>
    <div class="values">{values}</div>
  </div>
</section>
<section class="section section-cream">
  <div class="wrap">
    <div class="section-head reveal"><div><span class="eyebrow">{e(c.t(A['team_eyebrow']))}</span><h2>{e(c.t(A['team_h']))}</h2></div><p>{e(c.t(C.COMPANY['legal']))}</p></div>
    <div class="team">{team}</div>
  </div>
</section>
{markets_block(c)}
{cta_block(c)}
</main>
""" + footer(c)


def page_contact(c):
    K = C.CONTACT
    opts = '<option value="">%s</option>' % e(c.t(K["f_any"])) + "".join(
        '<option value="%s">%s</option>' % (p["slug"], e(c.t(p["name"]))) for p in C.PRODUCTS)

    def field(fid, label, typ="text", req=False, full=False, extra=""):
        r = ' <span class="req">*</span>' if req else ""
        return '<div class="field%s"><label for="f-%s">%s%s</label><input id="f-%s" name="%s" type="%s" data-label="%s"%s%s></div>' % (
            " full" if full else "", fid, e(label), r, fid, fid, typ, e(label), " required" if req else "", extra)

    phones = "".join('<a href="%s">%s</a>' % (tel(p), p) for p in C.COMPANY["phones"])
    emails = "".join('<a href="mailto:%s">%s</a>' % (m, m) for m in C.COMPANY["emails"])
    cert_text = {"en": "Please send us a copy of your %s certificate.", "az": "Zəhmət olmasa, %s sertifikatınızın nüsxəsini göndərin.",
                 "ru": "Пожалуйста, пришлите копию вашего сертификата %s."}[c.lang]
    map_src = "https://www.google.com/maps?q=%s&output=embed" % C.COMPANY["map_query"].replace(" ", "+")
    return head(c, c.t(K["title"]) + " | Bionut", c.t(K["meta"])) + header(c) + f"""<main id="main">
{page_hero(c, c.t(K['eyebrow']), c.t(K['h1']), c.t(K['lead']), [('contact', c.t(K['title']))])}
<section class="section section-cream">
  <div class="wrap contact-grid">
    <form class="form" id="enquiry" novalidate data-to="{C.COMPANY['emails'][0]}" data-subject="{e(c.t(K['f_subject']))}" data-required="{e(c.t(K['f_required']))}" data-cert-text="{e(cert_text)}">
      <h2>{e(c.t(K['form_h']))}</h2>
      <div class="form-grid">
        {field('name', c.t(K['f_name']), req=True, extra=' autocomplete="name"')}
        {field('company', c.t(K['f_company']), req=True, extra=' autocomplete="organization"')}
        {field('email', c.t(K['f_email']), 'email', req=True, extra=' autocomplete="email"')}
        {field('phone', c.t(K['f_phone']), 'tel', extra=' autocomplete="tel"')}
        {field('country', c.t(K['f_country']), extra=' autocomplete="country-name"')}
        {field('volume', c.t(K['f_volume']), 'text', extra=' inputmode="decimal"')}
        <div class="field full"><label for="f-product">{e(c.t(K['f_product']))}</label><select id="f-product" name="product" data-label="{e(c.t(K['f_product']))}">{opts}</select></div>
        <div class="field full"><label for="f-message">{e(c.t(K['f_message']))} <span class="req">*</span></label><textarea id="f-message" name="message" required data-label="{e(c.t(K['f_message']))}" placeholder="{e(c.t(K['f_message_ph']))}"></textarea></div>
        <p class="form-msg" role="alert"></p>
      </div>
      <div class="form-foot">
        <button class="btn btn-primary" type="submit">{e(c.t(K['f_submit']))} {ICON['arrow']}</button>
        <small>{e(c.t(K['f_note']))}</small>
      </div>
    </form>
    <aside class="contact-aside">
      <h2>{e(c.t(K['details_h']))}</h2>
      <ul class="contact-list">
        <li>{ICON['pin']}<div><div class="k">{e(c.t(C.UI['address']))}</div><div class="v">{e(c.t(C.COMPANY['address']))}</div></div></li>
        <li>{ICON['phone']}<div><div class="k">{e(c.t(C.UI['phone']))}</div><div class="v">{phones}</div></div></li>
        <li>{ICON['mail']}<div><div class="k">{e(c.t(C.UI['email']))}</div><div class="v">{emails}</div></div></li>
        <li>{ICON['clock']}<div><div class="k">GMT+4</div><div class="v">{e(c.t(K['hours']))}</div></div></li>
      </ul>
      <p class="muted" style="font-size:.85rem">{e(c.t(C.COMPANY['legal']))}</p>
    </aside>
  </div>
</section>
<div class="map-embed"><iframe src="{e(map_src)}" title="{e(c.t(K['map_title']))}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</main>
""" + footer(c)


def page_insights(c):
    P = C.INSIGHTS_PAGE
    cards = "".join(insight_card(c, a) for a in C.ARTICLES)
    return head(c, c.t(P["title"]) + " | Bionut", c.t(P["meta"])) + header(c) + f"""<main id="main">
{page_hero(c, c.t(P['eyebrow']), c.t(P['h1']), c.t(P['lead']), [('insights', c.t(P['title']))])}
<section class="section section-cream"><div class="wrap"><div class="insight-grid">{cards}</div></div></section>
{cta_block(c)}
</main>
""" + footer(c)


def page_article(c, a):
    title = c.t(a["title"])
    srcs = "".join('<li>%s: <a href="%s" target="_blank" rel="noopener">%s</a></li>' % (e(t), e(u), e(u)) for t, u in a["sources"])
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": title, "datePublished": a["date"],
          "inLanguage": c.lang, "image": SITE + "/assets/img/%s.webp" % a["img"],
          "publisher": {"@type": "Organization", "name": "Bionut", "logo": {"@type": "ImageObject", "url": SITE + "/assets/brand/bionut-logo.png"}}}
    others = [x for x in C.ARTICLES if x is not a]
    more = "".join(insight_card(c, x) for x in others)
    return head(c, title + " | Bionut", c.t(a["excerpt"]), extra='<script type="application/ld+json">%s</script>' % json.dumps(ld, ensure_ascii=False)) + header(c) + f"""<main id="main">
<section class="article-hero">
  <div class="wrap">
    {breadcrumb(c, [('insights', c.t(C.INSIGHTS_PAGE['title'])), (c.key, title)])}
    <div class="ic-meta"><span class="tag">{e(c.t(a['tag']))}</span><span>{e(c.t(a['date_label']))}</span><span>{a['read']} {e(c.t(C.UI['min_read']))}</span></div>
    <h1>{e(title)}</h1>
    <p class="lead">{e(c.t(a['excerpt']))}</p>
    <div class="article-cover">{pic(c, a['img'], title, sizes='100vw', priority=True)}</div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="prose">{c.t(a['body'])}</div>
    <div class="sources"><h2>{e(c.t(C.UI['sources']))}</h2><ol>{srcs}</ol></div>
  </div>
</section>
<section class="section section-cream">
  <div class="wrap">
    <div class="section-head"><div><span class="eyebrow">{e(c.t(C.UI['insights']))}</span><h2>{e(c.t(C.HOME['insights_h']))}</h2></div>
      <div class="head-actions"><a class="link-arrow" href="{c.url('insights')}">{e(c.t(C.UI['back_insights']))} {ICON['arrow']}</a></div></div>
    <div class="insight-grid">{more}</div>
  </div>
</section>
</main>
""" + footer(c)


def page_404():
    c = Ctx(C.DEFAULT_LANG, "home")
    c.rel = "/"  # 404 is served from arbitrary depths; use root-absolute assets
    body = f"""<main id="main"><section class="page-hero" style="min-height:60vh;display:flex;align-items:center"><div class="wrap">
<span class="eyebrow">404</span><h1>Səhifə tapılmadı</h1><p class="lead" style="margin-bottom:32px">Axtardığınız səhifə köçürülüb və ya artıq mövcud deyil. / Page not found.</p>
<a class="btn btn-primary" href="/">Ana səhifəyə qayıt {ICON['arrow']}</a></div></section></main>"""
    return head(c, "Səhifə tapılmadı | Bionut", "Səhifə tapılmadı") + header(c) + body + footer(c)


# ============================================================ spec sheet PDFs (minimal writer)
def _pdf_str(s):
    b = s.encode("cp1252", errors="replace")
    return b.replace(b"\\", b"\\\\").replace(b"(", b"\\(").replace(b")", b"\\)")


def _wrap(text, size, width):
    max_chars = int(width / (size * 0.5))
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > max_chars and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines


def spec_pdf(p, path, logo_jpg):
    ur = "Upon request"
    rows = [
        ("Product", p["name"]["en"]),
        ("Origin", "Gabala, Azerbaijan - own orchards"),
        ("Moisture", p["moisture"] or ur),
        ("Particle sizes" if p["size_kind"] == "sizes" else "Calibers", ", ".join(p["sizes"]) if p["sizes"] else ur),
        ("Packaging", p["packaging"]["en"] if p["packaging"] else ur),
        ("Applications", ", ".join(a["en"] for a in p["apps"])),
        ("Certifications", "FSSC 22000, ISO 22000:2018, Organic / Bio (organic lots), SEDEX member"),
        ("Minimum order", C.UI["moq"]["en"].replace("Minimum Order Quantity (MOQ): ", "")),
    ]
    ops = []

    def text(x, y, s, size=10, bold=False, color=(0.173, 0.094, 0.063)):
        ops.append("%.3f %.3f %.3f rg BT /%s %d Tf %.1f %.1f Td (" % (color + ("F2" if bold else "F1", size, x, y)))
        ops.append(_pdf_str(s))
        ops.append(") Tj ET\n")

    def line(x1, y1, x2, y2, w=0.5, color=(0.86, 0.82, 0.76)):
        ops.append("%.3f %.3f %.3f RG %.2f w %.1f %.1f m %.1f %.1f l S\n" % (color + (w, x1, y1, x2, y2)))

    gold = (0.773, 0.608, 0.373)
    green = (0.176, 0.31, 0.212)
    ops.append("0.980 0.969 0.949 rg 0 742 595 100 re f\n")
    ops.append("q 62 0 0 60 48 762 cm /Im1 Do Q\n")
    text(124, 800, "BIONUT", 18, True)
    text(124, 784, "Premium Hazelnut Ingredients from Azerbaijan", 9, False, (0.4, 0.33, 0.3))
    text(400, 800, "PRODUCT SPECIFICATION", 8, True, gold)
    text(400, 786, "Document: BN-SPEC-%s" % p["slug"][:16].upper(), 7, False, (0.4, 0.33, 0.3))
    text(400, 776, "Edition: 2026", 7, False, (0.4, 0.33, 0.3))
    line(0, 742, 595, 742, 1.2, gold)
    text(48, 700, p["name"]["en"], 22, True)
    y = 678
    for ln in _wrap(p["long"]["en"], 10, 500):
        text(48, y, ln, 10, False, (0.3, 0.24, 0.2))
        y -= 14
    y -= 18
    text(48, y, "TECHNICAL SPECIFICATION", 8, True, gold)
    y -= 12
    for k, v in rows:
        line(48, y, 547, y)
        vl = _wrap(v, 10, 330)
        yy = y - 16
        text(48, yy, k, 9, False, (0.45, 0.38, 0.34))
        for ln in vl:
            text(210, yy, ln, 10, True)
            yy -= 14
        y = yy - 6
    line(48, y, 547, y)
    y -= 28
    for ln in _wrap("Specifications are indicative. Detailed physical, chemical and microbiological parameters are confirmed per contract and accompanied by a Certificate of Analysis for each lot. Prices on request.", 8, 500):
        text(48, y, ln, 8, False, (0.45, 0.38, 0.34))
        y -= 11
    # footer
    ops.append("%.3f %.3f %.3f rg 0 0 595 92 re f\n" % green)
    text(48, 64, C.COMPANY["legal"]["en"], 9, True, (0.98, 0.97, 0.95))
    text(48, 50, C.COMPANY["address"]["en"], 8, False, (0.85, 0.85, 0.82))
    text(48, 37, "Tel: " + "  |  ".join(C.COMPANY["phones"]) + "     Email: info@bionut.az     www.bionut.az", 8, False, (0.85, 0.85, 0.82))
    text(48, 20, C.COMPANY["copyright"].replace("©", "(c)"), 7, False, gold)

    stream = zlib.compress(b"".join(o if isinstance(o, bytes) else o.encode("latin-1") for o in ops))
    img = open(logo_jpg, "rb").read()
    iw, ih = dims_any(logo_jpg)
    objs = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 4 0 R /F2 5 0 R >> /XObject << /Im1 6 0 R >> >> /Contents 7 0 R >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>",
        ("<< /Type /XObject /Subtype /Image /Width %d /Height %d /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length %d >>\nstream\n" % (iw, ih, len(img))).encode() + img + b"\nendstream",
        ("<< /Length %d /Filter /FlateDecode >>\nstream\n" % len(stream)).encode() + stream + b"\nendstream",
        ("<< /Title (%s - Product Specification) /Author (Bionut) /Producer (bionut.az) >>" % p["name"]["en"]).encode(),
    ]
    out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = []
    for i, o in enumerate(objs, 1):
        offsets.append(len(out))
        out += b"%d 0 obj\n" % i + o + b"\nendobj\n"
    xref = len(out)
    out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objs) + 1)
    for off in offsets:
        out += b"%010d 00000 n \n" % off
    out += b"trailer\n<< /Size %d /Root 1 0 R /Info %d 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (len(objs) + 1, len(objs), xref)
    open(path, "wb").write(out)


def dims_any(path):
    w, h = subprocess.check_output(["identify", "-format", "%w %h", path]).decode().split()[:2]
    return int(w), int(h)


# ============================================================ build
def write(rel_path, text):
    path = os.path.join(OUT, rel_path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"))

    keys = ["home", "about", "products", "process", "certifications", "contact", "insights"] + \
        ["product:" + p["slug"] for p in C.PRODUCTS] + ["article:" + a["slug"] for a in C.ARTICLES]
    urls = []
    for lang in C.LANGS:
        for key in keys:
            c = Ctx(lang, key)
            if key == "home":
                h = page_home(c)
            elif key == "about":
                h = page_about(c)
            elif key == "products":
                h = page_products(c)
            elif key == "process":
                h = page_process(c)
            elif key == "certifications":
                h = page_certs(c)
            elif key == "contact":
                h = page_contact(c)
            elif key == "insights":
                h = page_insights(c)
            elif key.startswith("product:"):
                h = page_product(c, next(p for p in C.PRODUCTS if p["slug"] == key[8:]))
            else:
                h = page_article(c, next(a for a in C.ARTICLES if a["slug"] == key[8:]))
            write(c.full + "index.html", h)
            urls.append((key, lang))
    write("404.html", page_404())

    # spec sheets
    specs = os.path.join(OUT, "assets", "specs")
    os.makedirs(specs, exist_ok=True)
    logo_jpg = os.path.join(specs, "_logo.jpg")
    subprocess.check_call(["convert", os.path.join(ROOT, "assets", "brand", "bionut-logo.png"), "-background", "#FAF7F2", "-flatten", "-quality", "92", logo_jpg])
    for p in C.PRODUCTS:
        spec_pdf(p, os.path.join(specs, "bionut-%s-specification.pdf" % p["slug"]), logo_jpg)
    os.remove(logo_jpg)

    # sitemap + robots
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for key, lang in urls:
        c = Ctx(lang, key)
        alts = "".join('<xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (l, c.abs(lang=l)) for l in C.LANGS)
        sm.append("<url><loc>%s</loc>%s<lastmod>2026-11-19</lastmod></url>" % (c.abs(), alts))
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm))
    write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)
    write(".nojekyll", "")
    print("Built %d pages into %s" % (len(urls) + 1, OUT))


if __name__ == "__main__":
    main()
