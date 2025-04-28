# pages/Quality_Insights.py

import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("🔧 Quality and Defect Rate Analysis")

    df = pd.read_csv('project10_supply_chain_data (1).csv')

    st.subheader("⚙️ Defect Rates Distribution")

    if 'Defect rates' in df.columns:
        fig = px.histogram(
            df,
            x='Defect rates',
            nbins=30,
            title="Distribution of Defect Rates",
            labels={'Defect rates': 'Defect Rate (%)'}
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        **Insight:**  
        Monitoring defect rates helps ensure quality control.  
        High defect rates can increase costs and customer dissatisfaction.
        """)

        st.subheader("🏭 Top Suppliers by Average Defect Rate")

        top_defects = df.groupby('Supplier name')['Defect rates'].mean().sort_values(ascending=False).head(10).reset_index()

        fig2 = px.bar(
            top_defects,
            x='Supplier name',
            y='Defect rates',
            color='Defect rates',
            color_continuous_scale='reds',
            labels={'Defect rates': 'Average Defect Rate', 'Supplier name': 'Supplier'}
        )
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("""
        **Insight:**  
        Identifying suppliers with higher average defect rates helps target corrective actions.
        """)
    else:
        st.warning("No Defect Rate information available in the dataset.")
