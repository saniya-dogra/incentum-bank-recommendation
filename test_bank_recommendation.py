# import joblib
# import pandas as pd
# from rules.eligibility_engine import bom_engine

# # -------------------------------------------------
# # Load trained ML model
# # -------------------------------------------------
# model = joblib.load("ml/model.pkl")

# # -------------------------------------------------
# # Dummy Incentum Form Data (User fills this)
# # -------------------------------------------------
# user_data = {
#     "age": 30,
#     "employment_type": "salaried",
#     "monthly_income": 300000,
#     "annual_income": 720000,
#     "cibil": 650,

#     "loan_amount": 250000,
#     "property_cost": 3000000,
#     "agreement_value": 3000000,
#     "realizable_value": 2800000,

#     "property_age": 5,
#     "city_type": "metro",
#     "existing_emi": 5000,
#     "tenure_years": 20,
#     "loan_category": "purchase",

#     "green_building": False,
#     "is_third_property": False
# }

# print("\n📩 USER INPUT (INCENTUM FORM DATA)")
# for k, v in user_data.items():
#     print(f"{k}: {v}")

# # -------------------------------------------------
# # Step 1: Rule Engine Check
# # -------------------------------------------------
# eligible, rule_result = bom_engine(user_data)

# print("\n📜 RULE ENGINE RESULT")
# print("Eligible:", eligible)

# if not eligible:
#     print("❌ REJECTED REASON:", rule_result)
#     exit()

# print("✅ RULE DETAILS:", rule_result)

# # -------------------------------------------------
# # Step 2: Prepare ML Input (ONLY TRAINED FEATURES)
# # -------------------------------------------------
# X = pd.DataFrame([{
#     "income": user_data["monthly_income"],
#     "cibil": user_data["cibil"],
#     "loan": user_data["loan_amount"]
# }])

# print("\n🤖 ML INPUT TO MODEL")
# print(X)

# # -------------------------------------------------
# # Step 3: ML Prediction
# # -------------------------------------------------
# probability = model.predict_proba(X)[0][1] * 100
# probability = round(float(probability), 2)

# print("\n🤖 ML OUTPUT")
# print(f"Approval Probability: {probability}%")

# # -------------------------------------------------
# # Step 4: Final Bank Recommendation
# # -------------------------------------------------
# recommendation = {
#     "bank": "Bank of Maharashtra",
#     "approval_probability": probability,
#     "roi": rule_result["roi"],
#     "emi": rule_result["emi"],
#     "foir": rule_result["foir"],
#     "ltv": rule_result["ltv"]
# }

# print("\n🏦 FINAL BANK RECOMMENDATION")
# for k, v in recommendation.items():
#     print(f"{k}: {v}")






import requests

URL = "http://127.0.0.1:5000/recommend"


user_data = {
    "age": 30,
    "employment_type": "salaried",
    "monthly_income": 300000,
    "annual_income": 3600000,
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


response = requests.post(URL, json=user_data)

result = response.json()


print("\n")
print("=" * 60)
print(" AI FINTECH RISK MANAGER ")
print("=" * 60)


print("\nApplicant Financial Summary")

print("-" * 60)

print(f"Age               : {user_data['age']}")

print(f"Employment        : {user_data['employment_type']}")

print(f"Monthly Income    : ₹{user_data['monthly_income']:,}")

print(f"CIBIL Score       : {user_data['cibil']}")

print(f"Loan Amount       : ₹{user_data['loan_amount']:,}")

print(f"Existing EMI      : ₹{user_data['existing_emi']:,}")

print(f"Tenure            : {user_data['tenure_years']} years")


print("\nFinancial Analysis")

print("-" * 60)

metrics = result["financial_metrics"]

print(f"Interest Rate     : {metrics['roi']} %")

print(f"Monthly EMI       : ₹{metrics['emi']:,.2f}")

print(f"FOIR              : {metrics['foir']} %")

print(f"LTV               : {metrics['ltv']} %")

print(f"Loan/Income Ratio : {metrics['loan_to_income']}")


print("\nAI Risk Assessment")

print("-" * 60)

risk = result["risk_assessment"]

print(f"Approval Probability : {risk['approval_probability']} %")

print(f"Risk Score           : {risk['risk_score']}")

print(f"Risk Level           : {risk['risk_level']}")

print(f"Recommended Action   : {risk['recommended_action']}")


print("\nWhy this decision?")

print("-" * 60)

for reason in result["risk_factors"]:
    print("•", reason)


print("\nRecommended Banks")

print("-" * 60)

banks = result["bank_recommendations"]

recommended = None

for bank in banks:

    status = "ELIGIBLE" if bank["eligible"] else "NOT ELIGIBLE"

    print(f"\n{bank['bank']}")

    print(f"Match Score : {bank['match_score']}")

    print(f"Status      : {status}")

    print("Reasons:")

    for r in bank["reasons"]:
        print("   -", r)

    if bank["eligible"] and recommended is None:
        recommended = bank


print("\n")
print("=" * 60)

if recommended:

    print(" FINAL RECOMMENDED BANK ")

    print("=" * 60)

    print(f"\n🏆 {recommended['bank']}")

    print(f"Match Score : {recommended['match_score']}")

    print("\nThis bank is the highest eligible recommendation")

else:

    print("No eligible bank found.")

print("\n" + "=" * 60)