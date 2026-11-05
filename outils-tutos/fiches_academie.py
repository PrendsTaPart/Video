#!/usr/bin/env python3
"""Fiches Académie (TypeScript) d'une série de tutoriels d'application.
fiches(T, cfg, textes, titres_bo) -> texte TS.
cfg : export, prefixe_rapido (ex. "foodeatup-haccp-"), prefixe_cle (ex. "app-haccp-"),
      module, section, ordre, app, dossier (série dans le dépôt Video), origine.
textes[sujet] = (a quoi ça sert, astuce du chef, slug de la fiche back-office liée)."""
import json, subprocess, os
B = "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/"

def duree(f):
    return round(float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f])))

def fiches(T, cfg, textes, titres_bo):
    out = []
    for i, v in enumerate(T):
        sujet = v["cle"][len(cfg["prefixe_cle"]):]
        quoi, astuce, lie = textes[sujet]
        f = {
            "slug": v["cle"], "title": v["titre"], "moduleSlug": cfg["module"],
            "subcategory": cfg["section"], "section": cfg["section"], "order": cfg["ordre"] + i,
            "videoUrl": B + cfg["prefixe_rapido"] + sujet + "-tuto",
            "thumbnailUrl": B + cfg["prefixe_rapido"] + sujet + "-vignette",
            "durationSeconds": duree(os.path.join(cfg["dossier"], "sortie", v["cle"] + "-tuto.mp4")),
            "howItWorks": v["etapes"], "whatItsFor": quoi, "chefTip": astuce,
            "claudePrompts": [{"title": v["titre"], "prompt":
                f"Explique-moi « {v['titre'][0].lower() + v['titre'][1:]} » sur {cfg['app']} pour mon établissement (ID [ID établissement]), étape par étape."}],
        }
        if lie:
            f["faq"] = [{"question": "Et depuis FoodEatUp sur ordinateur ?",
                         "reponse": f"Le même sujet côté logiciel est expliqué dans la fiche « {titres_bo[lie]} » : https://tutoriel.foodeatup.com/tutoriel/{lie}"}]
        out.append(f)
    corps = json.dumps(out, ensure_ascii=False, indent=2)
    return (f'import type {{ Tutorial }} from "./tutorials";\n\n/**\n * Tutoriels vidéo de l\'application « {cfg["nom"]} ».\n *\n'
            f' * {cfg["origine"]}\n * Voix Adam eleven_v4, montage HyperFrames. Sources : dépôt PrendsTaPart/Video,\n'
            f' * dossier {os.path.basename(cfg["dossier"])}. Fichiers hébergés dans la bibliothèque RapidoCMS.\n'
            f' * Comme fichesAppKds, ces fiches s\'ajoutent au catalogue en base sans jamais écraser\n * un contenu édité dans l\'admin.\n */\n'
            f'export const {cfg["export"]}: Tutorial[] = {corps};\n')
