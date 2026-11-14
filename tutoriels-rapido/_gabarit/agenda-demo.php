<?php
// Rendez-vous FICTIFS pour filmer CRM33 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Valeurs réelles de l'écran : type Visioconférence / Présentiel / Téléphonique ; mode d'envoi SMS / Email / SMS et Email.
// Usage : php agenda-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$now = date('Y-m-d H:i:s');
$ent = [];
foreach ($db->query("select id, nom from entreprises where company_id = 1") as $r) { $ent[$r['nom']] = $r['id']; }
$db->exec("delete from rendez_vous_users where rendez_vous_id in (select id from rendez_vous where user_id in (select id from users where company_id = 1))");
$db->exec("delete from rendez_vous_emails where rendez_vous_id in (select id from rendez_vous where user_id in (select id from users where company_id = 1))");
$db->exec("delete from rendez_vous where user_id in (select id from users where company_id = 1)");
// jour relatif à aujourd'hui, heure, durée (min), titre, entreprise, type, mode, organisateur
$rdv = [
    [0, '09:30', 30, 'Démo RapidoCRM', 'Lotus Lounge', 'Visioconférence', 'Email', 1],
    [0, '14:00', 60, 'Point devis', 'Maison Lafitte', 'Présentiel', 'SMS et Email', 1],
    [1, '11:00', 30, 'Appel de suivi', 'Café Mériadeck', 'Téléphonique', 'SMS', 2],
    [1, '16:00', 60, 'Signature du contrat', 'Clover Bistro', 'Présentiel', 'Email', 1],
    [2, '10:00', 45, 'Shooting produits', 'Petal & Plate', 'Présentiel', 'Email', 3],
    [3, '09:00', 30, 'Bilan trimestriel', 'Fournil des Chartrons', 'Visioconférence', 'Email', 1],
    [3, '15:30', 30, 'Relance devis', 'Atelier Garonne', 'Téléphonique', 'SMS', 4],
    [4, '11:30', 60, 'Déjeuner partenaire', 'Boulangerie Saint-Pierre', 'Présentiel', 'Email', 2],
    [7, '10:00', 60, 'Atelier fidélité', 'Lotus Lounge', 'Visioconférence', 'Email', 1],
    [-2, '14:30', 30, 'Découverte des besoins', 'Atelier Garonne', 'Visioconférence', 'Email', 1],
    [-3, '10:30', 60, 'Présentation de l\'offre', 'Clover Bistro', 'Présentiel', 'SMS et Email', 2],
];
foreach ($rdv as [$j, $h, $min, $titre, $nom, $type, $mode, $user]) {
    $debut = date('Y-m-d', strtotime("$j days")) . " $h:00";
    $fin = date('Y-m-d H:i:s', strtotime($debut) + $min * 60);
    $db->prepare("insert into rendez_vous (titre, entreprise_id, date_debut, date_fin, type, mode_envoi, meet_url, user_id, adresse, telephone, commentaire, created_at, updated_at)
        values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")->execute([
        "$titre — $nom", $ent[$nom] ?? null, $debut, $fin, $type, $mode,
        $type === 'Visioconférence' ? 'https://meet.exemple.test/' . substr(md5($titre . $j), 0, 10) : null, $user,
        $type === 'Présentiel' ? '12 quai des Chartrons, Bordeaux' : null, $type === 'Téléphonique' ? '05 56 00 00 00' : null,
        'Préparer la proposition et les tarifs.', $now, $now]);
}
echo 'rendez-vous : ' . $db->query("select count(*) from rendez_vous where user_id in (select id from users where company_id = 1)")->fetchColumn() . "\n";
