# KidAccountMath – Trump Account calculator site (static)

Build:  BASE_URL=https://YOURDOMAIN python3 src/build.py   # outputs ./public
Local:  cd public && python3 -m http.server 8765
Deploy: upload ./public to any static host (Cloudflare Pages / Netlify / GitHub Pages / Vercel).
After live: BASE_URL=https://YOURDOMAIN ./indexnow_ping.sh

Before launch, set env vars AUTHOR_NAME and CONTACT_EMAIL (real, monitored) and rebuild.
AdSense: paste the script tag in src/build.py <head> (comment marks the spot) and fill .ad-slot divs.
Facts sources: IRS Trump Accounts page + FAQ, Form 4547 instructions, 26 USC 530A, Invest America (Dell $250). Re-check monthly; update UPDATED in build.py.
