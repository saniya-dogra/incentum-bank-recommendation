# rules/age_rules.py

def check_age(age, employment_type):
    if age < 21:
        return False, "Applicant below minimum age"

    if employment_type == "salaried" and age > 60:
        return False, "Age exceeds retirement age"

    if employment_type in ["self_employed", "business"] and age > 65:
        return False, "Age exceeds allowed limit"

    if employment_type == "pensioner" and age > 70:
        return False, "Pensioner age limit exceeded"

    return True, "Age eligible"
