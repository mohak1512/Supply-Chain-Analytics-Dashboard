# pages/Executive_Summary.py

import streamlit as st
import pandas as pd

def app():
    st.title("📊 Executive Summary")

    # Load Data
    df = pd.read_csv('project10_supply_chain_data (1).csv')

    # KPIs Calculation
    total_revenue = df['Revenue generated'].sum()
    avg_manufacturing_cost = df['Manufacturing costs'].mean()
    total_units_sold = df['Number of products sold'].sum()
    avg_shipping_cost = df['Shipping costs'].mean()

    # Display Metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="💵 Total Revenue", value=f"₹ {total_revenue:,.2f}")
    with col2:
        st.metric(label="🏭 Avg Manufacturing Cost", value=f"₹ {avg_manufacturing_cost:,.2f}")
    with col3:
        st.metric(label="📦 Total Units Sold", value=f"{total_units_sold:,}")
    with col4:
        st.metric(label="🚚 Avg Shipping Cost", value=f"₹ {avg_shipping_cost:,.2f}")

    st.markdown("---")
    st.subheader("🔍 Business Overview")
    st.write("""
    The Executive Summary highlights key performance metrics for the business:
    - **Revenue** indicates the company's market performance.
    - **Manufacturing Costs** and **Shipping Costs** help track operational efficiency.
    - **Units Sold** measure overall market penetration and sales effectiveness.
    """)
