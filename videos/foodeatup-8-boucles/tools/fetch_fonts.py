#!/usr/bin/env python3
"""Produit `assets/fonts/fonts.css`, avec les polices inlinées en base64.

Titres : **Fredoka**, reprise du fichier déjà vendoré par le studio
(`studio-video/assets/vendor/fonts/Fredoka-Variable.woff2`). C'est la police
maison — la remplaçante de Goodly, la vraie police de marque, que Michael n'a
pas encore fournie. On la reprend telle quelle plutôt que d'introduire une
seconde police ronde dans le catalogue.

Corps : **Inter**, récupérée sur Google Fonts, sous-sets latin.

Inliner plutôt que référencer : c'est la seule forme auto-portée. Un `<link>`
Google Fonts retombe sur une police système au rendu et casse le déterminisme
(règle rappelée par le contrat HyperFrames comme par le pipeline local).
"""
import base64
import pathlib
import re
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
FONTS = HERE.parent / "assets" / "fonts"
UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)
CSS_URL = (
    "https://fonts.googleapis.com/css2"
    "?family=Inter:wght@400;500;600;700"
    "&display=block"
)
KEEP_SUBSETS = {"latin", "latin-ext"}
FREDOKA = HERE.parent.parent.parent / "studio-video/assets/vendor/fonts/Fredoka-Variable.woff2"


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=60).read()


def main() -> None:
    FONTS.mkdir(parents=True, exist_ok=True)
    css = get(CSS_URL).decode("utf-8")

    # Le CSS de Google est une suite de « /* subset */ @font-face { … } ».
    blocks = re.findall(r"/\*\s*([\w-]+)\s*\*/\s*(@font-face\s*\{[^}]*\})", css)

    # Inter est servie en police VARIABLE : le même woff2 couvre toutes les
    # graisses, et Google le répète dans un bloc par graisse. On garde un seul
    # @font-face par (famille, sous-set), avec une plage `font-weight`, sinon le
    # même mégaoctet de base64 est recopié seize fois.
    uniq: dict[tuple[str, str], dict] = {}
    for subset, block in blocks:
        if subset not in KEEP_SUBSETS:
            continue
        family = re.search(r"font-family:\s*'([^']+)'", block).group(1)
        url = re.search(r"url\((https://fonts\.gstatic\.com[^)]+)\)", block).group(1)
        weight = int(re.search(r"font-weight:\s*(\d+)", block).group(1))
        rng = re.search(r"unicode-range:\s*([^;]+);", block).group(1).strip()
        entry = uniq.setdefault(
            (family, subset), {"url": url, "range": rng, "weights": set()}
        )
        entry["weights"].add(weight)

    # Fredoka vient du dépôt, pas du réseau : une seule déclaration, plage de
    # graisses complète (c'est un fichier variable 300-700).
    fredoka = base64.b64encode(FREDOKA.read_bytes()).decode("ascii")
    print(f"  Fredoka   (dépôt)     {len(fredoka) // 1024} Ko b64")
    out = [
        "@font-face{font-family:'Fredoka';font-style:normal;font-weight:300 700;"
        f"font-display:block;src:url(data:font/woff2;base64,{fredoka}) format('woff2');}}"
    ]

    cache = {}
    for (family, subset), e in uniq.items():
        if e["url"] not in cache:
            cache[e["url"]] = base64.b64encode(get(e["url"])).decode("ascii")
            print(f"  {family:9s} {subset:10s} {len(cache[e['url']]) // 1024} Ko b64")
        lo, hi = min(e["weights"]), max(e["weights"])
        out.append(
            f"@font-face{{font-family:'{family}';font-style:normal;"
            f"font-weight:{lo} {hi};font-display:block;"
            f"src:url(data:font/woff2;base64,{cache[e['url']]}) format('woff2');"
            f"unicode-range:{e['range']};}}"
        )

    target = FONTS / "fonts.css"
    target.write_text(
        "/* Généré par tools/fetch_fonts.py — ne pas éditer à la main.\n"
        "   Fredoka (titres, depuis le dépôt) + Inter (corps, sous-sets latin), inlinées en base64. */\n"
        + "\n".join(out)
        + "\n",
        encoding="utf-8",
    )
    print(f"-> {target} ({target.stat().st_size / 1024:.0f} Ko, {len(out)} @font-face)")


if __name__ == "__main__":
    main()
