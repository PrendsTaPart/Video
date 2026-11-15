<?php
// Données de démonstration FICTIVES de RapidoCMS (base LOCALE du serveur 8125 uniquement — aucun compte réel).
// Usage : php cms-demo.php /home/user/rapido-cms
// - comptes « Studio Lumière » factices (Facebook, Instagram, LinkedIn) : jetons bidon, aucune publication réelle possible
//   (pas de planificateur local, et les jetons sont faux) ;
// - publications passées (publiées, avec statistiques en cache) et programmées sur 3 semaines, une en erreur ;
// - brouillons, 3 campagnes, prompts personnels, propositions de contenus, modèles, carte digitale, bibliothèque.
// Les images sont servies localement depuis public/demo-s3 (AWS_URL du .env local, dossier exclu de Git).
$racine = rtrim($argv[1] ?? '/home/user/rapido-cms', '/');
require $racine.'/vendor/autoload.php';
$app = require $racine.'/bootstrap/app.php';
$app->make(Illuminate\Contracts\Console\Kernel::class)->bootstrap();

use Illuminate\Support\Carbon;
use Illuminate\Support\Facades\Cache;
use Illuminate\Support\Facades\DB;

date_default_timezone_set('Europe/Paris');
$e = (int) (DB::table('users')->where('email', 'demo@rapido.test')->value('company_id') ?: 1);
$maintenant = now();
$base = 'http://127.0.0.1:8125/demo-s3';
$biblio = $base.'/rapidosoftware/cms/bibliotheque/';
$ins = function (string $table, array $ligne) use ($maintenant) {
    $colonnes = DB::getSchemaBuilder()->getColumnListing($table);
    $ligne += ['created_at' => $maintenant, 'updated_at' => $maintenant];

    return DB::table($table)->insertGetId(array_intersect_key($ligne, array_flip($colonnes)));
};

// Nettoyage des données de démo précédentes de la société
foreach (['cms_parametres_facebook', 'cms_parametres_instagram', 'cms_parametres_linkedin', 'cms_posts', 'cms_publications', 'campagnes_cms', 'postes_campagne_cms', 'cms_bibliotheque', 'mes_prompts_cms', 'mes_templates_cms'] as $t) {
    DB::table($t)->where('entreprise_id', $e)->delete();
}
$cartes = DB::table('cartes_digitales_user_cms')->where('entreprise_id', $e)->pluck('id');
$pages = DB::table('page_carte_digitale_cms')->whereIn('carte_id', $cartes)->pluck('id');
DB::table('liens_carte_digitale_cms')->whereIn('page_id', $pages)->delete();
DB::table('page_carte_digitale_cms')->whereIn('carte_id', $cartes)->delete();
DB::table('cartes_digitales_user_cms')->where('entreprise_id', $e)->delete();

// Comptes factices
$expire = Carbon::now()->addYear()->toDateTimeString();
$ins('cms_parametres_facebook', ['entreprise_id' => $e, 'page_id' => 'demo_fb_101', 'page_name' => 'Studio Lumière', 'page_img' => $base.'/pages/fb.png', 'access_token' => 'jeton-factice-demo', 'expires_in' => $expire]);
$ins('cms_parametres_instagram', ['entreprise_id' => $e, 'page_id' => 'demo_ig_201', 'page_name' => 'studio.lumiere', 'page_img' => $base.'/pages/ig.png', 'access_token' => 'jeton-factice-demo', 'expires_in' => $expire]);
$ins('cms_parametres_linkedin', ['entreprise_id' => $e, 'page_id' => 'demo_li_301', 'page_name' => 'Studio Lumière', 'access_token' => 'jeton-factice-demo', 'expires_in' => $expire]);
$comptes = ['facebook' => 'demo_fb_101', 'instagram' => 'demo_ig_201', 'linkedin' => 'demo_li_301'];

// Bibliothèque
$fichiers = [
    ['atelier-portrait.jpg', 'Séance portrait — novembre', 'image', 182],
    ['offre-noel.jpg', 'Offre de Noël', 'image', 175],
    ['coulisses.jpg', 'Coulisses d’un shooting', 'image', 168],
    ['avis-client.jpg', 'Avis client — Camille', 'image', 160],
    ['mariage-ete.jpg', 'Mariages 2027', 'image', 171],
    ['atelier-photo.jpg', 'Atelier photo débutants', 'image', 179],
    ['equipe.jpg', 'Notre équipe', 'image', 166],
    ['black-friday.jpg', 'Black Friday', 'image', 158],
    ['banniere-linkedin.png', 'Bannière LinkedIn', 'image', 92],
];
foreach ($fichiers as $i => [$f, $nom, $type, $ko]) {
    $d = $maintenant->copy()->subDays(20 - $i * 2);
    $ins('cms_bibliotheque', ['entreprise_id' => $e, 'file' => $f, 'nom' => $nom, 'type' => $type, 'taille' => $ko * 1024, 'created_at' => $d, 'updated_at' => $d]);
}

// Publications : passées (publiées) et programmées
$pubs = [
    [-12, '10:00', 'facebook', 'atelier-portrait.jpg', 'Nouvelles séances portrait en novembre 📸 Il reste quelques créneaux le samedi matin.', 1, null],
    [-11, '18:30', 'instagram', 'coulisses.jpg', 'Dans les coulisses d’un shooting produit ✨ #photographe #bordeaux', 1, null],
    [-9, '09:00', 'linkedin', 'equipe.jpg', 'Léa, Karim et Inès : l’équipe du Studio Lumière vous accueille quai des Chartrons.', 1, null],
    [-7, '12:00', 'facebook', 'avis-client.jpg', '« Un vrai coup de cœur » — merci Camille pour votre confiance ❤️', 1, null],
    [-5, '19:00', 'instagram', 'atelier-photo.jpg', 'Atelier photo débutants le 28 novembre : apprenez à cadrer en 2 heures.', 1, null],
    [-3, '11:00', 'linkedin', 'banniere-linkedin.png', 'Entreprises bordelaises : portraits professionnels sur site, devis en 24 h.', 1, null],
    [-2, '17:00', 'instagram', 'black-friday.jpg', 'Black Friday : tirages d’art à prix doux jusqu’à dimanche 🖤', 1, 'Le jeton Instagram a expiré : reconnectez le compte.'],
    [1, '10:00', 'facebook', 'offre-noel.jpg', 'Offre de Noël : -20 % sur les albums photo jusqu’au 24 décembre 🎄', 0, null],
    [2, '18:30', 'instagram', 'offre-noel.jpg', 'Le cadeau qui dure : un album photo de famille 🎁 -20 % jusqu’au 24/12', 0, null],
    [4, '09:00', 'linkedin', 'equipe.jpg', 'Fin d’année : offrez des portraits professionnels à vos équipes.', 0, null],
    [6, '12:00', 'facebook', 'mariage-ete.jpg', 'Mariages 2027 : les dates s’ouvrent aujourd’hui 💍', 0, null],
    [8, '19:00', 'instagram', 'mariage-ete.jpg', 'Vous vous mariez en 2027 ? Réservez votre photographe dès maintenant 💍', 0, null],
    [11, '10:00', 'facebook', 'atelier-photo.jpg', 'Dernières places pour l’atelier photo du 28 novembre !', 0, null],
    [15, '11:00', 'linkedin', 'coulisses.jpg', 'Photos produits pour e-commerce : nos tarifs 2027 sont en ligne.', 0, null],
];
$ids = [];
foreach ($pubs as $i => [$jours, $heure, $reseau, $image, $texte, $statut, $erreur]) {
    $date = $maintenant->copy()->addDays($jours)->setTimeFromTimeString($heure);
    $urn = $statut ? 'demo_urn_'.$reseau.'_'.$i : null;
    $ids[$i] = $ins('cms_publications', [
        'entreprise_id' => $e, 'post_name' => mb_substr($texte, 0, 40), 'account_id' => $comptes[$reseau], 'social_type' => $reseau,
        'media_url' => $biblio.$image, 'media_caption' => $texte, 'post_date' => $date->toDateString(), 'post_heure' => $heure,
        'post_urn' => $erreur ? null : $urn, 'errors' => $erreur, 'statut' => $statut, 'created_at' => $date->copy()->subDays(3), 'updated_at' => $date,
    ]);
    if ($urn && ! $erreur) {
        // Statistiques fictives mises en cache (l'application lit ce cache avant d'appeler les réseaux)
        Cache::forever('insight'.$urn, ['liked' => 40 + $i * 17, 'shares' => 3 + $i * 2, 'views' => 900 + $i * 340, 'comments' => 5 + $i * 3, 'post_id' => $urn]);
    }
}

// Brouillons
foreach ([
    ['Teaser calendrier 2027', 'instagram', 'media', 'equipe.jpg', 'Le calendrier 2027 du studio arrive bientôt… 👀'],
    ['Conseil photo de la semaine', 'facebook', 'text', null, 'Conseil de la semaine : photographiez à contre-jour à l’heure dorée pour des portraits lumineux.'],
    ['Témoignage mariage', 'linkedin', 'media', 'avis-client.jpg', 'Retour d’expérience : couvrir un mariage de 120 invités en Gironde.'],
    ['Jeu concours de Noël', 'instagram', 'media', 'offre-noel.jpg', 'Jeu concours : gagnez une séance photo de famille 🎄 (règlement en bio)'],
] as [$nom, $reseau, $type, $image, $texte]) {
    $ins('cms_posts', ['entreprise_id' => $e, 'post_name' => $nom, 'social_type' => $reseau, 'account_id' => $comptes[$reseau], 'post_type' => $type,
        'media_type' => $image ? 'image' : null, 'media_source' => $image ? 'bibliotheque' : null, 'media_url' => $image ? $biblio.$image : null, 'media_caption' => $texte]);
}

// Campagnes
foreach ([
    ['Noël 2026', 'Albums photo et cartes cadeaux, du 1er au 24 décembre', [7, 8, 9]],
    ['Mariages 2027', 'Ouverture des réservations de la saison 2027', [10, 11]],
    ['Atelier photo', 'Remplir l’atelier débutants du 28 novembre', [4, 12]],
] as [$nom, $description, $liste]) {
    $c = $ins('campagnes_cms', ['entreprise_id' => $e, 'nom' => $nom, 'description' => $description, 'facebook' => 1, 'instagram' => 1, 'linkedin' => 1, 'tiktok' => 0]);
    foreach ($liste as $k) {
        $ins('postes_campagne_cms', ['entreprise_id' => $e, 'campagne_id' => $c, 'publication_id' => $ids[$k], 'social' => $pubs[$k][2]]);
    }
}

// Prompts personnels
foreach ([
    ['text', 'Post promo saisonnière', 'Rédige un post Facebook chaleureux pour [offre] de Studio Lumière, photographe à Bordeaux, avec un appel à réserver et 3 hashtags locaux.'],
    ['text', 'Légende Instagram coulisses', 'Écris une légende Instagram courte (moins de 150 caractères) qui raconte les coulisses d’un shooting [type de shooting], ton complice, 2 emojis.'],
    ['text', 'Post LinkedIn B2B', 'Rédige un post LinkedIn pour proposer des portraits professionnels sur site aux entreprises de [ville], 3 bénéfices et une question en fin de post.'],
    ['visuel', 'Visuel offre de Noël', 'Visuel carré, ambiance cocooning, album photo ouvert sur une table en bois, guirlande lumineuse, couleurs rouge et or, place pour le texte en haut.'],
    ['visuel', 'Bannière atelier photo', 'Bannière horizontale lumineuse, appareil photo argentique sur fond pastel, style minimaliste, espace libre à gauche pour un titre.'],
] as [$type, $titre, $prompt]) {
    $ins('mes_prompts_cms', ['entreprise_id' => $e, 'type' => $type, 'titre' => $titre, 'prompt' => $prompt]);
}

// Propositions de contenus (bibliothèque commune de prompts, base locale)
if (DB::table('landing_prompts')->count() === 0) {
    $cats = [
        ['Promotion', 'text', 'ti ti-discount', ['Offres saisonnières' => ['Annonce de soldes' => 'Rédige un post pour annoncer [réduction] sur [produit] jusqu’au [date], avec un sentiment d’urgence et un appel à l’action.', 'Code promo' => 'Écris un post court qui présente le code promo [code] valable sur [offre], ton enjoué.']]],
        ['Engagement', 'text', 'ti ti-message-heart', ['Questions à la communauté' => ['Sondage en story' => 'Propose 3 idées de questions à poser en story à des clients de [secteur] pour faire réagir.', 'Avant / après' => 'Rédige un post « avant / après » pour [prestation], en 4 phrases, avec une question finale.']]],
        ['Expertise', 'text', 'ti ti-bulb', ['Conseils' => ['Astuce de la semaine' => 'Donne une astuce concrète de [métier] que les clients peuvent appliquer seuls, en 5 lignes.', 'Erreurs à éviter' => 'Liste 3 erreurs courantes en [domaine] et comment les éviter, format liste.']]],
        ['Événement', 'text', 'ti ti-calendar-event', ['Invitations' => ['Annonce d’atelier' => 'Rédige l’annonce d’un atelier [thème] le [date] à [lieu] : programme, durée, prix, places limitées.']]],
        ['Visuels produits', 'visuel', 'ti ti-photo', ['Mise en scène' => ['Produit sur fond uni' => 'Photo de [produit] sur fond uni pastel, lumière douce de studio, ombre légère, format carré.', 'Ambiance lifestyle' => 'Scène lifestyle avec [produit] utilisé dans un intérieur chaleureux, lumière naturelle.']]],
        ['Visuels saisonniers', 'visuel', 'ti ti-snowflake', ['Fêtes' => ['Noël' => 'Visuel festif avec [produit], guirlandes lumineuses, couleurs rouge et or, espace pour un titre.']]],
    ];
    foreach ($cats as [$nom, $type, $icone, $sous]) {
        $c = $ins('landing_prompts_categories', ['nom' => $nom, 'type' => $type, 'icon' => $icone]);
        foreach ($sous as $nomSous => $prompts) {
            $s = $ins('landing_prompts_sous_categories', ['categorie_id' => $c, 'nom' => $nomSous]);
            foreach ($prompts as $titre => $prompt) {
                $ins('landing_prompts', ['sous_categorie_id' => $s, 'titre' => $titre, 'prompt' => $prompt]);
            }
        }
    }
}

// Modèles (Mes templates)
foreach ([['Promotion carrée', 'modele-promo.png', 'Post promo 1080 × 1080 aux couleurs du studio'], ['Citation client', 'modele-citation.png', 'Mise en avant d’un avis client'], ['Annonce d’événement', 'modele-evenement.png', 'Date, lieu et inscription']] as [$nom, $image, $description]) {
    $ins('mes_templates_cms', ['entreprise_id' => $e, 'name' => $nom, 'type' => 'post', 'height' => 1080, 'width' => 1080, 'mots_cles' => 'studio, photo', 'description' => $description,
        'logiciel' => 'cms', 'prix' => 0, 'components' => '[]', 'style' => '[]', 'html' => '<div class="modele">'.$nom.'</div>', 'css' => '.modele{font-family:sans-serif}', 'js' => '', 'image' => $image]);
}

// Carte digitale
$carte = $ins('cartes_digitales_user_cms', ['entreprise_id' => $e, 'nom_carte' => 'Carte de Léa', 'nom_owner' => 'Martin', 'prenom_owner' => 'Léa', 'email_owner' => 'lea@studio-lumiere.test',
    'telephone_owner' => '05 00 00 00 00', 'supp_info' => 'Photographe — Studio Lumière, Bordeaux']);
$page = $ins('page_carte_digitale_cms', ['carte_id' => $carte, 'image' => $base.'/pages/ig.png', 'text' => 'Léa Martin — Studio Lumière', 'text_size' => 22, 'background_color' => '#f6f3ff', 'text_color' => '#1f2937']);
DB::table('cartes_digitales_user_cms')->where('id', $carte)->update(['page_id' => $page]);
foreach ([['Réserver une séance', 'https://studio-lumiere.test/reserver'], ['Portfolio', 'https://studio-lumiere.test/portfolio'], ['Instagram', 'https://instagram.com/studio.lumiere.demo'], ['Avis clients', 'https://studio-lumiere.test/avis']] as [$nom, $url]) {
    $ins('liens_carte_digitale_cms', ['page_id' => $page, 'name' => $nom, 'url' => $url]);
}

echo "Démo RapidoCMS (société #$e) : 3 comptes factices, ".count($pubs)." publications, 4 brouillons, 3 campagnes, 5 prompts, 3 modèles, 1 carte, ".count($fichiers)." fichiers.\n";
