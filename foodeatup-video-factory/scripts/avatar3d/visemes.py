#!/usr/bin/env python3
"""L'animation du chef, image par image, calculée depuis sa voix et son texte.

Le GLB porte les quinze visèmes Oculus, le jeu ARKit complet (sourcils, yeux,
joues, bouche) et un squelette de 67 os dont `Head`, `Neck` et les deux yeux.
On ne devine donc rien : on dit à chaque pièce quoi faire.

Trois couches, et elles ne servent pas la même chose :

  LA BOUCHE  suit le texte (quelle forme) et la voix (quand, et combien).
  LE REGARD  ne suit rien — il dérive et cligne selon son propre rythme. Un
             regard calé sur la parole donne un pantin ; un regard indépendant
             donne quelqu'un qui pense en parlant.
  LA TÊTE    suit la voix de très loin : un léger appui sur les syllabes
             fortes, sur un fond de balancement lent qui ne s'arrête jamais.

Rien n'est aléatoire : tout est une fonction de l'indice d'image, pour qu'un
même épisode rendu deux fois donne exactement le même plan.
"""
import array, json, math, subprocess, sys

FPS = 30

DIGRAMMES = [("eau","O"),("ch","CH"),("ph","FF"),("th","TH"),("gn","nn"),
             ("ou","U"),("au","O"),("ai","E"),("ei","E"),("on","O"),
             ("an","aa"),("en","aa"),("in","I"),("un","U"),("oi","U")]
LETTRES = {"a":"aa","à":"aa","â":"aa","e":"E","é":"E","è":"E","ê":"E","ë":"E",
           "i":"I","î":"I","ï":"I","y":"I","o":"O","ô":"O","u":"U","û":"U","ù":"U",
           "p":"PP","b":"PP","m":"PP","f":"FF","v":"FF","t":"DD","d":"DD",
           "k":"kk","g":"kk","c":"kk","q":"kk","x":"kk","n":"nn","l":"nn",
           "r":"RR","s":"SS","z":"SS","ç":"SS","j":"CH","h":"sil","w":"U"}
OUVERTES = ("aa", "E", "O", "I", "U")


def suite_visemes(texte):
    t, out, i = texte.lower(), [], 0
    while i < len(t):
        for d, v in DIGRAMMES:
            if t.startswith(d, i):
                out.append(v); i += len(d); break
        else:
            c = t[i]
            if c in LETTRES:
                out.append(LETTRES[c])
            elif c in " ,.;:!?'\n" and out and out[-1] != "sil":
                out.append("sil")
            i += 1
    return out or ["sil"]


def enveloppe(wav):
    raw = subprocess.run(["ffmpeg","-v","error","-i",wav,"-f","s16le","-ac","1",
                          "-ar","16000","-"], capture_output=True).stdout
    n = len(raw)//2
    ech = array.array("h"); ech.frombytes(raw[:n*2])
    par = max(1, 16000//FPS)
    niv = []
    for s in range(0, len(ech), par):
        f = ech[s:s+par]
        if not f: break
        niv.append(math.sqrt(sum(float(x)*x for x in f)/len(f))/32768.0)
    pic = max(niv) or 1.0
    return [min(1.0,(v/pic)**0.6) for v in niv]


def bruit(i, graine):
    """Un bruit lisse et reproductible, entre -1 et 1.

    Somme de trois sinus de périodes premières entre elles : ça ne se répète
    pas à l'œil sur la durée d'un épisode, et ça redonne les mêmes valeurs à
    chaque rendu — indispensable pour pouvoir reprendre un montage.
    """
    a = math.sin((i / 37.0) + graine * 1.7)
    b = math.sin((i / 53.0) + graine * 3.1) * 0.6
    c = math.sin((i / 89.0) + graine * 5.3) * 0.35
    return (a + b + c) / 1.95


def main(wav, texte, sortie):
    niv = enveloppe(wav)
    suite = suite_visemes(texte)
    parlantes = [i for i, v in enumerate(niv) if v > 0.08]
    rang_de = {img: r for r, img in enumerate(parlantes)}

    # Les clignements. Un intervalle fixe se remarque ; on alterne des attentes
    # de 2,4 s et 3,9 s, avec de temps en temps un double clignement, comme en
    # vrai. Chaque clignement dure 4 images — moins, il disparaît ; plus, il
    # ressemble à un endormissement.
    clign = set()
    t_img, k = 24, 0
    while t_img < len(niv):
        for d in range(4):
            clign.add((t_img + d, d))
        if k % 3 == 2:                       # un double, une fois sur trois
            for d in range(4):
                clign.add((t_img + 9 + d, d))
        t_img += 72 if k % 2 == 0 else 117
        k += 1
    courbe_clign = {}
    for img, d in clign:
        courbe_clign[img] = max(courbe_clign.get(img, 0.0), [0.35, 0.95, 0.8, 0.3][d])

    brut = []
    for i, v in enumerate(niv):
        m = {}
        parle = v > 0.08

        # ── la bouche ────────────────────────────────────────────────────────
        if parle and parlantes:
            k = suite[min(len(suite)-1, rang_de.get(i, 0) * len(suite) // max(1, len(parlantes)))]
            if k != "sil":
                # Amplitudes revues à la baisse. À 0,95 la bouche s'ouvrait en
                # grand sur chaque voyelle : le chef criait au lieu de parler.
                # Les voyelles plafonnent à 0,62, les consonnes à 0,48 — assez
                # pour être lu à la taille du segment D, sans la grimace.
                plafond = 0.62 if k in OUVERTES else 0.48
                m[f"viseme_{k}"] = min(plafond, 0.24 + 0.42 * v)
            m["jawOpen"] = 0.02 + 0.08 * v
            # La bouche d'un visage vivant n'est pas qu'un trou qui s'ouvre :
            # elle s'étire un peu sur les syllabes appuyées.
            m["mouthSmileLeft"] = m["mouthSmileRight"] = 0.06 + 0.10 * v
        else:
            m["viseme_sil"] = 0.35
            m["jawOpen"] = 0.02
            m["mouthSmileLeft"] = m["mouthSmileRight"] = 0.10

        # ── le regard ────────────────────────────────────────────────────────
        # Il dérive lentement et revient toujours vers la caméra : quelqu'un
        # qui s'adresse à vous décroche une seconde, puis vous retrouve.
        gx, gy = bruit(i, 1), bruit(i, 2)
        if gx > 0:
            m["eyeLookOutLeft"] = m["eyeLookInRight"] = 0.16 * gx
        else:
            m["eyeLookInLeft"] = m["eyeLookOutRight"] = 0.16 * -gx
        if gy > 0:
            m["eyeLookUpLeft"] = m["eyeLookUpRight"] = 0.11 * gy
        else:
            m["eyeLookDownLeft"] = m["eyeLookDownRight"] = 0.13 * -gy

        c = courbe_clign.get(i, 0.0)
        if c:
            m["eyeBlinkLeft"] = m["eyeBlinkRight"] = c
        # Les yeux se plissent quand on appuie un mot. Sans ça le regard reste
        # fixe et vide pendant que la bouche s'agite.
        m["eyeSquintLeft"] = m["eyeSquintRight"] = 0.10 + 0.16 * v

        # ── le visage ────────────────────────────────────────────────────────
        s = bruit(i, 4)
        m["browInnerUp"] = max(0.0, 0.09 + 0.20 * v + 0.06 * s)
        m["browOuterUpLeft"] = max(0.0, 0.05 + 0.13 * v + 0.05 * s)
        m["browOuterUpRight"] = max(0.0, 0.05 + 0.13 * v + 0.04 * s)
        m["cheekSquintLeft"] = m["cheekSquintRight"] = 0.05 + 0.09 * v
        m["mouthDimpleLeft"] = m["mouthDimpleRight"] = 0.04 + 0.07 * v

        # ── la tête ──────────────────────────────────────────────────────────
        # En radians. Trois degrés au maximum : au-delà, sur un plan serré, la
        # tête donne l'impression de chercher quelque chose.
        os_ = {
            "Head": [ -0.020 + 0.016 * bruit(i, 7) - 0.022 * v,
                       0.030 * bruit(i, 8),
                       0.012 * bruit(i, 9) ],
            "Neck": [  0.010 * bruit(i, 7) + 0.010 * v,
                       0.014 * bruit(i, 8),
                       0.006 * bruit(i, 9) ],
            "Spine2": [0.006 * bruit(i, 11), 0.008 * bruit(i, 12), 0.0],
        }
        brut.append((m, os_))

    # ── lissage ──────────────────────────────────────────────────────────────
    # 119 visèmes sur 244 images parlantes : chaque forme ne tient que deux
    # images. Sans lissage la bouche ne parle pas, elle vibre. Une moyenne
    # glissante sur trois images suffit à en faire de la parole, sans retarder
    # la bouche au point qu'elle décroche de la voix.
    #
    # Le clignement est EXCLU du lissage : lissé, il devient un battement mou
    # de paupières au lieu d'un clignement net.
    images = []
    for i in range(len(brut)):
        acc, poids = {}, 0.0
        for d, p in ((-1, 0.25), (0, 0.5), (1, 0.25)):
            j = i + d
            if 0 <= j < len(brut):
                for nom, val in brut[j][0].items():
                    if nom.startswith("eyeBlink"): continue
                    acc[nom] = acc.get(nom, 0.0) + val * p
                poids += p
        m = {nom: round(val / poids, 3) for nom, val in acc.items()}
        cl = brut[i][0].get("eyeBlinkLeft")
        if cl:
            m["eyeBlinkLeft"] = m["eyeBlinkRight"] = round(cl, 3)
        os_ = {k: [round(x, 4) for x in v] for k, v in brut[i][1].items()}
        images.append({"m": m, "os": os_})

    json.dump({"fps": FPS, "images": images}, open(sortie, "w"), indent=0)
    print(f"{len(images)} images · {len(images)/FPS:.2f}s · {len(suite)} visèmes "
          f"sur {len(parlantes)} images parlantes · {len(courbe_clign)} images de clignement")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
