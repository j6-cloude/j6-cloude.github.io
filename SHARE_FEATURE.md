# Share feature (KidAccountMath) — how it works / how to copy it

Goal: after a calculator result, let a parent share "their number" as a picture + a link that reproduces the result.
No tracking, no third-party scripts, no cookies. All client-side.

## Files (branch `source`)
- `src/share.js` — `window.KAMShare`. Draws a 1080x1350 PNG on a `<canvas>` (festive certificate style, see below; system fonts only), shows a preview `<img>` (object URL, re-rendered 350 ms after the last input), and wires buttons:
  - Download image (`<a download>` on the blob URL)
  - Native share (`navigator.share`, with `files:[File]` only if `navigator.canShare({files})` is true; URL also put in `text`
    because some apps drop `url` when files are attached). Button hidden when `navigator.share` is missing.
  - Fallback plain links (no SDKs): Facebook `https://www.facebook.com/sharer/sharer.php?u=`, SMS `sms:?&body=`,
    WhatsApp `https://wa.me/?text=`, Copy link (`navigator.clipboard`, falls back to `execCommand('copy')` on the readonly input).
- `src/calc.js` — after computing, calls `KAMShare.update({age,fam,emp,r,to,seed,dell,bal})`. On load, `prefill()` reads
  `?age=&amt=&r=` (+ optional `seed=0`, `dell=1`, `emp=`, `to=`) into the inputs before the first `run()`; existing clamps still
  apply. With no params, defaults are untouched (newborn, $1,000/yr, 7% → $39,627).
- `src/build.py` — share `<section id="share" hidden>` markup inside `CALC_FORM` right after `#out`; `share.js` loaded `defer`
  before `calc.js` (order matters); og meta on every page: `og:image` = `/assets/og.png` (1200x630), `twitter:card=summary_large_image`.
- `src/make_og.py` — Pillow script that renders `src/og.png` (numbers computed with the same formula). The PNG is committed so the
  build needs no extra deps; rerun it only if the numbers/brand change.
- `src/style.css` — `.share`, `.shimg`, `.shbtns`, `.shlinks`, `.shurl` (44px+ tap targets, mobile-first).

Shared links always point at the calculator page: `BASE/trump-account-calculator/?age=0&amt=1000&r=7`.

## Testing on this box
`google-chrome --dump-dom` hangs here. Driving Chrome over CDP works:
start `google-chrome --headless=new --no-sandbox --user-data-dir=/tmp/x --remote-debugging-port=9333 about:blank &`,
then a small Node script (`node --experimental-websocket`, Node 20) that navigates, evaluates
`KAMShare.draw(state).toDataURL()` and writes the PNG. See /tmp/cdp.mjs pattern (Page.navigate, Runtime.evaluate,
Page.captureScreenshot). Check: default result $39,627; `?age=3&amt=600&r=6` pre-fills and gives $17,152.

## Deploy
Build `BASE_URL=https://j6-cloude.github.io python3 src/build.py`, then copy `public/` into a worktree of `origin/main`,
commit, normal `git push origin main` (no force). Then `BASE_URL=https://j6-cloude.github.io ./indexnow_ping.sh`.

## Porting to another site
Copy `share.js`, change the colors/headline/assumptions text in `draw()` and the `query()`/`shareURL()` mapping; call
`KAMShare.update(state)` at the end of the calculator's render; add the markup block and a `prefill()` that maps params to inputs.

## v2: celebration certificate (festive, NOT official-looking)
Two card kinds, chosen by `data-kind` on `<section id="share">`:
- `proj` (calculator + home): "★ PROUD PARENT MOMENT ★ / [Name] / is on track for / $XX,XXX / by age 18! 🎉", gold rosette +
  ribbon banner with a milestone tier, "Started investing at age N", assumptions line, "Estimate, not a guarantee".
  Tiers (`TIERS` in share.js, [min, title, emoji, rosette label]): ≥100k Money Tree Legend 🌳, ≥40k Growth Superstar 🚀,
  ≥15k Compound Interest Champion 🏆 (default $39,627), ≥5k Little Saver Star ⭐, else Future Investor 🌱.
- `claim` (how-to-claim + eligibility checker): hidden behind button "I've claimed it — make my certificate" (`#shgo`).
  "★ ACHIEVEMENT UNLOCKED ★", CLAIMED! rosette, "We claimed [Name]'s $1,000 Trump Account seed!", "Did you claim yours? Check
  free at <host>". Self-declared, no verification of any kind. Share link = eligibility checker, no params.
- Look: cream paper #fffdf8 on #fff8ee, terracotta rounded outer border, gold dashed inner border + corner stars, seeded
  confetti, gold scalloped rosette with ribbon tails, serif name, big terracotta number. Palette: ink #2a2320, accent #c4512b /
  #9e3d1c, gold #e0a83a / #b9811c, teal #0f6b63.
- Hard rule: never official-looking. No eagles, seals, flags, "Department of the Treasury"/IRS styling, signatures, serial
  numbers. Footer always says "Awarded by KidAccountMath" + "(independent, not a government document)" + host.
- Name field (`#shname`, optional, max 20 chars, sanitized): drawn on the card only, stays in the browser. Default
  "Our little one". Added to the link as `&name=` ONLY if "Include name in link" (`#shincl`) is ticked; never in share text.
  `?name=` on load prefills the field and ticks the box.
- `src/make_og.py` renders the matching festive og.png (rosette + $3,363 / $14,242 / $39,627).
- Test: /tmp/cdp2.mjs (CDP) renders screenshots/cert-*.png and tier-*.png and checks name-not-in-URL + prefill.

Porting tip for j33: copy `frame()`, `rosette()`, `banner()`, `footer()` from share.js, swap the headline lines, tiers and
assumptions text; keep the independent-site footer.
