# -*- coding: utf-8 -*-
"""
WordPress niche content: all copy for seoprewordpress.info (SK + CZ).

Keywords grounded in Marketing Miner SK data (2026-09):
wordpress seo 360, seo optimalizacia wordpress 130, seo blog wordpress 120,
wordpress seo plugin 40, seo optimalizacia navod 1200, seo optimalizacia cena 620.
"""

from engine import _VIOLET, _ORANGE, _CERULEAN, _VIOLET_L, _sparkline, _bars

# ---------------------------------------------------------------- services
# (sk_path, cz_path, SK label, CZ label)
SERVICE_DEFS = [
    ("sluzby/seo-optimalizacia/", "sluzby/seo-optimalizace/",
     "SEO optimalizácia WordPress webu", "SEO optimalizace WordPress webu"),
    ("sluzby/technicke-seo/", "sluzby/technicke-seo/",
     "Technické SEO a rýchlosť WordPressu", "Technické SEO a rychlost WordPressu"),
    ("sluzby/obsah-a-blog/", "sluzby/obsah-a-blog/",
     "Obsah a blog na WordPress", "Obsah a blog na WordPress"),
    ("sluzby/wordpress-audit/", "sluzby/wordpress-audit/",
     "SEO audit WordPress webu", "SEO audit WordPress webu"),
]
SERVICE_DEFS_TEXT = [
    ("Nastavím WordPress tak, aby Google vašim stránkam rozumel: štruktúra, titulky, obsah aj interné odkazy.",
     "Nastavím WordPress tak, aby Google vašim stránkám rozumel: struktura, titulky, obsah i interní odkazy."),
    ("Rýchlosť, mobile-friendly, sitemap, robots.txt a čisté adresy. Základy, bez ktorých sa WordPress web nedostane hore.",
     "Rychlost, mobile-friendly, sitemap, robots.txt a čisté adresy. Základy, bez kterých se WordPress web nedostane výš."),
    ("Blog a obsahové stránky písané na kľúčové slová, ktoré hľadajú vaši zákazníci, nie len na slová, ktoré sa dajú napísať.",
     "Blog a obsahové stránky psané na klíčová slova, která hledají vaši zákazníci, ne jen na slova, která se dají napsat."),
    ("Presný obraz toho, čo váš WordPress web brzdí: 15-bodová kontrola s plánom podľa priorít.",
     "Přesný obraz toho, co váš WordPress web brzdí: 15-bodová kontrola s plánem podle priorit."),
]
SERVICE_DEFS_ICON = ["wp", "bolt", "mail", "audit"]
SERVICE_DEFS_COLOR = ["#6A3FC4", "#F75940", "#1DACD6", "#6A3FC4"]
SERVICE_DEFS_TAG = ["tag-violet", "tag-orange", "tag-cerulean", "tag-violet-light"]

SLIDES = [
    {"client": "WordPress web (klient)", "chip": "Obsah + technika",
     "period": "posledných 28 dní",
     "nums": [{"big": "121", "color": _VIOLET, "label": "klikov z Google (+49 %)"},
              {"big": "4 390", "color": _ORANGE, "label": "zobrazení v Google (+43 %)"},
              {"big": "+142 %", "color": _VIOLET_L, "label": "rast hlavnej stránky"}],
     "chart": _sparkline([40, 55, 48, 62, 58, 75, 70, 88, 95, 92, 110, 121], _VIOLET),
     "caption": "Prvý mesiac spolupráce na WordPress webe: technické SEO a obsah. Google začal prinášať zákazníkov hneď."},
    {"client": "Blog na WordPress (klient)", "chip": "Obsah na 6 stránkach",
     "period": "28 dní + posledný týždeň",
     "nums": [{"big": "11 000", "color": _CERULEAN, "label": "zobrazení mesačne (+14 %)"},
              {"big": "+43 %", "color": _VIOLET, "label": "klikov posledný týždeň"},
              {"big": "6", "color": _ORANGE, "label": "stránok, na ktorých sa to stalo"}],
     "chart": _sparkline([30, 38, 42, 50, 55, 62, 66, 72, 78, 84, 92, 102], _CERULEAN),
     "caption": "Pridané obsahové stránky na reálne dopyty zákazníkov. Len 6 stránok z celého WordPress webu posunulo celý web."},
]

PROCESS = {
    "sk": {
        "s1_t": "Bezplatný audit WordPress webu", "s1_x": "Začneme 30-minútovým hovorom a bezplatným auditom. Pozrieme štruktúru, rýchlosť, obsah aj to, čo Google o vašom webe vidí.",
        "s2_t": "Plán podľa priorít", "s2_x": "Z auditu spravím jasný plán: čo opraviť ako prvé, ktoré kľúčové slová prinášajú zákazníkov a koľko hodín mesačne to zaberie.",
        "s3_t": "Práca priamo vo vašom WordPress", "s3_x": "Pracujem v adminovi alebo cez staging: technika, obsah, pluginy, štruktúra. Vždy viete, čo sa stalo v predchádzajúcom týždni.",
        "s4_t": "Meranie a report", "s4_x": "Mesačný report vám dám osobne: 30-minútový telefonát. Pozície, kliky z Google, čo sme urobili a čo nasleduje. Platíte len za odpracované hodiny.",
    },
    "cz": {
        "s1_t": "Bezplatný audit WordPress webu", "s1_x": "Začneme 30minutovým hovorem a bezplatným auditem. Podíváme se na strukturu, rychlost, obsah i na to, co Google o vašem webu vidí.",
        "s2_t": "Plán podle priorit", "s2_x": "Z auditu udělám jasný plán: co opravit jako první, která klíčová slova přinášejí zákazníky a kolik hodin měsíčně to zabere.",
        "s3_t": "Práce přímo ve vašem WordPress", "s3_x": "Pracuji v adminu nebo přes staging: technika, obsah, pluginy, struktura. Vždy víte, co se stalo v předchozím týdnu.",
        "s4_t": "Měření a report", "s4_x": "Měsíční report vám dám osobně: 30minutový telefonát. Pozice, kliky z Google, co jsme udělali a co následuje. Platíte jen za odpracované hodiny.",
    },
}

FAQ = {
    "sk": {
        "common": [
            ("Koľko stojí SEO pre WordPress web?",
             "Za prácu platíte 12 EUR za hodinu. Malý WordPress web zvládnem za 10 hodín mesačne (120 EUR), väčší web s blogom za 20 až 30 hodín. Presný rozsah vám potvrdím v pláne po bezplatnom audite."),
            ("Je WordPress dobrý pre SEO?",
             "Áno. WordPress sám o sebe nie je prekážkou, ale šablóna, pluginy a rýchlosť často brzdia. Riešim presne to: aby web posielal Google správne signály a rýchlo sa načítal."),
            ("Ktorý WordPress SEO plugin potrebujem?",
             "Na meta titulky a popisy stačí jeden (Yoast alebo Rank Math). Plugin ale sám SEO neurobí, robí ho obsah a technika. Čo presne nastaviť vám ukážem pri audite."),
            ("Ako dlho trvá, kým WordPress SEO prinesie výsledky?",
             "Prvé pohyby na menej konkurenčných kľúčových slovách zvyčajne za 2 až 4 mesiace. Na hlavné dotazy 6 až 12 mesiacov. Reálne termíny vám poviem už v audite."),
            ("Pracujete aj s WooCommerce?",
             "Áno, WooCommerce e-shopy sú bežná súčasť mojej práce: kategórie, produkty aj technické zázemie WordPressu."),
        ],
        "sluzby": [
            ("Aké služby pre WordPress robíte?",
             "SEO optimalizáciu webu, technické SEO a rýchlosť, obsah a blog, aj komplexný SEO audit. Všetko priamo vo vašom WordPress adminovi, za 12 EUR za hodinu."),
            ("Potrebujem redizajn webu, aby sa zlepšilo SEO?",
             "Nemusí. Väčšinu zlepšení urobím v existujúcom WordPress: štruktúra, rýchlosť, obsah. Redizajn je posledná voľba, nie prvá."),
        ],
        "cennik": [
            ("Prečo hodinová cena a nie paušál?",
             "Lebo viete presne, za čo platíte. Každá hodina je vykázaná v mesačnom reporte. Balíčky sú len odporúčané rozsahy, kedykoľvek ich môžete meniť."),
            ("Koľko hodín potrebuje WordPress web mesačne?",
             "Malý web 10 hodín (120 EUR), web s blogom 15 až 20 hodín, e-commerce na WooCommerce 30 až 40 hodín. Spresní to plán po audite."),
        ],
        "proces": [
            ("Do akého WordPressu sa pripojím?",
             "Potrebujem dočasné prihlásenie do admina alebo konto s rolou admin. Pracujem aj cez staging prostredie, ak ho máte."),
            ("Čo ak mám WordPress web na šablene s limitmi?",
             "Riešim aj weby na webhostingoch s obmedzeniami. Čo sa nedá spraviť, vám povedané priamo pri audite, nie po mesiaci platby."),
        ],
    },
    "cz": {
        "common": [
            ("Kolik stojí SEO pro WordPress web?",
             "Za práci platíte 12 EUR za hodinu. Malý WordPress web zvládnu za 10 hodin měsíčně (120 EUR), větší web s blogem za 20 až 30 hodin. Přesný rozsah potvrdím v plánu po bezplatném auditu."),
            ("Je WordPress dobrý pro SEO?",
             "Ano. WordPress sám o sobě není překážkou, ale šablona, pluginy a rychlost často brzdí. Řeším přesně to: aby web posílal Google správné signály a rychle se načítal."),
            ("Který WordPress SEO plugin potřebuji?",
             "Na meta titulky a popisy stačí jeden (Yoast nebo Rank Math). Plugin ale sám SEO neudělá, dělá ho obsah a technika. Co přesně nastavit vám ukážu při auditu."),
            ("Jak dlouho trvá, než WordPress SEO přinese výsledky?",
             "První pohyby na méně konkurenčních klíčových slovech zpravidla za 2 až 4 měsíce. Na hlavní dotazy 6 až 12 měsíců. Reálné termíny vám řeknu už v auditu."),
            ("Pracujete i s WooCommerce?",
             "Ano, WooCommerce e-shopy jsou běžná součást mé práce: kategorie, produkty i technické zázemí WordPressu."),
        ],
        "sluzby": [
            ("Jaké služby pro WordPress děláte?",
             "SEO optimalizaci webu, technické SEO a rychlost, obsah a blog, i komplexní SEO audit. Vše přímo ve vašem WordPress adminu, za 12 EUR za hodinu."),
            ("Potřebuji redesign webu, aby se zlepšilo SEO?",
             "Nemusí. Většinu zlepšení udělám v existujícím WordPress: struktura, rychlost, obsah. Redesign je poslední volba, ne první."),
        ],
        "cennik": [
            ("Proč hodinová cena a ne paušál?",
             "Protože víte přesně, za co platíte. Každá hodina je vykázaná v měsíčním reportu. Balíčky jsou jen doporučené rozsahy, kdykoliv je můžete měnit."),
            ("Kolik hodin potřebuje WordPress web měsíčně?",
             "Malý web 10 hodin (120 EUR), web s blogem 15 až 20 hodin, e-commerce na WooCommerce 30 až 40 hodin. Spřesní to plán po auditu."),
        ],
        "proces": [
            ("Do jakého WordPressu se připojím?",
             "Potřebuji dočasné přihlášení do adminu nebo účet s rolí admin. Pracuji i přes staging prostředí, pokud ho máte."),
            ("Co když mám WordPress web na šabloně s limity?",
             "Řeším i weby na hostincích s omezeními. Co se nedá udělat, vám řeknu přímo při auditu, ne po měsíci platby."),
        ],
    },
}

DETAIL = [
    {  # 0: seo-optimalizacia
        "sk": {
            "h1": 'SEO optimalizácia WordPress webu: nech vás <span class="hl-violet">Google</span> nájde',
            "sub": "Štruktúra, titulky, obsah a interné odkazy nastavené priamo vo vašom WordPress. Bez zásahov do kódu, ak nie sú potrebné.",
            "title": "SEO optimalizácia WordPress webu | SEO pre WordPress",
            "desc": "SEO optimalizácia WordPress webu za 12 EUR za hodinu. Štruktúra, meta údaje, obsah a interné odkazy. Nokto Studio, SEO špecialista.",
            "b1_t": "Čo nastavím", "b1_x": "Štruktúru URL, meta titulky a popisy, nadpisy H1 až H3, interné odkazy medzi článkami a stránkami, sitemap a spracovanie 404 stránok.",
            "b2_t": "Čo dostanete", "b2_x": "WordPress web, ktorému Google rozumie: správne štruktúrované stránky, obsah na kľúčové slová zákazníkov a čisté interné odkazy.",
            "what_t": "Ako SEO na WordPress prebieha",
            "what_x": "Pracujem priamo vo vašom WordPress adminovi. Nemusím pristupovať ku kódu, ak to nie je potrebné. Každá zmena je popísaná v reporte.",
        },
        "cz": {
            "h1": 'SEO optimalizace WordPress webu: nech vás <span class="hl-violet">Google</span> najde',
            "sub": "Struktura, titulky, obsah a interní odkazy nastavené přímo ve vašem WordPress. Bez zásahů do kódu, pokud nejsou potřeba.",
            "title": "SEO optimalizace WordPress webu | SEO pro WordPress",
            "desc": "SEO optimalizace WordPress webu za 12 EUR za hodinu. Struktura, meta údaje, obsah a interní odkazy. Nokto Studio, SEO specialista.",
            "b1_t": "Co nastavím", "b1_x": "Strukturu URL, meta titulky a popisy, nadpisy H1 až H3, interní odkazy mezi články a stránkami, sitemap a spracování 404 stránek.",
            "b2_t": "Co dostanete", "b2_x": "WordPress web, kterému Google rozumí: správně strukturované stránky, obsah na klíčová slova zákazníků a čisté interní odkazy.",
            "what_t": "Jak SEO na WordPress probíhá",
            "what_x": "Pracuji přímo ve vašem WordPress adminu. Nemusím přistupovat ke kódu, pokud to není nutné. Každá změna je popsána v reportu.",
        },
    },
    {  # 1: technicke-seo
        "sk": {
            "h1": 'Technické SEO a <span class="hl-orange">rýchlosť</span> WordPressu',
            "sub": "Rýchlosť načítania, mobile-friendly, čisté adresy, sitemap, robots.txt. Základy, ktoré rozhodujú o tom, či sa web vôbec dostane hore.",
            "title": "Technické SEO a rýchlosť WordPressu | SEO pre WordPress",
            "desc": "Technické SEO a rýchlosť WordPress webu. Core Web Vitals, sitemap, robots.txt, čisté adresy. 12 EUR za hodinu, Nokto Studio.",
            "b1_t": "Čo riešim", "b1_x": "Rýchlosť načítania (Core Web Vitals), mobile verziu, správne presmerovania, sitemap, robots.txt, cache a optimalizáciu obrázkov.",
            "b2_t": "Prečo to rozhoduje", "b2_x": "Pomalý WordPress web stráca zákazníkov aj pozície. Google meria rýchlosť ako signál kvality. Oprava je často rýchlejšia, než sa čaká.",
            "what_t": "Ako technické SEO prebieha",
            "what_x": "Začnem meraním: PageSpeed Insights a Search Console. Potom nasledujú konkrétne opravy v adminovi, hostingu alebo v pluginoch.",
        },
        "cz": {
            "h1": 'Technické SEO a <span class="hl-orange">rychlost</span> WordPressu',
            "sub": "Rychlost načítání, mobile-friendly, čisté adresy, sitemap, robots.txt. Základy, které rozhodují o tom, zda se web vůbec dostane výš.",
            "title": "Technické SEO a rychlost WordPressu | SEO pro WordPress",
            "desc": "Technické SEO a rychlost WordPress webu. Core Web Vitals, sitemap, robots.txt, čisté adresy. 12 EUR za hodinu, Nokto Studio.",
            "b1_t": "Co řeším", "b1_x": "Rychlost načítání (Core Web Vitals), mobilní verzi, správná přesměrování, sitemap, robots.txt, cache a optimalizaci obrázků.",
            "b2_t": "Proč to rozhoduje", "b2_x": "Pomalý WordPress web ztrácí zákazníky i pozice. Google měří rychlost jako signál kvality. Oprava je často rychlejší, než se čeká.",
            "what_t": "Jak technické SEO probíhá",
            "what_x": "Začnu měřením: PageSpeed Insights a Search Console. Potom následují konkrétní opravy v adminu, hostingu nebo v pluginech.",
        },
    },
    {  # 2: obsah-a-blog
        "sk": {
            "h1": '<span class="hl-cerulean-light">Obsah</span> a blog na WordPress, ktorý Google aj ľudia čítajú',
            "sub": "Články písané na kľúčové slová, ktoré hľadajú vaši zákazníci. Štruktúra, ktorú Google rozumie, a štýl, ktorý ľudia dočítajú.",
            "title": "Obsah a blog na WordPress pre SEO | SEO pre WordPress",
            "desc": "Obsah a blog na WordPress písaný na kľúčové slová zákazníkov. Štruktúra pre Google aj čitateľov. 12 EUR za hodinu, Nokto Studio.",
            "b1_t": "Čo píšem", "b1_x": "Blogové články, obsahové stránky služieb a kategórií. Vždy na kľúčové slová, ktoré majú hľadanie, nie na slová, ktoré sa len ľahko napíšu.",
            "b2_t": "Prečo to funguje", "b2_x": "Google radí web výš, keď odpovedá na reálne otázky zákazníkov. Blog na WordPress je najrýchlejší spôsob, ako tieto otázky pokryť.",
            "what_t": "Ako obsah pre WordPress vzniká",
            "what_x": "Najprv kľúčové slová a štruktúra témy, potom článok. Vkladám ho priamo do WordPressu s meta údajmi, nadpismi a internými odkazmi.",
        },
        "cz": {
            "h1": '<span class="hl-cerulean-light">Obsah</span> a blog na WordPress, který Google i lidé čtou',
            "sub": "Články psané na klíčová slova, která hledají vaši zákazníci. Struktura, které Google rozumí, a styl, který lidé dočtou.",
            "title": "Obsah a blog na WordPress pro SEO | SEO pro WordPress",
            "desc": "Obsah a blog na WordPress psaný na klíčová slova zákazníků. Struktura pro Google i čtenáře. 12 EUR za hodinu, Nokto Studio.",
            "b1_t": "Co píšu", "b1_x": "Blogové články, obsahové stránky služeb a kategorií. Vždy na klíčová slova, která mají hledání, ne na slova, která se jen snadno napíšou.",
            "b2_t": "Proč to funguje", "b2_x": "Google řadí web výš, když odpovídá na reálné otázky zákazníků. Blog na WordPress je nejrychlejší způsob, jak tyto otázky pokrýt.",
            "what_t": "Jak obsah pro WordPress vzniká",
            "what_x": "Nejdřív klíčová slova a struktura tématu, potom článek. Vkládám ho přímo do WordPressu s meta údaji, nadpisy a interními odkazy.",
        },
    },
    {  # 3: wordpress-audit
        "sk": {
            "h1": '<span class="hl-violet-light">SEO audit</span> WordPress webu: 15 bodov, ktoré brzdia váš web',
            "sub": "Presný obraz toho, čo váš WordPress web brzdí: technika, obsah aj pozície v Google. Bezplatný audit ako prvý krok.",
            "title": "SEO audit WordPress webu | SEO pre WordPress",
            "desc": "SEO audit WordPress webu: 15 bodová kontrola techniky, obsahu a pozícií. Bezplatný vstupný audit. Nokto Studio, SEO špecialista.",
            "b1_t": "Čo auditem zistím", "b1_x": "Ktoré stránky Google vidí a ktoré nie, kde web stráca rýchlosť, čo brzdí obsah a na ktorých kľúčových slovách sa web dá posunúť ako prvé.",
            "b2_t": "Ako audit vyzerá", "b2_x": "15-bodová kontrola so zoznamom opráv podľa priorít. Bezplatný vstupný audit robím ešte pred prvou faktúrou, aby ste videli, čo by SEO u vás znamenalo.",
            "what_t": "Po audite",
            "what_x": "Dostanete plán: čo opraviť ako prvé, ktoré kľúčové slová riešiť a koľko hodín mesačne to zaberá. Rozhodnutie je vaše, bez záväzku.",
        },
        "cz": {
            "h1": '<span class="hl-violet-light">SEO audit</span> WordPress webu: 15 bodů, které brzdí váš web',
            "sub": "Přesný obraz toho, co váš WordPress web brzdí: technika, obsah i pozice v Google. Bezplatný audit jako první krok.",
            "title": "SEO audit WordPress webu | SEO pro WordPress",
            "desc": "SEO audit WordPress webu: 15 bodová kontrola techniky, obsahu a pozic. Bezplatný vstupní audit. Nokto Studio, SEO specialista.",
            "b1_t": "Co auditem zjistím", "b1_x": "Které stránky Google vidí a které ne, kde web ztrácí rychlost, co brzdí obsah a na kterých klíčových slovech se web dá posunout jako první.",
            "b2_t": "Jak audit vypadá", "b2_x": "15 bodová kontrola se seznamem oprav podle priorit. Bezplatný vstupní audit dělám ještě před první fakturou, abyste viděli, co by SEO u vás znamenalo.",
            "what_t": "Po auditu",
            "what_x": "Dostanete plán: co opravit jako první, která klíčová slova řešit a kolik hodin měsíčně to zabere. Rozhodnutí je vaše, bez závazku.",
        },
    },
]

DETAIL_FAQ = {
    0: {
        "sk": [("Zmeníte aj šablónu, ak treba?", "Áno, menším úpravám šablóny sa nevyhýbam. Väčší redizajn odporúčam až po audite, ak technika a obsah nezvládnu výsledok."),
               ("Pracujete aj s Elementor a page buildermi?", "Áno. Page buildery často pridávajú zbytočný kód, ktorý brzdí web. Viem posúdiť, čo opraviť a čo prenechať.")],
        "cz": [("Změníte i šablonu, pokud je potřeba?", "Ano, menším úpravám šablony se nevyhýbám. Větší redesign doporučím až po auditu, pokud technika a obsah nevezmou výsledek."),
               ("Pracujete i s Elementor a page buildery?", "Ano. Page buildery často přidávají zbytečný kód, který web brzdí. Umím posoudit, co opravit a co nechat.")],
    },
    1: {
        "sk": [("Ako dlho trvá oprava rýchlosti?", "Základné opravy (cache, obrázky, nepotrebné pluginy) trvajú zvyčajne pár hodín. Väčšie zásahy do hostingu pár dní."),
               ("Máte prístup aj k hostingu?", "Ak treba, áno. Väčšina technických opráv sa dá urobiť z admina, ale hosting niekedy rozhoduje.")],
        "cz": [("Jak dlouho trvá oprava rychlosti?", "Základní opravy (cache, obrázky, nepotřebné pluginy) trvají zpravidla pár hodin. Větší zásahy do hostingu pár dní."),
               ("Máte přístup i k hostingu?", "Když je potřeba, ano. Většina technických oprav jde udělat z adminu, ale hosting někdy rozhoduje.")],
    },
    2: {
        "sk": [("Vkladáte články aj do WordPressu, alebo mi ich pošlete?", "Vkladám ich priamo do WordPressu s meta údajmi, nadpismi a internými odkazmi. Vy len schvaľujete a publikujete."),
               ("Aká je dĺžka článkov?", "Dĺžku určuje téma a konkurencia, nie pravidlo. Typicky 800 až 2000 slov, každý článok má plán a cieľové kľúčové slovo.")],
        "cz": [("Vkládáte články i do WordPressu, nebo je pošlete?", "Vkládám je přímo do WordPressu s meta údaji, nadpisy a interními odkazy. Vy jen schvalujete a publikujete."),
               ("Jaká je délka článků?", "Délku určuje téma a konkurence, ne pravidlo. Typicky 800 až 2000 slov, každý článek má plán a cílové klíčové slovo.")],
    },
    3: {
        "sk": [("Je audit skutočne bezplatný?", "Áno. Audit a 30-minútový hovor sú bezplatné, bez záväzku. Platíte až za samotnú prácu po pláne."),
               ("Ako rýchlo dostanem výsledky auditu?", "Zvyčajne do 5 pracovných dní od hovoru. Pri väčších weboch som to povedané vopred.")],
        "cz": [("Je audit skutečně bezplatný?", "Ano. Audit a 30minutový hovor jsou bezplatné, bez závazku. Platíte až za samotnou práci po plánu."),
               ("Jak rychle dostanu výsledky auditu?", "Zpravidla do 5 pracovních dnů od hovoru. U větších webů to řeknu předem.")],
    },
}

BLOG_POSTS = {
    "sk": [
        {"href": "blog/seo-wordpress-navod/", "title": "SEO pre WordPress: návod krok za krokom (2026)",
         "desc": "Ako nastaviť WordPress pre Google: štruktúra, pluginy, rýchlosť a obsah. Bez zbytočnej technickej reči.", "tag": "Návod"},
        {"href": "blog/wordpress-seo-pluginy/", "title": "WordPress SEO pluginy: čo naozaj potrebujete",
         "desc": "Yoast vs Rank Math a prečo plugin sám SEO neurobí. Čo nastaviť v každom z nich.", "tag": "Nástroje"},
        {"href": "blog/rychlost-wordpressu/", "title": "Rýchlosť WordPressu: ako zrýchliť web pre Google",
         "desc": "Core Web Vitals, cache a obrázky. Čo najviac posúva rýchlosť a čo je len marketing.", "tag": "Technika"},
        {"href": "blog/seo-blog-na-wordpress/", "title": "Ako písať blog na WordPress, ktorý Google rád",
         "desc": "Štruktúra článku, kľúčové slová a interné odkazy. Ako písať, aby článok niekto čítal a Google ho rád.", "tag": "Obsah"},
    ],
    "cz": [
        {"href": "blog/seo-wordpress-navod/", "title": "SEO pro WordPress: návod krok za krokem (2026)",
         "desc": "Jak nastavit WordPress pro Google: struktura, pluginy, rychlost a obsah. Bez zbytečné technické řeči.", "tag": "Návod"},
        {"href": "blog/wordpress-seo-pluginy/", "title": "WordPress SEO pluginy: co opravdu potřebujete",
         "desc": "Yoast vs Rank Math a proč plugin sám SEO neudělá. Co nastavit v každém z nich.", "tag": "Nástroje"},
        {"href": "blog/rychlost-wordpressu/", "title": "Rychlost WordPressu: jak zrychlit web pro Google",
         "desc": "Core Web Vitals, cache a obrázky. Co nejvíc posouvá rychlost a co je jen marketing.", "tag": "Technika"},
        {"href": "blog/seo-blog-na-wordpress/", "title": "Jak psát blog na WordPress, který Google rád",
         "desc": "Struktura článku, klíčová slova a interní odkazy. Jak psát, aby článek někdo četl a Google ho rád.", "tag": "Obsah"},
    ],
}