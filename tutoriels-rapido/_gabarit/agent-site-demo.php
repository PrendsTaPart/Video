<?php
// Données fictives pour CRM73 (agent IA du site). Copie de tournage uniquement. Rejouable.
// Base de connaissances réindexée, question fréquente « horaires » retirée (elle est ajoutée pendant le tutoriel), simulations effacées.
use App\Models\AgentSite;
use App\Models\Connaissance;
use App\Models\Conversation;
use Illuminate\Support\Facades\DB;

$a = AgentSite::where('company_id', 1)->orderBy('id')->firstOrFail();
Connaissance::where('company_id', 1)->where('source', 'faq')->delete();
Conversation::where('agent_site_id', $a->id)->where('canal', 'simulation')->get()->each(function ($c) {
    DB::table('conversation_messages')->where('conversation_id', $c->id)->delete();
    $c->delete();
});
$s = app(\App\Services\ConnaissanceService::class)->indexer(1);
echo "Agent {$a->id} prêt ({$s['ajoutes']} ajout(s))\n";
