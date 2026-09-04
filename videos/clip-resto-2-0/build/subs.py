#!/usr/bin/env python3
"""Word-by-word lyric subtitles for the vertical cuts.

Placement: the episodes carry their own burned-in captions, at roughly
y 244-488 on the "problem" half of a rush and y 1272-1594 on the "solution"
half. The band y>1620 is the only one clear on every shot, so the lyrics sit
there and the agent name goes just above the solution captions instead.

Line timings are the sung-line boundaries measured from the local
transcription's word timestamps. The words themselves are an explicit sheet:
the transcriber mishears the sung hook ("FoodEatUp" -> "Fous des hâteux") and
splits French elisions, and burned-in text has to be right.

UNCERTAIN, to check against the official lyric sheet: the "Prêt à devenir un
resto 2.0" line — the transcription is unintelligible there ("un reste de
poursavier"); the title of the clip is what makes 'resto 2.0' the likely read.

Words inside a line are distributed in proportion to their length, so the
karaoke fill tracks the line rather than drifting.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CLOSE_IN = 152.28          # the closing animation carries its own text

# (start, end, line)
SHEET = [
    (11.12, 13.64, "T'en as marre de pas connaître ton stock"),
    (13.64, 16.26, "Le frigo dit oui, le carnet dit non"),
    (16.26, 18.62, "T'as pas le temps de communiquer"),
    (18.62, 21.40, "T'as pas le temps de gérer tes avis"),
    (21.40, 24.08, "T'as peur qu'un contrôle sonne à la porte"),
    (24.08, 26.70, "Le classeur dort, la date s'efface"),
    (26.70, 28.98, "T'as du mal à recruter"),
    (28.98, 31.70, "Trois annonces, zéro réponse"),

    (32.32, 34.82, "Tu perds tes clients et tu sais pas pourquoi"),
    (34.82, 37.40, "Tu galères à les faire revenir"),
    (37.40, 39.76, "Tu te transformes en médium"),
    (39.76, 42.10, "pour deviner tes commandes"),

    (44.64, 48.60, "FoodEatUp est fait pour toi"),
    (55.32, 59.60, "Prêt à devenir un resto 2.0"),
    (60.22, 63.80, "FoodEatUp, huit boucles logiciel"),
    (63.90, 66.40, "et ça tourne tout seul"),

    (71.00, 73.26, "Tu perds tes tickets en cuisine"),
    (73.26, 76.60, "Le pass hurle, personne ne répond"),
    (76.72, 79.08, "45 minutes pour servir une table"),
    (79.08, 81.20, "Le client attend, le client s'en va"),
    (81.24, 84.26, "Ton planning au doigt mouillé"),
    (84.26, 86.70, "Deux en salle quand il en faut cinq"),
    (86.76, 89.36, "Ton site c'est juste une vitrine"),
    (89.36, 91.80, "une belle photo qui vend rien"),

    (92.50, 94.86, "Tu perds tes clients et tu sais pas pourquoi"),
    (94.86, 97.30, "Tu galères à les faire revenir"),
    (97.34, 99.74, "Arrête de jouer les voyants"),
    (99.74, 102.20, "le logiciel, c'est déjà là"),

    (104.66, 108.50, "FoodEatUp est fait pour toi"),
    (109.50, 113.70, "FoodEatUp est fait pour toi"),
    (115.40, 119.50, "Prêt à devenir un resto 2.0"),
    (120.32, 123.80, "FoodEatUp, huit boucles logiciel"),
    (123.92, 126.30, "et ça tourne tout seul"),

    (126.36, 129.18, "Caroline décroche pendant que tu cuisines"),
    (129.18, 131.50, "Jarvis répond à ton équipe"),
    (131.56, 134.04, "PrediBot te dit ce qui va manquer"),
    (134.04, 136.30, "Iris parle pour ton resto"),

    (137.12, 141.30, "FoodEatUp est fait pour toi"),
    (146.86, 152.20, "Ton resto tourne, toi tu respires"),
]

CREME_FULL, CREME_DIM = '&H00E6F9FC', '&H8CE6F9FC'   # &HAABBGGRR
NOIR_BACK = '&H96231A0F'

HEADER = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Lyric,Poppins,70,{CREME_FULL},{CREME_DIM},{NOIR_BACK},{NOIR_BACK},-1,0,0,0,100,100,0,0,3,14,0,2,80,80,110,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""


def ass_time(t):
    cs = int(round(t * 100))
    h, cs = divmod(cs, 360000)
    m, cs = divmod(cs, 6000)
    s, cs = divmod(cs, 100)
    return '%d:%02d:%02d.%02d' % (h, m, s, cs)


def main():
    ev = []
    for start, end, line in SHEET:
        if start >= CLOSE_IN:
            continue
        end = min(end, CLOSE_IN - 0.05)
        words = line.split()
        weights = [len(w) + 1 for w in words]
        total = sum(weights)
        span = end - start
        # karaoke duration per word, in centiseconds, summing to the line span
        cs = [max(6, int(round(span * w / total * 100))) for w in weights]
        txt = ''.join(r'{\k%d}%s ' % (c, w) for c, w in zip(cs, words)).strip()
        ev.append('Dialogue: 0,%s,%s,Lyric,,0,0,0,,%s\n'
                  % (ass_time(start), ass_time(end), txt))

    open(os.path.join(HERE, 'lyrics.ass'), 'w').write(HEADER + ''.join(ev))
    with open(os.path.join(HERE, 'lyrics-resto-2-0.txt'), 'w') as f:
        f.write('Resto 2.0 — paroles relevées (à confirmer sur la feuille officielle)\n\n')
        for s, e, l in SHEET:
            f.write('%7.2f  %s\n' % (s, l))
    print('%d lignes de sous-titres (arrêt à %.2f s, début de la fermeture)'
          % (len(ev), CLOSE_IN))


if __name__ == '__main__':
    main()
