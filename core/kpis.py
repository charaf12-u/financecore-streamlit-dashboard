
# --> calcule KPIs
def calculate_kpis(df):

    # --> total transactions
    total_transactions = df["transaction_id"].nunique()

    # --> total revenue
    total_revenue = df["montant_eur"].sum()

    # --> active clients
    active_clients = df["client_id"].nunique()

    # --> average margin
    # marge = montant * taux_interet 
    mapping_taux = {
        "depot especes": 0.02,
        "retrait dab": 0.00,
        "prelevement": 0.00,
        "paiement cb": 0.00,
        "interets": 0.03,
        "remboursement credit": 0.08,
        "virement international": 0.01,
        "virement": 0.00
    }
    df["taux_interet_estime"] = df["categorie_nom"].map(mapping_taux)
    df["marge_estimee"] = (
        df["montant_eur"] * df["taux_interet_estime"]
    )

    if "taux_interet_estime" in df.columns:
        avg_margin = df["marge_estimee"].mean()
    else:
        avg_margin = 0.0
    

    return {
        "total_transactions": total_transactions,
        "total_revenue": total_revenue,
        "active_clients": active_clients,
        "avg_margin": avg_margin
    }