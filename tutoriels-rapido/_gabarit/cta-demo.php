<?php
// CTA FICTIFS pour filmer CRM25 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Usage : php cta-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec("delete from cta_crm where user_id = 1");
$t = fn ($j) => date('Y-m-d H:i:s', time() - $j * 86400);
foreach ([
    ['Prendre rendez-vous', 'url', 'https://studio-lumiere.test/rendez-vous', 184, 47, 9],
    ['Nous écrire', 'mail', 'contact@studio-lumiere.test', 96, 18, 6],
    ['Recevoir l\'offre par SMS', 'sms', '+33 5 56 00 12 34', 73, 21, 3],
] as [$nom, $type, $lien, $vues, $clics, $j]) {
    $db->prepare('insert into cta_crm (user_id, nom, vue, click, type, lien, created_at, updated_at) values (1, ?, ?, ?, ?, ?, ?, ?)')
        ->execute([$nom, $vues, $clics, $type, $lien, $t($j), $t($j)]);
}
echo "CTA de démo prêts\n";
