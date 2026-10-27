(function(){
 var $=function(i){return document.getElementById(i)};
 function run(){
  var y=parseInt($('qby').value,10),now=new Date().getFullYear(),li=[],btn;
  var acct=y+18>now;
  if(!acct){li.push('<strong>No Trump Account:</strong> a child must be under 18 for the whole year the account is opened.');btn=['/trump-account-vs-custodial-roth-ira/','Compare other accounts for older kids'];}
  else{
   li.push('<strong>An account, opened for your child:</strong> children under 18 with a Social Security number were auto-enrolled from Oct 1, 2026. You still have to claim it.');
   if(y>=2025&&y<=2028){li.push('<strong>$1,000 from the Treasury</strong> if your child is a U.S. citizen with an SSN. It is not automatic: you elect it on Form 4547.');btn=['/how-to-claim-trump-account/','How to claim the account and the $1,000'];}
   else if(y>=2016&&y<=2024){li.push('<strong>Maybe $250 from Michael &amp; Susan Dell:</strong> paid automatically (by Oct 9, 2026) to kids in ZIP codes with median family income of $117,300 or less, or living on a military base.');btn=['/trump-account-eligibility-checker/','Check the Dell $250 for your ZIP'];}
   else{li.push('No $1,000 seed or Dell $250 for this birth year, but the family can add up to $5,000 a year.');btn=['/trump-account-calculator/','See how much it could grow'];}
  }
  $('qout').innerHTML='<ul class="res">'+li.map(function(s){return '<li>'+s+'</li>'}).join('')+'</ul><p><a class="btn" href="'+btn[0]+'">'+btn[1]+' &rarr;</a></p>';
 }
 document.addEventListener('DOMContentLoaded',function(){var s=$('qby');if(!s)return;s.addEventListener('change',run);run();});
})();
