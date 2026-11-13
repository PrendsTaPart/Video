<?php
// CRM27 : formulaire d'inscription au jeu (prérequis de l'objectif « Remplir un formulaire ») et nettoyage
// des jeux « Roue des fêtes » d'une prise précédente (copie de tournage /home/user/rapido-crm-film uniquement).
// Usage : php jeux-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
foreach ($db->query("select id from companies_games where company_id = 1 and name = 'Roue des fêtes'")->fetchAll(PDO::FETCH_COLUMN) as $g) {
    $db->exec("delete from game_components where game_id = $g");
    $db->exec("delete from companies_games where id = $g");
}
if (!$db->query("select count(*) from forms_crm where user_id = 1 and nom = 'Inscription jeu concours'")->fetchColumn()) {
    $now = date('Y-m-d H:i:s');
    $db->prepare("insert into forms_crm (user_id, entreprise_id, nom, type, lien, champs, vue, click, created_at, updated_at) values (1, null, 'Inscription jeu concours', 'contact', '', ?, 0, 0, ?, ?)")
        ->execute([serialize(['nom', 'prenom', 'email', 'telephone']), $now, $now]);
}
echo "Jeux de démo prêts\n";
