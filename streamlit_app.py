import streamlit as st
import requests

st.set_page_config(page_title="Vehicle Insurance Response Predictor")
st.title("Vehicle Insurance Response Predictor")
st.write("---")

st.header("Insurance Response Prediction Form")

gender = st.selectbox("Your Gender", ["Select", "Male", "Female"])
age = st.number_input("Your Age", min_value=0, step=1)
dl = st.selectbox("Do you have a Driving Liscense?", ["Select", "Yes", "No"])
reg_code = st.number_input("Your Region Code", min_value=0, step=1)
prev_insured = st.selectbox("Are you previously insured?", ["Select", "Yes", "No"])
vehicle_age = st.selectbox("What's your vehicle age?", ["Select", "Less than 1 Year", "1-2 Years", "More than 2 Years"])
vehicle_damage = st.selectbox("Does your vehicle have/had damages?", ["Select", "Yes", "No"])
annual_premium = st.number_input("What's your Annual Premium?", min_value=0, step=1)
sales_channel = st.number_input("What's the Policy Sales Channel?", min_value=0, step=1)
vintage = st.number_input("Vintage of the customer", min_value=0, step=1)

st.write("---")

if st.button("Predict"):
    data = {
        "gender": gender,
        "age": age,
        "dl": dl,
        "reg_code": reg_code,
        "prev_insured": prev_insured,
        "vehicle_age": vehicle_age,
        "vehicle_damage": vehicle_damage,
        "annual_premium": annual_premium,
        "sales_channel": sales_channel,
        "vintage": vintage
    }
    
    try:
        response = requests.post("http://127.0.0.1:5000/predict", json=data)
        result = response.json()["prediction"]
        st.success(result)
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")
