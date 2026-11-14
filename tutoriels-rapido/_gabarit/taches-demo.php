<?php
// Tâches FICTIVES pour filmer CRM35 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Usage : php taches-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$now = date('Y-m-d H:i:s');
$ent = [];
foreach ($db->query("select id, nom from entreprises where company_id = 1") as $r) { $ent[$r['nom']] = $r['id']; }
$wf = $db->query("select id from workflows where company_id = 1 and deleted_at is null and statut = 'actif' order by id limit 1")->fetchColumn() ?: null;
$db->exec("delete from taches where company_id = 1");
if (! $db->query("select count(*) from taches")->fetchColumn()) { $db->exec("delete from sqlite_sequence where name = 'taches'"); }
// titre, description, priorité, statut, échéance (jours, heure), assigné, client, issue d'un workflow
$t = [
    ['Envoyer le devis de maintenance', 'Le client attend une offre sur 12 mois.', 'haute', 'a_faire', [-1, '10:00'], 2, 'Lotus Lounge', false],
    ['Rappeler pour la signature', 'Devis ouvert deux fois, pas encore signé.', 'haute', 'a_faire', [0, '16:00'], 1, 'Clover Bistro', true],
    ['Préparer la démo de l\'agent vocal', null, 'normale', 'en_cours', [1, '09:30'], 1, 'Café Mériadeck', false],
    ['Relancer la facture n° 7', 'Échéance dépassée de 4 jours.', 'normale', 'a_faire', [2, '11:00'], 3, 'Atelier Garonne', true],
    ['Mettre à jour la fiche client', 'Nouveau responsable des achats.', 'basse', 'a_faire', [5, '14:00'], 4, 'Fournil des Chartrons', false],
    ['Organiser le shooting produits', null, 'normale', 'a_faire', [6, '10:00'], 3, 'Petal & Plate', false],
    ['Envoyer les photos de l\'atelier', null, 'basse', 'terminee', [-3, '15:00'], 2, 'Maison Lafitte', false],
];
foreach ($t as [$titre, $desc, $prio, $statut, [$j, $h], $user, $nom, $deWf]) {
    $db->prepare("insert into taches (company_id, user_id, assigne_a, entreprise_id, titre, description, priorite, statut, echeance, workflow_id, created_at, updated_at)
        values (1, 1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
        ->execute([$user, $ent[$nom] ?? null, $titre, $desc, $prio, $statut, date('Y-m-d', strtotime("$j days")) . " $h:00", $deWf ? $wf : null, $now, $now]);
}
echo 'tâches : ' . $db->query("select count(*) from taches where company_id = 1")->fetchColumn() . "\n";
