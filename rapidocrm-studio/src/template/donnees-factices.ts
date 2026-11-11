import type { Script } from '../schema/index.ts';

/**
 * Données factices pour la composition « Preview » : elles permettent de valider
 * le template sans avoir d'enregistrement d'écran ni de voix off.
 */
export const SCRIPT_FACTICE: Script = {
  meta: {
    module: 'Comptabilité',
    numero: 1,
    titre: 'Créer une facture dans RapidoCRM',
    titre_court: 'Créer une facture',
    slug: 'creer-une-facture',
  },
  hook: {
    texte: 'Vous relancez vos factures impayées à la main ?',
    promesse: 'En 2 minutes, RapidoCRM le fait pour vous.',
    duree: 5,
    alternatives: [],
  },
  intro: {
    texte: "On part du module Comptabilité, et on ressort avec une facture envoyée.",
    duree: 3,
  },
  demo: {
    etapes: [
      {
        numero: 1,
        titre: 'Ouvrir le formulaire',
        voix: 'Depuis le module Comptabilité, cliquez sur Nouvelle facture.',
        debut_source: 0,
        fin_source: 8,
        zone_focus: { x: 0.6, y: 0.05, w: 0.35, h: 0.2 },
        annotation: 'Nouvelle facture',
        point: { x: 0.78, y: 0.13 },
      },
      {
        numero: 2,
        titre: "Choisir l'entreprise",
        voix: "Sélectionnez l'entreprise à facturer : le CRM reprend son adresse et sa TVA.",
        debut_source: 8,
        fin_source: 20,
        zone_focus: { x: 0.1, y: 0.25, w: 0.45, h: 0.2 },
        annotation: 'Champ Entreprise',
        point: { x: 0.3, y: 0.34 },
      },
      {
        numero: 3,
        titre: 'Ajouter les lignes',
        voix: 'Ajoutez vos produits. Le total et la TVA se calculent tout seuls.',
        debut_source: 20,
        fin_source: 34,
        zone_focus: { x: 0.08, y: 0.45, w: 0.8, h: 0.28 },
        annotation: 'Lignes de facture',
        point: { x: 0.45, y: 0.58 },
      },
      {
        numero: 4,
        titre: "Fixer la date d'échéance",
        voix: "Renseignez la date d'échéance : c'est elle qui déclenche les relances.",
        debut_source: 34,
        fin_source: 44,
        zone_focus: { x: 0.55, y: 0.3, w: 0.35, h: 0.16 },
        annotation: 'Échéance',
        point: { x: 0.72, y: 0.37 },
      },
      {
        numero: 5,
        titre: 'Enregistrer et envoyer',
        voix: 'Enregistrez, puis envoyez par email. La facture part avec son P.D.F.',
        debut_source: 44,
        fin_source: 56,
        zone_focus: { x: 0.62, y: 0.8, w: 0.32, h: 0.14 },
        annotation: 'Enregistrer et envoyer',
        point: { x: 0.78, y: 0.87 },
      },
    ],
  },
  segment_claude: {
    accroche: 'Ou demandez-le simplement.',
    voix: "Vous n'avez pas envie de cliquer ? Copiez ce prompt, collez-le dans Claude, et c'est fait.",
    prompt: {
      texte:
        "Crée une facture pour [nom de l'entreprise] avec [quantité] × [nom du produit], échéance à [nombre] jours, puis envoie-la par email.",
      variables: ["nom de l'entreprise", 'quantité', 'nom du produit', 'nombre'],
      outil_mcp: 'create_facture',
    },
    resultat_affiche: {
      titre: 'Facture FA-2024-118 créée',
      lignes: ['1 240 € TTC', 'Envoyée à contact@exemple.fr'],
    },
    duree: 16,
  },
  punchline: {
    texte: 'Une facture partie avant votre café.',
    duree: 5,
    alternatives: [],
  },
  seo: {
    titre: 'Créer une facture dans RapidoCRM — tutoriel',
    description:
      "Créez une facture dans RapidoCRM en deux minutes : entreprise, lignes, TVA, échéance et envoi par email. Le tutoriel pas à pas de l'Académie.",
    mots_cles: ['facture', 'RapidoCRM', 'comptabilité'],
    youtube_titre: 'Créer une facture dans RapidoCRM — RapidoCRM',
    youtube_description: 'Tutoriel RapidoCRM Académie.',
    youtube_tags: ['RapidoCRM', 'facture'],
  },
};
