/* KidAccountMath share card: client-side only. No tracking, no third-party scripts, no cookies.
   calc.js calls window.KAMShare.update(state) after each result. */
(function(){
 var W=1080,H=1350,BG='#faf8f4',INK='#1f2328',MUTED='#575d66',ACC='#c4512b',ACCD='#a8421f',SOFT='#fdf0ea',LINE='#e7e2da',TEAL='#0f6b63';
 var FONT='system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans","DejaVu Sans",sans-serif';
 var $=function(i){return document.getElementById(i)},S=null,timer=0,blob=null,objURL='';
 function money(x){return '$'+Math.round(x).toLocaleString('en-US')}
 function pct(x){return (Math.round(x*1000)/10).toString()}
 // Query string that reproduces the result. Only non-default extras are added to keep links short.
 function query(s){
  var q='age='+s.age+'&amt='+s.fam+'&r='+pct(s.r);
  if(!s.seed)q+='&seed=0'; if(s.dell)q+='&dell=1'; if(s.emp)q+='&emp='+s.emp; if(s.to!==18)q+='&to='+s.to;
  return q;
 }
 function shareURL(s){return location.origin+'/trump-account-calculator/?'+query(s)}
 function headline(s){return "Our kid's Trump Account could reach "+money(s.bal)+' by '+s.to}
 function assumptions(s){
  var a=['Starts at age '+s.age, money(s.fam+s.emp)+'/yr added', pct(s.r)+'% yearly return'];
  if(s.seed)a.push('$1,000 seed'); if(s.dell)a.push('Dell $250');
  return a.join(' · ');
 }
 function fit(ctx,text,weight,size,maxW){ctx.font=weight+' '+size+'px '+FONT;while(ctx.measureText(text).width>maxW&&size>20){size-=4;ctx.font=weight+' '+size+'px '+FONT;}return size}
 function rr(ctx,x,y,w,h,r){ctx.beginPath();ctx.moveTo(x+r,y);ctx.arcTo(x+w,y,x+w,y+h,r);ctx.arcTo(x+w,y+h,x,y+h,r);ctx.arcTo(x,y+h,x,y,r);ctx.arcTo(x,y,x+w,y,r);ctx.closePath()}
 function draw(s,canvas){
  canvas=canvas||document.createElement('canvas');canvas.width=W;canvas.height=H;
  var c=canvas.getContext('2d'),M=90,CW=W-2*M;
  c.fillStyle=BG;c.fillRect(0,0,W,H);
  c.fillStyle=ACC;c.fillRect(0,0,W,18);
  // brand
  rr(c,M,90,72,72,20);c.fillStyle=ACC;c.fill();
  c.strokeStyle='#fff';c.lineWidth=7;c.lineCap='round';c.lineJoin='round';c.beginPath();
  c.moveTo(M+18,M+52+0);c.lineTo(M+29,M+41);c.lineTo(M+38,M+48);c.lineTo(M+54,M+30);c.stroke();
  c.fillStyle=INK;c.font='800 44px '+FONT;c.textBaseline='middle';c.fillText('KidAccountMath',M+96,126);
  // main card
  rr(c,M,240,CW,760,40);c.fillStyle='#fff';c.fill();c.strokeStyle=LINE;c.lineWidth=3;c.stroke();
  c.textBaseline='alphabetic';c.textAlign='center';var cx=W/2;
  c.fillStyle=MUTED;c.font='600 50px '+FONT;c.fillText("Our kid's Trump Account",cx,370);
  c.fillText('could reach',cx,436);
  var big=money(s.bal),bs=fit(c,big,'800',200,CW-100);c.fillStyle=ACCD;c.fillText(big,cx,436+bs*1.0+40);
  var y=436+bs+40;
  c.fillStyle=INK;c.font='700 64px '+FONT;c.fillText('by age '+s.to,cx,y+110);
  rr(c,M+60,y+170,CW-120,4,2);c.fillStyle=SOFT;c.fill();
  var as=assumptions(s);fit(c,as,'500',34,CW-100);c.fillStyle=MUTED;c.fillText(as,cx,y+240);
  // footer band
  rr(c,M,1040,CW,120,30);c.fillStyle=SOFT;c.fill();
  c.fillStyle=ACCD;c.font='700 40px '+FONT;c.fillText('Estimate, not a guarantee',cx,1114);
  c.fillStyle=TEAL;c.font='700 44px '+FONT;c.fillText(location.host||'j6-cloude.github.io',cx,1240);
  c.fillStyle=MUTED;c.font='400 28px '+FONT;c.fillText('Free calculator · independent · not affiliated with the IRS or Treasury',cx,1292);
  return canvas;
 }
 function render(){
  if(!S)return;var cv=draw(S);
  cv.toBlob(function(b){blob=b;if(objURL)URL.revokeObjectURL(objURL);objURL=URL.createObjectURL(b);var im=$('shimg');if(im){im.src=objURL;im.hidden=false;}},'image/png');
 }
 function links(s){
  var u=shareURL(s),t=headline(s)+' (estimate). Try your own numbers:',e=encodeURIComponent;
  $('shfb').href='https://www.facebook.com/sharer/sharer.php?u='+e(u);
  $('shsms').href='sms:?&body='+e(t+' '+u);
  $('shwa').href='https://wa.me/?text='+e(t+' '+u);
  $('shurl').value=u;
 }
 function fname(){return 'trump-account-'+Math.round(S.bal)+'.png'}
 function download(){
  function go(){var a=document.createElement('a');a.href=objURL;a.download=fname();document.body.appendChild(a);a.click();a.remove();}
  if(blob)go();else draw(S).toBlob(function(b){blob=b;objURL=URL.createObjectURL(b);go();},'image/png');
 }
 function nativeShare(){
  var u=shareURL(S),t=headline(S)+' (estimate). Try your own numbers:';
  var data={title:'Trump Account estimate',text:t+' '+u,url:u};
  try{var f=new File([blob],fname(),{type:'image/png'});if(blob&&navigator.canShare&&navigator.canShare({files:[f]}))data.files=[f];}catch(e){}
  navigator.share(data).catch(function(){});
 }
 function copy(){
  var u=$('shurl').value,ok=function(){$('shcopy').textContent='Copied!';setTimeout(function(){$('shcopy').textContent='Copy link'},1800)};
  if(navigator.clipboard&&window.isSecureContext)navigator.clipboard.writeText(u).then(ok,function(){$('shurl').select();document.execCommand('copy');ok()});
  else{$('shurl').select();document.execCommand('copy');ok();}
 }
 function init(){
  var box=$('share');if(!box||box.dataset.ready)return;box.dataset.ready='1';box.hidden=false;
  $('shdl').addEventListener('click',download);$('shcopy').addEventListener('click',copy);
  if(navigator.share){$('shnat').hidden=false;$('shnat').addEventListener('click',nativeShare);}
 }
 window.KAMShare={
  update:function(s){S=s;init();links(s);blob=null;clearTimeout(timer);timer=setTimeout(render,350);},
  draw:draw,query:query,headline:headline,assumptions:assumptions,shareURL:shareURL
 };
})();
