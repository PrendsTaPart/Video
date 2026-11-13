<?php
// Comptes de réseaux sociaux FICTIFS pour filmer RapidoCMS en local (jetons factices, aucune connexion réelle).
// Usage : php reseaux-demo.php <database.sqlite> ajouter|retirer
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$tables = ['cms_parametres_facebook', 'cms_parametres_linkedin', 'cms_parametres_instagram'];
foreach ($tables as $t) {
    $db->exec("delete from $t where access_token = 'demo-token'");
}
if (($argv[2] ?? 'ajouter') === 'ajouter') {
    $now = date('Y-m-d H:i:s');
    $exp = date('Y-m-d H:i:s', strtotime('+60 days'));
    $db->prepare('insert into cms_parametres_facebook (entreprise_id,page_id,page_name,page_img,access_token,expires_in,created_at,updated_at) values (1,?,?,?,?,?,?,?)')
        ->execute(['100000000000001', 'Studio Lumière', '/assets/img/dash/Facebook.png', 'demo-token', $exp, $now, $now]);
    $db->prepare('insert into cms_parametres_instagram (entreprise_id,page_id,page_name,page_img,access_token,expires_in,created_at,updated_at) values (1,?,?,?,?,?,?,?)')
        ->execute(['300000000000001', 'studio.lumiere', '/assets/img/dash/Instagram.png', 'demo-token', $exp, $now, $now]);
    $db->prepare('insert into cms_parametres_linkedin (entreprise_id,page_id,page_name,access_token,expires_in,created_at,updated_at) values (1,?,?,?,?,?,?)')
        ->execute(['200000001', 'Studio Lumière', 'demo-token', $exp, $now, $now]);
    echo "Comptes fictifs ajoutés\n";
} else {
    echo "Comptes fictifs retirés\n";
}
