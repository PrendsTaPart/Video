import sys
A=[0,15.282,36.51,56.183,75.61,93.884,118.785,137.475,157.261,168.45]
P=[0.3,16.582,38.81,59.483,79.91,99.184,125.085,144.775,165.561]
S=[
 [("Tout le monde parle d'agents IA.",0.0),("Mais comment faire pour qu'une IA ne se contente plus",1.78),("de répondre à des questions,",3.58),("et puisse réellement travailler avec nos logiciels ?",4.58),("Un agent IA performant, ce n'est pas seulement un bon prompt.",6.96),("C'est un rôle, des compétences, des outils,",9.6),("des règles et des automatismes.",11.9),("Six briques. Voyons-les une par une.",13.48)],
 [("Première brique : les MCP, pour Model Context Protocol.",15.4),("Ce sont les mains de l'IA :",18.74),("un protocole qui lui permet de se brancher sur les outils de l'entreprise.",19.84),("Dans le plugin FoodEatUp, une seule ligne de configuration",22.86),("pointe vers le serveur MCP du logiciel.",24.98),("L'agent peut alors, par exemple, consulter les stocks d'un restaurant.",27.22),("Attention : un MCP donne accès aux fonctions",30.02),("autorisées pour le compte connecté.",31.98),("À lui seul, il ne garantit ni l'autonomie, ni la sécurité.",33.6)],
 [("Deuxième brique : les Skills, le savoir-faire.",36.7),("L'IA peut lire les stocks, mais sait-elle quoi en faire ?",39.02),("Un Skill est un fichier, SKILL.md, qui décrit une méthode :",41.44),("quand l'utiliser, les étapes, les règles.",45.2),("Le Skill de réapprovisionnement, par exemple, enchaîne :",47.26),("détecter les stocks bas, regrouper par fournisseur,",49.54),("faire valider, puis commander.",51.88),("Le Skill définit la méthode. Il ne déclenche rien tout seul.",53.36)],
 [("Troisième brique : les agents, les employés spécialisés.",56.2),("Un agent, c'est un rôle, un objectif et des instructions.",59.02),("Le chef-restaurateur raisonne en ratios :",61.76),("food cost, masse salariale, marge.",63.44),("Le directeur commercial pilote le pipeline.",65.46),("Le directeur général croise les signaux.",67.34),("Le catalogue en compte soixante-dix-sept.",69.08),("Un agent reçoit une mission, choisit ses outils et produit un résultat,",71.02),("dans les limites de sa configuration.",74.16)],
 [("Quatrième brique : les plugins, le paquet.",75.76),("Un plugin regroupe des Skills, des agents, des commandes,",77.92),("des Hooks et ses connexions MCP, pour tout installer en une fois.",80.62),("La marketplace BraindCode en propose trente-trois :",83.46),("FoodEatUp, RapidoCRM, RapidoCMS, RapidoRH, Plan'It…",85.88),("Dans Claude Code, deux commandes suffisent :",89.8),("ajouter la marketplace, puis installer le plugin.",91.54)],
 [("Cinquième brique : les Hooks, les réflexes.",94.04),("Un Hook se déclenche sur un événement précis :",96.18),("avant l'appel d'un outil, après,",98.1),("au démarrage d'une session, ou à la fin d'une réponse.",99.76),("Contrairement au modèle, un Hook est déterministe :",101.98),("il réagit toujours de la même façon.",104.2),("Dans FoodEatUp, un Hook refuse un relevé de température",105.94),("sans équipement identifié,",108.34),("et un autre impose une confirmation avant toute action destructrice.",109.56),("Mais attention : une vraie validation humaine",112.44),("passe par un mécanisme d'approbation.",114.68),("Un Hook seul ne fait pas toute la sécurité.",116.62)],
 [("Sixième brique : la connaissance de l'entreprise.",118.88),("Sans contexte, même un agent bien équipé ne connaît",121.32),("ni vos règles, ni vos objectifs, ni vos procédures.",123.66),("La base de connaissance, un dossier rapido-kb créé chez vous,",126.24),("contient vos seuils, vos processus, votre charte et votre ton.",129.16),("Elle persiste d'une session à l'autre,",132.28),("contrairement à l'historique d'une conversation.",133.72),("Et elle n'est jamais publiée dans le dépôt.",135.64)],
 [("Assemblons tout.",137.52),("Un restaurateur demande : analyse mes stocks",138.08),("et prépare mes achats fournisseurs pour les trois prochains jours.",140.46),("Le chef-restaurateur reçoit l'objectif.",142.9),("Il charge le Skill de réapprovisionnement.",144.84),("Le MCP FoodEatUp fournit les données autorisées.",146.7),("La base de connaissance donne les seuils.",149.14),("L'agent prépare ses recommandations.",150.84),("Les Hooks et les permissions encadrent les actions sensibles.",152.52),("Et le restaurateur valide avant toute commande.",155.02)],
 [("C'est en assemblant ces briques qu'on passe d'un chatbot",157.34),("à une équipe d'agents IA spécialisés,",159.38),("capables de réaliser des missions dans les outils de l'entreprise.",161.22),("C'est ce que nous construisons avec BraindCode.",164.06),("À retrouver sur plugin.braindcode.com",165.66)],
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
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Inter ExtraBold,40,&H00FFFFFF,&H00FFFFFF,&H00221608,&H96221608,0,0,0,0,100,100,0,0,3,12,0,2,200,200,28,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
with open(out+'.ass','w') as f:
    f.write(hdr)
    for a,b,t in cues: f.write(f"Dialogue: 0,{ts(a,0)},{ts(b,0)},Sub,,0,0,0,,{{\\fad(80,60)}}{t}\n")
print(len(cues))
