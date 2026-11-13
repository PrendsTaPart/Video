<?php
// Lignes de devis et de factures FICTIVES pour filmer CRM12/CRM13
// (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// Les devis/factures de démo n'avaient aucune ligne : l'aperçu affichait un tableau vide.
// On leur donne des lignes du catalogue et on recalcule les totaux (TVA 20 %).
// Usage : php facturation-demo.php <database.sqlite>
$db = new PDO('sqlite:' . $argv[1]);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$prix = $db->query('select id, prix_ht from offres where company_id = 1 and id <= 5')->fetchAll(PDO::FETCH_KEY_PAIR);
$plans = [[1, 3, 5], [1, 5], [3, 2], [1, 3, 5, 2], [3, 5], [5], [1, 2], [1, 3]];
$now = date('Y-m-d H:i:s');
foreach (['devis' => 'devis_offre', 'factures' => 'facture_offre'] as $table => $pivot) {
    $cle = $table === 'devis' ? 'devis_id' : 'facture_id';
    foreach ($db->query("select id from $table where company_id = 1 order by id")->fetchAll(PDO::FETCH_COLUMN) as $i => $id) {
        $db->exec("delete from $pivot where $cle = $id");
        $ht = 0;
        foreach ($plans[$i % count($plans)] as $o) {
            if (!isset($prix[$o])) continue;
            $db->prepare("insert into $pivot ($cle, offre_id, prix_ht, tva, created_at, updated_at) values (?, ?, ?, 20, ?, ?)")
                ->execute([$id, $o, $prix[$o], $now, $now]);
            $ht += $prix[$o];
        }
        $db->prepare("update $table set total_ht = ?, total_tva = ?, total_ttc = ?, delai_paiement = coalesce(delai_paiement, '14 jours'), mode_paiement = coalesce(mode_paiement, 'Virement') where id = ?")
            ->execute([$ht, round($ht * 0.2, 2), round($ht * 1.2, 2), $id]);
    }
}
echo "Lignes de devis et factures de démo prêtes\n";
