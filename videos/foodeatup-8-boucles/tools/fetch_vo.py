#!/usr/bin/env python3
"""Récupère les mp3 de voix off produits par le MCP ElevenLabs.

Le MCP ne rend pas les octets : il rend un lien signé, valable 15 minutes. Ces
URLs sont signées en Google V4, donc **toute** modification de la query string
— y compris réordonner les paramètres ou retirer `response-content-disposition`
— casse la signature et renvoie une erreur XML de 860 octets à la place du mp3.
D'où ce script : on passe les URLs telles quelles, sans les recomposer.

Usage : lui donner sur l'entrée standard un JSON
    {"<dossier vidéo>": {"p01": "<url>", "p02": "<url>", …}, …}
"""
import json
import pathlib
import sys
import urllib.request

PROJ = pathlib.Path(__file__).resolve().parent.parent

# Un mp3 commence par une balise ID3 ou une trame MPEG (0xFF 0xFB/0xF3/0xF2).
DEBUTS_MP3 = (b"ID3", b"\xff\xfb", b"\xff\xf3", b"\xff\xf2")


def main() -> None:
    lots = json.load(sys.stdin)
    total, rates = 0, []
    for dossier, plans in lots.items():
        cible = PROJ / dossier / "assets" / "vo"
        cible.mkdir(parents=True, exist_ok=True)
        for nom, url in sorted(plans.items()):
            try:
                octets = urllib.request.urlopen(url, timeout=90).read()
            except Exception as e:                      # noqa: BLE001
                rates.append(f"{dossier}/{nom} — {e}")
                continue
            if not octets.startswith(DEBUTS_MP3):
                # Presque toujours un lien expiré : le message est dans le XML.
                rates.append(f"{dossier}/{nom} — pas un mp3 : {octets[:180]!r}")
                continue
            (cible / f"{nom}.mp3").write_bytes(octets)
            total += 1
            print(f"  {dossier}/{nom}.mp3  {len(octets) // 1024} Ko")

    print(f"\n{total} piste(s) récupérée(s).")
    if rates:
        print(f"{len(rates)} ÉCHEC(S) :")
        for r in rates:
            print("  " + r)
        sys.exit(1)


if __name__ == "__main__":
    main()
