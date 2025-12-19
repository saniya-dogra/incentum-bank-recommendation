# validators.py

REQUIRED_FIELDS = [
    "age",
    "employment_type",
    "monthly_income",
    "annual_income",
    "cibil",
    "loan_amount",
    "property_cost",
    "property_age",
    "city_type",
    "existing_emi",
    "tenure_years",
    "loan_category"
]

def validate_input(data):
    missing = []

    for field in REQUIRED_FIELDS:
        if field not in data:
            missing.append(field)

    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"

    if data["monthly_income"] <= 0:
        return False, "Monthly income must be positive"

    if data["loan_amount"] <= 0:
        return False, "Loan amount must be positive"

    if data["cibil"] < 300 or data["cibil"] > 900:
        return False, "Invalid CIBIL score"

    return True, None
