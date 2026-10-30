(function(){
 var $=function(i){return document.getElementById(i)},f=function(x){return '$'+Math.round(x).toLocaleString('en-US')};
 function num(id,lo,hi){var v=parseFloat($(id).value);if(isNaN(v))v=0;return Math.min(hi,Math.max(lo,v));}
 var HOME_CAP=10000;
 function run(){
  var bal=num('wbal',0,1e8),bas=Math.min(num('wbas',0,1e8),bal),take=Math.min(num('wtake',0,1e8),bal),tax=num('wtax',0,50)/100,
      use=$('wuse').value,age=$('wage').checked,edu=num('wedu',0,1e8),used=num('whome',0,HOME_CAP);
  $('wedubox').hidden=use!=='edu';$('whomebox').hidden=use!=='home';
  // Part of the withdrawal covered by an exception (IRS Topic 557 / IRC 72(t)(2)).
  var exempt=age||use==='other'?take:use==='edu'?Math.min(take,edu):use==='home'?Math.min(take,HOME_CAP-used):0;
  var share=bal>0?bas/bal:0,taxfree=take*share,taxable=take-taxfree,inc=taxable*tax,
      hit=take>0?taxable*(take-exempt)/take:0,pen=hit*0.10,net=take-inc-pen,note;
  if(age)note=' (not owed: 59½+)';else if(exempt>=take&&take>0)note=' (not owed: exception covers it)';
  else if(exempt>0)note=' on '+f(hit)+' (only '+f(exempt)+' of the withdrawal is covered)';else note='';
  $('wout').innerHTML='<div class=lbl>You keep about</div><div class=big>'+f(net)+'</div><div class=lbl>of a '+f(take)+' withdrawal</div>'+
   '<table><tbody><tr><td>Tax-free part (family money already taxed)</td><td>'+f(taxfree)+'</td></tr>'+
   '<tr><td>Taxable part (seed, gifts, employer money, growth)</td><td>'+f(taxable)+'</td></tr>'+
   '<tr><td>Income tax at '+Math.round(tax*100)+'%</td><td>'+f(inc)+'</td></tr>'+
   '<tr><td>10% extra tax'+note+'</td><td>'+f(pen)+'</td></tr></tbody></table>'+
   '<p class=small>The tax-free share is spread across each withdrawal in proportion to the balance (pro-rata). We also spread the exception that way, which is the cautious reading; your real 10% may be a bit lower. College: only up to what you actually pay for qualified costs, minus costs paid with tax-free scholarships or grants. First home: $10,000 lifetime limit across all IRAs. A Trump Account is never combined with other IRAs for the pro-rata math. Estimate only; state tax not included.</p>';
 }
 ['wbal','wbas','wtake','wtax','wuse','wedu','whome','wage'].forEach(function(i){$(i).addEventListener('input',run);$(i).addEventListener('change',run);});
 run();
})();
