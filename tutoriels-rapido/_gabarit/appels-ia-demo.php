<?php
// Données fictives pour CRM86 (appels → analyse de réunion). Copie de tournage uniquement : trois appels de l'agent vocal IA
// (un prospect inconnu avec transcription, un client connu, un appel sans transcription), réglages remis à zéro. Rejouable.
use App\Models\AgentVocalAppel;
use App\Models\AgentVocalConfig;
use App\Models\Company;
use App\Models\Reunion;
use App\Models\User;

$u = User::where('email', 'demo@rapido.test')->firstOrFail();
$cid = $u->company_id;
Company::whereKey($cid)->update(['appels_enregistrement' => false, 'appels_analyse_auto' => false]);
foreach (Reunion::where('company_id', $cid)->whereNotNull('origine')->get() as $r) {
    app(\App\Services\ReunionService::class)->supprimer($r);
}
\App\Models\Contact::where('company_id', $cid)->where('source_canal', 'reunion')->delete();
\App\Models\Tache::where('company_id', $cid)->where('description', 'like', 'Issue de la réunion%')->delete();
$rv = \App\Models\RendezVous::where('titre', 'like', 'Suivi — %')->pluck('id');
\App\Models\RendezVousUser::whereIn('rendez_vous_id', $rv)->delete();
\App\Models\RendezVous::whereIn('id', $rv)->delete();
$config = AgentVocalConfig::firstOrCreate(['company_id' => $cid], ['user_id' => $u->id, 'entreprise_nom' => 'Rapido Studio',
    'entreprise_pitch' => 'Sites et outils marketing pour commerces.', 'entreprise_secteur' => 'marketing', 'objectif_appel' => 'rdv', 'ton_voix' => 'professionnel', 'actif' => true]);
AgentVocalAppel::where('company_id', $cid)->delete();
$cafe = \App\Models\Entreprise::firstOrCreate(['company_id' => $cid, 'nom' => 'Café des Arts'], ['user_id' => $u->id]);
$base = ['company_id' => $cid, 'user_id' => $u->id, 'entreprise_id' => 1, 'config_id' => $config->id, 'direction' => 'inbound', 'statut' => 'termine'];
$t = fn ($role, $s, $m) => ['role' => $role, 'message' => $m, 'time_in_call_secs' => $s];
AgentVocalAppel::create(array_merge($base, ['entreprise_id' => $cafe->id, 'telephone' => '+33633445566', 'duree_secondes' => 58, 'resultat' => 'rdv_pris', 'created_at' => now()->subHour(),
    'resume_ia' => 'Julien Morel (Café des Arts) souhaite un site avec commande en ligne, budget 3 000 €. Rendez-vous en visio jeudi prochain.',
    'transcript_json' => [
        $t('agent', 0, 'Bonjour, vous êtes bien chez Rapido Studio. Je suis l’assistant vocal, comment puis-je vous aider ?'),
        $t('client', 5, 'Bonjour, je suis Julien Morel, le gérant du Café des Arts. On aimerait un site avec la commande en ligne.'),
        $t('agent', 13, 'Avec plaisir. Vous avez un budget en tête ?'),
        $t('client', 17, 'Environ 3 000 €. C’est urgent, on voudrait être prêts pour les fêtes.'),
        $t('agent', 24, 'C’est noté. Quelle est votre adresse e-mail ?'),
        $t('client', 28, 'C’est julien.morel@cafedesarts.fr, et mon portable le 06 33 44 55 66.'),
        $t('agent', 36, 'Merci. On se retrouve jeudi de la semaine prochaine à 11h en visio avec notre conseillère ?'),
        $t('client', 44, 'Parfait. Vous pouvez aussi m’envoyer une proposition d’ici vendredi ?'),
        $t('agent', 51, 'C’est noté, une proposition vous sera envoyée d’ici vendredi. Bonne journée !'),
    ]]));
AgentVocalAppel::create(array_merge($base, ['telephone' => '+33645218790', 'duree_secondes' => 31, 'resultat' => 'a_rappeler', 'created_at' => now()->subHours(3),
    'resume_ia' => 'Hugo demande à décaler son rendez-vous.',
    'transcript_json' => [
        $t('agent', 0, 'Bonjour Hugo, que puis-je faire pour vous ?'),
        $t('client', 4, 'Je dois décaler notre rendez-vous de demain, il faut me rappeler pour trouver un autre créneau.'),
        $t('agent', 12, 'C’est noté, un conseiller vous rappelle dans la journée.'),
    ]]));
AgentVocalAppel::create(array_merge($base, ['telephone' => '+33698765432', 'duree_secondes' => 6, 'statut' => 'injoignable', 'created_at' => now()->subHours(5)]));
foreach (AgentVocalAppel::where('company_id', $cid)->orderBy('id')->get() as $i => $a) {
    $a->forceFill(['created_at' => now()->subHours([1, 3, 5][$i] ?? 6)->subMinutes(12 * $i)])->save();
}
echo "CRM86 prêt\n";
