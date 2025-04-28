import streamlit as st
from streamlit_option_menu import option_menu

# Set Streamlit page configuration
st.set_page_config(page_title="Supply Chain Analytics", layout="wide", initial_sidebar_state="expanded")

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        "Supply Chain Analytics Dashboard",
        [
            "Home",
            "Executive Summary",
            "Revenue Analysis",
            "Cost Analysis",
            "Efficiency Analysis",
            "Quality Insights",
            "Supplier Performance",
            "Transportation Insights",
            "Correlation Analysis",
            "Cost Prediction"
        ],
        icons=['house', 'bar-chart-line', 'cash-coin', 'box', 'clock', 'tools', 'people', 'truck', 'graph-up-arrow', 'lightbulb'],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#f0f2f6"},
            "icon": {"color": "blue", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px"},
            "nav-link-selected": {"background-color": "#2e7bcf", "color": "white"}
        }
    )

# Dynamic page loading
if selected == "Home":
    import pages.Home as home
    home.app()
elif selected == "Executive Summary":
    import pages.Executive_Summary as exec_sum
    exec_sum.app()
elif selected == "Revenue Analysis":
    import pages.Revenue_Analysis as revenue
    revenue.app()
elif selected == "Cost Analysis":
    import pages.Cost_Analysis as cost
    cost.app()
elif selected == "Efficiency Analysis":
    import pages.Efficiency_Analysis as efficiency
    efficiency.app()
elif selected == "Quality Insights":
    import pages.Quality_Insights as quality
    quality.app()
elif selected == "Supplier Performance":
    import pages.Supplier_Performance as supplier
    supplier.app()
elif selected == "Transportation Insights":
    import pages.Transportation_Insights as transport
    transport.app()
elif selected == "Correlation Analysis":
    import pages.Correlation_Analysis as correlation
    correlation.app()
elif selected == "Cost Prediction":
    import pages.Cost_Prediction as predict
    predict.app()
