#!/bin/bash
# RH33 (répondre dans la messagerie) : Camille pose à Hugo une demande d'information fictive dans #marketing, liée à une tâche.
cd /home/user/rapido-RH && php artisan tinker --execute='
$cam = App\Models\User::where("email","camille@studio-demo.test")->first();
$hugo = App\Models\User::where("email","hugo@studio-demo.test")->first();
$c = App\Models\Conversation::where("company_id",$cam->company_id)->where("title","marketing")->first();
$t = App\Models\Task::whereIn("project_id", App\Models\Project::where("company_id",$cam->company_id)->select("id"))->where("title","Photos des produits phares")->first();
app(App\Services\Messaging\MessagingService::class)->requestInformation($cam, $c, $hugo, "Les photos des produits phares sont-elles prêtes pour la boutique ?", $t?->id, null, "rh33-".time());
echo "ok demande RH33\n";' 2>&1 | tail -1
