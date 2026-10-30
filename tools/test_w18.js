#!/usr/bin/env node
// Dependencies: npm install --prefix /tmp/j3-node --cache /tmp/j3-npm-cache puppeteer-core jsdom
// Run: NODE_PATH=/tmp/j3-node/node_modules node tools/test_w18.js [--jsdom]
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const ids = ['wbal','wbas','wtake','wtax','wuse','wedu','whome','wage'];
const defaults = ['25000', '9000', '5000', '10', 'none', '0', '0', false];
// [name, changes by index, expected keep, expected 10% extra tax (optional, hard-coded)]
const cases = [
  ['Defaults', {}, 4360, 320],
  ['Empty fields', {0:'',1:'',2:'',3:''}, 0, 0],
  ['Empty balance', {0:''}, 0],
  ['Empty basis', {1:''}, 4000],
  ['Empty withdrawal', {2:''}, 0],
  ['Empty tax', {3:''}, 4680],
  ['Zero balance', {0:'0'}, 0],
  ['Basis > balance', {1:'50000'}, 5000],
  ['Take > balance', {2:'50000'}, 21800],
  ['Tax 0%', {3:'0'}, 4680],
  ['Tax 50%', {3:'50'}, 3080],
  ['Tax >50% clamped', {3:'99'}, 3080],
  ['Other exception (all covered)', {4:'other'}, 4680, 0],
  ['Age 59½+', {7:true}, 4680, 0],
  ['Age + home', {4:'home',7:true}, 4680, 0],
  ['Negative numbers', {0:'-100',1:'-100',2:'-100',3:'-10'}, 0],
  ['Negative basis', {1:'-100'}, 4000],
  ['Negative withdrawal', {2:'-100'}, 0],
  ['Negative tax', {3:'-10'}, 4680],
  ['Very large numbers', {0:'1e300',1:'1e299',2:'1e298',3:'1e200'}, 100000000],
  ['Large taxable withdrawal', {0:'1e300',1:'0',2:'1e298',3:'50'}, 40000000],
  // Split exceptions (IRS Topic 557 / Pub 590-B): only the covered part skips the 10%.
  ['First home $25k, no basis => 10% on $15k', {0:'30000',1:'0',2:'25000',3:'10',4:'home'}, 21000, 1500],
  ['First home $8k (under cap)', {0:'30000',1:'0',2:'8000',3:'10',4:'home'}, 7200, 0],
  ['First home $25k, $4k cap already used => 10% on $19k', {0:'30000',1:'0',2:'25000',3:'10',4:'home',6:'4000'}, 20600, 1900],
  ['First home, cap fully used', {0:'30000',1:'0',2:'25000',3:'10',4:'home',6:'10000'}, 20000, 2500],
  ['First home, used >cap clamped', {0:'30000',1:'0',2:'25000',3:'10',4:'home',6:'99999'}, 20000, 2500],
  ['First home pro-rata with basis', {0:'25000',1:'9000',2:'25000',3:'10',4:'home'}, 22440, 960],
  ['College $20k, costs $20k (no cap)', {0:'30000',1:'0',2:'20000',3:'10',4:'edu',5:'20000'}, 18000, 0],
  ['College $20k, costs $12k => 10% on $8k', {0:'30000',1:'0',2:'20000',3:'10',4:'edu',5:'12000'}, 17200, 800],
  ['College, costs empty => full 10%', {0:'30000',1:'0',2:'20000',3:'10',4:'edu',5:''}, 16000, 2000],
  ['College costs > withdrawal', {4:'edu',5:'50000'}, 4680, 0],
];
function inspect(ids, values, event) {
  if (values) ids.forEach((id,i) => {
    const el = document.getElementById(id);
    if(typeof values[i] === 'boolean') el.checked = values[i]; else el.value = values[i];
    el.dispatchEvent(new Event(event, {bubbles:true}));
  });
  const out = document.getElementById('wout');
  return {text:out.textContent, amounts:[out.querySelector('.big').textContent,
    out.querySelectorAll('.lbl')[1].textContent.match(/\$[\d,]+/)[0],
    ...Array.from(out.querySelectorAll('td:nth-child(2)'), el=>el.textContent)],
    rate:out.querySelectorAll('tr')[2].firstElementChild.textContent,
    eduHidden:document.getElementById('wedubox').hidden, homeHidden:document.getElementById('whomebox').hidden};
}
function expected(v) {
  const clamp = (s, hi) => Math.min(hi, Math.max(0, Number(s)||0));
  const balance = clamp(v[0],1e8), basis = Math.min(balance,clamp(v[1],1e8));
  const take = Math.min(balance,clamp(v[2],1e8)), rate = clamp(v[3],50);
  const free = balance ? take*basis/balance : 0, taxable = take-free;
  const use = v[4], exempt = v[7]||use==='other' ? take : use==='edu' ? Math.min(take,clamp(v[5],1e8))
    : use==='home' ? Math.min(take,10000-clamp(v[6],10000)) : 0;
  const income = taxable*rate/100, penalty = take ? taxable*(take-exempt)/take/10 : 0;
  return {amounts:[take-income-penalty,take,free,taxable,income,penalty]
    .map(n=>'$'+Math.round(n).toLocaleString('en-US')), rate, eduHidden:use!=='edu', homeHidden:use!=='home'};
}
async function main() {
  let browser, dom, evaluate, profile;
  const errors = [];
  try {
    if(process.argv.includes('--jsdom')) {
      const {JSDOM, VirtualConsole} = require('jsdom');
      const vc = new VirtualConsole();
      vc.on('jsdomError', e=>errors.push(e.message));
      vc.on('error', (...args)=>errors.push(args.join(' ')));
      // Load the actual built HTML, then execute its actual deferred calculator asset.
      const html = fs.readFileSync(path.join(root,'public/trump-account-withdrawal-rules/index.html'),'utf8');
      dom = new JSDOM(html, {runScripts:'outside-only',url:'http://127.0.0.1:8761/trump-account-withdrawal-rules/',virtualConsole:vc});
      dom.window.addEventListener('error', e=>errors.push(e.message));
      dom.window.eval(fs.readFileSync(path.join(root,'public/assets/w18.js'),'utf8'));
      evaluate = async (values,event)=>dom.window.eval(`(${inspect})(${JSON.stringify(ids)},${JSON.stringify(values)},${JSON.stringify(event)})`);
      console.log('Engine: jsdom (built HTML + built asset)');
    } else {
      const puppeteer = require('puppeteer-core');
      profile = fs.mkdtempSync('/tmp/j3-chrome-test-');
      browser = await puppeteer.launch({executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',headless:true,
        timeout:15000,userDataDir:profile,args:['--no-sandbox','--disable-gpu','--disable-dev-shm-usage']});
      const page = await browser.newPage();
      page.on('pageerror', e=>errors.push(e.message));
      page.on('console', m=>{if(m.type()==='error') errors.push(m.text()+' '+m.location().url);});
      await page.goto('http://127.0.0.1:8761/trump-account-withdrawal-rules/',{waitUntil:'networkidle0',timeout:15000});
      evaluate = (values,event)=>page.evaluate(inspect,ids,values,event);
      console.log('Engine: Chrome');
    }
    let failures = 0;
    console.log('| Case | Result | Keep | 10% tax |\n|---|---|---|---|');
    for(const [name, changes, net, pen] of cases) {
      const values = [...defaults];
      for(const [i,value] of Object.entries(changes)) values[i] = value;
      try {
        const want = expected(values);
        assert.equal(want.amounts[0], '$'+net.toLocaleString('en-US'));
        if(pen!==undefined) assert.equal(want.amounts[5], '$'+pen.toLocaleString('en-US'));
        // Check actual initial render before touching defaults; exercise both event handlers.
        const snapshots = name==='Defaults' ? [await evaluate(null,'input')] : [];
        for(const event of ['input','change']) snapshots.push(await evaluate(values,event));
        for(const actual of snapshots) {
          assert.doesNotMatch(actual.text,/NaN|Infinity|undefined/);
          assert.deepEqual(Array.from(actual.amounts),want.amounts);
          assert.equal(actual.rate,`Income tax at ${Math.round(want.rate)}%`);
          assert.equal(actual.eduHidden,want.eduHidden); assert.equal(actual.homeHidden,want.homeHidden);
        }
        console.log(`| ${name} | PASS | ${want.amounts[0]} | ${want.amounts[5]} |`);
      } catch(e) {failures++; console.log(`| ${name} | FAIL | ${e.message.replace(/\n/g,' ')} |`);}
    }
    assert.deepEqual(errors, [], 'Console/page errors');
    console.log(`Console/page errors: ${errors.length}; ${cases.length-failures}/${cases.length} cases passed.`);
    if(failures) process.exitCode = 1;
  } finally {
    if(dom) dom.window.close();
    if(browser) await browser.close();
    if(profile) fs.rmSync(profile,{recursive:true,force:true});
  }
}
main().catch(e=>{console.error(e);process.exitCode=1;});
