<?php
// Données fictives pour CRM75 / CRM76 (Marketing Map). Copie de tournage uniquement. Rejouable.
//   - supprime les cartes de la société de démo ;
//   - crée une carte ACTIVE « Salon de l'habitat » (modèle carte digitale + devis), reliée à la carte et au formulaire de devis de démo ;
//   - fait avancer 14 contacts fictifs dans les blocs (carte scannée, devis demandé, e-mail ouvert, appel, achat).
// Avec l'argument CRM75 (variable $mode), s'arrête après la suppression : l'épisode crée sa carte à l'écran.
use App\Models\Contact;
use App\Models\MarketingMap;
use App\Models\MarketingMapBloc;
use App\Models\User;
use App\Services\MarketingMapService;
use App\Services\MarketingMapSuiviService;
use Illuminate\Support\Facades\DB;

$u = User::where('email', 'demo@rapido.test')->firstOrFail();
$cid = $u->company_id;
$svc = app(MarketingMapService::class);
MarketingMap::where('company_id', $cid)->get()->each(fn ($m) => $svc->supprimer($m));
DB::table('sequences')->where('company_id', $cid)->where('nom', 'like', 'Marketing Map —%')->delete();
if (($mode ?? '') === 'CRM75') {
    echo "Marketing Map : aucune carte (épisode CRM75)\n";

    return;
}
$m = $svc->creer($cid, $u->id, ['nom' => 'Salon de l’habitat', 'modele' => 'carte_devis', 'objectif' => 'Transformer les rencontres du salon en devis signés']);
$carte = DB::table('cartes_digitales')->where('company_id', $cid)->value('id');
$form = DB::table('formulaires_devis')->where('company_id', $cid)->value('id');
MarketingMapBloc::where('marketing_map_id', $m->id)->where('cle', 'carte')->update(['ressource_type' => 'carte', 'ressource_id' => $carte]);
MarketingMapBloc::where('marketing_map_id', $m->id)->where('cle', 'devis')->update(['ressource_type' => 'formulaire_devis', 'ressource_id' => $form]);
$r = $svc->activer($m->fresh(), $u->id);
$seq = $r['sequence_id'];
$suivi = app(MarketingMapSuiviService::class);
$contacts = Contact::where('company_id', $cid)->orderBy('id')->limit(14)->get();
foreach ($contacts as $i => $c) {
    $suivi->enregistrer($c, 'carte', ['type' => 'carte', 'id' => $carte]);
    if ($i < 9) {
        $suivi->enregistrer($c, 'devis_demande', ['type' => 'formulaire_devis', 'id' => $form]);
    }
    if ($i < 6 && $seq) {
        $suivi->enregistrer($c, 'email_ouvert', ['type' => 'sequence', 'id' => $seq]);
    }
    if ($i < 3 && $seq) {
        $suivi->enregistrer($c, 'appel', ['type' => 'sequence', 'id' => $seq]);
    }
    if ($i < 2) {
        $suivi->enregistrer($c, 'achat');
    }
}
echo 'Marketing Map : carte '.$m->id.' active, '.DB::table('marketing_map_positions')->where('marketing_map_id', $m->id)->count()." positions\n";
