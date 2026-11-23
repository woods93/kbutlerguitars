#!/usr/bin/env python3
"""
Build the K. Butler Guitars static site.

    python3 build.py            -> writes index.html, about.html, guitars.html, contact.html, shop.html

PHOTOS: during preview the photos are loaded from the old site (kbutlerguitars.com) so we have
something to look at. Before going live, download the originals into ./img/ and set
USE_LOCAL_IMAGES = True, then rebuild. After DNS moves, the old links will stop working.
"""
import html
import os

USE_LOCAL_IMAGES = True
REMOTE_BASE = "https://kbutlerguitars.com/wp-content/uploads/"
LOCAL_BASE = "img/"

# Merch store (Fourthwall). Product photos are saved locally in img/.
SHOP_URL = "https://k-butler-guitars-shop.fourthwall.com"
TEE_IMG = "img/kbg-tee-front.jpg?v=2"

# Web3Forms access key (public by design; routes messages to the inbox it was created for)
WEB3FORMS_KEY = "912befac-b5f5-4486-b030-b5361d0c4362"

PHONE = "615-815-5119"
PHONE_LINK = "tel:+16158155119"
EMAIL = "kbutler@kbutlerguitars.com"
INSTAGRAM = "https://www.instagram.com/k.butlerguitars"

# filename -> path under /wp-content/uploads/ on the old site
SRC = {
    "k-butler-guitars-logo-w1x.png": "2023/07/",
    "k-butler-guitars-logo-w2x.png": "2023/07/",
    "k-butler-guitars-logo-bronze-600.png": "2023/07/",
    "kbutlerguitars-hero-1.jpg": "2015/02/",
    "red-guitar-hero.jpg": "2015/02/",
    "KellyButler-8547.jpg": "2023/08/",
    "k-butler-guitars-4-Final-Web.jpg": "2023/07/",
}
for n in list(range(1, 18)):
    SRC[f"k-butler-guitars-{n:02d}.jpg"] = "2023/07/"
for n in range(1, 8):
    SRC[f"k-butler-guitars-cheetah-{n:02d}.jpg"] = "2025/01/"
for n in range(1, 9):
    SRC[f"MSPP5-{n:02d}.jpg"] = "2024/02/"
for n in range(1, 8):
    SRC[f"wrangler-{n}.jpg"] = "2026/09/"
SRC_FULL_NAME = {"KellyButler-8595.jpg": "2023/08/KellyButler-8595-924x1024.jpg"}


def img(name):
    if USE_LOCAL_IMAGES:
        return LOCAL_BASE + name
    if name in SRC_FULL_NAME:
        return REMOTE_BASE + SRC_FULL_NAME[name]
    return REMOTE_BASE + SRC[name] + name


def esc(s):
    return html.escape(s, quote=True)


NAV = [("index.html", "Home"), ("about.html", "About"), ("guitars.html", "Guitars"),
       ("shop.html", "Shop"), ("family.html", "Family"), ("contact.html", "Contact")]


def page(filename, title, description, body, bodyclass=""):
    nav = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if href == filename else ""}>{label}</a></li>'
        for href, label in NAV)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;500;600&family=Barlow:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v=fam1">
</head>
<body class="{bodyclass}">
<a class="skip" href="#content">Skip to content</a>
<header class="side">
  <a class="logo" href="index.html"><img src="{img('k-butler-guitars-logo-w2x.png')}" alt="K. Butler Guitars"></a>
  <button class="menu-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav id="nav" aria-label="Main"><ul>{nav}</ul>
    <a class="ig" href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="K. Butler Guitars on Instagram">Instagram</a>
  </nav>
</header>
<main id="content">
{body}
<footer class="foot">
  <img src="{img('k-butler-guitars-logo-bronze-600.png')}" alt="" class="foot-logo">
  <p><a href="{PHONE_LINK}">{PHONE}</a> &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <p class="small">&copy; 2022&ndash;2026 K. Butler Guitars. Special guitars and basses, made in Tennessee.</p>
</footer>
</main>
<div class="lightbox" hidden><button class="lb-close" aria-label="Close">&times;</button><img alt=""></div>
<script src="js/site.js"></script>
</body>
</html>
"""


# ---------- content ----------
GUITARS = [
    dict(id="64", name="The ’64", status="Available locally at Caldwell Music",
         text="The ’64 single pickup version is the worlds greatest single pickup guitar. Maple neck, pau ferro fretboard, and one badass Ultra Clarifier humbucker. Loud enough to rage against whatever. Comes preloaded with over 300 Ramones songs. Finally you can unleash you teenage angst at the talent show with excellent tone and be judged by your peers at the same time! (Ramones songs not included)",
         imgs=["k-butler-guitars-06.jpg", "k-butler-guitars-08.jpg", "k-butler-guitars-07.jpg"]),
    dict(id="64v2", name="The ’64 V2", status="", text="",
         imgs=["k-butler-guitars-10.jpg", "k-butler-guitars-11.jpg", "k-butler-guitars-09.jpg"]),
    dict(id="cheetah", name="Cheetah Chrome Signature ’64", status="Currently taking orders.",
         text="Punk rock OG legend Cheetah Chrome of The Dead Boys is seen here with his signature CC ’64. The Dead Boys storied history began in the ’70s when punk rock was new, raw and rebellious. The title of their first record, “Young, Loud and Snotty,” could not have been more true to its name. The Dead Boys are killing it in front of sold-out venues all over the world again, and this guitar is keeping it loud and snotty night after night.\nAs a long-time fan since I was a teen, I couldn’t be more proud. You can also see one of these guitars on display at the Punk Rock Museum in Vegas.\nPics credit @charlie.glam",
         imgs=["k-butler-guitars-cheetah-06.jpg", "k-butler-guitars-cheetah-04.jpg", "k-butler-guitars-cheetah-07.jpg",
               "k-butler-guitars-cheetah-02.jpg", "k-butler-guitars-cheetah-01.jpg", "k-butler-guitars-cheetah-03.jpg",
               "k-butler-guitars-cheetah-05.jpg"]),
    dict(id="shark", name="The Shark Guitar", status="Available locally at Caldwell Music",
         text="Sporting a light weight baked Ash offset body with a flame maple neck and a pau ferro fretboard the Shark has a range from clean surf all the way to freakin’ KILLAAAAA. Available with swinging singles or humbuckers or both. Can clean up and twang or be as dirty as you wanna be.",
         imgs=["k-butler-guitars-03.jpg", "k-butler-guitars-14.jpg", "k-butler-guitars-05.jpg"]),
    dict(id="sharkbass", name="The Shark Bass", status="",
         text="The shark bass is a rock bass from one end to the other. J-style nut width on a maple neck, and equipped with the world famous DuoMag bass humbuckers. Now you can stand out in the crowd of same old same olds. You don’t have to play the same bass your grandfather played",
         imgs=["k-butler-guitars-13.jpg", "k-butler-guitars-12.jpg", "k-butler-guitars-15.jpg"]),
    dict(id="mspp5", name="The MSPP5", status="$2,500",
         text="Signature guitars of amazing guitar Nashville Guitar God, Mike Simmons. Equipped with a super fast, slim flame maple neck carved to Mikes specs, and original Floyd Rose bridge, and full humbucker in the bridge position and a bladed single coil sized humbucker in the neck position. Light weight Alder body carved for super comfortable high fret access. Shred like you mean it and come with the melody.",
         imgs=["MSPP5-04.jpg", "MSPP5-02.jpg", "MSPP5-01.jpg", "MSPP5-03.jpg", "MSPP5-06.jpg", "MSPP5-05.jpg",
               "MSPP5-07.jpg", "MSPP5-08.jpg", "k-butler-guitars-04.jpg", "k-butler-guitars-16.jpg",
               "k-butler-guitars-17.jpg"]),
    dict(id="wrangler", name="The Wrangler", status="",
         text="Ash body, maple neck, Hipshot open gear tuners, DiMarzio “Muscle T” pickups.",
         imgs=["wrangler-1.jpg", "wrangler-2.jpg", "wrangler-3.jpg", "wrangler-4.jpg", "wrangler-5.jpg",
               "wrangler-7.jpg", "wrangler-6.jpg"]),
]

TILES = [("64v2", "The ’64 V2", "k-butler-guitars-09.jpg"), ("shark", "The Shark Guitar", "k-butler-guitars-03.jpg"),
         ("mspp5", "The MSPP5", "k-butler-guitars-04.jpg"), ("cheetah", "The Cheetah", "k-butler-guitars-cheetah-02.jpg"),
         ("wrangler", "The Wrangler", "wrangler-6.jpg")]

INTRO = ("K. Butler, a name synonymous with unparalleled artistry and precision in the world of guitar making. "
         "With over three decades of experience, K. Butler has become a revered figure among musicians and collectors alike. "
         "Born with an innate passion for music and a natural talent for craftsmanship, K. Butler embarked on a journey to "
         "redefine the boundaries of custom electric guitar creation.")

ABOUT = [
    INTRO,
    "From a young age, K. Butler exhibited an unwavering dedication to mastering the intricate art of luthiery. Studying under renowned mentors and immersing himself in the rich heritage of guitar making, K. Butler honed his skills and developed a deep understanding of the harmonious interplay between design, materials, and sound.",
    "A true perfectionist at heart, K. Butler approaches each guitar as a unique masterpiece, meticulously handcrafting every detail to ensure unparalleled playability, tone, and aesthetics. His commitment to excellence is evident in the flawless finishes, exquisite fretwork, and precise electronics that grace each instrument bearing the K. Butler signature.",
    "Beyond his technical prowess, K. Butler possesses an intuitive ability to connect with musicians on a profound level. Each guitar becomes an extension of its player’s identity, an instrument that inspires and empowers them to explore new musical frontiers.",
    "As a master guitar craftsman, K. Butler has earned a reputation for pushing boundaries and embracing innovation. Continually exploring new techniques, materials, and technologies, he infuses his guitars with a perfect blend of tradition and modernity, blending timeless craftsmanship with cutting-edge advancements.",
    "Today, K. Butler’s creations grace the hands of discerning musicians across the globe, from passionate amateurs to world-renowned artists. Their guitars have become prized possessions, treasured for their extraordinary tone, exceptional playability, and breathtaking beauty.",
    "With every stroke of the chisel and every note that resonates through his instruments, K. Butler continues to redefine what is possible in the realm of custom electric guitars. His unwavering commitment to excellence, relentless pursuit of perfection, and deep love for music ensure that the legacy of K. Butler will resonate through generations of musicians to come.",
]
MISSION = ("At K. Butler Guitars, our mission is to craft exceptional custom electric guitars that inspire musicians and elevate their artistry to new heights. We are dedicated to pushing the boundaries of traditional guitar making, blending meticulous craftsmanship with innovative design and cutting-edge technology. Our commitment to excellence drives us to create instruments that deliver impeccable playability, unparalleled tone, and timeless beauty. With a deep understanding of musicians’ aspirations, we strive to create a harmonious connection between player and instrument, empowering artists to unleash their creativity and express their unique musical voice. At K. Butler Guitars, we are passionate about shaping the future of guitar making, one masterpiece at a time.")


def paras(text):
    return "".join(f"<p>{esc(p)}</p>" for p in text.split("\n") if p.strip())


def build_home():
    tiles = "".join(
        f'<a class="tile" href="guitars.html#{gid}"><img loading="lazy" src="{img(f)}" alt="{esc(n)}"><span class="tile-name">{esc(n)}</span><span class="tile-sub">K. Butler Guitars</span></a>'
        for gid, n, f in TILES)
    return f"""
<section class="hero" style="background-image:url('{img('kbutlerguitars-hero-1.jpg')}')">
  <div class="hero-text">
    <h1>K. Butler Guitars</h1>
    <p class="tag">Unleash your sound, crafted to perfection</p>
  </div>
</section>
<section class="band intro">
  <div class="intro-photos">
    <img src="{img('KellyButler-8547.jpg')}" alt="Kelly Butler in the shop" loading="lazy">
    <img src="{img('k-butler-guitars-02.jpg')}" alt="A K. Butler guitar" loading="lazy">
    <img src="{img('k-butler-guitars-01.jpg')}" alt="A K. Butler guitar" loading="lazy">
  </div>
  <div class="intro-copy"><p>{esc(INTRO)}</p><p><a class="btn" href="about.html">About</a></p></div>
</section>
<section class="tiles" aria-label="Featured guitars">{tiles}</section>
<section class="band cta"><a class="btn" href="guitars.html">Guitars</a> <a class="btn alt" href="shop.html">Shop</a></section>
"""


def build_about():
    body = "".join(f"<p>{esc(p)}</p>" for p in ABOUT)
    return f"""
<article class="prose">
  <h1>K. Butler Guitars</h1>
  <p class="tag">Unleash your sound, crafted to perfection</p>
  <div class="two-col">
    <div>{body}</div>
    <div class="side-photos">
      <img src="{img('k-butler-guitars-4-Final-Web.jpg')}" alt="K. Butler Guitars – The ’64 V2" loading="lazy">
      <img src="{img('KellyButler-8595.jpg')}" alt="Kelly Butler" loading="lazy">
    </div>
  </div>
  <h2>Mission</h2>
  <p class="tag">Shaping the future of guitar making, one masterpiece at a time.</p>
  <p>{esc(MISSION)}</p>
</article>
"""


def build_guitars():
    out = ['<article class="prose wide"><h1>Guitars</h1>']
    for g in GUITARS:
        gallery = "".join(
            f'<button class="shot" data-full="{img(f)}" aria-label="View larger: {esc(g["name"])}"><img loading="lazy" src="{img(f)}" alt="{esc(g["name"])} – K. Butler Guitars"></button>'
            for f in g["imgs"])
        status = f'<p class="status">{esc(g["status"])}</p>' if g["status"] else ""
        out.append(f'<section class="guitar" id="{g["id"]}"><h2>{esc(g["name"])}</h2>{paras(g["text"])}{status}<div class="gallery">{gallery}</div></section>')
    out.append("</article>")
    return "\n".join(out)


def build_contact():
    return f"""
<article class="prose">
  <h1>Get in touch</h1>
  <p class="tag">Have questions? We’ll be happy to answer!</p>
  <p>Thank you for your interest in K. Butler Guitars. We are thrilled to connect with fellow musicians and enthusiasts. Whether you have questions about our custom electric guitars, wish to explore bespoke instrument options, or simply want to discuss the art of luthiery, we welcome your inquiries with open arms.</p>
  <p class="contact-lines"><a href="{PHONE_LINK}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <form id="contact-form" class="form" action="https://api.web3forms.com/submit" method="POST">
    <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
    <input type="hidden" name="subject" value="New message from the K. Butler Guitars website">
    <input type="hidden" name="from_name" value="K. Butler Guitars website">
    <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
    <label>Name<input name="name" required autocomplete="name"></label>
    <label>Email<input type="email" name="email" required autocomplete="email"></label>
    <label>Message<textarea name="message" rows="6" required></textarea></label>
    <button class="btn" type="submit">Send</button>
    <p class="form-status" role="status" aria-live="polite"></p>
  </form>
  <div class="side-photos row"><img src="{img('k-butler-guitars-11.jpg')}" alt="The ’64 V2" loading="lazy"><img src="{img('k-butler-guitars-15.jpg')}" alt="Shark Bass" loading="lazy"></div>
</article>
"""


def build_shop():
    return f"""
<article class="prose">
  <h1>Shop</h1>
  <p class="tag">Shirts and gear – coming soon</p>
  <p>The K. Butler Guitars merch store is on its way: T-shirts and other gear, printed and shipped on demand. Check back soon, or drop a line and we’ll let you know when it opens.</p>
  <p><a class="btn" href="mailto:{EMAIL}?subject=Tell%20me%20when%20the%20shop%20opens">Tell me when it opens</a></p>
  <div class="products">
    <a class="product" href="{SHOP_URL}/products/k-butler-guitars-logo-tee">
      <img src="{TEE_IMG}" alt="K. Butler Guitars Logo Tee, black with bronze logo" loading="lazy">
      <span class="product-name">K. Butler Guitars Logo Tee</span>
      <span class="product-price">$30</span>
      <span class="product-note">Preview: the store link goes live at launch</span>
    </a>
    <div class="ph" aria-hidden="true">Hoodie<br><small>coming soon</small></div>
    <div class="ph" aria-hidden="true">Stickers<br><small>coming soon</small></div>
  </div>
  <p class="small">Looking for a guitar? See the <a href="guitars.html">Guitars</a> page.</p>
</article>
"""


SITE_ID = "k-butler-guitars"


def build_family():
    """Family page: cards for the other family sites, read from family.json."""
    import json
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "family.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    cards = []
    for f in data:
        if f["id"] == SITE_ID:
            continue
        pic = ('<a class="fam-pic" href="%s" rel="noopener"><img src="%s" alt="%s" loading="lazy" '
               'referrerpolicy="no-referrer" onerror="this.parentNode.remove()"></a>'
               % (esc(f["url"]), esc(f["image"]), esc(f["name"]))) if f.get("image") else ""
        cards.append('<article class="fam-card">%s<h3><a href="%s" rel="noopener">%s</a></h3><p>%s</p></article>'
                     % (pic, esc(f["url"]), esc(f["name"]), esc(f.get("blurb", ""))))
    return '''<article class="prose">
  <h1>Family</h1>
  <p class="lede">The artists and makers we have built websites for.</p>
  <div class="fam-grid">%s</div>
</article>''' % "".join(cards)


PAGES = [
    ("index.html", "K. Butler Guitars – Special guitars and basses made in Tennessee",
     "K. Butler Guitars: custom electric guitars and basses handmade in Tennessee by a luthier with over three decades of experience.",
     build_home, "home"),
    ("about.html", "About – K. Butler Guitars", "About K. Butler, luthier and maker of custom electric guitars and basses in Tennessee.", build_about, ""),
    ("guitars.html", "Guitars – K. Butler Guitars", "The ’64, ’64 V2, Cheetah Chrome Signature, Shark Guitar, Shark Bass, MSPP5 and Wrangler – handmade by K. Butler Guitars.", build_guitars, ""),
    ("shop.html", "Shop – K. Butler Guitars", "K. Butler Guitars merch: T-shirts and gear, coming soon.", build_shop, ""),
    ("family.html", "Family – K. Butler Guitars", "The artists and makers K. Butler Guitars shares a family with.", build_family, ""),
    ("contact.html", "Contact – K. Butler Guitars", "Contact K. Butler Guitars about custom electric guitars and basses.", build_contact, ""),
]

if __name__ == "__main__":
    for fname, title, desc, fn, cls in PAGES:
        with open(fname, "w", encoding="utf-8") as f:
            f.write(page(fname, title, desc, fn(), cls))
        print("wrote", fname)
