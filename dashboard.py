import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# Feature names (must match training)
features = ['Rent Index', 'Groceries Index', 'Restaurant Price Index', 'Local Purchasing Power Index']

# Streamlit UI
st.title("🌍 Cost of Living Index Predictor")
st.markdown("Enter values below to predict the **Cost of Living Index** using a pre-trained Linear Regression model.")

# Input sliders
rent_index = st.slider('🏠 Rent Index', min_value=0.0, max_value=100.0, value=30.0)
groceries_index = st.slider('🛒 Groceries Index', min_value=0.0, max_value=100.0, value=40.0)
restaurant_index = st.slider('🍽️ Restaurant Price Index', min_value=0.0, max_value=150.0, value=50.0)
purchasing_power = st.slider('💰 Local Purchasing Power Index', min_value=0.0, max_value=200.0, value=60.0)

# Prepare input for prediction
input_data = pd.DataFrame([[rent_index, groceries_index, restaurant_index, purchasing_power]],
                          columns=features)

# Predict
prediction = model.predict(input_data)[0]

# Display result
st.subheader("📊 Predicted Cost of Living Index:")
st.success(f"{prediction:.2f}")

# Optional: Show model coefficients
if st.checkbox("Show model details"):
    st.write("### Coefficients:")
    coeffs = pd.DataFrame(model.coef_, features, columns=["Coefficient"])
    st.dataframe(coeffs)

    intercept = model.intercept_
    st.markdown(f"**Intercept:** {intercept:.2f}")
