import json
W=json.load(open("v39/words.json")); O=0.3
fix={1:"burger,",5:"14",6:"€.",14:"Pain :",15:"0,45",16:"€.",17:"Steak :",18:"1,95",19:None,20:"€.",21:"Cheddar :",22:"0,35",23:"€.",24:"Sauce",26:"crudités :",27:"0,45",28:"€.",29:"Total :",30:"3,20",31:None,32:"€",36:"12,73",37:None,38:"€",39:"hors",40:"taxes,",42:"food",46:"25 %.",52:"30",53:"centimes,",57:"27,5 %.",58:None,63:"FoodEatUp,",64:None,65:None,85:"change ?",90:"recalculent,",91:"et",92:"tes",93:None,94:"marges",96:"Commente",97:"FOODCOST,",103:"t’envoie",104:None,98:None,99:None,100:None,101:"et"}
D=[]
for i,(w,s,e) in enumerate(W):
    if i in fix:
        if fix[i] is None: continue
        w=fix[i]
    if w in ("€.","€") and D: D[-1][0]+=" "+w; continue
    D.append([w,round(s+O,2),i])
S=[0,14,29,35,47,62,82,96]
P=[round(W[k][1]+O,2) for k in S]
cfg={"dur":round(W[-1][2]+O+3.4,2),"P":P,"words":D,"off":O}
open("v39/cfg.js","w").write("window.CFG="+json.dumps(cfg,ensure_ascii=False)+";")
json.dump(cfg,open("v39/cfg.json","w"),ensure_ascii=False)
print(cfg["dur"],P); print(" ".join(w for w,_,_ in D))
