#!/usr/bin/env python3
"""Generate the static Open Graph image src/og.png (1200x630), festive certificate style.
Independent brand only: no seals, eagles, flags, signatures or serial numbers. Run: python3 src/make_og.py"""
import math, pathlib, random
from PIL import Image, ImageDraw, ImageFont
OUT = pathlib.Path(__file__).parent / "og.png"
W, H = 1200, 630
BG, PAPER, INK, MUTED, ACC, ACCD, GOLD, GOLDD, TEAL, SOFT = ("#fff8ee", "#fffdf8", "#2a2320", "#6b5f57", "#c4512b",
    "#9e3d1c", "#e0a83a", "#b9811c", "#0f6b63", "#fdf0ea")
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FS = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
f = lambda p, s: ImageFont.truetype(p, s)
def proj(fam):  # mirror of build.project(): newborn, seed, 7% - 0.03% fee
    b = 1000.0
    for _ in range(18): b = (b + fam) * (1 + 0.07 - 0.0003)
    return b
def star(d, cx, cy, r, fill):
    pts = [(cx + (r if i % 2 == 0 else r * .45) * math.cos(-math.pi / 2 + i * math.pi / 5),
            cy + (r if i % 2 == 0 else r * .45) * math.sin(-math.pi / 2 + i * math.pi / 5)) for i in range(10)]
    d.polygon(pts, fill=fill)
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
rnd = random.Random(7); cols_c = [ACC, GOLD, TEAL, "#ee8f73", GOLDD]
for _ in range(110):  # confetti, mostly outside the paper
    x, y = rnd.uniform(0, W), rnd.uniform(0, H)
    if 40 < x < W - 40 and 40 < y < H - 40 and rnd.random() < .8: continue
    c = rnd.choice(cols_c)
    if rnd.random() < .5: d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=c)
    else:
        a = rnd.uniform(0, math.pi); dx, dy = 9 * math.cos(a), 9 * math.sin(a); d.line([(x - dx, y - dy), (x + dx, y + dy)], fill=c, width=6)
d.rounded_rectangle([30, 30, W - 30, H - 30], 30, fill=PAPER, outline=ACC, width=9)
# gold dashed inner border
x0, y0, x1, y1 = 54, 54, W - 54, H - 54
for (ax, ay, bx, by) in [(x0, y0, x1, y0), (x0, y1, x1, y1), (x0, y0, x0, y1), (x1, y0, x1, y1)]:
    L = math.hypot(bx - ax, by - ay); n = int(L // 22)
    for i in range(n):
        t0, t1 = i * 22 / L, min((i * 22 + 12) / L, 1)
        d.line([(ax + (bx - ax) * t0, ay + (by - ay) * t0), (ax + (bx - ax) * t1, ay + (by - ay) * t1)], fill=GOLD, width=3)
for cx, cy in [(x0 + 22, y0 + 22), (x1 - 22, y0 + 22), (x0 + 22, y1 - 22), (x1 - 22, y1 - 22)]: star(d, cx, cy, 16, GOLD)
for _ in range(26):  # light confetti on the paper, away from text
    x, y = rnd.uniform(80, 360), rnd.uniform(90, 560); d.ellipse([x - 4, y - 4, x + 4, y + 4], fill=rnd.choice(cols_c))
# rosette (left)
RX, RY, R = 225, 270, 120
for sx, col in [(-1, ACC), (1, ACCD)]:
    d.polygon([(RX + sx * 20, RY + 60), (RX + sx * 95, RY + 250), (RX + sx * 58, RY + 228), (RX + sx * 38, RY + 268), (RX - sx * 20 + sx * 30, RY + 80)], fill=col)
pts = []
for i in range(48):
    rr = R if i % 2 == 0 else R * .88; a = i * math.pi / 24; pts.append((RX + rr * math.cos(a), RY + rr * math.sin(a)))
d.polygon(pts, fill=GOLD)
d.ellipse([RX - 92, RY - 92, RX + 92, RY + 92], fill="#fff6e2", outline=GOLDD, width=4)
star(d, RX, RY - 28, 34, GOLD)
d.text((RX, RY + 30), "$1,000", font=f(F, 34), fill=ACCD, anchor="mm")
d.text((RX, RY + 64), "SEED", font=f(F, 20), fill=GOLDD, anchor="mm")
# text (right)
X = 400
d.text((X, 120), "★  PROUD PARENT MOMENT  ★", font=f(F, 24), fill=GOLDD, anchor="ls")
d.text((X, 190), "Is your little one on", font=f(FS, 46), fill=INK, anchor="ls")
d.text((X, 248), "track for", font=f(FS, 46), fill=INK, anchor="ls")
big = "${:,.0f}".format(proj(1000))
d.text((X + d.textlength("track for ", font=f(FS, 46)), 252), big + " by 18?", font=f(F, 52), fill=ACCD, anchor="ls")
d.rounded_rectangle([X, 285, 1120, 425], 24, fill=SOFT)
cols = [("Free $1,000 only", proj(0)), ("+ $25 a month", proj(300)), ("+ $1,000 a year", proj(1000))]
for i, (lab, v) in enumerate(cols):
    cx = X + (1120 - X) * (2 * i + 1) / 6
    d.text((cx, 330), lab, font=f(FR, 23), fill=MUTED, anchor="mm")
    d.text((cx, 380), "${:,.0f}".format(v), font=f(F, 42), fill=ACCD if i == 2 else INK, anchor="mm")
d.text((X, 470), "Make a free celebration card · estimate, not a guarantee", font=f(FR, 22), fill=MUTED, anchor="ls")
d.text((X, 512), "Awarded by KidAccountMath (independent, not a government document)", font=f(FR, 18), fill=MUTED, anchor="ls")
d.text((X, 552), "j6-cloude.github.io", font=f(F, 28), fill=TEAL, anchor="ls")
im.save(OUT, optimize=True); print(OUT, im.size, [round(v) for _, v in cols])
