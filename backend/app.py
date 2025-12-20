from flask import Flask, request, jsonify
from rules.eligibility_engine import bom_engine
from utils.validators import validate_input
import joblib

app = Flask(__name__)
model = joblib.load("ml/model.pkl")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json

    # 1️⃣ Validate input
    valid, msg = validate_input(data)
    if not valid:
        return jsonify({"status": "Error", "message": msg}), 400

    # 2️⃣ Apply Bank of Maharashtra rules
    eligible, result = bom_engine(data)
    if not eligible:
        return jsonify({"status": "Rejected", "reason": result})


    prob = model.predict_proba([[
        data["monthly_income"],
        data["cibil"],
        data["loan_amount"]
    ]])[0][1]

    return jsonify({
    "recommendations": [
        {
            "bank": "Bank of Maharashtra",
            "approval_probability": round(prob * 100, 2),
            "details": result
        }
    ]
})
