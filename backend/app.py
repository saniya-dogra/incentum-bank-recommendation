from flask import Flask, request, jsonify

import joblib
import pandas as pd

from rules.eligibility_engine import bom_engine

from rules.risk_engine import (
    calculate_risk,
    explain_risk
)

from rules.bank_recommender import (
    recommend_banks
)

from utils.validators import (
    validate_input
)

from . import config


app = Flask(__name__)


# ==========================================
# Load ML model
# ==========================================

model = joblib.load(config.MODEL_PATH)


# ==========================================
# Health Check
# ==========================================

@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "healthy",
        "service": "AI Fintech Risk Manager",
        "model": "Logistic Regression"
    })


# ==========================================
# Main Risk API
# ==========================================

@app.route("/recommend", methods=["POST"])
def recommend():

    data = request.get_json(silent=True)

    # ======================================
    # 1. Validate input
    # ======================================

    if not data:

        return jsonify({
            "status": "Error",
            "message": "JSON request body required"
        }), 400

    valid, message = validate_input(data)

    if not valid:

        return jsonify({
            "status": "Error",
            "message": message
        }), 400


    # ======================================
    # 2. Financial Rule Engine (Eligibility Gate)
    # ======================================

    # bom_engine runs ALL hard eligibility checks:
    # age, income, employment, tenure, property,
    # loan purpose, special cases (pensioner /
    # agriculturist), FOIR limit, and LTV limit.
    # If the applicant fails ANY of these, this is
    # the final gate — we reject here and never
    # reach the ML model or bank matching stage.

    eligible, rule_result = bom_engine(data)

    if not eligible:

        return jsonify({

            "status": "Success",

            "decision": "REJECTED",

            "rejection_reason": rule_result,

            "risk_assessment": None,

            "risk_factors": [],

            "financial_metrics": None,

            "bank_recommendations": []

        }), 200


    # ======================================
    # 3. Feature Engineering
    # ======================================

    monthly_income = data["monthly_income"]
    loan_amount = data["loan_amount"]
    existing_emi = data["existing_emi"]

    property_value = min(
        data["agreement_value"],
        data["realizable_value"]
    )

    loan_to_income = (
        loan_amount /
        (monthly_income * 12)
    )

    ltv = (
        loan_amount /
        property_value
    )

    emi = rule_result["emi"]

    foir = (
        emi + existing_emi
    ) / monthly_income


    # ======================================
    # 4. ML Risk Prediction
    # ======================================

    model_input = pd.DataFrame([{

        "age": data["age"],

        "income": monthly_income,

        "cibil": data["cibil"],

        "loan": loan_amount,

        "existing_emi": existing_emi,

        "tenure": data["tenure_years"],

        "property_age": data["property_age"],

        "property_value": property_value,

        "foir": foir,

        "ltv": ltv,

        "loan_to_income": loan_to_income,

        "employment_type":
            data["employment_type"],

        "city_type":
            data["city_type"]

    }])


    probability = model.predict_proba(
        model_input
    )[0][1]

    probability = float(probability)


    # ======================================
    # 5. Risk Assessment
    # ======================================

    risk = calculate_risk(

        probability,

        foir,

        ltv,

        data["cibil"],

        loan_to_income

    )


    risk_factors = explain_risk(

        data["cibil"],

        foir,

        ltv,

        loan_to_income

    )


    # ======================================
    # 6. Multi-Bank Recommendation
    # ======================================

    bank_recommendations = recommend_banks(

        data["cibil"],

        foir,

        ltv,

        probability

    )


    # ======================================
    # 7. Final Risk Decision
    # ======================================

    if risk["risk_level"] == "LOW":

        decision = "RECOMMEND_APPROVAL"

    elif risk["risk_level"] == "MEDIUM":

        decision = "MANUAL_REVIEW"

    else:

        decision = "HIGH_RISK_REVIEW"


    # ======================================
    # 8. Final Response
    # ======================================

    return jsonify({

        "status": "Success",

        "decision": decision,

        "risk_assessment": {

            "risk_level":
                risk["risk_level"],

            "risk_score":
                risk["risk_score"],

            "approval_probability":
                round(
                    probability * 100,
                    2
                ),

            "recommended_action":
                risk["recommended_action"]

        },

        "risk_factors":
            risk_factors,

        "financial_metrics": {

            "roi":
                rule_result["roi"],

            "emi":
                rule_result["emi"],

            "foir":
                round(
                    foir * 100,
                    2
                ),

            "ltv":
                round(
                    ltv * 100,
                    2
                ),

            "loan_to_income":
                round(
                    loan_to_income,
                    2
                )

        },

        "bank_recommendations":
            bank_recommendations

    })


# ==========================================
# Run application
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=config.PORT,
        debug=config.DEBUG
    )