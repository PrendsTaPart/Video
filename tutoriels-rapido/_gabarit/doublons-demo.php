<?php
// Doublons FICTIFS pour filmer CRM62 (fusion des doublons). Copie de tournage uniquement.
// Rejouable : supprime d'abord les doublons de démo, les fusions et les « ce ne sont pas des doublons » de la société,
// et remet les fiches d'origine telles qu'avant la fusion (champs complétés par la fusion vidés).
// Usage : php artisan tinker puis require '/home/user/video/tutoriels-rapido/_gabarit/doublons-demo.php';
$u = App\Models\User::where('email', 'demo@rapido.test')->first();
$cid = $u->company_id;
$noms = ['Maison Lafitte SARL', 'Lotus Lounge SAS'];
App\Models\Entreprise::withTrashed()->where('company_id', $cid)->whereIn('nom', $noms)->forceDelete();
App\Models\Entreprise::withTrashed()->where('company_id', $cid)->whereIn('nom', ['Maison Lafitte', 'Lotus Lounge'])->restore();
App\Models\Entreprise::where('company_id', $cid)->whereIn('nom', ['Maison Lafitte', 'Lotus Lounge'])->update(['telephone' => null, 'siret' => null]);
App\Models\Contact::where('company_id', $cid)->where('email', 'camille.demo@exemple.test')->delete();
App\Models\Contact::where('company_id', $cid)->where('email', 'camille@exemple.test')->update(['telephone' => null]);
DB::table('fusions')->where('company_id', $cid)->delete();
DB::table('doublons_ignores')->where('company_id', $cid)->delete();

$base = ['company_id' => $cid, 'user_id' => $u->id];
App\Models\Entreprise::create($base + ['nom' => 'Maison Lafitte SARL', 'email' => 'contact@maisonlafitte.test', 'telephone' => '05 56 12 34 56', 'siret' => '81234567800019']);
App\Models\Entreprise::create($base + ['nom' => 'Lotus Lounge SAS', 'email' => 'reservation@lotuslounge.test', 'telephone' => '05 56 98 76 54']);
$camille = App\Models\Contact::where('company_id', $cid)->where('email', 'camille@exemple.test')->first();
App\Models\Contact::create(['company_id' => $cid, 'entreprise_id' => $camille?->entreprise_id, 'nom' => 'Démo', 'prenom' => 'Camille',
    'email' => 'camille.demo@exemple.test', 'telephone' => '06 12 34 56 78']);
$d = app(App\Services\DoublonService::class);
echo 'doublons : '.count($d->detecter($cid, 'entreprise')).' groupe(s) de clients, '.count($d->detecter($cid, 'contact'))." groupe(s) de contacts\n";
