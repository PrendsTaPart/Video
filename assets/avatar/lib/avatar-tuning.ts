/**
 * Réglages de l'avatar, en un seul endroit.
 *
 * Ces valeurs étaient dispersées en littéraux dans `lipsync-engine`, `face-idle`
 * et le canvas. Les regrouper ici sert deux choses :
 *
 * 1. chaque module lit son défaut au même endroit, donc un réglage validé se
 *    change à un seul point ;
 * 2. la console `/debug/avatar` peut exporter un objet de **cette forme exacte**,
 *    prêt à coller ici — le va-et-vient entre l'oreille et le code se réduit à
 *    un copier-coller.
 *
 * Aucun de ces nombres n'est deviné : ce sont les valeurs actuellement en
 * production, extraites telles quelles.
 */

export type AvatarTuning = {
  /** Décalage de synchro labiale (ms). Positif = bouche en avance sur l'audio. */
  calibrationMs: number;
  /** Fenêtre de recouvrement entre visèmes (ms). Bornée à 40–70 par le moteur. */
  overlapMs: number;
  /** Amplitude minimale appliquée aux poids de visèmes (signal faible). */
  amplitudeMin: number;
  /** Amplitude maximale (signal fort). */
  amplitudeMax: number;
  /** Ouverture maximale de la mâchoire. */
  maxJaw: number;
  /**
   * Freinage de la mâchoire par l'indice de fricative, 0..1.
   * 0 = un « sss » ouvre autant qu'un « aaa » ; 1 = il ferme complètement.
   */
  fricativeDamping: number;
  /**
   * Intensité de la micro-vie du visage (respiration, balancement, saccades).
   * 1 = nominal, 0 = figé.
   */
  vitality: number;
  /** Images par seconde du moteur de rendu. */
  modelFPS: number;
};

export const DEFAULT_TUNING: AvatarTuning = {
  calibrationMs: 0,
  overlapMs: 55,
  amplitudeMin: 0.6,
  amplitudeMax: 1.15,
  maxJaw: 0.45,
  fricativeDamping: 0.65,
  vitality: 1,
  modelFPS: 60,
};

/* ------------------------------------------------------------------ *
 * Placement de l'avatar dans le cadre
 * ------------------------------------------------------------------ */

/** Vues de caméra supportées par le moteur. */
export type CameraView = "full" | "mid" | "upper" | "head";

/**
 * Placement de l'avatar : quelle vue, et comment on la décale.
 *
 * `cameraY` monte ou descend le point visé, `cameraDistance` recule (valeurs
 * négatives) ou rapproche, `cameraX` décentre horizontalement, et les deux
 * rotations inclinent la prise de vue. Ces valeurs étaient figées dans
 * `framingFor()` : les sortir ici les rend réglables au banc puis exportables.
 */
export type AvatarPlacement = {
  view: CameraView;
  cameraX: number;
  cameraY: number;
  cameraDistance: number;
  cameraRotateX: number;
  cameraRotateY: number;
};

/**
 * Deux cadrages : un pour les panneaux étroits (mobile), un pour les larges.
 * Le seuil de bascule est `NARROW_BREAKPOINT_PX`.
 */
export type AvatarPlacements = { narrow: AvatarPlacement; wide: AvatarPlacement };

export const NARROW_BREAKPOINT_PX = 420;

/**
 * Cadrage « toque + épaules ».
 *
 * Mesuré sur le modèle, pas deviné : la silhouette monte jusqu'à y = 1.828 en
 * repère monde (le haut de la toque), les yeux sont à 1.732, la demi-largeur
 * d'épaules vaut 0.353. Le cadrage précédent (`cameraY 0.32`,
 * `cameraDistance -1.05`) projetait le haut de la toque à **+1.14 en NDC**,
 * c'est-à-dire hors cadre : le chapeau était coupé quel que soit le rapport
 * d'image. Les valeurs ci-dessous le ramènent à +0.69 (bureau) et +0.63
 * (étroit), avec les yeux au tiers haut.
 *
 * Rappel utile au réglage : `cameraDistance` s'ajoute à la distance de la vue
 * (`upper` = 4.5), donc **moins négatif = caméra plus loin = cadre plus large**.
 * Le cadrage vertical ne dépend pas du rapport d'image (le champ est vertical) ;
 * seule la place pour les épaules en dépend, d'où le recul supplémentaire sur
 * les panneaux étroits.
 */
export const DEFAULT_PLACEMENT: AvatarPlacements = {
  narrow: {
    view: "upper",
    cameraX: 0,
    cameraY: 0.08,
    cameraDistance: -0.45,
    cameraRotateX: 0,
    cameraRotateY: 0,
  },
  wide: {
    view: "upper",
    cameraX: 0,
    cameraY: 0.08,
    cameraDistance: -0.6,
    cameraRotateX: 0,
    cameraRotateY: 0,
  },
};

/**
 * Cadrage du médaillon incrusté dans le lecteur vidéo.
 *
 * La lucarne est **ronde** : le cadre utile n'est pas le rectangle du canvas
 * mais son cercle inscrit, plus petit d'environ 30 % dans les coins. On recule
 * donc la caméra par rapport au cadrage de panneau (`cameraDistance` moins
 * négatif = caméra plus loin = cadre plus large, cf. ci-dessus) pour que la
 * toque et les épaules restent à l'intérieur du disque, et on redescend
 * légèrement le point visé pour centrer le buste dans le cercle plutôt que de
 * le poser au tiers haut comme dans le panneau.
 */
export const MEDALLION_PLACEMENT: AvatarPlacement = {
  view: "upper",
  cameraX: 0,
  cameraY: 0.04,
  cameraDistance: -0.25,
  cameraRotateX: 0,
  cameraRotateY: 0,
};
