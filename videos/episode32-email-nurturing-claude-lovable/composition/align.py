import json,re,sys,difflib,unicodedata
def n(w): w=unicodedata.normalize('NFD',w.lower()); return re.sub(r'[^a-z0-9]','',''.join(c for c in w if unicodedata.category(c)!='Mn'))
for ep in sys.argv[1:]:
  paras=[p.split() for p in open(f'txt{ep}.txt').read().strip().split('\n\n')]
  # drop pure punctuation tokens
  paras=[[w for w in p if n(w)] for p in paras]
  flat=[w for p in paras for w in p]
  W0=json.load(open(f'v{ep}/words.json'));W=[]
  for w in W0:
    if W and (w[0].startswith("'") or w[0].startswith("-")): W[-1]=[W[-1][0]+w[0],W[-1][1],w[2]]
    else: W.append(list(w))
  a=[n(w)[:5] for w in flat]; b=[n(w[0])[:5] for w in W]
  sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
  T=[None]*len(flat)
  for i,j,k in sm.get_matching_blocks():
    for x in range(k): T[i+x]=(W[j+x][1],W[j+x][2])
  # interpolate
  for i in range(len(T)):
    if T[i] is None:
      prev=next((T[k] for k in range(i-1,-1,-1) if T[k]),(0,0)); nxt=next((T[k] for k in range(i+1,len(T)) if T[k]),(prev[1]+.3,prev[1]+.6))
      T[i]=(prev[1],min(nxt[0],prev[1]+.3))
  out=[];k=0
  for p in paras:
    ws=[(w,)+T[k+i] for i,w in enumerate(p)]; k+=len(p); out.append(ws)
  json.dump(out,open(f'v{ep}/aligned.json','w'),ensure_ascii=False)
  print(ep,[ (round(s[0][1],2),round(s[-1][2],2)) for s in out], sum(1 for t in T if t is None))
