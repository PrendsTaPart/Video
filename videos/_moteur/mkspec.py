import json,re,sys
def marks(d):
    s=open(f"{d}/index.html").read()
    ms=re.findall(r"M\('((?:[^'\\]|\\.)*)'\)",s)
    out=[]
    for m in ms:
        m=m.replace("\\'","'")
        if m not in out: out.append(m)
    return out
def write(d,spec):
    spec["marks"]=marks(d)
    json.dump(spec,open(f"{d}/spec.json","w"),ensure_ascii=False,indent=0)
