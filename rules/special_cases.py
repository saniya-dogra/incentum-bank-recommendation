def pensioner_rules(monthly_pension, age):
    if age > 70:
        return False, "Pensioner age exceeds 70 years"
    if monthly_pension < 21000:
        return False, "Minimum pension ₹21,000 required"
    return True, None


def agriculturist_rules(annual_income, has_income_certificate):
    if not has_income_certificate:
        return False, "Income certificate required for agriculturist"
    if annual_income < 300000:
        return False, "Agriculturist income below ₹3 lakh"
    return True, None


def cre_penalty(is_third_property):
    return 1.00 if is_third_property else 0.0


def green_building_concession(is_green):
    return -0.10 if is_green else 0.0
