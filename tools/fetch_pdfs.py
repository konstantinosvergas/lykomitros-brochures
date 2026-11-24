"""Put the brochure PDFs into <out>/pdf/<slug>.pdf.

Source of truth: the repo folder pdf/<slug>.pdf, uploaded from the local folder next to the Excel
file by the macro button. If a brochure has no file there yet, the current PDF from
lykomitros-steel.gr is used instead, so every page always has a PDF.
"""
import json, os, shutil, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "_site"))
cfg = json.load(open(os.path.join(ROOT, "brochures.json"), encoding="utf-8"))
UA = {"User-Agent": "Mozilla/5.0 (brochure-pages build)"}


def get(url, dest):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
        f.write(r.read())


os.makedirs(os.path.join(OUT, "pdf"), exist_ok=True)
os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
missing = []
for b in cfg["brochures"]:
    local = os.path.join(ROOT, "pdf", b["slug"] + ".pdf")
    dest = os.path.join(OUT, "pdf", b["slug"] + ".pdf")
    try:
        if os.path.isfile(local):
            shutil.copyfile(local, dest); src = "repo pdf/"
        else:
            get(cfg["base_pdf_url"] + b["pdf"], dest); src = "lykomitros-steel.gr (fallback)"
        print(f"{os.path.getsize(dest)/1e6:6.1f} MB  {b['slug']:34s} from {src}")
    except Exception as ex:
        missing.append(b["slug"]); print("FAILED", b["slug"], ex)
try:
    get("https://www.lykomitros-steel.gr/wp-content/uploads/2026/11/cropped-ls-logo-Png-High-Resolution_2-300x266.png",
        os.path.join(OUT, "assets", "logo.png"))
except Exception as ex:
    print("logo FAILED", ex)
if len(missing) == len(cfg["brochures"]):
    sys.exit("No PDF available")
