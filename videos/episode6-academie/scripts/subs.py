import sys
A=[0,6.955,16.915,24.857,33.954,48.38,57.664,70.335,83.76]
P=[2.5,11.0,22.5,32.0,42.6,58.4,68.5,97.6]
S=[
 [("Aujourd'hui, tout le monde parle d'employés IA.",0.0),("Mais il y a une question que presque personne ne pose :",2.72),("comment est-ce qu'on les forme à leur métier ?",5.32)],
 [("Dans mes entreprises, j'ai développé beaucoup de logiciels",7.1),("et de connexions MCP.",9.44),("Mais donner des outils à une intelligence artificielle",10.74),("ne suffit pas.",12.78),("Elle doit aussi comprendre nos méthodes,",13.64),("nos règles et nos objectifs.",15.38)],
 [("J'ai donc développé FoodEatUp Academy.",16.92),("Une plateforme de formation avec des parcours,",19.0),("des missions, des quiz, des exercices",21.3),("et un suivi des compétences.",23.34)],
 [("Et j'ai connecté cette Académie directement à Claude,",24.88),("grâce à son propre MCP.",27.14),("Claude peut consulter les formations,",28.58),("récupérer les procédures,",30.48),("et utiliser les connaissances adaptées à ses missions.",31.64)],
 [("J'ai aussi ajouté une mémoire.",34.06),("Claude peut retrouver les préférences, les objectifs,",35.52),("les corrections et les méthodes qui ont fonctionné.",37.96),("Ces notes sont réinjectées dans son contexte de travail :",40.14),("le modèle n'est pas réentraîné.",42.58),("Et certaines connaissances peuvent être validées",44.04),("par le responsable,",45.76),("pour être partagées avec toute l'équipe.",46.58)],
 [("Ensuite, je peux préparer des agents spécialisés :",48.46),("commercial, marketing, gestion,",50.8),("formation ou pilotage.",52.84),("Chaque agent possède un rôle,",54.28),("des outils autorisés et des objectifs à atteindre.",55.68)],
 [("Et c'est là que ça devient intéressant.",57.84),("Je peux définir des routines, leur donner un objectif,",59.64),("mesurer les résultats,",62.22),("et décider si la méthode doit être conservée,",63.3),("améliorée ou arrêtée.",65.62),("Pour qu'elles tournent seules,",66.98),("il faut un orchestrateur réellement configuré.",67.98)],
 [("Mon objectif, ce n'est pas simplement",70.32),("d'avoir des agents IA qui répondent à des questions.",71.9),("C'est de construire une équipe qui connaît nos métiers,",74.34),("utilise nos outils, suit nos objectifs,",76.64),("et améliore progressivement ses méthodes.",78.72),("Et demain, je vous montrerai",80.84),("une nouvelle étape de cette aventure.",82.06)],
]
cues=[]
for i,sec in enumerate(S):
    end=P[i]+A[i+1]-A[i]-0.05
    for j,(txt,w) in enumerate(sec):
        st=max(P[i],P[i]+w-A[i]-0.08); en=(P[i]+sec[j+1][1]-A[i]-0.08) if j+1<len(sec) else end
        cues.append((st,en,txt))
def ts(t,srt):
    h=int(t//3600);m=int(t%3600//60);s=t%60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s%1)*1000))%1000:03d}" if srt else f"{h}:{m:02d}:{s:05.2f}"
out=sys.argv[1]; shift=float(sys.argv[2]) if len(sys.argv)>2 else 0
with open(out+'.srt','w') as f:
    for k,(a,b,t) in enumerate(cues,1): f.write(f"{k}\n{ts(a,1)} --> {ts(b,1)}\n{t}\n\n")
hdr="""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Poppins SemiBold,50,&H00E6F9FC,&H00E6F9FC,&H00231A0F,&H00231A0F,0,0,0,0,100,100,0,0,3,16,0,2,90,90,250,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
with open(out+'.ass','w') as f:
    f.write(hdr)
    for a,b,t in cues: f.write(f"Dialogue: 0,{ts(a,0)},{ts(b,0)},Sub,,0,0,0,,{{\\fad(80,60)}}{t}\n")
print(len(cues))
