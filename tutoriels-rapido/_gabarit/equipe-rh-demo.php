<?php

// Données de démonstration FICTIVES : connexion RapidoRH, règles « équipe », employés IA, livrables — copie de tournage seulement.
// Aucun appel réseau : la connexion est marquée « connecté » sans jeton réel (aucun envoi possible).
// Usage : cd /home/user/rapido-crm-film && php artisan tinker --execute="require '/home/user/video/tutoriels-rapido/_gabarit/equipe-rh-demo.php';"

use App\Models\ConnexionMcp;
use App\Models\EquipeEnvoi;
use App\Models\RegleEquipe;
use Illuminate\Support\Facades\DB;

$societe = 1;   // Studio Lumière (compte demo@rapido.test)
DB::table('connexion_journal')->where('company_id', $societe)->delete();
EquipeEnvoi::where('company_id', $societe)->delete();
RegleEquipe::where('company_id', $societe)->delete();
DB::table('equipe_employes_rh')->where('company_id', $societe)->delete();
ConnexionMcp::where('company_id', $societe)->where('application', 'rapidorh')->delete();

$c = ConnexionMcp::create(['company_id' => $societe, 'application' => 'rapidorh', 'nom' => 'RapidoRH', 'url_serveur' => 'https://rh.exemple.test/mcp',
    'etat' => 'connecte', 'connecte_par' => 1, 'connecte_le' => now()->subDays(6),
    'outils' => [['nom' => 'create-task-tool', 'description' => 'Créer une tâche'], ['nom' => 'send-email-tool', 'description' => 'Envoyer un e-mail'],
        ['nom' => 'send-whatsapp-tool', 'description' => 'Envoyer un message WhatsApp'], ['nom' => 'crm-event-tool', 'description' => 'Confier un événement du CRM à l’équipe'],
        ['nom' => 'get-ai-agents-list-tool', 'description' => 'Lister les employés IA']]]);

$employes = [[901, 'Iris — Assistante commerciale', 'Ventes'], [902, 'Hugo — Chargé de devis', 'Ventes'], [903, 'Nina — Support client', 'Service client']];
foreach ($employes as [$id, $nom, $pole]) {
    DB::table('equipe_employes_rh')->insert(['company_id' => $societe, 'rh_id' => $id, 'nom' => $nom, 'pole' => $pole, 'statut' => 'active',
        'vu_le' => now()->subHour(), 'created_at' => now(), 'updated_at' => now()]);
}

$regles = [
    ['devis_signe', 'playbook', 'Devis signé : lancer la production et l’accueil du client', 14],
    ['formulaire', 'tache', 'Qualifier le lead {nom} et le rappeler sous 24 h', 23],
    ['ticket_urgent', 'playbook', 'Traiter la demande urgente de {entreprise}', 4],
    ['conversation_escaladee', 'playbook', 'Reprendre la conversation de {nom} sur le site', 7],
];
$ids = [];
foreach ($regles as [$evt, $action, $titre, $n]) {
    $ids[$evt] = RegleEquipe::create(['company_id' => $societe, 'connexion_id' => $c->id, 'evenement' => $evt, 'action' => $action,
        'parametres' => ['priority' => 'high'], 'modele_titre' => $titre, 'actif' => true, 'declenchements' => $n, 'dernier_le' => now()->subHours(2)])->id;
}

$emp = fn ($i) => ['id' => $employes[$i][0], 'nom' => $employes[$i][1], 'type' => 'ia'];
$envois = [
    ['devis_signe', 'fait', 0, "Message d'accueil prêt : remerciements, prochaines étapes, rendez-vous de lancement proposé mardi 10 h.", 'accepte', 5],
    ['formulaire', 'fait', 0, 'Lead qualifié : besoin de 12 portraits d’équipe, budget indiqué, rappel prévu demain 9 h 30.', 'accepte', 3],
    ['formulaire', 'fait', 1, 'Brouillon de devis : shooting entreprise demi-journée + retouches, à relire avant envoi.', 'a_revoir', 2],
    ['ticket_urgent', 'fait', 2, 'Réponse proposée au client : lien de téléchargement des photos renvoyé, accès vérifié.', 'accepte', 1],
    ['conversation_escaladee', 'en_cours', 2, null, null, 0],
];
foreach ($envois as $i => [$evt, $statut, $e, $livrable, $avis, $jours]) {
    $env = EquipeEnvoi::create(['company_id' => $societe, 'regle_id' => $ids[$evt], 'cle' => "demo-$i", 'evenement' => $evt, 'outil' => 'crm-event-tool',
        'statut' => 'ok', 'retour_statut' => $statut, 'retour_le' => now()->subDays($jours)->addMinutes(40), 'livrable' => $livrable,
        'employe_rh' => $emp($e), 'livrable_avis' => $avis, 'livrable_avis_par' => $avis ? 1 : null, 'livrable_avis_le' => $avis ? now()->subDays($jours)->addHour() : null]);
    $env->forceFill(['created_at' => now()->subDays($jours), 'updated_at' => now()->subDays($jours)])->save();
    DB::table('connexion_journal')->insert(['company_id' => $societe, 'connexion_id' => $c->id, 'regle_id' => $ids[$evt], 'evenement' => $evt,
        'outil' => 'crm-event-tool', 'statut' => 'ok', 'detail' => $livrable ? 'Compte rendu reçu de RapidoRH' : 'Tâches confiées à l’équipe', 'created_at' => now()->subDays($jours)]);
}
echo 'Règles : '.RegleEquipe::where('company_id', $societe)->count().', envois : '.EquipeEnvoi::where('company_id', $societe)->count().PHP_EOL;
