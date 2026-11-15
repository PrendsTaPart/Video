<?php
// Entreprise de démonstration (données FICTIVES) pour filmer les tutoriels RapidoRH V2.
require '/home/user/rapido-RH/vendor/autoload.php';
$app = require '/home/user/rapido-RH/bootstrap/app.php';
$app->make(Illuminate\Contracts\Console\Kernel::class)->bootstrap();
config(['broadcasting.default' => 'null', 'features.messaging' => true, 'features.forum' => true, 'features.marketplace' => true, 'features.orchestration' => true]);
use App\Models\{Company, User, Role, Department, AgentConfig, CompanyAiSetting, Project, TaskList, Task, AgentExecution, AgentApproval};
use Illuminate\Support\Str;

if (User::where('email', 'camille@studio-demo.test')->exists()) { echo "déjà\n"; exit; }
$c = Company::factory()->onTrial()->create(['name' => 'Studio Démo (fictif)']);
$owner = User::factory()->owner()->create(['company_id' => $c->id, 'email' => 'camille@studio-demo.test', 'first_name' => 'Camille', 'last_name' => 'Durand', 'password' => bcrypt('Demo-Tuto-2026!')]);
$c->forceFill(['owner_id' => $owner->id])->save();
$role = Role::create(['name' => 'Équipe', 'company_id' => $c->id]);
$dep = Department::create(['name' => 'Marketing', 'company_id' => $c->id]);
$people = [];
foreach ([['Hugo', 'Martin'], ['Inès', 'Bernard'], ['Lucas', 'Petit']] as [$f, $l]) {
    $people[$f] = User::factory()->create(['company_id' => $c->id, 'first_name' => $f, 'last_name' => $l, 'role_id' => $role->id, 'department_id' => $dep->id, 'email' => strtolower(Str::ascii($f)).'@studio-demo.test']);
}
app(App\Services\Marketplace\CatalogImporter::class)->import();
app(App\Services\Agents\CatalogImporter::class)->import(json_decode(file_get_contents(base_path('docs/rapidorh-v2/100_EMPLOYES_IA.json')), true));
app(App\Services\Agents\AgentProvisioner::class)->provision($c, $owner, onlySlugs: ['chef-projet', 'planificateur-editorial', 'qualite', 'rapporteur', 'coordinateur']);
// Clé fictive (jamais utilisée pour un vrai appel pendant le tournage) : nécessaire à l'essai à blanc des routines.
CompanyAiSetting::create(['company_id' => $c->id, 'api_key' => 'sk-ant-demo-'.Str::random(32), 'api_key_last4' => 'demo', 'model' => 'claude-opus-5-5']);

// Livrable en attente de validation (tutoriel 2).
$agent = User::where('company_id', $c->id)->where('first_name', 'like', 'Planificat%')->first() ?? User::where('company_id', $c->id)->whereIn('member_type', User::AI_MEMBER_TYPES)->first();
$p = Project::create(['name' => 'Salon Food & Tech 2027', 'description' => 'Préparer la présence au salon', 'start_date' => now(), 'end_date' => now()->addMonths(2), 'company_id' => $c->id, 'project_manager_id' => $owner->id]);
$list = TaskList::create(['name' => 'À faire', 'project_id' => $p->id]);
$t = Task::create(['title' => 'Calendrier LinkedIn du salon', 'due_date' => now()->addWeek(), 'assigned_to' => $agent->id, 'tasklist_id' => $list->id, 'project_id' => $p->id]);
$text = "Calendrier LinkedIn — 4 semaines avant le salon\n\nSemaine 1 : annonce de notre présence (carrousel « 3 raisons de passer nous voir »)\nSemaine 2 : coulisses de la préparation du stand (vidéo courte)\nSemaine 3 : témoignage d'un client (citation + photo)\nSemaine 4 : rappel du stand B12 et prise de rendez-vous\n\nÀ valider : ton, fréquence (1 post par semaine), visuels à fournir par Hugo.";
$t->forceFill(['task_type' => 'semi_automated', 'ai_status' => 'awaiting_validation', 'ai_result' => $text, 'requires_validation' => true])->save();
$ex = AgentExecution::create(['correlation_id' => (string) Str::uuid(), 'idempotency_key' => 'demo-'.Str::random(8), 'company_id' => $c->id, 'agent_user_id' => $agent->id, 'task_id' => $t->id, 'project_id' => $p->id, 'attempt' => 1, 'status' => 'succeeded', 'result_summary' => $text, 'input_tokens' => 2100, 'output_tokens' => 640]);
AgentApproval::create(['company_id' => $c->id, 'execution_id' => $ex->id, 'task_id' => $t->id, 'payload_hash' => AgentApproval::hashFor($text, $ex->id), 'status' => 'pending', 'expires_at' => now()->addDays(2)]);

// Messagerie (tutoriels 4 et 5).
$svc = app(App\Services\Messaging\MessagingService::class);
$ch = $svc->create($owner, 'channel', [$people['Hugo']->id, $people['Inès']->id, $people['Lucas']->id, $agent->id], 'marketing', visibility: 'public', topic: 'Campagnes et contenus du salon Food & Tech');
$svc->post($people['Inès'], $ch, "Bonjour à tous ! Le salon approche : on fait le point sur la communication cette semaine.", 'seed-1');
$svc->post($people['Hugo'], $ch, "Les visuels du stand sont prêts, je les dépose ici demain matin.", 'seed-2');
$svc->create($owner, 'channel', [$people['Lucas']->id], 'evenements', visibility: 'public', topic: 'Salons et rendez-vous clients');
$svc->create($owner, 'direct', [$people['Inès']->id]);

// Forum (tutoriel 6).
$forum = app(App\Services\Forum\ForumService::class);
$forum->ensureCategories($c->id);
echo "ok company={$c->id} agent={$agent->first_name}\n";
