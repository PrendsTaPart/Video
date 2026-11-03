import sys
P=[0.6,12.6,25.6,42.4,56.8,67.6,75.6]; A=[0,5.355,14.994,28.583,39.83,47.44,52.833,64.72]
S=[
 [("Vous avez vu mes trois dernières vidéos ?",0.0),("Aujourd'hui, je vous montre comment elles ont été réalisées,",1.68),("avec mes outils IA.",4.12)],
 [("Tout commence par une idée, des captures d'écran,",5.5),("des démonstrations, et un prompt.",7.78),("Claude lit mes dépôts, mes sites et mes fichiers,",9.64),("vérifie ce qui existe vraiment,",12.16),("puis propose le scénario.",13.72)],
 [("Mon plugin Vidéo, rapido-video,",15.02),("apporte les recettes de montage :",16.94),("couper, assembler, mixer la voix et la musique,",18.54),("sous-titrer avec Whisper, exporter au bon format.",21.16),("Pour ces épisodes, Claude a aussi écrit",23.8),("des scènes animées en HTML, rendues image par image.",25.58)],
 [("Au lieu d'assembler à la main, je décris le résultat.",28.42),("Claude enchaîne : la voix off générée avec ElevenLabs,",31.04),("les mots calés à la seconde près,",33.78),("la musique qui baisse sous la voix,",35.36),("les sous-titres incrustés,",36.92),("puis les versions longues et courtes.",38.22)],
 [("Ensuite, RapidoCMS prend le relais :",39.84),("la vidéo part dans la bibliothèque,",41.84),("un brouillon est créé pour le réseau choisi,",43.46),("et la publication est programmée dans le calendrier.",45.2)],
 [("Ce qui reste humain :",47.58),("valider le scénario, les chiffres,",48.52),("l'accord des personnes citées,",50.26),("et le feu vert de publication.",51.36)],
 [("Une idée devient un scénario, puis une vidéo,",52.92),("puis un contenu prêt à être diffusé.",55.26),("Mon objectif, ce n'est pas seulement",56.94),("de créer des vidéos plus vite.",58.7),("C'est de construire une chaîne de production réutilisable,",60.28),("de l'idée jusqu'à la publication.",62.84)],
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
