# pages/Supplier_Performance.py

import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("📑 Supplier Performance Analysis")

    df = pd.read_csv('project10_supply_chain_data (1).csv')

    st.subheader("🏭 Top 10 Suppliers by Revenue Generated")

    top_suppliers = df.groupby('Supplier name')['Revenue generated'].sum().sort_values(ascending=False).head(10).reset_index()

    fig1 = px.bar(
        top_suppliers,
        x='Supplier name',
        y='Revenue generated',
        color='Revenue generated',
        color_continuous_scale='blues',
        labels={'Revenue generated': 'Revenue Generated (₹)', 'Supplier name': 'Supplier'}
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("""
    **Insight:**  
    Understanding top revenue-generating suppliers helps build strong strategic partnerships.
    """)

    st.subheader("🏭 Top 10 Suppliers by Manufacturing Costs")

    top_supplier_costs = df.groupby('Supplier name')['Manufacturing costs'].sum().sort_values(ascending=False).head(10).reset_index()

    fig2 = px.bar(
        top_supplier_costs,
        x='Supplier name',
        y='Manufacturing costs',
        color='Manufacturing costs',
        color_continuous_scale='reds',
        labels={'Manufacturing costs': 'Manufacturing Costs (₹)', 'Supplier name': 'Supplier'}
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    **Insight:**  
    Suppliers with higher manufacturing costs may need performance reviews for optimization.
    """)

    # Download Option
    st.subheader("📥 Download Supplier Performance Data")
    csv = df[['Supplier name', 'Revenue generated', 'Manufacturing costs']].to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Supplier Data CSV",
        data=csv,
        file_name='supplier_performance.csv',
        mime='text/csv'
    )
