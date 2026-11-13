<?php
// Workflows FICTIFS pour filmer CRM23 (copie de tournage /home/user/rapido-crm-film, jamais le dépôt).
// À lancer depuis la copie : php artisan tinker --execute="require '<ce fichier>';"
use App\Models\Workflow;
use App\Services\WorkflowService;
Workflow::where('company_id', 1)->get()->each->delete();
$svc = app(WorkflowService::class);
foreach ([[1, 'Bienvenue nouveaux clients', 'actif'], [10, 'Relance factures impayées', 'actif'], [5, 'Offre de fin d\'année', 'inactif']] as [$modele, $nom, $statut]) {
    $w = $svc->creerDepuisModele(1, 1, $modele, $nom);
    $w->update(['statut' => $statut]);
}
echo "Workflows de démo prêts\n";
