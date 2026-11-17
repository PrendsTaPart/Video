<?php
// Données fictives pour CRM83 (facture électronique Factur-X). Copie de tournage uniquement. Rejouable.
// Facture n° 1 (Maison Lafitte, 2 880 € TTC) : deux lignes, adresse du client ; numéro de TVA de la société vidé
// pour que le contrôle des mentions obligatoires s'affiche, puis soit corrigé dans le tutoriel.
use App\Models\Company;
use App\Models\Entreprise;
use App\Models\Facture;
use App\Models\User;
use Illuminate\Support\Facades\DB;

$u = User::where('email', 'demo@rapido.test')->firstOrFail();
$c = Company::findOrFail($u->company_id);
$c->num_tva = null;
$c->pays = 'FR';
$c->save();

$f = Facture::where('company_id', $c->id)->orderBy('id')->firstOrFail();
$e = Entreprise::findOrFail($f->entreprise_id);
$e->adresse = '12 rue Sainte-Catherine';
$e->code_postal = '33000';
$e->ville = 'Bordeaux';
$e->siret = '98765432100018';
$e->save();

DB::table('facture_offre')->where('facture_id', $f->id)->delete();
DB::table('facture_offre_supplementaire')->where('facture_id', $f->id)->delete();
$site = DB::table('offres')->where('company_id', $c->id)->where('nom', 'Site vitrine')->value('id');
$photo = DB::table('offres')->where('company_id', $c->id)->where('nom', 'Shooting photo')->value('id');
DB::table('facture_offre')->insert([
    ['facture_id' => $f->id, 'offre_id' => $site, 'prix_ht' => 1950, 'tva' => 20, 'created_at' => now(), 'updated_at' => now()],
    ['facture_id' => $f->id, 'offre_id' => $photo, 'prix_ht' => 450, 'tva' => 20, 'created_at' => now(), 'updated_at' => now()],
]);
$f->total_ht = 2400; $f->total_tva = 480; $f->total_ttc = 2880; $f->remise = 0; $f->delai_paiement = 30;
$f->save();
echo "Facture {$f->id} prête ({$e->nom}), TVA société vidée\n";
