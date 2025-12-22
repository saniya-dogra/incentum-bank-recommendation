# validators.py

REQUIRED_FIELDS = [
    "age",
    "employment_type",
    "monthly_income",
    "annual_income",
    "cibil",
    "loan_amount",
    "property_cost",
    "agreement_value",
    "realizable_value",
    "property_age",
    "city_type",
    "existing_emi",
    "tenure_years",
    "loan_category"
]

def validate_input(data):

    # Required fields
    missing = [f for f in REQUIRED_FIELDS if f not in data]
    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"

    # Basic validations
    if data["monthly_income"] <= 0:
        return False, "Monthly income must be positive"

    if data["loan_amount"] <= 0:
        return False, "Loan amount must be positive"

    if data["cibil"] < 300 or data["cibil"] > 900:
        return False, "Invalid CIBIL score"

    if data["tenure_years"] <= 0 or data["tenure_years"] > 30:
        return False, "Invalid tenure"

    # Co-applicant validation (optional)
    if "co_applicants" in data:
        if not isinstance(data["co_applicants"], list):
            return False, "co_applicants must be a list"

        for person in data["co_applicants"]:
            required = ["relation", "age", "monthly_income", "employment_type"]
            for field in required:
                if field not in person:
                    return False, f"Missing co-applicant field: {field}"

                if person["monthly_income"] <= 0:
                    return False, "Invalid co-applicant income"

    return True, None
