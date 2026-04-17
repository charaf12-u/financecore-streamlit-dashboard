import streamlit as st
import os
from PIL import Image
from utils.data_processing import get_processed_data
from utils.logger import log_info, log_error
import pages.ExecutiveView_page as exec_page
import pages.RiskAnalysis_page as risk_page

# --> config page
icon_path = os.path.join("asset", "images", "icon.png")
icon = Image.open(icon_path)
st.set_page_config(
    page_title="FinDash",
    page_icon=icon,
    layout="wide"
)

# --> read css
def load_css(path):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css(os.path.join("asset", "styles.css"))

# --> load data
try:
    with st.spinner("Loading data..."):
        df = get_processed_data()
        log_info("App data loaded")
except Exception as e:
    log_error(f"App load error: {str(e)}")
    st.error("[Error] loading data")
    st.stop()

# --> sidebar filters
st.sidebar.title("FILTERS")

# --> select agence
agence_filter = st.sidebar.multiselect(
    "AGENCE",
    sorted(df["agence_nom"].fillna("Unknown").unique()),
    default=sorted(df["agence_nom"].fillna("Unknown").unique())
)
# --> select segment
segment_filter = st.sidebar.multiselect(
    "SEGMENT CLIENT",
    sorted(df["segment_nom"].fillna("Unknown").unique()),
    default=sorted(df["segment_nom"].fillna("Unknown").unique())
)
# --> select produit
produit_filter = st.sidebar.multiselect(
    "PRODUIT",
    sorted(df["produit_nom"].fillna("Unknown").unique()),
    default=sorted(df["produit_nom"].fillna("Unknown").unique())
)
# --> select year
year_filter = st.sidebar.slider(
    "YEAR",
    int(df["year"].min()),
    int(df["year"].max()),
    (int(df["year"].min()), int(df["year"].max()))
)

filters = (agence_filter, segment_filter, produit_filter, year_filter)

# --> header
logo_path = os.path.join("asset", "images", "findash_logo.png")
col1, col2, col3 = st.columns([2,3,2])
with col2:
    c1, c2 = st.columns([3.6,3])
    with c1:
        st.markdown("<h1 class='header-title'>Dashboard</h1>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div style='display:flex; align-items:center; height:100%;'>", unsafe_allow_html=True)
        st.image(logo_path, width=1000)
        st.markdown("</div>", unsafe_allow_html=True)
# --> subheader (slogan)
st.markdown("<p class='header-sub'>Turning Financial Data into Decisions</p>", unsafe_allow_html=True)

# --> tabs (nav between pages)
tab1, tab2 = st.tabs(["EXECUTIVE VIEW", "RISK ANALYSIS"])
# --> tab page 1
with tab1:
    exec_page.run(df , filters)
# --> tab page 2
with tab2:
    risk_page.run(df, filters)