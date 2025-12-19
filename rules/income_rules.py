def check_income(annual_income):
    if annual_income < 300000:
        return False, "Income below ₹3 lakh minimum"
    return True, None
