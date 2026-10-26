import sys
P=[0.6,11.6,24.2,39.0,53.0,65.6,76.4]; A=[0,8.956,18.619,30.355,41.488,51.088,59.25,67.52]
S=[
 [("Pendant longtemps, on développait des logiciels",0.0),("pour que les humains travaillent dessus.",2.04),("Maintenant, je construis des compétences et des agents IA",3.82),("pour que les logiciels puissent aussi travailler avec nous.",6.32)],
 [("Première étape : connecter nos outils métier",9.12),("à Claude grâce aux MCP.",11.08),("Restaurant, CRM, marketing, ressources humaines…",12.66),("Chaque logiciel devient accessible",15.88),("à des agents autorisés.",17.34)],
 [("Mais donner accès aux outils ne suffit pas.",18.7),("Il faut apprendre aux agents comment travailler.",20.62),("D'où les Skills : des compétences qui expliquent",22.88),("les procédures, les règles métier et les étapes à suivre.",25.04),("Il y en a aujourd'hui 544 dans le catalogue.",27.56)],
 [("Ensuite, les agents, organisés par métier :",30.46),("directeur général, directeur commercial,",32.92),("marketing, finance, restaurant…",35.04),("Chacun avec son rôle, ses compétences et ses outils.",37.04),("77 agents au total.",39.88)],
 [("Par exemple, un agent peut repérer",41.48),("les stocks bas d'un restaurant",43.0),("et préparer une commande fournisseur.",44.12),("Mais rien ne part sans validation :",45.94),("une commande, un paiement ou une publication",47.56),("attend toujours votre accord.",49.34)],
 [("Et pour rendre tout ça accessible,",51.1),("il y a la marketplace BraindCode :",52.62),("33 plugins à installer dans Claude Code,",54.1),("avec une base de connaissance",56.16),("pour le contexte de votre entreprise.",57.46)],
 [("Le plus intéressant ?",59.24),("Cette équipe IA ne va pas seulement utiliser nos logiciels.",60.22),("Elle va aussi nous aider à en construire de nouveaux.",62.98),("Et dimanche, je suis passé à la pratique.",65.56)],
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
