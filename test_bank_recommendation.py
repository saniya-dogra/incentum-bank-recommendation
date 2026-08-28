import requests

URL = "http://127.0.0.1:5000/recommend"


def run_case(label, user_data):

    print("\n")
    print("=" * 60)
    print(f" AI FINTECH RISK MANAGER — {label} ")
    print("=" * 60)

    response = requests.post(URL, json=user_data)
    result = response.json()

    if result.get("status") == "Error":
        print("\nInput Error:", result["message"])
        return

    print(f"\nDecision: {result['decision']}")

    # ------------------------------------------------
    # REJECTED — hard eligibility rule failed
    # ------------------------------------------------
    if result["decision"] == "REJECTED":
        print("Rejection Reason:", result["rejection_reason"])
        return

    # ------------------------------------------------
    # Eligible — full risk + bank recommendation flow
    # ------------------------------------------------
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

    print("\n" + "=" * 60)

    if recommended:
        print(" FINAL RECOMMENDED BANK ")
        print("=" * 60)
        print(f"\n🏆 {recommended['bank']}")
        print(f"Match Score : {recommended['match_score']}")
        print("\nThis bank is the highest eligible recommendation")
    else:
        print("No eligible bank found.")

    print("\n" + "=" * 60)


# ==========================================================
# CASE 1 — Applicant who passes all eligibility rules
# ==========================================================

approved_applicant = {
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


# ==========================================================
# CASE 2 — Applicant who fails a hard eligibility rule
# (here: age exceeds retirement limit for salaried)
# ==========================================================

rejected_applicant = {
    "age": 63,
    "employment_type": "salaried",
    "monthly_income": 80000,
    "annual_income": 960000,
    "cibil": 700,
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

# ==========================================================
# CASE 3 — Riskier applicant who passes basic eligibility
# ==========================================================

high_risk_applicant = {
    "age": 35,
    "employment_type": "salaried",
    "monthly_income": 70000,
    "annual_income": 840000,
    "cibil": 660,
    "loan_amount": 2500000,
    "property_cost": 3500000,
    "agreement_value": 3500000,
    "realizable_value": 3500000,
    "property_age": 10,
    "city_type": "metro",
    "existing_emi": 15000,
    "tenure_years": 20,
    "loan_category": "purchase",
    "green_building": False,
    "is_third_property": False
}


if __name__ == "__main__":
    run_case("APPROVED CASE", approved_applicant)
    run_case("REJECTED CASE", rejected_applicant)
    run_case("MEDIUM RISK CASE", high_risk_applicant)