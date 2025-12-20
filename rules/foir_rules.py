def allowed_foir(monthly_income):
    if monthly_income < 20000:
        return 0.50
    if monthly_income < 50000:
        return 0.60
    if monthly_income < 100000:
        return 0.65
    if monthly_income < 200000:
        return 0.70
    if monthly_income < 500000:
        return 0.75
    return 0.80
