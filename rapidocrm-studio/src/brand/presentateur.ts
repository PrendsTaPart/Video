/**
 * La banque d'images du présentateur RapidoCRM, partagée par les 172 tutoriels.
 * Les fichiers vivent dans assets/presentateur/ et sont copiés dans public/ au
 * rendu. On ne régénère jamais ces photos : on pioche dedans.
 */

export type PosePresentateur =
  | 'surpris'
  | 'pointe-gauche'
  | 'pointe-droite'
  | 'victoire'
  | 'ordinateur'
  | 'presse-papier'
  | 'presse-papier-2'
  | 'casque-pouce'
  | 'dossier'
  | 'stop'
  | 'reflexion'
  | 'presentation'
  | 'accueil-cravate'
  | 'bras-ouverts'
  | 'deux-pouces'
  | 'ok';

export interface FichePose {
  pose: PosePresentateur;
  /** Ce que la pose raconte — sert à choisir sans regarder les fichiers. */
  intention: string;
  /** Côté vers lequel le regard ou le geste porte : le texte va en face. */
  regard: 'gauche' | 'droite' | 'face';
}

export const POSES: FichePose[] = [
  { pose: 'surpris', intention: 'la douleur, l\'étonnement — pour un hook qui pointe un problème', regard: 'face' },
  { pose: 'reflexion', intention: 'la question qu\'on se pose — hook interrogatif', regard: 'face' },
  { pose: 'stop', intention: 'l\'erreur à ne pas commettre — hook « arrêtez de… »', regard: 'face' },
  { pose: 'pointe-gauche', intention: 'désigne un élément placé à sa gauche', regard: 'gauche' },
  { pose: 'pointe-droite', intention: 'désigne un élément placé à sa droite', regard: 'droite' },
  { pose: 'presentation', intention: 'présente une idée, paume ouverte', regard: 'gauche' },
  { pose: 'ordinateur', intention: 'la démonstration à l\'écran', regard: 'face' },
  { pose: 'presse-papier', intention: 'la checklist, les étapes à suivre', regard: 'face' },
  { pose: 'presse-papier-2', intention: 'la checklist, variante', regard: 'face' },
  { pose: 'dossier', intention: 'les documents, la gestion administrative', regard: 'face' },
  { pose: 'casque-pouce', intention: 'le support, l\'accompagnement', regard: 'face' },
  { pose: 'accueil-cravate', intention: 'l\'accueil posé, l\'ouverture de tutoriel', regard: 'face' },
  { pose: 'bras-ouverts', intention: 'l\'invitation, la bienvenue', regard: 'face' },
  { pose: 'victoire', intention: 'le résultat obtenu — fin de tutoriel', regard: 'face' },
  { pose: 'deux-pouces', intention: 'c\'est fait, c\'est validé — fin de tutoriel', regard: 'face' },
  { pose: 'ok', intention: 'c\'est réglé, tout est en ordre — fin de tutoriel', regard: 'face' },
];

/** Poses réservées au hook : elles racontent le problème, pas la solution. */
export const POSES_HOOK: PosePresentateur[] = [
  'surpris',
  'reflexion',
  'stop',
  'pointe-droite',
  'pointe-gauche',
  'presentation',
  'presse-papier',
  'ordinateur',
];

/** Poses réservées à l'image de fin : elles racontent le résultat. */
export const POSES_FIN: PosePresentateur[] = [
  'victoire',
  'deux-pouces',
  'ok',
  'casque-pouce',
  'bras-ouverts',
  'accueil-cravate',
];

/** Chemin staticFile d'une pose. */
export const cheminPose = (pose: PosePresentateur): string =>
  `presentateur/${pose}.webp`;

/**
 * Choix déterministe et réparti : deux tutoriels voisins n'ont pas la même
 * pose, et un même tutoriel garde la sienne d'un rendu à l'autre.
 */
const empreinte = (graine: string): number => {
  let h = 0;
  for (const c of graine) h = (h * 31 + c.charCodeAt(0)) % 100_000;
  return h;
};

export const poseHook = (module: string, numero: number): PosePresentateur =>
  POSES_HOOK[empreinte(`${module}-hook-${numero}`) % POSES_HOOK.length] as PosePresentateur;

export const poseFin = (module: string, numero: number): PosePresentateur =>
  POSES_FIN[empreinte(`${module}-fin-${numero}`) % POSES_FIN.length] as PosePresentateur;
