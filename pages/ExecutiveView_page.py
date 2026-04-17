from core.filters import apply_filters
from core.kpis import calculate_kpis
from components.kpi_cards import display_kpis
from components.charts import *
from utils.logger import *
import streamlit as st

def run(df, filters):
     
    # --> titel page
    st.title("EXECUTIVE VIEW DASHBOARD")


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
        log_info(f"Executive filtered: {len(df_filtered)} rows")

        # --> check empty filter
        if df_filtered.empty:
            log_warning("Executive empty dataframe")
            st.warning("[WARNING] No data available")

    except Exception as e:
        log_error(f"Executive filtering error: {str(e)}")
        st.error("[ERROR] Error filtering data")
        st.stop()

    # --> calculate KPIs
    kpis = calculate_kpis(df_filtered)
    display_kpis(kpis)

    # --> charts
    col1, col2 = st.columns([3,2])
    # --> line chart transactions
    with col1:
        st.plotly_chart(line_transactions(df_filtered), use_container_width=True)
    # --> line chart montant
    with col2:
        st.plotly_chart(pie_segment(df_filtered), use_container_width=True)
    # --> bar charts
    col3, col4 = st.columns(2)
    # --> bar chart agence
    with col3:
        st.plotly_chart(bar_agence(df_filtered), use_container_width=True)
    # --> bar chart produit
    with col4:
        st.plotly_chart(bar_produit(df_filtered), use_container_width=True)

    st.divider()

    # -->
    col_left, col_right = st.columns([1,2])

    # --> export data
    with col_left:
        st.subheader("EXPORT DATA")

        try:
            csv = df_filtered.to_csv(index=False).encode("utf-8")

            if df_filtered.empty:
                log_warning("Export attempted with empty dataframe")

            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="financecore_filtered_data.csv",
                mime="text/csv"
            )

            log_info("Export button displayed")

        except Exception as e:
            log_error(f"Export error: {str(e)}")


    # --> executive summary
    with col_right:
        st.subheader("EXECUTIVE SUMMARY")

        try:
            if df_filtered["montant_eur"].mean() > 0:
                st.markdown("<div class='summary-positive'>📈 Positive financial trend detected</div>", unsafe_allow_html=True)
                log_info("Positive trend detected")

            else:
                st.markdown("<div class='summary-negative'>⚠️ Negative financial trend detected</div>", unsafe_allow_html=True)
                log_info("Negative trend detected")

        except Exception as e:
            log_error(f"Summary error: {str(e)}")