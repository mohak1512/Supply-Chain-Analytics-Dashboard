# pages/Efficiency_Analysis.py

import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("⏳ Efficiency Analysis (Lead Time vs Costs)")

    df = pd.read_csv('project10_supply_chain_data (1).csv')

    st.subheader("🕑 Lead Time vs Shipping Costs")

    fig1 = px.scatter(
        df,
        x='Lead times',
        y='Shipping costs',
        color='Location',
        title="Lead Times vs Shipping Costs",
        labels={'Lead times': 'Lead Times (days)', 'Shipping costs': 'Shipping Costs (₹)'},
        hover_data=['Supplier name']
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("""
    **Insight:**  
    Longer lead times often result in higher shipping costs.  
    Analyzing this relationship can help in negotiating better logistics contracts or optimizing warehousing.
    """)

    st.subheader("🕑 Manufacturing Lead Time vs Manufacturing Costs")

    fig2 = px.scatter(
        df,
        x='Manufacturing lead time',
        y='Manufacturing costs',
        color='Location',
        title="Manufacturing Lead Time vs Manufacturing Costs",
        labels={'Manufacturing lead time': 'Manufacturing Lead Time (days)', 'Manufacturing costs': 'Manufacturing Costs (₹)'},
        hover_data=['Supplier name']
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    **Insight:**  
    Higher manufacturing lead times can indicate inefficiencies or bottlenecks.  
    Improving lead time can directly reduce manufacturing costs and increase customer satisfaction.
    """)
