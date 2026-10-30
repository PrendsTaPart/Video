"""cfg.js de l'épisode 62 : texte affiché aligné sur les temps whisper de la prise B (difflib + interpolation)."""
import json,re,difflib
O=0.4
TXT=open('script.txt').read().strip().split('\n')
wh=json.load(open('voix/voix-prise-b.mp3.json'))
norm=lambda w:re.sub(r"[^a-z0-9àâäéèêëîïôöùûüç]","",w.lower())
NUM={'1':'un','2':'deux','3':'trois','4':'quatre','5':'cinq','6':'six','7':'sept','10':'dix'}
# jetons whisper fusionnés (j 'ai -> j'ai)
W=[]
for w,s,e in wh:
  if W and (w.startswith("'") or w.startswith('-')): W[-1]=[W[-1][0]+w,W[-1][1],e]
  else: W.append([NUM.get(w.strip(',.?'),w),s,e])
toks=[];lid=[]
for i,l in enumerate(TXT):
  for t in l.split():
    if t in (':',): continue
    toks.append(t);lid.append(i)
a=[norm(t) for t in toks];b=[norm(w[0]) for w in W]
T=[None]*len(a);E=[None]*len(a)
for blk in difflib.SequenceMatcher(None,a,b,autojunk=False).get_matching_blocks():
  for k in range(blk.size): T[blk.a+k]=W[blk.b+k][1];E[blk.a+k]=W[blk.b+k][2]
if T[0] is None:T[0]=W[0][1]
if T[-1] is None:T[-1]=W[-1][1]
kn=[i for i,t in enumerate(T) if t is not None]
for i in range(len(T)):
  if T[i] is None:
    lo=max(k for k in kn if k<i);hi=min(k for k in kn if k>i);T[i]=T[lo]+(T[hi]-T[lo])*(i-lo)/(hi-lo)
for i in range(1,len(T)):T[i]=max(T[i],T[i-1]+.05)
words=[[t,round(x+O,2),l] for t,x,l in zip(toks,T,lid)]
lines=[]
for i,l in enumerate(TXT):
  ws=[w for w in words if w[2]==i];last=max(j for j in range(len(lid)) if lid[j]==i)
  end=(E[last] if E[last] else T[last]+.4)+O
  lines.append({"t0":ws[0][1],"t1":round(end,2),"txt":l})
dur=round(W[-1][2]+O+3.2,2)
json.dump({"dur":dur,"words":words,"lines":lines},open('cfg.json','w'),ensure_ascii=False)
open('cfg.js','w').write("window.CFG="+json.dumps({"dur":dur,"words":words,"lines":lines},ensure_ascii=False)+";")
for i,l in enumerate(lines):print(i,l['t0'],l['t1'],l['txt'][:60])
print('dur',dur,'non alignés',sum(1 for x in E if x is None))
