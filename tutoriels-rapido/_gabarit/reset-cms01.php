<?php
// Remet à zéro le compte fictif filmé dans CMS01 (base SQLite LOCALE de RapidoCMS uniquement).
// Usage : php reset-cms01.php /chemin/vers/rapido-cms/database/database.sqlite
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$u = $db->query("select id, company_id from users where email = 'camille.durand@atelier-camille.test'")->fetch(PDO::FETCH_ASSOC);
if ($u) {
    if ($u['company_id']) {
        $db->exec('delete from abonnement_user_cms where entreprise_id = ' . (int) $u['company_id']);
        $db->exec('delete from companies where id = ' . (int) $u['company_id']);
    }
    $db->exec('delete from users where id = ' . (int) $u['id']);
}
$db->exec("delete from companies where email = 'contact@atelier-camille.test'");
echo "Compte de démonstration CMS01 réinitialisé\n";
