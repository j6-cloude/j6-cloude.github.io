import sys,re,html
def syl(w):
    w=w.lower(); w=re.sub(r'[^a-z]','',w)
    if not w: return 0
    if len(w)<=3: return 1
    w=re.sub(r'(?:[^laeiouy]es|ed|[^laeiouy]e)$','',w); w=re.sub(r'^y','',w)
    return max(1,len(re.findall(r'[aeiouy]{1,2}',w)))
def words(t): return [w for w in re.findall(r"[A-Za-z][A-Za-z'’-]*|\$?\d[\d,.%]*",t)]
def fk(t):
    sents=max(1,len([x for x in re.split(r'[.!?]+\s',t) if words(x)]))
    ws=words(t); n=max(1,len(ws)); sy=sum(syl(w) if w[0].isalpha() else 1 for w in ws)
    return 0.39*n/sents+11.8*sy/n-15.59, n
from html.parser import HTMLParser
def text_of(path):
    s=open(path).read()
    m=re.search(r'<main>(.*)</main>',s,re.S); s=m.group(1)
    s=re.sub(r'<(script|style|noscript)[^>]*>.*?</\1>','',s,flags=re.S)
    s=re.sub(r'<table.*?</table>','',s,flags=re.S)
    s=re.sub(r'<form.*?</form>','',s,flags=re.S)
    s=re.sub(r'<section class="sources">.*?</section>','',s,flags=re.S)
    s=re.sub(r'<h1.*?</h1>|<p class="meta">.*?</p>','',s,flags=re.S)
    s=s.replace('U.S.','US').replace('e.g.','eg').replace('i.e.','ie')
    top=s.split('<h2',1)[0]
    clean=lambda t:' '.join(html.unescape(re.sub(r'<(/p|/li|/h\d|br|/div|/summary)[^>]*>','. ',t)).replace('<','<').split())
    clean2=lambda t:re.sub(r'\.\s*\.','.',re.sub(r'<[^>]+>',' ',re.sub(r'</(p|li|h\d|div|summary|label|a class="step[^"]*")>|<br>','. ',t)))
    return clean2(top),clean2(s)
for p in sys.argv[1:]:
    top,full=text_of(p)
    a,n1=fk(top); b,n2=fk(full)
    print(f"{p}: top-of-page FK grade {a:.1f} ({n1} words) | whole page FK {b:.1f} ({n2} words)")
