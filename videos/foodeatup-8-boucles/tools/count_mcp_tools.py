#!/usr/bin/env python3
"""Compte les outils MCP FoodEatUp réellement exposés, boucle par boucle.

Pourquoi ce script existe : le brief annonçait 21/18/14/17/22/14/23/17 outils par
boucle et un total de 177. Ces deux chiffres sont incompatibles (la somme fait
146), et aucun des deux n'était vérifiable. La règle « aucun chiffre inventé »
impose donc de recompter sur la liste réelle du serveur, et d'afficher à l'écran
ce que ce script sort — pas ce que le brief supposait.

La liste `TOOLS` est celle exposée par le serveur MCP `Foodeatup` (relevée le
2026-08-07). Chaque outil est affecté à UNE boucle et une seule, pour que la
somme des huit compteurs soit exactement le total — un outil compté deux fois
gonflerait artificiellement les deux boucles concernées.
"""
import collections
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

# Ordre = ordre des boucles. Un outil tombe dans la PREMIÈRE boucle dont un
# préfixe/suffixe correspond ; les cas ambigus sont tranchés à la main dans
# OVERRIDES, jamais par hasard.
BOUCLES = [
    ("01", "configuration-boutique"),
    ("02", "equipe"),
    ("03", "stockvision"),
    ("04", "haccp"),
    ("05", "ecommerce"),
    ("06", "communication"),
    ("07", "fidelite"),
    ("08", "comptabilite"),
]

TOOLS = """
add_site_page add_temperature add_waitlist adjust_points adjust_stock
apply_site_template approve_leave assign_task cancel_reservation check_gift_card
checkin_reservation close_pos_session complete_haccp_tracabilite
confirm_reservation create_campaign create_category create_cleaning_zone
create_client create_dish create_dish_category create_employee
create_employee_contract create_equipment create_expense create_haccp_label
create_haccp_reception create_haccp_tracabilite create_hygiene_checklist
create_hygiene_checklist_validation create_ingredient create_invoice
create_job_offer create_notification create_order create_product
create_production_plan create_quote create_recipe create_reservation
create_shift create_supplier create_supplier_order create_table create_tva
create_whatsapp_template create_zone delete_category delete_client delete_dish
delete_employee delete_ingredient delete_product delete_recipe finance_summary
floor_plan_status get_campaign_stats get_client get_daily_brief
get_domain_status get_employee get_expense get_ingredient get_invoice
get_loyalty_account get_loyalty_program get_order get_page_content
get_pos_report get_pos_session get_product get_production_ingredients get_quote
get_recipe get_site_pages get_site_stats get_site_status get_station_load
get_supplier get_survey_results get_wheel_stats import_storefront_menu
launch_campaign list_attendances list_beverages list_campaigns list_categories
list_cleaning_actions list_cleaning_zones list_clients list_deliveries
list_delivery_zones list_dishes list_employee_contracts list_employee_documents
list_employees list_expenses list_gift_cards list_haccp_labels
list_haccp_reception list_haccp_temperatures list_haccp_tracabilite
list_happy_hours list_hygiene_checklists list_ingredients list_invoices
list_job_applications list_leaves list_low_stocks list_loyalty_rewards
list_notifications list_orders list_plannings list_pos_payments list_pos_tabs
list_private_event_requests list_production_alerts list_production_plans
list_products list_quotes list_recipes list_redemptions list_reservations
list_reviews list_rfm_segments list_site_leads list_site_templates list_stocks
list_suppliers list_surveys list_tables list_top_productions list_tva
list_units list_waitlist list_whatsapp_templates list_wheel_games list_zones
moderate_review no_show_reservation open_pos_session propose_campaigns
publish_site record_cleaning_action record_pos_payment reject_leave
remove_beverage_item reply_review reservation_availability search_entities
seat_waitlist set_site_theme submit_whatsapp_template toggle_site_page
update_application_status update_category update_client update_dish
update_employee update_employee_schedule update_event_request_status
update_ingredient update_invoice_status update_job_offer update_kds_item_status
update_loyalty_program update_order_status update_product update_quote_status
update_recipe update_section update_table_status upsert_beverage_item
upsert_delivery_zone upsert_happy_hour upsert_loyalty_reward validate_production
validate_redemption
""".split()

# Mots-clés discriminants, évalués dans l'ordre des boucles.
KEYWORDS = {
    "01": ["tva", "categor", "unit", "zone", "table", "dish", "recipe", "ingredient",
           "product", "supplier", "equipment", "section", "floor_plan"],
    "02": ["employee", "shift", "planning", "leave", "attendance", "contract",
           "job_", "application", "task", "station_load"],
    "03": ["stock", "production", "delivery", "deliveries", "supplier_order"],
    "04": ["haccp", "temperature", "hygiene", "cleaning", "tracabilite"],
    "05": ["site", "page", "order", "reservation", "waitlist", "pos_", "beverage",
           "happy_hour", "domain", "storefront", "kds", "template"],
    "06": ["campaign", "notification", "whatsapp", "review", "rfm", "lead"],
    "07": ["loyalty", "point", "gift_card", "redemption", "wheel", "survey",
           "client", "reward"],
    "08": ["invoice", "quote", "expense", "finance", "payment", "report"],
}

# Les outils que les mots-clés classeraient mal. Chaque ligne est un arbitrage
# assumé, pas un ajustement de confort.
OVERRIDES = {
    # « produits » et « recettes » sont le socle de la fiche technique (01),
    # mais leur CONSOMMATION est du stock (03).
    "adjust_stock": "03",
    "list_low_stocks": "03",
    "validate_production": "03",
    "get_production_ingredients": "03",
    "list_top_productions": "03",
    "list_production_alerts": "03",
    "create_supplier_order": "03",
    "list_deliveries": "03",
    # Les plans de production sont pilotés par StockVisionAI (« consommation par
    # la production »), pas par la configuration de la carte.
    "create_production_plan": "03",
    "list_production_plans": "03",
    # La privatisation est une demande entrante du canal de vente (script P5).
    "list_private_event_requests": "05",
    "update_event_request_status": "05",
    # Zones de nettoyage = HACCP, pas plan de salle.
    "create_cleaning_zone": "04",
    "list_cleaning_zones": "04",
    "list_cleaning_actions": "04",
    "record_cleaning_action": "04",
    # Les zones de livraison sont un canal de vente (05), pas le plan de salle.
    "upsert_delivery_zone": "05",
    "list_delivery_zones": "05",
    # Le client est l'actif de la boucle fidélité (07).
    "create_client": "07", "get_client": "07", "update_client": "07",
    "delete_client": "07", "list_clients": "07",
    # Les leads du site alimentent la communication (06).
    "list_site_leads": "06",
    # Les templates WhatsApp sont de la communication, pas du site.
    "create_whatsapp_template": "06", "list_whatsapp_templates": "06",
    "submit_whatsapp_template": "06",
    # Le rapport de caisse et les encaissements sont le livrable compta (08).
    "get_pos_report": "08", "record_pos_payment": "08", "list_pos_payments": "08",
    "close_pos_session": "08",
    # Transverses : rattachés à la boucle qui les expose au chef.
    "get_daily_brief": "08",
    "search_entities": "01",
    "assign_task": "02",
}


def classify(tool: str) -> str | None:
    if tool in OVERRIDES:
        return OVERRIDES[tool]
    for num, _ in BOUCLES:
        if any(k in tool for k in KEYWORDS[num]):
            return num
    return None


def main() -> None:
    counts = collections.Counter()
    detail = collections.defaultdict(list)
    unclassified = []
    for t in TOOLS:
        num = classify(t)
        if num is None:
            unclassified.append(t)
        else:
            counts[num] += 1
            detail[num].append(t)

    total = sum(counts.values())
    print(f"{len(TOOLS)} outils exposés par le serveur MCP Foodeatup\n")
    for num, slug in BOUCLES:
        print(f"  boucle {num} · {slug:24s} {counts[num]:3d}")
    print(f"  {'TOTAL classé':>36s} {total:3d}")
    if unclassified:
        print(f"\n  NON CLASSÉS ({len(unclassified)}) : {', '.join(unclassified)}")

    out = HERE.parent / "mcp-tool-counts.json"
    out.write_text(
        json.dumps(
            {
                "source": "serveur MCP Foodeatup, relevé le 2026-08-07",
                "totalExposed": len(TOOLS),
                "totalClassified": total,
                "perBoucle": {f"{n}-{s}": counts[n] for n, s in BOUCLES},
                "detail": {f"{n}-{s}": sorted(detail[n]) for n, s in BOUCLES},
                "unclassified": sorted(unclassified),
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"\n-> {out}")


if __name__ == "__main__":
    main()
