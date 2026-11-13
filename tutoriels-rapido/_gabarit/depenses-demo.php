<?php
// Articles de dépense FICTIFS pour filmer CRM14 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Usage : php depenses-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$now = date('Y-m-d H:i:s');
$items = [
    ['Location de studio', 'Prestation de service', 'Demi-journée de studio équipé', 180],
    ['Abonnement retouche photo', 'Prestation de service', 'Licence mensuelle du logiciel de retouche', 29],
    ['Impression de tirages', 'Marchandise', 'Tirages fine art 30 x 40', 75],
    ['Cartes de visite NFC', 'Marchandise', 'Lot de 50 cartes', 60],
];
$ids = [];
foreach ($items as [$nom, $nature, $desc, $prix]) {
    $id = $db->query('select id from items where company_id = 1 and nom = ' . $db->quote($nom))->fetchColumn();
    if (!$id) {
        $db->prepare('insert into items (nom, nature, description, prix_ht, tva, user_id, company_id, created_at, updated_at) values (?, ?, ?, ?, 20, 1, 1, ?, ?)')
            ->execute([$nom, $nature, $desc, $prix, $now, $now]);
        $id = $db->lastInsertId();
    }
    $ids[] = [(int) $id, $prix];
}
$plans = [[0, 1], [2], [0, 3], [1, 2, 3]];
foreach ($db->query('select id from depenses where company_id = 1 order by id')->fetchAll(PDO::FETCH_COLUMN) as $i => $dep) {
    $db->exec("delete from depense_item where depense_id = $dep");
    $ht = 0;
    foreach ($plans[$i % count($plans)] as $k) {
        [$id, $prix] = $ids[$k];
        $db->prepare('insert into depense_item (depense_id, item_id, prix_ht, tva, created_at, updated_at) values (?, ?, ?, 20, ?, ?)')->execute([$dep, $id, $prix, $now, $now]);
        $ht += $prix;
    }
    $db->prepare("update depenses set total_ht = ?, total_tva = ?, total_ttc = ?, mode_paiement = coalesce(mode_paiement, 'Carte bleu') where id = ?")
        ->execute([$ht, round($ht * 0.2, 2), round($ht * 1.2, 2), $dep]);
}
echo "Dépenses de démo prêtes\n";
