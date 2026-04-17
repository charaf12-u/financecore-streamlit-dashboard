
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
    if "taux_interet" in df.columns:
        df["marge"] = df["montant_eur"] * (df["taux_interet"] / 100)
        avg_margin = df["marge"].mean()
    else:
        avg_margin = 0

    return {
        "total_transactions": total_transactions,
        "total_revenue": total_revenue,
        "active_clients": active_clients,
        "avg_margin": avg_margin
    }