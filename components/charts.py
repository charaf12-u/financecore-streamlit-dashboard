import plotly.express as px



# --> line chart (transactions)
def line_transactions(df):

    df_grouped = df.groupby(["year", "month", "type_operation_nom"])["montant_eur"].sum().reset_index()
    df_grouped["date"] = df_grouped["year"].astype(str) + "-" + df_grouped["month"].astype(str)

    fig = px.line(
        df_grouped,
        x="date",
        y="montant_eur",
        color="type_operation_nom",
        title="EVOLUTION DES TRANSACTIONS PAR TYPE D'OPERATION"
    )

    return fig



# --> bar chart (agence)
def bar_agence(df):

    df_grouped = df.groupby("agence_nom")["montant_eur"].sum().reset_index()

    fig = px.bar(
        df_grouped,
        x="agence_nom",
        y="montant_eur",
        title="CA PAR AGENCE"
    )

    return fig


# --> bar chart (produit)
def bar_produit(df):

    df_grouped = df.groupby("produit_nom")["montant_eur"].sum().reset_index()

    fig = px.bar(
        df_grouped,
        x="produit_nom",
        y="montant_eur",
        title="CA PAR PRODUIT"
    )

    return fig



# --> pie chart (segment)
def pie_segment(df):

    df_grouped = df.groupby("segment_nom")["client_id"].nunique().reset_index()

    fig = px.pie(
        df_grouped,
        names="segment_nom",
        values="client_id",
        title="SEGMENTATION DES CLIENTS"
    )

    return fig