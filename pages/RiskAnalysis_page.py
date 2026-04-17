from core.filters import apply_filters
from core.risk_engine import classify_risk, top_risk_clients
from components.risk_chart import correlation_heatmap, risk_scatter
from utils.logger import *
import streamlit as st


def run(df, filters):




    # --> title page
    st.title("RISK ANALYSIS DASHBOARD")


    # --> apply filters
    try:
        if not filters:
            log_warning("No filters provided, using default")
            st.stop()
        
        agence_filter, segment_filter, produit_filter, year_filter = filters
        df_filtered = apply_filters(
            df,
            agence_filter,
            segment_filter,
            produit_filter,
            year_filter
        )

        log_info(f"Risk filtered: {len(df_filtered)} rows")
        # --> check empty filter
        if df_filtered.empty:
            log_warning("Risk empty dataframe")
            st.warning("[WARNING] No data available")

    except Exception as e:
        log_error(f"Risk filtering error: {str(e)}")
        st.error("[ERROR] Error filtering data")
        st.stop()

    # --> classify risk
    try:
        df_risk = classify_risk(df_filtered)
        log_info("Risk classification applied")
    except Exception as e:
        log_error(f"Risk classification error: {str(e)}")
        st.error("[ERROR] Error in risk classification")
        st.stop()

    # --> charts
    st.divider()

    col1, col2 = st.columns(2, gap="large")
    # --> correlation heatmap
    with col1:
        st.subheader("CORRELATION")
        try:
            st.plotly_chart(
                correlation_heatmap(df_risk),
                use_container_width=True
            )
            log_info("Correlation heatmap displayed")
        except Exception as e:
            log_error(f"Correlation error: {str(e)}")
            st.error("[ERROR] Error displaying correlation")
    # --> risk scatter
    with col2:
        st.subheader("RISK SCATTER")
        try:
            st.plotly_chart(
                risk_scatter(df_risk),
                use_container_width=True
            )
            log_info("Risk scatter displayed")
        except Exception as e:
            log_error(f"Risk scatter error: {str(e)}")
            st.error("[ERROR] Error displaying risk scatter")
    
    # --> top risk clients
    st.divider()
    st.subheader("TOP RISK CLIENTS")
    try:
        st.dataframe(
            top_risk_clients(df_risk),
            use_container_width=True
        )
        log_info("Top risk clients displayed")
    except Exception as e:
        log_error(f"Top clients error: {str(e)}")
        st.error("[ERROR] Error displaying table")