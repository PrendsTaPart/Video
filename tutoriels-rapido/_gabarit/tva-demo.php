<?php
// Taux de TVA de démo pour filmer CRM11+ (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Usage : php tva-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$now = date('Y-m-d H:i:s');
foreach ([['TVA réduite', 5.5], ['TVA intermédiaire', 10], ['TVA normale', 20]] as $i => [$nom, $p]) {
    if ($db->query("select count(*) from tvas where company_id = 1 and nom = " . $db->quote($nom))->fetchColumn()) continue;
    $t = date('Y-m-d H:i:s', time() - (10 - $i));
    $db->prepare('insert into tvas (nom, pourcentage, company_id, created_at, updated_at) values (?, ?, 1, ?, ?)')->execute([$nom, $p, $t, $t]);
}
echo "TVA de démo prêtes\n";
// Descriptions des produits de démo (la fiche produit affichait une description vide).
$desc = [
    'Site vitrine' => 'Site de 5 pages, responsive, optimisé pour le référencement local et livré en 3 semaines.',
    'Maintenance mensuelle' => 'Mises à jour, sauvegardes quotidiennes et petites modifications de contenu, chaque mois.',
    'Shooting photo' => 'Séance photo d\'une demi-journée sur site, 20 photos retouchées livrées sous 10 jours.',
    'Carte NFC' => 'Carte de visite connectée : un simple contact du téléphone ouvre votre fiche digitale.',
    'Campagne réseaux' => 'Un mois de publications sur Instagram, Facebook et LinkedIn, visuels compris.',
];
foreach ($desc as $nom => $txt) {
    $db->prepare("update offres set description = ? where company_id = 1 and nom = ? and (description is null or description = '')")->execute(['<p>' . $txt . '</p>', $nom]);
}
echo "Descriptions de démo prêtes\n";
