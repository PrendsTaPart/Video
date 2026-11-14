<?php
// Documents et bibliothèque FICTIFS pour filmer CRM39 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// - quotas de l'abonnement Premium recopiés depuis le forfait (comme lors d'une vraie souscription) : 10 Go de stockage ;
// - deux documents déjà déposés sur des fiches clients ; trois visuels et un texte dans la bibliothèque.
// Usage : php documents-demo.php <racine de la copie de tournage>
$racine = rtrim($argv[1], '/');
$db = new PDO('sqlite:' . $racine . '/database/database.sqlite');
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$ici = __DIR__;
$pub = $racine . '/storage/app/public';
@mkdir("$pub/foodeatup/entreprise/documents", 0777, true);
@mkdir("$pub/rapidosoftware/bibliotheque", 0777, true);

$db->exec("update abonnement_user_crm set stockage_go_disponibles = (select stockage_go from abonnements_crm a where a.id = abonnement_user_crm.abonnement_id) where user_id = 1");

$db->exec("delete from documents");
$db->exec("delete from bibliotheque_crm where user_id = 1");
$j = fn ($n) => date('Y-m-d H:i:s', strtotime("-$n days 10:00"));
$docs = [[3, 'Cahier des charges', 'demo-cdc-fournil.pdf', 9], [5, 'Bon de commande signé', 'demo-bdc-petal.pdf', 4]];
foreach ($docs as [$ent, $nom, $fichier, $age]) {
    copy("$ici/demo-proposition.pdf", "$pub/foodeatup/entreprise/documents/$fichier");
    $db->prepare("insert into documents (file, filename, type, size, user_id, entreprise_id, created_at, updated_at) values (?, ?, 'application/pdf', ?, 2, ?, ?, ?)")
        ->execute([$fichier, $nom, filesize("$ici/demo-proposition.pdf"), $ent, $j($age), $j($age)]);
}
$biblio = [['banniere-rentree.jpg', 'Bannière rentrée', 'image', 6], ['visuel-linkedin.jpg', 'Visuel LinkedIn', 'image', 3], ['affiche-salon.jpg', 'Affiche salon', 'image', 2], ['argumentaire-telephone.txt', 'Argumentaire téléphone', 'text', 1]];
foreach ($biblio as [$f, $nom, $type, $age]) {
    copy("$ici/biblio-demo/$f", "$pub/rapidosoftware/bibliotheque/$f");
    $db->prepare("insert into bibliotheque_crm (user_id, file, nom, type, taille, created_at, updated_at) values (1, ?, ?, ?, ?, ?, ?)")
        ->execute([$f, $nom, $type, filesize("$ici/biblio-demo/$f"), $j($age), $j($age)]);
}
echo "documents : " . $db->query("select count(*) from documents")->fetchColumn() . " ; bibliothèque : " . $db->query("select count(*) from bibliotheque_crm where user_id = 1")->fetchColumn() . "\n";
