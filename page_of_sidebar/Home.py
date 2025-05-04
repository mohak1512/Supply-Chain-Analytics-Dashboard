# pages/Home.py

import streamlit as st

# Define the app() function
def app():
    # Custom CSS for professional styling
    st.markdown("""
        <style>
            .css-1d391kg {background-color: #f9f9f9;}
            .block-container {padding-top: 1rem;}
            .sidebar .sidebar-content {
                background-color: #ffffff;
                padding: 2rem 1rem;
                border-right: 2px solid #e5e5e5;
                height: 100vh;
            }
            .css-1v0mbdj {padding-top: 0rem;}
            header {visibility: hidden;}
            .css-18e3th9 {padding-top: 2rem;}
            .css-1cpxqw2 {margin-top: -80px;}
            .top-banner {
                background-color: #0e1117;
                padding: 1rem 2rem;
               
                display: flex;
                align-items: center;
                justify-content: space-between;
            }
            .top-left {
                font-size: 22px;
                font-weight: 600;
                color: #2e7bcf;
                cursor: pointer;
            }
            .top-right {
                font-size: 16px;
            }
            .stButton>button {
                background-color: #2e7bcf;
                color: white;
                border: none;
                padding: 0.4rem 1rem;
                border-radius: 5px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Custom top bar
    st.markdown("""
        <div class="top-banner">
            <div class="top-left" onclick="window.location.reload()">Welcome, Mohak</div>
            <div class="top-right">
                🌗 
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Main Welcome Section
    st.title("🏠 Supply Chain Analytics Dashboard")

    st.markdown("""
        Welcome to the **Supply Chain Analytics Professional Dashboard**.  
        Explore deep insights into:
        - 📊 Revenue, Cost, and Efficiency Analysis
        - 🔧 Supplier and Quality Management
        - 🚚 Transportation & Logistics Insights
        - 🔮 Predictive Cost Modeling

        Use the left **Navigation Panel** to move through different business intelligence modules.
    """)
