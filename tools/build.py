"""Build the brochure landing pages from brochures.json into an output folder.

Usage: python tools/build.py _site
The PDFs themselves are downloaded into <out>/pdf/ by tools/fetch_pdfs.sh (run in GitHub Actions).
"""
import html, json, os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "_site"))
cfg = json.load(open(os.path.join(ROOT, "brochures.json"), encoding="utf-8"))
SITE = cfg["site"]
LOGO_REMOTE = "https://www.lykomitros-steel.gr/wp-content/uploads/2026/11/cropped-ls-logo-Png-High-Resolution_2-300x266.png"
PDFJS = "../assets/pdfjs/pdf.min.js"
e = html.escape

FOOT_LINKS = [
    ("Home", SITE), ("Projects", SITE + "projects/"), ("Certifications", SITE + "certifications/"),
    ("Downloads", SITE + "downloads/"), ("Contact", SITE + "contact-us/"),
    ("LinkedIn", "https://www.linkedin.com/company/lykomitros-steel-s-a-"),
]


def head(title, desc, prefix):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{LOGO_REMOTE}">
<link rel="icon" href="https://www.lykomitros-steel.gr/wp-content/uploads/2026/11/cropped-LykomitrosSteel-Logo-Redrawn-212x212-1-32x32.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Rubik:wght@600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
<header class="top"><div class="in">
  <a class="brand" href="{SITE}"><img src="{prefix}assets/logo.png" onerror="this.onerror=null;this.src='{LOGO_REMOTE}'" alt="Lykomitros Steel logo"><span>LYKOMITROS STEEL</span></a>
  <a class="btn btn-primary" href="{SITE}"><span class="label">Visit</span>&nbsp;lykomitros-steel.gr</a>
</div></header>
"""


def foot():
    links = "".join(f'<a href="{u}">{e(t)}</a>' for t, u in FOOT_LINKS)
    return f"""<footer><div class="in">
  <div>&copy; Lykomitros Steel S.A. &middot; <a href="mailto:info@lykomitros-steel.gr">info@lykomitros-steel.gr</a> &middot; <a href="tel:+302421096739">+30 24210 96739</a></div>
  <nav>{links}</nav>
</div></footer>
</body>
</html>
"""


def others(cur):
    items = "".join(
        f'<a href="../{b["slug"]}/">{e(b["title"])}<small>PDF brochure</small></a>'
        for b in cfg["brochures"] if b["slug"] != cur)
    return f'<section class="more"><h3>More brochures</h3><div class="grid">{items}</div></section>'


def cta():
    return f"""<section class="cta"><div class="box">
  <div><h2>Discuss your next project with us</h2><p>Explore our projects, certifications and facilities on our website.</p></div>
  <div class="actions"><a class="btn btn-primary" href="{SITE}">Visit lykomitros-steel.gr</a><a class="btn btn-outline" href="{SITE}contact-us/">Contact us</a></div>
</div></section>
"""


def page(b):
    original = cfg["base_pdf_url"] + b["pdf"]
    title = f'{b["title"]} | Lykomitros Steel'
    rel_t, rel_u = b["related"]
    return head(title, b["lead"], "../") + f"""<main>
<section class="hero">
  <p class="kicker">Brochure</p>
  <h1>{e(b["title"])}</h1>
  <p>{e(b["lead"])}</p>
  <div class="actions">
    <a class="btn btn-primary" href="{SITE}">Visit lykomitros-steel.gr</a>
    <a class="btn btn-outline" href="{original}" target="_blank" rel="noopener">Download PDF</a>
    <a class="btn btn-outline" href="{rel_u}">{e(rel_t)} on our website</a>
  </div>
</section>
<section class="viewer"><div class="pages" id="pages" data-pdf="../pdf/{b["slug"]}.pdf" data-original="{original}"><div class="status">Loading brochure&hellip;</div></div></section>
{cta()}{others(b["slug"])}
</main>
<script src="{PDFJS}"></script>
<script src="../assets/viewer.js"></script>
""" + foot()


def index():
    items = "".join(
        f'<a href="{b["slug"]}/">{e(b["title"])}<small>{e(b["lead"])}</small></a>' for b in cfg["brochures"])
    return head("Brochures | Lykomitros Steel", "Lykomitros Steel brochures.", "") + f"""<main>
<section class="hero"><p class="kicker">Downloads</p><h1>Lykomitros Steel brochures</h1>
<p>Heavy steel structures and fabrication. Choose a brochure to view it online.</p>
<div class="actions"><a class="btn btn-primary" href="{SITE}">Visit lykomitros-steel.gr</a></div></section>
<section class="more"><div class="grid">{items}</div></section>
{cta()}</main>
""" + foot()


os.makedirs(OUT, exist_ok=True)
shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"), dirs_exist_ok=True)
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(index())
for b in cfg["brochures"]:
    d = os.path.join(OUT, b["slug"])
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(page(b))
open(os.path.join(OUT, ".nojekyll"), "w").close()
print("built", len(cfg["brochures"]), "pages into", OUT)
