<?php
// Avis clients FICTIFS sur la fiche « Fournil des Chartrons » pour filmer CRM29
// (copie de tournage /home/user/rapido-crm-film, jamais le dépôt). Usage : php avis-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$ent = $db->query("select id from entreprises where company_id = 1 and nom = 'Fournil des Chartrons'")->fetchColumn();
$db->prepare('delete from entreprise_avis where entreprise_id = ?')->execute([$ent]);
foreach ([
    ['Sophie L.', 5, 'Des photos magnifiques de notre boutique, très professionnel et à l\'écoute.', 18],
    ['Marc D.', 4, 'Séance agréable et rapide, livraison des images dans les temps.', 11],
    ['Julie R.', 5, 'Notre vitrine n\'a jamais été aussi belle sur Instagram. Merci !', 4],
] as [$auteur, $note, $txt, $j]) {
    $t = date('Y-m-d H:i:s', time() - $j * 86400);
    $db->prepare('insert into entreprise_avis (entreprise_id, company_id, auteur, note, commentaire, date, created_at, updated_at) values (?, 1, ?, ?, ?, ?, ?, ?)')
        ->execute([$ent, $auteur, $note, $txt, substr($t, 0, 10), $t, $t]);
}
echo "Avis de démo prêts (entreprise #$ent)\n";
