<?php
// Données fictives pour CRM74 (boîte de réception et tickets). Copie de tournage uniquement. Rejouable.
use App\Models\Ticket;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\URL;

$cid = 1;
// Tickets créés par les essais et les tournages précédents
$ids = Ticket::where('company_id', $cid)->where('id', '>', 20)->pluck('id');
DB::table('ticket_messages')->whereIn('ticket_id', $ids)->delete();
Ticket::whereIn('id', $ids)->delete();
// SMS et e-mail reçus : à traiter, sans réponse
DB::table('messages_entrants')->where('company_id', $cid)->update(['ticket_id' => null, 'traite_le' => null, 'traite_par' => null,
    'reponse' => null, 'repondu_le' => null, 'repondu_par' => null, 'reponse_statut' => null]);
// Messages réalistes au lieu de « Message fictif de démonstration. »
$textes = [1 => 'Bonjour, je ne trouve pas la facture de septembre dans mon espace client. Pouvez-vous me la renvoyer ? Merci, Camille',
    2 => 'Bonjour, pouvons-nous décaler la livraison du 22 au 24 novembre ? Le traiteur ne sera pas prêt avant.',
    3 => 'Bonjour, l’offre de printemps est-elle valable pour une association ? Nous sommes une petite structure.'];
foreach ($textes as $id => $t) {
    DB::table('ticket_messages')->where('ticket_id', $id)->where('auteur', 'client')->update(['contenu' => $t]);
    DB::table('ticket_messages')->where('ticket_id', $id)->where('auteur', '!=', 'client')->delete();
    Ticket::where('id', $id)->update(['statut' => 'nouveau', 'premiere_reponse_le' => null, 'resolu_le' => null, 'csat_note' => null, 'csat_jeton' => null,
        'csat_le' => null, 'nps' => null, 'sla_depasse' => false, 'assigne_a' => null]);
}
// T-00001 urgent, ouvert il y a 3 heures : en retard
Ticket::where('id', 1)->update(['priorite' => 'haute', 'created_at' => now()->subHours(3), 'echeance_premiere_reponse' => now()->subHour(), 'echeance_resolution' => now()->addHours(5)]);
// T-00004 (Hélène Lafitte) résolu : lien d'avis pour la démonstration
$t = Ticket::findOrFail(19);
$jeton = \Illuminate\Support\Str::random(48);
$t->update(['statut' => 'resolu', 'resolu_le' => now()->subMinutes(20), 'csat_jeton' => hash('sha256', $jeton), 'csat_note' => null, 'csat_le' => null, 'nps' => null]);
URL::forceRootUrl('http://127.0.0.1:8124');
file_put_contents('/home/user/video/tutoriels-rapido/CRM74/lien-avis.txt', route('ticket.csat', $jeton));
echo "Tickets prêts\n";
