(function(){
 var $=function(i){return document.getElementById(i)},f=function(x){return '$'+Math.round(x).toLocaleString('en-US')};
 function num(id,lo,hi){var v=parseFloat($(id).value);if(isNaN(v))v=0;return Math.min(hi,Math.max(lo,v));}
 function mark(){var v=$('fam').value;[].forEach.call(document.querySelectorAll('[data-fam]'),function(bt){bt.setAttribute('aria-pressed',bt.getAttribute('data-fam')===v?'true':'false')});}
 function run(){
  var age=Math.round(num('age',0,17)),emp=num('emp',0,2500),fam=Math.min(num('fam',0,5000),5000-emp),
      r=num('ret',-5,15)/100,fee=num('fee',0,0.1)/100,to=Math.round(num('to',18,65)),tax=num('tax',0,50)/100,inf=num('inf',0,10)/100;
  var b=($('seed').checked?1000:0)+($('dell').checked?250:0),put=b,basis=0,rows=[];
  for(var a=age;a<to;a++){var c=a<18?fam+emp:0;b=(b+c)*(1+r-fee);put+=c;if(a<18)basis+=fam;rows.push([a+1,c,b]);}
  var taxable=Math.max(0,b-basis),pen=($('pen').checked&&to<59.5)?0.10:0,taxDue=taxable*(tax+pen),after=b-taxDue,real=b/Math.pow(1+inf,to-age);
  var capNote=(num('fam',0,1e9)+emp>5000)?'<p class=small>Family contribution reduced so family + employer stays within the $5,000 annual limit.</p>':'';
  var gifts=($('seed').checked?' and the $1,000 seed':'')+($('dell').checked?' and the Dell $250':'');
  $('out').innerHTML='<div class=lbl>Your child could have about</div><div class=big>'+f(b)+'</div><div class=lbl>at age '+to+'</div>'+
   '<p class=sentence>Adding '+f(fam+emp)+' a year from age '+age+gifts+', earning '+(r*100).toFixed(1).replace(/\.0$/,'')+'% a year, turns '+f(put)+' of deposits into about '+f(b)+'. That includes '+f(b-put)+' of investment growth. Returns are not guaranteed.</p>'+
   '<details class=more><summary>More detail: tax, inflation</summary><ul>'+
   '<li>In today\'s dollars ('+(inf*100).toFixed(1)+'% inflation): '+f(real)+'</li>'+
   '<li>Your after-tax basis (family money): '+f(basis)+'</li>'+
   '<li>Estimated tax'+(pen?' + 10% penalty':'')+' if all withdrawn at '+to+': '+f(taxDue)+'</li>'+
   '<li><strong>Estimated after-tax value: '+f(after)+'</strong></li></ul></details>'+capNote+
   '<p class=small>Illustration only; returns are not guaranteed. Contributions modeled at the start of each year until 18.</p>';
  var h='<table><thead><tr><th>Age</th><th>Added</th><th>Balance</th></tr></thead><tbody>';
  rows.forEach(function(x){h+='<tr><td>'+x[0]+'</td><td>'+f(x[1])+'</td><td>'+f(x[2])+'</td></tr>'});$('yy').innerHTML=h+'</tbody></table>';
  if(window.KAMShare)KAMShare.update({age:age,fam:fam,emp:emp,r:r,to:to,seed:$('seed').checked,dell:$('dell').checked,bal:b});
 }
 // Pre-fill from a shared link, e.g. ?age=0&amt=1000&r=7 (optional: seed=0, dell=1, emp=500, to=30)
 function prefill(){
  var q=new URLSearchParams(location.search),m={age:'age',amt:'fam',r:'ret',emp:'emp',to:'to'},hit=false;
  Object.keys(m).forEach(function(k){var v=parseFloat(q.get(k));if(q.has(k)&&isFinite(v)){$(m[k]).value=v;hit=true;}});
  if(q.has('seed')){$('seed').checked=q.get('seed')!=='0';hit=true;}
  if(q.has('dell')){$('dell').checked=q.get('dell')==='1';hit=true;}
  if((q.has('emp')||q.has('to')||q.has('dell'))&&$('emp').closest)$('emp').closest('details').open=true;
  return hit;
 }
 document.addEventListener('DOMContentLoaded',function(){var fm=$('calc');if(!fm)return;fm.addEventListener('input',function(e){if(e.target.id==='fam')mark();run();});fm.addEventListener('change',run);
  [].forEach.call(fm.querySelectorAll('[data-fam]'),function(bt){bt.addEventListener('click',function(){$('fam').value=bt.getAttribute('data-fam');mark();run();});});var hit=prefill();mark();run();if(hit)$('out').scrollIntoView({block:'center'});});
})();
