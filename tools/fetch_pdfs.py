"""Download the current brochure PDFs and logo from lykomitros-steel.gr into <out>/pdf and <out>/assets."""
import json, os, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "_site"))
cfg = json.load(open(os.path.join(ROOT, "brochures.json"), encoding="utf-8"))
UA = {"User-Agent": "Mozilla/5.0 (brochure-pages build)"}


def get(url, dest):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
        f.write(r.read())
    print(f"{os.path.getsize(dest)/1e6:6.1f} MB  {url}")


os.makedirs(os.path.join(OUT, "pdf"), exist_ok=True)
os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
failed = []
for b in cfg["brochures"]:
    try:
        get(cfg["base_pdf_url"] + b["pdf"], os.path.join(OUT, "pdf", b["slug"] + ".pdf"))
    except Exception as ex:  # page falls back to the direct link if a PDF is missing
        failed.append(b["pdf"]); print("FAILED", b["pdf"], ex)
try:
    get("https://www.lykomitros-steel.gr/wp-content/uploads/2026/11/cropped-ls-logo-Png-High-Resolution_2-300x266.png",
        os.path.join(OUT, "assets", "logo.png"))
except Exception as ex:
    print("logo FAILED", ex)
if len(failed) == len(cfg["brochures"]):
    sys.exit("No PDF could be downloaded")
