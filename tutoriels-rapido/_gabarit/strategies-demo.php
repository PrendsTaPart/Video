<?php
// Stratégies FICTIVES pour filmer CRM37 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Offre 1 « Site vitrine » : deux stratégies avec des contributions de l'équipe et un document.
// Usage : php strategies-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec("delete from document_strategies");
$db->exec("delete from description_strategies");
$db->exec("delete from strategies");
$db->exec("delete from sqlite_sequence where name in ('strategies','description_strategies','document_strategies')");
$j = fn ($n) => date('Y-m-d H:i:s', strtotime("-$n days 10:00"));
$strats = [
    ['Relance des artisans du quartier', 'Stratégie commerciale', 12, [
        [2, 11, "<p><strong>Cible :</strong> artisans et commerces de proximité sans site ou avec un site de plus de 5 ans.</p><ul><li>Appel de découverte, puis devis sous 48 h</li><li>Offre : maintenance offerte 3 mois</li></ul>"],
        [3, 6, "<p>Retour terrain : les boulangeries demandent surtout la commande en ligne. Ajouter une démo dédiée au prochain rendez-vous.</p>"],
    ]],
    ['Témoignages clients sur LinkedIn', 'Stratégie de communication', 5, [
        [3, 4, "<p>Un post par semaine : avant / après d'un site livré, avec l'accord du client.</p><p>Objectif : 3 demandes de devis par mois via LinkedIn.</p>"],
    ]],
];
foreach ($strats as [$nom, $type, $age, $descs]) {
    $db->prepare("insert into strategies (nom, type, offre_id, created_at, updated_at) values (?, ?, 1, ?, ?)")->execute([$nom, $type, $j($age), $j($age)]);
    $sid = $db->lastInsertId();
    foreach ($descs as [$uid, $a, $txt]) {
        $db->prepare("insert into description_strategies (user_id, strategie_id, description, created_at, updated_at) values (?, ?, ?, ?, ?)")->execute([$uid, $sid, $txt, $j($a), $j($a)]);
    }
}
$db->prepare("insert into document_strategies (user_id, strategie_id, filename, file, created_at, updated_at) values (2, 1, 'Argumentaire artisans', 'argumentaire-demo.pdf', ?, ?)")->execute([$j(10), $j(10)]);
echo "stratégies : " . $db->query("select count(*) from strategies")->fetchColumn() . "\n";
