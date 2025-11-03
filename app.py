import numpy as np
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("insurance-response-predictor.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    Male = 1 if data['gender'].lower() == 'male' else 0
    Age = int(data['age'])
    DL = 1 if data['dl'].lower() == 'yes' else 0
    RegCode = int(data['reg_code'])
    PrevIns = 1 if data['prev_insured'].lower() == 'yes' else 0
    VehDam = 1 if data['vehicle_damage'].lower() == 'yes' else 0
    AnnualPrem = float(data['annual_premium'])
    SalesChannel = int(data['sales_channel'])
    Vintage = int(data['vintage'])
    VehicleAge = data['vehicle_age']
    
    lessThanOne = 1 if VehicleAge == "Less than 1 Year" else 0
    moreThanTwo = 1 if VehicleAge == "More than 2 Years" else 0
    
    # Make prediction
    prediction = model.predict([[Male, Age, DL, RegCode, PrevIns, VehDam, AnnualPrem,
                                 SalesChannel, Vintage, lessThanOne, moreThanTwo]])
    
    result = "The customer will buy the insurance" if prediction[0] == 1 else "The customer will not buy the insurance"
    
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
