<?php
// Données fictives CRM42 : historique d'abonnements (essai, Medium mensuel, Premium annuel) et de packs.
$db = new PDO('sqlite:'.$argv[1]);
$db->exec("PRAGMA foreign_keys=OFF");
$u = 1;
$db->exec("DELETE FROM abonnement_user_crm WHERE user_id=$u AND created_at < '2026-11-01'");
$ins = $db->prepare("INSERT INTO abonnement_user_crm (user_id, abonnement_id, date_expiration, created_at, updated_at, comptes_commerciaux_disponibles, signature_electronique_disponibles, emails_disponibles, sms_disponibles, visioconference_heures_disponibles, cartes_nfc_disponibles, stockage_go_disponibles, requetes_ia_disponibles) VALUES (?,?,?,?,?,0,0,0,0,0,0,0,0)");
foreach ([[1, '2026-08-04 10:12:00', '2026-09-03 10:12:00'], [3, '2026-09-03 10:15:00', '2026-10-03 10:15:00'], [3, '2026-10-03 10:15:00', '2026-11-02 10:15:00']] as [$a, $c, $e]) {
    $ins->execute([$u, $a, $e, $c, $c]);
}
$db->exec("UPDATE abonnement_user_crm SET abonnement_id=4, created_at='2026-11-02 10:15:00', updated_at='2026-11-02 10:15:00', date_expiration='2027-11-02 10:15:00', emails_disponibles=4380, sms_disponibles=2210, signature_electronique_disponibles=94, stockage_go_disponibles=10 WHERE user_id=$u AND created_at >= '2026-11-01'");
$db->exec("DELETE FROM user_pack WHERE stripe_session_id LIKE 'demo_crm42_%'");
$taille = function ($type, $size) use ($db) {
    $q = $db->prepare("SELECT ps.id, p.id FROM pack_sizes ps JOIN packs p ON p.id=ps.pack_id WHERE p.type=? AND ps.size=?");
    $q->execute([$type, $size]);
    return $q->fetch(PDO::FETCH_NUM);
};
$p = $db->prepare("INSERT INTO user_pack (user_id, pack_id, size_id, quantite, created_at, updated_at, stripe_session_id) VALUES (?,?,?,1,?,?,?)");
foreach ([['sms', 500, '2026-09-18 14:02:00'], ['email', 5000, '2026-10-07 09:40:00'], ['agent_vocal', 30, '2026-11-09 16:25:00']] as $i => [$type, $size, $date]) {
    $t = $taille($type, $size);
    if ($t) { $p->execute([$u, $t[1], $t[0], $date, $date, 'demo_crm42_'.$i]); } else { fwrite(STDERR, "pack introuvable : $type $size\n"); }
}
echo "abonnement-demo OK\n";
