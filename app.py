import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load trained model
model = pickle.load(open("LinearRegressionModel.pkl", "rb"))

st.title("Car Price Predictor")
st.write("Enter car details to get the estimated resale price.")

# Input fields
name = st.text_input("Car Name (e.g., Maruti Suzuki Swift)")
company = st.text_input("Company (e.g., Maruti)")
year = st.number_input("Year of Purchase", min_value=1990, max_value=2025, value=2015)
kms_driven = st.number_input("Kilometers Driven", min_value=0, value=10000)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])

# Prediction
if st.button("Predict Price"):
    try:
        input_df = pd.DataFrame([[name, company, year, kms_driven, fuel_type]],
                                columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
        prediction = model.predict(input_df)[0]
        st.success(f"Estimated Price: ₹{int(prediction):,}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
