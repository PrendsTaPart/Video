// Timelines du film principal et des 5 Reels.
// Toutes les informations viennent du projet Lovable « Villa Beach NYE Gathering »
// (src/lib/offers.ts, src/lib/contact.ts, src/routes/index.tsx) — vérifiées le 27/11/2026.
//
// vo   : répliques ElevenLabs (fichiers audio/vo/<id>.mp3), `at` = départ en secondes.
//        `sub:false` = pas de sous-titre (la phrase est déjà le texte principal à l'écran).
// scenes : `from`/`to` en secondes, `type` = fonction de rendu dans index.html.

export const VO = {
  vo01: { text: "Vous ne pouvez pas fêter Noël avec vos proches le 24 décembre ?", est: 4.0 },
  vo02: { text: "Et si vous les invitiez le 23 ?", est: 2.2 },
  vo03: { text: "Vivez la magie de Noël au Domaine Villa Beach, à Lisses.", est: 3.4 },
  vo04: { text: "Retrouvez ceux qui vous sont chers autour d’un dîner de fête raffiné, dans une ambiance chaleureuse et féerique.", est: 6.5 },
  vo05: { text: "Découvrez nos formules à 79 euros sans champagne et à 99 euros avec champagne.", est: 5.2 },
  vo06: { text: "Et pour les plus petits, un menu enfant à seulement 29 euros.", est: 3.8 },
  vo07: { text: "Prolongez la soirée avec deux salles et deux ambiances festives.", est: 3.8 },
  vo08: { text: "Parce que la magie de Noël ne dépend pas d’une date, mais des personnes avec qui vous la partagez.", est: 6.0 },
  vo09: { text: "Le 23 décembre, créez de merveilleux souvenirs au Domaine Villa Beach. Réservez dès maintenant !", est: 5.8 },
};

const DISHES = [
  "Foie gras maison, chutney de figues",
  "Noix de Saint-Jacques snackées",
  "Filet de bœuf Wellington, sauce à la truffe",
];

const S = {
  q24: (from, to) => ({ type: "hookQuestion", from, to }),
  q23: (from, to) => ({ type: "hook23", from, to }),
  magic: (from, to) => ({ type: "hookMagic", from, to }),
  date: (from, to) => ({ type: "dateCard", from, to }),
  dinner: (from, to) => ({ type: "photoTitle", from, to, props: {
    img: "diner", kicker: "Restaurant ouvert dès 19h", title: "Un dîner de Noël<br><em>d’exception</em>",
    lines: [], note: "Signé par notre Chef" } }),
  dishes: (from, to) => ({ type: "photoTitle", from, to, props: {
    img: "chef", kicker: "Au menu de Noël", title: "Le Chef vous <em>régale</em>",
    lines: DISHES, note: "Menu complet sur le site · Farandole de bûches de Noël" } }),
  prices: (from, to) => ({ type: "offers", from, to, props: {
    bg: "dessert", kicker: "Dîner de fête · par personne", title: "Deux formules",
    cards: [
      { label: "Formule dîner", sub: "sans champagne", price: "79 €", unit: "/pers." },
      { label: "Formule dîner", sub: "avec champagne", price: "99 €", unit: "/pers.", hi: true },
    ],
    foot: "Vin, cotillons et accès aux 2 salles jusqu’à 05h inclus<br><span style=\"font-size:24px\">L’abus d’alcool est dangereux pour la santé. À consommer avec modération.</span>" } }),
  kids: (from, to) => ({ type: "kidsMenu", from, to }),
  rooms: (from, to) => ({ type: "rooms", from, to }),
  share: (from, to) => ({ type: "photoTitle", from, to, props: {
    img: "ambiance", kicker: "Jeux · blind test géant", title: "Partagez des moments<br><em>inoubliables</em>",
    lines: [], note: "Jeux toute la soirée et lots à gagner" } }),
  dance: (from, to) => ({ type: "photoTitle", from, to, props: {
    img: "dj", kicker: "DJs invités · jusqu’à 05h", title: "Prolongez la magie de Noël<br><em>sur la piste de danse</em>", size: 74,
    lines: [], note: "" } }),
  recap: (from, to) => ({ type: "offers", from, to, props: {
    bg: "fete", kicker: "Mercredi 23 décembre 2026", title: "Vos formules de Noël",
    cards: [
      { label: "Dîner de Noël", sub: "sans champagne", price: "79 €", unit: "/personne" },
      { label: "Dîner de Noël", sub: "avec champagne", price: "99 €", unit: "/personne", hi: true },
      { label: "Menu enfant", sub: "de Noël", price: "29 €", unit: "/enfant" },
    ],
    foot: "L’abus d’alcool est dangereux pour la santé. À consommer avec modération.", stacked: true } }),
  quote: (from, to) => ({ type: "quote", from, to }),
  final: (from, to) => ({ type: "final", from, to }),
};

export const TIMELINES = {
  // Film principal — 55 s
  main: {
    duration: 55,
    musicVolume: 0.22,
    vo: [
      { id: "vo01", at: 0.35, sub: false },
      { id: "vo02", at: 4.7, sub: false },
      { id: "vo03", at: 7.15, sub: false },
      { id: "vo04", at: 11.9 },
      { id: "vo05", at: 18.6 },
      { id: "vo06", at: 24.0 },
      { id: "vo07", at: 31.4 },
      { id: "vo08", at: 41.6, sub: false },
      { id: "vo09", at: 47.7 },
    ],
    scenes: [
      S.q24(0, 4.55), S.q23(4.55, 7.0), S.magic(7.0, 9.0), S.date(9.0, 11.7),
      S.dinner(11.7, 15.3), S.dishes(15.3, 19.0), S.prices(19.0, 23.7),
      S.kids(23.7, 31.2),
      S.rooms(31.2, 36.2), S.share(36.2, 38.4), S.dance(38.4, 40.8),
      S.recap(40.8, 44.3), S.quote(44.3, 47.4),
      S.final(47.4, 55),
    ],
  },

  // Reel 1 — L'accroche (le concept du 23)
  reel1: {
    duration: 17.5, musicVolume: 0.22,
    vo: [ { id: "vo01", at: 0.35, sub: false }, { id: "vo02", at: 4.7, sub: false }, { id: "vo03", at: 7.15, sub: false } ],
    scenes: [ S.q24(0, 4.55), S.q23(4.55, 7.0), S.magic(7.0, 9.0), S.date(9.0, 11.5), S.final(11.5, 17.5) ],
  },
  // Reel 2 — Le dîner du Chef
  reel2: {
    duration: 20, musicVolume: 0.22, musicOffset: 11.5,
    vo: [ { id: "vo04", at: 0.6 }, { id: "vo05", at: 7.6 } ],
    scenes: [ S.dinner(0, 3.6), S.dishes(3.6, 7.5), S.prices(7.5, 13.5), S.final(13.5, 20) ],
  },
  // Reel 3 — Noël en famille, menu enfant
  reel3: {
    duration: 15, musicVolume: 0.22, musicOffset: 20,
    vo: [ { id: "vo02", at: 0.5, sub: false }, { id: "vo06", at: 3.4 } ],
    scenes: [ S.q23(0, 3.2), S.kids(3.2, 9.5), S.final(9.5, 15) ],
  },
  // Reel 4 — 2 salles, 2 ambiances
  reel4: {
    duration: 17, musicVolume: 0.26, musicOffset: 25,
    vo: [ { id: "vo07", at: 0.5 } ],
    scenes: [ S.rooms(0, 5.2), S.share(5.2, 7.8), S.dance(7.8, 10.6), S.final(10.6, 17) ],
  },
  // Reel 5 — L'émotion + récap
  reel5: {
    duration: 15.3, musicVolume: 0.22, musicOffset: 40.6,
    vo: [ { id: "vo08", at: 0.4, sub: false }, { id: "vo09", at: 9.4 } ],
    scenes: [ S.quote(0, 6.1), S.recap(6.1, 9.2), S.final(9.2, 15.3) ],
  },
};
