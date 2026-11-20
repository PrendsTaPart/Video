// Épisode 135 « J'installe la Villa Beach avec FoodEatUp » : toutes les données et textes de la vidéo.
// Chiffres lus dans FoodEatUp (établissement 46, Villa Beach) le 20/11/2026 :
// list_dish_categories, get_stock_overview, get_haccp_overview, get_site_status, list_assets.

export const episode = {
  numero: 135,
  serie: 'Mes projets',
  titre: "J'installe la Villa Beach avec FoodEatUp",
  motCle: 'VILLA',
  musique: {fichier: 'musique.mp3', debut: 16, volume: 0.55},
  fps: 30,
};

// [début, fin] en secondes ; « *mot* » = mot surligné en orange.
export const scenes = {
  accroche: {t: [0, 3.5], lignes: ["J'ai installé", 'un restaurant', '*entier*', 'sur FoodEatUp']},
  restaurant: {t: [3.5, 7.5], nom: 'Villa Beach', lieu: 'Le Garden · Lisses', sous: 'Restaurant, lounge et club'},
  carte: {t: [7.5, 13.5], label: 'La carte', chips: ['91 plats', '19 catégories', 'Site en ligne'], video: 'carte.mp4', debutVideo: 6},
  communication: {
    t: [13.5, 20.5],
    label: 'La communication',
    grand: '15 vidéos',
    chips: ['9 plats en Reels', '6 vidéos des fêtes', 'Rangées dans FoodEatUp'],
    videos: ['plat-magret.mp4', 'plat-foie-gras.mp4', 'plat-veloute.mp4', 'plat-tagliatelles-burrata.mp4', 'plat-burger-poulet.mp4', 'plat-jarret-agneau.mp4', 'plat-supreme-poulet.mp4', 'plat-pain-perdu.mp4', 'plat-fondant-chocolat.mp4'],
  },
  reseaux: {t: [20.5, 25.5], label: 'Les réseaux sociaux', video: 'noel.mp4', debutVideo: 3, reseaux: ['Instagram', 'TikTok', 'LinkedIn', 'Facebook'], note: 'Légendes prêtes pour chaque réseau'},
  stocks: {
    t: [25.5, 31.5],
    label: 'Les stocks',
    grand: '152 références',
    alertes: [
      ['Cantal AOP jeune', 'rupture'],
      ['Bleu des Causses AOP', 'rupture'],
      ['Raviolis frais à la truffe', 'rupture'],
    ],
    commande: 'Commande fournisseur proposée',
  },
  haccp: {
    t: [31.5, 37.5],
    label: 'Le HACCP',
    equipements: ['Chambre froide positive', 'Congélateur surgelés', 'Frigo bar et boissons', 'Frigo crémerie et desserts', 'Frigo marée et produits crus'],
    chips: ['6 équipements suivis', '3 checklists par jour', '16 postes de nettoyage', '22 documents'],
  },
  fin: {t: [37.5, 43], phrase: 'Tout le restaurant, *une seule appli*', appel: 'Écris VILLA en commentaire'},
};

export const DUREE = 43;
