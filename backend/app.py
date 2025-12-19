from flask import Flask, request, jsonify
from rules.eligibility_engine import bom_engine
import joblib

app = Flask(__name__)
model = joblib.load("ml/model.pkl")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json

    eligible, result = bom_engine(data)
    if not eligible:
        return jsonify({"status":"Rejected","reason":result})

    prob = model.predict_proba([[
        data["monthly_income"],
        data["cibil"],
        data["loan_amount"]
    ]])[0][1]

    return jsonify({
        "bank": "Bank of Maharashtra",
        "approval_probability": round(prob*100,2),
        "details": result
    })
