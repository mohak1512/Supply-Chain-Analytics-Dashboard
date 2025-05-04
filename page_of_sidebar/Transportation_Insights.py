# pages/Transportation_Insights.py

import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("🚚 Transportation and Logistics Insights")

    df = pd.read_csv('project10_supply_chain_data (1).csv')

    st.subheader("🚚 Transportation Modes Distribution")

    if 'Transportation modes' in df.columns:
        transport_mode = df['Transportation modes'].value_counts().reset_index()
        transport_mode.columns = ['Transportation Mode', 'Count']

        fig = px.pie(
            transport_mode,
            names='Transportation Mode',
            values='Count',
            title="Transportation Mode Distribution",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        **Insight:**  
        Understanding preferred transportation modes helps in optimizing delivery strategies.
        """)
    else:
        st.warning("No Transportation Modes information available in the dataset.")

    st.subheader("🛣️ Top 10 Routes by Revenue Generated")

    if 'Routes' in df.columns:
        top_routes = df.groupby('Routes')['Revenue generated'].sum().sort_values(ascending=False).head(10).reset_index()

        fig2 = px.bar(
            top_routes,
            x='Routes',
            y='Revenue generated',
            color='Revenue generated',
            color_continuous_scale='blues',
            labels={'Revenue generated': 'Revenue Generated (₹)', 'Routes': 'Route'}
        )
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("""
        **Insight:**  
        Monitoring route performance can help optimize logistics operations.
        """)
    else:
        st.warning("No Routes information available in the dataset.")
