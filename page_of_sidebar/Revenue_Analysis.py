# pages/Revenue_Analysis.py

import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("💵 Revenue Analysis")

    df = pd.read_csv('project10_supply_chain_data (1).csv')

    # Top Locations by Revenue
    top_locations = df.groupby('Location')['Revenue generated'].sum().sort_values(ascending=False).head(10).reset_index()

    st.subheader("🏙️ Top 10 Locations by Revenue")
    fig = px.bar(
        top_locations,
        x='Location',
        y='Revenue generated',
        labels={'Revenue generated': 'Revenue Generated (₹)', 'Location': 'Location'},
        color='Revenue generated',
        color_continuous_scale='blues'
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Insight:**  
    These locations contribute the most to the overall revenue.  
    Focusing on top-performing locations can drive higher profitability.
    """)

    # Revenue Distribution
    st.subheader("💹 Revenue Distribution Overall")
    fig2 = px.histogram(
        df,
        x='Revenue generated',
        nbins=50,
        title="Revenue Distribution"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # Download Option
    st.subheader("📥 Download Top 10 Revenue Locations Data")
    csv = top_locations.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='top_locations_revenue.csv',
        mime='text/csv'
    )
