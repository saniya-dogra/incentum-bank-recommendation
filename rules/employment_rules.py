def check_employment(employment_type, business_years=0, itr_years=0):
    if employment_type == "self_employed":
        if business_years < 2 or itr_years < 2:
            return False, "Minimum 2 years business & ITR required"
    return True, None
