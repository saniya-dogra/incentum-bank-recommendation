import joblib
from rules.eligibility_engine import bom_engine

# -----------------------------
# Load trained ML model
# -----------------------------
model = joblib.load("ml/model.pkl")

# -----------------------------
# Dummy Incentum Form Data
# (same structure as frontend form)
# -----------------------------
user_data = {
    "age": 30,
    "employment_type": "salaried",
    "monthly_income": 60000,
    "annual_income": 720000,
    "cibil": 780,
    "loan_amount": 2500000,
    "property_cost": 3000000,
    "property_age": 5,
    "city_type": "metro",
    "existing_emi": 5000,
    "tenure_years": 20,
    "loan_category": "purchase",
    "green_building": False,
    "is_third_property": False
}

print("\n📩 USER INPUT (INCENTUM FORM DATA)")
print(user_data)

# -----------------------------
# Step 1: Run Rules Engine
# -----------------------------
eligible, rule_result = bom_engine(user_data)

print("\n📜 RULE ENGINE OUTPUT")
print("Eligible:", eligible)
print("Details:", rule_result)

if not eligible:
    print("\n❌ Application rejected by bank rules")
    exit()

# -----------------------------
# Step 2: Run ML Model
# -----------------------------
X = [[
    user_data["monthly_income"],
    user_data["cibil"],
    user_data["loan_amount"]
]]

probability = model.predict_proba(X)[0][1] * 100

print("\n🤖 ML MODEL OUTPUT")
print(f"Approval Probability: {probability:.2f}%")

# -----------------------------
# Step 3: Bank Recommendation
# -----------------------------
recommendation = {
    "bank": "Bank of Maharashtra",
    "approval_probability": round(probability, 2),
    "roi": rule_result["roi"],
    "emi": rule_result["emi"],
    "foir": rule_result["foir"],
    "ltv": rule_result["ltv"]
}

print("\n🏦 FINAL BANK RECOMMENDATION")
print(recommendation)
