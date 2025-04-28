# pages/Cost_Analysis.py

import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("📦 Cost Analysis")

    df = pd.read_csv('project10_supply_chain_data (1).csv')

    # Shipping Cost Distribution
    st.subheader("🚚 Shipping Costs Distribution")
    fig1 = px.histogram(
        df,
        x='Shipping costs',
        nbins=50,
        title="Shipping Costs Distribution",
        labels={'Shipping costs': 'Shipping Costs (₹)'}
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("""
    **Insight:**  
    Monitoring shipping costs helps identify cost-saving opportunities in logistics and transportation.
    """)

    # Manufacturing Cost Distribution
    st.subheader("🏭 Manufacturing Costs Distribution")
    fig2 = px.histogram(
        df,
        x='Manufacturing costs',
        nbins=50,
        title="Manufacturing Costs Distribution",
        labels={'Manufacturing costs': 'Manufacturing Costs (₹)'}
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    **Insight:**  
    Analyzing manufacturing costs can reveal inefficiencies in production processes.
    """)

    # Download Option
    st.subheader("📥 Download Full Cost Data")
    csv = df[['Manufacturing costs', 'Shipping costs']].to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Cost Data CSV",
        data=csv,
        file_name='cost_data.csv',
        mime='text/csv'
    )
