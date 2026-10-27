#!/usr/bin/env python3
"""Static site generator for the Trump Account calculator site.
Usage: BASE_URL=https://yourdomain.com python3 src/build.py   -> writes ./public
"""
import os, json, html, shutil, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "public"
BASE = os.environ.get("BASE_URL", "https://example.com").rstrip("/")
SITE = "KidAccountMath"
TAGLINE = "Free Trump Account (Section 530A) calculators and plain-English guides"
AUTHOR = os.environ.get("AUTHOR_NAME", "j6")
CONTACT_EMAIL = os.environ.get("CONTACT_EMAIL", "contact@example.com")  # replace before launch
UPDATED = "2026-10-27"
UPDATED_H = "October 27, 2026"
INDEXNOW_KEY = (ROOT / ".indexnow_key").read_text().strip()

# ---------- calculator (mirrors assets/calc.js) ----------
def project(age_now=0, seed=True, dell=False, family=1000, employer=0, ret=0.07, fee=0.0003, to_age=18):
    emp = min(employer, 2500); fam = min(family, 5000 - emp)
    b = (1000 if seed else 0) + (250 if dell else 0)
    rows = []; contrib = b; basis = 0
    for age in range(age_now, to_age):
        c = fam + emp if age < 18 else 0
        b = (b + c) * (1 + ret - fee)
        contrib += c; basis += fam if age < 18 else 0
        rows.append((age + 1, c, b))
    return b, contrib, basis, rows

def money(x): return "${:,.0f}".format(x)

# ---------- layout ----------
NAV = [("/", "Home"), ("/trump-account-calculator/", "Calculator"), ("/trump-account-eligibility-checker/", "Eligibility"),
       ("/trump-account-vs-529/", "vs 529"), ("/does-my-child-have-a-trump-account/", "Check my child"), ("/how-to-claim-trump-account/", "How to claim"), ("/trump-account-rules/", "Rules")]

ORG = {"@type": "Organization", "@id": BASE + "/#org", "name": SITE, "url": BASE + "/",
       "description": TAGLINE, "email": CONTACT_EMAIL}

def faq_ld(faqs):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": html.unescape(strip(a))}} for q, a in faqs]}

def strip(s):
    import re; return re.sub(r"<[^>]+>", "", s)

def faq_html(faqs):
    out = '<section id="faq"><h2>Frequently asked questions</h2>'
    for q, a in faqs:
        out += f'<h3>{q}</h3><p>{a}</p>'
    return out + "</section>"

def page(path, title, desc, body, ld=None, faqs=None, h1=None, sources=None):
    url = BASE + path
    graph = [ORG, {"@type": "WebSite", "@id": BASE + "/#site", "url": BASE + "/", "name": SITE, "publisher": {"@id": BASE + "/#org"}},
             {"@type": "WebPage", "@id": url, "url": url, "name": title, "description": desc, "dateModified": UPDATED,
              "isPartOf": {"@id": BASE + "/#site"}, "author": {"@type": "Person", "name": AUTHOR, "url": BASE + "/about/"}}]
    if path != "/":
        crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
                  {"@type": "ListItem", "position": 2, "name": h1 or title, "item": url}]
        graph.append({"@type": "BreadcrumbList", "itemListElement": crumbs})
    if ld: graph += ld if isinstance(ld, list) else [ld]
    if faqs: graph.append(faq_ld(faqs)); body += faq_html(faqs)
    if sources:
        body += '<section class="sources"><h2>Sources</h2><ul>' + "".join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in sources) + "</ul></section>"
    nav = "".join(f'<a href="{h}"{" aria-current=page" if h == path else ""}>{t}</a>' for h, t in NAV)
    doc = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{url}"><meta property="og:site_name" content="{SITE}">
<meta name="twitter:card" content="summary">
<link rel="alternate" type="text/plain" title="llms.txt" href="/llms.txt">
<link rel="stylesheet" href="/assets/style.css">
<!-- AdSense: paste the <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXX"> tag here after approval -->
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)}</script>
</head><body>
<header><a class="brand" href="/">{SITE}</a><nav>{nav}</nav></header>
<main>
<h1>{h1 or title}</h1>
<p class="meta">Written by <a href="/about/">{AUTHOR}</a> · Updated <time datetime="{UPDATED}">{UPDATED_H}</time> · Based on IRS/Treasury guidance · Not tax advice</p>
{body}
<div class="ad-slot" data-ad-slot="bottom" aria-hidden="true"></div>
</main>
<footer><p><a href="/about/">About</a> · <a href="/contact/">Contact</a> · <a href="/privacy/">Privacy</a> · <a href="/disclaimer/">Disclaimer</a> · <a href="/sitemap.xml">Sitemap</a> · <a href="/llms.txt">llms.txt</a></p>
<p>{SITE} is an independent educational site. It is not affiliated with the IRS, the U.S. Treasury, trumpaccounts.gov, BNY, Robinhood or any government agency. Figures are illustrations, not guarantees or advice.</p></footer>
</body></html>"""
    d = OUT / path.strip("/")
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(doc)
    PAGES.append((path, title, desc, strip(body)))

PAGES = []

# ---------- shared content ----------
DEF = ("A <strong>Trump Account</strong> is a tax-advantaged investment account for U.S. children created by the 2025 tax law "
       "(Internal Revenue Code section 530A). It is legally a type of traditional IRA for a child under 18. Family and others can add up to "
       "<strong>$5,000 a year</strong> (employers up to $2,500 of that), the money must sit in low-cost U.S. stock index funds (fees of 0.10% or less), "
       "and it generally cannot be withdrawn until the year the child turns 18. Children born 2025–2028 who are U.S. citizens can get a one-time "
       "<strong>$1,000</strong> from the Treasury.")

IRS = ("IRS: Trump Accounts", "https://www.irs.gov/trumpaccounts")
IRSFAQ = ("IRS: Trump Accounts – Frequently asked questions", "https://www.irs.gov/faqs/trump-accounts-frequently-asked-questions")
I4547 = ("IRS: Instructions for Form 4547", "https://www.irs.gov/instructions/i4547")
USC = ("26 U.S.C. § 530A (statute text)", "https://uscode.house.gov/us/usc/119-124/t26/s530A/")
GOV = ("trumpaccounts.gov (official program site)", "https://trumpaccounts.gov/")
DELL = ("Invest America: Dell $250 eligibility", "https://investamerica.org/check-dell-250-eligibility/")
IRSNEWS = ("IRS/Treasury guidance news release", "https://www.irs.gov/newsroom/treasury-irs-issue-guidance-on-trump-accounts-established-under-the-working-families-tax-cuts-notice-announces-upcoming-regulations")

def table(rows, head):
    return "<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>" + \
        "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>"

# quick-answer table used on several pages (7% gross, 0.03% fee)
def scenario_rows():
    out = []
    for fam in (0, 600, 1200, 2500, 5000):
        b18, contrib, basis, _ = project(0, True, False, fam, 0, 0.07, 0.0003, 18)
        b30, *_ = project(0, True, False, fam, 0, 0.07, 0.0003, 30)
        out.append(("Seed only" if fam == 0 else money(fam) + "/yr", money(contrib), money(b18), money(b30)))
    return out
SCEN = table(scenario_rows(), ["Family adds", "Total put in by 18", "Value at 18", "Value at 30 (no more deposits)"])
SCEN_NOTE = "<p class=small>Assumes a newborn who gets the $1,000 Treasury seed, deposits at the start of each year until age 17, a 7% annual return before a 0.03% fund fee, no withdrawals, nominal dollars (not inflation-adjusted), and the $5,000 limit held flat. Returns are not guaranteed; stock index funds can lose money in any year.</p>"

CALC_FORM = """
<form id="calc" class="calc" onsubmit="return false">
 <div class="grid">
  <label>Child's age today <input type="number" id="age" min="0" max="17" value="0"></label>
  <label>Annual family contribution ($) <input type="number" id="fam" min="0" max="5000" step="50" value="1000"></label>
  <label>Annual employer contribution ($, max 2,500) <input type="number" id="emp" min="0" max="2500" step="50" value="0"></label>
  <label>Expected annual return (%) <input type="number" id="ret" min="-5" max="15" step="0.5" value="7"></label>
  <label>Fund expense ratio (%, legal max 0.10) <input type="number" id="fee" min="0" max="0.1" step="0.01" value="0.03"></label>
  <label>Project to age <input type="number" id="to" min="18" max="65" value="18"></label>
  <label>Your expected tax rate when withdrawn (%) <input type="number" id="tax" min="0" max="50" step="1" value="12"></label>
  <label>Inflation for "today's dollars" (%) <input type="number" id="inf" min="0" max="10" step="0.5" value="2.5"></label>
 </div>
 <label class="chk"><input type="checkbox" id="seed" checked> Gets the $1,000 Treasury seed (U.S. citizen born 2025–2028, election made)</label>
 <label class="chk"><input type="checkbox" id="dell"> Got the Dell $250 deposit (born 2016–2024, qualifying ZIP)</label>
 <label class="chk"><input type="checkbox" id="pen" checked> Apply 10% early-withdrawal penalty if withdrawn before 59½ (education/first-home exceptions may apply)</label>
</form>
<div id="out" class="out" aria-live="polite"></div>
<details><summary>Year-by-year table</summary><div id="yy"></div></details>
<script src="/assets/calc.js" defer></script>
"""

# ---------- pages ----------
b18, c18, basis18, rows = project()
home_body = f"""
<p class="lead">{DEF}</p>
<div class="answer"><strong>Quick answer:</strong> the $1,000 seed alone grows to about <strong>{money(project(0,True,False,0)[0])}</strong> by age 18 at a 7% return. Adding $1,000 a year from birth gives about <strong>{money(b18)}</strong> by 18. The maximum ($5,000/yr) gives about <strong>{money(project(0,True,False,5000)[0])}</strong>. Use the calculator for your own numbers.</div>
<h2>Trump Account calculator</h2>
{CALC_FORM}
<noscript><p>The interactive calculator needs JavaScript. The table below shows common scenarios.</p></noscript>
<h2>How much will a Trump Account be worth? Common scenarios</h2>
{SCEN}{SCEN_NOTE}
<h2>Guides</h2>
<ul class="cards">
<li><a href="/trump-account-calculator/">Trump Account calculator with after-tax value</a> – projects the balance at 18 or later, and what you keep after tax.</li>
<li><a href="/trump-account-eligibility-checker/">Eligibility checker</a> – does your child qualify for the account, the $1,000 seed, or the Dell $250?</li>
<li><a href="/trump-account-vs-529/">Trump Account vs 529 plan</a> – which one to fund first, side-by-side table.</li>
<li><a href="/trump-account-vs-custodial-roth-ira/">Trump Account vs custodial Roth IRA vs UTMA</a> – comparison table.</li>
<li><a href="/does-my-child-have-a-trump-account/">How do I know if my child has a Trump Account?</a> – auto-enrollment check, and whether the app is legit.</li>
<li><a href="/how-to-claim-trump-account/">How to claim a Trump Account</a> – step by step after automatic enrollment.</li>
<li><a href="/form-4547-cp318-notice/">Form 4547 rejected / Notice CP318</a> – what it means and how to fix it.</li>
<li><a href="/trump-account-rules/">Trump Account rules 2026</a> – limits, investments, withdrawals, taxes.</li>
</ul>
"""
page("/", "Trump Account Calculator 2026 – Seed, $5,000 Limit & After-Tax Value", 
     "Free Trump Account calculator: project a child's 530A account from the $1,000 seed and yearly deposits, see after-tax value, and compare with a 529.",
     home_body, h1="Trump Account Calculator & Guide (2026)",
     ld={"@type": "WebApplication", "name": "Trump Account Calculator", "url": BASE + "/", "applicationCategory": "FinanceApplication",
         "operatingSystem": "Any (web browser)", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}},
     faqs=[("What is a Trump Account?", DEF),
           ("How much will $1,000 in a Trump Account be worth at 18?", f"At a 7% annual return (before a 0.03% fee), the $1,000 Treasury seed alone grows to about {money(project(0,True,False,0)[0])} by age 18. Returns are not guaranteed."),
           ("What is the Trump Account contribution limit?", "$5,000 per child per year from family and others, of which up to $2,500 can come from an employer. The $1,000 Treasury seed, qualified government/charity contributions and rollovers do not count toward the limit. The limit is indexed to inflation after 2027."),
           ("When can the money be withdrawn?", "Generally not before January 1 of the year the child turns 18. After that the account follows traditional IRA rules: earnings and pre-tax money are taxed as ordinary income when withdrawn, and withdrawals before age 59½ may face a 10% penalty unless an exception (such as qualified higher education or a first home) applies.")],
     sources=[IRS, IRSFAQ, I4547, USC])

# Calculator page
calc_body = f"""
<p class="lead">Enter your child's age, how much the family and an employer will add each year, and an expected return. The calculator applies the $5,000 annual cap (employer max $2,500), the 0.10% fund-fee cap, stops contributions at 18, and estimates what you would keep after tax if the money is withdrawn.</p>
{CALC_FORM}
<h2>How the calculation works</h2>
<p>Each year until the child turns 18: <code>balance = (balance + family + employer) × (1 + return − fee)</code>. From 18 onward no new Trump Account contributions are modeled and the balance compounds alone. The starting balance includes the $1,000 Treasury seed and/or the Dell $250 deposit if ticked.</p>
<p><strong>After-tax estimate.</strong> A Trump Account becomes a traditional-IRA-style account. Family contributions are after-tax money and create <em>basis</em>, which is not taxed again. The seed, the Dell gift, employer money and all growth are taxed as ordinary income when withdrawn. The calculator applies your chosen tax rate to that taxable part and, if ticked, a 10% penalty for withdrawals before 59½. This is a simplification; real taxes depend on the year, state and exceptions.</p>
<h2>Example: newborn, $1,000 a year, 7% return</h2>
{table([(r[0], money(r[1]), money(r[2])) for r in rows if r[0] in (1,5,10,15,18)], ["Age", "Contribution that year", "Balance"])}
<p class=small>Seed included. Total contributed by 18: {money(c18)}; balance {money(b18)}; of which your after-tax basis is {money(basis18)}.</p>
<h2>Scenarios</h2>{SCEN}{SCEN_NOTE}
"""
page("/trump-account-calculator/", "Trump Account Calculator: Growth to 18 and After-Tax Value (2026)",
     "Project a Trump Account balance from the $1,000 seed, family and employer deposits up to $5,000/yr, with fees, inflation and after-tax value.",
     calc_body, h1="Trump Account Calculator",
     ld={"@type": "WebApplication", "name": "Trump Account Calculator", "url": BASE + "/trump-account-calculator/", "applicationCategory": "FinanceApplication",
         "operatingSystem": "Any (web browser)", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}},
     faqs=[("Does the calculator include the $1,000 seed?", "Yes, if you tick the seed box. Only U.S. citizens born January 1, 2025 through December 31, 2028 qualify, and a parent must elect it on Form 4547."),
           ("What return should I use?", "There is no guaranteed return. Broad U.S. stock indexes have historically averaged roughly 10% nominal per year over long periods, with large losses in some years. Many planners use 5–7% to be conservative."),
           ("Is the Trump Account tax-free?", "No. It is tax-deferred, not tax-free. Growth is taxed as ordinary income when withdrawn (after 18), except the after-tax family contributions (basis).")],
     sources=[I4547, USC, IRSNEWS])

# Eligibility checker
elig_body = """
<p class="lead">Three different things are often confused: (1) the <strong>account itself</strong>, (2) the <strong>$1,000 Treasury seed</strong>, and (3) the <strong>Dell $250 gift</strong>. Each has its own rules.</p>
<form id="elig" class="calc" onsubmit="return false">
 <div class="grid">
 <label>Child's birth year <input type="number" id="by" min="2000" max="2028" value="2025"></label>
 <label>U.S. citizen? <select id="cit"><option value="1">Yes</option><option value="0">No</option></select></label>
 <label>Has a valid SSN? <select id="ssn"><option value="1">Yes</option><option value="0">No</option></select></label>
 <label>ZIP median family income ≤ $117,300 (or lives on a military base)? <select id="zip"><option value="u">Not sure</option><option value="1">Yes</option><option value="0">No</option></select></label>
 </div></form>
<div id="eout" class="out" aria-live="polite"></div>
<script src="/assets/elig.js" defer></script>
<h2>Eligibility rules at a glance</h2>
<table><thead><tr><th>Benefit</th><th>Who qualifies</th><th>How to get it</th></tr></thead><tbody>
<tr><td>Trump Account</td><td>Any child with a valid SSN who will not turn 18 before the end of the year the account is established</td><td>Treasury auto-enrolled eligible children from Oct 1, 2026; claim it in the Trump Accounts app/website. Otherwise file Form 4547.</td></tr>
<tr><td>$1,000 Treasury seed</td><td>U.S. citizens born Jan 1, 2025 – Dec 31, 2028 with a valid SSN</td><td>Must be elected on Form 4547 (app, website, or IRS Online Account), even if the account was auto-opened</td></tr>
<tr><td>Dell $250</td><td>Children born 2016–2024 in ZIP codes with median family income of about $117,300 or less, plus children on military bases</td><td>Automatic; no application. Check the ZIP on Invest America's lookup</td></tr>
</tbody></table>
<noscript><p>The checker needs JavaScript; the table above contains the same rules.</p></noscript>
"""
page("/trump-account-eligibility-checker/", "Trump Account Eligibility Checker: Account, $1,000 Seed and Dell $250",
     "Check whether your child qualifies for a Trump Account, the $1,000 Treasury seed (born 2025–2028) and the Dell $250 deposit (born 2016–2024).",
     elig_body, h1="Trump Account Eligibility Checker",
     ld={"@type": "WebApplication", "name": "Trump Account Eligibility Checker", "url": BASE + "/trump-account-eligibility-checker/", "applicationCategory": "FinanceApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}},
     faqs=[("Is my child born in 2024 eligible for the $1,000?", "No. The $1,000 seed is only for U.S. citizens born from January 1, 2025 through December 31, 2028. A 2024 child can still have a Trump Account and may get the Dell $250 if the ZIP code qualifies."),
           ("Do non-citizen children qualify?", "A child with a valid SSN can have a Trump Account. The $1,000 seed requires U.S. citizenship."),
           ("Do I need to apply for the Dell $250?", "No. According to Michael & Susan Dell's announcement, eligible children receive it automatically. The income threshold was set at a ZIP-code median family income of about $117,300 (as of Oct 9, 2026)."),
           ("My child was auto-enrolled. Do I still need Form 4547?", "Not to open the account, but yes to request the $1,000 seed if your child qualifies, and you must claim the account to manage it.")],
     sources=[IRS, IRSFAQ, DELL, ("Michael & Susan Dell: $250 contribution", "https://www.onedell.com/25-million-children-trump-accounts-dell-contribution/")])

# vs 529
v529 = """
<p class="lead"><strong>Short answer:</strong> if college is the main goal, a 529 usually wins because qualified education withdrawals are tax-free, while Trump Account growth is taxed as income. Always grab the free $1,000 seed (and any employer money) first; then a 529 for education; a Trump Account makes more sense for long-term, non-education wealth.</p>
<h2>Trump Account vs 529: comparison table</h2>
<table><thead><tr><th></th><th>Trump Account (530A)</th><th>529 plan</th></tr></thead><tbody>
<tr><td>Main purpose</td><td>Long-term investing; becomes an IRA at 18</td><td>Education (college, K-12 tuition up to limits, some apprenticeships)</td></tr>
<tr><td>Free money</td><td>$1,000 seed (born 2025–2028); possible Dell $250; employer up to $2,500/yr tax-free to employee</td><td>Some state matches/grants; no federal seed</td></tr>
<tr><td>Annual limit</td><td>$5,000 (plus exempt contributions)</td><td>No annual federal limit; gifts above the annual gift-tax exclusion need reporting; high lifetime caps set by states</td></tr>
<tr><td>Tax on contributions</td><td>No federal deduction</td><td>No federal deduction; many states give a state deduction</td></tr>
<tr><td>Tax on withdrawals</td><td>Earnings and non-basis money taxed as ordinary income; 10% penalty before 59½ unless an exception applies</td><td>Tax-free for qualified education; earnings taxed + 10% penalty for non-qualified use</td></tr>
<tr><td>Investments</td><td>Only U.S. stock index funds, fees ≤ 0.10%, no leverage</td><td>Plan menu: age-based, stock, bond, cash options</td></tr>
<tr><td>Access</td><td>Locked until the year the child turns 18</td><td>Any time (tax depends on use)</td></tr>
<tr><td>Who controls it after 18</td><td>The child (it becomes their IRA)</td><td>The account owner (usually the parent)</td></tr>
</tbody></table>
<h2>Which should you fund first?</h2>
<ol><li>Elect the $1,000 seed on Form 4547 if your child was born 2025–2028 — it costs nothing.</li>
<li>Take any employer Trump Account contribution; it is excluded from your income up to $2,500.</li>
<li>For expected college costs, fund a 529 (check your state's deduction).</li>
<li>Extra long-term money: a Trump Account, or a custodial Roth IRA if the child has earned income (see <a href="/trump-account-vs-custodial-roth-ira/">comparison</a>).</li></ol>
<p>Run your own numbers in the <a href="/trump-account-calculator/">Trump Account calculator</a>, which estimates the tax due on withdrawal.</p>
"""
page("/trump-account-vs-529/", "Trump Account vs 529 Plan: Which Is Better for Your Child? (2026)",
     "Side-by-side Trump Account vs 529 comparison: limits, free money, taxes on withdrawal, investments and which to fund first.",
     v529, h1="Trump Account vs 529 Plan",
     faqs=[("Is a Trump Account better than a 529?", "For college savings, a 529 is usually better because qualified education withdrawals are tax-free. A Trump Account is better for free money (the $1,000 seed, employer contributions) and long-term, non-education investing."),
           ("Can I have both a Trump Account and a 529?", "Yes. Nothing prevents a child from having both."),
           ("Can Trump Account money be used for college?", "After the account becomes IRA-like at 18, IRA rules apply: withdrawals for qualified higher-education expenses avoid the 10% early-withdrawal penalty, but the taxable part is still subject to income tax.")],
     sources=[I4547, USC, ("IRS: Topic 557 – additional tax on early IRA distributions (exceptions)", "https://www.irs.gov/taxtopics/tc557"), ("IRS: 529 plans – questions and answers", "https://www.irs.gov/newsroom/529-plans-questions-and-answers")])

vroth = """
<p class="lead"><strong>Short answer:</strong> a custodial Roth IRA is the best tax deal (tax-free growth) but needs the child to have earned income. A Trump Account needs no earned income but growth is taxed on withdrawal. A UTMA/UGMA has no limits or investment restrictions but its earnings are taxed yearly (kiddie tax) and the child controls it at 18–21.</p>
<table><thead><tr><th></th><th>Trump Account</th><th>Custodial Roth IRA</th><th>UTMA/UGMA</th></tr></thead><tbody>
<tr><td>Child needs earned income?</td><td>No</td><td>Yes (contribution ≤ earned income)</td><td>No</td></tr>
<tr><td>Annual limit</td><td>$5,000 (+ exempt contributions)</td><td>IRA limit or child's earned income, whichever is lower</td><td>None (gift-tax reporting above annual exclusion)</td></tr>
<tr><td>Free money</td><td>$1,000 seed (2025–2028 births), employer, charities</td><td>None</td><td>None</td></tr>
<tr><td>Tax on growth</td><td>Deferred; taxed as income when withdrawn</td><td>Tax-free if qualified</td><td>Taxed yearly (kiddie tax rules)</td></tr>
<tr><td>Investments</td><td>U.S. stock index funds only, ≤0.10% fees</td><td>Almost anything</td><td>Almost anything</td></tr>
<tr><td>Access</td><td>From the year the child turns 18</td><td>Contributions any time; earnings after 59½ (exceptions)</td><td>Child takes control at state age of majority (18–21)</td></tr>
<tr><td>Financial aid</td><td>Rules still developing</td><td>Retirement assets generally not reported on FAFSA</td><td>Counted as the student's asset</td></tr>
</tbody></table>
<p>Use the <a href="/trump-account-calculator/">calculator</a> to see the after-tax difference at different tax rates.</p>
"""
page("/trump-account-vs-custodial-roth-ira/", "Trump Account vs Custodial Roth IRA vs UTMA: Comparison Table",
     "Compare a Trump Account with a custodial Roth IRA and a UTMA/UGMA account: earned income rules, limits, taxes and access.",
     vroth, h1="Trump Account vs Custodial Roth IRA vs UTMA",
     faqs=[("Is a Roth IRA for kids better than a Trump Account?", "If your child has earned income, a custodial Roth IRA usually wins on taxes because qualified growth is tax-free. Many families can use both: the Trump Account for the free seed and non-earned money, the Roth for earned income."),
           ("Does a Trump Account count against FAFSA?", "Federal guidance on how Trump Accounts are treated for financial aid is still developing; check studentaid.gov before relying on any assumption.")],
     sources=[I4547, ("IRS: Retirement topics – IRA contribution limits", "https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-ira-contribution-limits")])

howto = """
<p class="lead"><strong>Short answer:</strong> since October 1, 2026 the Treasury has auto-enrolled eligible children. Download the official Trump Accounts app (or use the website), verify your identity, claim the account, and separately elect the $1,000 seed on Form 4547 if your child was born 2025–2028.</p>
<h2>Step-by-step</h2>
<ol>
<li><strong>Gather details:</strong> your name and identifying information, the child's legal name, Social Security number and date of birth, exactly as on Social Security records.</li>
<li><strong>Open the official channel:</strong> the Trump Accounts app (Apple App Store / Google Play) or the Trump Accounts website linked from trumpaccounts.gov. Beware of look-alike sites and texts; the SSA Inspector General warns of government-imposter scams.</li>
<li><strong>Verify your identity</strong> and your authority to manage the child's account.</li>
<li><strong>Claim and activate</strong> the account.</li>
<li><strong>Elect the $1,000 seed</strong> (born 2025–2028, U.S. citizen): submit Form 4547 and tick the pilot program contribution, via the app, the website, or your IRS Online Account.</li>
<li><strong>Optional:</strong> set up contributions (up to $5,000/yr) and ask your employer whether it offers Trump Account contributions.</li>
</ol>
<p>Who runs it: Treasury designated BNY as financial agent; Robinhood Securities is the brokerage provider and initial trustee (per the IRS FAQ). Help line: 866-USA-4547.</p>
<p>Got a rejection? See <a href="/form-4547-cp318-notice/">Form 4547 / CP318 fixes</a>.</p>
"""
page("/how-to-claim-trump-account/", "How to Claim a Trump Account (Auto-Enrolled Since Oct 2026): Step by Step",
     "How to claim your child's auto-enrolled Trump Account, elect the $1,000 seed on Form 4547, and avoid scams. Step-by-step guide.",
     howto, h1="How to Claim a Trump Account",
     ld={"@type": "HowTo", "name": "How to claim a Trump Account", "step": [
         {"@type": "HowToStep", "position": i + 1, "name": n, "text": t} for i, (n, t) in enumerate([
          ("Gather details", "Have your ID details and the child's legal name, SSN and date of birth matching SSA records."),
          ("Open the official app or website", "Use the Trump Accounts app or the website linked from trumpaccounts.gov."),
          ("Verify identity", "Verify your identity and authority to manage the account."),
          ("Claim and activate", "Complete the steps to claim and activate the account."),
          ("Elect the $1,000 seed", "If eligible, submit Form 4547 with the pilot program election."),
          ("Contribute (optional)", "Add up to $5,000 per year; check for employer contributions.")])]},
     faqs=[("Is Form 4547 required if my child was auto-enrolled?", "Not to open the account. You still need Form 4547 to request the $1,000 seed, and you must claim the account to manage it."),
           ("Is Form 4547 a real IRS form?", "Yes. The IRS confirms Form 4547, Trump Account Election(s), is an official form."),
           ("Who is the custodian of Trump Accounts?", "The IRS FAQ says Treasury designated BNY as financial agent and Robinhood Securities as brokerage provider and initial trustee.")],
     sources=[IRS, IRSFAQ, GOV, ("SSA OIG scam alert on COLA/imposters", "https://oig.ssa.gov/scam-alerts/2026-10-21-social-security-2027-cola-announced-beneficiaries-are-not-the-only-ones-looking-forward-to-the-cola/")])

cp = """
<p class="lead"><strong>Short answer:</strong> Notice CP318 means the IRS could not complete or process your Trump Account election, most often because a name, SSN or date of birth does not match Social Security records. Fix the data and resubmit Form 4547 as the notice instructs. Do <em>not</em> file Form 1040-X.</p>
<h2>Common causes and fixes</h2>
<table><thead><tr><th>Cause</th><th>What to check / do</th></tr></thead><tbody>
<tr><td>Child's name, SSN or DOB mismatch</td><td>Compare with the Social Security card/record exactly (suffixes, hyphens, recent name changes). Resubmit Form 4547 per the notice.</td></tr>
<tr><td>Your (responsible party's) details don't match IRS records</td><td>Use the same legal name, SSN/ITIN and DOB as on your tax return.</td></tr>
<tr><td>Account or election already exists</td><td>Another parent or guardian may already have elected; a child can have one funded Trump Account at a time. Claim the existing account in the app.</td></tr>
<tr><td>Missing or unreadable information</td><td>Common with forms filed alongside a tax return; resubmit electronically via the app, website or IRS Online Account.</td></tr>
<tr><td>Child outside the age window</td><td>The account must be established before the year the child turns 18.</td></tr>
</tbody></table>
<h2>What not to do</h2>
<ul><li>Don't file an amended return (1040-X) to fix Form 4547 — the IRS says not to.</li>
<li>Don't expect IRS phone agents to correct the election; the IRS says they cannot. For account changes after claiming, the program line is 866-USA-4547.</li>
<li>Don't give SSNs to anyone who contacts you first by text or phone.</li></ul>
"""
page("/form-4547-cp318-notice/", "IRS Notice CP318 / Form 4547 Rejected: What It Means and How to Fix It",
     "Got IRS Notice CP318 or 'unable to process' on Form 4547 for a Trump Account? Common causes, fixes, and what not to do.",
     cp, h1="Form 4547 Rejected or Notice CP318: How to Fix It",
     faqs=[("Why did I get Notice CP318?", "The IRS needs more action to complete or correct a Trump Account election, typically due to missing or mismatched information."),
           ("Should I file Form 1040-X to fix Form 4547?", "No. The IRS says not to; follow the CP318 instructions and resubmit Form 4547."),
           ("Can the IRS fix my election by phone?", "The IRS says its customer service representatives cannot correct the election by phone or help claim the account.")],
     sources=[IRSFAQ, I4547])

chk = """
<p class="lead"><strong>Short answer:</strong> if your child has a valid SSN and is under 18, the Treasury has probably opened one automatically (auto-enrollment began October 1, 2026). To confirm, use the official Trump Accounts app or website: the IRS says you can check there whether an account has been established and then claim it. You may also get a Treasury letter if your child may qualify for the $1,000 contribution.</p>
<h2>How to check, step by step</h2>
<ol><li>Install the <strong>Trump Accounts</strong> app from the Apple App Store or Google Play, or go to the website linked from <a href="https://trumpaccounts.gov/">trumpaccounts.gov</a>.</li>
<li>Verify your identity and your authority over the child.</li>
<li>Enter the child's legal name, SSN and date of birth exactly as on Social Security records. If an account exists, you will be able to claim and activate it.</li>
<li>Born 2025–2028? Separately elect the $1,000 seed (Form 4547) — auto-enrollment does not elect it for you.</li>
<li>Born 2016–2024? Check whether the Dell $250 was deposited (see the <a href="/trump-account-eligibility-checker/">eligibility checker</a>).</li></ol>
<h2>Is the Trump Account app legit?</h2>
<p>The IRS's own Trump Accounts page tells parents to download the Trump Accounts app from the Apple App Store or Google Play to claim an account, and its FAQ names BNY as Treasury's financial agent and Robinhood Securities as brokerage provider and initial trustee. So the official app is real — but scammers imitate it. Safe habits:</p>
<ul><li>Start from irs.gov/trumpaccounts or trumpaccounts.gov, not from a text, email or ad link.</li>
<li>No one from the program needs you to pay a fee to receive the $1,000 or $250.</li>
<li>Don't give an SSN to anyone who contacts you first. The official help line is 866-USA-4547 (866-872-4547).</li></ul>
"""
page("/does-my-child-have-a-trump-account/", "How Do I Know If My Child Has a Trump Account? (Auto-Enrollment 2026)",
     "Check whether your child was auto-enrolled in a Trump Account, how to claim it, and whether the Trump Accounts app is legit.",
     chk, h1="How Do I Know If My Child Has a Trump Account?",
     faqs=[("How do I know if my child has a Trump Account?", "Use the official Trump Accounts app or website; the IRS says it lets you check whether an account was established for your child and begin claiming it. Since October 1, 2026 eligible children have been auto-enrolled."),
           ("Is the Trump Account app legit?", "Yes, the IRS directs parents to the Trump Accounts app on the Apple App Store and Google Play. Reach it from irs.gov/trumpaccounts or trumpaccounts.gov to avoid imitations."),
           ("Does auto-enrollment include the $1,000?", "No. You must still elect the $1,000 pilot contribution on Form 4547 if your child qualifies."),
           ("Do I have to put money in?", "No. Contributions are optional; the account can hold just the seed or Dell gift.")],
     sources=[IRS, IRSFAQ, GOV])

rules = """
<p class="lead">All the key Trump Account numbers in one place, with links to the IRS and statute.</p>
<table><thead><tr><th>Rule</th><th>2026 value</th></tr></thead><tbody>
<tr><td>Legal basis</td><td>Internal Revenue Code § 530A (2025 tax law, signed July 4, 2025)</td></tr>
<tr><td>Contributions allowed from</td><td>July 4, 2026</td></tr>
<tr><td>Automatic enrollment</td><td>Eligible children auto-enrolled from October 1, 2026; parents must claim the account</td></tr>
<tr><td>Annual limit (family, others, employer)</td><td>$5,000 per child; indexed to inflation after 2027</td></tr>
<tr><td>Employer limit</td><td>$2,500 per employee per year, excluded from the employee's income, counts toward $5,000</td></tr>
<tr><td>Exempt from the limit</td><td>$1,000 Treasury seed, qualified general contributions (governments, 501(c)(3) charities), rollovers</td></tr>
<tr><td>Treasury seed</td><td>$1,000 one-time, U.S. citizens born Jan 1, 2025 – Dec 31, 2028, by election on Form 4547</td></tr>
<tr><td>Eligible investments</td><td>Mutual funds/ETFs tracking the S&amp;P 500 or another broad index of primarily U.S. companies; no leverage; fees ≤ 0.10%; no sector funds</td></tr>
<tr><td>Growth period ends</td><td>December 31 of the year before the child turns 18</td></tr>
<tr><td>Withdrawals</td><td>Generally none before Jan 1 of the year the child turns 18 (exceptions: full rollover, certain ABLE rollovers, death); then traditional IRA rules</td></tr>
<tr><td>Tax deduction for contributions</td><td>None during the growth period</td></tr>
<tr><td>Basis</td><td>Family/other contributions create basis (not taxed again); seed, charity, employer money and growth are taxable when withdrawn</td></tr>
<tr><td>Program operators</td><td>BNY (financial agent), Robinhood Securities (brokerage/initial trustee), per IRS FAQ</td></tr>
</tbody></table>
"""
page("/trump-account-rules/", "Trump Account Rules 2026: Limits, Investments, Withdrawals and Taxes",
     "Every Trump Account rule in one table: $5,000 limit, $2,500 employer cap, $1,000 seed, eligible index funds, withdrawal age and taxation.",
     rules, h1="Trump Account Rules (2026)",
     faqs=[("Can a Trump Account invest in individual stocks or crypto?", "No. During the growth period it can only hold eligible mutual funds or ETFs tracking a broad U.S. equity index, with no leverage and fees of 0.10% or less."),
           ("Do contributions to a Trump Account reduce my taxes?", "No federal deduction is allowed for contributions before the year the child turns 18. Employer contributions up to $2,500 are excluded from the employee's income."),
           ("What happens at 18?", "The account generally becomes subject to traditional IRA rules and belongs to the child.")],
     sources=[USC, I4547, IRSNEWS, IRSFAQ])

# trust pages
page("/about/", f"About {SITE}", f"Who runs {SITE}, how the calculators work, and how we source Trump Account information.",
     f"""<p>{SITE} publishes free calculators and plain-English explanations of Trump Accounts (Internal Revenue Code § 530A). Every rule we state links to a primary source: the IRS, the statute, Treasury/IRS guidance or the program operators.</p>
<h2>Editorial policy</h2><ul><li>Primary sources first; each page lists its sources and its last-updated date.</li><li>Calculators show their formula and assumptions. Projections are illustrations, not forecasts.</li><li>No paid placements inside answers. If we ever use affiliate links, they will be labeled.</li><li>Corrections: email <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>; we fix verified errors promptly and update the date.</li></ul>
<h2>Author</h2><p>Written by {AUTHOR}. Finance graduate-level training; not a CPA, attorney or registered investment adviser. Nothing here is personalized tax, legal or investment advice.</p>""", h1=f"About {SITE}")
page("/contact/", f"Contact {SITE}", f"How to contact {SITE} with corrections or questions.",
     f"<p>Email: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a></p><p>We can't give individual tax advice or help access anyone's account. For account help use the official line 866-USA-4547 or trumpaccounts.gov. Never send us SSNs or account numbers.</p>", h1="Contact")
page("/privacy/", "Privacy Policy", f"{SITE} privacy policy: calculators run in your browser; cookies and advertising disclosures.",
     f"""<p>Last updated {UPDATED_H}.</p><h2>Calculator data</h2><p>All calculations run in your browser. We do not receive or store the numbers you type.</p>
<h2>Advertising and cookies</h2><p>We may show ads served by Google and partners. Third-party vendors, including Google, use cookies to serve ads based on prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on visits to this and/or other sites. You can opt out of personalized advertising at <a href="https://www.google.com/settings/ads">Google Ads Settings</a> or <a href="https://www.aboutads.info/choices/">aboutads.info</a>. Visitors in the EEA/UK will be asked for consent where required.</p>
<h2>Analytics</h2><p>We may use privacy-friendly aggregate analytics (page views, referrers). No personal data is sold.</p>
<h2>Affiliate links</h2><p>Some links may be affiliate links; we may earn a commission at no cost to you. They are labeled.</p>
<h2>Contact</h2><p><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>""", h1="Privacy Policy")
page("/disclaimer/", "Disclaimer", "Educational information only; not tax, legal or investment advice.",
     "<p>Content and calculators on this site are for education only and are not tax, legal or investment advice. Rules can change and IRS regulations for Trump Accounts are partly proposed, not final. Investment returns are not guaranteed and index funds can lose value. Consult a qualified professional and the official sources (IRS, trumpaccounts.gov) before acting. This site is independent and not affiliated with any government agency or the account providers.</p>", h1="Disclaimer")

# ---------- assets ----------
A = OUT / "assets"; A.mkdir(parents=True, exist_ok=True)
shutil.copy(ROOT / "src" / "style.css", A / "style.css")
shutil.copy(ROOT / "src" / "calc.js", A / "calc.js")
shutil.copy(ROOT / "src" / "elig.js", A / "elig.js")

# 404
(OUT / "404.html").write_text(f'<!doctype html><html lang=en><meta charset=utf-8><title>Not found – {SITE}</title><link rel=stylesheet href=/assets/style.css><main><h1>Page not found</h1><p><a href="/">Go to the Trump Account calculator</a></p></main></html>')

# robots.txt – explicitly welcome search + AI crawlers
bots = ["Googlebot", "Bingbot", "GPTBot", "OAI-SearchBot", "ChatGPT-User", "PerplexityBot", "Perplexity-User", "ClaudeBot", "Claude-User", "Claude-SearchBot",
        "Google-Extended", "Applebot", "Applebot-Extended", "CCBot", "DuckDuckBot", "Amazonbot", "meta-externalagent", "MistralAI-User"]
robots = "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n"
(OUT / "robots.txt").write_text(robots)

# sitemap
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
     "".join(f"  <url><loc>{BASE}{p}</loc><lastmod>{UPDATED}</lastmod></url>\n" for p, *_ in PAGES) + "</urlset>\n"
(OUT / "sitemap.xml").write_text(sm)

# llms.txt + llms-full.txt
desc = {p: d for p, t, d, _ in PAGES}
core = [p for p, *_ in PAGES if p not in ("/about/", "/contact/", "/privacy/", "/disclaimer/")]
llms = f"# {SITE}\n\n> {TAGLINE}. Independent, free, no sign-up. Every rule links to IRS/Treasury primary sources. Last updated {UPDATED}.\n\n" \
       f"Author: {AUTHOR} ({BASE}/about/). Not affiliated with the IRS or Treasury.\n\nKey facts: {strip(DEF)}\n\n## Tools and guides\n\n" + \
       "".join(f"- [{t}]({BASE}{p}): {d}\n" for p, t, d, _ in PAGES if p in core) + \
       "\n## About\n\n" + "".join(f"- [{t}]({BASE}{p}): {d}\n" for p, t, d, _ in PAGES if p not in core) + \
       f"\n## Optional\n\n- [Full text of all pages]({BASE}/llms-full.txt)\n"
(OUT / "llms.txt").write_text(llms)
full = f"# {SITE} – full text\n\nSource: {BASE}/ · Updated {UPDATED}\n\n" + "\n\n".join(
    f"## {t}\nURL: {BASE}{p}\n\n" + " ".join(b.split()) for p, t, d, b in PAGES)
(OUT / "llms-full.txt").write_text(full)

# IndexNow key file
(OUT / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY)
# Netlify/Cloudflare Pages style headers (harmless elsewhere)
(OUT / "_headers").write_text("/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n/llms*.txt\n  Content-Type: text/plain; charset=utf-8\n")
print(f"Built {len(PAGES)} pages to {OUT} for {BASE}")
