#!/usr/bin/env python3
"""Generate the static Open Graph image src/og.png (1200x630). Run: python3 src/make_og.py"""
import pathlib, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, str(pathlib.Path(__file__).parent))
OUT = pathlib.Path(__file__).parent / "og.png"
W, H = 1200, 630
BG, INK, MUTED, ACC, ACCD, SOFT, TEAL, LINE = "#faf8f4", "#1f2328", "#575d66", "#c4512b", "#a8421f", "#fdf0ea", "#0f6b63", "#e7e2da"
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
f = lambda p, s: ImageFont.truetype(p, s)
# mirror of build.project(): newborn, seed, 7% - 0.03% fee
def proj(fam):
    b = 1000.0
    for _ in range(18): b = (b + fam) * (1 + 0.07 - 0.0003)
    return b
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
d.rectangle([0, 0, W, 14], fill=ACC)
d.rounded_rectangle([70, 70, 134, 134], 18, fill=ACC)
d.line([(86, 116), (96, 106), (104, 112), (118, 96)], fill="white", width=7, joint="curve")
d.text((154, 102), "KidAccountMath", font=f(F, 40), fill=INK, anchor="lm")
d.text((70, 215), "How much could your child's", font=f(F, 54), fill=INK, anchor="ls")
d.text((70, 285), "Trump Account be worth at 18?", font=f(F, 54), fill=INK, anchor="ls")
d.rounded_rectangle([70, 330, 1130, 500], 28, fill="white", outline=LINE, width=3)
cols = [("Free $1,000 only", proj(0)), ("+ $25 a month", proj(300)), ("+ $1,000 a year", proj(1000))]
for i, (lab, v) in enumerate(cols):
    x = 70 + 1060 * (2 * i + 1) / 6
    d.text((x, 395), lab, font=f(FR, 28), fill=MUTED, anchor="mm")
    d.text((x, 450), "${:,.0f}".format(v), font=f(F, 52), fill=ACCD, anchor="mm")
d.text((70, 550), "Newborn, 7% yearly return assumed. Estimate, not a guarantee.", font=f(FR, 26), fill=MUTED, anchor="ls")
d.text((70, 595), "Free calculator · j6-cloude.github.io", font=f(F, 28), fill=TEAL, anchor="ls")
im.save(OUT, optimize=True); print(OUT, im.size, [round(v) for _, v in cols])
