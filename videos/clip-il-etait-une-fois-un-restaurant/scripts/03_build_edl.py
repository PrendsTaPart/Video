#!/usr/bin/env python3
"""Étape 3 — construit l'EDL (work/edl.json) : quel plan, quand, combien de temps.

L'ordre narratif est imposé par le brief et ne se déduit pas de la musique ;
la musique décide seulement OÙ tombent les coupes (calage sur la grille de temps).

  intro + couplet 1 → actes « avant-cuisine » puis « avant-salle », plans 4–6 s
  pré-refrains       → « avant-bureau », plans 3 s
  refrains 1 et 2    → « apres-salle » + « apres-bureau », coupe sur chaque temps fort (2 s)
  couplet 2          → « avant-client », bascule sur EP522 pile sur « quelqu'un a décroché »,
                       puis EP523 et EP524
  pont               → EP525 en plan long, ralenti 0,85×, sans coupe
  refrain final      → « final » EP526→EP534, coupes 1,5 s → 1 s (accélération),
                       EP533 et EP534 calés sur leurs vers
  outro              → EP535, puis fondu au noir (étape 5)
"""

from __future__ import annotations

import argparse
import statistics
from pathlib import Path

import common

XFADE_SEC = 0.3          # fondu à chaque changement d'acte
PONT_SPEED = 0.85        # ralenti du pont
PONT_SPEED_MIN = 0.6     # au-delà, le ralenti devient de la bouillie
MIN_SEGMENT = 0.6        # aucun plan plus court que ça, même après calage


# ---------------------------------------------------------------- sections

def resolve_sections(structure: dict, duration: float, downbeats: list[float]) -> list[dict]:
    """Répartit les sections sur la durée réelle, puis cale chaque frontière sur un temps fort."""
    sections = structure["sections"]
    total_bars = sum(s["bars"] for s in sections)
    edges = [0.0]
    for section in sections:
        edges.append(edges[-1] + duration * section["bars"] / total_bars)
    edges[-1] = duration

    if downbeats:
        for i in range(1, len(edges) - 1):
            floor = edges[i - 1] + MIN_SEGMENT
            ceiling = duration - MIN_SEGMENT
            candidate = min(downbeats, key=lambda t: abs(t - edges[i]))
            if floor <= candidate <= ceiling:
                edges[i] = candidate

    return [
        {
            "id": section["id"],
            "label": section["label"],
            "start": round(edges[i], 3),
            "end": round(edges[i + 1], 3),
            "duration": round(edges[i + 1] - edges[i], 3),
        }
        for i, section in enumerate(sections)
    ]


def apply_overrides(sections: list[dict], override: Path) -> list[dict]:
    """work/sections.override.json : {"sections":[{"id":..,"start_sec":..,"end_sec":..}]}"""
    if not override.exists():
        return sections
    data = common.read_json(override)
    by_id = {s["id"]: s for s in data.get("sections", [])}
    for section in sections:
        patch = by_id.get(section["id"])
        if not patch:
            continue
        section["start"] = round(float(patch.get("start_sec", section["start"])), 3)
        section["end"] = round(float(patch.get("end_sec", section["end"])), 3)
        section["duration"] = round(section["end"] - section["start"], 3)
    print(f"= calage manuel appliqué depuis {override.relative_to(common.PROJECT)}")
    return sections


# ---------------------------------------------------------------- grilles

def snap(target: float, grid: list[float], low: float, high: float) -> float:
    """Ramène `target` sur le point de grille le plus proche dans [low, high]."""
    inside = [t for t in grid if low <= t <= high]
    if not inside:
        return max(low, min(target, high))
    return min(inside, key=lambda t: abs(t - target))


def weak_beats(beats: list[float], strength: list[float]) -> list[float]:
    """Les temps « faibles » : énergie sous la médiane — pour les coupes douces des couplets."""
    if not strength or len(strength) != len(beats):
        return beats
    median = statistics.median(strength)
    weak = [t for t, s in zip(beats, strength) if s <= median]
    return weak or beats


# ---------------------------------------------------------------- plans

class Pool:
    """Distribue les plans d'un acte sans jamais répéter deux fois de suite le même,
    et en décalant le point d'entrée à chaque réutilisation."""

    def __init__(self, rushes: dict[str, dict]):
        self.rushes = rushes
        self.uses: dict[str, int] = {}
        self.last: str | None = None
        self.rotation = 0

    def rotate(self) -> None:
        """Décale l'ordre de service : deux refrains sur le même pool ne se rejouent
        pas dans le même ordre, sinon le montage a l'air de boucler."""
        self.rotation += 1

    def pick(self, candidates: list[str]) -> str:
        available = [ep for ep in candidates if ep in self.rushes]
        if not available:
            raise common.StepError(f"aucun rush disponible parmi {candidates}")
        choices = [ep for ep in available if ep != self.last] or available
        chosen = min(
            choices,
            key=lambda ep: (self.uses.get(ep, 0), (available.index(ep) + self.rotation) % len(available)),
        )
        self.last = chosen
        return chosen

    def take(self, ep: str, length: float, speed: float = 1.0) -> tuple[float, float]:
        """Renvoie (in_point, longueur réellement tenable) pour ce plan."""
        source_needed = length * speed
        rush_duration = self.rushes[ep]["duration"]
        usable = max(0.0, rush_duration - source_needed - 0.05)
        index = self.uses.get(ep, 0)
        in_point = round((index * 2.3) % usable, 3) if usable > 0.05 else 0.0
        self.uses[ep] = index + 1
        held = min(length, (rush_duration - in_point - 0.05) / speed)
        return in_point, round(held, 3)


def cut_lengths(section: dict, start: float, end: float, first: float, last: float) -> list[float]:
    """Longueurs cibles de `start` à `end`, interpolées de `first` vers `last`."""
    span = end - start
    lengths: list[float] = []
    consumed = 0.0
    while span - consumed > MIN_SEGMENT:
        progress = consumed / span if span else 0.0
        target = first + (last - first) * progress
        target = min(target, span - consumed)
        lengths.append(target)
        consumed += target
    if lengths and span - consumed > 0:
        lengths[-1] += span - consumed
    return lengths or [span]


def fill(section: dict, candidates: list[str], pool: Pool, rushes: dict, grid: list[float],
         first: float, last: float, *, start: float | None = None, end: float | None = None,
         forced: list[str] | None = None) -> list[dict]:
    """Découpe [start, end] en plans du pool, chaque frontière calée sur la grille."""
    start = section["start"] if start is None else start
    end = section["end"] if end is None else end
    segments: list[dict] = []
    cursor = start
    targets = cut_lengths(section, start, end, first, last)
    forced = list(forced or [])

    for index, target in enumerate(targets):
        is_last = index == len(targets) - 1
        raw_end = cursor + target
        boundary = end if is_last else snap(
            raw_end, grid, cursor + max(MIN_SEGMENT, target * 0.55), min(end, cursor + target * 1.6)
        )
        if end - boundary < MIN_SEGMENT:
            boundary = end
        length = round(boundary - cursor, 3)
        if length < MIN_SEGMENT and segments:
            segments[-1]["end"] = round(end, 3)
            segments[-1]["len"] = round(segments[-1]["end"] - segments[-1]["start"], 3)
            break

        imposed = bool(forced)
        ep = forced.pop(0) if forced else pool.pick(candidates)
        pool.last = ep
        in_point, held = pool.take(ep, length)
        segments.append({
            "forced": imposed,
            "ep": ep,
            "acte": rushes[ep]["acte"],
            "titre": rushes[ep]["titre"],
            "section": section["id"],
            "start": round(cursor, 3),
            "end": round(boundary, 3),
            "len": length,
            "in_point": in_point,
            "speed": round(length / held, 4) if held < length - 0.01 else 1.0,
        })
        cursor = boundary
        if cursor >= end - 0.001:
            break

    if segments:
        segments[-1]["end"] = round(end, 3)
        segments[-1]["len"] = round(segments[-1]["end"] - segments[-1]["start"], 3)
        # Un résidu de fin de section (moitié du plan visé) ferait une coupe parasite :
        # on l'absorbe dans le plan précédent, sauf si c'est un plan imposé par le brief.
        reference = min(targets[-1], segments[-2]["len"]) if len(segments) > 1 else targets[-1]
        if len(segments) > 1 and not segments[-1]["forced"] and segments[-1]["len"] < reference * 0.6:
            stub = segments.pop()
            segments[-1]["end"] = stub["end"]
            segments[-1]["len"] = round(segments[-1]["end"] - segments[-1]["start"], 3)
    return segments


def anchor_time(structure: dict, sections: dict[str, dict], anchor_id: str) -> float | None:
    for anchor in structure.get("anchors", []):
        if anchor["id"] != anchor_id:
            continue
        section = sections.get(anchor["section"])
        if not section:
            return None
        return section["start"] + section["duration"] * float(anchor["fraction"])
    return None


# ---------------------------------------------------------------- montage

def build(beats: dict, rushes: dict, structure: dict, sections: list[dict]) -> list[dict]:
    grid_all = beats["beats_sec"]
    grid_strong = beats["downbeats_sec"] or grid_all
    grid_weak = weak_beats(grid_all, beats.get("beat_strength", []))
    by_id = {s["id"]: s for s in sections}
    pool = Pool(rushes)

    def actes(*names: str) -> list[str]:
        return [ep for ep, r in sorted(rushes.items()) if r["acte"] in names]

    avant_cuisine = actes("avant-cuisine")
    avant_salle = actes("avant-salle")
    avant_bureau = actes("avant-bureau")
    apres_refrain = [ep for ep in ("EP510", "EP511", "EP516", "EP517", "EP518") if ep in rushes]
    avant_client = actes("avant-client")
    # EP533 et EP534 sont réservés à leurs vers (« le Z avant d'éteindre », « sept heures
    # du matin ») : les laisser dans le pool de remplissage diluerait leur arrivée.
    final = [ep for ep in sorted(actes("final")) if ep not in ("EP525", "EP535", "EP533", "EP534")]

    segments: list[dict] = []

    # Intro — EP501 ouvre le clip, plan long, aucune coupe avant le premier couplet.
    intro = by_id["intro"]
    segments += fill(intro, avant_cuisine, pool, rushes, grid_weak, 6.0, 5.0,
                     forced=["EP501"])

    # Couplet 1 — la cuisine d'abord, la salle ensuite (l'ordre du brief), jamais mélangées :
    # la bascule tombe au milieu du couplet, calée sur un temps fort.
    pool.rotate()
    couplet1 = by_id["couplet1"]
    passage = snap(couplet1["start"] + couplet1["duration"] * 0.5, grid_strong,
                   couplet1["start"] + MIN_SEGMENT, couplet1["end"] - MIN_SEGMENT)
    segments += fill(couplet1, avant_cuisine, pool, rushes, grid_weak, 5.0, 4.5,
                     start=couplet1["start"], end=passage)
    segments += fill(couplet1, avant_salle, pool, rushes, grid_weak, 4.5, 4.0,
                     start=passage, end=couplet1["end"])

    # Pré-refrain 1 — le bureau, les plans raccourcissent à 3 s.
    pool.rotate()
    segments += fill(by_id["prerefrain1"], avant_bureau, pool, rushes, grid_all, 3.0, 3.0)

    # Refrain 1 — l'« après », coupe sur chaque temps fort (2 s).
    pool.rotate()
    segments += fill(by_id["refrain1"], apres_refrain, pool, rushes, grid_strong, 2.0, 2.0)

    # Couplet 2 — « avant-client », puis bascule EP522 / EP523 / EP524 sur l'ancre.
    couplet2 = by_id["couplet2"]
    switch = anchor_time(structure, by_id, "quelqu-un-a-decroche") or (
        couplet2["start"] + couplet2["duration"] * 0.5
    )
    switch = snap(switch, grid_strong, couplet2["start"] + MIN_SEGMENT, couplet2["end"] - MIN_SEGMENT)
    segments += fill(couplet2, avant_client, pool, rushes, grid_weak, 4.0, 3.0,
                     start=couplet2["start"], end=switch)
    decroche = [ep for ep in ("EP522", "EP523", "EP524") if ep in rushes]
    segments += fill(couplet2, decroche, pool, rushes, grid_all, 3.0, 2.5,
                     start=switch, end=couplet2["end"], forced=decroche)

    # Pré-refrain 2 — retour au bureau, 3 s.
    pool.rotate()
    segments += fill(by_id["prerefrain2"], avant_bureau, pool, rushes, grid_all, 3.0, 3.0)

    # Refrain 2 — même grammaire que le refrain 1.
    pool.rotate()
    segments += fill(by_id["refrain2"], apres_refrain, pool, rushes, grid_strong, 2.0, 2.0)

    # Pont — EP525 seul, ralenti, aucune coupe.
    pont = by_id["pont"]
    if "EP525" in rushes:
        rush_duration = rushes["EP525"]["duration"]
        start = pont["start"]
        # 0,85× ne tient que rush/0,85 secondes. Si le pont est plus long, on ralentit
        # davantage — jamais sous PONT_SPEED_MIN, au-delà l'image devient de la bouillie —
        # et le reliquat de tête est couvert par un plan « final ».
        if pont["duration"] > rush_duration / PONT_SPEED_MIN:
            head_end = snap(pont["end"] - rush_duration / PONT_SPEED_MIN, grid_all,
                            pont["start"] + MIN_SEGMENT, pont["end"] - MIN_SEGMENT)
            segments += fill(pont, final, pool, rushes, grid_all, 3.0, 3.0,
                             start=pont["start"], end=head_end)
            start = head_end
        span = pont["end"] - start
        segments.append({
            "forced": True,
            "ep": "EP525", "acte": rushes["EP525"]["acte"], "titre": rushes["EP525"]["titre"],
            "section": "pont", "start": round(start, 3), "end": pont["end"],
            "len": round(span, 3), "in_point": 0.0,
            "speed": round(min(PONT_SPEED, rush_duration / span), 4),
        })
        pool.last = "EP525"
        pool.uses["EP525"] = pool.uses.get("EP525", 0) + 1
    else:
        segments += fill(pont, final, pool, rushes, grid_all, 3.0, 3.0)

    # Refrain final — montage court qui accélère, EP533 et EP534 sur leurs vers.
    refrain_final = by_id["refrain_final"]
    z_time = anchor_time(structure, by_id, "le-z-avant-d-eteindre")
    lendemain = anchor_time(structure, by_id, "sept-heures-le-lendemain")
    marks = []
    for time, ep in ((z_time, "EP533"), (lendemain, "EP534")):
        if time is None or ep not in rushes:
            continue
        low = refrain_final["start"] + MIN_SEGMENT
        high = refrain_final["end"] - MIN_SEGMENT
        marks.append((snap(time, grid_strong, low, high), ep))
    marks.sort()

    cursor = refrain_final["start"]
    for mark_time, ep in marks:
        if mark_time - cursor > MIN_SEGMENT:
            segments += fill(refrain_final, final, pool, rushes, grid_strong, 1.5, 1.0,
                             start=cursor, end=mark_time)
        end = min(refrain_final["end"], mark_time + 1.5)
        end = snap(end, grid_strong, mark_time + MIN_SEGMENT, min(refrain_final["end"], mark_time + 2.2))
        segments += fill(refrain_final, [ep], pool, rushes, grid_strong, end - mark_time, end - mark_time,
                         start=mark_time, end=end, forced=[ep])
        cursor = end
    if refrain_final["end"] - cursor > MIN_SEGMENT:
        segments += fill(refrain_final, final, pool, rushes, grid_strong, 1.5, 1.0,
                         start=cursor, end=refrain_final["end"])

    # Outro — EP535 jusqu'au bout ; si la section dépasse le rush, on le ralentit,
    # et au-delà de 0,5× on fait précéder un plan « final » pour couvrir la tête.
    outro = by_id["outro"]
    if "EP535" in rushes:
        rush_duration = rushes["EP535"]["duration"]
        start = outro["start"]
        if outro["duration"] > rush_duration / 0.5:
            head_end = snap(outro["end"] - rush_duration / 0.5, grid_all,
                            outro["start"] + MIN_SEGMENT, outro["end"] - MIN_SEGMENT)
            segments += fill(outro, final, pool, rushes, grid_all, 2.0, 2.0,
                             start=outro["start"], end=head_end)
            start = head_end
        span = outro["end"] - start
        segments.append({
            "forced": True,
            "ep": "EP535", "acte": rushes["EP535"]["acte"], "titre": rushes["EP535"]["titre"],
            "section": "outro", "start": round(start, 3), "end": outro["end"],
            "len": round(span, 3), "in_point": 0.0,
            # 0,08 s de marge : sans elle le ralenti demanderait la toute dernière image
            # du rush et le rendu sortirait court d'une frame.
            "speed": round(min(1.0, (rush_duration - 0.08) / span), 4),
        })
    else:
        segments += fill(outro, final, pool, rushes, grid_all, 2.0, 2.0)

    return segments


def annotate(segments: list[dict], duration: float) -> list[dict]:
    """Numérote, pose les transitions (fondu 0,3 s à chaque changement d'acte) et les runs."""
    segments = [s for s in segments if s["len"] >= 0.2]
    segments.sort(key=lambda s: s["start"])

    # Chaque frontière est ramenée sur la grille d'images : un plan ne peut durer qu'un
    # nombre entier d'images à 30 i/s. Sans ça, 107 arrondis de rendu s'additionnent et
    # le montage finit décalé de plusieurs dixièmes par rapport à la chanson.
    def to_frame(t: float) -> float:
        return round(round(t * common.FPS) / common.FPS, 6)

    for segment in segments:
        segment["start"] = to_frame(segment["start"])

    # Recolle les frontières : le montage doit tuiler la chanson sans trou.
    for previous, current in zip(segments, segments[1:]):
        previous["end"] = current["start"]
        previous["len"] = round(previous["end"] - previous["start"], 6)
    segments[-1]["end"] = to_frame(duration)
    segments[-1]["len"] = round(segments[-1]["end"] - segments[-1]["start"], 6)

    def grade_of(segment: dict) -> str:
        return "froid" if segment["acte"] in common.ACTES_FROIDS else "chaud"

    run = 0
    for index, segment in enumerate(segments):
        nxt = segments[index + 1] if index + 1 < len(segments) else None
        # « Changement d'acte » au sens du montage = la bascule avant ↔ après, celle que
        # l'étalonnage rend visible (froid → chaud). Les alternances internes à un bloc
        # (salle ↔ bureau dans un refrain) restent des coupes franches sur le temps fort :
        # fondre un plan sur deux tuerait le montage sur les temps forts demandé au refrain.
        act_change = bool(nxt) and grade_of(nxt) != grade_of(segment)
        segment["index"] = index
        segment["id"] = f"{index:03d}-{segment['ep']}"
        segment["grade"] = grade_of(segment)
        segment["transition_out"] = "xfade" if act_change else ("cut" if nxt else "fin")
        segment["overlap_out"] = XFADE_SEC if act_change else 0.0
        # Le plan sortant est rendu 0,3 s plus long : le fondu mange ce rab, la
        # timeline musicale reste exactement à sa place.
        segment["render_len"] = round(segment["len"] + segment["overlap_out"], 6)
        segment["source_len"] = round(segment["render_len"] * segment.get("speed", 1.0), 6)
        segment["run"] = run
        segment["src"] = f"rushes/{segment['ep']}.mp4"
        if act_change:
            run += 1
    return segments


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--beats", default=str(common.WORK / "beats.json"))
    parser.add_argument("--out", default=str(common.WORK / "edl.json"))
    args = parser.parse_args()

    beats = common.read_json(Path(args.beats))
    rush_data = common.read_json(common.WORK / "rushes.json")
    rushes = {r["ep"]: r for r in rush_data["rushes"] if r.get("status") == "ok"}
    if not rushes:
        common.die("aucun rush valide — joue d'abord scripts/01_fetch_rushes.py")
    structure = common.load_structure()

    duration = beats["duration_sec"]
    sections = apply_overrides(
        resolve_sections(structure, duration, beats.get("downbeats_sec", [])),
        common.WORK / "sections.override.json",
    )
    segments = annotate(build(beats, rushes, structure, sections), duration)

    payload = {
        "song": beats["source"],
        "duration_sec": round(duration, 3),
        "bpm": beats["bpm"],
        "beat_engine": beats["engine"],
        "width": common.W, "height": common.H, "fps": common.FPS,
        "xfade_sec": XFADE_SEC,
        "sections": sections,
        "segments": segments,
        "missing_rushes": rush_data.get("missing", []),
    }
    common.write_json(Path(args.out), payload)

    print(f"\n{'#':>3}  {'début':>9}  {'durée':>6}  {'EP':7} {'acte':14} {'grade':6} {'trans':6} titre")
    print("-" * 104)
    for segment in segments:
        print(
            f"{segment['index']:3d}  {common.timecode(segment['start']):>9}  {segment['len']:5.2f}s  "
            f"{segment['ep']:7} {segment['acte']:14} {segment['grade']:6} {segment['transition_out']:6} {segment['titre']}"
        )

    total = sum(s["len"] for s in segments)
    print(f"\n{len(segments)} plans · {total:.2f}s montés pour {duration:.2f}s de chanson")
    if abs(total - duration) > 1.0 / common.FPS:
        common.die(f"le montage ne couvre pas la chanson (écart {total - duration:+.3f}s)")
    for previous, current in zip(segments, segments[1:]):
        if previous["ep"] == current["ep"]:
            common.die(f"plan répété consécutivement : {previous['ep']} aux index {previous['index']}/{current['index']}")
    print("✓ EDL cohérente : tuile toute la chanson, aucun plan répété consécutivement.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
