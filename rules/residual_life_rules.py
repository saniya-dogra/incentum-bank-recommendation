def check_residual_life(property_age, tenure_years, city_type):
    max_age = 40 if city_type == "metro" else 30
    residual_life = max_age - property_age

    if residual_life < tenure_years + 5:
        return False, "Property residual life insufficient for requested tenure"

    return True, None
