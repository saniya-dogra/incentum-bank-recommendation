def check_property(property_age, city_type, loan_category):
    if city_type == "metro" and property_age > 40:
        return False, "Property age exceeds metro limit"

    if city_type != "metro" and property_age > 30:
        return False, "Property age exceeds non-metro limit"

    if loan_category == "plot_only":
        return False, "Standalone plot loan not allowed"

    return True, None
