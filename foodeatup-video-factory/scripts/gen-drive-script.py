#!/usr/bin/env python3
"""Génère l'Apps Script qui prépare les 150 dossiers épisode sur le Drive.

Pourquoi un Apps Script et pas des appels API depuis ici : la structure complète
fait ~900 dossiers et ~750 fichiers. Créés un par un à distance, c'est des heures
de latence réseau. Exécuté dans Apps Script, c'est quelques minutes côté Google.

Le script produit est IDEMPOTENT (il saute ce qui existe) et REPRENABLE : Apps
Script coupe à 6 minutes, donc il mémorise sa progression et il suffit de le
relancer, ou de laisser le déclencheur horaire finir le travail.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "content" / "episodes.json").read_text(encoding="utf-8"))
hf = json.loads((ROOT / "content" / "prompts-higgsfield.json").read_text(encoding="utf-8"))

eps = []
for e in data["episodes"]:
    eid = f"EP{e['n']:03d}"
    eps.append({
        "id": eid,
        "n": e["n"],
        "t": e["t"],
        "mod": e["mod"],
        "ch": e["ch"],
        "drive": data["modules"][e["mod"]],
        "hook": e["hook"],
        "punch": e["punch"],
        "heygen": e["heygen"],
        "hf": hf.get(eid, ""),
    })

gs = """/**
 * FoodEatUp — prépare les 150 dossiers épisode sur le Drive de production.
 *
 * Généré par scripts/gen-drive-script.py. Ne pas éditer à la main : régénérer.
 *
 * INSTALLATION
 *   1. script.google.com > Nouveau projet, colle ce fichier
 *   2. Exécute creerTout()
 *   3. Apps Script coupe à 6 minutes : relance creerTout() jusqu'à voir
 *      "TERMINE". Le script reprend exactement où il s'est arrêté.
 *      (ou lance planifier() une fois : un déclencheur horaire finit seul)
 *
 * IDEMPOTENT : relançable sans risque, rien n'est jamais recréé ni écrasé.
 *
 * Pour repartir de zéro sur la progression (sans supprimer les dossiers) :
 *   reinitialiserProgression()
 */

var SAISONS = %SAISONS%;

var SOUS_DOSSIERS = ['01-PROMPTS', '02-ASSETS', '03-RESEAUX', '04-MASTERS', '05-ACADEMY'];

var LIMITE_MS = 4.5 * 60 * 1000;  // on s'arrête avant le couperet des 6 minutes

var EP = %EPISODES%;

function saisonDe(n) {
  if (n <= 30) return 1;
  if (n <= 60) return 2;
  if (n <= 90) return 3;
  if (n <= 120) return 4;
  return 5;
}

function creerTout() {
  var debut = new Date().getTime();
  var props = PropertiesService.getScriptProperties();
  var depart = parseInt(props.getProperty('curseur') || '0', 10);
  var faits = 0;

  for (var i = depart; i < EP.length; i++) {
    if (new Date().getTime() - debut > LIMITE_MS) {
      props.setProperty('curseur', String(i));
      Logger.log('Pause a l index ' + i + ' (' + EP[i].id + '). ' +
                 faits + ' episodes traites. Relance creerTout().');
      return;
    }
    creerEpisode(EP[i]);
    faits++;
  }

  props.setProperty('curseur', String(EP.length));
  Logger.log('TERMINE — ' + EP.length + ' episodes en place.');
  retirerDeclencheurs();
}

function creerEpisode(e) {
  var parent = DriveApp.getFolderById(SAISONS[saisonDe(e.n)]);
  var nom = e.id + ' - ' + e.t;

  var it = parent.getFoldersByName(nom);
  var dossier = it.hasNext() ? it.next() : parent.createFolder(nom);

  var sous = {};
  for (var i = 0; i < SOUS_DOSSIERS.length; i++) {
    sous[SOUS_DOSSIERS[i]] = sousDossier(dossier, SOUS_DOSSIERS[i]);
  }

  fichier(dossier, '00-FICHE-EPISODE-' + e.id + '.md', fiche(e));
  fichier(sous['01-PROMPTS'], '01-HIGGSFIELD-' + e.id + '.md', promptHiggsfield(e));
  fichier(sous['01-PROMPTS'], '02-HEYGEN-' + e.id + '.md', promptHeygen(e));
  fichier(sous['01-PROMPTS'], '03-ELEVENLABS-' + e.id + '.md', promptElevenlabs(e));
  fichier(sous['05-ACADEMY'], 'FICHE-ACADEMY-' + e.id + '.md', ficheAcademy(e));

  raccourci(sous['02-ASSETS'].getId(), e.drive, 'TUTO SOURCE - ' + e.mod);
}

function sousDossier(parent, nom) {
  var it = parent.getFoldersByName(nom);
  return it.hasNext() ? it.next() : parent.createFolder(nom);
}

/** N'ecrase jamais un fichier existant : l'humain a pu l'annoter. */
function fichier(dossier, nom, contenu) {
  if (dossier.getFilesByName(nom).hasNext()) return;
  dossier.createFile(nom, contenu, MimeType.PLAIN_TEXT);
}

function raccourci(parentId, cibleId, nom) {
  try {
    var parent = DriveApp.getFolderById(parentId);
    if (parent.getFilesByName(nom).hasNext()) return;
    Drive.Files.create({
      name: nom,
      mimeType: 'application/vnd.google-apps.shortcut',
      parents: [parentId],
      shortcutDetails: { targetId: cibleId }
    }, null, { supportsAllDrives: true });
  } catch (err) {
    Logger.log('Raccourci impossible (' + nom + ') : ' + err);
  }
}

function fiche(e) {
  return '# ' + e.id + ' — ' + e.t + '\\n\\n' +
    '| | |\\n|---|---|\\n' +
    '| Saison | ' + saisonDe(e.n) + ' |\\n' +
    '| Module | ' + e.mod + ' |\\n' +
    '| Chapitre | ' + e.ch + ' |\\n' +
    '| Tuto source | https://drive.google.com/drive/folders/' + e.drive + ' |\\n\\n' +
    '## Les trois fichiers a deposer dans 02-ASSETS\\n\\n' +
    '| Fichier | Ce que c est | Contrainte |\\n|---|---|---|\\n' +
    '| `' + e.id + '_hook.mp4` | clip Higgsfield 10 s | 9:16, AUCUN texte dans l image, chute a 5,0 s |\\n' +
    '| `' + e.id + '_avatar.mp4` | segment HeyGen | 10 s (max 12), avec audio, sans musique, sans sous-titres |\\n' +
    '| `' + e.id + '_soft.mp4` | extrait du tuto | 10 s ; sinon Claude Code le decoupe a la source |\\n\\n' +
    'Nommage strict : trois chiffres. Sans le zero, Drive trie EP1, EP10, EP100, EP11.\\n\\n' +
    '## Les textes de l episode\\n\\n' +
    '**Hook incruste (0,8 -> 3,5 s)**\\n\\n> ' + e.hook + '\\n\\n' +
    '**Punchline VO (5,0 s)**\\n\\n> ' + e.punch + '\\n\\n' +
    '**Script HeyGen (16,0 -> 26,0 s)**\\n\\n> ' + e.heygen + '\\n\\n' +
    '## Etat\\n\\n' +
    '- [ ] hook depose\\n- [ ] avatar depose\\n- [ ] extrait tuto\\n' +
    '- [ ] punchline generee\\n- [ ] master monte\\n- [ ] brouillons CMS crees\\n';
}

function promptHiggsfield(e) {
  return '# Prompt Higgsfield — ' + e.id + '\\n\\n' +
    'A generer TOI-MEME depuis l interface Higgsfield. Claude Code ne lance\\n' +
    'aucune generation. Telecharge le resultat en `' + e.id + '_hook.mp4`\\n' +
    'dans 02-ASSETS.\\n\\n' +
    'Modele conseille : Kling 3.0 (audio natif) ou Seedance 2.5.\\n' +
    'Format 9:16 · 1080x1920 · 10 s.\\n\\n' +
    '## Prompt\\n\\n```\\n' + e.hf + '\\n```\\n\\n' +
    '## Ce qui est verifie a la reception\\n\\n' +
    '- aucun texte, sous-titre, filigrane ni logo dans l image\\n' +
    '- la chute comique tombe a 5,0 s (c est la que la punchline arrive)\\n' +
    '- les 2 dernieres secondes tiennent le plan fige\\n' +
    '- premiere frame non noire : elle devient la vignette sur les 5 reseaux\\n';
}

function promptHeygen(e) {
  return '# Prompt HeyGen — ' + e.id + '\\n\\n' +
    'Segment D du master (16,0 -> 26,0 s). L avatar est en haut, le logiciel en bas.\\n' +
    'L avatar parle avec sa voix HeyGen. AUCUNE voix ElevenLabs sur ce segment.\\n\\n' +
    '## A coller dans HeyGen\\n\\n```\\n' +
    'Avatar : [ton avatar FoodEatUp]\\n' +
    'Format : 9:16 · 1080x1920 · duree cible 10 s (max 12 s)\\n' +
    'Cadrage : plan poitrine, avatar centre dans le tiers superieur, regard camera\\n' +
    'Fond : uni charte FoodEatUp\\n' +
    'Voix : voix FR de l avatar, debit pose, ton direct, tutoiement\\n' +
    'Musique : AUCUNE (le montage gere l audio)\\n' +
    'Sous-titres HeyGen : DESACTIVES (burn-in fait au montage)\\n' +
    'Gestes : naturels, une seule main, pas de pointage vers le bas du cadre\\n' +
    'Script : « ' + e.heygen + ' »\\n```\\n\\n' +
    '## Le screencast qui va dessous\\n\\n' +
    e.mod + ' > ' + e.ch + '\\n' +
    'https://drive.google.com/drive/folders/' + e.drive + '\\n';
}

function promptElevenlabs(e) {
  return '# Voix ElevenLabs — ' + e.id + '\\n\\n' +
    'Seule la punchline est propre a cet episode. Les trois VO fixes (VO_A, VO_B,\\n' +
    'VO_C) sont generees une fois pour les 150 et vivent dans _COMMUN.\\n\\n' +
    '## Punchline — ' + e.id + '_punchline.mp3\\n\\n' +
    '```\\n' + e.punch + '\\n```\\n\\n' +
    'Cible 2,0 a 2,5 s, plafond 2,8 s. Si le rendu depasse, RACCOURCIR LE TEXTE.\\n' +
    'Ne jamais accelerer l audio : une VO acceleree s entend.\\n\\n' +
    '## Reglages figes sur les 153 fichiers\\n\\n' +
    'stability 0.55 · similarity_boost 0.80 · style 0.15 · speaker_boost true\\n' +
    'eleven_multilingual_v2 · mp3_44100_128\\n';
}

function ficheAcademy(e) {
  return '# Fiche Academy — ' + e.id + ' ' + e.t + '\\n\\n' +
    '**Module** ' + e.mod + ' — **Chapitre** ' + e.ch + '\\n\\n' +
    '## Ce que l episode montre\\n\\n' + e.heygen + '\\n\\n' +
    '## Tutoriel complet\\n\\n' +
    'https://drive.google.com/drive/folders/' + e.drive + '\\n';
}

/** Declencheur horaire : laisse le script finir tout seul. */
function planifier() {
  retirerDeclencheurs();
  ScriptApp.newTrigger('creerTout').timeBased().everyMinutes(10).create();
  Logger.log('Declencheur pose. Il se retirera au TERMINE.');
}

function retirerDeclencheurs() {
  var t = ScriptApp.getProjectTriggers();
  for (var i = 0; i < t.length; i++) {
    if (t[i].getHandlerFunction() === 'creerTout') ScriptApp.deleteTrigger(t[i]);
  }
}

function reinitialiserProgression() {
  PropertiesService.getScriptProperties().deleteProperty('curseur');
  Logger.log('Progression remise a zero.');
}
"""

gs = gs.replace("%SAISONS%", json.dumps(data["saisons"], indent=2))
gs = gs.replace("%EPISODES%", json.dumps(eps, ensure_ascii=False, indent=1))

sortie = ROOT / "scripts" / "creer-drive-150.gs"
sortie.write_text(gs, encoding="utf-8")
print(f"{sortie.relative_to(ROOT)} — {len(gs) // 1024} Ko, {len(eps)} épisodes")
