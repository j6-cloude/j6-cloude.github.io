(function(){
 var $=function(i){return document.getElementById(i)},f=function(x){return '$'+Math.round(x).toLocaleString('en-US')};
 function num(id,lo,hi){var v=parseFloat($(id).value);if(isNaN(v))v=0;return Math.min(hi,Math.max(lo,v));}
 function run(){
  var bal=num('wbal',0,1e8),bas=Math.min(num('wbas',0,1e8),bal),take=Math.min(num('wtake',0,1e8),bal),tax=num('wtax',0,50)/100,
      ex=$('wex').checked,age=$('wage').checked;
  var share=bal>0?bas/bal:0,taxfree=take*share,taxable=take-taxfree,inc=taxable*tax,pen=(ex||age)?0:taxable*0.10,net=take-inc-pen;
  $('wout').innerHTML='<div class=lbl>You keep about</div><div class=big>'+f(net)+'</div><div class=lbl>of a '+f(take)+' withdrawal</div>'+
   '<table><tbody><tr><td>Tax-free part (family money already taxed)</td><td>'+f(taxfree)+'</td></tr>'+
   '<tr><td>Taxable part (seed, gifts, employer money, growth)</td><td>'+f(taxable)+'</td></tr>'+
   '<tr><td>Income tax at '+Math.round(tax*100)+'%</td><td>'+f(inc)+'</td></tr>'+
   '<tr><td>10% extra tax'+((ex||age)?' (not owed: exception or 59½+)':'')+'</td><td>'+f(pen)+'</td></tr></tbody></table>'+
   '<p class=small>The tax-free share is spread across each withdrawal in proportion to the balance (pro-rata). A Trump Account is never combined with other IRAs for this math. Estimate only; state tax not included.</p>';
 }
 ['wbal','wbas','wtake','wtax','wex','wage'].forEach(function(i){$(i).addEventListener('input',run);$(i).addEventListener('change',run);});
 run();
})();
