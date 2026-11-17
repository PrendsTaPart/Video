<?php
// Données fictives pour CRM70 / CRM71 (Téléphonie). Copie de tournage uniquement : compte Twilio factice (mode simulé),
// numéro de l'utilisatrice, téléphones des contacts et un historique d'appels varié. Rejouable.
use App\Models\AgentVocalTwilioCredentials;
use App\Models\Appel;
use App\Models\Contact;
use App\Models\User;

$u = User::where('email', 'demo@rapido.test')->firstOrFail();
$cid = $u->company_id;
$u->forceFill(['telephone' => '06 11 22 33 44'])->save();
AgentVocalTwilioCredentials::updateOrCreate(['company_id' => $cid], ['twilio_account_sid' => 'ACdemo0000000000000000000000000000', 'twilio_auth_token' => 'jeton-demo',
    'twilio_phone_number' => '+33186950000', 'statut' => 'actif']);
$tels = ['07 12 34 56 78', '06 45 21 87 90', '06 98 76 54 32', '07 66 12 40 18', '06 23 45 67 89', '07 81 92 03 14'];
$contacts = Contact::where('company_id', $cid)->orderBy('id')->limit(6)->get();
foreach ($contacts as $i => $c) {
    $c->forceFill(['telephone' => $tels[$i]])->save();
}
Appel::where('company_id', $cid)->delete();
$hist = [
    [0, 'termine', 'joint', 312, 'A validé le devis de printemps, envoyer le contrat lundi.', 1],
    [1, 'sans_reponse', null, 0, null, 1],
    [2, 'termine', 'rdv', 184, 'Rendez-vous pris jeudi 10 h pour la démonstration.', 2],
    [3, 'termine', 'rappeler', 96, 'Rappeler après le 20 : budget en cours de validation.', 3],
    [4, 'occupe', null, 0, null, 4],
    [5, 'termine', 'messagerie', 22, 'Message laissé sur la messagerie.', 5],
];
foreach ($hist as [$i, $statut, $resultat, $duree, $notes, $jours]) {
    $c = $contacts[$i] ?? null;
    if (! $c) {
        continue;
    }
    $debut = now()->subDays($jours)->setTime(9 + $i, 15);
    Appel::create(['company_id' => $cid, 'user_id' => $u->id, 'direction' => 'sortant', 'de' => '+33186950000', 'vers' => '+33'.substr(preg_replace('/\D/', '', $c->telephone), 1),
        'contact_id' => $c->id, 'entreprise_id' => $c->entreprise_id, 'statut' => $statut, 'duree_secondes' => $duree, 'resultat' => $resultat, 'notes' => $notes,
        'debut_le' => $debut, 'fin_le' => $debut->copy()->addSeconds($duree)])->forceFill(['created_at' => $debut])->save();
}
echo 'Téléphonie : '.Appel::where('company_id', $cid)->count()." appels de démonstration\n";
