import streamlit as st
import numpy as np
import joblib

# -------------------------------
# Load trained model
# -------------------------------
model = joblib.load("insurance-response-predictor.pkl")

# -------------------------------
# Page configuration
# -------------------------------
st.set_page_config(page_title="Vehicle Insurance Response Predictor")
st.title("🚗 Vehicle Insurance Response Predictor")
st.write("---")

st.header("Fill the details below:")

# -------------------------------
# User inputs
# -------------------------------
gender = st.selectbox("Your Gender", ["Select", "Male", "Female"])
age = st.number_input("Your Age", min_value=0, step=1)
dl = st.selectbox("Do you have a Driving License?", ["Select", "Yes", "No"])
reg_code = st.number_input("Your Region Code", min_value=0, step=1)
prev_insured = st.selectbox("Are you previously insured?", ["Select", "Yes", "No"])
vehicle_age = st.selectbox("What's your vehicle age?", ["Select", "Less than 1 Year", "1-2 Years", "More than 2 Years"])
vehicle_damage = st.selectbox("Does your vehicle have/had damages?", ["Select", "Yes", "No"])
annual_premium = st.number_input("What's your Annual Premium?", min_value=0, step=1)
sales_channel = st.number_input("What's the Policy Sales Channel?", min_value=0, step=1)
vintage = st.number_input("Vintage of the customer", min_value=0, step=1)

st.write("---")

# -------------------------------
# Predict button
# -------------------------------
if st.button("Predict"):
    if gender == "Select" or dl == "Select" or prev_insured == "Select" or vehicle_age == "Select" or vehicle_damage == "Select":
        st.warning("⚠️ Please fill all the fields before prediction.")
    else:
        # Encode categorical inputs
        Male = 1 if gender == 'Male' else 0
        DL = 1 if dl == 'Yes' else 0
        PrevIns = 1 if prev_insured == 'Yes' else 0
        VehDam = 1 if vehicle_damage == 'Yes' else 0
        lessThanOne = 1 if vehicle_age == "Less than 1 Year" else 0
        moreThanTwo = 1 if vehicle_age == "More than 2 Years" else 0

        # Create input array
        features = np.array([[Male, age, DL, reg_code, PrevIns, VehDam,
                              annual_premium, sales_channel, vintage,
                              lessThanOne, moreThanTwo]])

        # Make prediction
        prediction = model.predict(features)[0]
        result = "✅ The customer will buy the insurance" if prediction == 1 else "❌ The customer will not buy the insurance"

        # Display result
        st.success(result)
