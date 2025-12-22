import joblib
import pandas as pd
from rules.eligibility_engine import bom_engine

# -------------------------------------------------
# Load trained ML model
# -------------------------------------------------
model = joblib.load("ml/model.pkl")

# -------------------------------------------------
# Dummy Incentum Form Data (User fills this)
# -------------------------------------------------
user_data = {
    "age": 30,
    "employment_type": "salaried",
    "monthly_income": 60000,
    "annual_income": 720000,
    "cibil": 780,

    "loan_amount": 2500000,
    "property_cost": 3000000,
    "agreement_value": 3000000,
    "realizable_value": 2800000,

    "property_age": 5,
    "city_type": "metro",
    "existing_emi": 5000,
    "tenure_years": 20,
    "loan_category": "purchase",

    "green_building": False,
    "is_third_property": False
}

print("\n📩 USER INPUT (INCENTUM FORM DATA)")
for k, v in user_data.items():
    print(f"{k}: {v}")

# -------------------------------------------------
# Step 1: Rule Engine Check
# -------------------------------------------------
eligible, rule_result = bom_engine(user_data)

print("\n📜 RULE ENGINE RESULT")
print("Eligible:", eligible)

if not eligible:
    print("❌ REJECTED REASON:", rule_result)
    exit()

print("✅ RULE DETAILS:", rule_result)

# -------------------------------------------------
# Step 2: Prepare ML Input (ONLY TRAINED FEATURES)
# -------------------------------------------------
X = pd.DataFrame([{
    "income": user_data["monthly_income"],
    "cibil": user_data["cibil"],
    "loan": user_data["loan_amount"]
}])

print("\n🤖 ML INPUT TO MODEL")
print(X)

# -------------------------------------------------
# Step 3: ML Prediction
# -------------------------------------------------
probability = model.predict_proba(X)[0][1] * 100
probability = round(float(probability), 2)

print("\n🤖 ML OUTPUT")
print(f"Approval Probability: {probability}%")

# -------------------------------------------------
# Step 4: Final Bank Recommendation
# -------------------------------------------------
recommendation = {
    "bank": "Bank of Maharashtra",
    "approval_probability": probability,
    "roi": rule_result["roi"],
    "emi": rule_result["emi"],
    "foir": rule_result["foir"],
    "ltv": rule_result["ltv"]
}

print("\n🏦 FINAL BANK RECOMMENDATION")
for k, v in recommendation.items():
    print(f"{k}: {v}")
