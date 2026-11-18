<?php
// Données fictives pour CRM55 (ventes en ligne). Copie de tournage uniquement. Rejouable.
// Remet la page « Guide gratuit » (modèle 2) dans son état d'origine et en brouillon, et crée des commandes fictives.
use App\Models\Commande;
use Illuminate\Support\Facades\DB;

$cid = 1;
$modele = json_decode(file_get_contents('/home/user/video/tutoriels-rapido/_gabarit/ventes-demo/modele-2.json'), true);
// Photos servies par la copie de tournage (public/assets/demo/unsplash) : la vignette d'enregistrement ne les télécharge plus.
foreach ($modele as $k => $v) {
    if (is_string($v)) {
        $modele[$k] = preg_replace('#https:(\\\\*/){2}images\.unsplash\.com\\\\*/(photo-[0-9a-f-]+)\?[^"\\\\ )]*#', '/assets/demo/unsplash/$2.jpg', $v);
    }
}
DB::table('mes_templates_crm')->where('id', 2)->update(array_diff_key($modele, ['id' => 1]));
DB::table('site_pages')->where('id', 2)->update(['statut' => 'brouillon', 'publie_le' => null]);

Commande::where('company_id', $cid)->where('reference', 'like', 'CMD-DEMO%')->delete();
$offres = DB::table('offres')->where('company_id', $cid)->whereIn('nom', ['Shooting photo', 'Site vitrine', 'Carte NFC'])->pluck('id', 'nom');
$lignes = [
    ['Shooting photo', 540, 'payee', 'Claire Fontaine', 'claire.fontaine@exemple.test', 2, 'site'],
    ['Carte NFC', 30, 'payee', 'Paul Marceau', 'paul.marceau@exemple.test', 5, 'linkedin'],
    ['Site vitrine', 1440, 'payee', 'Atelier Garonne', 'contact@atelier-garonne.test', 9, 'site'],
    ['Shooting photo', 540, 'payee', 'Nora Haddad', 'nora.haddad@exemple.test', 14, 'newsletter'],
    ['Carte NFC', 30, 'en_attente', null, null, 1, 'site'],
];
foreach ($lignes as $i => [$produit, $montant, $statut, $nom, $email, $jours, $source]) {
    Commande::create(['company_id' => $cid, 'reference' => 'CMD-DEMO'.(101 + $i), 'offre_id' => $offres[$produit] ?? null, 'site_id' => 1,
        'libelle' => $produit, 'quantite' => 1, 'montant_ttc' => $montant * 100, 'devise' => 'eur', 'statut' => $statut, 'email' => $email, 'nom' => $nom,
        'provenance' => $source, 'payee_le' => $statut === 'payee' ? now()->subDays($jours) : null,
        'created_at' => now()->subDays($jours)->subHours(2), 'updated_at' => now()->subDays($jours)]);
}
echo "Ventes prêtes\n";
