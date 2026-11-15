<?php
// Entreprise de démonstration RapidoRH (données FICTIVES) pour filmer les tutoriels : Studio Démo (fictif).
// Usage : php demo-rh.php (depuis n'importe où ; base PostgreSQL de rapido-RH en local). Mot de passe de tous les comptes : Demo-Tuto-2026!
require '/home/user/rapido-RH/vendor/autoload.php';
$app = require '/home/user/rapido-RH/bootstrap/app.php';
$app->make(Illuminate\Contracts\Console\Kernel::class)->bootstrap();
config(['broadcasting.default' => 'null', 'features.messaging' => true, 'features.forum' => true, 'features.marketplace' => true, 'features.orchestration' => true]);
use App\Models\{Company, User, Role, Department, AgentConfig, CompanyAiSetting, Project, TaskList, Task, AgentExecution, AgentApproval, Permission, Daily, DailyTask, LeaveRequest, Appointment};
use Illuminate\Support\Str;
use Illuminate\Support\Facades\DB;

if (User::where('email', 'camille@studio-demo.test')->exists()) { echo "déjà\n"; exit; }
$c = Company::factory()->onTrial()->create(['name' => 'Studio Démo (fictif)']);
$owner = User::factory()->owner()->create(['company_id' => $c->id, 'email' => 'camille@studio-demo.test', 'first_name' => 'Camille', 'last_name' => 'Durand', 'password' => bcrypt('Demo-Tuto-2026!')]);
$c->forceFill(['owner_id' => $owner->id])->save();
$role = Role::create(['name' => 'Équipe', 'company_id' => $c->id]);
$dep = Department::create(['name' => 'Marketing', 'company_id' => $c->id]);
// Rôle « Collaborateur » aux droits limités (parcours employé) : projets, tâches, dailies, congés, rendez-vous.
$collab = Role::create(['name' => 'Collaborateur', 'company_id' => $c->id]);
$collab->permissions()->sync(Permission::whereIn('name', ['voir_liste_projets', 'voir_liste_taches', 'ajouter_tache', 'modifier_tache', 'voir_liste_conges', 'ajouter_conge', 'voir_liste_rendez_vous', 'ajouter_rendez_vous', 'voir_liste_documents', 'voir_liste_liens'])->pluck('id'));
$dev = Department::create(['name' => 'Développement', 'company_id' => $c->id]);
Department::create(['name' => 'Ressources humaines', 'company_id' => $c->id]);
$people = [];
foreach ([['Hugo', 'Martin', $collab, $dep], ['Inès', 'Bernard', $role, $dep], ['Lucas', 'Petit', $collab, $dev]] as [$f, $l, $r, $d]) {
    $people[$f] = User::factory()->create(['company_id' => $c->id, 'first_name' => $f, 'last_name' => $l, 'role_id' => $r->id, 'department_id' => $d->id,
        'email' => strtolower(Str::ascii($f)).'@studio-demo.test', 'password' => bcrypt('Demo-Tuto-2026!'), 'phone' => null, 'leave_days' => 25]);
}
app(App\Services\Marketplace\CatalogImporter::class)->import();
app(App\Services\Agents\CatalogImporter::class)->import(json_decode(file_get_contents(base_path('docs/rapidorh-v2/100_EMPLOYES_IA.json')), true));
app(App\Services\Agents\AgentProvisioner::class)->provision($c, $owner, onlySlugs: ['chef-projet', 'planificateur-editorial', 'qualite', 'rapporteur', 'coordinateur']);
// Clé fictive (jamais utilisée pour un vrai appel pendant le tournage) : nécessaire à l'essai à blanc des routines.
CompanyAiSetting::create(['company_id' => $c->id, 'api_key' => 'sk-ant-demo-'.Str::random(32), 'api_key_last4' => 'demo', 'model' => 'claude-opus-5-5']);

// Livrable en attente de validation (tutoriel 2).
$agent = User::where('company_id', $c->id)->where('first_name', 'like', 'Planificat%')->first() ?? User::where('company_id', $c->id)->whereIn('member_type', User::AI_MEMBER_TYPES)->first();
$p = Project::create(['name' => 'Salon Food & Tech 2027', 'description' => 'Préparer la présence au salon', 'start_date' => now(), 'end_date' => now()->addMonths(2), 'company_id' => $c->id, 'project_manager_id' => $owner->id]);
// Colonnes : celles créées par défaut avec le projet, renommées en français comme le ferait l'utilisateur.
$colonnes = function (Project $pr): array {
    $out = [];
    foreach ($pr->taskLists()->orderBy('order')->get() as $i => $l) { $l->update(['name' => ['À faire', 'En cours', 'Terminé'][$i] ?? $l->name]); $out[] = $l; }
    return $out;
};
$list = $colonnes($p)[0];
DB::table('project_user')->insert(['project_id' => $p->id, 'user_id' => $people['Hugo']->id, 'created_at' => now(), 'updated_at' => now()]);
$t = Task::create(['title' => 'Calendrier LinkedIn du salon', 'due_date' => now()->addWeek(), 'assigned_to' => $agent->id, 'tasklist_id' => $list->id, 'project_id' => $p->id]);
$text = "Calendrier LinkedIn — 4 semaines avant le salon\n\nSemaine 1 : annonce de notre présence (carrousel « 3 raisons de passer nous voir »)\nSemaine 2 : coulisses de la préparation du stand (vidéo courte)\nSemaine 3 : témoignage d'un client (citation + photo)\nSemaine 4 : rappel du stand B12 et prise de rendez-vous\n\nÀ valider : ton, fréquence (1 post par semaine), visuels à fournir par Hugo.";
$t->forceFill(['task_type' => 'semi_automated', 'ai_status' => 'awaiting_validation', 'ai_result' => $text, 'requires_validation' => true])->save();
$ex = AgentExecution::create(['correlation_id' => (string) Str::uuid(), 'idempotency_key' => 'demo-'.Str::random(8), 'company_id' => $c->id, 'agent_user_id' => $agent->id, 'task_id' => $t->id, 'project_id' => $p->id, 'attempt' => 1, 'status' => 'succeeded', 'result_summary' => $text, 'input_tokens' => 2100, 'output_tokens' => 640,
    'model' => 'claude-opus-5-5', 'cost_estimate' => 0.0212]); // 2 100 × 4 $ + 640 × 20 $ par million de tokens
// Daily IA, comme AgentRunner l'écrit après chaque exécution (un par exécution).
DB::table('dailies')->insertOrIgnore([['user_id' => $agent->id, 'date' => now()->toDateString(), 'source' => Daily::SOURCE_AI, 'execution_id' => $ex->id,
    'summary' => mb_substr("Tâche « {$t->title} » : livrable proposé, en attente de validation.\n\n".$text, 0, 2000), 'created_at' => now(), 'updated_at' => now()]]);
AgentApproval::create(['company_id' => $c->id, 'execution_id' => $ex->id, 'task_id' => $t->id, 'payload_hash' => AgentApproval::hashFor($text, $ex->id), 'status' => 'pending', 'expires_at' => now()->addDays(2)]);

// Projet humain avec Kanban, dailies, congés et rendez-vous (tutoriels RH01–RH19 et parcours employé).
$web = Project::create(['name' => 'Boutique en ligne', 'description' => 'Lancer la boutique en ligne du studio avant les fêtes.', 'start_date' => now()->subWeeks(2), 'end_date' => now()->addMonth(), 'company_id' => $c->id, 'project_manager_id' => $owner->id]);
foreach ([$people['Hugo'], $people['Lucas'], $people['Inès']] as $u) { DB::table('project_user')->insert(['project_id' => $web->id, 'user_id' => $u->id, 'created_at' => now(), 'updated_at' => now()]); }
$cols = [];
$cols = $colonnes($web);
$taches = [];
foreach ([['Rédiger les fiches produits', 0, 'Hugo', 1], ['Photos des produits phares', 0, 'Inès', 2], ['Intégrer le paiement en ligne', 1, 'Lucas', 0], ['Maquette de la page d\'accueil', 1, 'Hugo', 1], ['Choisir l\'hébergeur', 2, 'Lucas', 2], ['Charte graphique de la boutique', 2, 'Inès', 1]] as [$t, $col, $who, $prio]) {
    $taches[$t] = Task::create(['title' => $t, 'description' => 'Tâche de démonstration (données fictives).', 'due_date' => now()->addDays(3 + count($taches) * 2)->toDateString(), 'status' => $col, 'priority' => $prio,
        'assigned_to' => $people[$who]->id, 'tasklist_id' => $cols[$col]->id, 'project_id' => $web->id]);
    $taches[$t]->assignedUsers()->attach($people[$who]->id);
}
// Tâches terminées les semaines précédentes : historique de la progression hebdomadaire et du top 5.
foreach ([['Benchmark des concurrents', 'Inès', 3], ['Nom de domaine réservé', 'Lucas', 2], ['Liste des produits phares', 'Hugo', 1], ['Arborescence du site', 'Hugo', 1], ['Choix des moyens de paiement', 'Lucas', 2]] as [$t, $who, $weeks]) {
    $old = Task::create(['title' => $t, 'description' => 'Tâche de démonstration (données fictives).', 'due_date' => now()->subWeeks($weeks)->toDateString(), 'status' => 2, 'priority' => 1,
        'assigned_to' => $people[$who]->id, 'tasklist_id' => $cols[2]->id, 'project_id' => $web->id]);
    $old->assignedUsers()->attach($people[$who]->id);
    DB::table('tasks')->where('id', $old->id)->update(['created_at' => now()->subWeeks($weeks + 1), 'updated_at' => now()->subWeeks($weeks)->startOfWeek()->addDays(2)]);
}
foreach ([['Hugo', 'Rédiger les fiches produits', 3, 'Rédaction des 6 premières fiches'], ['Lucas', 'Intégrer le paiement en ligne', 5, 'Tests du paiement en mode bac à sable']] as [$who, $t, $h, $d]) {
    foreach ([1, 2] as $j) {
        $dl = Daily::create(['user_id' => $people[$who]->id, 'date' => now()->subDays($j)->toDateString()]);
        DailyTask::create(['daily_id' => $dl->id, 'task_id' => $taches[$t]->id, 'hours' => $h, 'description' => $d]);
    }
}
LeaveRequest::create(['user_id' => $people['Lucas']->id, 'type' => 0, 'reason' => 'Congés de fin d\'année', 'start_date' => now()->addWeeks(5)->toDateString(), 'end_date' => now()->addWeeks(6)->toDateString(), 'days_taken' => 5, 'status' => LeaveRequest::STATUS_PENDING]);
LeaveRequest::create(['user_id' => $people['Inès']->id, 'type' => 0, 'reason' => 'Pont de la Toussaint', 'start_date' => now()->subWeeks(3)->toDateString(), 'end_date' => now()->subWeeks(3)->addDay()->toDateString(), 'days_taken' => 2, 'status' => LeaveRequest::STATUS_APPROVED, 'approved_by' => $owner->id, 'decision_date' => now()->subWeeks(4)]);
$rdv = Appointment::create(['title' => 'Point boutique en ligne', 'description' => 'Avancement hebdomadaire (démonstration).', 'type' => 0, 'start_date' => now()->addDays(2)->setTime(10, 0), 'end_date' => now()->addDays(2)->setTime(10, 45), 'organizer_id' => $owner->id, 'meeting_url' => 'https://visio.studio-demo.test/point-boutique']);
foreach ([$people['Hugo'], $people['Lucas']] as $u) { DB::table('appointment_participants')->insert(['appointment_id' => $rdv->id, 'user_id' => $u->id, 'created_at' => now(), 'updated_at' => now()]); }

// Messagerie (tutoriels 4 et 5).
$svc = app(App\Services\Messaging\MessagingService::class);
$ch = $svc->create($owner, 'channel', [$people['Hugo']->id, $people['Inès']->id, $people['Lucas']->id, $agent->id], 'marketing', visibility: 'public', topic: 'Campagnes et contenus du salon Food & Tech');
$svc->post($people['Inès'], $ch, "Bonjour à tous ! Le salon approche : on fait le point sur la communication cette semaine.", 'seed-1');
$svc->post($people['Hugo'], $ch, "Les visuels du stand sont prêts, je les dépose ici demain matin.", 'seed-2');
$svc->create($owner, 'channel', [$people['Lucas']->id], 'evenements', visibility: 'public', topic: 'Salons et rendez-vous clients');
$svc->create($owner, 'direct', [$people['Inès']->id]);

// Routine proposée par le modèle du projet (tutoriel routines) : créée désactivée, sans budget.
app(App\Services\Routines\RoutineService::class)->proposeFromPlan($p, ['routine_proposals' => [[
    'id' => 'suivi-blocages', 'template' => 'demo', 'agent_id' => 'rrh-coordinateur', 'name' => 'Suivi quotidien des blocages',
    'goal' => 'Repérer chaque matin les tâches bloquées du salon et proposer une relance à leur responsable.',
    'steps' => ['Lister les tâches en retard ou bloquées', 'Proposer une relance par responsable', 'Résumer dans le canal #marketing'],
    'trigger' => 'weekdays_09_00', 'limits' => ['max_runs_per_day' => 1],
]]], $owner);

// Forum (tutoriel 6).
$forum = app(App\Services\Forum\ForumService::class);
$forum->ensureCategories($c->id);
echo "ok company={$c->id} agent={$agent->first_name}\n";
