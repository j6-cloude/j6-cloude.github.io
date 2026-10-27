# KidAccountMath – Trump Account calculator site (static)

Build:  BASE_URL=https://USERNAME.github.io python3 src/build.py   # or https://yourdomain.com (root only, no subpath); outputs ./public
Local:  cd public && python3 -m http.server 8765
Deploy: upload ./public to any static host (Cloudflare Pages / Netlify / GitHub Pages / Vercel).
After live: BASE_URL=https://YOURDOMAIN ./indexnow_ping.sh

Before launch, set env vars AUTHOR_NAME and CONTACT_EMAIL (real, monitored) and rebuild.
AdSense: paste the script tag in src/build.py <head> (comment marks the spot) and fill .ad-slot divs.
Facts sources: IRS Trump Accounts page + FAQ, Form 4547 instructions, 26 USC 530A, Invest America (Dell $250). Re-check monthly; update UPDATED in build.py.
Verify: GOOGLE_SITE_VERIFICATION=xxx BING_SITE_VERIFICATION=yyy BASE_URL=https://j6-cloude.github.io python3 src/build.py  (content= values only), then redeploy public/ to main.
Deploy (GitHub Pages, repo j6-cloude/j6-cloude.github.io): branch `source` = generator; branch `main` = contents of public/ (+ .nojekyll).
  BASE_URL=https://j6-cloude.github.io python3 src/build.py && rm -rf /tmp/deploy && git clone -q -b main https://github.com/j6-cloude/j6-cloude.github.io.git /tmp/deploy && cp -r public/. /tmp/deploy/ && cd /tmp/deploy && git add -A && git commit -qm deploy && git push origin main   # normal push, never -f
