<?php
// Données fictives pour CRM13 (factures). Copie de tournage uniquement. Rejouable (php artisan tinker).
// Lignes des factures de démonstration (cohérentes avec leurs totaux), échéances passées pour les relances,
// relances des factures désactivées (le tutoriel les active), historique des relances de la démo vidé.
use Illuminate\Support\Facades\DB;

$lignes = [4 => [[1, 1250]], 5 => [[3, 450], [5, 530]], 6 => [[3, 450]], 7 => [[5, 690]], 19 => [[3, 450]]];
foreach ($lignes as $facture => $offres) {
    DB::table('facture_offre')->where('facture_id', $facture)->delete();
    foreach ($offres as [$offre, $prix]) {
        DB::table('facture_offre')->insert(['facture_id' => $facture, 'offre_id' => $offre, 'prix_ht' => $prix, 'tva' => 20, 'created_at' => now(), 'updated_at' => now()]);
    }
}
DB::table('factures')->where('id', 7)->update(['date_fin' => now()->subDays(7)->toDateString(), 'destinataire' => 'contact@cafemeriadeck.test']);
DB::table('factures')->where('id', 6)->update(['date_fin' => now()->subDay()->toDateString(), 'destinataire' => 'contact@ateliergaronne.test']);
DB::table('relance_parametres')->updateOrInsert(['company_id' => 1], ['factures_actif' => 0, 'devis_actif' => 0, 'factures_jours' => json_encode([1, 7, 15]), 'devis_jours' => json_encode([3, 7, 14]), 'updated_at' => now(), 'created_at' => now()]);
DB::table('relances')->where('company_id', 1)->delete();
echo 'Factures prêtes : '.DB::table('facture_offre')->count()." lignes\n";
