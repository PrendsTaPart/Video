<?php
// Relances automatiques FICTIVES pour filmer CRM44 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Destinataires en @exemple.test, réglages activés, quelques relances déjà envoyées, devis « vus ».
// Usage : php relances-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$slug = fn ($s) => trim(preg_replace('/[^a-z0-9]+/', '', strtolower(iconv('UTF-8', 'ASCII//TRANSLIT', $s))));
foreach (['devis', 'factures'] as $t) {
    foreach ($db->query("select d.id, e.nom from $t d join entreprises e on e.id = d.entreprise_id where d.company_id = 1") as $r) {
        $db->prepare("update $t set destinataire = ? where id = ?")->execute(['contact@' . $slug($r['nom']) . '.exemple.test', $r['id']]);
    }
}
$db->exec("update factures set date_fin = date('now', '-4 days') where company_id = 1 and id = 7");
$db->exec("update devis set vu_le = null, nb_vues = 0 where company_id = 1");
$db->exec("update devis set vu_le = datetime('now', '-15 days', '+3 hours'), nb_vues = 2 where company_id = 1 and id = 7");
$db->exec("update devis set vu_le = datetime('now', '-12 days', '+5 hours'), nb_vues = 1 where company_id = 1 and id = 8");
$now = date('Y-m-d H:i:s');
$db->exec("delete from relance_parametres where company_id = 1");
$db->prepare("insert into relance_parametres (company_id, devis_actif, devis_jours, factures_actif, factures_jours, created_at, updated_at) values (1, 1, '[3,7,14]', 1, '[1,7,15]', ?, ?)")->execute([$now, $now]);
$db->exec("delete from relances where company_id = 1");
$hist = [
    ['devis', 6, 1, "date((select created_at from devis where id = 6), '+3 days') || ' 09:15:00'"],
    ['devis', 6, 2, "date((select created_at from devis where id = 6), '+7 days') || ' 09:15:00'"],
    ['devis', 7, 1, "date((select created_at from devis where id = 7), '+3 days') || ' 09:15:00'"],
    ['facture', 6, 1, "date((select created_at from factures where id = 6), '+15 days') || ' 09:15:00'"],
];
foreach ($hist as [$type, $id, $niveau, $date]) {
    $table = $type === 'devis' ? 'devis' : 'factures';
    $dest = $db->query("select destinataire from $table where id = $id")->fetchColumn();
    $db->exec("insert into relances (company_id, document_type, document_id, niveau, destinataire, statut, envoye_le, created_at, updated_at) values (1, '$type', $id, $niveau, " . $db->quote($dest) . ", 'envoyee', $date, '$now', '$now')");
}
echo "Relances de démo prêtes\n";
