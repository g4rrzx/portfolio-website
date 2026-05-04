# /usr/bin/env python3

import os
import shutil
import subprocess
import sys
from threading import Thread
from glob import glob


def is_img(fname: str):
    ext = os.path.splitext(fname)[1].lower()
    return ext in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"]


def optimized_name(fname: str):
    return fname + ".webp"


def optimize_image(fname: str):
    outname = optimized_name(fname)
    subprocess.run(["cwebp", "-q", "80", fname, "-o", outname, "-quiet"], check=True)

    os.remove(fname)

    print(f"Optimized {fname}")


CWEBP_AVAILABLE = shutil.which("cwebp") is not None

if not CWEBP_AVAILABLE:
    print(
        "optimize_images: 'cwebp' not found on PATH — skipping webp conversion "
        "and HTML rewrite. Install libwebp (e.g. `apt install webp`) to enable.",
        file=sys.stderr,
    )
    sys.exit(0)

imgs = [f for f in glob("dist/assets/*", recursive=True) if is_img(f)]
threads = []

for img in imgs:
    t = Thread(target=optimize_image, args=(img,))
    t.start()

    threads.append(t)


def replace_in_html(html: str, img_basenames: list):
    with open(html, "r") as f:
        content = f.read()

    for img in img_basenames:
        content = content.replace(img, optimized_name(img))

    with open(html, "w") as f:
        f.write(content)

    print(f"Replaced in {html}")


htmls = [f for f in glob("dist/**/*.html", recursive=True)]
img_basenames = [os.path.basename(img) for img in imgs]

for html in htmls:
    t = Thread(target=replace_in_html, args=(html, img_basenames))
    t.start()

    threads.append(t)

for t in threads:
    t.join()
