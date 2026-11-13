<?php
// Contrats envoyés et modèles d'e-mail/SMS FICTIFS pour filmer CRM12–CRM18
// (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Usage : php contrats-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$now = date('Y-m-d H:i:s');

// Modèles d'e-mail et de SMS (catégories libres)
$emails = [
    ['Envoi de devis', 'Devis', '<p>Bonjour,</p><p>Vous trouverez ci-joint notre proposition. Elle reste valable 30 jours.</p><p>Belle journée,<br>Léa Martin — Studio Lumière</p>'],
    ['Envoi de contrat', 'Autre', '<p>Bonjour,</p><p>Voici votre contrat. Il se signe en ligne en deux minutes, depuis le lien ci-dessous.</p><p>Merci de votre confiance,<br>Léa Martin — Studio Lumière</p>'],
    ['Relance facture', 'Relance', '<p>Bonjour,</p><p>Petit rappel : votre facture est en attente de règlement. Vous pouvez la payer par carte depuis le lien ci-dessous.</p><p>Merci,<br>Studio Lumière</p>'],
    ['Bienvenue nouveau client', 'Notification', '<p>Bienvenue chez Studio Lumière !</p><p>Votre espace client est prêt. Répondez simplement à cet e-mail si vous avez une question.</p>'],
    ['Offre de fin d\'année', 'Marketing', '<p>Pour les fêtes, -15 % sur les séances photo d\'équipe réservées avant le 20 décembre.</p><p>À très vite au studio !</p>'],
];
foreach ($emails as [$nom, $cat, $html]) {
    if ($db->query('select count(*) from template_emails where company_id = 1 and nom = ' . $db->quote($nom))->fetchColumn()) {
        $db->prepare('update template_emails set categorie = ? where company_id = 1 and nom = ?')->execute([$cat, $nom]);
        continue;
    }
    $db->prepare('insert into template_emails (company_id, nom, contenu, categorie, created_at, updated_at) values (1, ?, ?, ?, ?, ?)')->execute([$nom, $html, $cat, $now, $now]);
}
$sms = [
    ['Rappel de rendez-vous', 'RDV', 'Bonjour, petit rappel de votre séance photo demain à 10 h au Studio Lumière. À demain !'],
    ['Devis envoyé', 'Devis', 'Bonjour, votre devis Studio Lumière vient de vous être envoyé par e-mail. Bonne lecture !'],
    ['Offre flash', 'Marketing', 'Studio Lumière : -15 % sur les portraits d\'équipe jusqu\'au 20/12. Réservez en répondant OUI.'],
];
foreach ($sms as [$nom, $cat, $txt]) {
    if ($db->query('select count(*) from template_sms where company_id = 1 and nom = ' . $db->quote($nom))->fetchColumn()) {
        $db->prepare('update template_sms set categorie = ? where company_id = 1 and nom = ?')->execute([$cat, $nom]);
        continue;
    }
    $db->prepare('insert into template_sms (company_id, nom, contenu, categorie, created_at, updated_at) values (1, ?, ?, ?, ?, ?)')->execute([$nom, $txt, $cat, $now, $now]);
}

// Contrats envoyés aux clients : deux signés, deux en attente
$db->exec("delete from contrat_user_crm where (id between 9001 and 9010) or (user_id = 1 and destinataire like '%.test')");
$ents = $db->query('select id, email from entreprises where company_id = 1 and deleted_at is null order by id limit 4')->fetchAll(PDO::FETCH_ASSOC);
$envois = [[1, 'signature_demo_1.png', 12], [3, 'signature_demo_2.png', 8], [2, null, 3], [4, null, 1]];
foreach ($envois as $i => [$contrat, $sig, $jours]) {
    if (!isset($ents[$i])) break;
    $t = date('Y-m-d H:i:s', time() - $jours * 86400);
    $db->prepare('insert into contrat_user_crm (id, user_id, destinataire, content, debut, fin, contrat_id, entreprise_id, signature, created_at, updated_at) values (?, 1, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
        ->execute([9001 + $i, $ents[$i]['email'], $emails[1][2], date('Y-m-d', time() - $jours * 86400), date('Y-m-d', time() + 365 * 86400), $contrat, $ents[$i]['id'], $sig, $t, $t]);
}
echo "Contrats et modèles de démo prêts\n";
