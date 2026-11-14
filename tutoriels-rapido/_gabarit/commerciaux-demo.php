<?php
// Équipe commerciale FICTIVE pour filmer CRM36 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Objectifs mensuels pour Karim et Sophie (Yanis sans objectif), SMS et e-mails envoyés ce mois-ci.
// Usage : php commerciaux-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$now = date('Y-m-d H:i:s');
$users = [2 => [40, 30, 25, 8, 3, 20, 26, 18], 3 => [30, 20, 30, 6, 2, 15, 12, 24], 4 => null];
// [sms, appel, email, rdv, contrat, prospection, sms envoyés, e-mails envoyés]
$db->exec("delete from objectifs where user_id in (2, 3, 4)");
$db->exec("delete from sms where user_id in (2, 3, 4) and message like '[démo]%'");
$db->exec("delete from emails where user_id in (2, 3, 4) and sujet like '[démo]%'");
$ents = $db->query("select id from entreprises where company_id = 1 order by id limit 8")->fetchAll(PDO::FETCH_COLUMN);
foreach ($users as $uid => $v) {
    $db->prepare("update users set disponible = ? where id = ?")->execute([$uid === 4 ? 0 : 1, $uid]);
    if (! $v) { continue; }
    $db->prepare("insert into objectifs (nombre_sms, nombre_appel, nombre_email, nombre_RDV, nombre_contrat, nombre_prospection, user_id, created_at, updated_at) values (?, ?, ?, ?, ?, ?, ?, ?, ?)")
        ->execute([$v[0], $v[1], $v[2], $v[3], $v[4], $v[5], $uid, $now, $now]);
    for ($i = 0; $i < $v[6]; $i++) {
        $quand = date('Y-m-d H:i:s', strtotime(date('Y-m-01') . ' +' . ($i % max(1, (int) date('j'))) . ' days 10:00'));
        $db->prepare("insert into sms (entreprise_id, user_id, numero, message, created_at, updated_at) values (?, ?, '0600000000', '[démo] Rappel de rendez-vous', ?, ?)")->execute([$ents[$i % count($ents)], $uid, $quand, $quand]);
    }
    for ($i = 0; $i < $v[7]; $i++) {
        $quand = date('Y-m-d H:i:s', strtotime(date('Y-m-01') . ' +' . ($i % max(1, (int) date('j'))) . ' days 11:00'));
        $db->prepare("insert into emails (entreprise_id, user_id, destinataire, sujet, contenu, created_at, updated_at) values (?, ?, 'contact@client.exemple.test', '[démo] Suivi de votre devis', 'Bonjour…', ?, ?)")->execute([$ents[$i % count($ents)], $uid, $quand, $quand]);
    }
}
echo "objectifs : " . $db->query("select count(*) from objectifs where user_id in (2,3,4)")->fetchColumn() . "\n";
