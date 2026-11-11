/**
 * Banque d'écrans RapidoCRM, partagée par les 172 tutoriels.
 *
 * Ce sont des maquettes fournies par l'équipe produit, pas des enregistrements :
 * elles servent à illustrer, à prévisualiser le template et à choisir un plan de
 * repli quand un `source.mp4` manque encore. Elles ne remplacent jamais la
 * capture réelle pour un tutoriel publié.
 */

export type Cadrage =
  /** L'écran remplit le cadre : utilisable comme plan de démonstration. */
  | 'capture'
  /** Ordinateur en situation, décor autour : illustration seulement. */
  | 'mockup';

export interface Ecran {
  /** Nom de fichier, sans extension. */
  nom: string;
  /** Ce que l'écran montre, en une ligne. */
  titre: string;
  /** Module de l'Académie auquel il se rattache. */
  module: string;
  cadrage: Cadrage;
  /** Termes qui font correspondre un tutoriel à cet écran. */
  motsCles: string[];
}

export const ECRANS: Ecran[] = [
  {
    nom: 'tableau-de-bord',
    titre: 'Tableau de bord : contrats signés, tâches, clients, commercial du mois',
    module: 'Pilotage',
    cadrage: 'capture',
    motsCles: ['tableau de bord', 'dashboard', 'statistique', 'kpi', 'pilotage', 'interaction'],
  },
  {
    nom: 'liste-commerciaux',
    titre: 'Liste des commerciaux et leur disponibilité',
    module: 'Équipe',
    cadrage: 'capture',
    motsCles: ['commercial', 'commerciaux', 'equipe', 'disponibilite', 'profil'],
  },
  {
    nom: 'fiche-entreprise',
    titre: "Fiche entreprise : activités récentes, contacts, blocs finance et marketing",
    module: 'Clients',
    cadrage: 'capture',
    motsCles: ['entreprise', 'fiche client', 'activite', 'documentation'],
  },
  {
    nom: 'ajouter-entreprise-contact',
    titre: "Modales « Ajouter une entreprise » et « Ajouter un contact »",
    module: 'Clients',
    cadrage: 'mockup',
    motsCles: ['entreprise', 'contact', 'siret', 'acquisition', 'coordonnees'],
  },
  {
    nom: 'agenda',
    titre: 'Agenda mensuel avec rendez-vous et fiche du commercial',
    module: 'Agenda',
    cadrage: 'capture',
    motsCles: ['agenda', 'rendez-vous', 'rdv', 'calendrier', 'evenement', 'planning'],
  },
  {
    nom: 'fiche-produit',
    titre: 'Fiche produit : description, dates, prix, TVA, points de fidélité',
    module: 'Catalogue',
    cadrage: 'capture',
    motsCles: ['produit', 'catalogue', 'prix', 'tva', 'strategie'],
  },
  {
    nom: 'strategies-ia',
    titre: "Créer des stratégies à l'aide de l'IA : paramétrage, prompt, validation",
    module: 'Catalogue',
    cadrage: 'mockup',
    motsCles: ['strategie', 'prompt', 'produit'],
  },
  {
    nom: 'campagnes-mail-sms',
    titre: 'Campagnes Mail et SMS : ciblage, texte, validation, règles d\'automatisation',
    module: 'Marketing',
    cadrage: 'mockup',
    motsCles: ['campagne', 'mail', 'sms', 'ciblage', 'automatisation', 'relance'],
  },
  {
    nom: 'campagne-sms-modele-contrat',
    titre: "Campagne SMS et choix d'un modèle de contrat",
    module: 'Marketing',
    cadrage: 'mockup',
    motsCles: ['sms', 'contrat', 'statut entreprise'],
  },
  {
    nom: 'envoyer-newsletter',
    titre: "Modale « Envoyer un newsletter » : destinataire, date d'envoi, template",
    module: 'Marketing',
    cadrage: 'mockup',
    motsCles: ['newsletter', 'destinataire', 'planification'],
  },
  {
    nom: 'editeur-newsletter',
    titre: "Éditeur de newsletter : blocs Basic, Extra, Formulaire, CTA, Produits",
    module: 'Templates',
    cadrage: 'mockup',
    motsCles: ['editeur', 'newsletter', 'bloc', 'cta', 'formulaire', 'mise en page'],
  },
  {
    nom: 'themes-newsletter',
    titre: 'Bibliothèque de thèmes de newsletter',
    module: 'Templates',
    cadrage: 'capture',
    motsCles: ['theme', 'newsletter', 'bibliotheque'],
  },
  {
    nom: 'creer-sondage',
    titre: 'Campagne sondage : questions, réponses, dates, aperçu',
    module: 'Marketing',
    cadrage: 'mockup',
    motsCles: ['sondage', 'question', 'reponse', 'enquete', 'apercu'],
  },
  {
    nom: 'programme-fidelite',
    titre: 'Programme fidélité : statistiques des cartes NFC et fidélité',
    module: 'Fidélité',
    cadrage: 'capture',
    motsCles: ['fidelite', 'carte', 'nfc', 'recompense', 'points', 'programme'],
  },
  {
    nom: 'carte-nfc',
    titre: 'Création d\'une carte NFC : design, paramétrage, QR code',
    module: 'Fidélité',
    cadrage: 'mockup',
    motsCles: ['carte nfc', 'nfc', 'qr code'],
  },
  {
    nom: 'espace-fidelite-client',
    titre: 'Espace fidélité côté client : points, sondage, jeu concours, récompenses',
    module: 'Fidélité',
    cadrage: 'mockup',
    motsCles: ['fidelite', 'points', 'recompense', 'jeu concours', 'espace client'],
  },
  {
    nom: 'assistant-prompts-mail',
    titre: 'Assistant de rédaction : bibliothèque de prompts et chatbot',
    module: 'Templates',
    cadrage: 'capture',
    motsCles: ['prompt', 'chatbot', 'assistant', 'redaction'],
  },
];

/** Chemin staticFile d'un écran. */
export const cheminEcran = (nom: string): string => `ecrans/${nom}.webp`;

const normaliser = (texte: string): string =>
  texte
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9 ]/g, ' ');

/**
 * Choisit l'écran qui correspond le mieux à un tutoriel, en croisant son module
 * et son titre avec les mots-clés du manifeste.
 *
 * @param cadrage restreint le choix aux écrans utilisables comme plan de
 *   démonstration (`'capture'`) ou aux illustrations (`'mockup'`).
 * @returns l'écran retenu, ou `null` si rien ne correspond — auquel cas on ne
 *   met rien plutôt qu'un écran hors sujet.
 */
export const ecranPour = (
  module: string,
  titre: string,
  cadrage?: Cadrage,
): Ecran | null => {
  const texte = normaliser(`${module} ${titre}`);
  const candidats = cadrage ? ECRANS.filter((e) => e.cadrage === cadrage) : ECRANS;

  let meilleur: Ecran | null = null;
  let meilleurScore = 0;

  for (const ecran of candidats) {
    let score = 0;
    if (normaliser(ecran.module) === normaliser(module)) score += 3;
    for (const mot of ecran.motsCles) {
      if (texte.includes(normaliser(mot))) score += 2;
    }
    if (score > meilleurScore) {
      meilleurScore = score;
      meilleur = ecran;
    }
  }
  // Seuil à 3 : un seul mot-clé (2 points) ne suffit pas — il faut soit le
  // module en plus, soit deux mots-clés. Sinon on préfère ne rien proposer.
  return meilleurScore >= 3 ? meilleur : null;
};
