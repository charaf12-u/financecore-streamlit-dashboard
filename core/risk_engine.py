
# --> moteur de risque
def classify_risk(df):
    # --> logique de classification
    def label(row):
        if row["score_credit"] < 400 and row["montant_eur"] > 5000:
            return "High Risk"
        elif row["score_credit"] < 700:
            return "Medium Risk"
        else:
            return "Low Risk"

    df["risk_level"] = df.apply(label, axis=1)

    return df

# --> top 10 clients à risque
def top_risk_clients(df):
    top = df.sort_values(
        by=["montant_eur", "score_credit"],
        ascending=[False, True]
    ).head(10)

    return top[["client_id", "score_credit", "montant_eur", "categorie_risque"]]