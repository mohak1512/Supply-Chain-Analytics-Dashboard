# pages/Cost_Prediction.py

import streamlit as st
import numpy as np
from xgboost import XGBRegressor

def app():
    st.title("🔮 Predict Supply Chain Costs")

    st.markdown("""
    Use this tool to predict estimated supply chain costs based on important operational parameters.
    Please fill in the required details below:
    """)

    # Load trained model
    model = XGBRegressor()
    model.load_model('final_xgb_model.json')

    # Important features needed for prediction
    important_features = [
        'Price', 'Availability', 'Number of products sold', 'Revenue generated', 
        'Stock levels', 'Lead times', 'Order quantities', 'Shipping times', 
        'Shipping costs', 'Lead time', 'Production volumes', 
        'Manufacturing lead time', 'Manufacturing costs', 'Defect rates'
    ]

    # Collect input from user
    input_data = []
    for feature in important_features:
        value = st.number_input(f"Enter {feature.replace('_', ' ')}:", value=0.0)
        input_data.append(value)

    # Predict button
    if st.button("Predict Cost"):
        input_array = np.array(input_data).reshape(1, -1)
        prediction = model.predict(input_array)[0]
        st.success(f"✅ Predicted Supply Chain Cost: ₹ {prediction:.2f}")
