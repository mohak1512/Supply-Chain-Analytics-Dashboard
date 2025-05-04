# pages/Correlation_Analysis.py

import streamlit as st
import pandas as pd
import plotly.figure_factory as ff

def app():
    st.title("📈 Correlation Analysis")

    df = pd.read_csv('project10_supply_chain_data (1).csv')

    st.subheader("🔗 Correlation Heatmap")

    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    if not numeric_df.empty:
        corr = numeric_df.corr()

        fig = ff.create_annotated_heatmap(
            z=corr.values,
            x=list(corr.columns),
            y=list(corr.index),
            annotation_text=corr.round(2).values,
            showscale=True,
            colorscale='Blues'
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        **Insight:**  
        The correlation heatmap helps identify strong positive or negative relationships between supply chain variables.  
        For example, a positive correlation between 'Lead times' and 'Shipping costs' suggests that longer lead times may increase logistics expenses.
        """)
    else:
        st.warning("No numeric columns available for correlation analysis.")
