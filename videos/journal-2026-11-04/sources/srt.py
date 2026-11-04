import json,sys
def t(x):
    h=int(x//3600);m=int(x%3600//60);s=x%60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s-int(s))*1000)):03d}".replace(',1000',',999')
d=json.load(open(sys.argv[1]))
print('\n'.join(f"{i+1}\n{t(a)} --> {t(b)}\n{c}\n" for i,(a,b,c) in enumerate(d['subs'])))
