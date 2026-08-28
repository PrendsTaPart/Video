import decouverte from "@/assets/poses/pose-decouverte.png.asset.json";
import pointeGauche from "@/assets/poses/pose-pointe-gauche.png.asset.json";
import victoire from "@/assets/poses/pose-victoire.png.asset.json";
import laptop from "@/assets/poses/pose-laptop.png.asset.json";
import checklist from "@/assets/poses/pose-checklist.png.asset.json";
import casque from "@/assets/poses/pose-casque.png.asset.json";
import dossier from "@/assets/poses/pose-dossier.png.asset.json";
import stop from "@/assets/poses/pose-stop.png.asset.json";
import presentePaume from "@/assets/poses/pose-presente-paume.png.asset.json";

export type NomPose =
  | "decouverte"
  | "pointe-gauche"
  | "victoire"
  | "laptop"
  | "checklist"
  | "casque"
  | "dossier"
  | "stop"
  | "presente-paume";

/** Portraits de l'assistant, servis depuis le CDN. */
export const POSES: Record<NomPose, string> = {
  decouverte: decouverte.url,
  "pointe-gauche": pointeGauche.url,
  victoire: victoire.url,
  laptop: laptop.url,
  checklist: checklist.url,
  casque: casque.url,
  dossier: dossier.url,
  stop: stop.url,
  "presente-paume": presentePaume.url,
};

const ROTATION: NomPose[] = [
  "presente-paume",
  "pointe-gauche",
  "laptop",
  "checklist",
  "decouverte",
  "dossier",
  "casque",
  "victoire",
];

/**
 * Choisit la pose la plus parlante pour une réponse : d'abord selon le ton du
 * message, sinon en rotation pour éviter de répéter le même portrait.
 */
export function choisirPose(texte: string, index = 0): NomPose {
  const t = texte.toLowerCase();
  if (/(désolé|impossible|erreur|attention|indisponible|ne peux pas)/.test(t)) return "stop";
  if (/(bravo|parfait|félicitations|c'est fait|terminé|réussi)/.test(t)) return "victoire";
  if (/(étape|checklist|liste|1\.|2\.|d'abord|ensuite)/.test(t)) return "checklist";
  if (/(vidéo|tutoriel|regardez|formation|leçon)/.test(t)) return "pointe-gauche";
  if (/(connect|mcp|configur|paramètr|installer|brancher)/.test(t)) return "laptop";
  if (/(document|facture|dossier|contenu|bibliothèque)/.test(t)) return "dossier";
  if (/(aide|support|contact|question)/.test(t)) return "casque";
  return ROTATION[index % ROTATION.length]!;
}
