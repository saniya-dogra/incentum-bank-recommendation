def check_tenure(age, tenure_years):
    max_tenure = min(30, 75 - age)

    if tenure_years > max_tenure:
        return False, f"Tenure exceeds allowed limit of {max_tenure} years"

    return True, None
