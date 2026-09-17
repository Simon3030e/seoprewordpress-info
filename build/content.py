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


# ---------------------------------------------------------------- blog articles
# BLOG_ARTICLES[slug][market] = full post content. Answer-first structure per
# the noktostudio blog format: Stručná odpoveď, sections, FAQ, related posts.
# Pricing: 12 EUR/hod, monthly retainers 120-480 EUR.

BLOG_ARTICLES = {
    "seo-wordpress-navod": {
        "slug": "seo-wordpress-navod",
        "sk": {
            "label": "Návod",
            "h1": "SEO pre WordPress: kompletný návod 2026",
            "title": "SEO pre WordPress: kompletný návod 2026 | SEO pre WordPress",
            "desc": "SEO pre WordPress krok za krokom: nastavenie, pluginy, rýchlosť, obsah a meranie. Návod s reálnymi číslami a cenami od 120 EUR mesačne.",
            "date_display": "17. 9. 2026",
            "date_iso": "2026-09-17",
            "answer": "SEO pre WordPress je nastavenie webu tak, aby mu Google rozumel: čisté permalinky, jeden SEO plugin (Yoast alebo Rank Math), rýchlosť pod 2,5 sekundy LCP, sitemap v Search Console a obsah na dopyty, ktoré zákazníci reálne hľadajú. Prvé pohyby za 2 až 4 mesiace, cena od 120 EUR mesačne (12 EUR za hodinu, 10 hodín pre malý web).",
            "sections": """
<h2>Čo Google od WordPress webu očakáva</h2>
<p>WordPress je dobrý základ pre SEO, ale samotná inštalácia nestačí. Google hodnotí tri skupiny vecí: <strong>techniku</strong> (rýchlosť, indexáciu, mobilnú verziu), <strong>obsah</strong> (relevanciu k dopytom) a <strong>autoritu</strong> (odkazy a zmienky). WordPress weby najčastejšie zlyhávajú na dvoch miestach: rýchlosť (veľa pluginov, ťažká šablóna) a obsah (blog, ktorý nikto nepíše). Presne tieto dve veci riešim pri spolupráci.</p>

<h2>Krok 1: Základné nastavenie (30 minút)</h2>
<ul>
<li><strong>Permalinky</strong>: Nastavenia → Trvalé odkazy → "Názov príspevku". Čisté adresy ako /blog/seo-wordpress-navod/ nie /?p=123.</li>
<li><strong>SEO plugin</strong>: Yoast alebo Rank Math. Jeden stačí, dva sa bijú. Nastavíte meta titulky, popisy a sitemap.</li>
<li><strong>Search Console</strong>: overte si web a pošlite sitemap.xml. Google začne vidieť vaše stránky.</li>
<li><strong>HTTPS</strong>: vždy. Google meria bezpečnosť ako signál.</li>
</ul>

<h2>Krok 2: Rýchlosť, ktorá Google uspokojí</h2>
<p>WordPress weby bývajú pomalé kvôli ťažkým šablónam, zbytočným pluginom a neoptimalizovaným obrázkom. Cieľ: LCP pod 2,5 s, INP pod 200 ms, CLS pod 0,1. V praxi: jeden cache plugin (WP Rocket alebo LiteSpeed Cache), WebP obrázky, odinštalovať nepoužívané pluginy. Meranie: <a href="https://pagespeed.web.dev/" target="_blank" rel="noopener noreferrer">PageSpeed Insights</a>, bezplatný.</p>

<h2>Krok 3: Obsah na dopyty, ktoré hľadajú zákazníci</h2>
<p>Blog na WordPress je najrýchlejšia cesta k zákazníkom z Google. Napíšte články na otázky, ktoré si zákazníci kladú pred nákupom: "ako si vybrať...", "koľko stojí...", "najlepší X pre Y". Každý článok: jedno cieľové kľúčové slovo, H2 nadpisy, interný odkaz na službu, 800 až 1500 slov. Dopyty a objemy overíte cez Marketing Miner (SK/CZ dáta) alebo Google autocomplete.</p>

<h2>Krok 4: Meranie a udržiavanie</h2>
<p>Mesačne skontrolujte: pozície a kliky (Search Console), rýchlosť (PageSpeed), nové obsahy. Staré články po roku obnovte, Google ich rád re-indexuje. Ak nechcete robiť SEO sami, robím to za vás: 12 EUR za hodinu, retainer od 120 EUR mesačne pre malý web, 240 až 480 EUR pre web s blogom a e-commerce. Všetko vykázané v mesačnom reporte.</p>

<h2>Koľko to stojí v praxi</h2>
<p>Malý web (10 strán): 10 hodín mesačne = 120 EUR. Web s blogom (2 články mesačne + technika): 15 až 20 hodín = 180 až 240 EUR. WooCommerce e-shop: 30 až 40 hodín = 360 až 480 EUR. Prvá hodina je bezplatný hovor a audit, aby ste videli, čo by SEO u vás znamenalo.</p>
""",
            "faq": [
                ("Potrebujem na SEO WordPress platiť pluginy?", "Nie. Bezplatný Yoast alebo Rank Math pokrýva meta údaje a sitemap. Platene pluginy (WP Rocket na cache) pomáhajú pri rýchlosti, ale nie sú podmienkou."),
                ("Môžem SEO na WordPress robiť sám?", "Základy áno: permalinky, plugin, obsah. Práca s pozíciami na konkurenčných dopytoch, technika a stratégia sú už práca pre špecialistu. Začnite sám, keď narazíte na stenu, ozvite sa."),
                ("Ako dlho trvá, kým WordPress SEO funguje?", "Prvé pohyby na menej konkurenčných dopytoch za 2 až 4 mesiace. Hlavné dopyty 6 až 12 mesiacov. Záleží na konkurencii vo vašom odvetví."),
            ],
            "related": [
                ("wordpress-seo-pluginy", "WordPress SEO pluginy: čo naozaj potrebujete"),
                ("rychlost-wordpressu", "Rýchlosť WordPressu: ako zrýchliť web pre Google"),
            ],
        },
        "cz": {
            "label": "Návod",
            "h1": "SEO pro WordPress: kompletní návod 2026",
            "title": "SEO pro WordPress: kompletní návod 2026 | SEO pro WordPress",
            "desc": "SEO pro WordPress krok za krokem: nastavení, pluginy, rychlost, obsah a měření. Návod s reálnými čísly a cenami od 120 EUR měsíčně.",
            "date_display": "17. 9. 2026",
            "date_iso": "2026-09-17",
            "answer": "SEO pro WordPress je nastavení webu tak, aby mu Google rozumel: čisté permalinky, jeden SEO plugin (Yoast nebo Rank Math), rychlost pod 2,5 sekundy LCP, sitemap v Search Console a obsah na dotazy, které zákazníci reálně hledají. První pohyby za 2 až 4 měsíce, cena od 120 EUR měsíčně (12 EUR za hodinu, 10 hodin pro malý web).",
            "sections": """
<h2>Co Google od webu na WordPress očekává</h2>
<p>WordPress je dobrý základ pro SEO, ale samotná instalace nestačí. Google hodnotí tři skupiny věcí: <strong>techniku</strong> (rychlost, indexaci, mobilní verzi), <strong>obsah</strong> (relevanci k dotazům) a <strong>autoritu</strong> (odkazy a zmínky). WordPress weby nejčastěji selhávají na dvou místech: rychlost (mnoho pluginů, těžká šablona) a obsah (blog, který nikdo nepíše). Přesně tyhle dvě věci řeším při spolupráci.</p>

<h2>Krok 1: Základní nastavení (30 minut)</h2>
<ul>
<li><strong>Permalinky</strong>: Nastavení → Trvalé odkazy → "Název příspěvku". Čisté adresy jako /blog/seo-wordpress-navod/, ne /?p=123.</li>
<li><strong>SEO plugin</strong>: Yoast nebo Rank Math. Jeden stačí, dva se perou. Nastavíte meta titulky, popisy a sitemap.</li>
<li><strong>Search Console</strong>: ověřte web a pošlete sitemap.xml. Google začne vidět vaše stránky.</li>
<li><strong>HTTPS</strong>: vždy. Google měří jako signál kvality.</li>
</ul>

<h2>Krok 2: Rychlost, která Google uspokojí</h2>
<p>WordPress weby bývají pomalé kvůli těžkým šablonám, zbytečným pluginům a neoptimalizovaným obrázkům. Cíl: LCP pod 2,5 s, INP pod 200 ms, CLS pod 0,1. V praxi: jeden cache plugin (WP Rocket nebo LiteSpeed Cache), WebP obrázky, méně pluginů. Měření: <a href="https://pagespeed.web.dev/" target="_blank" rel="noopener noreferrer">PageSpeed Insights</a>, zdarma.</p>

<h2>Krok 3: Obsah na dotazy, které hledají zákazníci</h2>
<p>Blog na WordPress je nejrychlejší cesta k zákazníkům z Google. Pište články na otázky, které si zákazníci kladou před nákupem: "jak vybrat...", "kolik stojí...", "nejlepší X pro Y". Každý článek: jedno cílové klíčové slovo, H2 nadpisy, interní odkaz na službu, 800 až 1500 slov. Dotazy a objemy ověříte přes Marketing Miner (CZ/SK data) nebo zdarma přes autocomplete.</p>

<h2>Krok 4: Měření a udržování</h2>
<p>Měsíčně zkontrolujte: pozice a kliky (Search Console), rychlost (PageSpeed), staré články po roce obnovte. Když nechcete SEO dělat sami, udělám to za vás: 12 EUR za hodinu, retainer od 120 EUR měsíčně pro malý web, 240 až 480 EUR pro web s blogem a e-commerce. Vše vykázané v měsíčním reportu.</p>

<h2>Kolik to stojí v praxi</h2>
<p>Malý web (10 stránek): 10 hodin měsíčně = 120 EUR. Web s blogem (2 články měsíčně + technika): 15 až 20 hodin = 180 až 240 EUR. WooCommerce e-shop: 30 až 40 hodin = 360 až 480 EUR. První hodina je bezplatný hovor a audit, abyste viděli, co by SEO u vás znamenalo.</p>
""",
            "faq": [
                ("Potřebuji platit pluginy?", "Ne. Bezplatný Yoast nebo Rank Math pokrývá meta údaje a sitemap. Placené pluginy (WP Rocket) pomáhají s rychlostí, ale nejsou podmínkou."),
                ("Můžu SEO na WordPress dělat sám?", "Ano. Základy (permalinky, plugin, obsah) zvládne každý. Pozice na konkurenčních dotazech, technika a strategie jsou už práce pro specialistu."),
                ("Jak dlouho trvá, než WordPress SEO funguje?", "První pohyby na méně konkurenčních dotazech za 2 až 4 měsíce. Hlavní dotazy 6 až 12 měsíců. Záleží na konkurenci ve vašem oboru."),
            ],
            "related": [
                ("wordpress-seo-pluginy", "WordPress SEO pluginy: co opravdu potřebujete"),
                ("rychlost-wordpressu", "Rychlost WordPressu: jak zrychlit web pro Google"),
            ],
        },
    },
    "wordpress-seo-pluginy": {
        "slug": "wordpress-seo-pluginy",
        "sk": {
            "label": "Nástroje",
            "h1": "WordPress SEO pluginy: čo naozaj potrebujete (2026)",
            "title": "WordPress SEO pluginy: čo naozaj potrebujete | SEO pre WordPress",
            "desc": "Yoast vs Rank Math vs All in One SEO: ktorý WordPress SEO plugin vybrať, čo nastaviť a prečo plugin sám SEO neurobí. Cena od 120 EUR mesačne.",
            "date_display": "17. 9. 2026",
            "date_iso": "2026-09-17",
            "answer": "Potrebujete presne jeden SEO plugin: Yoast SEO (najrozšírenejší, zdarma) alebo Rank Math (viac funkcií v bezplatnej verzii). Nastavte v ňom meta titulky, meta popisy, XML sitemap a breadcrumbs. Žiadny plugin ale sám SEO neurobí: obsah, rýchlosť a odkazy robí človek, nie plugin.",
            "sections": """
<h2>Yoast vs Rank Math: ktorý vybrať</h2>
<p>Oba fungujú. Yoast má dlhšiu históriu a jednoduchšie rozhranie, Rank Math dáva v bezplatnej verzii viac (schema, 404 monitoring, viac kľúčových slov). Moje odporúčanie: <strong>Rank Math</strong> pre nové weby, <strong>Yoast</strong> ak už máte web na ňom rozbehatý. Prepočet medzi nimi je zbytočná práca.</p>

<h2>Čo v plugine nastaviť (a čo nechať)</h2>
<ul>
<li><strong>Meta titulky a popisy</strong>: ručne pre stránky služieb a hlavné kategórie. Nie automaticky, to dáva rovnaké titulky všade.</li>
<li><strong>XML sitemap</strong>: zapnúť a poslať do Search Console.</li>
<li><strong>Canonical</strong>: nechať zapnuté, plugin to rieši sám.</li>
<li><strong>Schema (štruktúrované dáta)</strong>: zapnúť Organization a WebSite. Article na blogu.</li>
<li><strong>Analysis (oranžové/sivé kolieska)</strong>: ignorovať. Koliesko je len odhad, nie Google. Obsah píšte pre zákazníkov.</li>
</ul>

<h2>Pluginy, ktoré SEO pomáhajú (sekundárne)</h2>
<p>Cache plugin (LiteSpeed Cache, WP Rocket) zrýchľuje web, čo Google meria. Broken link checker odhalí rozbité odkazy. Redirect plugin (Redirection) rieši presmerovania pri zmene URL. Ale pozor: každý ďalší plugin znamená viac kódu a spomalší web. Riešte len to, čo potrebujete.</p>

<h2>Čo plugin nespraví</h2>
<p>Plugin nenapíše obsah, nenastaví interné odkazy, nevyhľadá kľúčové slová a nezíska odkazy. To je 80 percent SEO práce. Plugin je len nástroj, ktorý zabezpečí technické minimum. Ak chcete pozície, potrebujete obsah na reálne dopyty a techniku, ktorá sa rýchlo načítava. Presne to robím v balíkoch od 120 EUR mesačne (12 EUR za hodinu).</p>
""",
            "faq": [
                ("Sú SEO pluginy zdarma dostatočné?", "Áno. Rank Math a Yoast v bezplatnej verzii pokrývajú meta údaje, sitemap aj schema. Platené verrie riešia viac webov alebo e-commerce, pre väčšinu webov nepotrebujete."),
                ("Môžem mať dva SEO pluginy naraz?", "Nie. Dva SEO pluginy sa perú o meta údaje a vytvárajú duplicitné schema. Vyberte jeden."),
                ("Pomôže mi SEO analytický plugin?", "Analýza v plugine (kolieska) je hrubý odhad. Reálne dáta sú v Search Console. Nenechajte sa mýliť zelenými kolieskami."),
            ],
            "related": [
                ("seo-wordpress-navod", "SEO pre WordPress: kompletný návod 2026"),
                ("seo-blog-na-wordpress", "Ako písať blog na WordPress, ktorý Google rád"),
            ],
        },
        "cz": {
            "label": "Nástroje",
            "h1": "WordPress SEO pluginy: co opravdu potřebujete (2026)",
            "title": "WordPress SEO pluginy: co opravdu potřebujete | SEO pro WordPress",
            "desc": "Yoast vs Rank Math vs All in One SEO: který WordPress SEO plugin vybrat, co nastavit a proč plugin sám SEO neudělá. Cena od 120 EUR měsíčně.",
            "date_display": "17. 9. 2026",
            "date_iso": "2026-09-17",
            "answer": "Potřebujete přesně jeden SEO plugin: Yoast (nejrozšířenější) nebo Rank Math (více funkcí zdarma). Nastavte v něm meta titulky, meta popisy, XML sitemap a schema. Žádný plugin ale sám SEO neudělá: obsah, rychlost a odkazy dělá člověk, ne plugin. Cena SEO práce od 120 EUR měsíčně (12 EUR za hodinu).",
            "sections": """
<h2>Yoast vs Rank Math</h2>
<p>Oba fungují. Yoast má delší historii a jednodušší rozhraní, Rank Math dává ve verzi zdarma víc: schema, monitoring 404, více klíčových slov. Moje doporučení: <strong>Rank Math</strong> pro nové weby, <strong>Yoast</strong> když už web běží na něm. Přepínání mezi nimi je zbytečná práce.</p>

<h2>Co v pluginu nastavit</h2>
<ul>
<li><strong>Meta titulky a popisy</strong>: ručně pro stránky služeb a hlavní kategorie. Ne automaticky, to dává stejný text všude.</li>
<li><strong>XML sitemap</strong>: zapnout a poslat do Search Console.</li>
<li><strong>Canonical</strong>: nechat zapnuté, plugin to řeší sám.</li>
<li><strong>Schema</strong>: zapnout Organization a WebSite, na blogu Article.</li>
<li><strong>Analysis (zelená kolečka)</strong>: ignorovat. Kolečko je hrubý odhad, obsah pište pro zákazníky.</li>
</ul>

<h2>Pluginy, které pomáhají vedle SEO pluginu</h2>
<p>Cache plugin (LiteSpeed Cache, WP Rocket) zrychluje web, co Google měří. Redirection řeší přesměrování při změně URL. Broken link checker najde rozbité odkazy. Ale pozor: každý plugin přidává kód a zpomaluje web. Méně pluginů = rychlejší web.</p>

<h2>Co plugin neudělá</h2>
<p>Plugin nenapíše obsah, nenajde klíčová slova a nezíská odkazy. To je práce člověka. Plugin zajistí technické minimum, ale pozice potřebují obsah na reálná hledání a techniku, která se rychle načítá. Přesně to dělám v balíčcích od 120 EUR měsíčně (12 EUR za hodinu).</p>
""",
            "faq": [
                ("Jsou SEO pluginy zdarma dostatečné?", "Ano. Rank Math a Yoast ve verzi zdarma pokrývají meta údaje, sitemap i schema. Placené verze řeší víc webů a e-commerce, pro většinu webů nepotřebujete."),
                ("Můžu mít dva SEO pluginy?", "Ne. Dva SEO pluginy se perou o meta údaje a vytvářejí duplicity. Vyberte jeden."),
                ("Věřit zeleným kolečkům v pluginu?", "Ne. Kolečko je hrubý odhad pluginu. Reálná data jsou ve Search Console."),
            ],
            "related": [
                ("seo-wordpress-navod", "SEO pro WordPress: kompletní návod 2026"),
                ("seo-blog-na-wordpress", "Jak psát blog na WordPress, který Google rád"),
            ],
        },
    },
    "rychlost-wordpressu": {
        "slug": "rychlost-wordpressu",
        "sk": {
            "label": "Technika",
            "h1": "Rýchlosť WordPressu: ako zrýchliť web pre Google (2026)",
            "title": "Rýchlosť WordPressu: ako zrýchliť web pre Google | SEO pre WordPress",
            "desc": "Rýchlosť WordPress webu: LCP pod 2,5s, cache, WebP obrázky a optimalizácia pluginov. Krok za krokom, s reálnymi číslami z praxe.",
            "date_display": "17. 9. 2026",
            "date_iso": "2026-09-17",
            "answer": "Rýchlosť WordPressu riešite v tomto poradí: jeden cache plugin (LiteSpeed Cache zdarma alebo WP Rocket), WebP formát obrázkov, menej pluginov (menej kódu), kvalitný hosting. Cieľ: LCP pod 2,5 sekundy, INP pod 200 ms, CLS pod 0,1 (Core Web Vitals). Pomalý web stráca zákazníkov aj pozície v Google.",
            "sections": """
<h2>Prečo je rýchlosť dôležitá</h2>
<p>Google meria rýchlosť ako signál kvality (Core Web Vitals). Pomalý web má vyšší odchodovú mieru: polovica návštevníkov odchádza, ak sa stránka načítava dlhšie ako 3 sekundy. Na WordPress weboch je rýchlosť navyše problém číslo jedna, lebo šablóny a pluginy pridávajú veľa kódu.</p>

<h2>Meranie: čo a ako merať</h2>
<p>Používajte <a href="https://pagespeed.web.dev/" target="_blank" rel="noopener noreferrer">PageSpeed Insights</a> (bezplatný). Dôležité tri metriky:</p>
<ul>
<li><strong>LCP</strong> (Largest Contentful Paint): čas načítania hlavného obsahu. Cieľ pod 2,5 s.</li>
<li><strong>INP</strong> (Interaction to Next Paint): reakcia na klik. Cieľ pod 200 ms.</li>
<li><strong>CLS</strong> (Cumulative Layout Shift): posúvanie obsahu pri načítaní. Cieľ pod 0,1.</li>
</ul>

<h2>Päť opráv, ktoré najviac posunú rýchlosť</h2>
<ul>
<li><strong>Cache plugin</strong>: LiteSpeed Cache (zdarma) alebo WP Rocket (cca 50 EUR/rok). Rozdiel vidno hneď.</li>
<li><strong>WebP obrázky</strong: konvertujte cez plugin (Imagify, Smush) alebo pred nahraním. Obrázky bývajú najväčším problémom.</li>
<li><strong>Menej pluginov</strong>: každý plugin pridáva CSS a JS. Vypnite a vymažte nepoužívané.</li>
<li><strong>Kvalitný hosting</strong: lacný shared hosting brzdí aj najlepšie optimalizovaný WordPress. Pre podnikanie si spravte upgrade.</li>
<li><strong>Lazy loading</strong: obrázky pod oknom načítavať až pri scrollovaní. WordPress to robí od verzie 5.5 automaticky.</li>
</ul>

<h2>Čo nerobiť (bežné chyby)</h2>
<p>Nesťahujte päť cache pluginov naraz, bojujú navzájom. Neoptimalizujte rýchlosť na úkor funkčnosti (preťažanie AMP, odstránenie všetkých pluginov). A nepresúvajte web na lacnejší hosting, ak problém je v šablóne s 20 pluginmi.</p>

<h2>Koľko rýchlosti stojí</h2>
<p>Základné opravy (cache, obrázky, menej pluginov) zvládnem za 3 až 5 hodín = 36 až 60 EUR. Väčšie zásahy (hosting, šablóna) 8 až 15 hodín = 96 až 180 EUR. Súčasťou mesačného retainera od 120 EUR je aj priebežné sledovanie rýchlosti.</p>
""",
            "faq": [
                ("Aká je ideálna rýchlosť WordPress webu?", "LCP pod 2,5 sekundy, INP pod 200 ms, CLS pod 0,1. Google to meria cez Core Web Vitals a radí rýchlejšie weby výš."),
                ("Pomôže CDN?", "Áno, pre weby s návštevníkmi z viacerých krajín. Pre slovenský web s lokálnym publikom je najprv cache a obrázky, CDN potom."),
                ("Prečo je môj WordPress pomalý, keď mám cache plugin?", "Najčastejšie: ťažká šablóna, veľa pluginov, neoptimalizované obrázky alebo slabý hosting. Cache rieši len jednu vrstvu."),
            ],
            "related": [
                ("seo-wordpress-navod", "SEO pre WordPress: kompletný návod 2026"),
                ("wordpress-seo-pluginy", "WordPress SEO pluginy: čo naozaj potrebujete"),
            ],
        },
        "cz": {
            "label": "Technika",
            "h1": "Rychlost WordPressu: jak zrychlit web pro Google (2026)",
            "title": "Rychlost WordPressu: jak zrychlit web pro Google | SEO pro WordPress",
            "desc": "Rychlost WordPress webu: LCP pod 2,5 sekundy, cache, WebP obrázky a optimalizace pluginů. Krok za krokem, s reálnymi čísly z praxe.",
            "date_display": "17. 9. 2026",
            "date_iso": "2026-09-17",
            "answer": "Rychlost WordPressu řešte v tomto pořadí: jeden cache plugin (LiteSpeed Cache zdarma), WebP formát obrázků, méně pluginů, kvalitní hosting. Cíl: LCP pod 2,5 sekundy, INP pod 200 ms, CLS pod 0,1 (Core Web Vitals). Pomalý web ztrácí zákazníky i pozice v Google.",
            "sections": """
<h2>Proč je rychlost důležitá</h2>
<p>Google měří rychlost jako signál kvality (Core Web Vitals) a pomalé weby řadí níž. Půlka návštěvníků odejde, když se web načítá déle než 3 sekundy. U WordPress webů je rychlost častější problém, protože šablony a pluginy přidávají hodně kódu.</p>

<h2>Měření</h2>
<p>Používejte <a href="https://pagespeed.web.dev/" target="_blank" rel="noopener noreferrer">PageSpeed Insights</a> (zdarma). Tři metriky:</p>
<ul>
<li><strong>LCP</strong>: čas načtení hlavního obsahu. Cíl pod 2,5 s.</li>
<li><strong>INP</strong>: reakce na klik. Cíl pod 200 ms.</li>
<li><strong>CLS</strong>: posouvání obsahu při načítání. Cíl pod 0,1.</li>
</ul>

<h2>Pět oprav, které nejvíc posunou rychlost</h2>
<ul>
<li><strong>Cache plugin</strong>: LiteSpeed Cache (zdarma) nebo WP Rocket. Rozdíl vidíte okamžitě.</li>
<li><strong>WebP obrázky</strong>: konvertujte přes plugin (Imagify, Smush). Obrázky bývají hlavní problém.</li>
<li><strong>Méně pluginů</strong>: každý plugin přidává CSS a JS. Vypněte nepoužívané.</li>
<li><strong>Kvalitní hosting</strong>: lacný hosting brzdí i nejrychlejší WordPress.</li>
<li><strong>Lazy loading</strong>: obrázky pod oknem načítat při scrollu. WordPress to umí od verze 5.5.</li>
</ul>

<h2>Čo nedělat</h2>
<p>Nepoužívejte pět cache pluginů najednou, bojují mezi sebou. Neoptimalizujte rychlost za cenu funkce webu. A měňte hosting jen tehdy, když víte, že hosting je problém, ne šablona.</p>

<h2>Kolik to stojí</h2>
<p>Základní opravy (cache, obrázky, méně pluginů) zvládnu za 3 až 5 hodin = 36 až 60 EUR. Větší zásahy (hosting, šablona) 8 až 15 hodin = 96 až 180 EUR. Součástí měsíčního retaineru od 120 EUR je i průběžné sledování rychlosti.</p>
""",
            "faq": [
                ("Jaká je ideální rychlost WordPress webu?", "LCP pod 2,5 sekundy, INP pod 200 ms, CLS pod 0,1. Google měří Core Web Vitals a rychlejší weby řadí výš."),
                ("Pomůže CDN?", "Ano, pro weby s návštěvníky z více zemí. Pro český web s lokálním publikem je první cache a obrázky."),
                ("Proč je můj WordPress pomalý, když mám cache?", "Nejčastěji: těžká šablona, mnoho pluginů, neoptimalizované obrázky nebo slabý hosting. Cache řeší jen jednu vrstvu."),
            ],
            "related": [
                ("seo-wordpress-navod", "SEO pro WordPress: kompletní návod 2026"),
                ("wordpress-seo-pluginy", "WordPress SEO pluginy: co opravdu potřebujete"),
            ],
        },
    },
    "seo-blog-na-wordpress": {
        "slug": "seo-blog-na-wordpress",
        "sk": {
            "label": "Obsah",
            "h1": "Ako písať blog na WordPress, ktorý Google aj zákazníci čítajú",
            "title": "Ako písať blog na WordPress pre Google | SEO pre WordPress",
            "desc": "Blog na WordPress krok za krokom: výber tém podľa dopytov, štruktúra článku, interné odkazy. Od 120 EUR mesačne s obsahom v cene.",
            "date_display": "17. 9. 2026",
            "date_iso": "2026-09-17",
            "answer": "Blog, ktorý Google rád, odpovedá na otázky, ktoré zákazníci reálne hľadajú. Štruktúra: jedno hlavné kľúčové slovo, H2 nadpisy podľa otázok, odpoveď v prvých 50 slovach, interné odkazy na služby. Dĺžka: 800 až 1500 slov. Frekvencia: 2 až 4 články mesačne stavia autoritu rýchlejšie, než jeden článok mesačne.",
            "sections": """
<h2>Najprv témy, nie písanie</h2>
<p>Najčastejšia chyba: firma píše o sebe, nie o tom, čo zákazníci hľadajú. Témy hľadajte cez autocomplete v Google (začnite písať hlavné slovo a pozrite doplnky) a cez Marketing Miner (objemy na SK/CZ). Každý článok = jedno hlavné kľúčové slovo s objemom minimálne 10 vyhľadaní mesačne.</p>

<h2>Štruktúra článku, ktorý Google rád</h2>
<ul>
<li><strong>Nadpis</strong>: hlavné kľúčové slovo na začiatku, dĺžka do 60 znakov.</li>
<li><strong>Úvod (50 slov)</strong>: odpoveď na otázku hneď. Google to cituje, zákazník to dočíta.</li>
<li><strong>H2 nadpisy</strong>: jednotlivé podotázky. Ideálne vo forme, v akej ľudia hľadajú ("ako...", "koľko...", "čo je...").</li>
<li><strong>Odstavce</strong>: krátke, 3 až 4 riadky. Nie steny textu.</li>
<li><strong>Interné odkazy</strong>: z článku na službu a na ďalšie články. To je to, čo posúva celý web.</li>
<li><strong>Záver + CTA</strong>: čo má čitateľ urobiť ďalej.</li>
</ul>

<h2>Ako často publikovať</h2>
<p>Pravidelnosť prekoná objem. Dva články mesačne, každý na plánované kľúčové slovo, stavia autoritu systémovo. Desať článkov naraz a potom ticho Google neodmení. Pri mojej spolupráci obsahuje retainer od 180 EUR mesačne 2 až 4 články na WordPress priamo s vložením, meta údajmi a internými odkazmi.</p>

<h2>Staré články sú zlato</h2>
<p>Článok po 12 mesiacoch obnovte: aktualizujte čísla, pridajte nové informácie, skontrolujte odkazy. Google rád re-indexuje obnovený obsah a často posunie vyššie. Obnova býva účinnejšia než nový článok, lebo stránka už má históriu v Google.</p>
""",
            "faq": [
                ("Koľko slov má mať blogový článok?", "Dĺžku určuje téma a konkurencia. Typicky 800 až 1500 slov. Kvalita a pokrytie otázok zákazníkov rozhoduje viac než počet slov."),
                ("Ako často publikovať na blogu?", "2 až 4 články mesačne je dobrý rytmus. Dôležitejšia je pravidelnosť a plán kľúčových slov než objem."),
                ("Robí mi blog aj texty?", "Áno. Píšem články priamo do WordPressu s meta údajmi, nadpismi a internými odkazmi. Vy len schvaľujete a publikujete. Od 180 EUR mesačne v retaineri."),
            ],
            "related": [
                ("seo-wordpress-navod", "SEO pre WordPress: kompletný návod 2026"),
                ("rychlost-wordpressu", "Rýchlosť WordPressu: ako zrýchliť web pre Google"),
            ],
        },
        "cz": {
            "label": "Obsah",
            "h1": "Jak psát blog na WordPress, který Google i zákazníci čtou",
            "title": "Jak psát blog na WordPress pro Google | SEO pro WordPress",
            "desc": "Blog na WordPress krok za krokem: výběr témat, struktura článku, interní odkazy. Od 120 EUR měsíčně s obsahem v ceně.",
            "date_display": "17. 9. 2026",
            "date_iso": "2026-09-17",
            "answer": "Blog, který Google rád, odpovídá na otázky, které zákazníci reálně hledají. Struktura: jedno hlavní klíčové slovo, H2 nadpisy podle otázek, odpověď v prvních 50 slovech, interní odkazy na služby. Délka: 800 až 1500 slov. Frekvence: 2 až 4 články měsíčně stávají autoritu systémově.",
            "sections": """
<h2>Nejdřív témata, potom psaní</h2>
<p>Nejčastější chyba: psaní bez plánu. Témata hledejte přes autocomplete v Google a přes Marketing Miner (objemy na CZ/SK). Každý článek = jedno hlavní klíčové slovo s objemem minimálně 10 hledání měsíčně.</p>

<h2>Struktura článku, který Google rád</h2>
<ul>
<li><strong>Nadpis</strong>: hlavní klíčové slovo na začátku, délka do 60 znaků.</li>
<li><strong>Úvod (50 slov)</strong>: odpověď hned. Google ji cituje, zákazník dočte.</li>
<li><strong>H2 nadpisy</strong>: jednotlivé podotázky ve formě, jakou lidé hledají ("jak...", "kolik...", "co je...").</li>
<li><strong>Odstavce</strong>: krátké, 3 až 4 řádky. Žádné zdi textu.</li>
<li><strong>Interní odkazy</strong>: z článku na služby a další články. To posouvá celý web.</li>
<li><strong>Závěr + CTA</strong>: co má čtenář udělat dál.</li>
</ul>

<h2>Jak často publikovat</h2>
<p>Pravidelnost překoná objem. Dva články měsíčně, každý na plánované klíčové slovo, staví autoritu systémově. Retainer od 180 EUR měsíčně obsahuje 2 až 4 články s meta údaji a interními odkazy, vložené přímo do WordPressu.</p>

<h2>Staré články jsou zlato</h2>
<p>Článek po 12 měsících obnovte: aktualizujte čísla, přidejte nové informace. Google rád re-indexuje obnovený obsah a často ho posune výš. Obnova bývá efektivnější než nový článek, protože stránka už má historii.</p>
""",
            "faq": [
                ("Kolik slov má mít článek?", "Typicky 800 až 1500 slov. Délku určuje téma a konkurence, kvalita a pokrytí dotazů rozhoduje víc než počet slov."),
                ("Jak často publikovat?", "2 až 4 články měsíčně. Pravidelnost a plán klíčových slov důležitější než objem."),
                ("Píšete mi i články?", "Ano. Píšu články přímo do WordPressu s meta údaji a interními odkazy. Vy jen schvalujete. Od 180 EUR měsíčně v retaineru."),
            ],
            "related": [
                ("seo-wordpress-navod", "SEO pro WordPress: kompletní návod 2026"),
                ("rychlost-wordpressu", "Rychlost WordPressu: jak zrychlit web pro Google"),
            ],
        },
    },
}
