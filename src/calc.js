(function(){
 var $=function(i){return document.getElementById(i)},f=function(x){return '$'+Math.round(x).toLocaleString('en-US')};
 function num(id,lo,hi){var v=parseFloat($(id).value);if(isNaN(v))v=0;return Math.min(hi,Math.max(lo,v));}
 function run(){
  var age=Math.round(num('age',0,17)),emp=num('emp',0,2500),fam=Math.min(num('fam',0,5000),5000-emp),
      r=num('ret',-5,15)/100,fee=num('fee',0,0.1)/100,to=Math.round(num('to',18,65)),tax=num('tax',0,50)/100,inf=num('inf',0,10)/100;
  var b=($('seed').checked?1000:0)+($('dell').checked?250:0),put=b,basis=0,rows=[];
  for(var a=age;a<to;a++){var c=a<18?fam+emp:0;b=(b+c)*(1+r-fee);put+=c;if(a<18)basis+=fam;rows.push([a+1,c,b]);}
  var taxable=Math.max(0,b-basis),pen=($('pen').checked&&to<59.5)?0.10:0,taxDue=taxable*(tax+pen),after=b-taxDue,real=b/Math.pow(1+inf,to-age);
  var capNote=(num('fam',0,1e9)+emp>5000)?'<p class=small>Family contribution reduced so family + employer stays within the $5,000 annual limit.</p>':'';
  $('out').innerHTML='<div>Projected balance at age '+to+'</div><div class=big>'+f(b)+'</div><ul>'+
   '<li>Total put in (incl. seed/gifts): '+f(put)+'</li><li>Investment growth: '+f(b-put)+'</li>'+
   '<li>In today\'s dollars ('+(inf*100).toFixed(1)+'% inflation): '+f(real)+'</li>'+
   '<li>Your after-tax basis (family money): '+f(basis)+'</li>'+
   '<li>Estimated tax'+(pen?' + 10% penalty':'')+' if all withdrawn at '+to+': '+f(taxDue)+'</li>'+
   '<li><strong>Estimated after-tax value: '+f(after)+'</strong></li></ul>'+capNote+
   '<p class=small>Illustration only; returns are not guaranteed. Contributions modeled at the start of each year until 18.</p>';
  var h='<table><thead><tr><th>Age</th><th>Added</th><th>Balance</th></tr></thead><tbody>';
  rows.forEach(function(x){h+='<tr><td>'+x[0]+'</td><td>'+f(x[1])+'</td><td>'+f(x[2])+'</td></tr>'});$('yy').innerHTML=h+'</tbody></table>';
 }
 document.addEventListener('DOMContentLoaded',function(){var fm=$('calc');if(!fm)return;fm.addEventListener('input',run);fm.addEventListener('change',run);run();});
})();
