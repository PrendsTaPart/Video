// Toutes les données des vidéos de fêtes de la Villa Beach : textes, plats, prix, dates, couleurs, musiques.
// Modifier ce fichier puis relancer `bash rendre.sh` suffit à régénérer les six vidéos.

export const restaurant = {
  nom: 'Villa Beach',
  lieu: 'Le Garden',
  adresse: '23 rue des Pyrénées, 91090 Lisses',
  telephone: '01 84 60 20 46',
  logo: 'logo.png',
};

export const charte = {
  or: '#C9A45C',
  creme: '#F2EAD6',
  titres: 'Bebas Neue',
  textes: 'Cormorant Garamond',
};

// Tempo de calage des transitions (un temps = 0,5 s à 120 BPM, une mesure = 4 temps).
export const tempo = { bpm: 120, fps: 30 };

export type Section = { titre: string; plats: string[]; photo: string };

export type Fete = {
  cle: 'noel' | 'nye';
  nom: string;
  fond: string; // couleur de fond de la fête
  hero: string; // image d'ouverture (dans assets/)
  surtitre: string;
  accroche: string;
  sections: Section[];
  prix: string; // texte de la pastille
  details: string[]; // lignes sous la pastille (dates, extras)
  cta: string;
  compteARebours: boolean; // 3-2-1 + confettis (Nouvel An)
  musique: { fichier: string; debut: number; volume: number }; // debut : seconde de départ dans le morceau
  teaser: { accroche: string; mots: string[]; photos: string[] };
};

export const fetes: Record<'noel' | 'nye', Fete> = {
  noel: {
    cle: 'noel',
    nom: 'Menu de Noël',
    fond: '#0F1D16',
    hero: 'hero-noel.png',
    surtitre: 'Menu de Noël',
    accroche: 'Cette année, Noël se fête à la Villa',
    sections: [
      {
        titre: 'Entrées',
        plats: ['Foie gras maison au poivre de Timut', 'Saint-Jacques sauce champagne', 'Œuf parfait, crème de cèpes et truffe'],
        photo: 'foie-gras-chutney.jpg',
      },
      {
        titre: 'Plats',
        plats: ['Filet de bœuf aux morilles', 'Dos de cabillaud, beurre blanc au champagne', 'Raviolis à la truffe blanche'],
        photo: 'jarret-agneau-puree.jpg',
      },
      {
        titre: 'Desserts',
        plats: ['Bûche chocolat praliné', 'Bûche vanille-marron', 'Café gourmand de Noël'],
        photo: 'fondant-chocolat-fruits.jpg',
      },
    ],
    prix: '99 € par personne',
    details: ['Boissons comprises', 'Du 20 au 25 décembre'],
    cta: 'Réservez votre table',
    compteARebours: false,
    musique: { fichier: 'music-noel.mp3', debut: 0, volume: 0.9 },
    teaser: {
      accroche: 'Noël à la Villa',
      mots: ['Places', 'limitées'],
      photos: ['hero-noel.png', 'magret-ardoise-bois-vertical.jpg', 'fondant-chocolat-fruits.jpg', 'foie-gras-chutney.jpg'],
    },
  },
  nye: {
    cle: 'nye',
    nom: 'Réveillon du Nouvel An',
    fond: '#0B0A08',
    hero: 'hero-nouvel-an.png',
    surtitre: 'Réveillon du 31 décembre',
    accroche: 'Le 31, on passe minuit à la Villa',
    sections: [
      {
        titre: 'Entrées',
        plats: ['Foie gras au sauternes', 'Saint-Jacques rôties, beurre noisette', 'Velouté de potimarron, burrata'],
        photo: 'veloute.jpg',
      },
      {
        titre: 'Plats',
        plats: ['Tournedos Rossini', 'Demi-homard sauce champagne', 'Wellington végétarien'],
        photo: 'magret-ardoise-marbre-vert.jpg',
      },
      {
        titre: 'Desserts',
        plats: ['Sphère chocolat', 'Entremets champagne-framboise', 'Pavlova exotique'],
        photo: 'pain-perdu-brioche-flambe-2.jpg',
      },
    ],
    prix: '149 €',
    details: ['Champagne à minuit', "Club jusqu'à l'aube"],
    cta: 'Réservez votre table',
    compteARebours: true,
    musique: { fichier: 'music-nye.mp3', debut: 16, volume: 0.9 },
    teaser: {
      accroche: 'Réveillon à la Villa',
      mots: ['Places', 'limitées'],
      photos: ['hero-nouvel-an.png', 'magret-ardoise-marbre-vert.jpg', 'pain-perdu-brioche-flambe-2.jpg', 'veloute.jpg'],
    },
  },
};

// Durées en secondes (calées sur des mesures de 2 s à 120 BPM).
export const durees = { menu: 20, teaser: 8 };
