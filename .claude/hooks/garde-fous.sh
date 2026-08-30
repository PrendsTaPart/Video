#!/usr/bin/env bash
# Les trois gestes qu'un agent ne fait pas sans un humain.
#
# La bible FoodEatUp (IV.7) les nomme : envoyer, dépenser, détruire. Ils ont un
# point commun — aucun ne se rattrape. Un brouillon mal écrit se réécrit ; un
# message parti est parti, une dépense est engagée, une ligne supprimée n'est
# plus là.
#
# Le filtre `matcher` de settings.json présélectionne largement ; c'est ici que
# la décision se prend, sur le nom exact. Un outil que le matcher attrape sans
# qu'il soit dans une des trois familles passe : mieux vaut laisser filer un
# candidat que bloquer du travail légitime en silence.
#
# Sortie : le contrat des hooks PreToolUse — permissionDecision allow|deny.
set -euo pipefail

outil="$(jq -r '.tool_name // ""')"

refuser() {
  jq -cn --arg r "$1" '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: $r
    }
  }'
  exit 0
}

case "$outil" in
  # ENVOYER — un message parti ne se rappelle pas. On prépare, un humain envoie.
  *__send_message|*__send_email|*__send_sms|*__send_newsletter \
  |*__schedule_email|*__schedule_sms|*__lancer_campagne|*__launch_campaign \
  |*__reply|*__forward|*appeler_entreprise_vocal|*prospecter_et_appeler_vocal)
    refuser "Envoi direct refusé : cet agent prépare des brouillons, un humain envoie. Créez le brouillon (create_draft_tool, create_draft, draft_newsletter) et signalez-le." ;;

  # DÉPENSER — une dépense engagée ne s'annule pas d'un appel.
  *__buy_*|*__stripe_api_write|*__ads_activate_entity|*__create_payment_link)
    refuser "Dépense refusée : engager de l'argent est un geste humain. Chiffrez et proposez, ne payez pas." ;;

  # DÉTRUIRE — sans exception, y compris pour « nettoyer ».
  #
  # Les jokers s'arrêtent là où le mot cesse de vouloir dire détruire :
  # `remove_*` aurait attrapé `remove_background`, qui est de la retouche
  # d'image, et `cancel_*` aurait attrapé `cancel_job`, qui annule un rendu.
  # Les vrais retraits sont donc nommés un par un — une liste qu'on relit vaut
  # mieux qu'un motif qui bloque le travail au hasard.
  *__execute_sql|*__apply_migration|*__delete_*|*__*_delete|*__destroy_*|*__trash_* \
  |*__unpublish_*|*__depublier_*|*__revoke_* \
  |*__remove_asset|*__remove_post_campagne|*__remove_sequence_etape|*__remove_beverage_item \
  |*__retirer_plan|*__cancel_reservation|*__cancel_event|*__cancel_schedules_post \
  |*__liberer_episode|*__unpublish_lead_magnet|*__depublier_le_lot_du_jour)
    refuser "Destruction refusée, sans exception. Si quelque chose doit sortir, dites-le et arrêtez-vous : c'est une décision humaine." ;;
esac

# Hors des trois familles : rien à dire, le tour suit son cours.
exit 0
