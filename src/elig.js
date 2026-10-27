(function(){
 var $=function(i){return document.getElementById(i)},Y='<span class="badge yes">Yes</span>',N='<span class="badge no">No</span>',M='<span class="badge maybe">Maybe</span>';
 function run(){
  var y=parseInt($('by').value,10),cit=$('cit').value==='1',ssn=$('ssn').value==='1',zip=$('zip').value,now=new Date().getFullYear(),out=[];
  var acct=ssn&&(y+18>now);
  out.push((acct?Y:N)+' <strong>Trump Account:</strong> '+(acct?'Eligible (needs a valid SSN; must be established before the year the child turns 18). If auto-enrolled, claim it in the official app.':(ssn?'Not eligible: the child turns 18 in or before this year.':'Requires a valid Social Security number.')));
  var seed=cit&&ssn&&y>=2025&&y<=2028;
  out.push((seed?Y:N)+' <strong>$1,000 Treasury seed:</strong> '+(seed?'Likely eligible. You must elect it on Form 4547 (app, website or IRS Online Account), even if the account was auto-opened.':'Only U.S. citizens with an SSN born Jan 1, 2025 – Dec 31, 2028.'));
  var dy=y>=2016&&y<=2024;
  out.push((dy&&zip==='1'?Y:dy&&zip==='u'?M:N)+' <strong>Dell $250:</strong> '+(!dy?'Only children born Jan 1, 2016 – Dec 31, 2024.':zip==='1'?'Likely received automatically (all deposits were made by Oct 9, 2026). Check the account in the official app.':zip==='u'?'Depends on ZIP code: median family income of $117,300 or less (Census 2020–2024 ACS), or living on a military base. Check your ZIP on <a href="https://investamerica.org/check-dell-250-eligibility/" rel="noopener">Invest America</a>.':'Probably not (ZIP above $117,300), unless your family enrolled before auto-enrollment began (Oct 1, 2026).')+' <span class=small>(Source: Invest America, as of Oct 9, 2026.)</span>');
  $('eout').innerHTML='<ul class="res">'+out.map(function(s){return '<li>'+s+'</li>'}).join('')+'</ul><p class=small>Guidance based on IRS and program announcements as of Oct 2026. Not an official determination; confirm in the official app.</p><p><a class="btn" href="/trump-account-calculator/">Next: see how much it could grow &rarr;</a></p>';
 }
 document.addEventListener('DOMContentLoaded',function(){var fm=$('elig');if(!fm)return;fm.addEventListener('input',run);fm.addEventListener('change',run);run();});
})();
