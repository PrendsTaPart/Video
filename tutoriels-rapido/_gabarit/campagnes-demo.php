<?php
// Campagnes e-mail, SMS et newsletters FICTIVES pour filmer CRM17–CRM19
// (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Usage : php campagnes-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$j = fn ($n) => date('Y-m-d H:i:s', strtotime("$n days 10:00"));
$db->exec("delete from campagne_sms where company_id = 1 and contenu like '%Studio Lumière%'");
$emails = [
    ['Entreprises', 'Commerce', -12, 'Vos photos d\'équipe pour 2027', '<p>Bonjour,</p><p>Nouvelle année, nouveau site ? Nous réalisons vos portraits d\'équipe sur place, en une demi-journée.</p><p>Léa — Studio Lumière</p>'],
    ['Contacts', null, -5, 'Offre de fin d\'année : -15 %', '<p>Pour les fêtes, -15 % sur les séances photo réservées avant le 20 décembre.</p>'],
    ['Entreprises', 'Commerce', 3, 'Invitation : portes ouvertes au studio', '<p>Venez découvrir le studio le 16 novembre, de 17 h à 20 h. Verre de l\'amitié offert !</p>'],
];
foreach ($emails as [, , , $objet]) {
    $db->prepare('delete from campagne_email where company_id = 1 and objet = ?')->execute([$objet]);
}
foreach ($emails as [$cible, $dom, $n, $objet, $html]) {
    $db->prepare('insert into campagne_email (cible, domaine, date_envoi, contenu, company_id, objet, created_at, updated_at) values (?, ?, ?, ?, 1, ?, ?, ?)')
        ->execute([$cible, $dom, $j($n), $html, $objet, $j(min($n, 0) - 1), $j(min($n, 0) - 1)]);
}
$sms = [
    ['Contacts', null, -8, 'Studio Lumière : -15 % sur les portraits d\'équipe jusqu\'au 20/12. Réservez en répondant OUI.'],
    ['Entreprises', 'Commerce', 2, 'Studio Lumière : portes ouvertes le 16/11 de 17 h à 20 h. On vous attend !'],
];
foreach ($sms as [$cible, $dom, $n, $txt]) {
    $db->prepare('insert into campagne_sms (cible, domaine, date_envoi, contenu, company_id, created_at, updated_at) values (?, ?, ?, ?, 1, ?, ?)')
        ->execute([$cible, $dom, $j($n), $txt, $j(min($n, 0) - 1), $j(min($n, 0) - 1)]);
}
echo "Campagnes de démo prêtes\n";
