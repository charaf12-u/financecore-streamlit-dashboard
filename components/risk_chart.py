import plotly.express as px



# --> Affiche la heatmap de correlation des risques
def correlation_heatmap(df):

    # --> Calcul la correlation
    cols = [
        "score_credit",
        "montant_eur",
        "taux_interet"
    ]
    corr = df[cols].corr()
    # --> Affiche la heatmap de correlation
    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        title="CORRELATION DES RISQUES CLIENTS"
    )
    return fig



# --> Affiche le scatter plot des risques
def risk_scatter(df):

    df_plot = df.copy()
    df_plot["montant_abs"] = df_plot["montant_eur"].abs()
    fig = px.scatter(
        df_plot,
        x="score_credit",
        y="montant_eur",
        color="transaction_type",
        hover_data=["client_id"],
        size="montant_abs",
        title="RISQUE DETECTE POUR LES CLIENTS",
        color_discrete_map={
            "Positive": "green",
            "Negative": "red"
        }
    )

    return fig