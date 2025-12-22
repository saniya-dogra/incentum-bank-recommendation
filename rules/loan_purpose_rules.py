def check_loan_purpose(loan_category, loan_amount, property_cost):
    if loan_category == "plot_only":
        return False, "Standalone plot loan not allowed"

    if loan_category == "renovation":
        if loan_amount > 0.25 * property_cost:
            return False, "Renovation loan exceeds 25% of property value"

    if loan_category == "plot_plus_construction":
        if loan_amount > 0.75 * property_cost:
            return False, "Plot funding exceeds permissible limit"

    return True, None
