from rules.residual_life_rules import check_residual_life

def check_property(property_age, city_type, loan_category, tenure_years):
    if city_type == "metro" and property_age > 40:
        return False, "Property age exceeds metro limit"

    if city_type != "metro" and property_age > 30:
        return False, "Property age exceeds non-metro limit"

    if loan_category == "plot_only":
        return False, "Standalone plot loan not allowed"

    ok, msg = check_residual_life(property_age, tenure_years, city_type)
    if not ok:
        return False, msg

    return True, None
