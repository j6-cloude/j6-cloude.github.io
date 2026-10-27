/* KidAccountMath celebration cards: client-side canvas PNGs. No tracking, no third-party scripts, no cookies, no storage.
   Two kinds: 'proj' (projection certificate, fed by calc.js via KAMShare.update) and 'claim' (self-declared "we claimed it" card).
   Design rule: festive + clearly unofficial. No seals, eagles, flags, signatures, serial numbers or agency styling. */
(function(){
 var W=1080,H=1350,
  C={bg:'#fff8ee',paper:'#fffdf8',ink:'#2a2320',muted:'#6b5f57',acc:'#c4512b',accd:'#9e3d1c',gold:'#e0a83a',goldd:'#b9811c',teal:'#0f6b63',pink:'#ee8f73',soft:'#fdf0ea'},
  SANS='system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans","DejaVu Sans",sans-serif',SERIF='Georgia,"Times New Roman","Noto Serif","DejaVu Serif",serif',
  EMO='"Apple Color Emoji","Segoe UI Emoji","Noto Color Emoji",sans-serif';
 var $=function(i){return document.getElementById(i)},S=null,KIND='proj',timer=0,blob=null,objURL='';
 function money(x){return '$'+Math.round(x).toLocaleString('en-US')}
 function pct(x){return (Math.round(x*1000)/10).toString()}
 function cleanName(n){return String(n||'').replace(/[\u0000-\u001f<>]/g,'').replace(/\s+/g,' ').trim().slice(0,20)}
 function nameOf(){var el=$('shname');return cleanName(el?el.value:'')}
 function poss(n){return /s$/i.test(n)?n+"'":n+"'s"}
 // light, fun tiers (by projected balance)
 var TIERS=[[100000,'Money Tree Legend','🌳','LEGEND'],[40000,'Growth Superstar','🚀','SUPERSTAR'],[15000,'Compound Interest Champion','🏆','CHAMPION'],[5000,'Little Saver Star','⭐','STAR'],[0,'Future Investor','🌱','INVESTOR']];
 function tier(b){for(var i=0;i<TIERS.length;i++)if(b>=TIERS[i][0])return TIERS[i];return TIERS[TIERS.length-1]}
 // ---- URLs / text ----
 function query(s,withName){
  var q='age='+s.age+'&amt='+s.fam+'&r='+pct(s.r);
  if(!s.seed)q+='&seed=0'; if(s.dell)q+='&dell=1'; if(s.emp)q+='&emp='+s.emp; if(s.to!==18)q+='&to='+s.to;
  var n=nameOf(); if(withName&&n)q+='&name='+encodeURIComponent(n);
  return q;
 }
 function incName(){var c=$('shincl');return !!(c&&c.checked)}
 function shareURL(){return KIND==='claim'?location.origin+'/trump-account-eligibility-checker/':location.origin+'/trump-account-calculator/?'+query(S,incName())}
 function shareText(){
  if(KIND==='claim')return "We claimed our kid's free $1,000 Trump Account seed! 🎉 Did you claim yours? Check free:";
  return "Our kid's Trump Account could reach "+money(S.bal)+' by '+S.to+' (estimate). Try your own numbers:';
 }
 function assumptions(s){
  var a=[money(s.fam+s.emp)+'/yr added', pct(s.r)+'% yearly return'];
  if(s.seed)a.push('$1,000 seed'); if(s.dell)a.push('Dell $250'); a.push('0.03% fee');
  return 'Assumes '+a.join(' · ');
 }
 // ---- canvas helpers ----
 function font(w,sz,fam){return w+' '+sz+'px '+(fam||SANS)}
 function fit(c,t,w,sz,max,fam){c.font=font(w,sz,fam);while(c.measureText(t).width>max&&sz>18){sz-=2;c.font=font(w,sz,fam);}return sz}
 function wrap(c,t,max){var ws=t.split(' '),ls=[],l='';ws.forEach(function(w){var x=l?l+' '+w:w;if(c.measureText(x).width>max&&l){ls.push(l);l=w}else l=x});if(l)ls.push(l);return ls}
 function rr(c,x,y,w,h,r){c.beginPath();c.moveTo(x+r,y);c.arcTo(x+w,y,x+w,y+h,r);c.arcTo(x+w,y+h,x,y+h,r);c.arcTo(x,y+h,x,y,r);c.arcTo(x,y,x+w,y,r);c.closePath()}
 function rng(seed){return function(){seed=(seed*16807)%2147483647;return (seed-1)/2147483646}}
 function star(c,x,y,r,col){c.save();c.translate(x,y);c.beginPath();for(var i=0;i<10;i++){var a=Math.PI/5*i-Math.PI/2,rad=i%2?r*.45:r;c.lineTo(Math.cos(a)*rad,Math.sin(a)*rad)}c.closePath();c.fillStyle=col;c.fill();c.restore()}
 function confetti(c,w,h,seed,n,avoid){
  var R=rng(seed),cols=[C.acc,C.gold,C.teal,C.pink,'#f2c14e','#7fb7a9'];
  for(var i=0;i<n;i++){
   var x=R()*w,y=R()*h;
   if(avoid&&x>avoid[0]&&x<avoid[2]&&y>avoid[1]&&y<avoid[3])continue;
   var col=cols[Math.floor(R()*cols.length)],k=R();c.save();c.translate(x,y);c.rotate(R()*Math.PI);c.globalAlpha=.75;c.fillStyle=col;
   if(k<.45)c.fillRect(-9,-4,18,8);else if(k<.75){c.beginPath();c.arc(0,0,5+R()*3,0,7);c.fill();}
   else if(k<.9){c.strokeStyle=col;c.lineWidth=4;c.beginPath();c.moveTo(-12,0);c.quadraticCurveTo(0,-10,12,0);c.stroke();}
   else{c.restore();star(c,x,y,9,col);continue;}
   c.restore();
  }
 }
 // scalloped rosette with two ribbon tails
 function rosette(c,x,y,r,label,emoji){
  c.save();
  [[-1,C.acc],[1,C.accd]].forEach(function(p){c.beginPath();var s=p[0];c.moveTo(x+s*r*.18,y+r*.4);c.lineTo(x+s*r*.75,y+r*1.75);c.lineTo(x+s*r*.42,y+r*1.55);c.lineTo(x+s*r*.28,y+r*1.9);c.lineTo(x-s*r*.12,y+r*.6);c.closePath();c.fillStyle=p[1];c.fill();});
  c.beginPath();var n=24;for(var i=0;i<=n*2;i++){var a=Math.PI*i/n,rad=i%2?r*.9:r;c.lineTo(x+Math.cos(a)*rad,y+Math.sin(a)*rad)}c.closePath();c.fillStyle=C.gold;c.fill();
  c.beginPath();c.arc(x,y,r*.76,0,7);c.fillStyle='#fff4dc';c.fill();c.lineWidth=5;c.strokeStyle=C.goldd;c.setLineDash([2,9]);c.stroke();c.setLineDash([]);
  c.textAlign='center';c.textBaseline='middle';c.font=font('400',r*.62,EMO);c.fillText(emoji,x,y-r*.12);
  c.fillStyle=C.accd;fit(c,label,'800',r*.2,r*1.3);c.fillText(label,x,y+r*.46);
  c.restore();
 }
 function frame(c,seed){
  c.fillStyle=C.bg;c.fillRect(0,0,W,H);
  confetti(c,W,H,seed,140,[70,70,W-70,H-70]);
  rr(c,48,48,W-96,H-96,34);c.fillStyle=C.paper;c.fill();c.lineWidth=10;c.strokeStyle=C.acc;c.stroke();
  rr(c,72,72,W-144,H-144,24);c.lineWidth=3;c.strokeStyle=C.gold;c.setLineDash([14,10]);c.stroke();c.setLineDash([]);
  [[100,100],[W-100,100],[100,H-100],[W-100,H-100]].forEach(function(p){star(c,p[0],p[1],20,C.gold)});
  // inner confetti only in text-free zones: strip above the headline + thin side gutters
  var R=rng(seed+7),cols=[C.acc,C.gold,C.teal,C.pink,'#f2c14e','#7fb7a9'];
  for(var i=0;i<30;i++){var x,y;if(i<14){x=150+R()*(W-300);y=100+R()*16;}else{x=(i%2?W-108:94)+R()*14;y=150+R()*(H-500);}
   var col=cols[Math.floor(R()*cols.length)],k=R();c.save();c.translate(x,y);c.rotate(R()*Math.PI);c.globalAlpha=.75;c.fillStyle=col;
   if(k<.5)c.fillRect(-8,-3.5,16,7);else{c.beginPath();c.arc(0,0,4+R()*2,0,7);c.fill();}c.restore();}
 }
 function banner(c,y,text){
  c.save();c.textAlign='center';c.textBaseline='middle';var sz=fit(c,text,'800',40,640),w=c.measureText(text).width+120,x=W/2-w/2;
  c.fillStyle=C.accd;[[x-46,x],[x+w+46,x+w]].forEach(function(p){c.beginPath();c.moveTo(p[1],y-26);c.lineTo(p[0],y-26);c.lineTo(p[0]+(p[0]<p[1]?22:-22),y+4);c.lineTo(p[0],y+34);c.lineTo(p[1],y+34);c.fill();});
  rr(c,x,y-34,w,68,12);c.fillStyle=C.acc;c.fill();c.fillStyle='#fff';c.font=font('800',sz);c.fillText(text,W/2,y+1);c.restore();
 }
 function footer(c,assume){
  c.textAlign='center';c.textBaseline='alphabetic';var cx=W/2,host=location.host||'j6-cloude.github.io';
  if(assume){c.fillStyle=C.muted;fit(c,assume,'500',28,W-240);c.fillText(assume,cx,H-302);
   c.fillStyle=C.accd;c.font=font('700',30);c.fillText('Estimate, not a guarantee',cx,H-260);}
  c.strokeStyle='#efdcc8';c.lineWidth=2;c.beginPath();c.moveTo(230,H-232);c.lineTo(W-230,H-232);c.stroke();
  c.fillStyle=C.ink;c.font=font('700',30);c.fillText('Awarded by KidAccountMath',cx,H-192);
  c.fillStyle=C.muted;c.font=font('400',25);c.fillText('(independent, not a government document)',cx,H-158);
  c.fillStyle=C.teal;c.font=font('800',30);c.fillText(host,cx,H-114);
 }
 function drawProj(s,c){
  var n=nameOf()||'Our little one',t=tier(s.bal),cx=W/2;frame(c,Math.round(s.bal)%997+11);
  c.textAlign='center';c.textBaseline='alphabetic';
  c.fillStyle=C.goldd;c.font=font('800',30);c.fillText('★  PROUD PARENT MOMENT  ★',cx,168);
  c.fillStyle=C.ink;fit(c,n,'700',92,W-260,SERIF);c.fillText(n,cx,268);
  c.fillStyle=C.muted;c.font=font('600',44);c.fillText('is on track for',cx,336);
  c.fillStyle=C.accd;fit(c,money(s.bal),'900',168,W-260);c.fillText(money(s.bal),cx,496);
  c.fillStyle=C.ink;c.font=font('800',54);c.fillText('by age '+s.to+'! 🎉',cx,576);
  rosette(c,cx,704,96,t[3],t[2]);
  banner(c,866,t[1]);
  c.fillStyle=C.teal;c.font=font('700',36);c.fillText('Started investing at age '+s.age,cx,966);
  footer(c,assumptions(s));
 }
 function drawClaim(c){
  var n=nameOf(),who=n?poss(n):"our little one's",cx=W/2,msg='We claimed '+who+' $1,000 Trump Account seed!';frame(c,4242);
  c.textAlign='center';c.textBaseline='alphabetic';
  c.fillStyle=C.goldd;c.font=font('800',30);c.fillText('★  ACHIEVEMENT UNLOCKED  ★',cx,168);
  rosette(c,cx,318,112,'CLAIMED!','🎉');
  var sz=68,lines;do{c.font=font('800',sz);lines=wrap(c,msg,W-260);sz-=4}while(lines.length>3&&sz>40);
  var lh=sz*1.16,y=626;lines.forEach(function(l){c.fillStyle=/\$1,000/.test(l)?C.accd:C.ink;c.fillText(l,cx,y);y+=lh;});
  c.font=font('400',54,EMO);c.fillText('🎉  🥳  🎈',cx,y+4);
  var by=Math.min(y+40,888);rr(c,150,by,W-300,124,26);c.fillStyle=C.soft;c.fill();
  c.fillStyle=C.ink;c.font=font('700',38);c.fillText('Did you claim yours?',cx,by+54);
  var chk='Check free at '+(location.host||'j6-cloude.github.io');c.fillStyle=C.teal;fit(c,chk,'700',34,W-340);c.fillText(chk,cx,by+102);
  c.fillStyle=C.muted;c.font=font('500',26);c.fillText('Self-declared by a proud parent. Claiming is free;',cx,H-302);c.fillText('never pay anyone to claim.',cx,H-268);
  footer(c,'');
 }
 function draw(s,canvas,kind){
  canvas=canvas||document.createElement('canvas');canvas.width=W;canvas.height=H;var c=canvas.getContext('2d');
  if((kind||KIND)==='claim')drawClaim(c);else drawProj(s,c);return canvas;
 }
 // ---- DOM ----
 function render(){
  draw(S).toBlob(function(b){blob=b;if(objURL)URL.revokeObjectURL(objURL);objURL=URL.createObjectURL(b);var im=$('shimg');if(im){im.src=objURL;im.hidden=false;}},'image/png');
 }
 function refresh(){
  var u=shareURL(),t=shareText(),e=encodeURIComponent;
  $('shfb').href='https://www.facebook.com/sharer/sharer.php?u='+e(u);
  $('shsms').href='sms:?&body='+e(t+' '+u);
  $('shwa').href='https://wa.me/?text='+e(t+' '+u);
  $('shurl').value=u;blob=null;clearTimeout(timer);timer=setTimeout(render,300);
 }
 function fname(){return KIND==='claim'?'trump-account-claimed.png':'trump-account-certificate-'+Math.round(S.bal)+'.png'}
 function withBlob(fn){if(blob)fn(blob);else draw(S).toBlob(function(b){blob=b;if(objURL)URL.revokeObjectURL(objURL);objURL=URL.createObjectURL(b);fn(b)},'image/png')}
 function download(){withBlob(function(){var a=document.createElement('a');a.href=objURL;a.download=fname();document.body.appendChild(a);a.click();a.remove();})}
 function nativeShare(){
  withBlob(function(b){
   var u=shareURL(),data={title:'KidAccountMath',text:shareText()+' '+u,url:u};
   try{var f=new File([b],fname(),{type:'image/png'});if(navigator.canShare&&navigator.canShare({files:[f]}))data.files=[f];}catch(e){}
   navigator.share(data).catch(function(){});
  });
 }
 function copy(){
  var u=$('shurl').value,ok=function(){$('shcopy').textContent='Copied!';setTimeout(function(){$('shcopy').textContent='Copy link'},1800)};
  if(navigator.clipboard&&window.isSecureContext)navigator.clipboard.writeText(u).then(ok,function(){$('shurl').select();document.execCommand('copy');ok()});
  else{$('shurl').select();document.execCommand('copy');ok();}
 }
 function init(){
  var box=$('share');if(!box||box.dataset.ready)return false;box.dataset.ready='1';KIND=box.getAttribute('data-kind')||'proj';
  $('shdl').addEventListener('click',download);$('shcopy').addEventListener('click',copy);
  if(navigator.share){$('shnat').hidden=false;$('shnat').addEventListener('click',nativeShare);}
  var nm=$('shname');if(nm){var q=new URLSearchParams(location.search);if(q.get('name')){nm.value=cleanName(q.get('name'));if($('shincl'))$('shincl').checked=true;}
   nm.addEventListener('input',function(){if(S||KIND==='claim')refresh()});}
  if($('shincl'))$('shincl').addEventListener('change',function(){if(S)refresh()});
  if(KIND==='claim'){var go=$('shgo');S={};go.addEventListener('click',function(){$('shbody').hidden=false;go.hidden=true;refresh();$('shbody').scrollIntoView({block:'start',behavior:'smooth'});});}
  else box.hidden=false;
  return true;
 }
 document.addEventListener('DOMContentLoaded',init);
 window.KAMShare={
  update:function(s){init();S=s;refresh();},
  draw:draw,query:query,tier:tier,assumptions:assumptions,setName:function(n){var el=$('shname');if(el)el.value=n;}
 };
})();
