# Extra guides (added 2026-10-28). Executed inside build.py, so page(), table(), money(), project() and sources exist.
HC = ("Trump Accounts Help Center (official program support, linked from IRS.gov)", "https://trumpaccount.com/us/en/support/")
HC_OV = ("Trump Accounts Help Center: overview and FAQ", "https://trumpaccount.com/us/en/support/articles/overview/")
HC_CF = ("Trump Accounts Help Center: contributions FAQ", "https://trumpaccount.com/us/en/support/articles/contributions-faq/")
HC_MC = ("Trump Accounts Help Center: make a contribution", "https://trumpaccount.com/us/en/support/articles/make-a-contribution/")
HC_INV = ("Trump Accounts Help Center: investing FAQ", "https://trumpaccount.com/us/en/support/articles/investing-faq/")
HC_TAX = ("Trump Accounts Help Center: tax documents FAQ", "https://trumpaccount.com/us/en/support/articles/tax-documents-faq/")
HC_CLAIM = ("Trump Accounts Help Center: claim an account", "https://trumpaccount.com/us/en/support/articles/claim-an-account/")
HC_4547 = ("Trump Accounts Help Center: complete the claim form (Form 4547) and 'unable to process'", "https://trumpaccount.com/us/en/support/articles/form-4547/")
HC_CLOSE = ("Trump Accounts Help Center: how to close or transfer an account", "https://trumpaccount.com/us/en/support/articles/account-closure/")
N2568 = ("IRS Notice 2025-68 (Trump account guidance)", "https://www.irs.gov/pub/irs-drop/n-25-68.pdf")
TREGS = ("Federal Register: Trump Accounts temporary regulations (Sept 30, 2026)", "https://www.federalregister.gov/documents/2026/09/30/2026-20026/trump-accounts")
TC557 = ("IRS Topic 557: 10% additional tax on early IRA distributions (exceptions)", "https://www.irs.gov/taxtopics/tc557")
RP2625 = ("IRS Rev. Proc. 2026-25: gift tax safe harbor for Trump account contributions", "https://www.irs.gov/pub/irs-drop/rp-26-25.pdf")
RP2625N = ("IRS news release: safe harbor for certain Trump account contributions", "https://www.irs.gov/newsroom/treasury-irs-provide-safe-harbor-for-certain-contributions-to-trump-accounts-under-the-working-families-tax-cuts")
S128 = ("26 U.S.C. § 128 (employer contributions)", "https://uscode.house.gov/us/usc/119-124/t26/s128/")
PR128 = ("IRS news release: proposed regulations on employer contributions (Aug 11, 2026)", "https://www.irs.gov/newsroom/treasury-irs-issue-proposed-regulations-on-employer-contributions-to-trump-accounts-under-the-working-families-tax-cuts")
FR128 = ("Federal Register: proposed regulations under sections 128 and 129 (Aug 11, 2026)", "https://www.federalregister.gov/documents/2026/08/11/2026-16314/")
SB0602 = ("Treasury: employer contributions guidance and corporate commitments (Aug 11, 2026)", "https://home.treasury.gov/news/press-releases/sb0602")
PSCA = ("PSCA / Retirement Learning Center: Trump Accounts and FAFSA (Oct 13, 2026)", "https://www.psca.org/news/psca-news/2026/10/case-of-the-week-trump-accounts-and-fafsa/")
CNBC = ("CNBC: how Trump Account assets may affect college aid (Jul 9, 2026)", "https://www.cnbc.com/2026/07/09/trump-accounts-college-financial-aid.html")
SPYM = ("State Street: SPDR Portfolio S&P 500 ETF (SPYM) fact sheet", "https://www.ssga.com/us/en/individual/etfs/state-street-spdr-portfolio-sp-500-etf-spym")
TREAS_TABLE = '<p class=small>Source: Treasury and IRS, Table 3 in the <a href="https://www.federalregister.gov/documents/2026/09/30/2026-20026/trump-accounts" rel="noopener">temporary regulations</a> (Sept 30, 2026). Based on a broad U.S. stock index for birth cohorts 1926 to 2006 (gross market returns, before fees). Past returns do not predict future returns.</p>'
T3 = [("At birth", 2980, 6180, 13800), ("1", 2860, 5690, 11990), ("2", 2680, 4920, 10040), ("3", 2400, 4750, 9030), ("4", 2150, 4260, 8040),
      ("5", 2020, 3990, 7110), ("6", 1770, 3620, 6350), ("7", 1660, 3280, 5380), ("8", 1680, 3150, 4670), ("9", 1480, 2740, 4110),
      ("10", 1350, 2460, 3560), ("11", 1340, 2350, 3040), ("12", 1180, 2050, 2720), ("13", 1050, 1890, 2390), ("14", 1020, 1630, 2060),
      ("15", 990, 1400, 1810), ("16", 970, 1240, 1590), ("17", 900, 1160, 1330)]
def t3(rows=None):
    rs = [r for r in T3 if rows is None or r[0] in rows]
    return table([(r[0], money(r[1]), money(r[2]), money(r[3])) for r in rs],
                 ["$1,000 added at age", "Bad case (10th percentile)", "Typical (median)", "Good case (90th percentile)"])

NEXT.update({
 "/trump-account-withdrawal-rules/": ("/trump-account-taxes/", "See how each dollar is taxed", "Which money is tax-free and which is taxed at 18."),
 "/trump-account-taxes/": ("/trump-account-withdrawal-rules/", "Estimate tax on a withdrawal", "Plug in a balance and see what you keep."),
 "/trump-account-rollover/": ("/trump-account-withdrawal-rules/", "See the rules at 18", "What changes the year your child turns 18."),
 "/trump-account-grandparents/": ("/trump-account-calculator/", "See what a monthly gift grows to", "Try $25 or $50 a month from a grandparent."),
 "/trump-account-employer-contributions/": ("/trump-account-calculator/", "Add employer money to the calculator", "Open Advanced options and enter the employer amount."),
 "/trump-account-fafsa/": ("/trump-account-vs-529/", "Compare with a 529 plan", "529s get better aid and tax treatment for college."),
 "/trump-account-investment-options/": ("/trump-account-calculator/", "Run your own growth numbers", "Pick a return and see the value at 18."),
 "/trump-account-older-kids/": ("/trump-account-calculator/", "Try your child's age", "Enter the age and a monthly amount."),
 "/trump-account-pros-and-cons/": ("/how-to-claim-trump-account/", "Claim the account (free)", "Step by step, in the official app."),
 "/trump-account-app-problems/": ("/form-4547-cp318-notice/", "Fix a CP318 notice", "What the IRS letter means and how to resubmit."),
 "/trump-account-deadlines/": ("/trump-account-eligibility-checker/", "Check if my child qualifies", "Takes 30 seconds."),
})

# 1. Withdrawal rules / what happens at 18
W18_FORM = """
<form id="w18" class="calc card" onsubmit="return false">
 <div class="grid">
  <label for="wbal">Balance at 18 ($) <input type="number" inputmode="numeric" id="wbal" min="0" step="100" value="25000"></label>
  <label for="wbas">Family money put in ($) <input type="number" inputmode="numeric" id="wbas" min="0" step="100" value="9000"></label>
  <label for="wtake">Amount to take out ($) <input type="number" inputmode="numeric" id="wtake" min="0" step="100" value="5000"></label>
  <label for="wtax">Child's income tax rate (%) <input type="number" inputmode="numeric" id="wtax" min="0" max="50" step="1" value="10"></label>
 </div>
 <label class="chk"><input type="checkbox" id="wex"> Used for college costs or a first home (up to $10,000) or another IRS exception</label>
 <label class="chk"><input type="checkbox" id="wage"> Child is 59½ or older</label>
 <div id="wout" class="out" aria-live="polite"><noscript>The calculator needs JavaScript. See the worked example below.</noscript></div>
</form>
<script src="/assets/w18.js" defer></script>"""
ex_bal = 25000; ex_bas = 9000; ex_take = 5000
ex_free = ex_take * ex_bas / ex_bal; ex_taxable = ex_take - ex_free
wr = f"""
<p class="lead"><strong>Short answer:</strong> no one can take money out before the year your child turns 18. Then the account turns into a normal traditional IRA in your child's name. Your child, not you, controls it. They can take money out, but part of it is taxed as income. Most withdrawals before age 59½ also owe a 10% extra tax. Some uses skip that 10%, like college costs or a first home (up to $10,000).</p>
<div class="card"><strong>Key facts</strong><ul>
<li>Last year to add money: the year your child turns 17 (by Dec 31).</li>
<li>From Jan 1 of the year they turn 18: IRA rules apply.</li>
<li>At 18 your child signs in and takes control. You lose access.</li>
<li>If no one ever claimed the account, it still becomes your child's IRA. The money is not lost.</li></ul></div>
<h2>Withdrawal tax calculator</h2>
{W18_FORM}
<h2>Worked example</h2>
<p>Say the account holds {money(ex_bal)} at 18. Family put in {money(ex_bas)} of their own (already-taxed) money. Your child takes out {money(ex_take)} for rent, at a 10% tax rate.</p>
{table([("Tax-free part (" + f"{ex_bas/ex_bal:.0%}" + " of the account is family money)", money(ex_free)), ("Taxable part", money(ex_taxable)), ("Income tax at 10%", money(ex_taxable*0.10)), ("10% extra tax (rent is not an exception)", money(ex_taxable*0.10)), ("Kept", money(ex_take - ex_taxable*0.2))], ["", "Amount"])}
<p class=small>If the same {money(ex_take)} paid for college, the 10% extra tax would not apply and your child would keep {money(ex_take - ex_taxable*0.1)}. The tax-free share follows the IRA pro-rata rule. A Trump Account is never combined with your child's other IRAs for this rule (Notice 2025-68).</p>
<h2>What can come out before 18?</h2>
<p>Almost nothing. During the growth period the law allows only these moves:</p>
<ul><li>A rollover of the <em>whole</em> balance to another Trump Account provider (trustee to trustee).</li>
<li>A rollover to an ABLE account (for a child with a disability) in the year the child turns 17.</li>
<li>Return of money put in over the $5,000 limit.</li>
<li>Payment after the child's death.</li></ul>
<p>There is no hardship or emergency withdrawal before 18, unlike some other IRAs.</p>
<h2>Which uses skip the 10% extra tax after 18?</h2>
<p>The usual IRA exceptions apply. Common ones: qualified higher-education costs, up to $10,000 (lifetime) for a first home, and a few more listed by the IRS in Topic 557. Income tax still applies to the taxable part. See the full list at the IRS link below.</p>
<h2>What happens if my child leaves it alone?</h2>
<p>It keeps growing tax-deferred, like any IRA. After 18 your child can add more only under normal IRA rules, which need earned income (a job).</p>
"""
page("/trump-account-withdrawal-rules/", "Trump Account Withdrawal Rules: What Happens at 18 (Tax Calculator)",
     "When can money come out of a Trump Account, who controls it at 18, how withdrawals are taxed, and which uses skip the 10% penalty. Free calculator.",
     wr, h1="Trump Account Withdrawal Rules: What Happens at 18",
     ld={"@type": "WebApplication", "name": "Trump Account withdrawal tax calculator", "url": BASE + "/trump-account-withdrawal-rules/", "applicationCategory": "FinanceApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}},
     faqs=[("When can my child withdraw money from a Trump Account?", "Starting January 1 of the year the child turns 18. Before that, withdrawals are not allowed except for a full rollover, an ABLE rollover in the year the child turns 17, removing excess contributions, or death."),
           ("Who controls a Trump Account at 18?", "The child. The account becomes a traditional IRA in their name; they set up their own login and the parent (responsible party) loses access."),
           ("Is there a penalty for withdrawing from a Trump Account?", "After 18, the taxable part of a withdrawal before age 59½ generally owes a 10% additional tax unless an IRS exception applies, such as qualified higher-education costs or up to $10,000 for a first home. Income tax applies to the taxable part either way."),
           ("Can you contribute to a Trump Account after 18?", "Not as a Trump Account. Contributions stop after December 31 of the year the child turns 17. After the account becomes a traditional IRA, the child can add money only under normal IRA rules, which require earned income."),
           ("What happens if nobody claims the account?", "It stays invested. At 18 it converts to a traditional IRA in the child's name and the child verifies their identity to take control.")],
     sources=[HC_OV, HC_CF, HC_CLAIM, N2568, TREGS, TC557, USC])

# 2. Taxes
tx_rows = []
for fam in (0, 600, 1200):
    b, c, basis, _ = project(0, True, False, fam, 0, 0.07, 0.0003, 18)
    tx_rows.append((("$0" if fam == 0 else money(fam/12) + "/month"), money(b), money(basis), money(b - basis)))
tx = f"""
<p class="lead"><strong>Short answer:</strong> a Trump Account is <strong>tax-deferred, not tax-free</strong>. You get no tax deduction for what you put in. No one pays tax on the growth each year. When money comes out (age 18 or later), the growth is taxed as your child's income. The money family put in is not taxed again.</p>
<div class="card"><strong>Each kind of money, in one line</strong><ul>
<li><strong>Family money:</strong> no deduction going in; tax-free coming out.</li>
<li><strong>The $1,000 seed and charity gifts:</strong> taxed as income coming out.</li>
<li><strong>Employer money:</strong> not taxed to you going in (up to $2,500); taxed coming out.</li>
<li><strong>Growth:</strong> not taxed each year; taxed coming out.</li></ul></div>
<h2>Tax treatment table</h2>
{table([("Family, friends, the child", "No", "Yes (basis)", "No"), ("Treasury $1,000 seed", "n/a", "No", "Yes"), ("Charity or state gifts (qualified general contributions)", "n/a", "No", "Yes"), ("Employer (§128, up to $2,500 per employee)", "Excluded from employee's income tax", "No", "Yes"), ("Investment growth", "Not taxed yearly", "No", "Yes")], ["Money source", "Tax break going in?", "Tax-free coming out?", "Taxed as income when withdrawn?"])}
<h2>Example: how much would be taxable at 18?</h2>
{table(tx_rows, ["Family adds", "Value at 18", "Tax-free (family basis)", "Taxable when withdrawn"])}
<p class=small>Newborn with the $1,000 seed, 7% yearly return before a 0.03% fee, deposits at the start of each year until 17. Illustration only.</p>
<h2>Tax forms</h2>
<ul><li><strong>Form 5498-TA:</strong> sent each year for each account that got contributions. It is for your records; you generally do not file it.</li>
<li><strong>Form 1099-R:</strong> only if money comes out (for example, an excess contribution is returned).</li>
<li>No 1099-DIV or 1099-INT. Dividends inside the account are not taxed each year, so there is no kiddie tax on them.</li>
<li><strong>Form 4547:</strong> the election form to open an account or get the $1,000. It is not a tax bill.</li></ul>
<h2>Other tax points</h2>
<ul><li>You cannot count a deposit made in early 2027 toward 2026. Every deposit counts for the calendar year it is made.</li>
<li>Gifts from relatives can need a gift tax return only in rare cases. See <a href="/trump-account-grandparents/">grandparents and gift tax</a>.</li>
<li>Keep records of what family put in. That is the basis your child will not pay tax on later.</li></ul>
"""
page("/trump-account-taxes/", "Are Trump Accounts Tax-Free? Deductions, Taxable Money and Tax Forms (2026)",
     "Trump Account taxes explained: no deduction, no yearly tax, what is taxed at withdrawal, basis, and Forms 5498-TA, 1099-R and 4547.",
     tx, h1="Trump Account Taxes: What Is Taxed and When",
     faqs=[("Are Trump Account contributions tax deductible?", "No. Personal contributions from parents, relatives or friends are not deductible. Employer contributions up to $2,500 per employee are excluded from the employee's income instead."),
           ("Is a Trump Account tax-free?", "No. It is tax-deferred. Earnings are not taxed each year, but earnings, the $1,000 seed, employer money and charity gifts are taxed as ordinary income when withdrawn. Family contributions (basis) come out tax-free."),
           ("What tax form do I get for a Trump Account?", "Form 5498-TA each year the account gets contributions, and Form 1099-R only if a permitted distribution is made. You generally do not need to file Form 5498-TA with your return."),
           ("Do I have to report Trump Account earnings on my child's tax return each year?", "No. Earnings stay tax-deferred inside the account, and the account does not issue 1099-DIV or 1099-INT."),
           ("Can I make a Trump Account contribution for last year?", "No. Contributions count toward the limit for the calendar year in which they are made.")],
     sources=[HC_TAX, HC_INV, N2568, I4547, USC])

# 3. Rollover
ro_ex = []
for bal, bas in ((20000, 0), (20000, 8000), (40000, 15000)):
    ro_ex.append((money(bal), money(bas), money(bal - bas), money((bal - bas) * 0.12), money((bal - bas) * 0.22)))
ro = f"""
<p class="lead"><strong>Short answer:</strong> before 18, you can only move the <em>whole</em> account to a new Trump Account firm. Or, in the year your child turns 17, to an ABLE account. You can't move it to a 529 or a Roth IRA. You can't move a 529 into it, either. At 18 it is a normal IRA. Then your child can move it to any IRA firm. They can also switch it to a Roth IRA and pay tax on the taxable part.</p>
<h2>What moves are allowed, by age</h2>
{table([("Move to another Trump Account provider", "Yes, whole balance, trustee to trustee (when other providers exist)", "Yes (it is an IRA)"),
        ("Move to an ABLE account", "Only in the year the child turns 17", "IRA rules"),
        ("Move to a 529 plan", "No", "No direct rollover"),
        ("Convert to a Roth IRA", "No", "Yes; taxable part is taxed as income"),
        ("Roll to an IRA at Fidelity, Vanguard, Schwab etc.", "No (unless that firm becomes a Trump Account trustee)", "Yes"),
        ("Move a 529, UTMA or custodial IRA <em>into</em> it", "No", "No (IRA rules apply to new money)"),
        ("Have two Trump Accounts with money", "No; only one at a time", "n/a")],
       ["Move", "Before 18 (growth period)", "From the year the child turns 18"])}
<h2>Can you switch away from Robinhood?</h2>
<p>Robinhood Securities is the first trustee. The rules allow a trustee-to-trustee move of the full balance to another approved Trump Account trustee. The official help center says this is available "when available," so for now there may be no other provider to move to. A move gives the account a new number; it does not reset any rules.</p>
<h2>Roth conversion after 18: tax estimate</h2>
<p>Converting moves money from the traditional IRA into a Roth IRA. Your child pays income tax now on the taxable part (seed, employer money, growth). After that, qualified Roth growth is tax-free. The family basis is not taxed again.</p>
{table(ro_ex, ["Balance converted", "Family basis", "Taxable amount", "Tax at 12%", "Tax at 22%"])}
<p class=small>Simple estimate of federal tax on a full conversion. A low-income year (for example, a college year with little pay) means a lower rate. The 10% early-withdrawal tax does not apply to a direct conversion. Check current IRS rules or a tax pro before acting.</p>
"""
page("/trump-account-rollover/", "Trump Account Rollover: Roth IRA, ABLE, 529 and Switching Providers",
     "Can a Trump Account be rolled over to a Roth IRA, IRA, ABLE account or 529? The rules before and after 18, plus a Roth conversion tax table.",
     ro, h1="Trump Account Rollover Rules",
     faqs=[("Can a Trump Account be converted to a Roth IRA?", "Not before 18. From the year the child turns 18 it follows traditional IRA rules, which include Roth conversions; the taxable part of the converted amount is taxed as ordinary income."),
           ("Can I roll a Trump Account into a 529?", "No. The only rollovers allowed during the growth period are a full transfer to another Trump Account and an ABLE rollover in the year the child turns 17."),
           ("Can I roll a 529 or custodial IRA into a Trump Account?", "No. The official help center says 529 plans and custodial IRAs cannot be rolled into a Trump Account, and ACATS transfers are not supported."),
           ("Can I move my child's Trump Account to Fidelity or Vanguard?", "Only to another approved Trump Account trustee, and only the whole balance. After 18 it is a traditional IRA and can be moved to any IRA provider."),
           ("Can my child have two Trump Accounts?", "Only one Trump Account with money in it at a time.")],
     sources=[N2568, TREGS, HC_OV, HC_CLOSE, I4547])

# 4. Grandparents
gp = []
for mo in (25, 50, 100):
    for age in (0, 5):
        b, *_ = project(age, False, False, mo * 12, 0, 0.07, 0.0003, 18)
        gp.append((money(mo) + "/month", "newborn" if age == 0 else f"age {age}", money(mo * 12 * (18 - age)), money(b)))
gpb = f"""
<p class="lead"><strong>Short answer:</strong> yes. Grandparents, aunts, uncles and friends can all add money. The parent who manages the account sends them a link or QR code from the app. They pay by bank account or debit card. Checks are not accepted. Everyone shares one limit: <strong>$5,000 per child per year</strong> in total.</p>
<h2>How a grandparent adds money</h2>
<ol><li>The parent claims the account first. Gifts cannot go in before that.</li>
<li>The parent opens the child's account in the app, taps the QR code icon, then <em>Share link</em>, and sends it by text or email.</li>
<li>The grandparent opens the link and pays from a bank account or debit card. Bank transfers take up to 5 business days; debit cards are usually instant.</li></ol>
<p>Only the parent (the responsible party) can log in. Grandparents cannot see the balance in the app.</p>
<h2>Can a grandparent open the account?</h2>
<p>Sometimes. Form 4547 lists who may open an account: a legal guardian first, then a parent, then an adult sibling, then a grandparent. In most families the parent claims it. Only one person can manage it, and the first to finish the claim gets control.</p>
<h2>The $5,000 limit is shared</h2>
<p>If parents add $3,000 and a grandparent adds $2,500, the app declines anything past $5,000 for that year. Employer money also counts. The $1,000 Treasury seed and charity gifts do not count.</p>
<h2>What a monthly gift could grow to</h2>
{table(gp, ["Grandparent gives", "Starting", "Total given by 18", "Value at 18 (7%)"])}
<p class=small>7% yearly return before a 0.03% fee, deposits at the start of each year. Not guaranteed. Try your own numbers in the <a href="/trump-account-calculator/">calculator</a>.</p>
<h2>Gift tax: do grandparents need to file?</h2>
<p>Usually not. IRS Rev. Proc. 2026-25 gives a safe harbor. A cash gift to a Trump Account counts as a normal gift under the yearly exclusion ($19,000 per person in 2026) if all your gifts to that grandchild in the year stay at or under $19,000 and you do not otherwise have to file a gift tax return. If you give more than $19,000 to that grandchild in total, you file Form 709 and the Trump Account gifts must be reported too.</p>
<h2>Is it a good gift?</h2>
<p>It grows untaxed until 18, and the grandparent's money becomes basis, so it comes out tax-free later. The trade-offs: it is locked until 18, then the grandchild controls it. For college, a 529 may be better. See <a href="/trump-account-vs-529/">Trump Account vs 529</a> and <a href="/trump-account-fafsa/">FAFSA effects</a>.</p>
"""
page("/trump-account-grandparents/", "Can Grandparents Contribute to a Trump Account? How-To, Limits and Gift Tax",
     "How grandparents and relatives add money to a Trump Account (link or QR code), the shared $5,000 limit, gift tax rules, and what a monthly gift could grow to.",
     gpb, h1="Can Grandparents Contribute to a Trump Account?",
     ld={"@type": "HowTo", "name": "How a grandparent contributes to a Trump Account", "step": [
         {"@type": "HowToStep", "position": 1, "name": "Parent claims the account", "text": "The parent or guardian claims the child's account in the official Trump Accounts app or website."},
         {"@type": "HowToStep", "position": 2, "name": "Parent shares a contribution link", "text": "In the child's account, tap the QR code icon, then Share link, and send it by text or email."},
         {"@type": "HowToStep", "position": 3, "name": "Grandparent pays electronically", "text": "Open the link and contribute from a bank account or debit card. Checks are not accepted."}]},
     faqs=[("Can grandparents contribute to a Trump Account?", "Yes. Anyone can contribute once the account is claimed. The parent shares a contribution link or QR code from the app, and the grandparent pays by bank account or debit card."),
           ("How much can a grandparent put in a Trump Account?", "All contributors together can add up to $5,000 per child per year (2026), including any employer money. Contributions over the limit are declined."),
           ("Can grandparents open a Trump Account?", "A grandparent is on the list of authorized individuals in the Form 4547 instructions, after a legal guardian, parent and adult sibling. Only one person can be the responsible party."),
           ("Do grandparents have to file a gift tax return?", "Generally no. Under Rev. Proc. 2026-25, cash Trump Account gifts are treated as present-interest gifts if the donor's total gifts to that grandchild for the year are no more than the $19,000 annual exclusion (2026) and no gift tax return is otherwise required."),
           ("Can I mail a check to a Trump Account?", "No. The official help center says checks are not accepted; contributions are made electronically.")],
     sources=[HC_MC, HC_CF, HC_OV, I4547, RP2625, RP2625N])

# 5. Employer contributions
emp_rows = [(money(2500), "12%", money(300)), (money(2500), "22%", money(550)), (money(2500), "24%", money(600))]
em = f"""
<p class="lead"><strong>Short answer:</strong> an employer can put up to <strong>$2,500 a year</strong> into your children's Trump Accounts without it counting as income for you. The $2,500 is per worker, not per child. It counts toward each child's $5,000 limit. Over 50 companies have said they will offer it. Ask HR if yours does.</p>
<h2>The rules in plain words</h2>
<ul><li><strong>Limit:</strong> $2,500 per employee per year, in total for all your kids. It rises with inflation after 2027.</li>
<li><strong>Tax:</strong> left out of your federal income tax. Proposed IRS rules say it still counts as wages for Social Security and Medicare (FICA) tax unless another rule excludes it.</li>
<li><strong>Your own pay:</strong> an employer can let you put part of your pay in before tax through a cafeteria (Section 125) plan, but only for your dependent's account, not your own.</li>
<li><strong>Later:</strong> employer money is taxed as your child's income when withdrawn. It does not create basis.</li>
<li><strong>Plan needed:</strong> the employer must have a separate written plan, give notices and send yearly statements.</li>
<li><strong>Self-employed?</strong> Owners such as sole proprietors and partners can set up a plan for staff but cannot use it themselves (proposed rules).</li></ul>
<h2>Companies that announced contributions</h2>
<p>Treasury's August 11, 2026 release quoted these companies:</p>
{table([("Visa", "Company match of the government's $1,000 contribution"), ("State Street", "Will match the Treasury contribution"), ("Franklin Templeton", "Matching the government's contribution for eligible children of U.S. employees"), ("Vanguard", "Crew members can direct a $1,500 employer contribution to an eligible Trump Account"), ("Chime", "Employee match for Trump Accounts"), ("Kraken", "Sponsoring a Trump Account for every child born in Wyoming in 2026"), ("ADP, Edward Jones", "Supportive statements; ADP plans payroll support for employer plans")], ["Company", "What Treasury's release says"])}
<p class=small>Details, start dates and eligibility vary; check your benefits portal. The official help center says employer contributions in the app are "coming soon."</p>
<h2>How much does it save?</h2>
{table(emp_rows, ["Employer puts in", "Your federal tax bracket", "Federal income tax you avoid"])}
<p class=small>Compared with getting the same $2,500 as taxable pay. Federal income tax only; FICA still applies under the proposed rules. Your child pays tax later on withdrawal.</p>
<h2>If you have two kids</h2>
<p>The $2,500 cap covers both. The employer could put $1,250 in each, or $2,500 in one. Each child's own $5,000 cap still applies to everything added to that child.</p>
"""
page("/trump-account-employer-contributions/", "Trump Account Employer Contributions: $2,500 Rules and Companies Offering Them",
     "How employer Trump Account contributions work: $2,500 per employee, taxes, cafeteria-plan pre-tax option, and companies like Visa, State Street and Vanguard.",
     em, h1="Trump Account Employer Contributions",
     faqs=[("How much can an employer contribute to a Trump Account?", "Up to $2,500 per employee per year excluded from income, across all of the employee's children combined. It counts toward each child's $5,000 annual limit."),
           ("Are employer Trump Account contributions taxable?", "They are excluded from the employee's federal income (up to $2,500). Proposed regulations say they are still wages for FICA and FUTA unless another exclusion applies. They are taxed to the child when withdrawn."),
           ("Which companies match Trump Account contributions?", "Treasury's August 11, 2026 release cites Visa, State Street and Franklin Templeton matching the $1,000, Vanguard offering a $1,500 employer contribution, Chime offering a match, and Kraken sponsoring Wyoming babies born in 2026. Over 50 companies have committed."),
           ("Can I contribute pre-tax from my paycheck?", "Yes, if your employer adds Trump Account contributions to its Section 125 cafeteria plan, for your dependent's account (not your own)."),
           ("Is the $2,500 per child?", "No. It is per employee, so two children share one $2,500 exclusion.")],
     sources=[S128, N2568, PR128, FR128, SB0602, HC_TAX, HC_OV])

# 6. FAFSA
fa = f"""
<p class="lead"><strong>Short answer:</strong> no one knows yet. The U.S. Education Department has not said how to report a Trump Account on the FAFSA. FAFSA rules leave out retirement accounts like IRAs, and a Trump Account is legally a traditional IRA. So some experts think it will not count. Others think it will count as the student's money, which could cut need-based aid by up to 20% of the balance.</p>
<div class="card warn"><strong>Do not skip the free $1,000 over this.</strong> Even in the worst case, the aid you lose is smaller than the account itself.</div>
<h2>The two views</h2>
{table([("Not reported", "A Trump Account is a traditional IRA (IRC §408(a)). FAFSA instructions exclude retirement plans, including non-education IRAs.", "Kalman Chany (CNBC); Retirement Learning Center (PSCA, Oct 13, 2026)"),
        ("Reported as a student asset", "Student assets are assessed at 20% in the Student Aid Index.", "Mark Kantrowitz (CNBC, Jul 9, 2026)")], ["View", "Why", "Who says so"])}
<h2>Worst-case math</h2>
{table([(money(b), money(b * 0.20), money(b * 0.0564)) for b in (2500, 6000, 10000, 25000)], ["Account balance", "Lost aid if a 20% student asset", "For comparison: 5.64% (max rate on parent assets, e.g. a parent-owned 529)"])}
<p class=small>Rates from CNBC's July 9, 2026 report. Only affects need-based aid. If FAFSA treats it like other IRAs, the asset effect is $0.</p>
<h2>Withdrawals can count as income</h2>
<p>Taxable money taken out in college counts as the student's income on a later FAFSA, which can reduce aid. One planning idea quoted by CNBC: wait to withdraw until Jan 1 of the student's sophomore year, so the income falls outside the years FAFSA looks at. Check this against current FAFSA rules before acting.</p>
<h2>What to do now</h2>
<ul><li>Claim the account and the $1,000 if eligible.</li>
<li>If college is the main goal for extra savings, a parent-owned <a href="/trump-account-vs-529/">529 plan</a> gets better aid and tax treatment.</li>
<li>Watch studentaid.gov for Trump Account guidance. We will update this page when it appears.</li></ul>
"""
page("/trump-account-fafsa/", "Does a Trump Account Affect FAFSA and Financial Aid? (2026)",
     "Will a Trump Account reduce college financial aid? What FAFSA rules say about IRAs, the 20% student-asset worst case, and what to do now.",
     fa, h1="Does a Trump Account Affect FAFSA?",
     faqs=[("Does a Trump Account count on the FAFSA?", "Federal Student Aid has not issued guidance yet. Because a Trump Account is a traditional IRA, current FAFSA instructions excluding non-education IRAs suggest it may not be reported, but this is unconfirmed."),
           ("How much financial aid could a Trump Account cost?", "If it were treated as a student investment asset, up to 20% of the balance per year in need-based aid (for example, up to $2,000 on a $10,000 account), according to Mark Kantrowitz via CNBC."),
           ("Should I skip the $1,000 seed to protect financial aid?", "Experts quoted by CNBC say to claim it: in the worst case you would not lose more aid than the value of the account."),
           ("Do Trump Account withdrawals affect financial aid?", "Taxable withdrawals add to the student's income, which can reduce aid on a later FAFSA.")],
     sources=[PSCA, CNBC, N2568, ("Federal Student Aid (studentaid.gov)", "https://studentaid.gov/")])

# 7. Investment options
inv = f"""
<p class="lead"><strong>Short answer:</strong> right now all Trump Account money goes into one fund: <strong>SPYM</strong>, an S&amp;P 500 index fund. It holds about 500 large U.S. companies. You cannot pick another fund yet. The official help center says more choices are expected later. The fund fee is 0.02% a year (about $2 per $10,000). There is no account fee.</p>
<h2>The rules for what it can hold</h2>
<ul><li>Only mutual funds or ETFs that track a broad index of mostly U.S. stocks (like the S&amp;P 500).</li>
<li>No leverage. No single stocks, bonds, cash or crypto.</li>
<li>Fund fees of 0.10% or less.</li>
<li>Money is invested within about 1 business day. Dividends are reinvested.</li></ul>
<h2>Is the money safe?</h2>
<p>It is held in a trust account by a registered trustee. SIPC covers up to $500,000 if the broker fails. SIPC does <strong>not</strong> cover market losses. The account can drop in value, and the government does not guarantee it.</p>
<h2>How much has $1,000 grown in the past?</h2>
<p>Treasury and the IRS looked at U.S. stock returns for children born 1926 to 2006. This is what $1,000 put in at each age was worth at 18:</p>
{t3()}
{TREAS_TABLE}
<p>So for a newborn, the middle result was about 6 times the money. Even in a bad stretch (10th percentile) it nearly tripled. Money added at 17 had only one year, and in a bad year it lost value.</p>
<h2>What this means for you</h2>
<ul><li>Earlier money matters most. $1,000 at birth did far better than $1,000 at age 10.</li>
<li>You don't need to pick funds or time the market. There is one choice for now.</li>
<li>If your child will need the money right at 18, remember the last year can be a down year.</li></ul>
"""
page("/trump-account-investment-options/", "What Is a Trump Account Invested In? SPYM, Fees and Historical Returns",
     "Trump Account investment options: the SPYM S&P 500 fund, fees, the legal rules, SIPC, and Treasury's historical data on what $1,000 grew to by 18.",
     inv, h1="What Is a Trump Account Invested In?",
     ld={"@type": "Dataset", "name": "Value at 18 of $1,000 invested in a broad U.S. stock index, by age invested", "description": "Treasury/IRS Table 3 from the Trump Accounts temporary regulations (Sept 30, 2026), 10th/50th/90th percentiles over birth cohorts 1926-2006.", "creator": {"@type": "Organization", "name": "U.S. Department of the Treasury and IRS"}, "isBasedOn": TREGS[1]},
     faqs=[("What is a Trump Account invested in?", "All contributions are automatically invested in SPYM, an S&P 500 index ETF. There is no other option yet; more choices are expected for claimed accounts later."),
           ("Can I choose investments in a Trump Account?", "Not at this time. By law, options are limited to low-cost, unleveraged funds tracking a broad index of mainly U.S. stocks."),
           ("What are the fees on a Trump Account?", "No fee to claim or maintain the account. Funds may charge an expense ratio of at most 0.1%; SPYM's is 0.02%."),
           ("Can a Trump Account lose money?", "Yes. It is invested in stocks and not guaranteed by the government. SIPC protection does not cover market losses."),
           ("How much will $1,000 in a Trump Account be worth at 18?", "Treasury's historical data (birth cohorts 1926–2006) shows a median of about $6,180 for $1,000 invested at birth, with a 10th–90th percentile range of $2,980 to $13,800.")],
     sources=[HC_INV, HC_OV, HC_CLAIM, TREGS, N2568, SPYM])

# 8. Older kids
ok_rows = []
for age in (5, 8, 10, 12, 14, 16):
    b0, c0, *_ = project(age, False, False, 600, 0, 0.07, 0.0003, 18)
    b1, c1, *_ = project(age, False, False, 1200, 0, 0.07, 0.0003, 18)
    ok_rows.append((age, money(c0), money(b0), money(c1), money(b1)))
ok = f"""
<p class="lead"><strong>Short answer:</strong> yes, older kids get a Trump Account too. Any child under 18 with a Social Security number can have one. Treasury began opening them automatically on Oct 1, 2026. Older kids do <strong>not</strong> get the $1,000 (that is only for U.S. citizens born 2025 to 2028). Many kids born 2016 to 2024 got $250 from the Dell gift. Starting late still helps, but there are fewer years to grow.</p>
<h2>What an older child can get</h2>
{table([("2025–2028", "Yes", "Yes (if U.S. citizen and you elect it)", "No"), ("2016–2024", "Yes", "No", "Maybe $250, paid by Oct 9, 2026 in qualifying ZIP codes"), ("2009–2015", "Yes (born 2009: open it in 2026)", "No", "No")], ["Born", "Account", "$1,000 seed", "Dell $250"])}
<p class=small>An account must be set up before the year the child turns 18. In 2026 that means born in 2009 or later.</p>
<h2>How long can you add money?</h2>
<p>Only until Dec 31 of the year your child turns 17. A child who is 14 now has about 4 more years of deposits.</p>
<h2>Is it worth starting late? Real history</h2>
<p>Treasury's data on U.S. stocks (children born 1926–2006) shows what $1,000 added at each age was worth at 18:</p>
{t3(["8", "10", "12", "14", "16", "17"])}
{TREAS_TABLE}
<h2>Projection: monthly deposits from today</h2>
{table(ok_rows, ["Age now", "Put in by 18 at $50/mo", "Value at 18", "Put in by 18 at $100/mo", "Value at 18"])}
<p class=small>7% yearly return before a 0.03% fee, deposits at the start of each year, no seed or Dell gift. Not guaranteed.</p>
<h2>Is a Trump Account the best place for a teen's money?</h2>
<ul><li>If your teen has a job, a <a href="/trump-account-vs-custodial-roth-ira/">custodial Roth IRA</a> is usually better: growth can be tax-free.</li>
<li>If the money is for college in a few years, a <a href="/trump-account-vs-529/">529</a> is usually better.</li>
<li>A Trump Account still makes sense for employer money, charity gifts, and long-term money with no earned income.</li>
<li>At 18 your child controls it. Talk with them about leaving it invested.</li></ul>
"""
page("/trump-account-older-kids/", "Trump Accounts for Older Kids (Born 2009–2024): What They Get and Is It Worth It?",
     "Older kids can have a Trump Account but no $1,000. What children born 2009–2024 get, how long you can contribute, and Treasury data on late starts.",
     ok, h1="Trump Accounts for Older Kids",
     faqs=[("Can older kids get a Trump Account?", "Yes. Any child with a valid SSN can have one if it is set up before the year they turn 18. In 2026 that means children born in 2009 or later."),
           ("Do older kids get the $1,000?", "No. The $1,000 pilot contribution is only for U.S. citizens born January 1, 2025 through December 31, 2028."),
           ("What is the $250 for older kids?", "A private gift from Michael and Susan Dell for children born 2016–2024 in ZIP codes with median family income of $117,300 or less (or on military bases). It was deposited automatically by October 9, 2026."),
           ("Is it worth opening a Trump Account for a teenager?", "It can be, especially for employer or charity money, but a custodial Roth IRA (if the teen has earned income) or a 529 (for college) often has better tax treatment."),
           ("When do contributions stop?", "After December 31 of the year the child turns 17.")],
     sources=[HC_4547, HC_OV, TREGS, I4547, DELL])

# 9. Pros and cons
pc = f"""
<p class="lead"><strong>Short answer:</strong> it costs nothing to claim, and the $1,000 is free. So claim it. The catches come later. The money is locked until 18. Most of it is taxed when it comes out. At 18 your child gets full control. And for now there is just one fund.</p>
<h2>Pros</h2>
<ul><li><strong>Free money:</strong> $1,000 for U.S. citizens born 2025–2028. Possible employer, charity and state gifts.</li>
<li><strong>No fees</strong> to claim or keep it. The fund fee is 0.02% now (legal max 0.10%).</li>
<li><strong>No yearly tax</strong> on growth until money comes out.</li>
<li><strong>No earned income needed,</strong> unlike a custodial IRA.</li>
<li><strong>Simple:</strong> one low-cost S&amp;P 500 fund.</li>
<li><strong>Family money comes out tax-free</strong> (it is basis).</li></ul>
<h2>The catches (cons)</h2>
<ul><li><strong>Locked until 18.</strong> No emergency withdrawals.</li>
<li><strong>Tax-deferred, not tax-free.</strong> Growth, the seed and employer money are taxed as income later. Many withdrawals before 59½ also owe 10%.</li>
<li><strong>Your child controls it at 18.</strong> You cannot stop them from spending it.</li>
<li><strong>No contribution deduction</strong> for family money.</li>
<li><strong>One fund only</strong> for now, all in U.S. stocks. It can fall in value.</li>
<li><strong>Can't be closed</strong> once claimed (except in rare cases).</li>
<li><strong>First to claim wins.</strong> Between separated parents, whoever finishes the claim first manages it.</li>
<li><strong>FAFSA effect is unknown</strong> (see <a href="/trump-account-fafsa/">FAFSA guide</a>).</li>
<li><strong>Scams</strong> copy the program. Real notices come only from the official app, trumpaccount.com, or no-reply@trumpaccounts.treasury.gov.</li></ul>
<h2>Which account wins for which goal?</h2>
{table([("Claim the free $1,000 / employer money", "Trump Account"), ("Save for college", "529 plan (tax-free for school, better for aid)"), ("Teen has a job", "Custodial Roth IRA (tax-free growth)"), ("Money the child may need before 18", "Savings or UTMA account"), ("Long-term gift with no earned income", "Trump Account")], ["Goal", "Usually best"])}
<h2>Does it really grow?</h2>
<p>Treasury's own history check: $1,000 put in at birth in a broad U.S. stock index was worth $6,180 at 18 in the middle case and $2,980 in a bad (10th percentile) case, for children born 1926–2006. See <a href="/trump-account-investment-options/">investment options</a>.</p>
"""
page("/trump-account-pros-and-cons/", "Trump Account Pros and Cons: What's the Catch? (2026)",
     "Honest Trump Account pros and cons: the free $1,000, no fees and tax deferral vs the lock until 18, taxes on withdrawal, child control at 18 and FAFSA risk.",
     pc, h1="Trump Account Pros and Cons: What's the Catch?",
     faqs=[("What's the catch with Trump Accounts?", "The money is locked until 18, most of it (growth, seed, employer money) is taxed as income when withdrawn, the child controls it at 18, there is only one fund for now, and the financial aid treatment is not yet settled."),
           ("Is a Trump Account worth it?", "Claiming is free and the $1,000 seed (for eligible children) is free money, so claiming is generally worth it. Whether to add your own money depends on your goal: 529s are usually better for college and custodial Roth IRAs for teens with jobs."),
           ("Are there fees on Trump Accounts?", "There is no fee to claim or maintain the account. Funds may charge up to 0.1%; the current fund, SPYM, charges 0.02%."),
           ("Can I close a Trump Account?", "Once claimed it generally cannot be closed until 18, except in limited cases such as the child's death or an ABLE rollover."),
           ("Is the Trump Account a scam?", "No, the program is real and run under IRS and Treasury rules, but scammers imitate it. Real activation emails come only from no-reply@trumpaccounts.treasury.gov.")],
     sources=[HC_OV, HC_CLAIM, HC_INV, N2568, TREGS, CNBC])

# 10. App problems
ap = f"""
<p class="lead"><strong>Short answer:</strong> most claim errors come from a mismatch. The name, SSN or birth date you typed must match what the IRS and Social Security have on file, for you and your child. Fix it in your IRS online account, then send a new claim form. You need a photo ID and a live selfie to verify. Delays of a few days can be normal.</p>
<div class="card warn"><strong>Stay safe.</strong> The real app is "Trump Accounts" on the Apple App Store or Google Play, or trumpaccount.com. Activation emails come only from no-reply@trumpaccounts.treasury.gov. No one will ask for your password or a one-time code.</div>
<h2>Fixes by error message</h2>
{table([
 ("Can't verify my identity", "Have a valid government photo ID and good light for the live selfie. Use your legal name, SSN or ITIN and birth date exactly as on your tax return. If verification fails as the responsible party, sign in to your IRS online account, correct your election details, and submit a new claim form."),
 ("My child is ineligible / can't be verified", "Usually the child's name, SSN or birth date doesn't match your tax return or Social Security records. In your IRS online account go to My Elections, then Unable to Process, read the notice, correct it, and resubmit."),
 ("Child already has an account", "Only one account per child. Another parent or guardian may have claimed it first. The help center can't share who (tax privacy law). Talk to the co-parent, or contact support if you think it was not authorized."),
 ("Status says Processing", "Wait for the email from no-reply@trumpaccounts.treasury.gov. IRS processing usually takes 1–3 business days."),
 ("Child turns 18 this year", "Too late: the account must be opened before the year the child turns 18. This can't be overridden."),
 ("No SSN yet (newborn or parent)", "The child needs an SSN; you need an SSN or ITIN. Submit the claim form once you have them."),
 ("Forgot to elect the $1,000", "Not too late. Submit a new claim form with the pilot program election."),
 ("Started but didn't finish", "Your claim progress is saved. Sign back in with the same username and password. (The paper-style Form 4547 screens are not saved if you close before identity verification.)"),
 ("Deposit reversed or card declined", "Make sure the bank account has enough money; you get an email if a deposit is reversed, and many reversals can unlink the bank. A debit card must allow online purchases.")],
 ["Problem", "What to do"])}
<h2>Check your claim status</h2>
<ol><li>Sign in to your IRS online account with ID.me.</li>
<li>Go to <em>Forms</em>, then <em>Trump Accounts</em>.</li>
<li>Read the <em>Election status</em> table. "Unable to process" links to a notice that says why (see <a href="/form-4547-cp318-notice/">CP318 guide</a>).</li></ol>
<h2>App basics</h2>
<ul><li>Works on iOS 16 or newer, Android 7 or newer, and Chrome, Safari, Firefox and Edge.</li>
<li>Tablets may work but are not officially supported.</li>
<li>Only the responsible party can log in. There is no shared login yet.</li>
<li>One login can manage several children: use <em>Add child</em> in the account switcher.</li>
<li>For help, use the support pages in the app or at trumpaccount.com (linked from IRS.gov).</li></ul>
"""
page("/trump-account-app-problems/", "Trump Account App Problems: Can't Verify Identity, Login and 'Unable to Process' Fixes",
     "Fix common Trump Account app problems: identity verification fails, child ineligible or already claimed, processing status, login and bank transfer errors.",
     ap, h1="Trump Account App Problems and Fixes",
     faqs=[("Why can't the Trump Account app verify my identity?", "The most common cause is a mismatch between what you entered (legal name, SSN or ITIN, date of birth) and IRS records. Correct your election in your IRS online account and submit a new claim form. Verification needs a government photo ID and a live selfie."),
           ("Why does it say my child already has an account?", "Each child can have only one Trump Account, and the first eligible adult to complete the claim becomes the responsible party. Another parent or guardian may have claimed it."),
           ("How long does the Trump Account claim take?", "The official help center says IRS processing of the claim form takes 1–3 business days; you then get an email from no-reply@trumpaccounts.treasury.gov to finish claiming."),
           ("Is there a deadline to claim the Trump Account?", "No. Unclaimed accounts stay open and invested and become the child's traditional IRA at 18."),
           ("Can both parents log in?", "No. Only the responsible party can log in for now; read-only access for a trusted contact is planned.")],
     sources=[HC_4547, HC_CLAIM, HC_OV, HC_CF, IRSFAQ])

# 11. Deadlines and key dates
dl = f"""
<p class="lead"><strong>Short answer:</strong> there is <strong>no deadline to claim</strong> your child's account. The real cut-offs are about age: the account must be set up before the year your child turns 18, and deposits stop after Dec 31 of the year they turn 17. The $1,000 is for babies born from Jan 1, 2025 to Dec 31, 2028. You can elect it any time.</p>
<h2>Deadlines that matter for your family</h2>
{table([
 ("Claim the account", "No deadline", "Unclaimed accounts stay invested and become the child's IRA at 18"),
 ("Elect the $1,000 (Form 4547)", "No fixed date; file any time", "Child must be a U.S. citizen born Jan 1, 2025 – Dec 31, 2028"),
 ("Open an account", "Before Jan 1 of the year the child turns 18", "In 2026: children born 2009 or later"),
 ("Last deposit", "Dec 31 of the year the child turns 17", "Then nothing until it becomes an IRA"),
 ("ABLE rollover", "Only in the year the child turns 17", "For children with a disability"),
 ("Yearly $5,000 limit", "Resets each Jan 1", "Can't count a January deposit toward last year"),
 ("Withdrawals", "From Jan 1 of the year the child turns 18", "IRA rules and taxes apply")],
 ["What", "When", "Note"])}
<h2>Program timeline</h2>
{table([
 ("Jul 4, 2025", "Law signed creating Trump Accounts (IRC §530A)"),
 ("Dec 2, 2025", "IRS Notice 2025-68 gives first guidance"),
 ("Jun 30, 2026", "IRS online account starts taking Form 4547; gift-tax safe harbor (Rev. Proc. 2026-25)"),
 ("Jul 4, 2026", "Contributions open; app launches"),
 ("Aug 11, 2026", "Employer contribution rules proposed; 50+ companies commit"),
 ("Sep 30, 2026", "Temporary regulations published"),
 ("Oct 1, 2026", "Treasury starts opening accounts automatically for eligible children"),
 ("Oct 9, 2026", "Dell $250 deposits completed"),
 ("After 2027", "$5,000 and $2,500 limits start rising with inflation"),
 ("Dec 31, 2028", "Last birth date that qualifies for the $1,000")
],
 ["Date", "What happened / happens"])}
<p class=small>"Deadline June 30" searches refer to the date the IRS added online Form 4547 filing in 2026, not a deadline to sign up.</p>
"""
page("/trump-account-deadlines/", "Trump Account Deadlines and Key Dates (2025–2029): Is There a Deadline to Claim?",
     "Is there a deadline to claim a Trump Account or the $1,000? All the real cut-off dates by age, plus the full program timeline from 2025 to 2029.",
     dl, h1="Trump Account Deadlines and Key Dates",
     faqs=[("Is there a deadline to sign up for a Trump Account?", "No deadline to claim an account that was opened for your child. An account must be set up before the year the child turns 18."),
           ("Is there a deadline for the $1,000 Trump Account money?", "No fixed filing deadline was announced; the official help center says you can elect it any time. The child must be a U.S. citizen born January 1, 2025 through December 31, 2028."),
           ("What was the June 30 Trump Account date?", "June 30, 2026 is when the IRS let people file Form 4547 through their IRS online account and announced gift-tax relief. It was not a sign-up deadline."),
           ("When do Trump Account contributions stop?", "After December 31 of the year the child turns 17."),
           ("When did automatic enrollment start?", "Treasury began opening accounts automatically for eligible children on October 1, 2026. Parents still need to claim them.")],
     sources=[HC_CLAIM, HC_4547, N2568, TREGS, IRSNEWS, RP2625N, SB0602, DELL])
