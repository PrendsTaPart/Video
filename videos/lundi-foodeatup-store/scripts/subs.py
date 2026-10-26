import sys
P=[0.4,12.2,23.6,36.6,51.4,71.2]; A=[0,10.686,17.502,26.786,36.635,52.666,62.08]
S=[
 [("Hier, dimanche,",0.0),("je vous montrais les quatre applications Flutter",1.12),("et le jeu vidéo qu'on a développés pour FoodEatUp.",2.76),("Mais ce matin, une nouvelle idée :",5.16),("et si toutes ces applications",6.9),("étaient accessibles directement depuis FoodEatUp ?",8.0)],
 [("L'objectif, c'est simple :",10.72),("transformer FoodEatUp en une plateforme",12.1),("où chaque restaurateur peut choisir",13.9),("les applications dont il a réellement besoin.",15.4)],
 [("Aujourd'hui, avec Soulayma,",17.48),("on s'est attaqués à cette nouvelle fonctionnalité :",18.88),("imaginer le parcours utilisateur,",20.88),("organiser les extensions,",22.68),("et préparer leur intégration directement dans FoodEatUp.",24.1)],
 [("Demain, un restaurant pourra",26.84),("retrouver ses outils au même endroit :",28.02),("la fidélité, le HACCP,",29.62),("la caisse mobile, le menu digital…",31.78),("mais aussi de nouvelles applications",33.6),("et des extensions intelligentes.",34.94)],
 [("Et le plus intéressant,",36.66),("c'est que ces applications ne sont pas pensées",37.76),("comme des outils isolés.",39.42),("Elles s'inscrivent dans le même écosystème FoodEatUp,",40.64),("avec des fonctionnalités métier et des connexions MCP.",42.74),("L'IA ne sert pas seulement",45.72),("à développer des applications plus vite :",46.62),("elle permet aussi de repenser la manière",48.5),("dont on construit tout un écosystème logiciel.",50.22)],
 [("Dimanche, on construisait les applications.",52.76),("Lundi, avec Soulayma,",54.82),("on construit la plateforme",56.08),("qui permettra de les retrouver au même endroit.",57.14),("Le FoodEatUp Store arrive bientôt.",59.06),("Et ce n'est que le début.",61.12)],
]
cues=[]
for i,sec in enumerate(S):
    end=P[i]+A[i+1]-A[i]-0.05
    for j,(txt,w) in enumerate(sec):
        st=max(P[i],P[i]+w-A[i]-0.08); en=(P[i]+sec[j+1][1]-A[i]-0.08) if j+1<len(sec) else end
        cues.append((st,en,txt))
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
Style: Sub,Inter ExtraBold,54,&H00FFFFFF,&H00FFFFFF,&H00231A0F,&H96231A0F,0,0,0,0,100,100,0,0,3,16,0,8,90,90,1600,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
with open(out+'.ass','w') as f:
    f.write(hdr)
    for a,b,t in cues: f.write(f"Dialogue: 0,{ts(a,0)},{ts(b,0)},Sub,,0,0,0,,{{\\fad(80,60)}}{t}\n")
print(len(cues))
