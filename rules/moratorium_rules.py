def get_moratorium(loan_category):
    if loan_category == "under_construction":
        return "Up to project completion or 48 months"
    if loan_category == "plot":
        return "No moratorium"
    return "Up to 2 months"
