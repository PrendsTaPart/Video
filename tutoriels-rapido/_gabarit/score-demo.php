<?php
// Scores FICTIFS pour filmer CRM64 (score des prospects). Copie de tournage uniquement. Rejouable :
// barème par défaut, scores et historique remis à zéro, tâches « Prospect chaud » de démo supprimées, puis interactions simulées.
// Usage : php artisan tinker puis require '/home/user/video/tutoriels-rapido/_gabarit/score-demo.php';
$u = App\Models\User::where('email', 'demo@rapido.test')->first();
$cid = $u->company_id;
DB::table('score_reglages')->where('company_id', $cid)->delete();
DB::table('score_historique')->where('company_id', $cid)->delete();
App\Models\Contact::where('company_id', $cid)->update(['score_engagement' => 0, 'chaud_le' => null]);
DB::table('taches')->where('company_id', $cid)->where('titre', 'like', 'Prospect chaud :%')->delete();
$s = app(App\Services\ScoreService::class);
$c = App\Models\Contact::where('company_id', $cid)->orderBy('id')->take(6)->get()->values();
$parcours = [
    0 => [['email_ouvert', 'Newsletter de novembre'], ['email_clic', 'Lien « Nos offres »'], ['lead_magnet', 'Guide : 10 idées de menus'], ['devis_vu', 'Devis D-2026-014'], ['rdv', 'Rendez-vous du 18/11']],
    1 => [['formulaire', 'Formulaire de contact'], ['devis_demande', 'Devis en ligne : traiteur'], ['email_clic', 'Relance devis'], ['devis_vu', 'Devis D-2026-015']],
    2 => [['email_ouvert', 'Newsletter de novembre'], ['cta', 'Bannière « Essai gratuit »'], ['sondage', 'Satisfaction 2026']],
    3 => [['carte', 'Carte digitale de Léa Martin'], ['fidelite', 'Programme Les Gourmands']],
    4 => [['email_ouvert', 'Newsletter de novembre']],
];
foreach ($parcours as $i => $evts) {
    foreach ($evts as [$e, $d]) { if (isset($c[$i])) { $s->ajouter($c[$i]->fresh(), $e, $d); } }
}
echo 'scores : '.App\Models\Contact::where('company_id', $cid)->where('score_engagement', '>', 0)->count().' contacts, '.$s->chauds($cid)->count()." chaud(s)\n";
