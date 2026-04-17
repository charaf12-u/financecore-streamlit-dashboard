import streamlit as st

def display_kpis(kpis):

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("TRANSACTION", f"{kpis['total_transactions']:,}")
    col2.metric("REVENUE (€)", f"{kpis['total_revenue']:,.2f}")
    col3.metric("CLIENTS ACTIFS", f"{kpis['active_clients']:,}")
    col4.metric("MARGE MOYENNE", f"{kpis['avg_margin']:,.2f}")