<?php
// Données fictives pour les captures du site RapidoSoftware (blog, agent du site, tickets, boîte de réception). Copie de tournage seulement. Rejouable.
use App\Models\User;
use Illuminate\Support\Facades\DB;

$u = User::where('email', 'demo@rapido.test')->firstOrFail();
$cid = $u->company_id;
$site = \App\Models\Site::where('company_id', $cid)->first();
if ($site && ! DB::table('articles')->where('company_id', $cid)->exists()) {
    $a = app(\App\Services\ArticleService::class);
    foreach ([
        ['Comment choisir son traiteur pour un séminaire', 'traiteur séminaire', '<h2>Les bonnes questions</h2><p>Un séminaire réussi commence par un repas réussi. Voici comment choisir votre traiteur pour un séminaire : budget, régimes, horaires et logistique.</p><h2>Le budget</h2><p>Comptez entre 25 et 60 € par personne selon la formule.</p>'],
        ['5 idées de menus d’automne pour vos clients', 'menus automne', '<h2>Des produits de saison</h2><p>Courge, champignons, châtaignes : nos menus d’automne plaisent à tous.</p>'],
    ] as [$titre, $mc, $html]) {
        $art = $a->enregistrer($cid, $u->id, ['site_id' => $site->id, 'titre' => $titre, 'mot_cle' => $mc, 'contenu' => $html, 'extrait' => 'Nos conseils pratiques.', 'categorie' => 'Conseils']);
        $art->forceFill(['statut' => 'publie', 'publie_le' => now()->subDays(3)])->save();
    }
}
if (! DB::table('agents_site')->where('company_id', $cid)->exists()) {
    app(\App\Services\AgentSiteService::class)->creerDepuisModele($cid, $u->id, 'accueil', 'Assistant du site');
}
if (! DB::table('tickets')->where('company_id', $cid)->exists()) {
    $t = app(\App\Services\TicketService::class);
    $contacts = \App\Models\Contact::where('company_id', $cid)->orderBy('id')->limit(3)->pluck('id');
    foreach ([['Facture introuvable dans mon espace', 'haute'], ['Changer la date de livraison', 'normale'], ['Question sur l’offre de printemps', 'basse']] as $i => [$sujet, $prio]) {
        $t->creer($cid, $u->id, ['sujet' => $sujet, 'description' => 'Message fictif de démonstration.', 'priorite' => $prio, 'contact_id' => $contacts[$i] ?? null]);
    }
}
if (! DB::table('messages_entrants')->where('company_id', $cid)->exists()) {
    $c = \App\Models\Contact::where('company_id', $cid)->orderBy('id')->first();
    DB::table('messages_entrants')->insert([
        ['company_id' => $cid, 'canal' => 'sms', 'de' => '+33712345678', 'contact_id' => $c?->id, 'contenu' => 'Bonjour, est-ce que vous livrez samedi matin ?', 'sujet' => null, 'created_at' => now()->subMinutes(25)],
        ['company_id' => $cid, 'canal' => 'email', 'de' => 'contact@maisonlafitte.test', 'contact_id' => $c?->id, 'contenu' => 'Pouvez-vous me renvoyer le devis de printemps ?', 'sujet' => 'Devis de printemps', 'created_at' => now()->subHours(2)],
    ]);
}
echo "captures prêtes\n";
