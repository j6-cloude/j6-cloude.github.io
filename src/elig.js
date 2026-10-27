(function(){
 var $=function(i){return document.getElementById(i)};
 function run(){
  var y=parseInt($('by').value,10),cit=$('cit').value==='1',ssn=$('ssn').value==='1',zip=$('zip').value,now=new Date().getFullYear(),out=[];
  var acct=ssn&&(y+18>now);
  out.push((acct?'✅':'❌')+' <strong>Trump Account:</strong> '+(acct?'Eligible (needs a valid SSN; must be established before the year the child turns 18). If auto-enrolled, claim it in the official app.':(ssn?'Not eligible: the child turns 18 in or before this year.':'Requires a valid Social Security number.')));
  var seed=cit&&ssn&&y>=2025&&y<=2028;
  out.push((seed?'✅':'❌')+' <strong>$1,000 Treasury seed:</strong> '+(seed?'Likely eligible. You must elect it on Form 4547 (app, website or IRS Online Account), even if the account was auto-opened.':'Only U.S. citizens with an SSN born Jan 1, 2025 – Dec 31, 2028.'));
  var dy=y>=2016&&y<=2024;
  out.push((dy&&zip==='1'?'✅':dy&&zip==='u'?'❔':'❌')+' <strong>Dell $250:</strong> '+(!dy?'Only children born 2016–2024.':zip==='1'?'Likely received automatically.':zip==='u'?'Depends on ZIP code: median family income ≤ about $117,300 or living on a military base. Check Invest America\'s ZIP lookup.':'Probably not (ZIP above threshold), unless you signed up before auto-enrollment.'));
  $('eout').innerHTML='<ul style="list-style:none;padding:0">'+out.map(function(s){return '<li style="margin:.5rem 0">'+s+'</li>'}).join('')+'</ul><p class=small>Guidance based on IRS and program announcements as of Oct 2026. Not official determination.</p>';
 }
 document.addEventListener('DOMContentLoaded',function(){var fm=$('elig');if(!fm)return;fm.addEventListener('input',run);fm.addEventListener('change',run);run();});
})();
