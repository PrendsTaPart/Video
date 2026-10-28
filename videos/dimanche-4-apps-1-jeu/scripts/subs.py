import sys
P=[0.4,7.0,17.0,31.0,42.0,50.6,57.2,69.0]; A=[0,5.71,13.71,24.48,33.19,39.26,43.01,49.21,56.24]
S=[
 [("Mon dimanche à la maison ?",0.0),("J'ai décidé de développer",1.26),("quatre applications mobiles…",2.4),("et un jeu vidéo, pour FoodEatUp.",3.64)],
 [("Première application :",5.76),("une borne de fidélité",6.84),("à installer directement au comptoir,",7.82),("pour récompenser les clients.",9.4),("Ils cumulent des points,",10.82),("tournent la roue",11.84),("et répondent à des sondages.",12.38)],
 [("Deuxième application :",13.72),("un assistant HACCP vocal,",14.84),("avec un avatar 3D.",16.38),("Avec des oreillettes,",17.98),("les équipes accèdent aux fonctionnalités HACCP,",18.98),("impriment sur une imprimante compatible,",21.32),("et apprennent grâce au mode école.",22.7)],
 [("Troisième application :",24.26),("une caisse mobile pour les serveurs,",25.7),("avec scanner de QR code,",27.14),("et un mode école",28.44),("accompagné par un avatar 3D.",29.2),("Le paiement sans contact,",30.96),("c'est la prochaine étape.",32.0)],
 [("Quatrième application :",33.24),("une tablette interactive pour les clients,",34.3),("avec menu digital, commandes,",35.88),("jeux-concours et fidélité.",37.84)],
 [("Et chaque restaurant peut personnaliser",39.3),("le thème et la charte graphique de ses applications.",40.76)],
 [("Et pour terminer,",43.06),("FoodEatUp Rush :",44.02),("un jeu vidéo 3D",44.9),("qui transforme l'univers de la restauration",45.88),("en expérience interactive.",47.66)],
 [("Tout ça, depuis la maison,",49.2),("avec Flutter, l'IA",50.36),("et les outils MCP FoodEatUp.",51.74),("Maintenant, prochaine étape :",53.3),("Google Play et l'App Store.",54.8)],
]
cues=[]
for i,sec in enumerate(S):
    end=P[i]+A[i+1]-A[i]-0.05
    for j,(txt,w) in enumerate(sec):
        st=max(P[i], P[i]+w-A[i]-0.08)
        en=(P[i]+sec[j+1][1]-A[i]-0.08) if j+1<len(sec) else end
        cues.append((st,en,txt))
    if i==2: cues.append((28.2,29.8,"Jarvis : « C'est enregistré, merci ! »"))
def ts(t,srt):
    h=int(t//3600);m=int(t%3600//60);s=t%60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s%1)*1000)):03d}" if srt else f"{h}:{m:02d}:{s:05.2f}"
out=sys.argv[1]
with open(out+'.srt','w') as f:
    for k,(a,b,t) in enumerate(cues,1): f.write(f"{k}\n{ts(a,1)} --> {ts(b,1)}\n{t}\n\n")
hdr="""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Manrope ExtraBold,58,&H00FFFFFF,&H00FFFFFF,&H00231A0F,&H96231A0F,0,0,0,0,100,100,0,0,3,16,0,8,90,90,1540,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
with open(out+'.ass','w') as f:
    f.write(hdr)
    for a,b,t in cues:
        if t.startswith("Jarvis"): continue  # déjà à l'écran dans la bulle
        f.write(f"Dialogue: 0,{ts(a,0)},{ts(b,0)},Sub,,0,0,0,,{{\\fad(80,60)}}{t}\n")
print(len(cues))
