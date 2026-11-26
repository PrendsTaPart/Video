<?php

// Données de démonstration FICTIVES pour le tutoriel CRM78 (Mots-clés, scores et tendances) — copie de tournage seulement.
// Aucun appel à DataForSEO : les recherches et mots-clés sont insérés directement, le score est calculé par MotsClesService.
// Usage : cd /home/user/rapido-crm-film && php artisan tinker --execute="require '/home/user/video/tutoriels-rapido/_gabarit/mots-cles-demo.php';"

use App\Models\MotCle;
use App\Models\MotsClesRecherche;
use App\Services\MotsClesService;

$societe = 1;   // Studio Lumière (compte demo@rapido.test)
$auteur = 1;
$service = app(MotsClesService::class);
$motsProduits = ['site', 'vitrine', 'shooting', 'photo', 'carte', 'nfc'];

MotCle::where('company_id', $societe)->delete();
MotsClesRecherche::where('company_id', $societe)->delete();

// Courbe sur 12 mois : $depart → $arrivee, avec un léger bruit déterministe.
$courbe = function (int $depart, int $arrivee) {
    $mois = [];
    for ($i = 0; $i < 12; $i++) {
        $mois[] = (int) round($depart + ($arrivee - $depart) * $i / 11 * (0.92 + 0.08 * (($i * 7) % 5) / 4));
    }

    return $mois;
};

$recherches = [
    ['carte de visite nfc', 3, [
        ['carte de visite nfc', 'commercial', 42, 0.61, 1.10, [900, 2400]],
        ['carte nfc personnalisée', 'transactional', 31, 0.55, 0.95, [500, 1300]],
        ['carte de visite digitale', 'commercial', 38, 0.48, 0.85, [1100, 1900]],
        ['carte de visite connectée', 'informational', 25, 0.40, 0.70, [400, 700]],
        ['prix carte nfc', 'transactional', 22, 0.52, 0.90, [300, 650]],
        ['comment fonctionne une carte nfc', 'informational', 14, 0.12, 0.30, [700, 760]],
    ]],
    ['shooting photo entreprise', 2, [
        ['shooting photo entreprise', 'commercial', 47, 0.58, 1.60, [1200, 1350]],
        ['photographe corporate', 'transactional', 51, 0.66, 2.10, [800, 820]],
        ['photo portrait professionnel', 'commercial', 44, 0.50, 1.20, [1600, 1700]],
        ['portrait linkedin photographe', 'transactional', 29, 0.44, 1.30, [350, 900]],
        ['idée photo équipe entreprise', 'informational', 18, 0.15, 0.40, [450, 470]],
    ]],
    ['création site vitrine', 1, [
        ['création site vitrine', 'commercial', 63, 0.74, 3.40, [2900, 3000]],
        ['site vitrine prix', 'transactional', 55, 0.70, 2.80, [1300, 1250]],
        ['agence site vitrine', 'transactional', 58, 0.72, 4.10, [700, 690]],
        ['site vitrine artisan', 'commercial', 34, 0.46, 1.90, [400, 820]],
        ['exemple site vitrine', 'informational', 27, 0.20, 0.60, [1000, 980]],
    ]],
];

foreach ($recherches as [$requete, $joursAvant, $lignes]) {
    $r = MotsClesRecherche::create(['company_id' => $societe, 'user_id' => $auteur, 'requete' => $requete, 'pays' => 'FR', 'langue' => 'fr',
        'nb_resultats' => count($lignes), 'cout_usd' => 0, 'statut' => 'ok']);
    $r->forceFill(['created_at' => now()->subDays($joursAvant), 'updated_at' => now()->subDays($joursAvant)])->save();
    foreach ($lignes as [$mot, $intention, $difficulte, $concurrence, $cpc, [$depart, $arrivee]]) {
        $tendance = $courbe($depart, $arrivee);
        $l = ['mot_cle' => $mot, 'volume' => end($tendance), 'cpc' => $cpc, 'concurrence' => $concurrence, 'difficulte' => $difficulte,
            'intention' => $intention, 'tendance' => $tendance];
        MotCle::create($l + ['company_id' => $societe, 'recherche_id' => $r->id, 'score' => $service->score($l, $motsProduits)]);
    }
}

echo 'Recherches : '.MotsClesRecherche::where('company_id', $societe)->count().', mots-clés : '.MotCle::where('company_id', $societe)->count()
    .', sujets en hausse : '.count($service->tendances($societe, 8)).PHP_EOL;
