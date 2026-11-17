<?php
// Données fictives pour CRM81 (portail client). Copie de tournage uniquement. Rejouable.
// Contact Hélène Lafitte (client Maison Lafitte) : devis en attente, facture à régler, demande avec réponse de l'équipe,
// rendez-vous à venir en visio, contrat envoyé. Écrit le lien magique signé dans CRM81/lien-portail.txt.
use App\Models\Contact;
use App\Models\Devis;
use App\Models\Facture;
use App\Models\RendezVous;
use App\Models\Ticket;
use App\Models\User;
use Illuminate\Support\Facades\DB;

$u = User::where('email', 'demo@rapido.test')->firstOrFail();
$cid = $u->company_id;
$client = 1; // Maison Lafitte
$h = Contact::firstOrNew(['company_id' => $cid, 'email' => 'helene@maisonlafitte.test']);
$h->fill(['prenom' => 'Hélène', 'nom' => 'Lafitte', 'entreprise_id' => $client, 'telephone' => '+33600000081'])->save();

// Devis en attente et facture à régler (en plus du devis accepté et de la facture payée n° 1)
$base = ['company_id' => $cid, 'user_id' => $u->id, 'entreprise_id' => $client, 'destinataire' => 'contact@maisonlafitte.test', 'remise' => 0, 'delai_paiement' => 30];
Devis::where('company_id', $cid)->where('entreprise_id', $client)->where('id', '>', 1)->delete();
Facture::where('company_id', $cid)->where('entreprise_id', $client)->where('id', '>', 7)->delete();
Devis::create($base + ['statut' => 0, 'total_ht' => 980, 'total_tva' => 196, 'total_ttc' => 1176]);
Facture::create($base + ['statut' => 0, 'total_ht' => 450, 'total_tva' => 90, 'total_ttc' => 540]);

// Demande ouverte avec une réponse de l'équipe
$ids = Ticket::where('company_id', $cid)->where('contact_id', $h->id)->pluck('id');
DB::table('ticket_messages')->whereIn('ticket_id', $ids)->delete();
Ticket::whereIn('id', $ids)->delete();
$ts = app(\App\Services\TicketService::class);
$t = $ts->creer($cid, null, ['sujet' => 'Ajouter une page « Carte des vins »', 'description' => 'Bonjour, pouvez-vous ajouter une page pour notre carte des vins sur le site ?', 'priorite' => 'normale', 'contact_id' => $h->id]);
$ts->repondre($t, $u, 'Bonjour Hélène, c’est noté : la page sera en ligne jeudi. Nous vous enverrons un aperçu avant.');

RendezVous::where('entreprise_id', $client)->where('titre', 'like', '%Lotus%')->update(['titre' => 'Présentation du nouveau site']);
// Rendez-vous à venir en visio
RendezVous::where('entreprise_id', $client)->where('titre', 'Point site et photos')->delete();
RendezVous::create(['type' => 'visio', 'mode_envoi' => 'email', 'user_id' => $u->id, 'entreprise_id' => $client, 'titre' => 'Point site et photos',
    'date_debut' => now()->addDays(4)->setTime(10, 0), 'date_fin' => now()->addDays(4)->setTime(10, 30), 'meet_url' => 'https://whereby.com/studio-lumiere-demo']);

// Contrat de maintenance envoyé pour signature
config(['mail.default' => 'array']);
$cs = app(\App\Services\ContratService::class);
\App\Models\ContratUserCrm::where('company_id', $cid)->where('entreprise_id', $client)->get()->each(function ($k) {
    DB::table('contrat_evenements')->where('contrat_user_id', $k->id)->delete();
    $k->delete();
});
$k = $cs->creer($u, ['entreprise_id' => $client, 'titre' => 'Maintenance du site 2027', 'contenu' => '<h2>Contrat de maintenance</h2><p>Mises à jour, sauvegardes et support du site de Maison Lafitte, 49 € HT par mois.</p>',
    'destinataire' => 'helene@maisonlafitte.test', 'montant' => 588, 'debut' => now()->addMonth()->startOfMonth()->toDateString(), 'fin' => now()->addMonth()->startOfMonth()->addYear()->subDay()->toDateString()]);
$cs->envoyer($k, $u);

\Illuminate\Support\Facades\URL::forceRootUrl('http://127.0.0.1:8124');
file_put_contents('/home/user/video/tutoriels-rapido/CRM81/lien-portail.txt', app(\App\Services\PortailClientService::class)->lien($h));
echo "Portail prêt pour {$h->prenom} {$h->nom} (contact {$h->id})\n";
